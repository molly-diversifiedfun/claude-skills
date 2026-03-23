# PRD: decision-maker

## Problem

People get stuck between options. They make pros/cons lists that go nowhere, ask friends who tell them what they want to hear, or agonize until the deadline decides for them. When they use Claude, they get balanced analysis that refuses to recommend — leaving them exactly where they started. No existing tool produces a finished, shareable decision document with a stated recommendation, confidence level, and structural bias countermeasures.

## Solution

A skill that takes 2-4 options and produces a one-page decision brief — a document you can sleep on, hand to a co-founder, or revisit in 90 days. Seven sections, ~350 words, optimized for the person re-reading it three months later. The template's structure silently counters six cognitive biases through task-specific redesign, not awareness warnings.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Confidence format | **Numeric + categorical** ("70% — High") | Enables calibration tracking over time. Comparing stated confidence to actual outcomes is the single most reliable calibration mechanism. |
| Pre-mortem scope | **Recommended option only** | That's what you check on review day. Per-option pre-mortems blow the page budget. |
| Recommendation strength | **Strongly opinionated with explicit confidence** | Hedged recommendations leave the user exactly where they started. The entire value prop is escaping neutral option-listing. |
| "Do Nothing" option | **Mandatory** | Status quo bias is pervasive. Forced evaluation of inaction almost always adds value. Allow "Do Nothing is not viable because [X]." |
| Option comparison format | **Prose with standardized structure** | Each option addresses benefit/risk/cost in the same order. Matrix discipline without matrix rigidity. |
| Tone | **Direct, slightly conversational, first-person** | First-person for pre-mortem and kill conditions ("I'd reverse this if...") creates accountability. |
| Review trigger | **Built in** | Default 90 days post-decision. The entire retrospective value depends on actually revisiting. |

## The Six Silent Debiasing Mechanisms

The template's structure does cognitive work the user never sees:

| Bias | Structural Countermeasure |
|------|--------------------------|
| **Analysis paralysis** | Reversibility field (one-way/two-way door) calibrates appropriate rigor. "Decide by" deadline prevents indefinite deliberation. |
| **Anchoring** | Options in alphabetical order with identical formatting. Recommendation appears AFTER all options, never before. |
| **Sunk cost** | Forward-only language rule: options describe future costs and benefits only. Mandatory "clean slate" check. |
| **Status quo bias** | "Do Nothing" is a mandatory, explicitly evaluated option with a "cost of inaction" field. |
| **Framing effects** | Identical option template. Dual-framing on recommendation (best-case and worst-case). Quantified where possible. |
| **Confirmation bias** | Mandatory pre-mortem (recommender argues against their own pick). Kill conditions pre-commit to disconfirming evidence. |

## Interaction Model

### Step 1: Intake (2-3 min)

Three questions, asked one at a time:

1. "What's the decision? State it as a question — 'Should we X, Y, or Z?'"

2. "What are your options? List 2-4. Don't worry about details yet."
   → If user omits "do nothing" / "wait" / "status quo": skill adds it automatically and explains why.

3. "What's the context I need? Who's affected, what's the deadline, and what's at stake?"
   → If user says "high stakes": "Is this a one-way door (hard to reverse) or a two-way door (easy to reverse)?"
   → If user says "low stakes" or two-way door: "Got it — I'll keep this brief. Two-way doors deserve fast decisions, not agonized ones."

### Step 2: Clarifying Questions (0-3 questions)

Only if the intake left gaps the skill can't fill:
- "What's your gut telling you? I'll use this as a signal, not an answer."
- "What's the cost of getting this wrong?"
- "Is there information you wish you had but don't? What would you estimate?"

Never more than 3 clarifying questions. Bezos's 70% rule: "If you wait for 90% of the information, you're probably being slow."

### Step 3: Brief Generation (automatic)

Produce the one-page decision brief:

