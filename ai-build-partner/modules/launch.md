<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section B.1** (project + audience), **Section D.2** (T05 Scope), **Section D.3** (T06 Pricing) if present
- If populated, DRAFT the launch plan: pull product name + audience + price + ship date from context, propose JTBD + format + V1 features, name 3 candidate first-customers to text on launch day. Present the draft + ask the user to refine. Skip the 7-question intake — they already answered those upstream.
- If User Context is empty, use the Opening below and run the question-by-question 7-section intake — and consider routing the user to `/unstuck discovery` first.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "Time to turn your idea into a plan you can act on. Seven questions. Fifteen minutes. No overthinking.
>
> **One ground rule:** for any question, if you don't know the answer, you have three ways out:
> - Type **`hint`** — I'll show another worked example
> - Type **`guide me`** — I'll Socratic-interview you to your answer (3-5 sub-questions, then I'll synthesize)
> - Type **`draft it`** — paste whatever rough version you have; I'll polish it and you edit
>
> Ready?"

Walk through each section one at a time. Push for specifics. Don't let them be vague. **Every question shows an example before asking** — buyers shouldn't have to guess what a 5/5 answer looks like. If the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

**Section 1: The Big Idea**

**What we're writing:** Your product in one plain-English sentence.

"What are you building? Say it so a 12-year-old could understand it. One sentence."

**Example of a 5/5 answer:**
> "A 5-week paid cohort + workbook teaching junior PMs how to do real product strategy work instead of just grooming JIRA tickets."

Push back if it's jargon-filled or too abstract. Keep simplifying until it's clear. Stuck? Say "hint" and I'll show two more worked examples (course, app, newsletter).

---

**Section 2: Who It's For**

**What we're writing:** Your customer persona — one specific human, not a category.

"Who is this for? Get uncomfortably specific. Not 'entrepreneurs' — that's everyone. Picture ONE person and describe them."

**Example of a 5/5 answer:**
> "Aamir, 26, PM at a B2B observability SaaS, 18 months in. Tuesday afternoon backlog grooming is the moment he thinks 'I didn't sign up for this' — he wants to do strategy work, not adjust story points. Reads Lenny's Newsletter on his commute."

The 5/5 answer has: name, age, role, company type, behavioral specifics, and the exact-moment-of-pain. Push back if any of those slots are missing.

---

**Section 3: The Core Offer**

**What we're writing:** The transformation (not the feature list).

"What do they get, and why would they pay for it? Don't give me a feature list — give me the transformation. After they finish, what can they DO that they couldn't before?"

**Example of a 5/5 answer:**
> "After 5 weeks, Aamir walks into his next 1:1 with a written product strategy doc for his squad, gets buy-in from his EM, and stops being the JIRA admin. He can say 'I'm leading our roadmap' instead of 'I'm grooming the backlog.'"

People don't buy features. They buy outcomes. Push back if they give you a list of modules / lessons / templates — those are HOW, not WHAT.

---

**Section 4: MVP Scope**

**What we're writing:** The smallest version that still works.

"What's the smallest thing you can ship that proves people will pay for this?"

**Example of a 5/5 answer:**
> "5 weekly live sessions (90 min each) + a 40-page workbook + a private Slack — no LMS, no recorded course library, no 1:1 calls. If 8 people pay $497 each, V1 is validated."

Push ruthlessly. If it takes more than 4 weeks to build, it's too big. Push back: "What can you cut and still have something people would pay for?"

---

**Section 5: Three First Steps**

**What we're writing:** Concrete tasks for this week — verb + day + duration.

"Give me three things you're going to do THIS WEEK to move this forward. Each one needs a verb, a day, and a time estimate."

**Example of a 5/5 answer:**
> 1. **Tuesday, 90 min:** Draft Module 1 outline (Strategy vs. Tickets)
> 2. **Thursday, 60 min:** Message 3 junior PMs in my network — ask if they'd pay $497 for this
> 3. **Saturday, 2 hr:** Build the landing page (one page, Stripe payment link, no automations)

**Bad answers** to push back on:
- "Research competitors" (no day, no duration, vague verb)
- "Work on the cohort" (no specifics)
- "Set up tools" (passive — what tools, when?)

---

**Section 6: Launch Date**

**What we're writing:** A specific calendar date.

"When is this shipping? Give me a month, day, and year. Not 'sometime in Q2.'"

**Example of a 5/5 answer:**
> "First cohort kicks off Monday June 15, 2026. Landing page goes live Friday May 22. Doors close Sunday June 8."

The date creates pressure. Pressure creates decisions. Decisions create momentum. Push back hard on "I'm not sure yet" — pick a date now, you can adjust later.

---

**Section 7: Success Metric**

**What we're writing:** ONE measurable signal.

"How will you know if this worked? Define success before you launch, or you'll move the goalposts forever."

**Example of a 5/5 answer:**
> "8 paying customers at $497 by June 15. Anything less than 5 = the offer or audience is wrong. More than 12 = next cohort gets a price test at $697."

Help them pick ONE measurable metric. Push back on multiples ("I want X and Y and Z") — what's the ONE thing that decides if V1 worked?

---

**Present the Launch Plan**

Use template at templates/launch-plan.md. Hand the buyer the locked plan in paste-ready form for User Context Section D.6.

**Chain to next module**

- If they're early stage (no validation): recommend `/unstuck validate`
- If they're ready to build: recommend `/unstuck scope`

</process>

<success_criteria>
This module is complete when:
- [ ] All 7 sections filled in with specific answers
- [ ] No vague or jargon-filled entries
- [ ] Three first steps have verbs, days, and time estimates
- [ ] Launch date is a specific calendar date
- [ ] Success metric is measurable
- [ ] Launch Plan artifact delivered
- [ ] Next module recommended
</success_criteria>
