---
name: proposal-docs
description: Generate complete client proposals — renders a DOCX from a styled Word template using docxtpl, creates a Stripe payment link, and generates an Excalidraw architecture diagram. Use when creating client proposals, sales documents, or project quotes.
allowed-tools: Read, Grep, Glob, Bash, Write
argument-hint: [client brief or scope of work]
---

# Proposal Document Generator

## Goal

Analyze a client brief and generate a complete proposal package:
1. A **DOCX proposal** rendered from a styled Word template using `docxtpl` (Jinja2)
2. A **Stripe payment link** for the deposit amount (optional — requires Stripe API key)
3. An **Excalidraw architecture diagram** of the proposed system

## Tech Stack

| Component | Tool | Cost |
|-----------|------|------|
| Template engine | `docxtpl` (Python, Jinja2) | Free, runs locally |
| Template format | Word `.docx` with `{{ tags }}` | Free |
| HTML body content | `htmldocx` (Python) | Free, runs locally |
| Payment links | Stripe API | Free (Stripe takes % on payments) |
| Architecture diagrams | Excalidraw (via `excalidraw-diagrams` skill) | Free |
| Output | `.docx` → upload to Google Drive | Free |

## Input

The user provides a client brief — either as free-form text or structured description — containing some or all of:
- Client name and company
- The problem the client faces
- The proposed solution
- Scope of work / deliverables
- Timeline (phases and duration)
- Pricing (line items, quantities)
- Payment terms (deposit percentage)
- External platform costs (SaaS subscriptions the client will pay)

If any required information is missing from the brief, **ask the user before generating**.

## Process

### Phase 0: First-Run Onboarding
On the **very first use**, check if the user has previously provided their sender information. If not, ask:
1. "What is your first name and last name?" (the person sending the proposal)
2. "What is your company name?"

Store these as the default sender for all future proposals. The user can always override per-proposal.

### Phase 1: Understand the Brief
- Read the brief carefully
- Identify missing information and ask the user
- Clarify scope, pricing, and timeline if ambiguous

### Phase 2: Generate Proposal Content
Generate all content following the **Writing Style** rules below. Structure the output as a config JSON matching the **Config JSON Format** section.

**Important:** The `problemDescription`, `solutionDescription`, `sowDescription`, and all `technical.*` text fields must be **HTML** — not plain text. This is how the document gets proper formatting (bold headings, numbered lists, bullet points).

### Phase 3: Write Config JSON
Write the config to `/tmp/proposal_config.json`:
```bash
cat > /tmp/proposal_config.json << 'CONFIGEOF'
{...the generated config...}
CONFIGEOF
```

### Phase 4: Dry Run
Run the script in preview mode so the user can review:
```bash
python3 .claude/skills/proposal-docs/proposal_docs.py --config /tmp/proposal_config.json
```

### Phase 5: Live Run
After user confirms, render the DOCX (and optionally create a Stripe payment link if configured):
```bash
# Full run (DOCX + Stripe)
python3 .claude/skills/proposal-docs/proposal_docs.py --config /tmp/proposal_config.json --live

# Or separately:
python3 .claude/skills/proposal-docs/proposal_docs.py --config /tmp/proposal_config.json --live --only doc
python3 .claude/skills/proposal-docs/proposal_docs.py --config /tmp/proposal_config.json --live --only stripe
```

Output filename follows the convention: `firstName-companyName-proposal.docx`

### Phase 6: Architecture Diagram
Invoke the `excalidraw-diagrams` skill to generate a system architecture diagram based on the solution and technical breakdown described in the proposal.

**Important:** Save the diagram in the same client folder as the proposal. The output path must be:
```
.tmp/proposals/{firstName}-{companyName}/{firstName}-{companyName}-architecture.excalidraw
```
This keeps all deliverables for one client in a single folder.

## Writing Style

Follow these rules strictly when generating content.

**Voice and tone:**
- Write in first person ("I spent some time...", "My proposed solution...", "We'll build...")
- Confident but not pushy — "I consider this reasonably straightforward and am confident I can do an outstanding job"
- Focus on business impact, not technical jargon
- Mirror the client's language and industry terminology

**Problem section (`client.problem` + `client.problemDescription`):**
- `client.problem` is a lowercase plain text headline: format as "[noun phrase] is [costing/forcing/preventing] your team [consequence]"
- `client.problemDescription` is **HTML** — an ordered list with bold titles and paragraph explanations:
```html
<ol>
<li><b>Problem title here</b><br/>
2-3 sentence explanation focused on business impact.</li>

<li><b>Second problem title</b><br/>
2-3 sentence explanation.</li>
</ol>
```
- 3-5 problems, each distinct with no overlap

