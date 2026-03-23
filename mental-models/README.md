# Mental Models

## The Problem

There are hundreds of named mental models. The paradox of choice means most people either pick the famous one (First Principles, because Elon said so) or pick none at all.

When they do pick one, they can't facilitate it themselves. Asking "what are my assumptions?" into the void produces nothing. You need a counterpart asking the right follow-up questions at the right time.

Existing tools don't solve this:

- **Developer-only CLIs** (CC-Thinking-Skills) — 39 models, no interactive facilitation, 10 GitHub stars
- **Static reference sites** (Untools.co) — best explanations on the web, zero AI integration
- **ChatGPT templates** — one-shot, no routing, reviews say "long, rambly, and not practical"
- **Anthropic's prompt library** — 60+ templates, nothing for structured thinking frameworks

The gap: no tool combines intelligent problem-type routing with interactive step-by-step facilitation.

## What It Does

12 thinking frameworks. One intelligent router. You describe your problem, the router recommends the right model (1 primary + 1 complementary), then walks you through it — one question at a time. Each step produces a concrete artifact. Every session closes with a 3-line brief: core insight, key risk, next action.

Not a reference library. A facilitated thinking session.

## The 12 Models

| # | Model | The Question It Answers |
|---|-------|------------------------|
| 1 | First Principles | What's actually true underneath all the assumptions? |
| 2 | Pre-Mortem | What specific risks am I blind to? |
| 3 | Second-Order Thinking | What happens after what happens next? |
| 4 | Regret Minimization | Will I regret not doing this in 20 years? |
| 5 | Opportunity Cost | What am I invisibly giving up by choosing this? |
| 6 | Eisenhower Matrix | Am I spending time on urgent trivia instead of important work? |
| 7 | OODA Loop | How do I act decisively when the situation keeps changing? |
| 8 | Systems Thinking | How do these parts interact and create feedback loops? |
| 9 | Bayesian Updating | How should this new evidence change my confidence? |
| 10 | Steel-Manning | What's the strongest version of the argument I disagree with? |
| 11 | 5 Whys | What's the root cause underneath the symptoms? |
| 12 | Decision Matrix | How do these 3+ options compare across my criteria? |

## How to Use It

### Claude.ai

Add the skill to your project, then describe your problem naturally:

- "I'm about to launch this feature and I want to stress-test the plan"
- "I keep having the same argument with my cofounder about pricing"
- "I have three job offers and can't decide"

You never need to know model names. The router handles it.

### Claude Code

Reference the skill directly:

```
When I describe a problem, use the mental-models skill from ~/claude-code-toolkit/skills/mental-models/SKILL.md
```

Or add it to your project's `.claude/settings.json` as a slash command.

## How the Router Works

Three classification layers, applied in order. First high-confidence match wins.

1. **Keyword signals** — Phrases like "what could go wrong" route to Pre-Mortem, "keeps happening" routes to 5 Whys, "can't decide between" routes to Decision Matrix
2. **Problem structure** — Binary irreversible choice routes to Regret Minimization, 3+ options routes to Decision Matrix, recurring symptom routes to 5 Whys
3. **Cynefin domain (internal only)** — For ambiguous cases, classifies the problem as Clear/Complicated/Complex/Chaotic and maps to appropriate frameworks. Never exposed to the user.

Every recommendation includes 1 primary + 1 complementary model. Single-option presentation reduces engagement ~70% (Mochon 2013). Two gives choice without paralysis.

## The Research Behind It

### The overlap test that cut 4 candidates

Started with 16 candidates. Ran pairwise overlap analysis:

- **Inversion** — absorbed into Pre-Mortem (prospective hindsight framing surfaces 30% more risks than direct critique)
- **10/10/10 Rule** — overlaps Regret Minimization + Second-Order Thinking
- **Cynefin** — creates recursion if user-facing (router picks Cynefin, Cynefin says "use another model"). Absorbed into router logic.
- **SCAMPER** — too narrow for "messy problem to decision" flow. First Principles covers the rethink-from-scratch case.

**Added:** Decision Matrix. No original candidate handled the common "I have 3 options and can't pick" problem.

### Empirical evidence

Most mental models rest on practitioner authority alone. Three have controlled studies:

- **Pre-Mortem** — Prospective hindsight increases correct identification of failure causes by 30% (Mitchell, Russo & Pennington 1989). Outperforms standard critique, pros/cons, and cons-only analysis at reducing overconfidence (Veinott, Klein & Wiggins 2010).
- **Bayesian Updating** — Superforecasters using probabilistic updating performed 30% better than intelligence analysts with classified access (Tetlock's Good Judgment Project).
- **Steel-Manning / Consider-the-Opposite** — Multiple RCT-equivalent studies show it reduces anchoring bias, confirmation bias, and overconfidence (Lord, Lepper & Preston 1984; Mussweiler, Strack & Pfeiffer 2000).

For First Principles, Eisenhower, OODA, 5 Whys, and the rest: zero controlled studies testing them against alternatives.

### Bayesian Updating accessibility

Natural frequencies instead of probability notation. "How sure are you, on a scale of 1-10?" not "What's your prior probability?" Gigerenzer & Hoffrage (1995) showed this dramatically improves Bayesian reasoning in non-experts.

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Models per recommendation | 1 primary + 1 complementary | Single-option reduces engagement ~70%. Two gives choice without paralysis. |
| Cynefin role | Router-internal only | User-facing creates recursion. Use its domain classification as first-pass filter for ambiguous cases. |
| Bayesian notation | Natural frequencies (1-10 scale) | Non-experts can't reason with raw probabilities. Natural frequencies fix this. |
| Router override behavior | Default into recommendation with escape hatch | Most users follow the default. Always give final choice to the user. |
| Wrong-model redirect | Validate the impulse, not the choice | "Eisenhower is great for prioritization -- but your core question sounds like 'why does this keep happening.'" Never say "wrong model." |
| Session closing | Standardized 3-line brief | Core insight, key risk, next action. Portable across all 12 models. Must reference specific things the user said. |
| Questions per message | Exactly one | Stacking questions is a failure state. Ask, then wait. |
| Lectures | Banned | No definitions, no theory, no history. The user came to think, not to learn. |

## Pairs With

| Skill | When to Chain |
|-------|---------------|
| **devil's-advocate** | After a mental model session, challenge the conclusion before committing |
| **decision-maker** | When the model leads to a choice between options, structure the final brief |
| **self-interview** | When the user can't articulate the problem clearly enough for routing |
