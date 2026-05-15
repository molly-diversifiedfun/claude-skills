---
name: explain-like
description: Explain a concept by mapping it onto a domain the user already knows deeply. Activate when the user wants something explained through the lens of their own expertise (cooking, sailing, litigation, gardening, basketball, accounting), wants a "real ELI5" that doesn't patronize, says "explain X to me like I'm a [role]," asks "make this make sense to a [role]," wants to understand a concept from another field, says they're stuck on a topic and need a fresh angle, or mentions analogy, metaphor, mental model, or "explain it through the lens of." NOT for generic simplification — this skill grounds the explanation in the user's stated domain.
---

# Explain Like

## What This Skill Does

Takes a concept the user wants explained and a domain they already know deeply. Produces a structurally-mapped analogy at a calibrated explanation level, with explicit markers for where the analogy breaks down.

The mapping is relational, not surface-level. The level is calibrated to prior knowledge, not chronological age. The breakdown markers are mandatory, not optional.

## What This Skill Does NOT Do

- Generic "explain like I'm 5" simplification with kid-friendly language. If the user doesn't give a domain, ask for one.
- Mnemonics or memorization aids (different cognitive task)
- Full course material or lesson plans (this is single-concept explanation)
- Multi-domain mashups ("explain ML using cooking AND sailing AND chess")
- Force an analogy when no structural mapping exists — refuse instead
- Patronize adult learners. A 40-year-old chef who doesn't know distributed systems is not a child.

---

## Phase 1: Two Questions (sometimes three)

Ask both at once. Do not drip them.

> 1. What concept do you want explained?
> 2. What's a domain you already know well — well enough that I can use it as a lens? (Examples: cooking, sailing, litigation, gardening, accounting, basketball, parenting, music, woodworking.)

If the user seems uncertain about depth they want, add:

> 3. What level do you want? Pick one or say "you guess."
>    - Level 1: Just-introduced novice. I've never heard of this.
>    - Level 2: Curious beginner. I've heard the term, want the basic shape.
>    - Level 3: Informed adult. I want the mechanism + tradeoffs.
>    - Level 4: Practitioner peer. I want the nuance and where it breaks.
>    - Level 5: Expert. Compress it for me, point me at the open questions.

If the user gives a concept but no domain: ask for the domain. Do not invent one. Do not default to "cooking" or any stock domain.

If the user gives a domain that's extremely narrow ("I only know about 17th-century Dutch shipbuilding"): accept it. Narrow domains often produce the best mappings because the user holds the structural knowledge tightly.

---

## Phase 2: Structural-Mapping Check (silent, before delivering)

This is the core of the skill. Run this internally before writing anything.

### Step 1: List the core relations in the target concept

Not the attributes. The *relations*. For "gradient descent" the relations are:

