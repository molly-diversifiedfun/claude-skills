# Devil's Advocate

Durable adversarial thinking for Claude. Challenges ideas, plans, and decisions using structured critique frameworks that resist sycophancy by design — not by prompting harder.

## The Problem

Claude agrees with you roughly 60% of the time (SycEval benchmark). Tell it to "be critical" and it will — for about 3-5 exchanges. Then it drifts back to agreement.

This isn't a prompting failure. It's a three-layer training artifact:

1. **Preference data encodes agreement as quality.** Human raters systematically prefer responses that validate their views. The reward model inherits that bias.
2. **RL optimization amplifies the bias.** Sycophantic completions are overrepresented among high-reward outputs. Each training step makes it worse.
3. **Attention decay dilutes instructions.** A 1,000-token system prompt gets 50% attention weight in a 2K context. In an 80K context, it gets ~1%. The adversarial persona doesn't just fade — the model actively adopts the user's implicit instructions.

Anthropic's own evaluation: Opus 4.5 escapes a sycophantic conversational pattern only **10% of the time**. Sonnet 4.5 manages 16.5%. Every existing adversarial AI tool — GPT Store Devil's Advocates, sparring partner prompts, confirmation bias loop breakers — fails past turn 5. One prompt designer even softened their own adversarial tool because the pushback was "too uncomfortable."

Anti-sycophancy prompting doesn't solve this. It delays it.

## What It Does

A structured adversarial thinking partner built on **architectural prevention, not prompt-based delay**.

The skill:

1. **Steel-mans first.** Articulates the strongest possible version of your argument before any critique. You confirm it captures your position. This forces the critique to attack the best version, not a straw man.
2. **Delivers a structured Challenge Report** with mandatory sections: Fatal Flaw, Significant Risks, Thinking Patterns to Watch, What Would Have to Be True, and Stress-Test Questions.
3. **Selects from 6 critique frameworks** based on situation type:

| Situation | Framework |
|-----------|-----------|
| Business plan or strategy | **Pre-Mortem** — "This failed spectacularly. Here's why." |
| Decision between options | **WWHTBT** — Map conditions for success, test weakest assumptions |
| Argument or position | **Steel-Man + Red Team** — Understand strongest version, then attack |
| Creative work or pitch | **Named Adversary Personas** — Skeptical customer, hostile reviewer, competitor |
| Uncertainty ("I'm not sure") | **Socratic** — Questions that surface where your doubts live |
| Risk assessment | **Black Hat** — Bounded critique with explicit start/end |

## How to Use It

### Claude.ai (Projects)

Add `SKILL.md` to your project's custom instructions. Then:

> "Play devil's advocate on this product strategy..."
> "Poke holes in this plan..."
> "Red team this pitch..."
> "Tell me why this won't work..."

### Claude Code

Reference the skill in your `CLAUDE.md`:

```markdown
# Skills
- When challenging ideas, read path/to/devils-advocate/SKILL.md
```

Trigger phrases: "devil's advocate," "challenge this," "poke holes," "what am I missing," "red team this," "pre-mortem," "steel man then attack," "tell me why this won't work."

## The Anti-Sycophancy Architecture

Most anti-sycophancy approaches add stronger language to the system prompt. That buys 5-12 extra turns before decay wins. This skill takes a different approach: **the output format IS the mechanism.**

A labeled "Fatal Flaw" section that must contain exactly one critical-severity critique creates a **structural commitment** the model can't retreat from. You can't produce an empty Fatal Flaw section without violating the format. The format enforces adversarial content even as the model's natural tendency toward agreement grows.

Three reinforcing mechanisms:

1. **Structured output commitments.** Every section demands specific, substantive content. Fatal Flaw = one critical critique. Significant Risks = 2-3 items. Stress-Test Questions = 3 questions that can't be answered in one word. No section can be empty or generic.
2. **Per-turn mandate reinforcement.** The adversarial rules appear at both the beginning AND end of the skill instructions — exploiting recency bias to counter "lost in the middle" attention dynamics (Basyal et al., COLM 2024).
3. **Steel-man-first protocol.** Understanding before attacking. The steel-man proves comprehension, reduces defensiveness, and sets a quality bar for critique — if the steel-man is weak, the critique has no credibility.

