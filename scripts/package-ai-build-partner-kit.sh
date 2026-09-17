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

# WHERE THE ZIP ACTUALLY GOES
#
# theshipitsystem, not unstuckwithmolly. The kit is served from
# theshipitsystem.com/portal/ai-build-partner-kit.zip - that is the URL in
# src/data/unstuck-install.ts and in the Meta delivery email - and
# unstuckwithmolly.com 307s to it. unstuckwithmolly has not held the zip for
# some time, so every sync that "succeeded" against it was updating a file
# nobody downloads.
#
# SITE_PATH is the name; UNSTUCK_PATH is still read for callers that set it.
# Locally: defaults to ~/github/theshipitsystem.
SITE_PATH="${SITE_PATH:-${UNSTUCK_PATH:-$HOME/github/theshipitsystem}}"
UNSTUCK_PATH="$SITE_PATH"
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

# The folder name is what Claude shows; SKILL.md `name: unstuck` is the
# slash command every ad and install page tells people to type.
KIT_DIR="$STAGE/unstuck"
mkdir -p "$KIT_DIR"

# 1. Copy claude-skills canonical content
cp "$CLAUDE_SKILLS/SKILL.md" "$KIT_DIR/SKILL.md"
# modules/, minus _archived: those are superseded versions kept for history, and
# several still carry framing the live modules have moved off (the money-first
# launch flow, for one). Shipping them to a buyer offers them a worse copy of a
# module they already have. The zip built before this exclusion existed did not
# contain them either - `cp -r` started pulling them in when _archived/ was
# added, which nobody noticed because the sync had already stopped running.
cp -r "$CLAUDE_SKILLS/modules" "$KIT_DIR/modules"
rm -rf "$KIT_DIR/modules/_archived"
cp -r "$CLAUDE_SKILLS/references" "$KIT_DIR/references"
rm -rf "$KIT_DIR/references/_archived"
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
zip -qr "$OUTPUT_FILE.tmp" unstuck

# 5. Atomically replace
mv "$OUTPUT_FILE.tmp" "$OUTPUT_FILE"

SIZE=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE")
echo ""
echo "✅ Kit packaged → $OUTPUT_FILE ($SIZE bytes)"
# The site serves the kit at TWO paths, and both are linked from live pages.
# Writing one and not the other is how they drift.
SECOND_COPY="$SITE_PATH/public/portal/downloads/ai-build-partner-kit/ai-build-partner-kit.zip"
if [ -d "$(dirname "$SECOND_COPY")" ]; then
  cp "$OUTPUT_FILE" "$SECOND_COPY"
  echo "   also wrote: public/portal/downloads/ai-build-partner-kit/ai-build-partner-kit.zip"
fi

echo "   Download URL: theshipitsystem.com/portal/ai-build-partner-kit.zip"
echo ""
echo "Next: commit + push the updated zip in the theshipitsystem repo."