- A surface has a slope at every point
- The slope tells you a direction
- Following the slope reduces a value
- The step size affects what you find
- Repeating the step converges (or doesn't)

Notice: none of these mention math, vectors, or learning rates. Those are the labels. The relations are what need to map.

### Step 2: Find the corresponding relations in the user's domain

If the user said "hiking in mountains":

- A mountain has a tilt at every point ✓
- The tilt tells you which way is downhill ✓
- Following the tilt reduces altitude ✓
- Step size affects where you land ✓
- Repeating the step gets you to the bottom ✓

Five-for-five. Strong mapping. Proceed.

If the user said "carpentry" for "quantum entanglement":

- Two particles correlated regardless of distance? Carpentry has joints, but joints are physically connected. No relation maps.
- Measuring one instantly determines the other? No analog. Carpentry doesn't have non-local correlations.

Zero-for-five. No structural mapping. Refuse.

### Step 3: Score the mapping

- **3+ relations map cleanly:** Proceed. This is a strong analogy.
- **1-2 relations map:** Proceed cautiously. Lean heavily on breakdown markers. Tell the user upfront which relations work and which don't.
- **0 relations map:** Refuse. Use one of the three refusal patterns below.

### Step 4: Distinguish surface from structural mapping

Surface mapping: the *labels* line up. ("Atoms have a nucleus, like the sun is at the center of the solar system.")

Structural mapping: the *relations* line up. ("Atoms have a small central object that other small objects orbit around, bound by an attractive force — same shape of relations as a solar system.")

If only the surface lines up, the analogy will mislead. Refuse or pivot domains.

---

## Phase 3: The Three Refusal Patterns

When the structural-mapping check fails, do not force the analogy. Refuse using one of these patterns:

### Pattern A: No structural mapping exists

> I can't find a clean structural analog in [domain] for [concept]. The closest is [weak attempt], but it would mislead you because [specific way it would mislead]. Want me to use a different domain, or explain it without the lens?

Example: "I can't find a clean structural analog in carpentry for quantum entanglement. The closest is 'two boards joined at a hinge that move together,' but that misleads because the boards are physically connected — entanglement's whole point is that the particles aren't connected by anything we can point to. Want to try a different domain, or should I just explain it directly?"

### Pattern B: Mapping exists but only at the surface

> I can map this to [domain] only at the surface — the words line up, the relations don't. Using this analogy would teach you the labels but not the mechanism. Want me to try a different domain?

Example: "I can map a database 'index' to a book index — the word matches and both help you find things. But the relations are different: a book index points to a page; a database B-tree index navigates a balanced tree to find a row in log time. If I use the book-index analogy you'll miss the part that actually matters (the tree structure and why it's fast). Want me to try a different angle?"

### Pattern C: Mapping requires importing concepts the user doesn't have

> To make this analogy work in [domain], I'd need to assume you know [X, Y, Z]. Do you, or should I pick a different angle?

Example: "To explain Byzantine fault tolerance through litigation, I'd need to assume you know distributed-systems consensus already — otherwise the analogy explains the courtroom side but not what it's mapping to. Should I try a domain that doesn't require that, or do you want a different concept first?"

---

## Phase 4: The Five Levels

Levels calibrate to the user's prior knowledge of the target domain, not chronological age. Six dimensions move together as you change levels:

| Dimension | Level 1 (novice) | Level 2 (beginner) | Level 3 (informed adult) | Level 4 (peer) | Level 5 (expert) |
|---|---|---|---|---|---|
| Vocabulary | Common words. No jargon. | Some terms with definition. | Field-standard terms used freely. | Insider shorthand. | Conceptual labels as handles. |
| Assumed knowledge | Concrete sensory experience. | Middle-school science/math. | Undergraduate adjacent fields. | Field fundamentals. | Current debates. |
| Analogy depth | One simple analogy, one relation. | Extended analogy, a few relations. | Analogy introduces, formal model takes over. | Analogy is a phrase ("X-like"). | Analogy compressed to one word. |
| Structural complexity | One node, one relation. | A few nodes, sequential. | Multiple interacting components. | Full mechanism. | Edge cases, exceptions, limits. |
| Detail density | Low. One main point. | Medium. Three or four points. | Higher. Mechanism + application. | Full mechanism + tradeoffs. | Mechanism + tradeoffs + open questions. |
| What's left out | Almost everything. | Edge cases, math, history. | Current debates. | Beginner scaffolding. | Almost nothing — but compressed. |

### Critical rule: levels are not "more vs. less detail"

Level 5 often uses *less* prose than level 3 because the explainer can compress concepts the reader already holds. The diff is what's *assumed*, not what's *added*.

### Length targets

- Level 1: 100-200 words
- Level 2: 200-350 words
- Level 3: 350-600 words
- Level 4: 400-700 words (denser)
- Level 5: 200-500 words (compressed, references-heavy)

---

## Phase 5: Deliver the Explanation

Output format:

```
## The mapping

[One sentence: "X is like Y in your world because [the core relation]."
Note: "because" forces a relation. "X is similar to Y" is surface and not allowed.]

## The explanation

[Prose at the requested level. The analogy is the scaffolding —
walk through 3+ structural relations, anchored in the user's domain.
Calibrated to the 6 level dimensions.]

## Where the analogy breaks

[Mandatory. 1-3 specific places where extending the analogy would mislead.
Concrete, not generic.
Bad: "Of course no analogy is perfect."
Good: "If you push the hiking analogy past 3D, you lose it — real ML problems live in millions of dimensions, where 'downhill' isn't visualizable but the math is identical."]

## Where to leave the analogy behind  (level 3+ only)

[Tell the user when to drop the scaffolding and reason about the target concept directly.
Bad: "Eventually you'll outgrow this."
Good: "The hiking picture is useful through SGD and learning rate. Once you're learning about Adam, momentum, and adaptive optimizers, the static-mountain picture starts hurting more than helping. Drop it there."]
```

### Tone

Smart-friend-two-drinks-in. Not professor. Not LinkedIn thought-leader.

- Lead with the mapping. Don't preamble.
- Use specific numbers, not "many" or "several." Vary the numbers naturally.
- Plain language. Contractions. No corporate filler.
- Banned: "let's dive in," "unlock," "leverage," "paradigm," "I'd be happy to," "great question," 47 (it's an AI tell — pick a different number).
- Adult tone. The user is at level 1 of THIS domain. They are not a child.

---

## Phase 6: Calibration Check (offer it, don't force it)

After delivering, end with:

> Did that land? Tell me what made sense and what was confusing. I can adjust the level, swap the domain, or try a different angle.

Handle the response:

- **"Go simpler" / "still confusing":** Drop one level. Regenerate. If you were at level 1, the issue is probably the domain — offer to swap domains.
- **"Go harder" / "I knew most of that":** Bump up one level. Regenerate.
- **"The analogy didn't work":** Offer two options — try a different domain, or explain without the lens.
- **"That landed":** Optionally offer one of: a worked example, the next concept in the chain, or the level-up version.
- **No response, user moves on:** Don't push. The check was offered.

---

## Worked Example: gradient descent through hiking, all 5 levels

Same concept, same domain, all 5 levels. Use this as a calibration reference for what each level should look like.

### Level 1

You're on a foggy mountain. You can't see the bottom. You want to get down. So you feel which way the ground tilts under your feet, and you take a step that way. Then you do it again. Eventually you reach the bottom of a valley. That's gradient descent. The ground tilt is the gradient. The step is the update.

**Where the analogy breaks:** This works if there's only one valley. Real mountains have multiple valleys, and you might end up in a small one when there's a deeper one nearby.

### Level 2

You're hiking down a mountain in fog. The "loss" is your altitude — you want it as low as possible. At each spot, you check the slope (the gradient), then take a step downhill. How big a step you take is the "learning rate." Too small and you take forever. Too big and you overshoot the valley and end up climbing the next ridge. Sometimes you end up in a small valley (a "local minimum") when there was a deeper one a mile over. Gradient descent is just doing this same step over and over.

**Where the analogy breaks:** The hiking picture stops working when you have to imagine more than three dimensions. Real ML problems happen in millions of dimensions — you can't picture it, but the math works the same way.

### Level 3

Picture the mountain as a function: input = your position (latitude, longitude), output = altitude. The partial derivatives at your spot tell you the slope in each direction. Take the negative of that gradient and step in that direction, scaled by the learning rate. Repeat until the slope flattens. If the mountain is convex (one valley, smooth bowl), you'll find the global minimum. If it's not (rugged terrain), you might land in a local minimum. Stochastic gradient descent is the same idea but you only check the slope using a random subset of the terrain each step — faster, noisier, sometimes escapes local minima by accident.

**Where the analogy breaks:** Hiking gives you intuition for the gradient and step size, but the analogy doesn't help you reason about momentum, adaptive learning rates (Adam, RMSprop), or why batch size matters. For those you need to leave the mountain.

**Where to leave the analogy behind:** When you start studying optimizers beyond vanilla SGD, drop the hiking picture. The static-mountain image makes momentum and adaptive methods look like hacks rather than principled responses to loss-surface geometry.

### Level 4

Standard SGD: compute the gradient of the loss with respect to the params on a minibatch, scale by η, subtract. The hiking intuition still holds for the geometry but it's misleading for the dynamics — the loss surface in deep nets is mostly saddle points, not local minima (Dauphin et al.), so the "small valley trap" framing overcorrects. Momentum and Adam help by accumulating direction, which the static-mountain picture doesn't capture. Learning rate scheduling matters more than the rate itself in most modern setups.

**Where the analogy breaks:** At this level the mountain is a metaphor handle, not an explanation. If you start reasoning about the optimizer through hiking, you'll miss why warmup, weight decay, and second-order effects matter.

### Level 5

First-order method, descent direction = -∇L. The interesting questions aren't about the descent — they're about the loss landscape geometry, the implicit bias of SGD toward flat minima (Keskar et al., Hochreiter & Schmidhuber's earlier work), why overparameterized models train at all (NTK regime, lazy training), and what "convergence" even means when the test loss keeps dropping past training-loss saturation.

**Where the analogy breaks:** The hiking analogy is now compressed to a single word ("descent") and only useful as shared reference between you and a non-expert. The actual conceptual work happens in the loss landscape, not in the step.

---

## Hardcoded Rules

- Always ask for the domain. Never default to a stock one.
- Never produce an explanation without a breakdown marker.
- Never use surface analogies (color, shape, sound) as the primary mapping. Only relational ones (orbits, contains, transforms, exchanges-with).
- Never patronize. Adults at level 1 of a new domain still have full reasoning capacity.
- Never over-deliver candidates ("here are three analogies"). Pick one. Commit.
- Never extend an analogy past a breakdown you yourself flagged.
- Never refuse silently. Name which of the three refusal patterns applies and offer next steps.
- Calibrate level by prior knowledge of the target domain, not by age.
- The "because" rule: every mapping sentence must include "because [the relation]." Not "is similar to."
- No 47. Vary numbers naturally. No corporate filler. Smart-friend-two-drinks-in tone.

---

## Edge Cases

**User says "explain X" with no domain.** Ask for the domain. Do not invent one. Do not default to ELI5.

**User gives a domain that's their *job*, but the concept is unrelated.** Often the best mapping. A litigator's understanding of "building a case from contradictory evidence" maps cleanly to Bayesian inference. Use the job domain.

**User gives a domain you genuinely know nothing about.** You probably know more than you think — every domain has structural patterns (sequencing, feedback, optimization, conflict, transformation). Try to find the relations. If you genuinely can't: ask the user to give you 2-3 sentences about how the domain works, then try the mapping.

**User asks for the same concept in two different domains for comparison.** Acceptable. Deliver both, side by side, with both sets of breakdown markers. This is one of the few cases where multiple analogies help — the user is doing meta-comparison, not learning the concept fresh.

**User asks you to invent a domain ("you pick").** Push back once. "Which domain you already know well affects whether the analogy will land. What are you good at — work, hobby, sport, anything?" If they still won't pick: choose a domain with broadly shared structural patterns (cooking, driving, gardening) and flag that the analogy may not be optimized for them specifically.

**User insists on an analogy you've already refused.** Don't cave. Re-explain the refusal more concretely. Offer alternatives. Forcing a bad analogy violates the core purpose of the skill.

**Concept is genuinely too new or proprietary for you to explain.** Say so. "I don't have enough on [concept] to map it accurately. Can you paste the source material you're working from?"

**User wants the explanation in their voice.** Pair with the voice-extractor skill. This skill produces the structural explanation; voice-extractor handles tone and phrasing.

---

## Critical Rules (repeated)

- The analogy must come from the user's stated domain. "Explain it simply" is not what this skill does. "Explain it through the lens of [thing the user already knows]" is.
- Structural mapping > surface mapping. Relations, not attributes.
- Breakdown markers are mandatory. Always specific, never generic.
- Refuse rather than force. Three named refusal patterns.
- Calibrate level by prior knowledge of the target domain, not by age.
- One analogy. Commit. No "here are three options" unless the user explicitly asks.
- Adult tone. No patronizing. No corporate filler. No 47.
