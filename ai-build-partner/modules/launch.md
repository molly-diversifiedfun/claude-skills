<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan `.unstuck/context.md`:
- Read **Section B.1** (project + audience), **Section D.2** (T05 Scope), **Section D.3** (T06 Pricing) if present
- If populated, DRAFT the launch plan: pull product name + audience + price + ship date from context, propose JTBD + format + V1 features, name 3 candidate first-customers to text on launch day. Present the draft + ask the user to refine. Skip the 7-question intake — they already answered those upstream.
- If `.unstuck/context.md` is empty, use the Opening below and run the question-by-question 7-section intake — and consider routing the user to `/unstuck discovery` first.

Don't ask what you can read. Draft what you can infer.

---

**Step 0.5 — If they already have a One-Page Launch Plan, take it**

The free prompt at `theshipitsystem.com/launch-prompt` produces a One-Page
Launch Plan in whatever AI they were already using. People arrive here holding
one. Asking them seven questions they answered twenty minutes ago is the
fastest way to lose them.

So before the Opening, ask ONCE, in one line, whether they have a plan to
paste. Yes or no, not an essay. **If no — fall through to the Opening below,
completely unchanged.**

If they paste one, map it. Accept loose formatting: prose, a bulleted plan, or
the exact headings.

| What the plan says | Where it lands here | Notes |
|---|---|---|
| The one action someone takes when it works | Seeds **Section 3** and **Section 7** | It is the observable thing, not a transformation and not a metric. Still ask both; open from this. |
| The first real person, by name | Seeds **Section 2** | A name is not a persona. Still ask Section 2 — open with "You said <name>. Tell me about them." |
| Everything that has to be true first | Nowhere | Working material, already superseded by V1. Do not carry it forward. |
| What that person would notice missing — V1 | **Section 4**, as given | See rule 3. |
| The part they keep redoing, named and closed | `.unstuck/context.md`, not this plan | It is a stuck pattern, not a launch-plan field. |
| The day they get it, and the hours available | **Section 6**, as given | Carry the hours too — write them under the date, since Section 6 has no slot for them and they are what makes the date checkable. |
| Three moves this week, with done-whens | **Section 5**, as given | |
| The context block (`## B. The project`) | **Section 1** — working name, one-sentence outcome | This is the only place the project gets named; the plan body never names it. |

Four rules, all load-bearing:

1. **A tagged field is not an answer.** The prompt marks its own guesses
   `[MY CALL]` and its gaps `[STILL FUZZY]`. Those tags exist precisely because
   the user never answered. Ingesting them untagged launders another AI's guess
   into their decision, silently, and every module downstream then reads it as
   fact. Ask every tagged field in this module's own wording, exactly as if the
   plan had left it blank.

2. **Read it back before you use it.** Field by field: what you extracted and
   where it landed. Ask them to confirm or correct. Show a blank as a blank —
   never fill one from another field, from the project's shape, or from what a
   plan like this usually says.

3. **Do not re-cut V1.** That V1 came out of an item-by-item pass where the user
   made every cut themselves, under a rule that said once something was out it
   stayed out. Section 4 below says to push ruthlessly — **that instruction does
   not apply to an ingested V1.** Take it as given. If it looks too big for the
   date, say so once as arithmetic and move on. Do not reopen items, and do not
   offer to add anything back.

4. **There is no price in it.** The prompt bans money on purpose, so an ingested
   plan carries no price and its V1 was never scoped to a paid thing. Sections
   3, 4 and 7 are written assuming one. Ask whether there is a price before you
   use that wording. If there isn't, the success metric is a first subscriber,
   reader, member, or reply — those count the same here.

Then run only the sections the plan did not fill, in the order below. Say one
line up front naming which ones you are skipping and why, then skip them
without further comment.

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

→ Next: **Section 2** — define your specific customer persona

---

**Section 2: Who It's For**

**What we're writing:** Your customer persona — one specific human, not a category.

"Who is this for? Get uncomfortably specific. Not 'entrepreneurs' — that's everyone. Picture ONE person and describe them."

**Example of a 5/5 answer:**
> "Aamir, 26, PM at a B2B observability SaaS, 18 months in. Tuesday afternoon backlog grooming is the moment he thinks 'I didn't sign up for this' — he wants to do strategy work, not adjust story points. Reads Lenny's Newsletter on his commute."

