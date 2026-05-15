# PRD: explain-like

## Problem

"Explain it like I'm 5" tools dumb things down with generic kid-friendly language and produce condescending output that doesn't actually transfer understanding. The gap isn't simplicity — it's *grounding*. Adults who don't know a topic still know plenty of other domains deeply. A chef who doesn't understand distributed systems still understands a high-volume Saturday night service. A litigator who doesn't understand gradient descent still understands building a case from contradictory evidence. The fastest path to understanding is mapping the new concept onto a domain the learner already holds.

The cognitive science is settled here: structure-mapping (Gentner, 1983) is the actual mechanism by which analogy produces understanding. The mapping has to be *relational*, not surface-level. And it has to mark its own breakdown points — the #1 source of misconception in pedagogy literature is teachers who fail to say "the analogy stops working here" (Brown 1992; CBE-LSE 2023).

Existing tools fail on five dimensions: no domain input, no structural-mapping check, no refusal logic, no breakdown markers, no level calibration. This skill fills all five.

## Solution

A skill that asks two questions — what concept, what domain you already know — then produces a structurally-mapped analogy at a calibrated explanation level, with explicit markers for where the analogy breaks down. Refuses when the user's domain doesn't structurally map to the target concept rather than forcing a misleading analogy.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Domain source | **User-specified, asked explicitly** | Inferring background from phrasing is high-variance. One extra question prevents a wrong-domain analogy that erodes trust. The cost of a bad analogy (user walks away with a wrong mental model) far exceeds the cost of asking. |
| Pre-baked domain pairings vs. fresh derivation | **Fresh derivation every time** | Lookup tables ossify into pattern-matching, not structure-mapping. Two users who both "know cooking" have different available metaphors. Bakery owner and fine-dining chef map distributed systems differently. |
| One analogy vs. multiple candidates | **One primary analogy. Alternates only if user asks.** | Multiple analogies fragment attention and signal that none are great. Pick the strongest mapping and commit. |
| Force vs. refuse | **Refuse explicitly, with three named refusal patterns** | Forcing a bad analogy is worse than no analogy. Misconception literature is unanimous. Three patterns: no structural mapping exists, mapping is surface-only, mapping requires importing concepts the user doesn't have. |
| Levels as buckets vs. slider | **5 named levels, treated as a slider across 6 dimensions** | WIRED's 5-level format gives shared vocabulary. The actual diff lives across vocabulary, assumed knowledge, analogy depth, structural complexity, detail density, and what's-left-out. Users can request "level 2.5." |
| Levels = age vs. levels = prior knowledge | **Prior knowledge of the target domain** | A 40-year-old chef is level 1 for distributed systems but level 5 for kitchen workflows. Conflating accessibility with childlike explanation patronizes adult learners who just lack one specific domain. |
| Breakdown markers | **Mandatory at every output** | Single biggest source of misconception in pedagogy research. Every analogy must say where it stops working. |
| Validation step | **Offer a calibration check after delivery** | "Did this land? What was confusing?" One feedback loop catches wrong-level or wrong-domain cases before the user walks away with a bad model. |
| Surface vs. structural mapping | **Validate structurally before delivering** | An analogy must map *relations* (orbits, pulled-toward, exchanged-with) — not attributes (yellow, round, hot). If only attributes map, refuse. |

## Target User

Adults learning a new domain who already know other domains deeply. Specifically:

- A senior person in field A trying to understand field B for a strategic decision (PM understanding ML, lawyer understanding crypto, doctor understanding statistics)
- A self-learner who hit a conceptual wall in a textbook or course and wants a different angle
- A teacher or writer who needs to explain a concept to a specific audience and wants to test the analogy before using it
- A practitioner debugging their own understanding by reframing a known concept through a fresh lens

NOT the user: children, people who want generic ELI5, people looking for memorizable mnemonics rather than understanding.

## Interaction Model

**Phase 1: Two questions**

Ask both at once:

1. "What concept do you want explained?"
2. "What's a domain you already know well — well enough that I can use it as a lens? (Examples: cooking, sailing, litigation, gardening, accounting, basketball.)"

Optional third: "What level do you want — 1 (just-introduced novice) through 5 (expert)? If you're not sure, I'll guess and you can tell me to go up or down."

**Phase 2: Structural-mapping check (silent, before delivering)**

Before writing the explanation, run an internal check:

