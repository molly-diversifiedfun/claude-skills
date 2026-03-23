# Decision Maker

## The Problem

You're stuck between options. You make pros/cons lists that go nowhere. You ask friends who tell you what you want to hear. You ask Claude and get balanced analysis that refuses to recommend — leaving you exactly where you started.

No existing tool — not weighted-matrix apps, not AI analyzers, not Notion templates, not ad-hoc ChatGPT prompts — produces a finished, shareable decision document with a stated recommendation, confidence level, and structural bias countermeasures.

## What It Does

Produces a **one-page decision brief** from 2-4 options. Seven sections, ~350 words, optimized for the person re-reading it three months later.

The brief always includes:
- An opinionated recommendation (never "it depends")
- A numeric confidence level (never vague)
- Assumptions stated as checkable facts
- A pre-mortem where the recommender argues against their own pick
- Kill conditions that convert a future review into a 30-second checklist

This is not a pros/cons list. It is a decision document with a stated call, a confidence level, and pre-committed conditions for reversal.

## How to Use It

**Claude.ai** — Start a conversation and say:
> "Help me decide: should I [X], [Y], or [Z]?"

Any phrasing works: "I can't choose between...", "weighing options on...", "what would you pick...", or just "pros and cons of..."

**Claude Code** — Add the skill to your config, then:
```
claude "Help me decide whether to build in-house, hire a contractor, or delay the project"
```

The skill asks three intake questions (decision, options, context), asks 0-3 clarifying questions if needed, then generates the brief.

## The Template

### One-Way Door (Full Brief)

```
### DECISION BRIEF

**Date:** Jan 15, 2026 · **Decider:** Jamie Torres · **Decide by:** Jan 22
**Stakes:** High · **Door:** One-way · **Review by:** Apr 15
**State of mind:** Slightly anxious — pressure from board timeline
**Who's affected:** Engineering team, Series A investors, customers on waitlist

---

**THE DECISION**
How do we ship the payment integration by Q2 — build internally,
hire a specialized contractor, or delay and revisit after fundraise?

---

**OPTIONS**

**A. Build in-house.** Benefit: Full control; team builds institutional
knowledge. Risk: Current team is stretched — likely 4-month timeline,
not 2. Cost: ~$40K in opportunity cost from diverted engineering time.

**B. Do Nothing (delay 3 months).** Benefit: Preserves cash; lets us
hire post-fundraise at better rates. Risk: Waitlist customers churn;
board loses confidence. Cost of inaction: ~$80K in estimated lost
revenue; fundraise narrative weakens.

**C. Hire contractor (Acme Payments).** Benefit: Ships in 6 weeks;
team stays focused on core product. Risk: Vendor lock-in; integration
debt if we later bring in-house. Cost: $55K fixed-price contract.

---

**RECOMMENDATION:** Option C — Hire contractor · **Confidence: 70% — Moderate**
Payment integration live by March 1, unlocking ~$200K ARR from waitlist
conversion. B is close, but timeline risk is the dealbreaker given
board pressure. Worst case: $55K spent and we still rebuild in-house.

---

**THIS ASSUMES:**
(1) Acme can actually deliver in 6 weeks — they quoted 4-6.
(2) Integration debt is manageable when we bring in-house in ~12 months.
(3) Board fundraise timeline holds at Q2.

---

**PRE-MORTEM:** It's April and this failed because Acme delivered late,
we burned $55K AND still had to rebuild in-house, and the fundraise
slipped anyway — making the entire urgency argument moot.

---

**KILL CONDITIONS — I'd reverse this if:**
(1) Acme misses their first milestone by more than 1 week.
(2) Fundraise timeline moves past Q3, removing the urgency.
(3) A qualified senior engineer becomes available to hire before Feb 1.
```

**Key structural rules:**
- Options alphabetized to prevent presentation-order anchoring
- Recommendation appears after all options, never before
- Confidence is always numeric: 50-59% Lean, 60-74% Moderate, 75-84% High, 85-95% Strong
- "Do Nothing" is mandatory (status quo bias is pervasive)
- All costs are forward-looking — no sunk cost language

## 6 Silent Debiasing Mechanisms

