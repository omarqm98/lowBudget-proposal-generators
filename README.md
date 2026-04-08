# Low Budget Proposal Generators (PandaDocs Alternative)

Generate professional client proposals using Claude Code — for free. No expensive SaaS tools needed.

<div align="center">
  <a href="https://www.loom.com/share/4170dd3b6e704b6bba302e55b3282015">
    <img src="https://cdn.loom.com/sessions/thumbnails/4170dd3b6e704b6bba302e55b3282015-898097c0c43bc596.jpg" width="600" alt="Watch the video walkthrough" />
    <br/>
    <strong>Watch the full video walkthrough</strong>
  </a>
</div>

This repo contains two Claude Code skills that work together:

1. **proposal-docs** — Generates a styled Word proposal (.docx) from a client brief, with optional Stripe payment link
2. **excalidraw-diagrams** — Generates system architecture diagrams (.excalidraw) to include with your proposals

## What You Get

From a simple conversation with Claude, you get:
- A **professional Word proposal** with your branding, ready to send
- A **Stripe payment link** for the deposit (optional)
- A **system architecture diagram** you can share with the client

Total cost: **$0** (you just need a Claude Code subscription)

## Prerequisites

Before installing, make sure you have:

1. **Claude Code** installed ([download here](https://claude.ai/code))
2. **Python 3.8+** installed on your machine
3. A **Word proposal template** with Jinja2 tags (a starter template is included)

## Installation

### Option 1: Automatic (recommended)

```bash
git clone https://github.com/omarqm98/lowBudget-proposal-generators.git
cd lowBudget-proposal-generators
chmod +x install.sh
./install.sh
```

The install script will:
- Copy both skills to your Claude Code skills directory
- Install the required Python packages
- Create a `.env` file for your API keys (optional)

### Option 2: Manual

1. Copy the `proposal-docs/` folder to `.claude/skills/proposal-docs/` in your project
2. Copy the `excalidraw-diagrams/` folder to `.claude/skills/excalidraw-diagrams/` in your project
3. Install Python dependencies:
   ```bash
   pip3 install docxtpl docxcompose htmldocx python-dotenv requests
   ```

## Quick Start

Once installed, open Claude Code in your project and say:

```
Help me build a proposal for my client.
```

On your **first use**, Claude will ask for your name and company so it can personalize all future proposals.

Then just describe your client's project — Claude will:
1. Ask clarifying questions if anything is missing
2. Generate the proposal content
3. Show you a preview (dry run)
4. Generate the final Word document after your approval

## Setting Up Your Template

A starter template is included at `proposal-docs/templates/proposal_template.docx`. To customize it:

1. Open the template in Google Docs or Microsoft Word
2. Replace the company name and logo with yours
3. Keep the `{{ tags }}` exactly as they are — these get replaced with your proposal content
4. Save as `.docx` format

For a full video walkthrough, watch the [Loom walkthrough](https://www.loom.com/share/4170dd3b6e704b6bba302e55b3282015) at the top of this page.

## Optional: Stripe Payment Links

To automatically generate payment links with each proposal:

1. Create a Stripe account at [stripe.com](https://stripe.com)
2. Go to Developers > API Keys
3. Copy your Secret Key
4. Add it to your project's `.env` file:
   ```
   STRIPE_SECRET_KEY=sk_test_your_key_here
   ```

If you skip this step, proposals will still generate — you just won't get automatic payment links.

## Optional: Architecture Diagrams

After generating a proposal, Claude can also create a system architecture diagram. Just ask:

```
Now create an architecture diagram for this proposal.
```

The diagram is saved as an `.excalidraw` file. To view or edit it:
- **Online**: Drag the file into [excalidraw.com](https://excalidraw.com)
- **VS Code**: Install the Excalidraw extension and open the file

## Project Structure

```
lowBudget-proposal-generators/
├── README.md
├── install.sh                          # Automatic installer
├── examples/
│   └── sample_config.json              # Example proposal config
├── proposal-docs/                      # Proposal generator skill
│   ├── SKILL.md                        # Skill definition (Claude reads this)
│   ├── proposal_docs.py                # Python script that renders the DOCX
│   ├── templates/
│   │   └── proposal_template.docx      # Starter Word template
│   └── references/
│       ├── stripe_api_reference.md
│       └── carbone_reference.md
└── excalidraw-diagrams/                # Diagram generator skill
    ├── SKILL.md                        # Skill definition
    └── references/
        ├── excalidraw_schema_reference.md
        └── diagram_templates.md
```

## How It Works (Under the Hood)

1. You describe the project to Claude in plain English
2. Claude generates a structured JSON config following the proposal format
3. The Python script uses `docxtpl` to render a Word document from your template
4. Optionally, Stripe API creates a payment link for the deposit
5. Optionally, Claude generates an Excalidraw architecture diagram

No databases, no servers, no monthly fees. Everything runs locally on your machine.

## License

MIT — use it however you want.
