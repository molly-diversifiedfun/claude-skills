# PRD: mental-models

## Problem

People know they should "think more clearly" but don't know which framework applies to their specific problem. There are hundreds of named mental models — the paradox of choice prevents action. When they do pick one (usually First Principles, because it's famous), they can't facilitate it themselves. Existing tools are either developer-only CLIs (CC-Thinking-Skills), static reference sites (Untools.co), or shallow ChatGPT templates. No tool combines intelligent problem routing with interactive step-by-step facilitation.

## Solution

A skill with 12 thinking frameworks and a router. Describe your problem, the router recommends the right model (1 primary + 1 complementary), then walks you through it step-by-step — asking questions, producing artifacts, and closing with a concrete next action. Not a reference library — a facilitated thinking session.

## The 12 Models

| # | Model | Unique Question It Answers | Steps | Time |
|---|-------|---------------------------|-------|------|
| 1 | First Principles | "What's actually true underneath all the assumptions?" | 6 | ~12 min |
| 2 | Pre-Mortem | "What specific risks am I blind to?" | 5 | ~8 min |
| 3 | Second-Order Thinking | "What happens after what happens next?" | 4 | ~8 min |
| 4 | Regret Minimization | "Will I regret not doing this in 20 years?" | 4 | ~6 min |
| 5 | Opportunity Cost | "What am I invisibly giving up by choosing this?" | 4 | ~7 min |
| 6 | Eisenhower Matrix | "Am I spending time on urgent trivia instead of important work?" | 3 | ~5 min |
| 7 | OODA Loop | "How do I act decisively when the situation keeps changing?" | 4 | ~8 min |
| 8 | Systems Thinking | "How do these parts interact and create feedback loops?" | 5 | ~10 min |
| 9 | Bayesian Updating | "How should this new evidence change my confidence?" | 4 | ~7 min |
| 10 | Steel-Manning | "What's the strongest version of the argument I disagree with?" | 5 | ~10 min |
| 11 | 5 Whys | "What's the root cause underneath the symptoms?" | 5 | ~7 min |
| 12 | Decision Matrix | "How do these 3+ options compare across my criteria?" | 5 | ~10 min |

**Cut and why:** Inversion (overlaps Pre-Mortem), 10/10/10 (overlaps Regret Minimization + Second-Order Thinking), Cynefin (absorbed into router logic), SCAMPER (too narrow).

**Added:** Decision Matrix — fills the common "I have 3 options and can't decide" gap no candidate on the original list addressed.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Router recommendation count | **1 primary + 1 complementary** | Single-option presentation reduces engagement ~70% (Mochon 2013). Two gives choice without paralysis. |
| Cynefin role | **Router-internal, not user-facing** | Exposing it creates recursion (router picks Cynefin, Cynefin says "use another model"). Use its domain classification (Clear/Complicated/Complex/Chaotic) as the router's first-pass filter. |
| Bayesian Updating accessibility | **Natural frequencies, not probabilities** | "On a scale of 1-10, how sure are you?" instead of "What's your prior probability?" Gigerenzer & Hoffrage (1995): natural frequencies dramatically improve Bayesian reasoning in non-experts. |
| Router override | **Default into recommended model with escape hatch** | "Let's use a Pre-Mortem. Here's step 1..." but "If this doesn't feel right, I can suggest alternatives." Most users follow the default. |
| Session closing artifact | **Standardized 3-line brief after every model** | (1) Core insight/decision, (2) Key risk/assumption to watch, (3) Immediate next action. Portable and actionable regardless of which model was used. |
| Wrong-model redirect | **Validate the impulse, not the choice** | "Eisenhower is great for prioritization — but your core question sounds like 'why does this keep happening.' Want to try 5 Whys?" Never say "that's the wrong model." |

## Interaction Model

### Step 1: Problem Intake (30 sec)

"What are you thinking about? Describe the problem, decision, or situation in a few sentences."

### Step 2: Router (automatic)

The router classifies using three signal layers:
1. **Keywords** (highest confidence): "what could go wrong" → Pre-Mortem, "keeps happening" → 5 Whys
2. **Problem structure**: temporal orientation, constraint signals, emotional valence
3. **Cynefin domain** (meta-filter for ambiguous cases): Clear → simple frameworks, Complex → Systems Thinking / OODA

Router output to user:

> "This sounds like a [problem type] problem. I'd recommend **[Primary Model]** — it's designed for [one sentence why].
>
> We could also layer in **[Complementary Model]** to [what it adds].
>
> Want to start with [Primary]?"

### Step 3: Facilitated Session

Each model has a defined facilitation flow (see below). Core principles across all models:
- **One question at a time.** Wait for the answer.
- **Adapt based on answers.** If an answer reveals the problem is different than initially classified, offer to switch models.
- **Never lecture.** The user does the thinking; the skill provides structure.
- **Produce artifacts at each step.** Each step creates a tangible output (risk list, assumption list, causal chain, scored matrix).

