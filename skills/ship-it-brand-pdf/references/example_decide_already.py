"""Build the Decide Already PDF workbook matching Ship or Kill design."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from brand_pdf import *
from reportlab.platypus import Spacer, PageBreak, Paragraph, KeepTogether
from reportlab.lib.enums import TA_CENTER

# Output to the canonical lead-magnet location in ship-it-system repo.
# (Falls back to local references/.. path if the canonical dir isn't present.)
_CANONICAL = os.path.expanduser('~/github/ship-it-system/01_Lead_Magnets/decide_already.pdf')
OUTPUT = _CANONICAL if os.path.isdir(os.path.dirname(_CANONICAL)) else os.path.join(os.path.dirname(__file__), '..', 'decide_already.pdf')

doc = BrandDoc(OUTPUT, "DECIDE ALREADY")

S = get_styles()
story = []

# ============================================================
# COVER
# ============================================================
cover_page(story,
    title_italic=True,
    title="Decide Already.",
    subtitle="A Ship It System Workbook",
    description=(
        "The scoring framework that turns \u201cI have too many ideas\u201d "
        "into one clear, defensible decision \u2014 in under 3 hours."
    ),
    brand_line="THE SHIP IT SYSTEM",
)

# ============================================================
# TITLE PAGE
# ============================================================
title_page(story, S, title_italic=True,
    title="Decide Already.",
    byline="By Molly Shelestak",
    dedication=(
        "This workbook is for the person who has between 3 and 47 ideas "
        "and hasn\u2019t started any of them. Not because you\u2019re lazy \u2014 "
        "because you\u2019re stuck in the decision loop."
    ),
    bold_statement="Infrastructure, not aspiration.",
    copyright_text="\u00a9 2026 Molly Shelestak | theshipitsystem.com"
)

# ============================================================
# TABLE OF CONTENTS
# ============================================================
story.append(Paragraph("What\u2019s Inside This Workbook", S['h2_center']))
story.append(CenteredGoldRule(width=60, height=3, color=GOLD))
story.append(Spacer(1, 16))

toc_data = [
    ["SECTION", "TOPIC", "TIME"],
    ["01", "The Decision Problem \u2014 Why you\u2019re stuck", "5 min"],
    ["02", "The Idea Dump \u2014 Get every idea out of your head", "15 min"],
    ["03", "The SHIP Score \u2014 Score each idea on 4 factors", "60 min"],
    ["04", "The Reality Check \u2014 Stress-test your top scorer", "30 min"],
    ["05", "The Decision \u2014 Lock it in. Build the anti-regret protocol.", "15 min"],
    ["06", "What Comes Next \u2014 Your first 3 moves", "5 min"],
]
t = make_table(toc_data, col_widths=[60, 300, 108])
story.append(t)
story.append(Spacer(1, 16))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">Total time: 2\u20133 hours</font>',
    S['body_center']
))
story.append(Spacer(1, 12))
story.append(CalloutBox(
    "You don\u2019t need to do this in one sitting. But you do need to finish it. "
    "Half-scored ideas are worse than unscored ones \u2014 they give you the illusion "
    "of progress without an actual decision.",
    S
))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "How to use this workbook: Print it or fill it out digitally. Answer every question \u2014 "
    "don\u2019t skip the ones that feel uncomfortable. The uncomfortable ones are usually the "
    "most important. When you get to the scoring section, be brutally honest. A low "
    "score isn\u2019t failure \u2014 it\u2019s intelligence.",
    S['small']
))
story.append(PageBreak())

# ============================================================
# SECTION 01: The Decision Problem
# ============================================================
section_divider(story, 1, "The Decision Problem", "Why you\u2019re stuck \u2014 and why it\u2019s not a character flaw")

story.append(Paragraph(
    "Let me guess. You have between 3 and 47 ideas for things you could build. Some of them have been "
    "living in your Notes app for months. A few have purchased domain names. One has a half-finished "
    "Canva logo.",
    S['body']
))
story.append(Paragraph(
    "And you haven\u2019t started any of them. Not because you\u2019re lazy \u2014 you\u2019re clearly not, "
    "because lazy people don\u2019t buy workbooks about decision-making. You haven\u2019t started because "
    "you\u2019re stuck in the Decision Loop:",
    S['body']
))
story.append(Spacer(1, 8))

# Decision Loop
loop_items = [
    "1. Get excited about an idea \u2192",
    "2. Start researching it \u2192",
    "3. Think of a \u201cbetter\u201d idea \u2192",
    "4. Switch to the new idea \u2192",
    "5. Get overwhelmed by options \u2192",
    "6. Do nothing \u2192",
    "7. Feel guilty about doing nothing \u2192",
    "8. Go back to Step 1 \u25a0",
]
for item in loop_items:
    story.append(Paragraph(item, ParagraphStyle('loop', fontName='Outfit-Light', fontSize=10, leading=16, textColor=CHARCOAL, leftIndent=24)))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<font name="CormorantGaramond-Italic" size="14">Sound familiar? Good. That means this workbook is for you.</font>',
    S['serif_italic']
))
story.append(Spacer(1, 16))

# Three Decision Killers
story.append(Paragraph("The Three Decision Killers", S['h3']))
story.append(Spacer(1, 4))

story.append(Paragraph(
    '<font name="Outfit-SemiBold">The Opportunity Cost Trap.</font> '
    'You\u2019re so afraid of picking the wrong idea that you pick no idea. But here\u2019s the math '
    'most people ignore: the cost of NOT choosing is always higher than the cost of choosing imperfectly. '
    'Every month you spend deliberating is a month of zero revenue, zero learning, and zero momentum. '
    'A \u201cwrong\u201d idea that you actually ship still teaches you more than a \u201cperfect\u201d idea '
    'that lives in your Notes app forever.',
    S['body']
))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">The Passion Myth.</font> '
    'You\u2019ve been told to \u201cfollow your passion.\u201d So you\u2019re waiting for an idea that makes '
    'your heart sing every time you think about it. That\u2019s not how products work. Products are built on '
    'problems \u2014 other people\u2019s problems. Your job is to find a painful problem, in a market that can pay, '
    'that you\u2019re qualified to solve. Competence + market demand will outperform passion + no strategy every single time.',
    S['body']
))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">The Perfectionism Disguise.</font> '
    '\u201cI\u2019m just doing more research\u201d is procrastination in a lab coat. At some point, more information '
    "doesn\u2019t improve the decision \u2014 it delays it. You will never have 100% certainty. What you can have "
    "is a framework that gives you 80% confidence. That\u2019s what the SHIP Score does.",
    S['body']
))
story.append(Spacer(1, 8))
story.append(CalloutBox(
    "You don\u2019t need more ideas. You don\u2019t need more inspiration. You need a "
    "scoring system and the guts to commit to whatever comes out on top. That\u2019s what "
    "the next 5 sections give you.",
    S, bold_label="Real talk:"
))
story.append(PageBreak())

# ============================================================
# SECTION 02: The Idea Dump
# ============================================================
section_divider(story, 2, "The Idea Dump", "Get every idea out of your head and onto paper")

story.append(Paragraph(
    "Before we can score anything, we need to see the full list. Every idea you\u2019ve been carrying around \u2014 "
    "the serious ones, the silly ones, the \u201cmaybe someday\u201d ones. Write them ALL down. Don\u2019t edit. "
    "Don\u2019t judge. Just dump.",
    S['body']
))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">Set a timer for 10 minutes.</font> Write every product, business, or project idea '
    "you\u2019ve considered in the last 12 months. One idea per line. Go.",
    S['body']
))
story.append(Spacer(1, 8))
story.append(Paragraph("MY IDEA DUMP", S['burgundy_bold']))
for i in range(1, 16):
    story.append(NumberedFillLine(i))
story.append(PageBreak())

# Gut-Check Filter
story.append(Paragraph("THE GUT-CHECK FILTER", S['burgundy_bold']))
story.append(Paragraph(
    "Now go back through your list. For each idea, ask these three elimination questions. "
    "If the answer to ANY of them is \u201cyes,\u201d cross the idea out. Be ruthless.",
    S['body']
))
story.append(Spacer(1, 8))

filters = [
    ("\u201cWould I need to quit my job to make this work?\u201d", 
     "If it requires full-time effort before it can generate revenue, it\u2019s not a side-project product. Cross it out."),
    ("\u201cWould it take more than 30 days to build a sellable version?\u201d",
     "If v1 requires months of development, you\u2019re thinking too big for a first product. Cross it out."),
    ("\u201cAm I the only person on earth who wants this?\u201d",
     "If you can\u2019t name 10 real people who have this problem, it\u2019s a hobby project, not a business. Cross it out."),
]
for question, explanation in filters:
    story.append(Paragraph(f'<font name="Outfit-SemiBold">{question}</font> \u2014 {explanation}', S['body']))

story.append(Spacer(1, 12))
story.append(CalloutBox(
    "After filtering, you should have 3\u20135 surviving ideas. If you have more than 5, "
    "apply the gut-check filter more aggressively. If you have fewer than 3, your filter "
    "might be too strict. The SHIP Score needs at least 3 ideas to be useful.",
    S
))
story.append(Spacer(1, 16))

story.append(Paragraph("MY TOP IDEAS (survivors only)", S['burgundy_bold']))
story.append(Paragraph("Write your surviving ideas below. These are the ones we\u2019re scoring.", S['body']))
for label in ["IDEA A", "IDEA B", "IDEA C", "IDEA D", "IDEA E"]:
    story.append(FillInLine(f"{label}:"))
story.append(PageBreak())

# ============================================================
# SECTION 03: The SHIP Score
# ============================================================
section_divider(story, 3, "The SHIP Score", "Score each idea on 4 factors. Math, not vibes.")

story.append(Paragraph(
    "The SHIP Score is adapted from RICE \u2014 the framework product managers use to prioritize features at "
    "companies like Google, Stripe, and Heap. I\u2019ve rebuilt it for side-project decisions.",
    S['body']
))
story.append(Spacer(1, 4))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">S</font> = Size \u2014 How big is the market?<br/>'
    '<font name="Outfit-SemiBold">H</font> = Hurt \u2014 How painful is the problem?<br/>'
    '<font name="Outfit-SemiBold">I</font> = Implementation \u2014 How fast can YOU build a sellable v1?<br/>'
    '<font name="Outfit-SemiBold">P</font> = Profit Path \u2014 Clear path to money within 90 days?',
    S['body']
))
story.append(Paragraph(
    "Each factor is scored 1\u20135. Then we multiply S \u00d7 H \u00d7 I \u00d7 P for a total SHIP Score. "
    "Highest score wins.",
    S['body']
))
story.append(Spacer(1, 8))

# S = SIZE rubric
story.append(Paragraph("S = SIZE  |  \u201cHow many people have this problem?\u201d", S['body_bold']))
s_data = [
    ["SCORE", "MARKET SIZE", "WHAT IT LOOKS LIKE"],
    ["1", "Tiny niche", "Fewer than 1,000 potential buyers. Hard to find them."],
    ["2", "Small niche", "1,000\u201310,000 potential buyers. 1\u20132 online communities."],
    ["3", "Solid niche", "10,000\u201350,000 potential buyers. Multiple communities, subreddits."],
    ["4", "Large market", "50,000\u2013500,000 potential buyers. Established industry."],
    ["5", "Massive market", "500,000+ potential buyers. Everyone knows someone with this problem."],
]
story.append(make_table(s_data, col_widths=[50, 90, 328]))
story.append(Spacer(1, 12))

# H = HURT rubric
story.append(Paragraph("H = HURT  |  \u201cHow painful is this problem?\u201d", S['body_bold']))
h_data = [
    ["SCORE", "PAIN LEVEL", "WHAT IT LOOKS LIKE"],
    ["1", "Mild annoyance", "They notice it but don\u2019t lose sleep over it."],
    ["2", "Recurring friction", "Bothers them weekly. They complain but haven\u2019t paid to fix it."],
    ["3", "Active problem", "They\u2019ve searched for solutions. Tried free options. Still not solved."],
    ["4", "Costly problem", "Costs them real money, time, or missed opportunities. They\u2019d pay today."],
    ["5", "Hair on fire", "Desperately searching. Revenue, career, or sanity depends on it."],
]
story.append(make_table(h_data, col_widths=[50, 100, 318]))
story.append(PageBreak())

# I = IMPLEMENTATION rubric
story.append(Paragraph("I = IMPLEMENTATION  |  \u201cHow fast can you build a sellable v1?\u201d", S['body_bold']))
i_data = [
    ["SCORE", "BUILD TIME", "WHAT IT LOOKS LIKE"],
    ["1", "3+ months", "Requires custom development, new skills, or complex production."],
    ["2", "6\u201312 weeks", "Doable but requires significant learning curve."],
    ["3", "4\u20136 weeks", "You have most skills needed. Focused evening/weekend work."],
    ["4", "2\u20133 weeks", "You already know how. Mostly assembling what you know."],
    ["5", "Under 2 weeks", "You could build this in a sprint. Templates and resources you already have."],
]
story.append(make_table(i_data, col_widths=[50, 90, 328]))
story.append(Spacer(1, 12))

# P = PROFIT PATH rubric
story.append(Paragraph("P = PROFIT PATH  |  \u201cCan you make money within 90 days?\u201d", S['body_bold']))
p_data = [
    ["SCORE", "REVENUE PATH", "WHAT IT LOOKS LIKE"],
    ["1", "Unclear", "Need to build an audience first. No obvious buyer."],
    ["2", "Possible", "You can imagine a buyer, but need to test."],
    ["3", "Probable", "People already pay for similar things. Competitors exist."],
    ["4", "Strong", "You know exactly who would buy. You could name 10 people."],
    ["5", "Near-certain", "People have already asked you for this. Or you\u2019ve been giving it away free."],
]
story.append(make_table(p_data, col_widths=[50, 100, 318]))
story.append(Spacer(1, 12))

story.append(CalloutBox(
    "If you\u2019re waffling between two scores, go with the lower one. Optimism "
    "is the #1 killer of product decisions. Score what IS \u2014 not what you hope will be true.",
    S, bold_label="Scoring tip:"
))
story.append(PageBreak())

# SHIP Score Worksheets
story.append(Paragraph("SHIP Score Worksheets", S['h2']))
story.append(Paragraph("Complete one worksheet per surviving idea. Be honest. Then calculate.", S['body']))
story.append(Spacer(1, 8))

for label in ["IDEA A", "IDEA B", "IDEA C"]:
    story.append(Paragraph(f'<font name="Outfit-SemiBold" color="#763c47">{label}:</font>', S['burgundy_bold']))
    story.append(FillInLine("Describe the idea in one sentence:"))
    story.append(Spacer(1, 4))
    ws_data = [
        ["FACTOR", "SCORE (1\u20135)", "WHY? (1 sentence)"],
        ["S = Size", "", ""],
        ["H = Hurt", "", ""],
        ["I = Implementation", "", ""],
        ["P = Profit Path", "", ""],
    ]
    story.append(make_table(ws_data, col_widths=[120, 80, 268]))
    story.append(Paragraph(f"TOTAL SHIP SCORE: S (___) \u00d7 H (___) \u00d7 I (___) \u00d7 P (___) = _______", S['body_bold']))
    story.append(Spacer(1, 16))

story.append(PageBreak())

# Ideas D & E
for label in ["IDEA D", "IDEA E"]:
    story.append(Paragraph(f'<font name="Outfit-SemiBold" color="#763c47">{label}:</font>', S['burgundy_bold']))
    story.append(FillInLine("Describe the idea in one sentence:"))
    story.append(Spacer(1, 4))
    ws_data = [
        ["FACTOR", "SCORE (1\u20135)", "WHY? (1 sentence)"],
        ["S = Size", "", ""],
        ["H = Hurt", "", ""],
        ["I = Implementation", "", ""],
        ["P = Profit Path", "", ""],
    ]
    story.append(make_table(ws_data, col_widths=[120, 80, 268]))
    story.append(Paragraph(f"TOTAL SHIP SCORE: S (___) \u00d7 H (___) \u00d7 I (___) \u00d7 P (___) = _______", S['body_bold']))
    story.append(Spacer(1, 16))

# Scoreboard
story.append(Paragraph("THE SCOREBOARD", S['burgundy_bold']))
story.append(Paragraph("Rank your ideas from highest to lowest SHIP Score.", S['body']))
sb_data = [
    ["RANK", "IDEA", "S", "H", "I", "P", "TOTAL"],
    ["1st", "", "", "", "", "", ""],
    ["2nd", "", "", "", "", "", ""],
    ["3rd", "", "", "", "", "", ""],
    ["4th", "", "", "", "", "", ""],
    ["5th", "", "", "", "", "", ""],
]
story.append(make_table(sb_data, col_widths=[50, 140, 50, 50, 50, 50, 78]))
story.append(Spacer(1, 12))

interp = [
    ["SCORE", "INTERPRETATION"],
    ["250+", "Strong candidate. Proceed to the Reality Check with confidence."],
    ["100\u2013249", "Decent but not obvious. The Reality Check will help you decide."],
    ["Under 100", "Weak signal. Don\u2019t build this first. It might make a great second product."],
]
story.append(make_table(interp, col_widths=[80, 388]))
story.append(Spacer(1, 8))
story.append(CalloutBox(
    "What if two ideas are within 50 points of each other? Go with the one that scores higher on "
    "Implementation. The fastest path to revenue teaches you the most. You can always build the other "
    "idea later \u2014 with the skills, confidence, and cash flow from shipping the first one.",
    S
))
story.append(PageBreak())

# ============================================================
# SECTION 04: The Reality Check
# ============================================================
section_divider(story, 4, "The Reality Check", "Stress-test your top scorer before you commit")

story.append(Paragraph(
    "Your SHIP Score gave you a frontrunner. Good. But a score isn\u2019t a decision \u2014 it\u2019s a hypothesis. "
    "Before you commit, run your top idea through these four stress tests.",
    S['body']
))
story.append(FillInLine("MY TOP IDEA:"))
story.append(Spacer(1, 12))

# Test 1
story.append(Paragraph("TEST 1: The 10 Real People Test", S['body_bold']))
story.append(Paragraph(
    "Can you name 10 specific, real humans who have this problem? Not categories of people \u2014 actual names.",
    S['body']
))
for i in range(1, 11):
    story.append(NumberedFillLine(i))
story.append(Paragraph("RESULT:  \u25a1 PASS (named 10)     \u25a1 FAIL (couldn\u2019t reach 10)", S['body']))
story.append(PageBreak())

# Test 2
story.append(Paragraph("TEST 2: The Saturday Morning Test", S['body_bold']))
story.append(Paragraph(
    "Imagine it\u2019s Saturday morning. You have 3 unscheduled hours. Would you spend those hours working "
    "on this product \u2014 not because you \u201cshould,\u201d but because the problem genuinely interests you?",
    S['body']
))
story.append(Paragraph(
    "This isn\u2019t about passion. It\u2019s about sustainability. If you dread working on it before you\u2019ve even started, "
    "you won\u2019t finish it.",
    S['small']
))
story.append(Paragraph("Honest answer:  \u25a1 Yes, I\u2019d genuinely choose this     \u25a1 No, I\u2019d find an excuse", S['body']))
story.append(Spacer(1, 16))

# Test 3
story.append(Paragraph("TEST 3: The Boring Middle Test", S['body_bold']))
story.append(Paragraph(
    "Every product has a boring middle \u2014 the unglamorous work between the exciting idea and the exciting launch. "
    "What\u2019s the boring middle of your top idea?",
    S['body']
))
story.append(FillInLine("The boring middle of this product is:"))
story.append(FillInLine())
story.append(Paragraph("Can I grind through this?  \u25a1 Yes     \u25a1 No \u2014 and that\u2019s important information", S['body']))
story.append(Spacer(1, 16))

# Test 4
story.append(Paragraph("TEST 4: The First $500 Test", S['body_bold']))
story.append(Paragraph(
    "Map out the realistic path to your first $500 in revenue from this product.",
    S['body']
))
story.append(FillInLine("My price point: $"))
story.append(FillInLine("Sales needed for $500:"))
story.append(FillInLine("Where will I find these buyers?"))
story.append(FillInLine("How will I reach them?"))
story.append(FillInLine("Realistic timeline to first sale:"))
story.append(Paragraph("Is the path clear?  \u25a1 Yes \u2014 I can see how to get there     \u25a1 No \u2014 it\u2019s fuzzy", S['body']))
story.append(Spacer(1, 12))

# Results
story.append(Paragraph("REALITY CHECK RESULTS:", S['burgundy_bold']))
results_data = [
    ["PASSES", "VERDICT"],
    ["4 passes", "You\u2019ve got your product. Move to Section 5."],
    ["3 passes", "Proceed with awareness. The failed test tells you where to de-risk first."],
    ["2 or fewer", "Go back to the Scoreboard. Your #2 idea might be a better fit."],
]
story.append(make_table(results_data, col_widths=[80, 388]))
story.append(PageBreak())

# ============================================================
# SECTION 05: The Decision
# ============================================================
section_divider(story, 5, "The Decision", "Lock it in. Write it down. Build the anti-regret protocol.")

story.append(Paragraph(
    "This is the page that matters. Everything before this was analysis. This is commitment.",
    S['body']
))
story.append(Paragraph(
    '<font name="CormorantGaramond-Italic" size="14">'
    'Write your decision in ink if you printed this. Not pencil. Ink. Because you\u2019re not going back.</font>',
    S['serif_italic']
))
story.append(Spacer(1, 12))

story.append(Paragraph("MY DECISION", S['burgundy_bold']))
story.append(FillInLine("I am building:"))
story.append(FillInLine("It helps [specific person] do/get/solve [specific outcome]:"))
story.append(FillInLine())
story.append(FillInLine("My SHIP Score was: _____ and it passed ___ /4 Reality Checks."))
story.append(FillInLine("I chose this because:"))
story.append(FillInLine())
story.append(Spacer(1, 4))
story.append(Paragraph("The format will be:", S['body']))
story.append(Paragraph(
    "\u25a1 Template kit     \u25a1 Digital guide     \u25a1 Video course     \u25a1 Workshop     \u25a1 Tool     \u25a1 Other: _________",
    S['body']
))
story.append(FillInLine("My price point: $"))
story.append(FillInLine("My deadline to ship v1: ___/___/______"))
story.append(Spacer(1, 16))

# Anti-Regret Protocol
story.append(Paragraph("THE ANTI-REGRET PROTOCOL", S['burgundy_bold']))
story.append(Paragraph(
    "Doubt will come. Not today \u2014 today you feel good about your decision. But in 2 weeks, "
    "when you\u2019re in the boring middle, you\u2019ll start wondering if you picked the wrong idea.",
    S['body']
))
story.append(Spacer(1, 4))

story.append(Paragraph(
    '<font name="Outfit-SemiBold">The 48-Hour Rule:</font> When doubt hits, do NOT switch ideas for 48 hours. '
    "Write down the doubt, set a timer, and keep building. 90% of the time, the doubt passes.",
    S['body']
))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">The Sunk Cost Reframe:</font> The work you\u2019ve already done isn\u2019t wasted '
    "if you switch \u2014 BUT the momentum you\u2019ve built IS lost. Starting over resets everything.",
    S['body']
))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">The \u201cIs This Actually Better?\u201d Test:</font> If you\u2019re considering switching, '
    "score the new idea with SHIP right now. If it doesn\u2019t score at least 20% higher, it\u2019s not worth the switch. "
    "It\u2019s just novelty.",
    S['body']
))
story.append(Spacer(1, 12))

story.append(Paragraph(
    '<font name="CormorantGaramond-Italic" size="14">'
    '\u201cThe best idea in the world is worthless until it ships. A decent idea that ships beats '
    'a brilliant idea that doesn\u2019t \u2014 every single time.\u201d</font>',
    S['quote_center']
))
story.append(Paragraph("\u2014 Molly Shelestak", S['quote_attr_center']))
story.append(PageBreak())

# ============================================================
# SECTION 06: What Comes Next
# ============================================================
section_divider(story, 6, "What Comes Next", "You decided. Here\u2019s your first 3 moves.")

story.append(Paragraph(
    "You now have something 94% of aspiring entrepreneurs don\u2019t: a clear, scored, defensible decision "
    "about what to build. Not a vibe. Not a hunch. A decision backed by a framework.",
    S['body']
))
story.append(Paragraph(
    "But a decision without a build plan is just a nicer version of an idea in your Notes app.",
    S['body_bold']
))
story.append(Spacer(1, 8))

story.append(Paragraph("YOUR NEXT 48 HOURS", S['burgundy_bold']))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">Tell someone.</font> Text a friend, post in a community, reply to my email \u2014 '
    "tell one person what you\u2019re building. Stating your decision out loud makes it real. It also makes quitting harder. "
    "That\u2019s the point.",
    S['body']
))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">Validate with 5 conversations.</font> Find 5 of those 10 people from your Reality Check '
    'and ask them one question: \u201cIf I built [your product] for [your price], would you buy it?\u201d '
    'Not \u201cwould you use it\u201d \u2014 would you buy it. The word \u2018buy\u2019 changes the answer.',
    S['body']
))
story.append(Paragraph(
    '<font name="Outfit-SemiBold">Set your ship date.</font> Open your calendar. Count 30 days from today. '
    "Block that date. Write \u201cLAUNCH DAY\u201d on it.",
    S['body']
))
story.append(Spacer(1, 24))

# CTA
story.append(ChampagneLine())
story.append(Spacer(1, 16))
story.append(Paragraph("Ready to Execute Your Decision?", S['h2_center']))
story.append(CenteredGoldRule(width=60, height=3, color=GOLD))
story.append(Spacer(1, 8))

story.append(Paragraph(
    '<font name="CormorantGaramond-Italic" size="14">'
    "Decide Already gave you the decision. But a decision is Day 1. You still need to validate, scope, "
    "build, set up your landing page, wire your email system, and launch. That\u2019s Days 2 through 30.</font>",
    S['quote_center']
))
story.append(Spacer(1, 12))

story.append(Paragraph(
    '<font name="Outfit-SemiBold">THE SHIP IT SYSTEM \u2014 $199 ($159 launch)</font>',
    S['burgundy_bold_center']
))
story.append(Paragraph(
    "Everything you need to go from \u201cI picked my idea\u201d to first sale by Day 30, PMF by Day 60, and a "
    "mapped path to $10K MRR by Day 90.",
    S['body_center']
))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "\u2022 <font name='Outfit-SemiBold'>The Ship It Kit</font> ($149 standalone) \u2014 150+ page playbook, 90-day arc<br/>"
    "\u2022 <font name='Outfit-SemiBold'>20 templates</font> \u2014 Fill-in-the-blank decision frameworks<br/>"
    "\u2022 <font name='Outfit-SemiBold'>Marketing OS</font> ($79 standalone) \u2014 25 AI skills that draft your landing pages, emails, ads<br/>"
    "\u2022 <font name='Outfit-SemiBold'>AI Build Partner</font> (free) \u2014 conversational coach in Claude.ai<br/>"
    "\u2022 <font name='Outfit-SemiBold'>Save $29</font> \u2014 vs buying Kit + Marketing OS separately ($228)",
    S['body_center']
))
story.append(Spacer(1, 16))
story.append(Paragraph(
    '<font name="Outfit-SemiBold" color="#763c47" size="14">theshipitsystem.com</font>',
    ParagraphStyle('cta', fontName='Outfit-SemiBold', fontSize=14, textColor=BURGUNDY, alignment=TA_CENTER, spaceAfter=16)
))
story.append(Spacer(1, 16))
story.append(Paragraph("You did the hard part \u2014 you decided. Now go build it.", S['body_center']))
story.append(Paragraph("\u2014 Molly", S['body_center']))
story.append(Spacer(1, 8))
story.append(Paragraph(
    '<font name="Outfit-Medium" color="#5c4f46">Infrastructure, not aspiration.</font>',
    ParagraphStyle('tag', fontName='Outfit-Medium', fontSize=11, textColor=MUTED_FG, alignment=TA_CENTER)
))

# ============================================================
# BUILD
# ============================================================
doc.build(story)
print(f"Built: {OUTPUT}")