The template's structure does cognitive work the user never sees. Warning labels ("be aware of confirmation bias") produce zero behavior change. Structural countermeasures work mechanically.

| Bias | How the Template Counters It |
|------|------------------------------|
| **Analysis paralysis** | Reversibility field (one-way/two-way door) calibrates rigor. "Decide by" deadline prevents indefinite deliberation. |
| **Anchoring** | Options alphabetized with identical formatting. Recommendation appears after all options. |
| **Sunk cost** | Forward-only language rule. Options describe future costs and benefits only. |
| **Status quo bias** | "Do Nothing" is mandatory with a "cost of inaction" field that forces explicit evaluation. |
| **Framing effects** | Identical option template. Dual-framing on recommendation (expected upside AND worst realistic downside). |
| **Confirmation bias** | Pre-mortem forces recommender to argue against their own pick. Kill conditions pre-commit to disconfirming evidence. |

Source: Kaufmann et al. (2010) meta-review of 62 debiasing studies found structure-focused interventions consistently outperformed awareness-based ones.

## Two-Way Door Compression

Bezos's reversibility heuristic: most decisions are two-way doors — changeable, reversible. These deserve fast decisions, not agonized ones.

When a decision is classified as a two-way door, the brief compresses to ~150 words:

- Skip state-of-mind and who's-affected
- Options get 1-2 lines each instead of 3-5
- Pre-mortem becomes one sentence
- Kill conditions become one trigger
- Closes with: *"This is a two-way door. The biggest risk is spending too long deciding, not deciding wrong."*

```
### DECISION BRIEF

**Date:** Jan 15, 2026 · **Decide by:** Jan 17 · **Door:** Two-way · **Review by:** Apr 15

---

**THE DECISION**
Which analytics tool do we use for the MVP — Mixpanel, Amplitude, or PostHog?

---

**OPTIONS**

**A. Amplitude.** Free tier covers MVP scale. Slightly steeper learning curve.
**B. Mixpanel.** Best onboarding flow. Free tier caps at 20M events.
**C. PostHog.** Self-hostable, open source. Smaller community.

---

**RECOMMENDATION:** Option B — Mixpanel · **Confidence: 60% — Moderate**
Fastest to value for a 2-person team. Switch cost is low if we outgrow it.

---

**THIS ASSUMES:** (1) We stay under 20M events for 6+ months. (2) Team size stays under 5.

---

**PRE-MORTEM:** We hit the event cap in month 2 and migrated under pressure.

---

**KILL CONDITION:** Monthly events exceed 15M before month 4.
```

## The Research Behind It

The template synthesizes five decision frameworks:

- **Amazon's 6-pager** — Narrative structure forces better thinking than bullet points. Silent reading eliminates presenter-charisma bias.
- **Bezos's reversibility heuristic** — One-way doors need rigor. Two-way doors need speed. Classification comes first because it determines how much analysis the decision deserves.
- **Bain's RAPID + McKinsey research** — Fast decisions are 1.98x more likely to be good decisions. The brief compresses rather than expands.
- **Military MDMP** — Criteria established before options are generated. Each option passes the same gates (suitable, feasible, acceptable).
- **Farnam Street's decision journal** — Explicit probability estimates. Power comes from the review cycle: comparing stated confidence to actual outcomes.

The core design insight: **optimize for the person re-reading it three months later**, not the person filling it out today. When decisions fail, it is almost always because a hidden assumption broke, not because the analysis was wrong. That is why assumptions and kill conditions are the review mechanism — they convert a 10-minute re-read into a 30-second checklist.

Kahneman called the pre-mortem his single most valuable decision technique. A 1989 study found "prospective hindsight" increases ability to identify failure reasons by 30%.

## Pairs With

| Skill | When to Combine |
|-------|----------------|
| **devil's-advocate** | Run before decision-maker to stress-test options under sustained adversarial pressure. The brief's pre-mortem is one stress test; devil's-advocate provides many. |
| **mental-models** | If stuck on how to frame the decision, mental-models can reframe it before decision-maker structures the choice. |
| **research-brief** | If you lack the information to evaluate options, research-brief gathers it first. Decision-maker structures what you know — it does not gather new data. |
