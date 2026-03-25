"""Build the One-Page Launch Plan PDF matching Ship or Kill design."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from brand_pdf import *
from reportlab.platypus import Spacer, PageBreak, Paragraph, KeepTogether

OUTPUT = os.path.join(os.path.dirname(__file__), '..', 'one_page_launch_plan.pdf')

doc = BrandDoc(OUTPUT, "THE ONE-PAGE LAUNCH PLAN")

styles = get_styles()
story = []

# ============================================================
# PAGE 1: COVER (dark background)
# ============================================================
cover_page(
    story,
    title="The One-Page<br/>Launch Plan",
    subtitle="A Ship It System Workbook",
    description=(
        "Go from \u201cI have an idea\u201d to \u201cI have a plan\u201d in 15 minutes. "
        "The exact framework adapted from how product managers at top tech companies "
        "scope and greenlight million-dollar projects."
    ),
    author_name="Molly Shelestak",
    author_role="20 years in tech  |  Multiple businesses built & launched",
    website="theshipitsystem.com",
    handle="@unstuckwithmolly",
    brand_line="THE SHIP IT SYSTEM",
)

# ============================================================
# PAGE 2: Title/Intro page
# ============================================================
title_page(
    story, styles,
    title="The One-Page Launch Plan",
    byline="By Molly Shelestak",
    dedication=(
        "This is for the person with 47 ideas in their Notes app and zero launched products. "
        "Not because you\u2019re lazy \u2014 because nobody gave you a framework."
    ),
    bold_statement="Infrastructure, not aspiration.",
    copyright_text="\u00a9 2026 Molly Shelestak | theshipitsystem.com"
)

# ============================================================
# PAGE 3: Why This Works
# ============================================================
story.append(Paragraph("You Don\u2019t Have an Idea Problem.", styles['h2']))
story.append(Paragraph(
    '<font name="CormorantGaramond-Italic" size="20">You Have an Infrastructure Problem.</font>',
    styles['serif_italic']
))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "Here\u2019s what I\u2019ve learned in 20 years of building products that make real money:",
    styles['body']
))
story.append(Paragraph(
    "The difference between people who launch and people who don\u2019t isn\u2019t talent, "
    "motivation, or some magical entrepreneurial gene. It\u2019s that launchers have a "
    "system for turning a messy idea into a clear plan \u2014 and they do it FAST, "
    "before self-doubt and overthinking kick in.",
    styles['body']
))
story.append(Paragraph(
    "Product managers at companies like Google, Stripe, and Anthropic don\u2019t "
    "\u201cwing it.\u201d They use frameworks to evaluate, scope, and sequence ideas "
    "into shippable plans every single day. That\u2019s literally the job.",
    styles['body']
))
story.append(Paragraph(
    "I\u2019ve adapted the best of those frameworks into this single page.",
    styles['body_bold']
))
story.append(Spacer(1, 16))
story.append(ChampagneLine())
story.append(Spacer(1, 8))

story.append(Paragraph("HOW TO USE THIS:", styles['body_bold']))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">1.</font> Set a 15-minute timer. Seriously. Speed creates clarity.<br/>'
    '<font name="Outfit-SemiBold">2.</font> Fill in each section with the FIRST answer that comes to mind.<br/>'
    '<font name="Outfit-SemiBold">3.</font> Resist the urge to make it perfect. Perfection is a stall tactic.',
    styles['body']
))
story.append(Spacer(1, 8))
story.append(Paragraph("When you\u2019re done, you\u2019ll have:", styles['body']))
story.append(Paragraph(
    "\u2022 A clear, one-sentence description of what you\u2019re building<br/>"
    "\u2022 Your exact target customer (not \u201ceveryone\u201d)<br/>"
    "\u2022 A price point that makes sense<br/>"
    "\u2022 The 5 steps between you and a launched product<br/>"
    "\u2022 A realistic timeline that doesn\u2019t require quitting your job",
    styles['body']
))
story.append(Spacer(1, 8))
story.append(CalloutBox(
    "That\u2019s more progress than most people make in 6 months of \u201cthinking about it.\u201d "
    "Let\u2019s go. Your timer starts now.",
    styles, bold_label="Real talk:"
))
story.append(PageBreak())

# ============================================================
# PAGE 4: YOUR PLAN - The Worksheet
# ============================================================
story.append(Paragraph("Your Launch Plan", styles['h2']))
story.append(Paragraph(
    '<font name="Outfit-SemiBold" color="#763c47">15 MINUTES. ONE PAGE. TOTAL CLARITY.</font>',
    styles['burgundy_bold']
))
story.append(Spacer(1, 12))

# Section 01
story.append(Paragraph(
    '<font name="CormorantGaramond" size="16" color="#763c47">01</font>'
    '  <font name="Outfit-SemiBold" size="12">THE IDEA</font>'
    '  <font name="Outfit-Light" size="10" color="#5c4f46">(In One Sentence)</font>',
    styles['body']
))
story.append(Paragraph(
    "I\u2019m building _____________ that helps _____________ do/get/solve _____________.",
    styles['body']
))
story.append(FillInLine())
story.append(Paragraph(
    '<font name="Outfit-Light" size="9" color="#5c4f46">'
    'Force yourself into one sentence. If you can\u2019t explain it simply, you don\u2019t understand it yet.</font>',
    styles['small']
))
story.append(Spacer(1, 12))

# Section 02
story.append(Paragraph(
    '<font name="CormorantGaramond" size="16" color="#763c47">02</font>'
    '  <font name="Outfit-SemiBold" size="12">THE PERSON</font>'
    '  <font name="Outfit-Light" size="10" color="#5c4f46">(Your Exact Customer)</font>',
    styles['body']
))
story.append(Paragraph(
    "My ideal buyer is a _______ who is struggling with _______ and has already tried _______ "
    "but it didn\u2019t work because _______.",
    styles['body']
))
story.append(FillInLine())
story.append(FillInLine())
story.append(Paragraph(
    '<font name="Outfit-Light" size="9" color="#5c4f46">'
    '\u201cWomen aged 25-45\u201d is not a customer. \u201cA freelance photographer who\u2019s losing bookings '
    'because her Instagram grid doesn\u2019t show her actual range\u201d \u2014 THAT\u2019s a customer.</font>',
    styles['small']
))
story.append(Spacer(1, 12))

# Section 03
story.append(Paragraph(
    '<font name="CormorantGaramond" size="16" color="#763c47">03</font>'
    '  <font name="Outfit-SemiBold" size="12">THE PRICE</font>'
    '  <font name="Outfit-Light" size="10" color="#5c4f46">(What They\u2019ll Pay)</font>',
    styles['body']
))
story.append(Paragraph(
    "I\u2019ll charge $_______ because the cost of NOT solving this is $_______/year in lost revenue, "
    "wasted time, or missed opportunity.",
    styles['body']
))
story.append(FillInLine())
story.append(Paragraph(
    '<font name="Outfit-Light" size="9" color="#5c4f46">'
    'Don\u2019t underprice. If your thing saves someone 10 hours/month and their time is worth $50/hr, '
    'that\u2019s $6,000/year. A $97 product is a steal.</font>',
    styles['small']
))
story.append(PageBreak())

# ============================================================
# PAGE 5: Continued worksheet
# ============================================================
# Section 04
story.append(Paragraph(
    '<font name="CormorantGaramond" size="16" color="#763c47">04</font>'
    '  <font name="Outfit-SemiBold" size="12">THE FORMAT</font>'
    '  <font name="Outfit-Light" size="10" color="#5c4f46">(What They Actually Get)</font>',
    styles['body']
))
story.append(Paragraph(
    "Circle one: Digital Guide / Template Kit / Video Course / Workshop / Tool / Membership",
    styles['body']
))
story.append(Paragraph(
    '<font name="Outfit-Light" size="9" color="#5c4f46">'
    'Pick the simplest format that delivers the result. A $97 template kit that gets used beats a '
    '$497 course that collects dust. Ship fast > ship fancy.</font>',
    styles['small']
))
story.append(Spacer(1, 16))

# Section 05
story.append(Paragraph(
    '<font name="CormorantGaramond" size="16" color="#763c47">05</font>'
    '  <font name="Outfit-SemiBold" size="12">THE 5 STEPS</font>'
    '  <font name="Outfit-Light" size="10" color="#5c4f46">(Your Path to Launched)</font>',
    styles['body']
))
for i in range(1, 6):
    story.append(FillInLine(f"Step {i}: by ___/___"))
story.append(Paragraph(
    '<font name="Outfit-Light" size="9" color="#5c4f46">'
    'Not 47 steps. Five. If your plan needs more than five steps before the first dollar comes in, '
    'you\u2019re overbuilding. Strip it down.</font>',
    styles['small']
))
story.append(Spacer(1, 16))
story.append(CalloutBox(
    "You just did in 15 minutes what most people spend 6 months avoiding.",
    styles, bold_label="Done?"
))
story.append(PageBreak())

# ============================================================
# PAGE 6: GUT CHECK SCORECARD
# ============================================================
story.append(Paragraph("The Gut Check Scorecard", styles['h2']))
story.append(Paragraph(
    "Before you build anything, score your idea. Adapted from the RICE framework product managers "
    "use to decide which projects get resources. Circle your honest answer for each.",
    styles['body']
))
story.append(Spacer(1, 8))

# Scoring table
score_data = [
    ["FACTOR", "1", "2", "3", "4"],
    ["REACH\nHow many people have this problem?",
     "Basically just me", "A few hundred", "Thousands", "Tens of thousands+"],
    ["IMPACT\nHow painful is this problem?",
     "Mild annoyance", "Frustrating", "Costs them money/time", "Keeps them up at night"],
    ["CONFIDENCE\nHow sure are you people will pay?",
     "It\u2019s a hunch", "I\u2019ve seen demand", "People have asked for it", "People have tried to pay me"],
    ["EFFORT\nHow long to build a first version?",
     "6+ months", "2\u20133 months", "2\u20134 weeks", "A weekend"],
]

t = make_table(score_data, col_widths=[120, 85, 85, 85, 85])
story.append(t)
story.append(Spacer(1, 16))

story.append(Paragraph("YOUR SCORE: _____ / 16", styles['body_bold']))
story.append(Spacer(1, 8))

interp_data = [
    ["SCORE", "WHAT IT MEANS"],
    ["13\u201316", "Ship it. Now. Stop reading and go build."],
    ["9\u201312", "Strong idea. Needs minor refinement. Do customer conversations this week."],
    ["5\u20138", "Promising but risky. Validate before you build \u2014 talk to 10 people first."],
    ["4 or below", "Pivot. This isn\u2019t the one. Go back to your Launch Plan and try a different idea."],
]
t2 = make_table(interp_data, col_widths=[80, CONTENT_W - 80])
story.append(t2)
story.append(Spacer(1, 16))

story.append(CalloutBox(
    "A 9/16 idea that ships beats a 16/16 idea that lives in your Notes app forever. "
    "The plan you just made isn\u2019t precious. It\u2019s a starting point. The market will tell "
    "you what to fix. But it can\u2019t tell you anything if you never put it out there.",
    styles, bold_label="The truth nobody tells you:"
))
story.append(Spacer(1, 12))

story.append(Paragraph(
    '<font name="CormorantGaramond-Italic" size="14">'
    'The most expensive thing you own is an unlaunched idea.</font>',
    styles['quote_center']
))
story.append(PageBreak())

# ============================================================
# PAGE 7: CTA / Next Steps
# ============================================================
story.append(Spacer(1, 60))
story.append(Paragraph("Ready to Execute This Plan?", styles['h2_center']))
story.append(CenteredGoldRule(width=60, height=3, color=GOLD))
story.append(Spacer(1, 16))

story.append(Paragraph(
    '<font name="CormorantGaramond-Italic" size="16">'
    'The Ship It Kit has everything you need to go from \u201cI picked my idea\u201d '
    'to \u201cI have paying customers\u201d in 30 days.</font>',
    styles['quote_center']
))
story.append(Spacer(1, 16))

story.append(Paragraph("What\u2019s inside:", styles['body_bold_center']))
story.append(Paragraph(
    "\u2022 <font name='Outfit-SemiBold'>The Ship It Playbook</font> \u2014 60+ page step-by-step guide<br/>"
    "\u2022 <font name='Outfit-SemiBold'>12 templates</font> \u2014 Fill-in-the-blank. No blank pages.<br/>"
    "\u2022 <font name='Outfit-SemiBold'>3 case study teardowns</font> \u2014 Real launches, real revenue<br/>"
    "\u2022 <font name='Outfit-SemiBold'>Private podcast</font> \u2014 5 episodes, 15\u201320 min each<br/>"
    "\u2022 <font name='Outfit-SemiBold'>30-day timeline</font> \u2014 Day by day, nothing forgotten",
    styles['body_center']
))
story.append(Spacer(1, 20))

story.append(Paragraph(
    '<font name="Outfit-SemiBold" color="#763c47" size="14">theshipitsystem.com</font>',
    ParagraphStyle('cta', fontName='Outfit-SemiBold', fontSize=14, textColor=BURGUNDY, alignment=TA_CENTER, spaceAfter=24)
))

story.append(Spacer(1, 40))
story.append(Paragraph(
    "You did the hard part \u2014 you decided. Now go build it.",
    styles['body_center']
))
story.append(Paragraph(
    "\u2014 Molly",
    styles['body_center']
))
story.append(Spacer(1, 16))
story.append(Paragraph(
    '<font name="Outfit-Medium" color="#5c4f46">Infrastructure, not aspiration.</font>',
    ParagraphStyle('tagline', fontName='Outfit-Medium', fontSize=11, textColor=MUTED_FG, alignment=TA_CENTER)
))

# ============================================================
# BUILD
# ============================================================
doc.build(story)
print(f"Built: {OUTPUT}")
