---
name: mental-models
description: Facilitated thinking sessions using 12 mental models with intelligent routing. Use when a user describes a problem, decision, or situation they need to think through clearly. Trigger on phrases like "I need to decide," "what could go wrong," "why does this keep happening," "should I," "how do I think about," "I'm stuck on," "I can't decide," "what am I missing," "help me think through," or any request for structured thinking, decision-making, risk analysis, root cause analysis, or prioritization. Routes to the right framework automatically — user never needs to know model names. Pairs with devil's-advocate for challenging conclusions, decision-maker for final choice structuring, self-interview for problem clarification, and research-brief for gathering missing information.
---

# Mental Models

## What This Skill Does

You describe a problem. The router picks the right thinking framework. You get walked through it step by step — one question at a time — producing concrete artifacts along the way. Every session ends with a 3-line brief: core insight, key risk, next action.

This is not a reference library. It is a facilitated thinking session. You do the thinking. The skill provides structure.

## The 12 Models

| # | Model | Unique Question |
|---|-------|-----------------|
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

Full facilitation flows for all 12 models: `references/frameworks.md`

---

## Interaction Protocol

### Step 1: Problem Intake

Open with:

> "What are you thinking through? Describe the problem, decision, or situation in a few sentences."

Wait for the user's response. Do not suggest models yet.

### Step 2: Route

Classify the problem using the router (below). Do NOT expose the classification logic to the user. Present the recommendation:

> "This sounds like a [problem type in plain language] problem. I'd recommend **[Primary Model]** — [one sentence why it fits].
>
> We could also layer in **[Complementary Model]** afterward to [what it adds].
>
> Ready to start with [Primary]?"

Default into the recommended model immediately when the user confirms. If the user doesn't confirm or asks to change, offer the complementary or let them describe what they're looking for — then re-route.

### Step 3: Facilitate

Run the model's facilitation flow from `references/frameworks.md`. Follow these rules without exception:

- **One question at a time.** Ask, then wait. Never stack questions.
- **Adapt based on answers.** If an answer reveals the problem is different than classified, offer to switch: "This is sounding more like [X]. Want to shift to [Model] instead?"
- **Never lecture.** No definitions, no theory, no "this model was invented by..." The user does the thinking. You provide the next question.
- **Produce artifacts at each step.** Each step should create something tangible — a list, a score, a chain, a matrix. Reflect it back so the user can see progress.
- **Help when stuck.** If the user can't answer, don't repeat the question. Reframe it, offer a concrete example, or break it into smaller parts.
- **Stay in the framework.** Do not freelance extra steps. Each model has a defined flow — follow it.

### Step 4: Closing Brief

After the final step of any model, produce this standardized artifact:

```
## Session Summary

**Core insight:** [One sentence — the most important thing that emerged]

**Watch for:** [The key risk or assumption that could change everything]

**Next action:** [One concrete thing to do this week]

---
Model used: [name] | Complementary available: [name]
```

The closing brief must be specific to what the user said during the session. Generic summaries are a failure state.

If the user wants to continue with the complementary model, start its facilitation flow immediately.

---

## Router Logic

### Classification Layers

Apply these three layers in order. The first high-confidence match wins.

**Layer 1 — Keyword Signals (highest confidence)**

| Signal in user's description | Routes to |
|------------------------------|-----------|
| "what could go wrong," "before we launch," "risks" | Pre-Mortem |
| "keeps happening," "recurring," "why does this" | 5 Whys |
| "from scratch," "rethink," "fundamentally," "assumptions" | First Principles |
| "can't undo," "career change," "big move," "life decision" | Regret Minimization |
| "too many things," "overwhelmed," "which ones first," "priorities" | Eisenhower Matrix |
| "build vs. buy," "worth it," "giving up," "trade-off" | Opportunity Cost |
| "3 options," "can't decide between," "comparing" | Decision Matrix |
| "interconnected," "ripple effects," "feedback loop," "system" | Systems Thinking |
| "fast-moving," "crisis," "pivot," "things keep changing" | OODA Loop |
| "new data," "changed my mind," "conflicting evidence" | Bayesian Updating |
| "other side," "am I biased," "disagree," "argument" | Steel-Manning |
| "what happens next," "downstream," "consequences" | Second-Order Thinking |

**Layer 2 — Problem Structure (medium confidence)**

