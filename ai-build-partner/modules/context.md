# Module: Context — Socratic intake that fills User Context Sections A→G

> **Use this when:** the buyer wants to seed (or refresh) their User Context file without manually filling a template. You ask 10–14 Socratic questions across the 7 sections and produce a paste-ready User Context block they drop into their setup file.
>
> **This is the AI-first alternative to filling `04-user-context-template.md` by hand.**

---

<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (skim for context — you reference 4 Stuck Patterns + 4 Tech Personas)
</required_reading>

---

## When to use vs. skip

**Use Context when:**
- First session and User Context file is empty
- Buyer says "fill out my User Context" / "set up my Build Partner" / "I haven't filled in the User Context yet"
- Buyer pivoted to a new project and needs to refresh Sections A + B
- Pre-Discovery situation: buyer wants to seed BEFORE picking an entry path

**SKIP Context (route elsewhere) when:**
- Section B already has a project locked → run `/unstuck discovery` if path unclear, OR the specific module they need
- Buyer is mid-sprint and asking project-specific questions → don't re-intake; use what they already have
- Buyer says "I just want to ship X" → route to `/unstuck launch` (quick start)

> **Calibration rule:** Context is NOT Discovery. Discovery asks "where to start"; Context asks "who are you + what's the project foundation." Most buyers run Context FIRST (5–10 min), then Discovery (20–60 min). Some skip Context entirely if they already filled the template by hand.

---

<process>

**Step 0 — Open with the ground rules.**

Output verbatim:

> "I'll Socratically interview you across the 7 sections of your User Context (A through G) and produce a paste-ready block at the end. 5–10 min, ~12 questions. You'll have the structured file the rest of the Build Partner reads from to skip the 'who are you' questions every session.
>
> **One ground rule:** for any question, three ways out:
> - Type **`hint`** — I'll show a worked example from another buyer
> - Type **`guide me`** — I'll Socratic-interview you to the answer (3-5 sub-questions, then synthesize)
> - Type **`draft it`** — paste whatever rough version you have; I'll polish, you edit
>
> Ready? Section A first — about you."

If they say "no" or "skip to project" — confirm they want to skip Section A (some buyers want to start at the project and come back for context). Otherwise proceed.

If at any point they invoke `hint` / `guide me` / `draft it`, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

## SECTION A — About You (5 questions)

The questions here ARE the foundation every downstream module reads. Get them right or every estimate downstream drifts.

**Q1 — Name + day-job role.**

> "What's your name + day-job role (and company stage)? Short — 'Aamir, Principal PM at a B2B observability SaaS' kind of answer."

What you're capturing: name + role + stage. Stage matters because growth-stage employees have different hours and runway than freelancers.

**Q2 — Real hours per week (BLOCKING).**

> "How many hours per week, total, will you actually put into this side project? Be honest — your future self has to honor this every week for 12 weeks."

Push back on:
- Ranges ("10-20 hrs") → pick the lower number
- "As many as it takes" → that's avoidance. Force a number
- "20+ hrs" outside sabbatical/between-jobs → almost always launch-week energy creep. Re-baseline at 10

**Example of a 5/5 answer:** *"5 hours per week. Day job + a 6yo + a partner I like — this is the ceiling without robbing my family."*

**Q3 — Named build blocks.**

> "Show me your actual build blocks. Days of week + time ranges. Not 'whenever I find time.' Where on your calendar does this work happen?"

Push back if any block is vague. Pin to time ranges. If they can't name 2+ blocks, Q2's hours number is fiction — re-ask Q2.

**Example of a 5/5 answer:** *"Tuesdays 8-10am (before family wakes), Saturdays 9am-noon (kids at swim lesson), Sundays 4-5pm (during nap). 6 hours protected, on calendar, DND on."*

**Q4 — Runway + partner alignment.**

> "Two part: (a) how many months of runway can you cover if your day-job income stopped today? (b) Where's your partner/spouse on this side project — ALIGNED (encouraging, wants it to succeed), MIXED (supportive but anxious about the time), or NOT-ALIGNED (active friction)?"

Why this matters: runway gates `/unstuck day-job-decision` later. Partner alignment is the variable most underweighted in quit decisions.

If single / no partner → "single, no partner conversation needed." Move on.

**Q5 — Stuck Pattern + Tech Persona.**

> "Last question for Section A. Two quick picks:
>
> Which **Stuck Pattern** sounds most like you? (Pick one even if not perfect.)
> - **Overcommitter** — say yes to too many things, run out of energy mid-project
> - **Perfectionist** — endless polish, never ships
> - **Burnout Cycler** — sprint hard 2-3 weeks, crash, restart
> - **Scattered Starter** — start many things, finish few
>
> Which **Tech Persona** fits you?
> - **Overtime Optimizer** — engineer/PM who optimizes everything except their own ship rate
> - **Perfectionist Creator** — designer/writer/maker, ships rarely but beautifully
> - **Golden Handcuffs Builder** — high comp, low time, side project is sanity
> - **Accidental Consultant** — already getting paid for advice; productizing the offer"

