#!/usr/bin/env bash
# Package the AI Build Partner kit into a zip for buyer download.
#
# Single canonical source (2026-05-23 — Plan A landed):
#   claude-skills/ai-build-partner/
#     SKILL.md, modules/, references/, templates/, exports/
#     kit-files/ (00-master-system-prompt + 01-brand-guide + 02-voice-dna + 03-audience-personas + 04-user-context-template + README)
#
# Output: unstuckwithmolly/public/portal/ai-build-partner-kit.zip
#
# To regenerate GPT knowledge-files from the same canonical source:
#   python3 scripts/sync-gpt-knowledge-files.py
#
# Idempotent. Re-run after any skill / MSP / template update.

set -euo pipefail

# Script lives in claude-skills/scripts/. Canonical source is one dir up.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_SKILLS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
CLAUDE_SKILLS="$CLAUDE_SKILLS_ROOT/ai-build-partner"
KIT_FILES="$CLAUDE_SKILLS/kit-files"

# In CI: unstuckwithmolly is checked out alongside; set UNSTUCK_PATH to its checkout dir.
# Locally: defaults to ~/github/unstuckwithmolly.
UNSTUCK_PATH="${UNSTUCK_PATH:-$HOME/github/unstuckwithmolly}"
OUTPUT_DIR="$UNSTUCK_PATH/public/portal"
OUTPUT_FILE="$OUTPUT_DIR/ai-build-partner-kit.zip"

# Sanity checks
if [ ! -d "$CLAUDE_SKILLS" ]; then
  echo "ERROR: $CLAUDE_SKILLS not found" >&2
  exit 1
fi
if [ ! -d "$KIT_FILES" ]; then
  echo "ERROR: $KIT_FILES not found (Plan A: kit-files now live in claude-skills)" >&2
  exit 1
fi
if [ ! -d "$OUTPUT_DIR" ]; then
  echo "ERROR: $OUTPUT_DIR not found — is unstuckwithmolly checked out?" >&2
  exit 1
fi

# Build in a temp dir so we can atomically replace the zip
STAGE=$(mktemp -d)
trap "rm -rf '$STAGE'" EXIT

KIT_DIR="$STAGE/ai-build-partner"
mkdir -p "$KIT_DIR"

# 1. Copy claude-skills canonical content
cp "$CLAUDE_SKILLS/SKILL.md" "$KIT_DIR/SKILL.md"
cp -r "$CLAUDE_SKILLS/modules" "$KIT_DIR/modules"
cp -r "$CLAUDE_SKILLS/references" "$KIT_DIR/references"
cp -r "$CLAUDE_SKILLS/templates" "$KIT_DIR/templates"
if [ -d "$CLAUDE_SKILLS/exports" ]; then
  cp -r "$CLAUDE_SKILLS/exports" "$KIT_DIR/exports"
fi

# 2. Copy kit-files (MSP + brand-guide + voice-dna + audience-personas + user-context-template)
mkdir -p "$KIT_DIR/kit-files"
for f in 00-master-system-prompt.md 01-brand-guide.md 02-voice-dna.md 03-audience-personas.md 04-user-context-template.md README.md; do
  src="$KIT_FILES/$f"
  if [ -f "$src" ]; then
    cp "$src" "$KIT_DIR/kit-files/$f"
  fi
done

# 3. Count what's in the package (for the build log)
MODULES_COUNT=$(find "$KIT_DIR/modules" -name "*.md" | wc -l | tr -d ' ')
TEMPLATES_COUNT=$(find "$KIT_DIR/templates" -name "*.md" | wc -l | tr -d ' ')
KIT_FILES_COUNT=$(find "$KIT_DIR/kit-files" -name "*.md" | wc -l | tr -d ' ')

echo "Packaging AI Build Partner kit..."
echo "  Modules:   $MODULES_COUNT (canonical: claude-skills/ai-build-partner/modules/)"
echo "  Templates: $TEMPLATES_COUNT"
echo "  Kit files: $KIT_FILES_COUNT (MSP + brand-guide + voice-dna + personas + user-context)"

# 4. Zip it
cd "$STAGE"
zip -qr "$OUTPUT_FILE.tmp" ai-build-partner

# 5. Atomically replace
mv "$OUTPUT_FILE.tmp" "$OUTPUT_FILE"

SIZE=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE")
echo ""
echo "✅ Kit packaged → $OUTPUT_FILE ($SIZE bytes)"
echo "   Download URL: unstuckwithmolly.com/portal/ai-build-partner-kit.zip"
echo ""
echo "Next: commit + push the updated zip in the unstuckwithmolly repo."