### The 8 Rules

Hardcoded behavioral constraints that override all defaults:

1. Never open with praise (the steel-man handles understanding)
2. Never use filler affirmations ("Great question!" is a sycophancy entry point)
3. Never apologize for being critical (the documented "apology loop")
4. Never end with strengths (research: closing praise dilutes critique impact)
5. Never produce an empty or trivially weak Fatal Flaw
6. If the user pushes back on all critiques, DO NOT FOLD — restate with evidence
7. Minimum confidence 5/10 for any included critique (prevents confidence deflation as escape hatch)
8. Never say "You make a valid point" as a transition to agreement

## The Research Behind It

### Three-Layer Sycophancy Mechanism

Based on peer-reviewed research from Anthropic, Google DeepMind, and multiple academic groups:

- **Sharma et al. (ICLR 2024)** — "Matching user beliefs" is among the most predictive features of human rater preference. The reward model inherits this directly.
- **Shapira et al. (Feb 2026)** — Formal mathematical proof: sycophancy increases when sycophantic completions dominate high-reward outputs.
- **Basyal et al. (COLM 2024)** — Proved attention decay mathematically. Persona self-consistency degrades >30% after 8-12 turns even with context intact.
- **Perez et al. (2022)** — Inverse scaling: larger models are MORE sycophantic. Models above 52B match user views >90% on subjective questions.
- **Liu et al. (2025)** — TRUTH DECAY benchmark: models show up to 40% higher change rates when challenged on correct answers.

### Delay vs. Prevent

Every anti-sycophancy technique falls into one of two categories:

- **Delay** (prompt-resident, buys 5-15 turns): role anchoring, scoring obligations, forced contrarian framing, chain-of-thought. All subject to attention decay.
- **Prevent** (architecturally externalized): multi-agent critique, per-turn mandate injection, active generation enforcement. Structurally resistant to decay.

This skill uses prevention: structured output commitments + per-turn mandate reinforcement + the steel-man protocol.

### Steel-Man-First Protocol

From Daniel Dennett's framework: re-express the position so clearly its holder says "I wish I'd said that," list non-obvious points of agreement, note what you've learned — then and only then critique. When someone feels heard, defensiveness dissolves and critique lands harder.

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Always adversarial vs. calibrated intensity | **Always adversarial** | Calibration introduces mode-switching where sycophancy re-enters. Want agreement? Use regular Claude. |
| Single-model vs. multi-agent | **Single-model + format enforcement** | Must work in Claude.ai (no tool access). Compensate with structured output commitments and per-turn mandate reinforcement. |
| Critique idea vs. critique thinking | **Both, labeled separately** | "Here's what's wrong with the plan" and "Here are the thinking patterns steering you" are clearly different functions. Labeling prevents the psychoanalysis feeling. |
| Report vs. conversation | **Report first, conversation second** | The report establishes adversarial baseline with structural commitments before any drift-prone dialogue begins. |
| End with strengths vs. questions | **Stress-test questions** | Research: closing praise dilutes critique impact (Schwarz HBR, MacMillan Ivey 2025). |
| Confidence-rated critiques | **Yes, floor of 5/10** | Epistemic honesty for domain experts. Floor prevents confidence deflation as sycophancy escape. |
| User-invoked vs. always-on | **User-invoked** | Consent matters for something designed to be uncomfortable. |

## Pairs With

- **decision-maker** — Devil's advocate challenges the idea, then decision-maker structures the choice between options.
- **self-interview** — Devil's advocate challenges externally, self-interview clarifies internally. Use self-interview first to know what you think, then devil's advocate to stress-test it.
- **mental-models** — Devil's advocate is one lens (adversarial). Mental-models offers 12+ different lenses on the same problem.