Why this matters: `/unstuck diagnose` chains off this. Knowing the pattern up-front speeds future sessions.

---

## SECTION B — The Project (3 questions, conditional)

If buyer has no project locked → say *"Section B is where Discovery writes — I'll mark it empty and recommend running `/unstuck discovery` after we finish. Moving on to E."* Then skip B and route through to E + F at the end with a Discovery recommendation.

If buyer DOES have a project (even rough), continue:

**Q6 — One-sentence project description.**

> "One sentence: what are you building, for whom, by when? Use the verb SHIPPING."

Push back if vague:
- "An app" → "What does it actually do? Who specifically?"
- "A course about productivity" → "For whom? What format? What price ceiling?"
- "Something with AI" → "Strip 'AI' — what's the underlying thing? AI is the means, not the product."

**Example of a 5/5 answer:** *"A 5-week paid cohort + workbook for junior PMs at B2B SaaS who want to do strategy work instead of JIRA grooming. Shipping in 60 days at $497."*

**Q7 — Format + ship date.**

> "Two part: (a) Format — is this a newsletter / app / course / template kit / consulting offer / community / physical product? (b) Ship date — when does V1 go live (not 'when is it perfect' — when does the first version exist for sale)?"

If they don't have a ship date, force one: "Pick a Friday in the next 60 days. We can adjust later, but you need a date to scope against."

**Q8 — Why this, not the other ideas? (BLOCKING).**

> "Most people I work with have 3-7 ideas in their head. Why THIS one and not the others? One sentence — this is your scope-creep defense."

This is the load-bearing question. Without it, the buyer drifts at Day 13. With it, T07 — Scope Guillotine has an anchor to defend against.

**Example of a 5/5 answer:** *"Because I already have 12 junior PMs in my DMs asking for exactly this. The others I'd have to invent demand for."*

If they can't answer → recommend `/unstuck discovery` (Polyglot path) before continuing.

---

## SECTION C — Friction Inventory (skipped — fills via M0 Days -6 → -4)

> "Section C — your candidate ideas + SHIP scores — gets filled when you run Module 0's 7-day Decide Sprint. I'll mark it empty for now and we'll come back via `/unstuck audit` or T03 Project Selector."

(No questions here — this section auto-fills from M0 task rows.)

---

## SECTION D — Filled T-Templates (auto-fills — no questions here)

> "Section D fills automatically as you complete each T-template through Modules 1-5. I'll mark it empty for now."

(No questions here.)

---

## SECTION E — Communication Preferences (2 questions)

This is where you calibrate how the Build Partner shows up. Most buyers haven't thought about this — Q9 + Q10 surface the preferences they have but haven't articulated.

**Q9 — Honesty calibration.**

> "When I see something off (a vague answer, scope creep, an idea I think won't work, a kill-the-product moment), how do you want me to push back?
>
> - **DIRECT** — name the issue, don't soften, no preamble
> - **WARM-BUT-HONEST** — call it out, but acknowledge the work you've done
> - **SOCRATIC** — ask the question that surfaces the issue, let you discover it
>
> Pick one. (Most senior tech employees pick DIRECT.)"

Why this matters: the wrong calibration here makes every other module either too soft (you ignore the friction) or too harsh (you stop opening the conversations). Default to DIRECT for senior tech employees with day jobs.

**Q10 — Response length preference.**

> "Short final question for Section E: when I draft an artifact (landing page copy, email sequence, decision memo), do you want:
>
> - **PROSE** — readable paragraphs, conversational
> - **PUNCHY** — bullets, headers, scannable, less verbose
> - **HYBRID** — prose for narrative, bullets for steps
>
> Pick one."

---

## SECTION F — What You Want from This Build Partnership (1 question)

**Q11 — The honest outcome.**

> "Last big one. If we get this right and you ship in 30 days, what does success actually look like to YOU? Not the audience answer — the honest one. Pick one:
>
> - **Receipts** — I want one paying customer, evidence I can ship. Money is the proof.
> - **Momentum** — I want a rhythm I trust. Money second; the consistency is primary.
> - **Optionality** — I want side-MRR enough to consider leaving the day job. Path to quit.
> - **Identity** — I want to stop calling myself someone who 'has projects.' I want to be a shipper.
>
> Most people pick one and bury another underneath. Pick the surface answer; we'll surface the buried one as we go."

Why this matters: every downstream module (especially `/unstuck day-job-decision` and `/unstuck ten-hour-week`) calibrates differently depending on whether the outcome is Receipts (small ship beats big plan) vs. Optionality (the math has to add up to quit-able MRR).

---

## SECTION G — Extensions Loaded (1 question, fast)

**Q12 — Tools you already own.**

