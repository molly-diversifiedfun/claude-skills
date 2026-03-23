# Mental Models — Research Results

The strongest evidence favors **12 models with 4 cuts from your candidate list and 1 addition** — a Weighted Decision Matrix earns its place because no listed candidate handles multi-option comparison. The most important design insight: **Pre-Mortem, Inversion, and Second-Order Thinking** produce dangerously similar outputs on risk-related problems, so your set needs aggressive deduplication. Three models have strong empirical backing (Pre-Mortem, Bayesian Updating, Steel-Manning/Consider-the-Opposite); most others rest on practitioner authority alone. The router should recommend **1 primary model + 1 complementary**, using Cynefin's domain logic as its internal classifier rather than exposing Cynefin as a user-facing model.

---

## Q1: Fourteen candidates enter, twelve survive

### The empirical evidence is thinner than expected

Decision science gives us surprisingly few controlled studies comparing named frameworks. **Pre-Mortem has the strongest experimental support**: Mitchell, Russo & Pennington (1989) found prospective hindsight increases correct identification of failure causes by **30%**, and Veinott, Klein & Wiggins (2010) demonstrated it outperforms standard critique, pros/cons listing, and cons-only analysis at reducing overconfidence. Consider-the-Opposite (the mechanism behind both Inversion and Steel-Manning) has multiple RCT-equivalent studies showing it reduces anchoring bias, confirmation bias, and overconfidence (Lord, Lepper & Preston, 1984; Mussweiler, Strack & Pfeiffer, 2000). Bayesian Updating draws on Tetlock's Good Judgment Project, where superforecasters using probabilistic updating performed **30% better than intelligence analysts with classified access**.

For everything else — First Principles, Eisenhower Matrix, OODA Loop, SCAMPER, Regret Minimization, 5 Whys — **zero controlled studies exist** testing them against alternatives.

### The overlap analysis

**Inversion vs. Pre-Mortem.** Both generate lists of failure modes. Pre-Mortem wins: prospective hindsight framing surfaces 30% more risks than direct critique, and its facilitation flow is more structured for chat.

**10/10/10 Rule vs. Regret Minimization.** Both project forward in time. Regret Minimization wins: stronger emotional framing for conversational interface, Bezos credibility.

**Cynefin as model vs. router.** Making it user-facing creates recursion (router picks Cynefin, Cynefin says "use another model"). Belongs inside the router's classification logic.

**SCAMPER.** Too narrow for "messy problem → decision" flow. First Principles covers the "rethink from scratch" use case.

### Per-model evaluation

| # | Model | Distinctiveness | Teachability | Breadth | Unique question |
|---|-------|----------------|-------------|---------|-----------------|
| 1 | First Principles | HIGH | MEDIUM | WIDE | "What's actually true underneath all the assumptions?" |
| 2 | Pre-Mortem | HIGH | HIGH | WIDE | "What specific risks am I blind to in this plan?" |
| 3 | Second-Order Thinking | HIGH | HIGH | WIDE | "What happens after what happens next?" |
| 4 | Regret Minimization | HIGH | HIGH | MODERATE | "Will I regret not doing this in 20 years?" |
| 5 | Opportunity Cost | MEDIUM-HIGH | HIGH | WIDE | "What am I invisibly giving up by choosing this?" |
| 6 | Eisenhower Matrix | HIGH | HIGH | NARROW | "Am I spending time on urgent trivia instead of important work?" |
| 7 | OODA Loop | HIGH | MEDIUM | MODERATE | "How do I act decisively when the situation keeps changing?" |
| 8 | Systems Thinking | HIGH | MEDIUM | WIDE | "How do these parts interact and create feedback loops?" |
| 9 | Bayesian Updating | HIGH | LOW-MEDIUM | WIDE | "How should this new evidence change my confidence?" |
| 10 | Steel-Manning | HIGH | HIGH | MODERATE | "What's the strongest version of the argument I disagree with?" |
| 11 | 5 Whys | HIGH | HIGH | MODERATE | "What's the root cause underneath the symptoms?" |
| 12 | Decision Matrix | HIGH | HIGH | WIDE | "How do these 3+ options actually compare across my criteria?" |

---

## Q2: Router design

### Problem taxonomy — 10 types mapped to models

| Problem type | Trigger signals | Primary | Complementary |
|-------------|----------------|---------|---------------|
| Root cause diagnosis | "why," "keeps happening," "recurring" | 5 Whys | Systems Thinking |
| Risk anticipation | "what could go wrong," "before we launch" | Pre-Mortem | Second-Order Thinking |
| Innovation / reimagination | "from scratch," "rethink," "fundamentally" | First Principles | — |
| Irreversible life decision | "can't undo," "career change," "big move" | Regret Minimization | Opportunity Cost |
| Prioritization / triage | "too many things," "which ones first" | Eisenhower Matrix | Opportunity Cost |
| Trade-off comparison | "build vs. buy," "worth it," "giving up" | Opportunity Cost | Decision Matrix |
| Multi-option selection | "3 options," "can't decide between" | Decision Matrix | Opportunity Cost |
| Complex system problem | "interconnected," "ripple effects," "feedback" | Systems Thinking | Second-Order Thinking |
| Rapid response / crisis | "fast-moving," "crisis," "pivot now" | OODA Loop | Bayesian Updating |
| Belief/evidence evaluation | "new data," "conflicting opinions" | Bayesian Updating | Steel-Manning |
| Argument / position testing | "other side," "am I biased" | Steel-Manning | Pre-Mortem |

