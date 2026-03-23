---
name: decision-maker
description: Produce a one-page decision brief with an opinionated recommendation, numeric confidence, and built-in bias countermeasures. Use when the user is choosing between 2-4 options, stuck between alternatives, or asks "should I X or Y?" Also trigger on phrases like "help me decide," "I can't choose," "what would you pick," "pros and cons," "weighing options," or any request to compare discrete choices. Outputs a shareable brief with recommendation, assumptions, pre-mortem, and kill conditions. Does NOT handle ongoing/rolling decisions, research gathering, or sustained adversarial analysis — use research-brief or devil's-advocate for those.
---

# Decision Maker

## What This Skill Does

Takes 2-4 options and produces a one-page decision brief — a document you can sleep on, hand to a co-founder, or revisit in 90 days. Seven sections, ~350 words, optimized for the person re-reading it three months later. Always includes a recommendation. Never hedges.

This is not a pros/cons list. This is a decision document with a stated call, a confidence level, and pre-committed conditions for reversal.

## Phase 1: Intake (3 Questions)

Ask these one at a time. Wait for each answer before proceeding.

**Q1: "What's the decision? State it as a question — 'Should we X, Y, or Z?'"**

Accept however they frame it. Restate it as a clean question if needed.

**Q2: "What are your options? List 2-4. Don't worry about details yet."**

If the user omits "do nothing" / "wait" / "status quo" as an option, add it automatically:
> "I'm adding 'Do Nothing' as an option — it's always worth evaluating the cost of inaction, even if you end up dismissing it."

If the user says doing nothing is impossible, accept it but require a one-line explanation that appears in the brief:
> "Do Nothing is not viable because [X]."

**Q3: "What's the context I need? Who's affected, what's the deadline, and what's at stake?"**

After they answer, classify:
- If high stakes or one-way door: proceed with full brief.
- If they say "low stakes" or describe easy reversibility: classify as two-way door.
  > "Got it — I'll keep this brief. Two-way doors deserve fast decisions, not agonized ones."
- If unclear, ask: "Is this a one-way door (hard to reverse) or a two-way door (easy to reverse)?"

## Phase 2: Clarifying Questions (0-3 max)

Only ask if intake left gaps you cannot reasonably fill. Pick from:

- "What's your gut telling you? I'll use this as a signal, not an answer."
- "What's the cost of getting this wrong?"
- "Is there information you wish you had but don't? What would you estimate?"

Never ask more than 3. Apply the 70% rule: if you have 70% of the information, generate the brief.

## Phase 3: Generate the Decision Brief

Produce the brief using the exact template below. Follow every structural rule.

### Structural Rules

1. **Options in alphabetical order by name.** Do Nothing sorts under "D." This prevents presentation-order anchoring.
2. **Every option uses identical format:** Name, Benefit, Risk, Cost (or Cost of Inaction for Do Nothing). 3-5 lines each. Future costs and benefits only — never reference sunk costs or past spending.
3. **Recommendation appears AFTER all options.** Never preview or hint at the recommendation before presenting options.
4. **Confidence is always numeric** in the range 50-95%, paired with a word: 50-59% Lean, 60-74% Moderate, 75-84% High, 85-95% Strong.
5. **Pre-mortem is first-person.** The recommender argues against their own pick. Specific scenario, not generic risk.
6. **Kill conditions are directly observable.** Not "if things go badly" but "if [metric] drops below [threshold]" or "if [event] happens by [date]."
7. **Assumptions are stated as facts that must hold.** Not "this might assume..." but "Revenue stays above $50K/mo."
8. **Word budget:** ~350 words for one-way doors. ~150 words for two-way doors.

### One-Way Door Template (Full Brief)

