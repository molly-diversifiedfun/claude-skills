"""
Test script: generates a sample PDF using every component of the
Grounded Work brand_pdf module.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brand_pdf import *
from reportlab.platypus import Spacer, PageBreak, KeepTogether

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      "..", "test_output.pdf")

doc = BrandDoc(OUTPUT, "GROUNDED WORK TEST")
S = get_styles()
story = []

# --- Cover page ---
cover_page(story,
    title="The Clarity Compass.",
    subtitle="Find your direction in 25 minutes",
    description="A values-first workbook for conscious professionals.",
)

# --- Title page ---
title_page(story, S,
    title="The Clarity Compass.",
    byline="By Molly Shelestak",
    dedication="For the conscious professionals who've done the inner work "
               "— and now need the outer plan.",
    bold_statement="Applied clarity.",
    copyright_text="© 2026 Molly Shelestak | unstuckwithmolly.com"
)

# --- Typography test page ---
story.append(Paragraph("Typography Test", S['h1']))
story.append(Paragraph("H1 — Caveat SemiBold 32pt", S['h1']))
story.append(Paragraph("H2 — Caveat SemiBold 26pt", S['h2']))
story.append(Paragraph("H3 — Caveat Medium 18pt", S['h3']))
story.append(Paragraph("Body — Quicksand Light 11pt. Lorem ipsum dolor sit "
    "amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut "
    "labore et dolore magna aliqua.", S['body']))
story.append(Paragraph("Body Bold — Quicksand SemiBold 11pt.", S['body_bold']))
story.append(Paragraph("Small — Quicksand Light 9pt caption text.", S['small']))
story.append(Paragraph("Sage Bold — accent label text", S['sage_bold']))
story.append(Paragraph('<i>"Quote text in Shadows Into Light — the journal-entry '
    'style companion font."</i>', S['quote']))
story.append(Paragraph("— Attribution, Quicksand Light", S['quote_attr']))
story.append(PageBreak())

# --- Flowables test page ---
story.append(Paragraph("Flowables Test", S['h2']))
story.append(Spacer(1, 12))

story.append(Paragraph("SageRule:", S['small']))
story.append(SageRule())
story.append(Spacer(1, 12))

story.append(Paragraph("CenteredSageRule:", S['small']))
story.append(CenteredSageRule())
story.append(Spacer(1, 12))

story.append(Paragraph("StoneLine:", S['small']))
story.append(StoneLine())
story.append(Spacer(1, 12))

story.append(Paragraph("CalloutBox:", S['small']))
story.append(CalloutBox(
    "This is a callout box with a sage left border. Use it for tips, "
    "important notes, and AI Power Move prompts.",
    S, bold_label="AI Power Move:"))
story.append(Spacer(1, 12))

story.append(Paragraph("FillInLine:", S['small']))
story.append(FillInLine("Your core value:"))
story.append(FillInLine())
story.append(Spacer(1, 12))

story.append(Paragraph("NumberedFillLine:", S['small']))
for i in range(1, 4):
    story.append(NumberedFillLine(i))
story.append(PageBreak())

# --- Table test page ---
story.append(Paragraph("Table Test", S['h2']))
story.append(Spacer(1, 12))
data = [
    ["DIMENSION", "SCORE", "NOTES"],
    ["Values Alignment", "4/5", "Strong match with current role"],
    ["Energy Protection", "3/5", "Needs boundary work"],
    ["Action Clarity", "5/5", "Clear next steps identified"],
    ["Integration", "2/5", "Gap between knowing and doing"],
]
story.append(make_table(data, col_widths=[150, 80, 238]))
story.append(PageBreak())

# --- Section divider test ---
section_divider(story, 1, "Values-to-Action Bridge",
                "Connecting what matters to what you do next")

# --- Post-divider content ---
story.append(Paragraph("Content After Divider", S['h2']))
story.append(Paragraph(
    "This page should have a cream background with a stone line at the top "
    "and the standard footer. The section divider page before it should have "
    "the stone line at 35% page height.", S['body']))
story.append(Spacer(1, 12))
story.append(Paragraph("Exercise: Core Values Audit", S['h3']))
story.append(Paragraph("List your top 3 operating values — the ones you "
    "actually live by, not the ones you aspire to.", S['body']))
story.append(FillInLine("Value 1:"))
story.append(FillInLine("Value 2:"))
story.append(FillInLine("Value 3:"))
story.append(Spacer(1, 12))
story.append(Paragraph("☐ I can point to a decision I made this week based "
    "on each value above.", S['body']))
story.append(Paragraph("☐ These values would surprise no one who knows me "
    "well.", S['body']))

# Build
doc.build(story)
print(f"Test PDF generated: {OUTPUT}")