### Present 1 + 1

Mochon (2013): single-option presentation reduces engagement by ~70%. Present one highlighted default plus one complementary: "I'd suggest Pre-Mortem for this. We could also layer in Second-Order Thinking afterward. Want to start?"

### Graceful redirect

When user picks a poor-fit model, validate the impulse, not the choice: "Eisenhower is great for prioritization — but it sounds like your core question is 'why does this keep happening.' Want to try 5 Whys instead?"

---

## Q3: Facilitation flows for top five

### Pre-Mortem (5 steps, ~8 min)
1. State the plan (2-3 sentences)
2. Project forward: "Imagine it's [timeframe] from now and this failed spectacularly. What happened?"
3. Extract 3-5 discrete risk factors
4. Score likelihood and impact (1-5 each)
5. Mitigation actions for top 2-3 risks → **Artifact: risk-mitigation action plan**

### First Principles (6 steps, ~12 min)
1. Name the problem (one sentence)
2. Surface assumptions (list 5-8)
3. Challenge each: "Is this true, or convention?"
4. Identify fundamentals (2-4 bedrock truths)
5. Rebuild from fundamentals (2-3 novel approaches)
6. Feasibility check → **Artifact: reframed solution + next action**

### Regret Minimization (4 steps, ~6 min)
1. Frame the decision (both options clearly)
2. Project to age 80: specific regret per option
3. Separate fear from regret (values-based vs. fear-based)
4. Commit + first step → **Artifact: decision + first action**

### 5 Whys (5 steps, ~7 min)
1. State the symptom
2-4. Three rounds of "Why?" with evidence probing
5. Root cause → intervention plan → **Artifact: causal chain + intervention**

### Steel-Manning (5 steps, ~10 min)
1. State your position
2. Identify the opposition
3. Build the strongest opposing case
4. Find the tension point
5. Refine or revise → **Artifact: refined position statement**

---

## Q4: Competitive landscape

**CC-Thinking-Skills** (tjboudreaux): 39 models, 3-layer routing, but locked to CLI, no interactive facilitation, 10 GitHub stars.

**ChatGPT GPT Store**: uniformly weak — one-shot templates, no routing, reviews describe "long, rambly, and not practical."

**Anthropic's prompt library**: ~60 templates but nothing for structured thinking frameworks. Genuine first-mover gap.

**Untools.co**: Best model explanations and manual routing, but static with no AI integration.

**The gap**: No tool combines intelligent problem-type routing with interactive step-by-step facilitation for a general audience.

---

## The Final 12

| # | Model | Problem type trigger | Priority |
|---|-------|---------------------|----------|
| 1 | First Principles | Innovation, convention-challenging | HIGH |
| 2 | Pre-Mortem | Plan stress-testing, launch prep | HIGH |
| 3 | Second-Order Thinking | Downstream impact, policy/strategy | HIGH |
| 4 | Regret Minimization | Life-changing choices, one-way doors | HIGH |
| 5 | Opportunity Cost | Resource trade-offs, build vs. buy | HIGH |
| 6 | Eisenhower Matrix | Overwhelm, prioritization | MEDIUM |
| 7 | OODA Loop | Crisis response, incomplete info | MEDIUM |
| 8 | Systems Thinking | Interconnected problems, org dynamics | HIGH |
| 9 | Bayesian Updating | Conflicting data, forecast revision | MEDIUM |
| 10 | Steel-Manning | Debates, checking bias | HIGH |
| 11 | 5 Whys | Recurring failures, diagnostics | HIGH |
| 12 | Decision Matrix | Multiple competing options | HIGH |

**Cut**: Inversion (overlaps Pre-Mortem), 10/10/10 (overlaps Regret Minimization + SOT), Cynefin (absorbed into router), SCAMPER (too narrow).

---

## Design decisions

> **Cynefin as user model vs. router logic:** Router-internal. Surface only when problem is genuinely ambiguous.

> **Models recommended per problem:** 1 primary + 1 complementary. Single-option presentation reduces engagement ~70%.

> **Inversion survival:** Cut. Absorbed into Pre-Mortem and Steel-Manning.

> **Bayesian Updating teachability:** Simplified with natural frequencies and confidence scales instead of probability notation. Gigerenzer & Hoffrage (1995) showed this dramatically improves Bayesian reasoning in non-experts.

> **Router override:** Default into recommended model immediately with escape hatch.

> **Session artifact:** Every session closes with a 3-line brief: (1) core insight/decision, (2) key risk/assumption to watch, (3) immediate next action. Model-specific artifacts live above this.