**Solution section (`client.solution` + `client.solutionDescription`):**
- `client.solution` is a lowercase plain text headline: "automated [X] powered by [Y]"
- `client.solutionDescription` is **HTML** — same format as problem, with matching number of points:
```html
<ol>
<li><b>Solution title here</b><br/>
2-3 sentence explanation.</li>

<li><b>Second solution title</b><br/>
2-3 sentence explanation.</li>
</ol>
```

**Scope section (`project.sowDescription`):**
- `project.sowDescription` is **HTML** — a paragraph followed by an unordered list:
```html
<p>[Your Company] will create an automated system that fulfils the following:</p>
<ul>
<li>Two (2) automated data pipelines that scrape real estate listings</li>
<li>One (1) structured cloud database with tables for active listings</li>
<li>Detailed video documentation + written for the client's team</li>
</ul>
```
- Each bullet is a specific, concrete deliverable
- Include quantities and specifics where possible (e.g., "one (1) custom template", "two (2) automated pipelines")

**Technical Breakdown (`technical` object):**
This section is optional — include it when the project has meaningful technical complexity. It has 4 sub-sections:

- `technical.whatWeAreBuilding` is **HTML** — a short 1-2 sentence summary of the system:
```html
<p>A fully automated market intelligence system that collects, processes, and visualizes
real estate listing data — giving your commercial team instant access to pricing,
inventory, and market trends across Lima's districts.</p>
```

- `technical.howItWorks` is **HTML** — numbered explanation of each system layer with details:
```html
<ol>
<li><b>Data Collection (Automated Scrapers)</b><br/>
Two custom scrapers run automatically on a set schedule, collecting listings from:
<ul><li>AdondeVivir — Peru's largest real estate portal</li>
<li>Urbania — Peru's second-largest portal</li></ul></li>

<li><b>Data Processing (Automated Pipeline)</b><br/>
After each scrape, the data flows through an automated pipeline that:
<ul><li>Cleans and standardizes all entries</li>
<li>Converts prices from Soles to USD</li>
<li>Removes duplicate listings</li></ul></li>
</ol>
```

- `technical.techStack` is an **array** for the Technology Stack table (Component | Tool | Purpose)

- `technical.reliability` is **HTML** — bullet list of monitoring, alerts, and resilience features:
```html
<ul>
<li>Automated health checks run daily — alerts sent if a scrape fails</li>
<li>Price history tracked over time for trend analysis</li>
<li>Each run is logged with statistics: total processed, new found, errors</li>
</ul>
```

**Timeline section (`timeline` array):**
- Each phase has: phase number, task description, duration (business days), start day, end day
- Phases should be sequential and realistic
- `project.totalDuration` is the sum in business days

**Pricing rules:**
- Default deposit is 50% unless the brief specifies otherwise
- Round all amounts to the nearest dollar (no cents unless the brief specifies them)
- Each line item has: name, price, qty, subtotal
- If the brief mentions recurring/external tool costs (API fees, SaaS subscriptions), list them in the `externalCosts` array
- If no pricing is provided in the brief, ask the user before generating

**Sender defaults:**
- Use the sender information collected during **Phase 0: First-Run Onboarding**
- If no onboarding has been completed, ask the user before generating

## Config JSON Format

```json
{
  "proposalName": "Project Name for Client Company",
  "companyName": "Client Company",
  "client": {
    "firstName": "John",
    "lastName": "Smith",
    "companyName": "Client Company Inc.",
    "problem": "lowercase problem headline",
    "problemDescription": "<ol><li><b>Problem Title</b><br/>Explanation paragraph...</li><li><b>Problem Title</b><br/>Explanation paragraph...</li></ol>",
    "solution": "lowercase solution headline",
    "solutionDescription": "<ol><li><b>Solution Title</b><br/>Explanation paragraph...</li><li><b>Solution Title</b><br/>Explanation paragraph...</li></ol>"
  },
  "sender": {
    "firstName": "Your First Name",
    "lastName": "Your Last Name",
    "companyName": "Your Company"
  },
  "project": {
    "sowDescription": "<p>[Your Company] will create an automated system that fulfils the following:</p><ul><li>Deliverable one</li><li>Deliverable two</li></ul>",
    "investment": "Your investment",
    "externalPlatformCosts": "Tech Stack Costs",
    "totalDuration": "12 Business Days"
  },
  "timeline": [
    {"phase": "1", "task": "Phase description", "duration": "3", "startDay": "Day 1", "endDay": "Day 3"},
    {"phase": "2", "task": "Phase description", "duration": "4", "startDay": "Day 4", "endDay": "Day 7"}
  ],
  "lineItems": [
    {"name": "Service name", "price": 3000, "qty": 1, "subtotal": 3000},
    {"name": "Add-on service", "price": 500, "qty": 1, "subtotal": 500}
  ],
  "pricing": {
    "total": 3500,
    "depositPercent": 50,
    "depositAmount": 1750,
    "dueAtSigning": 1750
  },
  "externalCosts": [
    {"service": "Automation Engine", "platform": "n8n", "frequency": "Monthly", "subtotal": 35},
    {"service": "AI Processing", "platform": "OpenAI (API)", "frequency": "Usage-based", "subtotal": 50}
  ],
  "technical": {
    "whatWeAreBuilding": "<p>A fully automated system that collects, processes, and delivers...</p>",
    "howItWorks": "<ol><li><b>Data Collection</b><br/>Description of the first layer...</li><li><b>Data Processing</b><br/>Description of the second layer...</li></ol>",
    "techStack": [
      {"component": "Automation", "tool": "n8n (workflow engine)", "purpose": "Orchestrates the pipeline"},
      {"component": "AI Processing", "tool": "OpenAI (API)", "purpose": "Handles classification and extraction"}
    ],
    "reliability": "<ul><li>Automated health checks run daily</li><li>Error alerts sent via email/Slack</li></ul>"
  },
  "stripe": {
    "productName": "Project Name — Client Company",
    "amountCents": 175000,
    "currency": "usd"
  }
}
```

