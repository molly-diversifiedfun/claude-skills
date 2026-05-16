"""
Unstuck with Molly — Brand PDF Module
Matches the Ship or Kill PDF design system exactly.
Fonts: Cormorant Garamond (headings) + Outfit (body)

Source of truth: molly-diversifiedfun/claude-skills (skills/ship-it-brand-pdf/).
~/github/skills and ~/github/claude-skills are two local checkouts of the same
remote — pull before edits, push after.
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
        os.path.join(os.path.expanduser("~"), "skills", "skills", "ship-it-brand-pdf", "assets", "fonts"),
        os.path.join(os.getcwd(), "assets", "fonts"),
    ]:
        if os.path.isdir(_fallback):
            FONTS_DIR = _fallback
            break

def register_fonts():
    fonts = {
        "CormorantGaramond": "CormorantGaramond-Regular.ttf",
        "CormorantGaramond-Italic": "CormorantGaramond-Italic.ttf",
        "CormorantGaramond-SemiBold": "CormorantGaramond-SemiBold.ttf",
        "CormorantGaramond-SemiBoldItalic": "CormorantGaramond-SemiBoldItalic.ttf",
        "CormorantGaramond-Bold": "CormorantGaramond-Bold.ttf",
        "CormorantGaramond-Light": "CormorantGaramond-Light.ttf",
        "Outfit-Light": "Outfit-Light.ttf",
        "Outfit": "Outfit-Regular.ttf",
        "Outfit-Medium": "Outfit-Medium.ttf",
        "Outfit-SemiBold": "Outfit-SemiBold.ttf",
        "Outfit-Bold": "Outfit-Bold.ttf",
    }
    for name, filename in fonts.items():
        path = os.path.join(FONTS_DIR, filename)
        if os.path.exists(path):
            pdfmetrics.registerFont(TTFont(name, path))

register_fonts()

# ============================================================
# BRAND COLORS
# ============================================================
BURGUNDY = HexColor("#763c47")
CREAM = HexColor("#f9f6f0")
CHARCOAL = HexColor("#251f1c")
GOLD = HexColor("#b8922e")
CHAMPAGNE = HexColor("#e5dbc8")
SAND = HexColor("#f3efe6")
ROSE_LIGHT = HexColor("#c4808d")
ROSE_DARK = HexColor("#54242e")
MUTED_FG = HexColor("#5c4f46")
WHITE = HexColor("#ffffff")
DARK_BG = HexColor("#1a1614")

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
    # Headings
    s['h1'] = ParagraphStyle('h1', fontName='CormorantGaramond', fontSize=36, leading=42, textColor=CHARCOAL, spaceAfter=16)
    s['h1_center'] = ParagraphStyle('h1c', parent=s['h1'], alignment=TA_CENTER)
    s['h2'] = ParagraphStyle('h2', fontName='CormorantGaramond', fontSize=28, leading=34, textColor=CHARCOAL, spaceAfter=12, spaceBefore=24)
    s['h2_center'] = ParagraphStyle('h2c', parent=s['h2'], alignment=TA_CENTER)
    s['h3'] = ParagraphStyle('h3', fontName='CormorantGaramond', fontSize=20, leading=26, textColor=CHARCOAL, spaceAfter=8, spaceBefore=16)
    s['h3_center'] = ParagraphStyle('h3c', parent=s['h3'], alignment=TA_CENTER)
    # Serif italic
    s['serif_italic'] = ParagraphStyle('si', fontName='CormorantGaramond-Italic', fontSize=20, leading=26, textColor=CHARCOAL, spaceAfter=8, spaceBefore=8)
    s['serif_italic_center'] = ParagraphStyle('sic', parent=s['serif_italic'], alignment=TA_CENTER)
    s['subtitle_italic'] = ParagraphStyle('sti', fontName='CormorantGaramond-Italic', fontSize=18, leading=24, textColor=CHARCOAL, spaceAfter=8)
    s['subtitle_italic_center'] = ParagraphStyle('stic', parent=s['subtitle_italic'], alignment=TA_CENTER)
    # Body
    s['body'] = ParagraphStyle('body', fontName='Outfit-Light', fontSize=11, leading=18, textColor=CHARCOAL, spaceAfter=10)
    s['body_center'] = ParagraphStyle('bodyc', parent=s['body'], alignment=TA_CENTER)
    s['body_bold'] = ParagraphStyle('bb', fontName='Outfit-SemiBold', fontSize=11, leading=18, textColor=CHARCOAL, spaceAfter=10, spaceBefore=10)
    s['body_bold_center'] = ParagraphStyle('bbc', parent=s['body_bold'], alignment=TA_CENTER)
    # Small
    s['small'] = ParagraphStyle('small', fontName='Outfit-Light', fontSize=9, leading=14, textColor=MUTED_FG, spaceAfter=4)
    s['small_center'] = ParagraphStyle('smallc', parent=s['small'], alignment=TA_CENTER)
    # Callout body
    s['callout_body'] = ParagraphStyle('cb', fontName='Outfit-Light', fontSize=11, leading=18, textColor=CHARCOAL, spaceAfter=4)
    # Burgundy bold
    s['burgundy_bold'] = ParagraphStyle('burgb', fontName='Outfit-SemiBold', fontSize=12, leading=18, textColor=BURGUNDY, spaceAfter=10, spaceBefore=10)
    s['burgundy_bold_center'] = ParagraphStyle('burgbc', parent=s['burgundy_bold'], alignment=TA_CENTER)
    # Section divider styles
    s['section_number'] = ParagraphStyle('sn', fontName='CormorantGaramond', fontSize=48, leading=52, textColor=BURGUNDY, alignment=TA_CENTER, spaceAfter=8)
    s['section_title'] = ParagraphStyle('st', fontName='CormorantGaramond', fontSize=32, leading=40, textColor=CHARCOAL, alignment=TA_CENTER, spaceAfter=8)
    s['section_subtitle'] = ParagraphStyle('ss', fontName='Outfit-Light', fontSize=12, leading=18, textColor=MUTED_FG, alignment=TA_CENTER, spaceAfter=8)
    # Table
    s['table_header'] = ParagraphStyle('th', fontName='Outfit-SemiBold', fontSize=9, leading=13, textColor=BURGUNDY)
    s['table_cell'] = ParagraphStyle('tc', fontName='Outfit-Light', fontSize=9.5, leading=14, textColor=CHARCOAL)
    s['table_cell_bold'] = ParagraphStyle('tcb', fontName='Outfit-SemiBold', fontSize=9.5, leading=14, textColor=CHARCOAL)
    # Fill label
    s['fill_label'] = ParagraphStyle('fl', fontName='Outfit-Light', fontSize=10, leading=16, textColor=CHARCOAL, spaceAfter=4)
    # Copyright
    s['copyright'] = ParagraphStyle('copy', fontName='Outfit-Light', fontSize=9, leading=14, textColor=MUTED_FG, alignment=TA_CENTER)
    # Quote
    s['quote'] = ParagraphStyle('q', fontName='CormorantGaramond-Italic', fontSize=14, leading=22, textColor=CHARCOAL, leftIndent=24, rightIndent=24, spaceAfter=4, spaceBefore=12)
    s['quote_center'] = ParagraphStyle('qc', parent=s['quote'], alignment=TA_CENTER, leftIndent=0, rightIndent=0)
    s['quote_attr'] = ParagraphStyle('qa', fontName='Outfit-Light', fontSize=10, leading=14, textColor=MUTED_FG, spaceAfter=12, spaceBefore=2)
    s['quote_attr_center'] = ParagraphStyle('qac', parent=s['quote_attr'], alignment=TA_CENTER)
    return s


# ============================================================
# CUSTOM FLOWABLES
# ============================================================

class GoldRule(Flowable):
    def __init__(self, width=60, height=3, color=BURGUNDY):
        Flowable.__init__(self)
        self.rule_width = width
        self.rule_height = height
        self.rule_color = color
        self.width = width
        self.height = height + 8

    def draw(self):
        self.canv.setFillColor(self.rule_color)
        self.canv.rect(0, 4, self.rule_width, self.rule_height, fill=1, stroke=0)


class CenteredGoldRule(Flowable):
    def __init__(self, width=60, height=3, color=GOLD, page_width=CONTENT_W):
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


class ChampagneLine(Flowable):
    def __init__(self, width=CONTENT_W, thickness=0.5, color=CHAMPAGNE):
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
            content = f'<b><font name="Outfit-SemiBold">{self.bold_label}</font></b> {self.text}'
        else:
            content = self.text
        self.para = Paragraph(content, self.styles['callout_body'])
        w, h = self.para.wrap(inner_w, 1000)
        self.para_height = h
        self.width = self.box_width
        self.height = h + 24

    def draw(self):
        self.canv.setFillColor(BURGUNDY)
        self.canv.rect(0, 0, 4, self.height, fill=1, stroke=0)
        self.para.drawOn(self.canv, 20, 12)


class FillInLine(Flowable):
    def __init__(self, label="", width=CONTENT_W, line_color=CHAMPAGNE):
        Flowable.__init__(self)
        self.label = label
        self.line_width = width
        self.line_color = line_color
        self.width = width
        self.height = 28

    def draw(self):
        if self.label:
            self.canv.setFont("Outfit-Light", 10)
            self.canv.setFillColor(MUTED_FG)
            self.canv.drawString(0, 14, self.label)
        self.canv.setStrokeColor(self.line_color)
        self.canv.setLineWidth(0.5)
        self.canv.line(0, 4, self.line_width, 4)


class NumberedFillLine(Flowable):
    def __init__(self, number, width=CONTENT_W, line_color=CHAMPAGNE):
        Flowable.__init__(self)
        self.number = number
        self.line_width = width
        self.line_color = line_color
        self.width = width
        self.height = 26

    def draw(self):
        self.canv.setFont("CormorantGaramond", 12)
        self.canv.setFillColor(BURGUNDY)
        self.canv.drawString(0, 8, f"{self.number:02d}")
        self.canv.setStrokeColor(self.line_color)
        self.canv.setLineWidth(0.5)
        self.canv.line(28, 4, self.line_width, 4)


# ============================================================
# PAGE DECORATION HANDLERS
# ============================================================

def _draw_footer(canvas, doc):
    """Shared footer for content and divider pages."""
    canvas.setFont("Outfit-Light", 8)
    canvas.setFillColor(MUTED_FG)
    canvas.drawString(MARGIN_L, 36, f"{doc.product_name}  |  {doc.website}")
    page_num = canvas.getPageNumber()
    canvas.drawRightString(PAGE_W - MARGIN_R, 36, f"{doc.handle}  |  {page_num}")


def draw_content_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(CHAMPAGNE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_L, PAGE_H - 36, PAGE_W - MARGIN_R, PAGE_H - 36)
    _draw_footer(canvas, doc)
    canvas.restoreState()


def draw_cover_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK_BG)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.75)
    cx, cy = MARGIN_L, PAGE_H - MARGIN_T + 20
    canvas.line(cx, cy, cx, cy + 50)
    canvas.line(cx, cy + 50, cx + 50, cy + 50)
    canvas.restoreState()


def draw_section_divider_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setStrokeColor(CHAMPAGNE)
    canvas.setLineWidth(0.5)
    canvas.line(MARGIN_L, PAGE_H * 0.35, PAGE_W - MARGIN_R, PAGE_H * 0.35)
    _draw_footer(canvas, doc)
    canvas.restoreState()


# ============================================================
# BRAND DOCUMENT (replaces SimpleDocTemplate + BrandPageHandler)
# ============================================================

def BrandDoc(output_path, product_name, website="theshipitsystem.com",
             handle="@unstuckwithmolly"):
    """Create a BaseDocTemplate with cover, content, and divider page templates.

    Usage:
        doc = BrandDoc("/path/to/output.pdf", "PRODUCT NAME")
        story = [...]
        doc.build(story)

    Section dividers automatically get the correct background — no manual
    page tracking needed.
    """
    frame = Frame(MARGIN_L, MARGIN_B, CONTENT_W, PAGE_H - MARGIN_T - MARGIN_B,
                  id='main')

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
               author_role="Build Partner for Side-Project Shippers",
               website="theshipitsystem.com", handle="@unstuckwithmolly",
               brand_line="THE SHIP IT SYSTEM",
               title_italic=False):
    story.append(Spacer(1, 60))
    story.append(Paragraph(
        brand_line,
        ParagraphStyle('cb', fontName='Outfit-SemiBold', fontSize=11, leading=14, textColor=GOLD, spaceAfter=20, letterSpacing=3)
    ))
    # Italic titles use the Italic variant — matches canonical headline pattern
    # ("text-primary italic font-light") for voice-driven, attitude-laden titles
    # like "Decide Already." Per brand-guide.md, italic ≠ bold.
    _title_font = 'CormorantGaramond-Italic' if title_italic else 'CormorantGaramond'
    story.append(Paragraph(title,
        ParagraphStyle('ct', fontName=_title_font, fontSize=52, leading=58, textColor=CREAM, spaceAfter=8)))
    story.append(GoldRule(width=60, height=3, color=GOLD))
    story.append(Spacer(1, 16))
    story.append(Paragraph(subtitle,
        ParagraphStyle('cs', fontName='CormorantGaramond-Italic', fontSize=18, leading=24, textColor=CREAM, spaceAfter=8)))
    story.append(Paragraph(description,
        ParagraphStyle('cd', fontName='Outfit-Light', fontSize=12, leading=18, textColor=CHAMPAGNE)))
    story.append(Spacer(1, 140))
    story.append(Paragraph(f'<font name="Outfit-SemiBold">{author_name}</font>',
        ParagraphStyle('ca', fontName='Outfit-SemiBold', fontSize=12, leading=16, textColor=ROSE_LIGHT, spaceAfter=2)))
    story.append(Paragraph(author_role,
        ParagraphStyle('cr', fontName='Outfit-Light', fontSize=10, leading=14, textColor=CHAMPAGNE, spaceAfter=2)))
    story.append(Paragraph(f'{website} | {handle}',
        ParagraphStyle('cu', fontName='Outfit-Light', fontSize=10, leading=14, textColor=MUTED_FG)))
    # Switch to content template for subsequent pages
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())


def title_page(story, styles, title, byline, dedication=None, bold_statement=None, copyright_text=None, title_italic=False):
    story.append(Spacer(1, 80))
    if title_italic:
        # Use italic variant for attitude-driven titles like "Decide Already."
        _title_style = ParagraphStyle('h1ci', parent=styles['h1_center'], fontName='CormorantGaramond-Italic')
        story.append(Paragraph(title, _title_style))
    else:
        story.append(Paragraph(title, styles['h1_center']))
    story.append(Paragraph(f'<i>{byline}</i>', styles['subtitle_italic_center']))
    story.append(CenteredGoldRule(width=60, height=3, color=GOLD))
    if dedication:
        story.append(Paragraph(f'<i>{dedication}</i>', styles['serif_italic_center']))
    if bold_statement:
        story.append(Spacer(1, 8))
        story.append(Paragraph(bold_statement, styles['burgundy_bold_center']))
    if copyright_text:
        story.append(Spacer(1, 80))
        story.append(Paragraph(copyright_text, styles['copyright']))
    story.append(PageBreak())


def section_divider(story, number, title, subtitle=None, handler=None):
    # Switch to divider template for this page
    story.append(NextPageTemplate('divider'))
    story.append(PageBreak())
    story.append(Spacer(1, 200))
    num_str = f"{number:02d}" if isinstance(number, int) else str(number)
    story.append(Paragraph(num_str,
        ParagraphStyle('dn', fontName='CormorantGaramond', fontSize=48, leading=52, textColor=BURGUNDY, alignment=TA_CENTER, spaceAfter=8)))
    story.append(Paragraph(title,
        ParagraphStyle('dt', fontName='CormorantGaramond', fontSize=32, leading=40, textColor=CHARCOAL, alignment=TA_CENTER, spaceAfter=8)))
    if subtitle:
        story.append(Paragraph(subtitle,
            ParagraphStyle('ds', fontName='Outfit-Light', fontSize=12, leading=18, textColor=MUTED_FG, alignment=TA_CENTER)))
    # Switch back to content for the next page
    story.append(NextPageTemplate('content'))
    story.append(PageBreak())


def make_table(data, col_widths=None, header_row=True):
    styles = get_styles()
    table_data = []
    for i, row in enumerate(data):
        cells = []
        for cell in row:
            style = styles['table_header'] if (i == 0 and header_row) else styles['table_cell']
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
        ('LINEBELOW', (0, 0), (-1, 0), 0.5, CHAMPAGNE),
        ('LINEBELOW', (0, 1), (-1, -1), 0.25, CHAMPAGNE),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            cmds.append(('BACKGROUND', (0, i), (-1, i), SAND))
    t.setStyle(TableStyle(cmds))
    return t


# ============================================================
# LEGACY SUPPORT (for existing scripts using SimpleDocTemplate)
# ============================================================

class BrandPageHandler:
    """Legacy handler for scripts using SimpleDocTemplate.

    For new scripts, use BrandDoc() + cover_page() instead — it handles page
    templates automatically. This class is kept for backward compatibility
    with the original ship-it PDF builders.
    """
    def __init__(self, doc):
        self.doc = doc
        self.divider_pages = set()
        self.cover_params = None

    def set_cover(self, title, subtitle, description,
                  brand_line="THE SHIP IT SYSTEM",
                  author_name="Molly Shelestak",
                  author_role="Build Partner for Side-Project Shippers",
                  website=None, handle=None):
        """Define cover-page text; drawn on the dark cover canvas in on_first_page."""
        self.cover_params = {
            "title": title,
            "subtitle": subtitle,
            "description": description,
            "brand_line": brand_line,
            "author_name": author_name,
            "author_role": author_role,
            "website": website or getattr(self.doc, "website", "theshipitsystem.com"),
            "handle": handle or getattr(self.doc, "handle", "@unstuckwithmolly"),
        }

    def set_divider_pages(self, pages):
        self.divider_pages = set(pages)

    def on_first_page(self, canvas, doc):
        draw_cover_page(canvas, doc)
        if self.cover_params:
            _draw_cover_text(canvas, self.cover_params)

    def on_later_pages(self, canvas, doc):
        page_num = canvas.getPageNumber()
        if page_num in self.divider_pages:
            draw_section_divider_page(canvas, doc)
        else:
            draw_content_page(canvas, doc)


def _draw_cover_text(canvas, p):
    """Render cover text overlay on the dark cover background.

    Mirrors the cover_page() story-helper layout for builders that drive the
    cover via canvas (BrandPageHandler.set_cover) rather than story flowables.
    """
    canvas.saveState()

    # Brand line — top, gold, letterspaced caps
    canvas.setFillColor(GOLD)
    canvas.setFont('Outfit-SemiBold', 11)
    canvas.drawString(MARGIN_L, PAGE_H - MARGIN_T - 40,
                      _letterspaced(p['brand_line'], 3))

    # Title — large serif, cream
    canvas.setFillColor(CREAM)
    canvas.setFont('CormorantGaramond', 52)
    title_y = PAGE_H - MARGIN_T - 110
    for line in _wrap_for_cover(canvas, p['title'], 'CormorantGaramond', 52,
                                 PAGE_W - MARGIN_L - MARGIN_R):
        canvas.drawString(MARGIN_L, title_y, line)
        title_y -= 58

    # Gold rule under title
    canvas.setFillColor(GOLD)
    canvas.rect(MARGIN_L, title_y + 18, 60, 3, fill=1, stroke=0)

    # Subtitle — italic cream
    canvas.setFillColor(CREAM)
    canvas.setFont('CormorantGaramond-Italic', 18)
    sub_y = title_y - 12
    for line in _wrap_for_cover(canvas, p['subtitle'], 'CormorantGaramond-Italic', 18,
                                 PAGE_W - MARGIN_L - MARGIN_R):
        canvas.drawString(MARGIN_L, sub_y, line)
        sub_y -= 24

    # Description — champagne caps
    canvas.setFillColor(CHAMPAGNE)
    canvas.setFont('Outfit-Light', 12)
    canvas.drawString(MARGIN_L, sub_y - 8, p['description'])

    # Author block — bottom-left
    canvas.setFillColor(ROSE_LIGHT)
    canvas.setFont('Outfit-SemiBold', 12)
    canvas.drawString(MARGIN_L, MARGIN_B + 50, p['author_name'])

    canvas.setFillColor(CHAMPAGNE)
    canvas.setFont('Outfit-Light', 10)
    canvas.drawString(MARGIN_L, MARGIN_B + 34, p['author_role'])

    canvas.setFillColor(MUTED_FG)
    canvas.drawString(MARGIN_L, MARGIN_B + 18,
                      f"{p['website']} | {p['handle']}")

    canvas.restoreState()


def _letterspaced(text, spacing):
    """Approximate letter-spacing by inserting hair spaces (cheap, no kerning math)."""
    sep = " " * (spacing // 2) if spacing else ""
    return sep.join(text)


def _wrap_for_cover(canvas, text, font, size, max_width):
    """Naive word-wrap for cover text using canvas.stringWidth."""
    canvas.setFont(font, size)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        candidate = (cur + " " + w).strip()
        if canvas.stringWidth(candidate, font, size) <= max_width:
            cur = candidate
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [text]