### Step 4: Closing Brief (automatic)

Every session ends with:

```
## Session Summary

**Core insight:** [One sentence — the most important thing that emerged]

**Watch for:** [The key risk or assumption that could change everything]

**Next action:** [One concrete thing to do this week]

---
Model used: [name] | Complementary available: [name]
```

## Facilitation Flows (Top 5)

### Pre-Mortem (5 steps, ~8 min)

1. "Describe the plan you're about to execute in 2-3 sentences."
2. "Imagine it's [timeframe] from now and this has failed spectacularly. Don't hold back — what happened?"
3. Extract 3-5 discrete risk factors. Ask "What else?" until dry.
4. Score each: "How likely (1-5)? How damaging if it happens (1-5)?"
5. For top 2-3 risks: "What's one concrete thing you could do this week to reduce this risk?"

**Artifact:** Scored risk matrix + mitigation action plan.

### First Principles (6 steps, ~12 min)

1. "What are you trying to solve or build? One sentence."
2. "What are you taking for granted? List everything you assume is true." (Aim for 5-8)
3. For each assumption: "Is this actually true, or is it convention? What evidence supports it?"
4. "Strip away the questionable assumptions. What remains that's definitely true?" (2-4 bedrock truths)
5. "Given only these truths, what solutions become possible that weren't visible before?"
6. "Which is most realistic? What's the first step?"

**Artifact:** Assumption audit → first principles → reframed solution + next action.

### Regret Minimization (4 steps, ~6 min)

1. "What's the choice? State both options clearly."
2. "You're 80, looking back. For each option: what would you specifically regret?"
3. "Which regrets come from genuine values, and which come from fear of discomfort?"
4. "Which path minimizes your deepest regret? What's one thing you'd do this week?"

**Artifact:** Regret analysis → decision + first action.

### 5 Whys (5 steps, ~7 min)

1. "What's the problem as you see it right now?"
2. "Why is that happening?" (probe if vague)
3-4. Two more rounds of "Why?" — watching for logic jumps, asking for evidence.
5. "We've reached a cause you can act on. What would change if you addressed this directly?"

**Artifact:** 5-level causal chain → root cause → intervention plan.

### Steel-Manning (5 steps, ~10 min)

1. "What's your current view on this?"
2. "Who disagrees, and what's their position?"
3. "Now argue their side as persuasively as you can. What evidence supports them?"
4. "Where does their strongest point directly challenge your weakest assumption?"
5. "Do you want to modify your position, add a caveat, or address the vulnerability?"

**Artifact:** Steel-manned opposition → tension point → refined position.

## Remaining 7 Models (abbreviated flows)

**Second-Order Thinking:** State the action → "What happens next?" → "And then what happens?" → chain 3-4 consequences → identify non-obvious effects → decide whether the second/third-order effects change the decision.

**Opportunity Cost:** State what you're choosing → "What's the best alternative you're NOT choosing?" → Quantify the value of each → "Is the gap worth it?" → Name the invisible price.

**Eisenhower Matrix:** List everything on your plate → Classify each (Urgent+Important / Important+Not Urgent / Urgent+Not Important / Neither) → Identify what to delegate or eliminate → Focus plan for Important+Not Urgent items.

**OODA Loop:** Observe (what do you see happening right now?) → Orient (what does this mean given your context?) → Decide (what's the minimum viable action?) → Act → cycle back to Observe with new data.

**Systems Thinking:** Define the system boundary → Map the key components → Identify feedback loops (reinforcing and balancing) → Find leverage points → "Where would a small change produce the biggest effect?"

**Bayesian Updating:** State your current belief + confidence (1-10) → Present the new evidence → "Does this evidence change your confidence? By how much?" → Recalibrate → "What evidence would move you significantly in either direction?"

**Decision Matrix:** List options → Define 3-5 criteria → Weight criteria (must-have vs. nice-to-have) → Score each option on each criterion → Calculate weighted totals → Sensitivity check: "If you changed the top weight, would the winner change?"

## Success Criteria

- Router matches the right model in >80% of cases (measured by whether users stay or redirect)
- Users complete the facilitation flow (don't abandon mid-session)
- The closing brief is specific enough that someone who didn't see the session understands the insight
- Each model produces a distinct artifact (not generic advice)
- Users return to try different models on different problems

## What This Skill Does NOT Do

- Teach mental model theory (no lectures — just facilitation)
- Handle more than one problem per session (stay focused)
- Replace domain expertise (frameworks structure thinking, they don't provide facts)
- Guarantee the "right" answer (frameworks improve decision quality on average, not every time)

## Pairs With

- **devil's-advocate**: After a mental model session, challenge the conclusion
- **decision-maker**: If the model leads to a choice between options, decision-maker structures the final brief
- **self-interview**: If the user can't articulate the problem clearly enough for routing, self-interview helps first
- **research-brief**: If the user lacks information to feed into a model, research-brief gathers it
