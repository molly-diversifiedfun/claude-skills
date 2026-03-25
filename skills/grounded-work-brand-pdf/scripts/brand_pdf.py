"""
Grounded Work — Brand PDF Module
Matches the Grounded Work (Conscious Shipping) design system.
Fonts: Caveat (headings) + Quicksand (body) + Shadows Into Light (quotes/italic)
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, BaseDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, KeepTogether, Flowable, Frame, PageTemplate,
    NextPageTemplate
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ============================================================
# FONT REGISTRATION
# ============================================================
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(_SCRIPT_DIR, "..", "assets", "fonts")
# Fallback: check common locations
if not os.path.isdir(FONTS_DIR):
    for _fallback in [
        os.path.join(os.path.expanduser("~"), "github", "skills", "skills",
                     "grounded-work-brand-pdf", "assets", "fonts"),
        os.path.join(os.getcwd(), "assets", "fonts"),
    ]:
        if os.path.isdir(_fallback):
            FONTS_DIR = _fallback
            break


def register_fonts():
    fonts = {
        "Caveat": "Caveat-Regular.ttf",
        "Caveat-Medium": "Caveat-Medium.ttf",
        "Caveat-SemiBold": "Caveat-SemiBold.ttf",
        "Caveat-Bold": "Caveat-Bold.ttf",
        "Quicksand-Light": "Quicksand-Light.ttf",
        "Quicksand": "Quicksand-Regular.ttf",
        "Quicksand-Medium": "Quicksand-Medium.ttf",
        "Quicksand-SemiBold": "Quicksand-SemiBold.ttf",
        "Quicksand-Bold": "Quicksand-Bold.ttf",
        "ShadowsIntoLight": "ShadowsIntoLight-Regular.ttf",
    }
    for name, filename in fonts.items():
        path = os.path.join(FONTS_DIR, filename)
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont(name, path))


register_fonts()

# ============================================================
# BRAND COLORS
# ============================================================
SAGE = HexColor("#4A6741")
CREAM = HexColor("#F5F0E1")
ESPRESSO = HexColor("#2E2A26")
TERRACOTTA = HexColor("#C67B5C")
STONE = HexColor("#E8E0D0")
SADDLE = HexColor("#8B6D4F")
SAND = HexColor("#F0E8D5")
BORDER = HexColor("#D4C4A8")
MUTED = HexColor("#5C5347")
WHITE = HexColor("#FFFFFF")
DARK_BG = HexColor("#2E2A26")  # Same as ESPRESSO — cover background

# ============================================================
# PAGE DIMENSIONS
# ============================================================
PAGE_W, PAGE_H = letter
MARGIN_L = 72
MARGIN_R = 72
MARGIN_T = 72
MARGIN_B = 72
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

# ============================================================
# PARAGRAPH STYLES
# ============================================================
def get_styles():
    s = {}
    # Headings — Caveat (adjusted sizes for larger x-height)
    s['h1'] = ParagraphStyle('h1', fontName='Caveat-SemiBold', fontSize=32,
                             leading=38, textColor=ESPRESSO, spaceAfter=16)
    s['h1_center'] = ParagraphStyle('h1c', parent=s['h1'], alignment=TA_CENTER)
    s['h2'] = ParagraphStyle('h2', fontName='Caveat-SemiBold', fontSize=26,
                             leading=32, textColor=ESPRESSO, spaceAfter=12,
                             spaceBefore=24)
    s['h2_center'] = ParagraphStyle('h2c', parent=s['h2'], alignment=TA_CENTER)
    s['h3'] = ParagraphStyle('h3', fontName='Caveat-Medium', fontSize=18,
                             leading=24, textColor=ESPRESSO, spaceAfter=8,
                             spaceBefore=16)
    s['h3_center'] = ParagraphStyle('h3c', parent=s['h3'], alignment=TA_CENTER)
    # Serif italic — Shadows Into Light (replaces Cormorant Garamond Italic)
    s['serif_italic'] = ParagraphStyle('si', fontName='ShadowsIntoLight',
                                       fontSize=20, leading=26,
                                       textColor=ESPRESSO, spaceAfter=8,
                                       spaceBefore=8)
    s['serif_italic_center'] = ParagraphStyle('sic', parent=s['serif_italic'],
                                              alignment=TA_CENTER)
    s['subtitle_italic'] = ParagraphStyle('sti', fontName='ShadowsIntoLight',
                                          fontSize=18, leading=24,
                                          textColor=ESPRESSO, spaceAfter=8)
    s['subtitle_italic_center'] = ParagraphStyle('stic',
                                                  parent=s['subtitle_italic'],
                                                  alignment=TA_CENTER)
    # Body — Quicksand
    s['body'] = ParagraphStyle('body', fontName='Quicksand-Light', fontSize=11,
                               leading=18, textColor=ESPRESSO, spaceAfter=10)
    s['body_center'] = ParagraphStyle('bodyc', parent=s['body'],
                                      alignment=TA_CENTER)
    s['body_bold'] = ParagraphStyle('bb', fontName='Quicksand-SemiBold',
                                    fontSize=11, leading=18,
                                    textColor=ESPRESSO, spaceAfter=10,
                                    spaceBefore=10)
    s['body_bold_center'] = ParagraphStyle('bbc', parent=s['body_bold'],
                                           alignment=TA_CENTER)
    # Small
    s['small'] = ParagraphStyle('small', fontName='Quicksand-Light', fontSize=9,
                                leading=14, textColor=MUTED, spaceAfter=4)
    s['small_center'] = ParagraphStyle('smallc', parent=s['small'],
                                       alignment=TA_CENTER)
    # Callout body
    s['callout_body'] = ParagraphStyle('cb', fontName='Quicksand-Light',
                                       fontSize=11, leading=18,
                                       textColor=ESPRESSO, spaceAfter=4)
    # Sage bold (replaces burgundy_bold)
    s['sage_bold'] = ParagraphStyle('sageb', fontName='Quicksand-SemiBold',
                                    fontSize=12, leading=18, textColor=SAGE,
                                    spaceAfter=10, spaceBefore=10)
    s['sage_bold_center'] = ParagraphStyle('sagebc', parent=s['sage_bold'],
                                           alignment=TA_CENTER)
    # Section divider styles
    s['section_number'] = ParagraphStyle('sn', fontName='Caveat-Bold',
                                         fontSize=44, leading=48,
                                         textColor=SAGE, alignment=TA_CENTER,
                                         spaceAfter=8)
    s['section_title'] = ParagraphStyle('st', fontName='Caveat-SemiBold',
                                        fontSize=28, leading=36,
                                        textColor=ESPRESSO, alignment=TA_CENTER,
                                        spaceAfter=8)
    s['section_subtitle'] = ParagraphStyle('ss', fontName='Quicksand-Light',
                                           fontSize=12, leading=18,
                                           textColor=MUTED, alignment=TA_CENTER,
                                           spaceAfter=8)
    # Table
    s['table_header'] = ParagraphStyle('th', fontName='Quicksand-SemiBold',
                                       fontSize=9, leading=13, textColor=SAGE)
    s['table_cell'] = ParagraphStyle('tc', fontName='Quicksand-Light',
                                     fontSize=9.5, leading=14,
                                     textColor=ESPRESSO)
    s['table_cell_bold'] = ParagraphStyle('tcb', fontName='Quicksand-SemiBold',
                                          fontSize=9.5, leading=14,
                                          textColor=ESPRESSO)
    # Fill label
    s['fill_label'] = ParagraphStyle('fl', fontName='Quicksand-Light',
                                     fontSize=10, leading=16,
                                     textColor=ESPRESSO, spaceAfter=4)
    # Copyright
    s['copyright'] = ParagraphStyle('copy', fontName='Quicksand-Light',
                                    fontSize=9, leading=14, textColor=MUTED,
                                    alignment=TA_CENTER)
    # Quote — Shadows Into Light
    s['quote'] = ParagraphStyle('q', fontName='ShadowsIntoLight', fontSize=14,
                                leading=22, textColor=ESPRESSO, leftIndent=24,
                                rightIndent=24, spaceAfter=4, spaceBefore=12)
    s['quote_center'] = ParagraphStyle('qc', parent=s['quote'],
                                       alignment=TA_CENTER, leftIndent=0,
                                       rightIndent=0)
    s['quote_attr'] = ParagraphStyle('qa', fontName='Quicksand-Light',
                                     fontSize=10, leading=14, textColor=MUTED,
                                     spaceAfter=12, spaceBefore=2)
    s['quote_attr_center'] = ParagraphStyle('qac', parent=s['quote_attr'],
                                            alignment=TA_CENTER)
    return s


# ============================================================
# CUSTOM FLOWABLES
# ============================================================

class SageRule(Flowable):
    """Decorative horizontal rule. Default: SAGE."""
    def __init__(self, width=60, height=3, color=SAGE):
        Flowable.__init__(self)
        self.rule_width = width
        self.rule_height = height
        self.rule_color = color
        self.width = width
        self.height = height + 8

    def draw(self):
        self.canv.setFillColor(self.rule_color)
        self.canv.rect(0, 4, self.rule_width, self.rule_height, fill=1, stroke=0)


class CenteredSageRule(Flowable):
    """Centered decorative horizontal rule. Default: TERRACOTTA."""
    def __init__(self, width=60, height=3, color=TERRACOTTA, page_width=CONTENT_W):
        Flowable.__init__(self)
        self.rule_width = width
        self.rule_height = height
        self.rule_color = color
        self.page_width = page_width
        self.width = page_width
        self.height = height + 16

    def draw(self):
        self.canv.setFillColor(self.rule_color)
        x = (self.page_width - self.rule_width) / 2
        self.canv.rect(x, 8, self.rule_width, self.rule_height, fill=1, stroke=0)


class StoneLine(Flowable):
    """Full-width thin line. Default: STONE."""
    def __init__(self, width=CONTENT_W, thickness=0.5, color=STONE):
        Flowable.__init__(self)
        self.line_width = width
        self.thickness = thickness
        self.line_color = color
        self.width = width
        self.height = thickness + 12

    def draw(self):
        self.canv.setStrokeColor(self.line_color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 6, self.line_width, 6)


class CalloutBox(Flowable):
    """Left-border callout box. Border: SAGE."""
    def __init__(self, text, styles, width=CONTENT_W, bold_label=None):
        Flowable.__init__(self)
        self.text = text
        self.bold_label = bold_label
        self.box_width = width
        self.styles = styles
        self._setup()

    def _setup(self):
        inner_w = self.box_width - 24 - 16
        if self.bold_label:
            content = (f'<b><font name="Quicksand-SemiBold">'
                       f'{self.bold_label}</font></b> {self.text}')
        else:
            content = self.text
        self.para = Paragraph(content, self.styles['callout_body'])
        w, h = self.para.wrap(inner_w, 1000)
        self.para_height = h
        self.width = self.box_width
        self.height = h + 24

    def draw(self):
        self.canv.setFillColor(SAGE)
        self.canv.rect(0, 0, 4, self.height, fill=1, stroke=0)
        self.para.drawOn(self.canv, 20, 12)


class FillInLine(Flowable):
    """Fill-in-the-blank line. Line color: STONE. Label font: Quicksand-Light."""
    def __init__(self, label="", width=CONTENT_W, line_color=STONE):
        Flowable.__init__(self)
        self.label = label
        self.line_width = width
        self.line_color = line_color
        self.width = width
        self.height = 28

    def draw(self):
        if self.label:
            self.canv.setFont("Quicksand-Light", 10)
            self.canv.setFillColor(MUTED)
            self.canv.drawString(0, 14, self.label)
        self.canv.setStrokeColor(self.line_color)
        self.canv.setLineWidth(0.5)
        self.canv.line(0, 4, self.line_width, 4)


class NumberedFillLine(Flowable):
    """Numbered fill-in line. Number: Caveat in SAGE. Line: STONE."""
    def __init__(self, number, width=CONTENT_W, line_color=STONE):
        Flowable.__init__(self)
        self.number = number
        self.line_width = width
        self.line_color = line_color
        self.width = width
        self.height = 26

    def draw(self):
        self.canv.setFont("Caveat", 12)
        self.canv.setFillColor(SAGE)
        self.canv.drawString(0, 8, f"{self.number:02d}")
        self.canv.setStrokeColor(self.line_color)
        self.canv.setLineWidth(0.5)
        self.canv.line(28, 4, self.line_width, 4)


# ============================================================
# PAGE DECORATION HANDLERS
# ============================================================

def _draw_footer(canvas, doc):
    """Shared footer for content and divider pages."""
    canvas.setFont("Quicksand-Light", 8)
    canvas.setFillColor(SADDLE)
    canvas.drawString(MARGIN_L, 36, f"{doc.product_name}  |  {doc.website}")
    page_num = canvas.getPageNumber()
    canvas.drawRightString(PAGE_W - MARGIN_R, 36,
                           f"{doc.handle}  |  {page_num}")


def draw_content_page(canvas, doc):
    """Content page: CREAM bg, STONE top line, SADDLE footer."""
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(STONE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_L, PAGE_H - 36, PAGE_W - MARGIN_R, PAGE_H - 36)
    _draw_footer(canvas, doc)
    canvas.restoreState()


def draw_cover_page(canvas, doc):
    """Cover page: ESPRESSO bg, TERRACOTTA L-corner accent."""
    canvas.saveState()
    canvas.setFillColor(ESPRESSO)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # L-corner accent — terracotta stroke at top-left
    canvas.setStrokeColor(TERRACOTTA)
    canvas.setLineWidth(0.75)
    cx, cy = MARGIN_L, PAGE_H - MARGIN_T + 20
    canvas.line(cx, cy, cx, cy + 50)
    canvas.line(cx, cy + 50, cx + 50, cy + 50)
    canvas.restoreState()


def draw_section_divider_page(canvas, doc):
    """Section divider: CREAM bg, STONE line at 35% height."""
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(STONE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_L, PAGE_H * 0.35, PAGE_W - MARGIN_R, PAGE_H * 0.35)
    _draw_footer(canvas, doc)
    canvas.restoreState()


# ============================================================
# BRAND DOCUMENT
# ============================================================

def BrandDoc(output_path, product_name, website="unstuckwithmolly.com",
             handle="@unstuckwithmolly"):
    """Create a BaseDocTemplate with cover, content, and divider page templates.

    Usage:
        doc = BrandDoc("/path/to/output.pdf", "PRODUCT NAME")
        story = [...]
        doc.build(story)
    """
    frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W,
                  PAGE_H - MARGIN_T - MARGIN_B, id='main')

    cover_template = PageTemplate(id='cover', frames=[frame],
                                  onPage=draw_cover_page)
    content_template = PageTemplate(id='content', frames=[frame],
                                    onPage=draw_content_page)
    divider_template = PageTemplate(id='divider', frames=[frame],
                                    onPage=draw_section_divider_page)

    doc = BaseDocTemplate(
        output_path, pagesize=letter,
        leftMargin=MARGIN_L, rightMargin=MARGIN_R,
        topMargin=MARGIN_T, bottomMargin=MARGIN_B,
        pageTemplates=[cover_template, content_template, divider_template]
    )
    doc.product_name = product_name
    doc.website = website
    doc.handle = handle
    return doc


# ============================================================
# STORY HELPERS
# ============================================================

def cover_page(story, title, subtitle, description,
               author_name="Molly Shelestak",
               author_role="Build Partner for Conscious Professionals",
               website="unstuckwithmolly.com", handle="@unstuckwithmolly",
               brand_line="GROUNDED WORK"):
    """Add a dark cover page with terracotta L-corner accent."""
    story.append(Spacer(1, 60))
    # Brand line — tracked uppercase in terracotta
    story.append(Paragraph(
        brand_line,
        ParagraphStyle('cb', fontName='Quicksand-SemiBold', fontSize=11,
                       leading=14, textColor=TERRACOTTA, spaceAfter=20,
                       letterSpacing=3)
    ))
    # Title — large Caveat in cream
    story.append(Paragraph(title,
        ParagraphStyle('ct', fontName='Caveat-SemiBold', fontSize=48,
                       leading=54, textColor=CREAM, spaceAfter=8)))
    # Decorative rule — terracotta
    story.append(SageRule(width=60, height=3, color=TERRACOTTA))
    story.append(Spacer(1, 16))
    # Subtitle — Shadows Into Light in cream
    story.append(Paragraph(subtitle,
        ParagraphStyle('cs', fontName='ShadowsIntoLight', fontSize=18,
                       leading=24, textColor=CREAM, spaceAfter=8)))
    # Description — Quicksand in stone
    story.append(Paragraph(description,
        ParagraphStyle('cd', fontName='Quicksand-Light', fontSize=12,
                       leading=18, textColor=STONE)))
    story.append(Spacer(1, 140))
    # Author name — sage (light variant)
    story.append(Paragraph(
        f'<font name="Quicksand-SemiBold">{author_name}</font>',
        ParagraphStyle('ca', fontName='Quicksand-SemiBold', fontSize=12,
                       leading=16, textColor=SAGE, spaceAfter=2)))
    # Author role — stone
    story.append(Paragraph(author_role,
        ParagraphStyle('cr', fontName='Quicksand-Light', fontSize=10,
                       leading=14, textColor=STONE, spaceAfter=2)))
    # Website + handle — saddle
    story.append(Paragraph(f'{website} | {handle}',
        ParagraphStyle('cu', fontName='Quicksand-Light', fontSize=10,
                       leading=14, textColor=SADDLE)))
    # Switch to content template for subsequent pages
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())


def title_page(story, styles, title, byline, dedication=None,
               bold_statement=None, copyright_text=None):
    """Add a centered title/dedication page."""
    story.append(Spacer(1, 80))
    story.append(Paragraph(title, styles['h1_center']))
    story.append(Paragraph(f'<i>{byline}</i>',
                           styles['subtitle_italic_center']))
    story.append(CenteredSageRule(width=60, height=3, color=TERRACOTTA))
    if dedication:
        story.append(Paragraph(f'<i>{dedication}</i>',
                               styles['serif_italic_center']))
    if bold_statement:
        story.append(Spacer(1, 8))
        story.append(Paragraph(bold_statement, styles['sage_bold_center']))
    if copyright_text:
        story.append(Spacer(1, 80))
        story.append(Paragraph(copyright_text, styles['copyright']))
    story.append(PageBreak())


def section_divider(story, number, title, subtitle=None, handler=None):
    """Add a section divider page with large number and title."""
    # Switch to divider template for this page
    story.append(NextPageTemplate('divider'))
    story.append(PageBreak())
    story.append(Spacer(1, 200))
    num_str = f"{number:02d}" if isinstance(number, int) else str(number)
    story.append(Paragraph(num_str,
        ParagraphStyle('dn', fontName='Caveat-Bold', fontSize=44, leading=48,
                       textColor=SAGE, alignment=TA_CENTER, spaceAfter=8)))
    story.append(Paragraph(title,
        ParagraphStyle('dt', fontName='Caveat-SemiBold', fontSize=28,
                       leading=36, textColor=ESPRESSO, alignment=TA_CENTER,
                       spaceAfter=8)))
    if subtitle:
        story.append(Paragraph(subtitle,
            ParagraphStyle('ds', fontName='Quicksand-Light', fontSize=12,
                           leading=18, textColor=MUTED, alignment=TA_CENTER)))
    # Switch back to content for the next page
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())


def make_table(data, col_widths=None, header_row=True):
    """Create a branded table with SAND headers, SAGE header text, STONE borders."""
    styles = get_styles()
    table_data = []
    for i, row in enumerate(data):
        cells = []
        for cell in row:
            style = (styles['table_header'] if (i == 0 and header_row)
                     else styles['table_cell'])
            cells.append(Paragraph(str(cell), style))
        table_data.append(cells)
    t = Table(table_data, colWidths=col_widths)
    cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), SAND),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, STONE),
        ('LINEBELOW', (0, 1), (-1, -1), 0.25, STONE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            cmds.append(('BACKGROUND', (0, i), (-1, i), SAND))
    t.setStyle(TableStyle(cmds))
    return t