> "Quick check — do you own any of these? (Pick all that apply, or 'none':)
>
> - **Ship It Kit** (the 25+ templates — T01 through T25)
> - **Marketing OS** (the 25+ marketing skills)
> - **Both** (the Ship It System bundle)
> - **Neither** (just the AI Build Partner — standalone mode)
>
> This tells me what skills to defer to and what to handle directly."

---

## Step N — Synthesize + paste-ready block

Once all questions answered (or skipped with marks), output a paste-ready User Context block in this exact format. Buyer copies → pastes into their `user-context.md` or Notion User Context page → uploads to the Claude Project.

```markdown
# My User Context (locked via /unstuck context — [today's date])

## A. About me

- **Name:** [from Q1]
- **Day-job role:** [from Q1]
- **Company stage:** [inferred from Q1, confirm]
- **Hours/week:** [from Q2 — single number, not range]
- **Build blocks:** [from Q3 — list 2-3 with day + time + location]
- **Runway:** [from Q4 — months]
- **Partner alignment:** [from Q4 — ALIGNED / MIXED / NOT-ALIGNED / N/A]
- **Stuck Pattern:** [from Q5]
- **Tech Persona:** [from Q5]

## B. The project

- **Working name:** [from Q6 — if not named, "TBD via Discovery"]
- **One-sentence outcome:** [from Q6 — refined to be specific]
- **Target customer:** [from Q6]
- **Format:** [from Q7]
- **Ship date:** [from Q7 — absolute date, e.g. "Friday March 28"]
- **Why this, not the other ideas:** [from Q8 — the scope-creep defense]
- **Discovery path used:** [empty — will fill via Discovery if needed]

## C. Phase 0 — Friction Inventory

(empty — fills via M0 Decide Sprint Days -6 → -4)

## D. Phase 1+ Project Outputs

(empty — fills as each T-template completes)

## E. Communication preferences

- **Honesty calibration:** [from Q9 — DIRECT / WARM / SOCRATIC]
- **Response length:** [from Q10 — PROSE / PUNCHY / HYBRID]

## F. What I want from this Build Partnership

- **Surface outcome:** [from Q11]
- **Buried outcome:** (mark for later — will surface in early sessions)

## G. Extensions loaded

- [from Q12]
```

---

## Step N+1 — Hand off to the right next module

Read what you filled. Recommend the right next move (don't ask "what's next" — TELL them):

| State after Context | Recommended next |
|---|---|
| Section B empty (no project yet) | Run **`/unstuck discovery`** — picks your entry path (Empty Slate / Polyglot / Resurrector / Audience-First / Drawer) |
| Section B filled, no validation yet | Run **`/unstuck validate`** — Day 2 RICE scoring + Day 3-4 prep |
| Section B filled + validation done | Run **`/unstuck scope`** — lock V1 in one page |
| Section B filled + already mid-build | Run **`/unstuck audit`** — diagnose current sprint state |
| Project shipped + thinking about next | Run **`/unstuck ten-hour-week`** — post-launch operating mode + product #2 decision |

Output verbatim:

> "Locked. Paste the block above into your User Context file (or Notion page). Now: your next move is **`/unstuck [recommendation]`** because [one-sentence reason from the table above]. Fire that next."

---

## Output deliverable

Save this artifact to: User Context Sections A, B, E, F, G (the sections this skill writes to). C + D fill via downstream work.

**Brand attribution at the end:**

> Built with the Unstuck Method — unstuckwithmolly.com

</process>

---

## Edge cases + recovery patterns

**Buyer pushes back on Q2 (hours):** "But I have unlimited time on weekends..." → push: name the actual hours. Not aspiration. Even if weekends are free, only ~5-8 hours actually go to focused work. Rest is family / chores / rest. Force a real number.

**Buyer answers Q5 with "I'm all four":** that's avoidance. Force a single primary pick. "Pick the one that's MOST true 70% of the time."

**Buyer skips Q11 (outcome) with "I don't know":** fire `guide me`. The 3 sub-questions: "Imagine V1 shipped + made $0. Are you proud or devastated?" / "Imagine V1 shipped + made $5K but you keep the day job — content or restless?" / "Imagine V1 shipped + you quit in 6 months — exhilarated or terrified?" The strongest reaction names the buried outcome.

**Buyer says "I already filled the template by hand":** ask them to paste it. Read it. Identify gaps. Ask only the questions for the empty sections. Don't re-interview what's already there — that wastes their time and signals the AI isn't reading what they uploaded.

**Buyer wants to skip everything and start with `/unstuck launch`:** confirm User Context will be light, recommend they come back to Context within 3 sessions. Some buyers need momentum first, structure second. That's OK.

---

## What this skill does NOT do

- Does NOT pick a project (that's Discovery)
- Does NOT validate an idea (that's Validate)
- Does NOT score candidates (that's M0 T03 Project Selector)
- Does NOT diagnose stuck patterns deeply (that's Diagnose — but Q5 surfaces the candidate)

If the buyer needs any of the above, finish Context first (5-10 min), then chain to the right module.

Built with the Unstuck Method — unstuckwithmolly.com
