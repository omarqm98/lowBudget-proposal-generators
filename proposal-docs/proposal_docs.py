#!/usr/bin/env python3
"""
Proposal Document Generator

Renders DOCX proposals from a styled template using docxtpl (Jinja2)
and creates Stripe payment links.

Usage:
    # Dry run (preview what would be created)
    python3 proposal_docs.py --config /tmp/proposal_config.json

    # Live run (render DOCX + create Stripe payment link)
    python3 proposal_docs.py --config /tmp/proposal_config.json --live

    # Only render document (skip Stripe)
    python3 proposal_docs.py --config /tmp/proposal_config.json --live --only doc

    # Only create Stripe payment link (skip document)
    python3 proposal_docs.py --config /tmp/proposal_config.json --live --only stripe
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: 'python-dotenv' package not installed. Run: pip3 install python-dotenv")
    sys.exit(1)

try:
    from docxtpl import DocxTemplate
except ImportError:
    print("ERROR: 'docxtpl' package not installed. Run: pip3 install docxtpl docxcompose")
    sys.exit(1)

try:
    from htmldocx import HtmlToDocx
except ImportError:
    print("ERROR: 'htmldocx' package not installed. Run: pip3 install htmldocx")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("ERROR: 'requests' package not installed. Run: pip3 install requests")
    sys.exit(1)


# --- Constants ---
TEMPLATE_DIR = Path(__file__).parent / "templates"
OUTPUT_BASE = Path(__file__).parent.parent.parent.parent / ".tmp" / "proposals"
REQUIRED_FIELDS = ["proposalName", "companyName", "client", "sender", "project", "lineItems", "pricing"]


def get_proposal_dir(config):
    """Get the output directory for a proposal: .tmp/proposals/firstName-companyName/"""
    first_name = config["client"]["firstName"].lower().strip()
    company = re.sub(r"[^a-zA-Z0-9]+", "-", config["companyName"]).strip("-").lower()
    slug = f"{first_name}-{company}"
    proposal_dir = OUTPUT_BASE / slug
    proposal_dir.mkdir(parents=True, exist_ok=True)
    return proposal_dir, slug


def load_env():
    """Load environment variables from .env file."""
    env_paths = [
        Path.cwd() / ".env",
        Path(__file__).parent.parent.parent.parent / ".env",  # workspace root
    ]
    for env_path in env_paths:
        if env_path.exists():
            load_dotenv(env_path)
            return
    load_dotenv()


def get_stripe_key():
    """Get Stripe secret key from environment. Returns None if not configured."""
    key = os.getenv("STRIPE_SECRET_KEY")
    if not key:
        return None
    return key


def validate_config(config):
    """Validate that the config has all required fields."""
    missing = [f for f in REQUIRED_FIELDS if f not in config]
    if missing:
        print(f"ERROR: Config is missing required fields: {', '.join(missing)}")
        sys.exit(1)

    client = config.get("client", {})
    for field in ["firstName", "lastName", "companyName", "problem", "problemDescription", "solution", "solutionDescription"]:
        if field not in client:
            print(f"ERROR: Config client is missing required field: {field}")
            sys.exit(1)

    pricing = config.get("pricing", {})
    for field in ["total", "depositPercent", "depositAmount", "dueAtSigning"]:
        if field not in pricing:
            print(f"ERROR: Config pricing is missing required field: {field}")
            sys.exit(1)


def format_currency(amount):
    """Format a number as USD currency string."""
    return f"${amount:,.2f}"


def html_to_subdoc(tpl, html_content):
    """Convert HTML string to a docxtpl subdocument with proper Word formatting.

    Applies 1.25 line spacing to all paragraphs to match the template styling.
    """
    from docx.shared import Pt
    from docx.oxml.ns import qn

    parser = HtmlToDocx()
    temp_doc = parser.parse_html_string(html_content)

    # Apply 1.25 line spacing (300 twips = 240 * 1.25) to all paragraphs
    for para in temp_doc.paragraphs:
        pPr = para._p.get_or_add_pPr()
        spacing = pPr.find(qn('w:spacing'))
        if spacing is None:
            spacing = para._p.makeelement(qn('w:spacing'), {})
            pPr.append(spacing)
        spacing.set(qn('w:line'), '300')
        spacing.set(qn('w:lineRule'), 'auto')

    temp_path = OUTPUT_BASE / "_temp_subdoc.docx"
    temp_path.parent.mkdir(parents=True, exist_ok=True)
    temp_doc.save(str(temp_path))
    subdoc = tpl.new_subdoc(str(temp_path))
    temp_path.unlink()
    return subdoc


def build_template_context(config, tpl):
    """Build the Jinja2 context dict from the config.

    Converts HTML body sections into subdocuments for proper Word formatting.
    Plain text fields are left as-is for simple {{ tag }} replacement.
    """
    pricing = config["pricing"]
    client = config["client"]

    # Format line items with currency strings
    line_items = []
    for item in config.get("lineItems", []):
        line_items.append({
            **item,
            "price_fmt": format_currency(item["price"]),
            "subtotal_fmt": format_currency(item["subtotal"]),
        })

    # Format external costs
    external_costs = []
    for cost in config.get("externalCosts", []):
        external_costs.append({
            **cost,
            "subtotal_fmt": format_currency(cost["subtotal"]),
        })

    # Convert HTML body sections to subdocuments
    # These are the sections with rich formatting (bold, lists, paragraphs)
    problem_subdoc = html_to_subdoc(tpl, client["problemDescription"])
    solution_subdoc = html_to_subdoc(tpl, client["solutionDescription"])
    sow_subdoc = html_to_subdoc(tpl, config["project"]["sowDescription"])

    # Technical specification subdocuments (optional section)
    technical = config.get("technical", {})
    tech_context = {}
    if technical:
        if technical.get("whatWeAreBuilding"):
            tech_context["whatWeAreBuilding"] = html_to_subdoc(tpl, technical["whatWeAreBuilding"])
        if technical.get("howItWorks"):
            tech_context["howItWorks"] = html_to_subdoc(tpl, technical["howItWorks"])
        if technical.get("reliability"):
            tech_context["reliability"] = html_to_subdoc(tpl, technical["reliability"])
        if technical.get("techStack"):
            tech_context["techStack"] = technical["techStack"]

    return {
        "proposalName": config["proposalName"],
        "companyName": config["companyName"],
        "client": {
            **client,
            # Override the text fields with subdocuments for {{p }} tags
            "problemDescription": problem_subdoc,
            "solutionDescription": solution_subdoc,
        },
        "sender": config["sender"],
        "project": {
            **config["project"],
            "sowDescription": sow_subdoc,
        },
        "timeline": config.get("timeline", []),
        "lineItems": line_items,
        "pricing": {
            **pricing,
            "total_fmt": format_currency(pricing["total"]),
            "depositAmount_fmt": format_currency(pricing["depositAmount"]),
            "dueAtSigning_fmt": format_currency(pricing["dueAtSigning"]),
        },
        "externalCosts": external_costs,
        "technical": tech_context,
    }


# --- Document Generation (docxtpl) ---

def render_document(config, template_path, output_path):
    """Render a DOCX document from template with data using docxtpl."""
    if not template_path.exists():
        print(f"ERROR: Template file not found: {template_path}")
        print(f"  Save your proposal template as: {template_path}")
        sys.exit(1)

    print(f"  Loading template: {template_path.name}...")
    tpl = DocxTemplate(str(template_path))

    context = build_template_context(config, tpl)
    print(f"  Rendering document...")
    tpl.render(context)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    tpl.save(str(output_path))
    print(f"  Saved to: {output_path}")
    return output_path


# --- Stripe API ---

def stripe_request(method, endpoint, api_key, data=None):
    """Make an authenticated request to the Stripe API."""
    url = f"https://api.stripe.com/v1{endpoint}"
    headers = {"Authorization": f"Bearer {api_key}"}

    resp = requests.request(method, url, headers=headers, data=data, timeout=60)
    if resp.status_code >= 400:
        print(f"ERROR: Stripe {method} {endpoint} returned {resp.status_code}")
        try:
            print(json.dumps(resp.json(), indent=2))
        except Exception:
            print(resp.text[:500])
        sys.exit(1)
    return resp.json()


def create_stripe_payment_link(api_key, product_name, amount_cents, currency="usd"):
    """Create a Stripe payment link: Product -> Price -> PaymentLink."""
    print(f"  Creating Stripe product: {product_name}...")
    product = stripe_request("POST", "/products", api_key, data={
        "name": product_name,
    })
    product_id = product["id"]
    print(f"  Product created. ID: {product_id}")

    print(f"  Creating price: ${amount_cents / 100:.2f} {currency.upper()}...")
    price = stripe_request("POST", "/prices", api_key, data={
        "product": product_id,
        "unit_amount": amount_cents,
        "currency": currency,
    })
    price_id = price["id"]
    print(f"  Price created. ID: {price_id}")

    print(f"  Creating payment link...")
    payment_link = stripe_request("POST", "/payment_links", api_key, data={
        "line_items[0][price]": price_id,
        "line_items[0][quantity]": 1,
    })
    link_url = payment_link["url"]
    print(f"  Payment link created: {link_url}")
    return {
        "product_id": product_id,
        "price_id": price_id,
        "payment_link_id": payment_link["id"],
        "url": link_url,
    }


# --- Commands ---

def dry_run(config):
    """Preview the proposal that would be generated."""
    print(f"\n{'='*60}")
    print("DRY RUN — Proposal Preview")
    print(f"{'='*60}\n")

    print(f"Proposal: {config['proposalName']}")
    print(f"Client: {config['client']['firstName']} {config['client']['lastName']} | {config['client']['companyName']}")
    sender = config.get("sender", {})
    print(f"Sender: {sender.get('firstName', 'N/A')} {sender.get('lastName', 'N/A')} | {sender.get('companyName', 'N/A')}")
    print()

    print(f"Problem headline: {config['client']['problem']}")
    desc = config['client']['problemDescription']
    print(f"Problem body: {desc[:150]}{'...' if len(desc) > 150 else ''}")
    print()
    print(f"Solution headline: {config['client']['solution']}")
    desc = config['client']['solutionDescription']
    print(f"Solution body: {desc[:150]}{'...' if len(desc) > 150 else ''}")
    print()

    sow = config.get("project", {}).get("sowDescription", "")
    print(f"Scope of Work: {sow[:150]}{'...' if len(sow) > 150 else ''}")
    print()

    timeline = config.get("timeline", [])
    if timeline:
        print("Timeline:")
        for phase in timeline:
            print(f"  Phase {phase['phase']}: {phase['task']} ({phase['duration']} days)")
        total_dur = config.get("project", {}).get("totalDuration", "")
        if total_dur:
            print(f"  Total: {total_dur}")
        print()

    print("Pricing:")
    for item in config.get("lineItems", []):
        print(f"  {item['name']}: ${item.get('price', item.get('amount', 0)):,.2f} x {item.get('qty', 1)}")
    pricing = config["pricing"]
    print(f"  Total: ${pricing['total']:,.2f}")
    print(f"  Deposit ({pricing['depositPercent']}%): ${pricing['depositAmount']:,.2f}")
    print(f"  Due at signing: ${pricing['dueAtSigning']:,.2f}")
    print()

    ext_costs = config.get("externalCosts", [])
    if ext_costs:
        print("External Platform Costs:")
        for cost in ext_costs:
            print(f"  {cost['service']} ({cost['platform']}): ${cost['subtotal']:,.2f}/{cost.get('frequency', 'Monthly')}")
        print()

    stripe_cfg = config.get("stripe", {})
    if stripe_cfg:
        print(f"Stripe payment link:")
        print(f"  Product: {stripe_cfg.get('productName', config['proposalName'])}")
        print(f"  Amount: ${stripe_cfg.get('amountCents', pricing['depositAmount'] * 100) / 100:,.2f}")
        print(f"  Currency: {stripe_cfg.get('currency', 'usd').upper()}")
        print()

    template_path = TEMPLATE_DIR / "proposal_template.docx"
    if template_path.exists():
        print(f"Template: {template_path} (found)")
    else:
        print(f"Template: {template_path} (NOT FOUND)")
    print()

    print(f"{'='*60}")
    print("This is a DRY RUN. No documents were generated.")
    print("Run with --live to render the DOCX and create the Stripe link.")
    print(f"{'='*60}")


def run_live(config, only=None):
    """Render the proposal DOCX and/or create Stripe payment link."""
    load_env()
    proposal_dir, slug = get_proposal_dir(config)

    results = {
        "mode": "live",
        "proposal_name": config["proposalName"],
        "client": f"{config['client']['firstName']} {config['client']['lastName']}",
        "company": config["companyName"],
        "folder": str(proposal_dir),
        "created_at": datetime.now().strftime("%Y%m%d_%H%M%S"),
    }

    # --- Document ---
    if only is None or only == "doc":
        template_path = TEMPLATE_DIR / "proposal_template.docx"

        print(f"\n{'='*60}")
        print("GENERATING PROPOSAL (DOCX)")
        print(f"{'='*60}\n")

        output_path = proposal_dir / f"{slug}-proposal.docx"
        render_document(config, template_path, output_path)
        results["doc_path"] = str(output_path)

    # --- Stripe Payment Link (optional) ---
    if only is None or only == "stripe":
        stripe_key = get_stripe_key()
        if stripe_key:
            stripe_cfg = config.get("stripe", {})
            pricing = config["pricing"]

            product_name = stripe_cfg.get("productName", f"{config['proposalName']} — {config['companyName']}")
            amount_cents = stripe_cfg.get("amountCents", int(pricing["depositAmount"] * 100))
            currency = stripe_cfg.get("currency", "usd")

            print(f"\n{'='*60}")
            print("CREATING STRIPE PAYMENT LINK")
            print(f"{'='*60}\n")

            stripe_result = create_stripe_payment_link(stripe_key, product_name, amount_cents, currency)
            results["stripe"] = stripe_result
        else:
            print(f"\n{'='*60}")
            print("STRIPE SKIPPED — No STRIPE_SECRET_KEY found in .env")
            print("To enable payment links, add STRIPE_SECRET_KEY to your .env file.")
            print(f"{'='*60}")

    # Save results
    results_file = proposal_dir / f"{slug}-results.json"
    results_file.write_text(json.dumps(results, indent=2))

    # Summary
    print(f"\n{'='*60}")
    print("PROPOSAL GENERATED SUCCESSFULLY")
    print(f"{'='*60}\n")
    print(f"  Folder: {proposal_dir}")
    if "doc_path" in results:
        print(f"  Document: {results['doc_path']}")
    if "stripe" in results:
        print(f"  Stripe payment link: {results['stripe']['url']}")
    print(f"  Results: {results_file}")
    print(f"\n{'='*60}")

    return results


def main():
    parser = argparse.ArgumentParser(description="Proposal Document Generator")
    parser.add_argument("--config", help="Path to proposal config JSON file")
    parser.add_argument("--live", action="store_true", help="Execute live (default is dry run)")
    parser.add_argument("--only", choices=["doc", "stripe"], help="Only run one part (doc or stripe)")
    args = parser.parse_args()

    load_env()

    if not args.config:
        print("ERROR: --config is required.")
        print()
        print("Usage:")
        print("  python3 proposal_docs.py --config /tmp/proposal_config.json          # dry run")
        print("  python3 proposal_docs.py --config /tmp/proposal_config.json --live    # live run")
        sys.exit(1)

    config_path = Path(args.config)
    if not config_path.exists():
        print(f"ERROR: Config file not found: {config_path}")
        sys.exit(1)

    config = json.loads(config_path.read_text())
    validate_config(config)

    if args.live:
        run_live(config, only=args.only)
    else:
        dry_run(config)


if __name__ == "__main__":
    main()