The 5/5 answer has: name, age, role, company type, behavioral specifics, and the exact-moment-of-pain. Push back if any of those slots are missing.

→ Next: **Section 3** — define the transformation, not the feature list

---

**Section 3: The Core Offer**

**What we're writing:** The transformation (not the feature list).

"What do they get, and why would they pay for it? Don't give me a feature list — give me the transformation. After they finish, what can they DO that they couldn't before?"

**Example of a 5/5 answer:**
> "After 5 weeks, Aamir walks into his next 1:1 with a written product strategy doc for his squad, gets buy-in from his EM, and stops being the JIRA admin. He can say 'I'm leading our roadmap' instead of 'I'm grooming the backlog.'"

People don't buy features. They buy outcomes. Push back if they give you a list of modules / lessons / templates — those are HOW, not WHAT.

→ Next: **Section 4** — cut to the smallest shippable version

---

**Section 4: MVP Scope**

**What we're writing:** The smallest version that still works.

"What's the smallest thing you can ship that proves people will pay for this?"

**Example of a 5/5 answer:**
> "5 weekly live sessions (90 min each) + a 40-page workbook + a private Slack — no LMS, no recorded course library, no 1:1 calls. If 8 people pay $497 each, V1 is validated."

Push ruthlessly. If it takes more than 4 weeks to build, it's too big. Push back: "What can you cut and still have something people would pay for?"

→ Next: **Section 5** — three concrete tasks for this week

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

→ Next: **Section 6** — pick a specific launch date

---

**Section 6: Launch Date**

**What we're writing:** A specific calendar date.

"When is this shipping? Give me a month, day, and year. Not 'sometime in Q2.'"

**Example of a 5/5 answer:**
> "First cohort kicks off Monday June 15, 2026. Landing page goes live Friday May 22. Doors close Sunday June 8."

The date creates pressure. Pressure creates decisions. Decisions create momentum. Push back hard on "I'm not sure yet" — pick a date now, you can adjust later.

→ Next: **Section 7** — define one measurable success signal

---

**Section 7: Success Metric**

**What we're writing:** ONE measurable signal.

"How will you know if this worked? Define success before you launch, or you'll move the goalposts forever."

**Example of a 5/5 answer:**
> "8 paying customers at $497 by June 15. Anything less than 5 = the offer or audience is wrong. More than 12 = next cohort gets a price test at $697."

Help them pick ONE measurable metric. Push back on multiples ("I want X and Y and Z") — what's the ONE thing that decides if V1 worked?

→ Next: **Present** — generate the Launch Plan artifact

---

**Present the Launch Plan**

Use template at templates/launch-plan.md. Hand the buyer the locked plan in paste-ready form for User Context Section D.6.

→ Next: **Save** — persist the artifact

---

**Save artifact**

Save the completed Launch Plan to `.unstuck/launch-YYYY-MM-DD.md` using the Write tool. Use today's date.

→ Next: **Update context**

---

**Update context**

Append a summary to `.unstuck/context.md` under **Section D.6** (Launch Plan):
- Product name + one-line description
- Target persona
- MVP scope summary
- Launch date
- Success metric
- Date locked

---

**What's next**

> **BRANCHING EXIT — pick the path that fits:**
>
> - **Early stage (no validation yet):** run `/unstuck validate` — you need real conversations before building.
> - **Ready to build (validation done):** run `/unstuck scope` — lock your V1 features and ship date.
>
↩ Come back to `/unstuck launch` when: your launch plan is stale or you're launching a new product.

</process>

<success_criteria>
This module is complete when:
- [ ] All 7 sections filled in with specific answers
- [ ] No vague or jargon-filled entries
- [ ] If a plan was pasted: every `[MY CALL]` / `[STILL FUZZY]` field in it was
      re-asked, not carried over
- [ ] If a plan was pasted: the extraction was read back field by field and
      confirmed, and no blank was filled by inference
- [ ] If a plan was pasted: V1 was taken as given — no item reopened, cut, or
      added back
- [ ] Three first steps have verbs, days, and time estimates
- [ ] Launch date is a specific calendar date
- [ ] Success metric is measurable
- [ ] Launch Plan artifact delivered
- [ ] Artifact saved to `.unstuck/launch-YYYY-MM-DD.md`
- [ ] Context updated in `.unstuck/context.md` Section D.6
- [ ] Next module recommended
</success_criteria>