**Notes on the config:**
- `stripe.amountCents` = `pricing.depositAmount` × 100 (Stripe uses cents)
- `externalCosts` is optional — omit if there are no third-party platform costs
- `technical` is optional — omit for simple projects without technical complexity
- `lineItems[].subtotal` = `price` × `qty`
- `pricing.dueAtSigning` = `pricing.depositAmount` (same value, shown as the amount due)

## Template Tags Reference

The Word template (`.claude/skills/proposal-docs/templates/proposal_template.docx`) uses these Jinja2 tags:

**Plain text tags** (`{{ tag }}`):
- `{{ proposalName }}`, `{{ companyName }}`
- `{{ client.firstName }}`, `{{ client.lastName }}`, `{{ client.companyName }}`
- `{{ client.problem }}`, `{{ client.solution }}`
- `{{ sender.firstName }}`, `{{ sender.lastName }}`, `{{ sender.companyName }}`
- `{{ project.investment }}`, `{{ project.externalPlatformCosts }}`
- `{{ pricing.total_fmt }}`, `{{ pricing.depositAmount_fmt }}`, `{{ pricing.dueAtSigning_fmt }}`

**HTML subdoc tags** (`{{p tag }}`) — these render formatted HTML content:
- `{{p client.problemDescription }}`
- `{{p client.solutionDescription }}`
- `{{p project.sowDescription }}`
- `{{p technical.whatWeAreBuilding }}`
- `{{p technical.howItWorks }}`
- `{{p technical.reliability }}`

**Table loop tags** — these repeat table rows for each item in the array:
- Timeline: `{%tr for t in timeline %}` ... `{{ t.phase }}`, `{{ t.task }}`, `{{ t.duration }}`, `{{ t.startDay }}`, `{{ t.endDay }}` ... `{%tr endfor %}`
- Pricing: `{%tr for item in lineItems %}` ... `{{ item.name }}`, `{{ item.price_fmt }}`, `{{ item.qty }}`, `{{ item.subtotal_fmt }}` ... `{%tr endfor %}`
- External costs: `{%tr for cost in externalCosts %}` ... `{{ cost.service }}`, `{{ cost.platform }}`, `{{ cost.frequency }}`, `{{ cost.subtotal_fmt }}` ... `{%tr endfor %}`
- Tech stack: `{%tr for s in technical.techStack %}` ... `{{ s.component }}`, `{{ s.tool }}`, `{{ s.purpose }}` ... `{%tr endfor %}`

## First-Run Setup

If the script fails on first run, guide the user through setup:

1. **Install dependencies:**
   ```bash
   pip3 install docxtpl docxcompose htmldocx python-dotenv requests stripe
   ```

2. **Add Stripe key to `.env` (optional — only needed for payment links):**
   ```
   STRIPE_SECRET_KEY=sk_test_...
   ```
   If no Stripe key is configured, the script will generate the DOCX and skip the payment link.

3. **Template** is already set up at `.claude/skills/proposal-docs/templates/proposal_template.docx`. If redesigning:
   - Design in Google Docs with `{{ tags }}` typed in one go (don't edit parts of tags)
   - Download as `.docx` (File > Download > Microsoft Word)
   - Use **Arial** font for cross-platform compatibility
   - Save to `.claude/skills/proposal-docs/templates/proposal_template.docx`

## Hard Rules

- **Ask before assuming** — if the brief is missing client name, pricing, or key details, ask rather than guess
- **Do NOT add URLs or links** in any generated content
- **Always run dry mode first** — never go straight to --live without user review
- **Stripe amount = deposit amount** — the payment link is for the deposit, not the full total
- **Sequential phases** — timeline phases must follow logically, no overlapping days
- **HTML for body sections** — problemDescription, solutionDescription, sowDescription, and technical.* text fields must always be HTML, never plain text
- **Output format** — always DOCX (user uploads to Google Drive for editing and e-signatures)