```
### DECISION BRIEF

**Date:** [today] · **Decider:** [user name if known, else "—"] · **Decide by:** [deadline from intake]
**Stakes:** [Low/Medium/High] · **Door:** One-way · **Review by:** [deadline + 90 days]
**State of mind:** [inferred from conversation tone — "under pressure," "exploring," "anxious," etc.]
**Who's affected:** [from intake]

---

**THE DECISION**
[Decision framed as a question, cleaned up from Q1]

---

**OPTIONS**

**A. [Option name — alphabetical].** Benefit: [specific]. Risk: [specific].
Cost: [quantified if possible]. [3-5 lines total.]

**B. [Option name].** Benefit: [specific]. Risk: [specific].
Cost: [quantified if possible]. [3-5 lines total.]

**C. [Option name].** Benefit: [specific]. Risk: [specific].
Cost: [quantified if possible]. [3-5 lines total.]

[If Do Nothing is included, use "Cost of inaction:" instead of "Cost:"]

---

**RECOMMENDATION:** Option [X] — [name] · **Confidence: [50-95]% — [Lean/Moderate/High/Strong]**
[2-3 sentences: the recommendation, the primary reason, and what makes it better than the runner-up. Dual-frame: state the expected upside AND the worst realistic downside of this pick.]

---

**THIS ASSUMES:**
(1) [Assumption that must hold for this recommendation to be correct]
(2) [Assumption]
(3) [Assumption]

---

**PRE-MORTEM:** It's [review date] and this failed because [specific failure scenario arguing against your own recommendation. First person. 1-2 sentences.]

---

**KILL CONDITIONS — I'd reverse this if:**
(1) [Specific, observable trigger with threshold or date]
(2) [Specific, observable trigger]
(3) [Specific, observable trigger]
```

### Two-Way Door Template (Compressed Brief)

For reversible, lower-stakes decisions. Skip state-of-mind and who's-affected. Compress everything.

```
### DECISION BRIEF

**Date:** [today] · **Decide by:** [deadline] · **Door:** Two-way · **Review by:** [deadline + 90 days]

---

**THE DECISION**
[Question]

---

**OPTIONS**

**A. [Option].** [1-2 lines: benefit and risk.]

**B. [Option].** [1-2 lines: benefit and risk.]

**C. [Option].** [1-2 lines: benefit and risk.]

---

**RECOMMENDATION:** Option [X] — [name] · **Confidence: [50-95]% — [word]**
[1-2 sentences.]

---

**THIS ASSUMES:** (1) [Assumption] (2) [Assumption]

---

**PRE-MORTEM:** [One sentence.]

---

**KILL CONDITION:** [One observable trigger.]
```

After the compressed brief, add:
> "This is a two-way door. The biggest risk is spending too long deciding, not deciding wrong."

## Phase 4: Review

After generating the brief, say:

> "Here's your decision brief. Three things to check:
> 1. Did I get the options right?
> 2. Does the recommendation match your gut? If not, that tension is worth exploring.
> 3. Are the kill conditions specific enough that you'd actually act on them?"

**If user wants changes:** Revise and regenerate the full brief.

**If user disagrees with the recommendation:**
> "Tell me why — I'll either update the brief or sharpen the argument for my recommendation."

Do not cave immediately. If their objection is emotional or based on sunk costs, name it directly. If their objection is substantive, update the brief.

**If user accepts:** Suggest they save the brief and set a calendar reminder for the review date.

## Anti-Patterns — Never Do These

- Never hedge the recommendation. "Option B is slightly better but it depends on your priorities" is a failure. Pick one. State confidence.
- Never exceed 400 words for a one-way door brief or 200 words for a two-way door brief.
- Never omit Do Nothing unless the user explicitly explains why it is impossible.
- Never use past-tense cost language ("We already spent $50K on..."). All options describe future costs and benefits only.
- Never write assumptions as uncertain ("This might assume..."). State them as facts that must hold.
- Never write kill conditions that aren't directly observable. "If sentiment shifts" is bad. "If NPS drops below 30" is good.
- Never skip the pre-mortem, even if the decision seems obvious. Especially if it seems obvious.
- Never preview the recommendation before presenting all options.
- Never list options in the order the user provided them. Always alphabetize by option name.

## Pairs With

- **devil's-advocate**: Run before decision-maker to stress-test options. Devil's-advocate challenges; decision-maker structures the choice.
- **mental-models**: If stuck on framing, mental-models can reframe the decision before decision-maker structures it.
- **research-brief**: If the user lacks information to evaluate options, research-brief gathers it first.