1. List the 3-5 core *relations* (not attributes) in the target concept.
2. Find the corresponding relations in the user's domain.
3. Score the mapping: do the relations align, or only the surface labels?
4. If 3+ relations map cleanly: proceed.
5. If only 1-2 relations map: deliver the explanation but lean heavily on breakdown markers.
6. If 0 relations map: refuse via one of the three refusal patterns. Don't force it.

**Phase 3: Deliver the explanation**

Output structure:

```
## The mapping

[One sentence: "X is like Y in your world because..."]

## The explanation

[Prose explanation at the requested level. Uses the analogy as scaffolding.
Calibrated to the 6 level dimensions: vocabulary, assumed knowledge, analogy depth,
structural complexity, detail density, what's left out.]

## Where the analogy breaks

[Mandatory. List 1-3 specific places where extending the analogy would mislead.
Be concrete: "If you push this past X, you'll start assuming Y, which is wrong because Z."]

## Where to leave the analogy behind

[For levels 3+: tell the user when to drop the analogy and reason about the target concept directly.]
```

**Phase 4: Calibration check (offer it)**

After delivering, ask:

> Did that land? Tell me what made sense and what was confusing. I can adjust the level, swap the domain, or try a different angle.

If user says "go simpler" or "go harder": adjust level, regenerate.
If user says "the analogy didn't work": offer to try a different domain, or drop the analogy entirely.
If user says it landed: optionally offer one of: a worked example, the next concept in the chain, or the level-up version.

## Output Spec

Every explanation includes:

- **One mapping sentence.** "X is like Y because [the core relation]." Not "X is similar to Y" — that's surface. The "because" forces a relation.
- **Explanation prose.** Calibrated to one of 5 levels. Uses the analogy as scaffolding, not as decoration.
- **At least one breakdown marker.** Specific. Not "of course, no analogy is perfect." Concrete: "If you imagine the gradient as ground tilt, you'll miss why momentum matters — momentum has no analog in the hiking picture."
- **Optional: leave-the-analogy moment.** For level 3+, tell the user when to drop the scaffolding.

Length guidance:
- Level 1: 100-200 words
- Level 2: 200-350 words
- Level 3: 350-600 words
- Level 4: 400-700 words (denser, more compressed)
- Level 5: 200-500 words (compressed, references-heavy)

## Success Criteria

- The user finishes the explanation able to predict one new behavior of the target concept (the test of structure-mapping working: it produces *generative* understanding, not just labels).
- The user can name where the analogy breaks down without being told (because it was marked).
- The user does not extend the analogy past its valid range in follow-up questions.
- When the skill refuses to force a bad analogy, the user trusts the refusal and asks for a different angle.
- A user who comes in at the wrong level recognizes it within 1-2 follow-up turns and gets a recalibrated explanation.

## What This Skill Does NOT Do

- Generic "explain like I'm 5" simplification (no domain grounding = not what this is)
- Mnemonics or memorization aids (different cognitive task)
- Full course material or lesson plans (this is single-concept explanation)
- Explanations without breakdown markers ("of course no analogy is perfect" doesn't count)
- Multi-domain mashups ("explain ML using cooking AND sailing AND chess")
- Force an analogy when no structural mapping exists — refuse instead
- Replace expertise — the user still needs to do real learning beyond this initial scaffolding

## Anti-Patterns to Avoid in Implementation

- Never default to a stock domain ("let's use cooking"). Always derive from the user's stated domain.
- Never produce an explanation without a breakdown marker.
- Never use surface analogies (color, shape, sound) as the primary mapping — only relational ones (orbits, contains, transforms, pulled-toward).
- Never patronize. Adult learners at level 1 of a domain are not children. They have full reasoning capacity, they just lack vocabulary in this specific area.
- Never over-deliver candidates ("here are 3 analogies"). Pick one, commit.
- Never extend an analogy that the skill itself flagged as breaking. If you marked the breakdown at gradient → momentum, don't then use the gradient analogy to explain momentum.
- Never refuse silently. If the domain doesn't map, name which of the three refusal patterns applies and offer next steps.
- Never confuse level with audience age. Calibrate by prior knowledge of the target domain.
- Never use 47 in examples. Vary numbers naturally.
- No corporate filler. No "let's dive in." No "I'd be happy to."

## Technical Notes

- Pure prompt-based — no tools, no API calls, no external lookups
- Works in Claude.ai (paste SKILL.md, or load via Project) and Claude Code (place in `~/.claude/skills/explain-like/`)
- Single-conversation skill — no persistent state, no profile artifact
- Pairs with: voice-extractor (write the explanation in your voice), self-interview (clarify your own thinking before explaining), mental-models (when you want frameworks instead of analogies)
