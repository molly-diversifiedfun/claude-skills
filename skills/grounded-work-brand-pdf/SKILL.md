---
name: grounded-work-brand-pdf
description: Generate branded PDFs for the Grounded Work (Conscious Shipping) product line. Use this skill whenever the user asks to create, rebuild, or generate any PDF product — workbooks, guides, lead magnets, or any downloadable asset for the Grounded Work brand. Also use when the user mentions brand-consistent PDFs, the Grounded Work design, or references products like "Clarity Compass," "Alignment Sprint," or "Kickstart." Trigger for any PDF request within the conscious-shipping project since all PDFs must match the brand design system.
---

# Grounded Work — Brand PDF Generator

## Overview

This skill generates production-quality branded PDFs that match the Grounded Work design system. Every PDF uses Caveat (handwritten headings) + Quicksand (sans body) + Shadows Into Light (quotes/italic) typography with the brand color palette: sage, cream, espresso, terracotta, stone, saddle.

## Quick Start

```python
import sys
sys.path.insert(0, '/path/to/grounded-work-brand-pdf/scripts')
from brand_pdf import *
from reportlab.platypus import Spacer, PageBreak

OUTPUT = "/path/to/my_product.pdf"

# BrandDoc handles all page templates automatically
doc = BrandDoc(OUTPUT, "PRODUCT NAME")

S = get_styles()
story = []

# Cover page (espresso bg, terracotta corner accent)
cover_page(story,
    title="Your Title Here.",
    subtitle="A Grounded Work Workbook",
    description="One-line description of what this product does.",
)

# Title page (cream bg, centered)
title_page(story, S,
    title="Your Title Here.",
    byline="By Molly Shelestak",
    dedication="Who this is for and why it matters.",
    bold_statement="Applied clarity.",
    copyright_text="© 2026 Molly Shelestak | unstuckwithmolly.com"
)

# Content pages (cream bg, stone line at top)
story.append(Paragraph("Your heading", S['h2']))
story.append(Paragraph("Your body text.", S['body']))

# Section dividers (cream bg, stone line at 35% — auto-detected)
section_divider(story, 1, "Section Title", "Subtitle goes here")

# Build — page backgrounds switch automatically
doc.build(story)
```

## Design System Reference

### Page Types