```
### DECISION BRIEF

**Date:** [today] · **Decider:** [user name if known] · **Decide by:** [deadline]
**Stakes:** [Low/Medium/High] · **Door:** [One-way / Two-way] · **Review by:** [date + 90 days]
**State of mind:** [captured from conversation tone — "under pressure," "exploring," etc.]
**Who's affected:** [from intake]

---

**THE DECISION**
[The decision framed as a question, from Step 1]

---

**OPTIONS**

**A. [Do Nothing / Status Quo].** Benefit: [specific]. Risk: [specific].
Cost of inaction: [quantified if possible].

**B. [Option name].** Benefit: [specific]. Risk: [specific].
Cost: [quantified if possible].

**C. [Option name].** Benefit: [specific]. Risk: [specific].
Cost: [quantified if possible].

[Alphabetical by name. Same structure per option. Future costs only.
3-5 lines each.]

---

**RECOMMENDATION:** Option [X] — [name] · **Confidence: [50-95]%**
[2-3 sentences: the recommendation, the primary reason, and what
makes it better than the runner-up]

---

**THIS ASSUMES:**
(1) [Assumption the decision depends on]
(2) [Assumption the decision depends on]
(3) [Assumption the decision depends on]

[2-3 assumptions. These are what you check on review day.]

---

**PRE-MORTEM:** It's [review date] and this failed because [the recommender
argues against their own pick — specific scenario, not generic risk].

[1-2 sentences. First person.]

---

**KILL CONDITIONS — I'd reverse this if:**
(1) [Specific, observable trigger]
(2) [Specific, observable trigger]
(3) [Specific, observable trigger]

[2-3 triggers. Converts future review into a 30-second checklist.]
```

### Step 4: Review (1 min)

"Here's your decision brief. Three things to check:
1. Did I get the options right?
2. Does the recommendation match your gut? If not, that tension is worth exploring.
3. Are the kill conditions specific enough that you'd actually act on them?"

If user wants changes: revise and regenerate.
If user disagrees with recommendation: "Tell me why — I'll either update the brief or sharpen the argument for my recommendation."

### Calibration for Two-Way Doors

If the decision is classified as a two-way door, the skill compresses:
- Skip state-of-mind and who's-affected
- Options get 1-2 lines each, not 3-5
- Pre-mortem becomes one sentence
- Kill conditions become one trigger
- Total output: ~150 words
- Message: "This is a two-way door. The biggest risk is spending too long deciding, not deciding wrong."

## Success Criteria

- Brief fits on one page (~350 words for one-way doors, ~150 for two-way)
- Recommendation is always present and always opinionated (never "it depends")
- Confidence level is always numeric (never vague)
- Assumptions are specific enough that on review day, you can answer "did this hold?" in under 10 seconds per assumption
- Kill conditions are observable (not "if things go badly" but "if [specific metric] drops below [threshold]")
- The user can hand the brief to someone who wasn't in the conversation and they understand the decision

## What This Skill Does NOT Do

- Make the decision for you (it recommends, you decide)
- Provide research or data you don't have (it structures what you know — research-brief handles gathering information)
- Handle ongoing/rolling decisions (this is for point-in-time choices between discrete options)
- Replace devil's-advocate (the pre-mortem is one stress test; devil's-advocate provides sustained adversarial analysis)

## Anti-Patterns to Avoid in Implementation

- Never hedge the recommendation ("Option B is slightly better but it depends on your priorities") — pick one, state confidence
- Never produce a brief longer than 400 words for a one-way door or 200 words for a two-way door
- Never omit "Do Nothing" as an option unless the user explicitly explains why it's impossible
- Never use future-uncertain language in assumptions ("This might assume...") — state them as facts that must hold
- Never produce kill conditions that aren't directly observable ("if sentiment shifts" → bad; "if NPS drops below 30" → good)
- Never skip the pre-mortem, even if the decision seems obvious — especially if it seems obvious

## Pairs With

- **devil's-advocate**: Run before decision-maker to stress-test the options. Devil's-advocate challenges; decision-maker structures the choice.
- **mental-models**: If stuck on framing, mental-models can help reframe the decision before decision-maker structures it.
- **self-interview**: If the user can't articulate their options, self-interview helps clarify thinking first.
- **research-brief**: If the user lacks information to evaluate options, research-brief gathers it before decision-maker structures the choice.
