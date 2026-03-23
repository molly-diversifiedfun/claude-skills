# Decision Maker — Research Results

A one-page decision brief needs exactly seven sections to structurally improve decision quality — and not one more. This conclusion emerges from analyzing five serious decision formats (Amazon's 6-pager, Bezos's reversibility heuristic, Bain's RAPID, the military's MDMP, and Farnam Street's decision journal), cross-referenced against behavioral debiasing research and the current tool landscape. The core design insight: **optimize the brief for the person re-reading it three months later**, not for the person filling it out today. When decisions fail, it's almost always because a hidden assumption broke, not because the analysis was wrong. The template below bakes that principle into every section.

No existing tool — not weighted-matrix apps, not AI analyzers, not Notion templates, not ad-hoc ChatGPT prompts — produces a finished, shareable decision document with a stated recommendation, confidence level, and structural bias countermeasures. That's the whitespace.

---

## Five formats, one recurring lesson

Each of the five formats studied solves a different piece of the decision-quality puzzle. What they share is a conviction that **the document structure itself does cognitive work** — it's not just a container for analysis.

**Amazon's 6-pager** uses narrative prose across six sections (Introduction, Goals, Tenets, State of Business, Lessons Learned, Strategic Priorities) plus an unlimited appendix. Bezos banned PowerPoint because, as he wrote in his 2004 memo, "the narrative structure of a good memo forces better thought and better understanding of what's more important than what, and how things are related." Meetings begin with **20-30 minutes of silent reading** to eliminate presenter-charisma bias.

**Bezos's reversibility heuristic** sits above any specific format. From his 2015 shareholder letter: "Some decisions are consequential and irreversible — one-way doors — and these decisions must be made methodically, carefully, slowly, with great deliberation. But most decisions aren't like that — they are changeable, reversible — they're two-way doors." His 2016 letter adds: "Most decisions should probably be made with somewhere around **70% of the information** you wish you had." The practical implication: reversibility classification should be the *first* field, because it determines how much rigor the rest of the document deserves.

**Bain's RAPID framework** (Recommend, Input, Agree, Decide, Perform) clarifies roles, not content. Its core insight: every decision needs exactly one Recommender and exactly one Decider. McKinsey's research complements this: **fast decisions are 1.98x more likely to be good decisions**. Fortune 500 companies waste ~530,000 days of managers' time annually on ineffective decision processes. The lesson: the brief must compress, not expand.

**The Military Decision-Making Process (MDMP)** contributes the most rigorous option-comparison methodology. Each option must pass five gates — suitable, feasible, acceptable, distinguishable, and complete. The war-gaming step: an intelligence officer plays the adversary, making optimal counter-moves against each COA. Critical detail: **criteria are established before options are generated**, reducing anchoring.

**Farnam Street's decision journal** is optimized for retrospective learning. Shane Parrish's template captures mental/physical state, the problem frame, variables governing the situation, alternatives considered, and **explicit probability estimates** for expected outcomes. The journal's power comes from its 6-month review cycle: "When you look at your own handwriting you come face to face with the person you were when you made the decision."

---

## Seven sections that earn their space on one page

The one-page constraint forces a ruthless question: what do people actually check when they revisit a decision? Research converges: they check whether their assumptions held and whether any kill conditions triggered. They do *not* re-read the option comparison. This hierarchy drives what earns space.

**Included (7 sections):** Decision statement, options (with mandatory "do nothing"), recommendation with confidence, key assumptions, pre-mortem, kill conditions, and a compressed context header. **Excluded:** weighted criteria matrix (consumes 40-60% of page space for marginal retrospective value) and per-option detailed analysis (fold into option descriptions using a uniform template).

The **pre-mortem** deserves special emphasis. Daniel Kahneman called it his single most valuable decision technique. A 1989 study found that "prospective hindsight" increases the ability to identify failure reasons by **30%**. Veinott, Klein, and Wiggins (2010) found pre-mortems produced the greatest reduction in overconfidence compared to other methods.

The **assumptions** and **kill conditions** sections together create the most efficient review mechanism. Instead of re-reading the entire brief, the reviewer checks: "Did any assumptions break? Did any kill conditions trigger?" This converts a 10-minute re-read into a 30-second checklist.

**Confidence level** on the recommendation is non-negotiable. Without a written probability estimate, you cannot distinguish good decisions from lucky ones.

---

## Six biases the template structurally counters

Warning labels don't work. "Be aware of confirmation bias" produces zero behavior change. What works is **task-specific redesign** — changing the document structure so that following the template's instructions mechanically produces less-biased output. Kaufmann et al.'s 2010 meta-review of 62 debiasing studies found that structure-focused interventions consistently outperformed awareness-based ones.

- **Analysis paralysis** → Reversibility field in header calibrates rigor. Hard deadline field prevents indefinite deliberation.
- **Anchoring** → Options in alphabetical order with identical formatting. Recommendation appears after all options.
- **Sunk cost** → Forward-only language rule. Mandatory "clean slate" check.
- **Status quo bias** → "Do Nothing" mandatory as an explicitly evaluated option with "cost of inaction" field.
- **Framing effects** → Identical option template. Dual-framing on recommendation (best-case and worst-case).
- **Confirmation bias** → Mandatory pre-mortem (recommender argues against own pick) + kill conditions (pre-commits to disconfirming evidence).

---

## The gap no existing tool fills

Six categories analyzed: weighted-matrix apps (Best Decision), AI analyzers (Rationale by Jina AI), decision journals (Decision Journal App), online calculators, templates (Notion), and ad-hoc ChatGPT. None combines all five required elements: structured option input, a finished shareable document, a recommendation with confidence level, retrospective design for later review, and structural bias countermeasures.

---

## Key design decisions

**Confidence as number vs. word:** **Numeric with categorical anchor** (e.g., "70% — High") because calibration tracking is the core learning mechanism.

**Pre-mortem scope:** **Single pre-mortem on the recommendation only** since that's what you check later.

**How opinionated the recommendation should be:** **Strongly opinionated with explicit confidence** — hedged recommendations leave the user exactly where they started.

**"Do Nothing" always present vs. optional:** **Mandatory** but allow "Do Nothing is not viable because [X]" rather than forcing fake analysis.

**Criteria matrix vs. prose comparison:** **Prose with standardized structure** (each option addresses the same 2-3 factors in the same order) — matrix discipline without matrix rigidity.

**Tone:** **Direct and slightly conversational** using first-person for pre-mortem and kill conditions to create accountability.

**Review trigger:** **Include the field** with a default of 90 days post-decision.

---

## Decision Brief Template v1

> ### DECISION BRIEF
>
> **Date:** Jan 15, 2026 · **Decider:** Jamie Torres · **Decide by:** Jan 22
> **Stakes:** High · **Door:** One-way (contractor lock-in is 6 months) · **Review by:** Apr 15
> **State of mind:** Slightly anxious — pressure from board timeline
> **Who's affected:** Engineering team, Series A investors, customers on waitlist
>
> ---
>
> **THE DECISION**
> How do we ship the payment integration by Q2 — build internally, hire a specialized contractor, or delay and revisit after fundraise?
>
> ---
>
> **OPTIONS**
>
> **A. Do Nothing (delay 3 months).** Benefit: Preserves cash; lets us hire post-fundraise at better rates. Risk: Waitlist customers churn; board loses confidence. Cost of inaction: ~$80K in estimated lost revenue; fundraise narrative weakens.
>
> **B. Build in-house.** Benefit: Full control; team builds institutional knowledge. Risk: Current team is stretched — likely 4-month timeline, not 2. Cost: ~$40K in opportunity cost from diverted engineering time.
>
> **C. Hire contractor (Acme Payments).** Benefit: Ships in 6 weeks; team stays focused on core product. Risk: Vendor lock-in; integration debt if we later bring in-house. Cost: $55K fixed-price contract.
>
> ---
>
> **RECOMMENDATION:** Option C — Hire contractor · **Confidence: 70%**
> Expected outcome: Payment integration live by March 1, unlocking ~$200K ARR from waitlist conversion. B is close, but timeline risk is the dealbreaker given board pressure.
>
> ---
>
> **THIS ASSUMES:** (1) Acme can actually deliver in 6 weeks — they quoted 4-6. (2) Integration debt is manageable when we bring in-house in ~12 months. (3) Board fundraise timeline holds at Q2.
>
> ---
>
> **PRE-MORTEM:** It's July and this failed because Acme delivered late, we burned $55K AND still had to rebuild in-house, and the fundraise slipped anyway — making the entire urgency argument moot.
>
> ---
>
> **KILL CONDITIONS — I'd reverse this if:**
> (1) Acme misses their first milestone by more than 1 week.
> (2) Fundraise timeline moves past Q3, removing the urgency.
> (3) A qualified senior engineer becomes available to hire before Feb 1.

**Section budget:**

| Section | Lines | Purpose |
|---|---|---|
| Header / context | 3-4 | Anchors who, when, what's at stake |
| Decision statement | 1-2 | Frames the choice |
| Options (3 shown) | 9-15 | Equal-format comparison, "Do Nothing" included |
| Recommendation + confidence | 2-3 | The actual call, with stated certainty |
| Assumptions | 2-3 | What breaks this decision |
| Pre-mortem | 1-2 | Stress-test from the recommender |
| Kill conditions | 2-3 | When to reverse — the review checklist |
| **Total** | **~25-32 lines** | **~350 words, fits one page** |