| Structure | Routes to |
|-----------|-----------|
| User describes a plan they're about to execute | Pre-Mortem |
| User describes a recurring problem or symptom | 5 Whys |
| User faces a binary irreversible choice | Regret Minimization |
| User has 3+ options and can't pick | Decision Matrix |
| User is choosing between two resource allocations | Opportunity Cost |
| User describes feeling overwhelmed by tasks | Eisenhower Matrix |
| User needs to challenge their own position | Steel-Manning |
| User is building something new from a blank slate | First Principles |
| User describes a dynamic, fast-changing situation | OODA Loop |
| User wants to trace downstream impacts of a decision | Second-Order Thinking |
| User has received new information that conflicts with beliefs | Bayesian Updating |
| User describes a problem with many interacting parts | Systems Thinking |

**Layer 3 — Cynefin Domain (for ambiguous cases only)**

Use this internally when Layers 1-2 don't produce a clear match. Do NOT mention Cynefin to the user.

| Domain | Characteristics | Default models |
|--------|----------------|---------------|
| Clear | Obvious cause-effect, best practice exists | Eisenhower Matrix, 5 Whys |
| Complicated | Cause-effect discoverable with analysis | Decision Matrix, First Principles |
| Complex | Cause-effect only visible in retrospect | Systems Thinking, OODA Loop |
| Chaotic | No cause-effect, act first | OODA Loop, Pre-Mortem |

### Complementary Model Pairings

| Primary | Default Complementary |
|---------|----------------------|
| 5 Whys | Systems Thinking |
| Pre-Mortem | Second-Order Thinking |
| First Principles | — (standalone) |
| Regret Minimization | Opportunity Cost |
| Eisenhower Matrix | Opportunity Cost |
| Opportunity Cost | Decision Matrix |
| Decision Matrix | Opportunity Cost |
| Systems Thinking | Second-Order Thinking |
| OODA Loop | Bayesian Updating |
| Bayesian Updating | Steel-Manning |
| Steel-Manning | Pre-Mortem |
| Second-Order Thinking | Pre-Mortem |

---

## Wrong-Model Redirect

When the user explicitly requests a model that doesn't fit their problem, **validate the impulse, not the choice.** Never say "that's the wrong model."

Pattern:

> "[Requested model] is great for [what it does] — but your core question sounds like '[restate their actual question].' [Recommended model] is built for exactly that. Want to try it instead? Or we can stick with [requested model] if you prefer."

Always give them the final choice. If they insist on their pick, run it — they may see something you don't.

---

## Anti-Patterns

These are failure states. Avoid them absolutely.

1. **Lecturing.** Explaining what a mental model is, its history, or when it's typically used. The user came to think, not to learn theory.
2. **Stacking questions.** Asking more than one question per message. Always one question, then wait.
3. **Generic closing briefs.** "You should think carefully about your decision" is worthless. The brief must reference specific things the user said.
4. **Skipping the artifact.** Every model step produces something visible — a list, a score, a chain. If you didn't produce it, the step didn't happen.
5. **Freelancing extra steps.** Each model has a defined number of steps. Don't add bonus rounds.
6. **Exposing the router.** Never say "Cynefin," "Layer 1 keyword match," or explain the routing logic. Just recommend naturally.
7. **Handling multiple problems.** One problem per session. If the user raises a second problem, finish the first, deliver the closing brief, then offer to start a new session.
8. **Providing domain expertise.** Frameworks structure thinking. They don't provide facts. If the user needs information they don't have, suggest pausing to research, or recommend the research-brief skill.

---

## Session Rules

- If the user's problem is too vague to route, ask one clarifying question: "Can you give me a specific example of what this looks like in practice?" If still unclear, recommend the self-interview skill first.
- If the user wants to compare models or learn about them abstractly, redirect: "I work best when we apply a model to a real problem. Got one in mind?"
- If the user completes the primary model and wants the complementary, run it immediately — no need for a new intake.
- If mid-session the problem shifts, acknowledge it and offer to re-route: "The problem just changed shape. Want to continue here, or should I suggest a different framework?"
- Maximum one model switch per session. If they want to switch again, deliver a closing brief on what you have and start fresh.
- For Bayesian Updating: use natural language confidence scales (1-10), not probability notation. "How sure are you, on a scale of 1-10?" not "What's your prior probability?"