| Page Type | Background | When Used |
|-----------|-----------|-----------|
| **Cover** | Espresso (#2E2A26) with terracotta L-corner accent | First page only |
| **Title** | Cream (#F5F0E1), centered content | Page 2 (dedication/copyright) |
| **Content** | Cream bg, thin stone line at top, footer | All body pages |
| **Section Divider** | Cream bg, centered sage number + title | Before each major section |

### Colors (all pre-defined as constants)

| Constant | Hex | Usage |
|----------|-----|-------|
| `SAGE` | #4A6741 | Primary accent, section numbers, CTAs, callout borders |
| `CREAM` | #F5F0E1 | Page backgrounds |
| `ESPRESSO` | #2E2A26 | Body text, headings, cover background |
| `TERRACOTTA` | #C67B5C | Cover accent, decorative rules, L-corner |
| `STONE` | #E8E0D0 | Page top lines, table borders, fill-in lines |
| `SADDLE` | #8B6D4F | Captions, footers, secondary text |
| `SAND` | #F0E8D5 | Table header backgrounds |
| `BORDER` | #D4C4A8 | Explicit border color |
| `MUTED` | #5C5347 | Muted foreground text |
| `WHITE` | #FFFFFF | Cover text, reversed elements |
| `DARK_BG` | #2E2A26 | Cover page background (alias for ESPRESSO) |

### Typography

| Role | Font | Style Key |
|------|------|-----------|
| H1 heading | Caveat SemiBold 32pt | `S['h1']` |
| H2 heading | Caveat SemiBold 26pt | `S['h2']` |
| H3 heading | Caveat Medium 18pt | `S['h3']` |
| Italic emphasis | Shadows Into Light 20pt | `S['serif_italic']` |
| Body text | Quicksand Light 11pt | `S['body']` |
| Body bold | Quicksand SemiBold 11pt | `S['body_bold']` |
| Small/caption | Quicksand Light 9pt | `S['small']` |
| Sage label | Quicksand SemiBold 12pt sage | `S['sage_bold']` |
| Table header | Quicksand SemiBold 9pt sage | `S['table_header']` |
| Table cell | Quicksand Light 9.5pt | `S['table_cell']` |
| Quote | Shadows Into Light 14pt | `S['quote']` |
| Quote attribution | Quicksand Light 10pt muted | `S['quote_attr']` |

Centered variants: Append `_center` to any style name (e.g., `S['h2_center']`, `S['body_center']`).

### Available Flowables

| Flowable | Purpose | Usage |
|----------|---------|-------|
| `SageRule(width, height, color)` | Decorative horizontal rule | After cover titles |
| `CenteredSageRule(width, height, color)` | Centered decorative rule | After section headings |
| `StoneLine()` | Full-width thin stone line | Section separators |
| `CalloutBox(text, styles, bold_label=None)` | Sage left-border callout | Tips, AI Power Moves |
| `FillInLine(label="")` | Fill-in-the-blank line | Worksheet fields |
| `NumberedFillLine(number)` | Numbered fill-in line | Idea dumps, lists |

### Helper Functions

| Function | Purpose |
|----------|---------|
| `BrandDoc(output_path, product_name, website, handle)` | Creates doc with cover/content/divider templates |
| `cover_page(story, title, subtitle, description, brand_line)` | Adds espresso cover with terracotta corner |
| `title_page(story, S, title, byline, dedication, bold_statement, copyright_text)` | Adds centered title/dedication page |
| `section_divider(story, number, title, subtitle)` | Adds centered section break page (auto-switches template) |
| `make_table(data, col_widths)` | Creates branded table with sand headers |
| `get_styles()` | Returns dict of all paragraph styles |

### Table Design

Tables use `make_table(data, col_widths)`:
- First row = header (sand background, sage Quicksand SemiBold text)
- Body rows have alternating subtle tint
- Stone borders, clean spacing
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
'<font name="Quicksand-SemiBold">Bold text</font> normal text'

# Italic inline
'<font name="ShadowsIntoLight" size="14">Emphasis</font>'

# Colored inline
'<font name="Quicksand-SemiBold" color="#4A6741">Sage text</font>'
```

### Note: Section Divider Page Breaks

`section_divider()` handles its own `PageBreak()` and template switching. Don't add a `PageBreak()` before calling it or you'll get a blank page.

## Requirements

```bash
pip install reportlab
```

## File Structure

```
grounded-work-brand-pdf/
├── SKILL.md                              # This file
├── requirements.txt                      # Python dependencies
├── scripts/
│   └── brand_pdf.py                      # Core module (import this)
└── assets/
    └── fonts/                            # TTF font files
        ├── Caveat-Regular.ttf
        ├── Caveat-Medium.ttf
        ├── Caveat-SemiBold.ttf
        ├── Caveat-Bold.ttf
        ├── Quicksand-Light.ttf
        ├── Quicksand-Regular.ttf
        ├── Quicksand-Medium.ttf
        ├── Quicksand-SemiBold.ttf
        ├── Quicksand-Bold.ttf
        └── ShadowsIntoLight-Regular.ttf
```

## Building a New Product PDF

### Step-by-step process:

1. **Set up the document** with `BrandDoc(output, product_name)` — handles all page templates
2. **Add cover page** using `cover_page()`
3. **Add title page** using `title_page()`
4. **Add content** using the style dictionary from `get_styles()`
5. **Use section dividers** between major sections with `section_divider()`
6. **Add worksheets** using `FillInLine()` and `NumberedFillLine()`
7. **Add tables** using `make_table()`
8. **Add callouts** using `CalloutBox()` for tips and AI Power Moves
9. **Build** with `doc.build(story)` — page backgrounds handled automatically

### Content patterns:

- **Workbooks**: Section dividers -> instruction text -> worksheet -> callout -> next section
- **Exercises**: `FillInLine(label="...")` for text fields, `NumberedFillLine(n)` for ordered lists
- **AI Power Moves**: `CalloutBox(prompt_text, S, bold_label="AI Power Move:")` after exercises
- **Rating scales**: `make_table()` with `[1] [2] [3] [4] [5]` score boxes
- **Checkboxes**: `Paragraph("☐ Label text", S['body'])`

### CTA pages (end of every product):

Always end with a `StoneLine()`, centered heading, `CenteredSageRule()`, italic pull quote, product name + price in `sage_bold`, bullet list, and `unstuckwithmolly.com` link. Sign off with "— Molly" and "Applied clarity."

## Brand Rules (Non-Negotiable)

1. **Fonts**: Caveat for ALL headings. Quicksand for ALL body/sans. Shadows Into Light for quotes/italic. Never substitute.
2. **Colors**: Use the defined constants. Never use raw hex values outside the palette.
3. **Cover**: Always espresso bg with terracotta L-corner accent. Brand line in terracotta tracked uppercase.
4. **Body pages**: Always cream background with thin stone line at top, footer with product name + URL.
5. **Section dividers**: Sage number (44pt Caveat Bold), espresso title (28pt Caveat SemiBold), muted subtitle.
6. **Tables**: Sand header bg, sage header text, stone borders. Always use `make_table()`.
7. **Callouts**: Sage left border. Use `CalloutBox()`.
8. **Voice**: Direct, practical, anti-fluff. Values-first language. No guru-speak. "Applied clarity."
9. **Footer**: "unstuckwithmolly.com" on left, "@unstuckwithmolly" on right.
