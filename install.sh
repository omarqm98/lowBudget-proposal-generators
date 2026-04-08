#!/bin/bash
#
# lowBudget Proposal Generators — Installer
#
# Copies Claude Code skills to your project and installs dependencies.
#

set -e

echo ""
echo "============================================"
echo "  lowBudget Proposal Generators — Installer"
echo "============================================"
echo ""

# --- Determine target directory ---
TARGET_DIR=""

if [ -n "$1" ]; then
    TARGET_DIR="$1"
elif [ -d ".claude/skills" ]; then
    TARGET_DIR="$(pwd)"
else
    echo "Where is your project directory?"
    echo "(This is the folder where you use Claude Code)"
    echo ""
    read -p "Path: " TARGET_DIR
fi

# Expand ~ to home directory
TARGET_DIR="${TARGET_DIR/#\~/$HOME}"

if [ ! -d "$TARGET_DIR" ]; then
    echo "ERROR: Directory not found: $TARGET_DIR"
    exit 1
fi

SKILLS_DIR="$TARGET_DIR/.claude/skills"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing skills to: $SKILLS_DIR"
echo ""

# --- Copy skills ---
echo "[1/3] Copying skills..."

mkdir -p "$SKILLS_DIR/proposal-docs/templates"
mkdir -p "$SKILLS_DIR/proposal-docs/references"
mkdir -p "$SKILLS_DIR/excalidraw-diagrams/references"

cp "$SCRIPT_DIR/proposal-docs/SKILL.md" "$SKILLS_DIR/proposal-docs/"
cp "$SCRIPT_DIR/proposal-docs/proposal_docs.py" "$SKILLS_DIR/proposal-docs/"
cp "$SCRIPT_DIR/proposal-docs/templates/proposal_template.docx" "$SKILLS_DIR/proposal-docs/templates/"
cp "$SCRIPT_DIR/proposal-docs/references/"*.md "$SKILLS_DIR/proposal-docs/references/"

cp "$SCRIPT_DIR/excalidraw-diagrams/SKILL.md" "$SKILLS_DIR/excalidraw-diagrams/"
cp "$SCRIPT_DIR/excalidraw-diagrams/references/"*.md "$SKILLS_DIR/excalidraw-diagrams/references/"

echo "  Done."

# --- Install Python dependencies ---
echo ""
echo "[2/3] Installing Python dependencies..."
pip3 install docxtpl docxcompose htmldocx python-dotenv requests 2>&1 | tail -1
echo "  Done."

# --- Create .env if it doesn't exist ---
echo ""
echo "[3/3] Setting up environment..."

ENV_FILE="$TARGET_DIR/.env"
if [ ! -f "$ENV_FILE" ]; then
    echo "# Optional: Add your Stripe key to enable payment links" > "$ENV_FILE"
    echo "# STRIPE_SECRET_KEY=sk_test_your_key_here" >> "$ENV_FILE"
    echo "  Created .env file at $ENV_FILE"
    echo "  (Add your Stripe key there if you want payment links)"
else
    echo "  .env file already exists — skipping."
fi

# --- Done ---
echo ""
echo "============================================"
echo "  Installation complete!"
echo "============================================"
echo ""
echo "Next steps:"
echo "  1. Open Claude Code in your project: $TARGET_DIR"
echo "  2. Say: \"Help me build a proposal for my client.\""
echo "  3. Claude will ask for your name and company on first use."
echo ""
echo "Optional:"
echo "  - Customize the template at:"
echo "    $SKILLS_DIR/proposal-docs/templates/proposal_template.docx"
echo "  - Add your Stripe key to $ENV_FILE for payment links"
echo ""
