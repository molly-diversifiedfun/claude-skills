---
name: ship-it-brand-pdf
description: Generate branded PDFs for the Ship It System and Unstuck with Molly product lines. Use this skill whenever the user asks to create, rebuild, or generate any PDF product — workbooks, guides, lead magnets, playbooks, or any downloadable asset. Also use when the user mentions brand-consistent PDFs, the Ship It System design, or references existing products like "Decide Already," "One-Page Launch Plan," "Ship It Kit," or "90 Days to Ship or Kill." Trigger even for generic PDF requests within this project since all PDFs must match the brand design system.
---

# Ship It System — Brand PDF Generator

## Overview

This skill generates production-quality branded PDFs that match the established Ship or Kill design system. Every PDF uses Cormorant Garamond (serif headings) + Outfit (sans body) typography with the brand color palette: burgundy, cream, charcoal, gold, champagne.

## Quick Start

```python
import sys
sys.path.insert(0, '/path/to/ship-it-brand-pdf/scripts')
from brand_pdf import *
from reportlab.platypus import Spacer, PageBreak

OUTPUT = "/path/to/my_product.pdf"

# BrandDoc handles all page templates automatically
doc = BrandDoc(OUTPUT, "PRODUCT NAME")

S = get_styles()
story = []

# Cover page (dark bg, gold corner accent)
cover_page(story,
    title="Your Title Here.",
    subtitle="A Ship It System Workbook",
    description="One-line description of what this product does.",
)

# Title page (cream bg, centered)
title_page(story, S,
    title="Your Title Here.",
    byline="By Molly Shelestak",
    dedication="Who this is for and why it matters.",
    bold_statement="Infrastructure, not aspiration.",
    copyright_text="© 2026 Molly Shelestak | theshipitsystem.com"
)

# Content pages (cream bg, champagne line at top)
story.append(Paragraph("Your heading", S['h2']))
story.append(Paragraph("Your body text.", S['body']))

# Section dividers (cream bg, champagne line at 35% — auto-detected)
section_divider(story, 1, "Section Title", "Subtitle goes here")

# Build — page backgrounds switch automatically
doc.build(story)
```

## Design System Reference

### Page Types

The module provides four page types via the `BrandPageHandler`:

| Page Type | Background | When Used |
|-----------|-----------|-----------|
| **Cover** | Dark charcoal (#1a1614) with gold L-corner accent | First page only |
| **Title** | Cream (#f9f6f0), centered content | Page 2 (dedication/copyright) |
| **Content** | Cream bg, thin champagne line at top, footer | All body pages |
| **Section Divider** | Cream bg, centered burgundy number + title | Before each major section |

### Colors (all pre-defined as constants)

| Constant | Hex | Usage |
|----------|-----|-------|
| `BURGUNDY` | #763c47 | Primary accent, section numbers, CTAs |
| `CREAM` | #f9f6f0 | Page backgrounds |
| `CHARCOAL` | #251f1c | Body text, headings |
| `GOLD` | #b8922e | Cover accent, decorative rules |
| `CHAMPAGNE` | #e5dbc8 | Borders, subtle lines |
| `SAND` | #f3efe6 | Table header backgrounds |
| `DARK_BG` | #1a1614 | Cover page background |
| `MUTED_FG` | #5c4f46 | Secondary/caption text |

### Typography

| Role | Font | Style Key |
|------|------|-----------|
| H1 heading | Cormorant Garamond 36pt | `S['h1']` |
| H2 heading | Cormorant Garamond 28pt | `S['h2']` |
| H3 heading | Cormorant Garamond 20pt | `S['h3']` |
| Serif italic emphasis | Cormorant Garamond Italic 20pt | `S['serif_italic']` |
| Body text | Outfit Light 11pt | `S['body']` |
| Body bold | Outfit SemiBold 11pt | `S['body_bold']` |
| Small/caption | Outfit Light 9pt | `S['small']` |
| Burgundy label | Outfit SemiBold 12pt burgundy | `S['burgundy_bold']` |
| Table header | Outfit SemiBold 9pt burgundy | `S['table_header']` |
| Table cell | Outfit Light 9.5pt | `S['table_cell']` |
| Quote | Cormorant Garamond Italic 14pt | `S['quote']` |
| Quote attribution | Outfit Light 10pt muted | `S['quote_attr']` |

Centered variants: Append `_center` to any style name (e.g., `S['h2_center']`, `S['body_center']`).

### Available Flowables

| Flowable | Purpose | Usage |
|----------|---------|-------|
| `GoldRule(width, height, color)` | Decorative horizontal rule | After cover titles |
| `CenteredGoldRule(width, height, color)` | Centered decorative rule | After section headings |
| `ChampagneLine()` | Full-width thin champagne line | Section separators |
| `CalloutBox(text, styles, bold_label=None)` | Burgundy left-border callout | Tips, important notes |
| `FillInLine(label="")` | Fill-in-the-blank line | Worksheet fields |
| `NumberedFillLine(number)` | Numbered fill-in line | Idea dumps, lists |

### Helper Functions

| Function | Purpose |
|----------|---------|
| `BrandDoc(output_path, product_name, website, handle)` | Creates doc with cover/content/divider templates |
| `cover_page(story, title, subtitle, description, brand_line)` | Adds dark cover with gold corner |
| `title_page(story, S, title, byline, dedication, bold_statement, copyright_text)` | Adds centered title/dedication page |
| `section_divider(story, number, title, subtitle)` | Adds centered section break page (auto-switches template) |
| `make_table(data, col_widths)` | Creates branded table with sand headers |
| `get_styles()` | Returns dict of all paragraph styles |

### Table Design

Tables use `make_table(data, col_widths)`:
- First row = header (sand background, burgundy Outfit SemiBold text)
- Body rows have alternating subtle tint
- Champagne borders, clean spacing
- `data` is a list of lists; first sublist is headers

```python
data = [
    ["COLUMN 1", "COLUMN 2", "COLUMN 3"],
    ["Row 1 cell", "Content", "More content"],
    ["Row 2 cell", "Content", "More content"],
]
table = make_table(data, col_widths=[80, 200, 188])
story.append(table)
```

### Inline Font Switching

Within Paragraph text, use XML tags to switch fonts:
```python
# Bold inline
'<font name="Outfit-SemiBold">Bold text</font> normal text'

# Italic serif inline
'<font name="CormorantGaramond-Italic" size="14">Emphasis</font>'

# Colored inline
'<font name="Outfit-SemiBold" color="#763c47">Burgundy text</font>'
```

### Note: Section Divider Page Breaks

`section_divider()` handles its own `PageBreak()` and template switching. Don't add a `PageBreak()` before calling it or you'll get a blank page.

## Requirements

```bash
pip install reportlab
```

## File Structure

```
ship-it-brand-pdf/
├── SKILL.md                              # This file
├── requirements.txt                      # Python dependencies
├── scripts/
│   └── brand_pdf.py                      # Core module (import this)
├── assets/
│   └── fonts/                            # TTF font files
│       ├── CormorantGaramond-Regular.ttf
│       ├── CormorantGaramond-Italic.ttf
│       ├── CormorantGaramond-SemiBold.ttf
│       ├── CormorantGaramond-SemiBoldItalic.ttf
│       ├── CormorantGaramond-Bold.ttf
│       ├── CormorantGaramond-Light.ttf
│       ├── Outfit-Light.ttf
│       ├── Outfit-Regular.ttf
│       ├── Outfit-Medium.ttf
│       ├── Outfit-SemiBold.ttf
│       └── Outfit-Bold.ttf
└── references/
    ├── example_launch_plan.py            # Full build script: One-Page Launch Plan
    └── example_decide_already.py         # Full build script: Decide Already workbook
```

## Building a New Product PDF

### Step-by-step process:

1. **Read the reference examples** in `references/` to see the exact patterns
2. **Set up the document** with `BrandDoc(output, product_name)` — handles all page templates
3. **Add cover page** using `cover_page()`
4. **Add title page** using `title_page()`
5. **Add content** using the style dictionary from `get_styles()`
6. **Use section dividers** between major sections with `section_divider()`
7. **Add worksheets** using `FillInLine()` and `NumberedFillLine()`
8. **Add tables** using `make_table()`
9. **Add callouts** using `CalloutBox()` for tips and important notes
10. **Build** with `doc.build(story)` — page backgrounds handled automatically

### Content patterns from existing products:

- **Workbooks** (Decide Already): Section dividers → instruction text → worksheet → callout → next section
- **Guides** (Launch Plan): Cover → overview → worksheet pages → scorecard → CTA
- **Playbooks** (Ship or Kill): Cover → chapter pages with long-form prose → checklists → decision frameworks

### CTA pages (end of every product):

Always end with a champagne line, centered heading, gold rule, italic pull quote about the next product in the ladder, product name + price in burgundy bold, bullet list of what's included, and `theshipitsystem.com` link. Sign off with "— Molly" and "Infrastructure, not aspiration."

## Brand Rules (Non-Negotiable)

1. **Fonts**: Cormorant Garamond for ALL headings/serif. Outfit for ALL body/sans. Never substitute.
2. **Colors**: Use the defined constants. Never use raw hex values outside the palette.
3. **Cover**: Always dark charcoal bg with gold L-corner accent. Brand line in gold tracked uppercase.
4. **Body pages**: Always cream background with thin champagne line at top, footer with product name + URL.
5. **Section dividers**: Burgundy number (48pt Cormorant), charcoal title (32pt Cormorant), muted subtitle.
6. **Tables**: Sand header bg, burgundy header text, champagne borders. Always use `make_table()`.
7. **Callouts**: Burgundy left border. Use `CalloutBox()`.
8. **Voice**: Direct, practical, anti-fluff. Infrastructure metaphors. No guru-speak.
