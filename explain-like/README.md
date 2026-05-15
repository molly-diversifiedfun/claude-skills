# Explain Like

**Stop dumbing things down. Start explaining them through what the user already knows.**

## The Problem

"Explain like I'm 5" tools produce two kinds of bad output: condescending kid-speak that adult learners reject, or generic simplification that leaves the user with labels but no mechanism. Both miss the point.

The fastest path to understanding a new concept is mapping it onto a domain the learner already holds tightly. A litigator who doesn't know Bayesian inference still understands building a case from contradictory evidence. A chef who doesn't know distributed systems still understands a high-volume Saturday night service. A gardener who doesn't know feedback control loops still understands what happens when you over-water a plant.

The cognitive science is settled. Dedre Gentner's structure-mapping theory (1983) is the de facto account of how analogies actually transfer understanding. The mapping has to be relational — not surface-level. And it has to mark its own breakdown points. The single biggest source of misconception in pedagogy literature is teachers who fail to say "the analogy stops working here" (Brown 1992; CBE-LSE 2023).

Existing tools fail on five dimensions: no domain input, no structural-mapping check, no refusal logic, no breakdown markers, no level calibration. This skill fills all five.

## What It Does

You give the skill two things:
1. A concept you want explained
2. A domain you already know deeply (cooking, sailing, litigation, gardening, basketball, accounting — anything)

The skill runs an internal structural-mapping check. If the relations in the target concept align with relations in your domain, it produces an explanation that uses your domain as scaffolding — calibrated to the level you asked for, with explicit markers showing where the analogy breaks down.

If the structural mapping fails — your domain doesn't actually map to the concept — the skill refuses to force a bad analogy. It tells you which of three failure modes applies and offers next steps.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Open the skill: say "Use the explain-like skill" (if added to a Project) or paste `SKILL.md` as your first message
3. Answer two questions: what concept, what domain
4. Optionally specify the level (1 novice through 5 expert)
5. Get the explanation with mandatory breakdown markers
6. Tell the skill if it landed or needs adjustment

### In Claude Code

1. Copy `SKILL.md` to `~/.claude/skills/explain-like/SKILL.md`
2. Or reference it in your project `CLAUDE.md`: "When explaining concepts through a known-domain lens, read path/to/explain-like/SKILL.md"
3. Tell Claude: "Explain [concept] to me through the lens of [domain]"
4. Iterate on level and domain as needed

### Tips for Better Results

- **Pick a domain you actually know.** Not a domain you've heard of. The mapping works because you can verify the relations against your own knowledge.
- **Narrow domains often work better than broad ones.** "17th-century Dutch shipbuilding" produces tighter mappings than "history."
- **Pick the level honestly.** If you'd already understand level 3 fine, asking for level 1 wastes your time. If you'd be lost at level 4, asking for it produces frustration.
- **Trust the refusal.** If the skill says "carpentry doesn't map to quantum entanglement," it's not being lazy — it's preventing you from walking away with a wrong mental model.
- **Use the breakdown markers.** They tell you exactly where to stop trusting the analogy. Memorize the boundary, not just the analogy.

## What You Get

### The Output Structure

```markdown
## The mapping

[One sentence: "X is like Y in your world because [core relation]."]

## The explanation

[Prose at the requested level — uses your domain as scaffolding, walks through
the structural relations one at a time. Calibrated to vocabulary, assumed
knowledge, analogy depth, structural complexity, detail density, and what to leave out.]

## Where the analogy breaks

[1-3 specific places where extending the analogy would mislead. Concrete, not generic.]

## Where to leave the analogy behind  (levels 3+)

[When to drop the scaffolding and reason about the concept directly.]
```

### The Five Levels

Levels calibrate to your prior knowledge of the *target* domain — not your age, not your general intelligence, not your knowledge of the *source* domain.

| Level | Audience | Vocabulary | Analogy use |
|-------|----------|------------|-------------|
| 1 | Just-introduced novice | Common words only | One simple analogy, one relation |
| 2 | Curious beginner | Some terms with definitions | Extended analogy, a few relations |
| 3 | Informed adult | Field-standard terms used freely | Analogy introduces, formal model takes over |
| 4 | Practitioner peer | Insider shorthand | Analogy compressed to a phrase |
| 5 | Expert | Conceptual labels as handles | Analogy compressed to one word |

A 40-year-old chef is level 1 for distributed systems but level 5 for kitchen workflows. The skill calibrates to *this concept*, not to *you generally*.

### The Three Refusal Patterns

When the structural-mapping check fails, the skill refuses rather than forcing a bad analogy. The three patterns:

1. **No structural mapping exists.** "Carpentry doesn't map to quantum entanglement. Want a different domain or want me to explain it directly?"
2. **Mapping exists only at the surface.** "Database index → book index — the words match but the relations don't. The book analogy would teach you the label and miss the mechanism."
3. **Mapping requires concepts you don't have.** "To make this analogy work, I'd need to assume you know X, Y, Z. Do you?"

Refusal is a feature. The misconception literature is unanimous: a forced bad analogy is worse than no analogy.

## The Research Behind It

Four findings shaped the design:

**Structure-mapping is the actual mechanism.** Gentner (1983) established that analogies transfer understanding when they map *relations* between objects (orbits, pulled-toward, exchanges-with) — not attributes (color, shape, size). "Atoms are like solar systems" works because the relational structure aligns, not because nuclei are yellow. The skill validates structural mapping before delivering, refuses when only the surface lines up.

**Analogies mislead in five specific ways.** Brown (1992) and the 2023 CBE-LSE pedagogy review converge on the failure modes: unattended breakdown, surface overgeneralization, mechanical use, stretched metaphor, and source-domain misconceptions transferred to the target. The #1 fix across all five: explicit breakdown markers. The skill makes them mandatory.

**The curse of knowledge is why experts explain badly.** Camerer, Loewenstein & Weber (1989) coined the term. Fisher & Keil (2016) showed experts have miscalibrated explanatory insight — they overestimate clarity because intermediate steps have become unconscious. Telling experts about the bias doesn't fix it. Financial incentives don't fix it. The only thing that helps: a constraint. The Feynman Technique uses "explain it to a child." This skill uses "explain it through this specific domain." Same mechanism, more useful output.

**WIRED's 5-Levels series is the closest empirical model for level calibration.** 50+ episodes of the same expert explaining one concept to a child, teen, college student, grad student, and expert. Pattern review across episodes reveals the diff isn't "more vs. less detail" — it's six dimensions moving together (vocabulary, assumed knowledge, analogy depth, structural complexity, detail density, what's left out). Level 5 often uses *less* prose than level 3 because the explainer compresses concepts the reader already holds.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Domain source | User-specified, asked explicitly | Inferring is high-variance. One extra question prevents a wrong-domain analogy that erodes trust. |
| Pre-baked pairings vs. fresh derivation | Fresh every time | Lookup tables ossify into pattern-matching, not structure-mapping. Two users who both "know cooking" have different available metaphors. |
| One analogy vs. multiple candidates | One. Alternates only if user asks. | Multiple candidates fragment attention and signal that none are great. |
| Force vs. refuse | Refuse, with three named patterns | Forcing a bad analogy is worse than no analogy. Misconception literature is unanimous. |
| Levels as buckets vs. slider | Five levels as a slider across six dimensions | Shared vocabulary + flexibility. Users can ask for "level 2.5." |
| Levels = age vs. levels = prior knowledge | Prior knowledge of the target domain | A chef is level 1 for distributed systems and level 5 for kitchens. Conflating accessibility with childlike explanation patronizes adults. |
| Breakdown markers | Mandatory at every output | Single biggest source of misconception in pedagogy research. |
| Validation step | Offered after delivery | One feedback loop catches wrong-level or wrong-domain cases before the user walks away with a bad model. |

## Pairs With

- **[voice-extractor](/voice-extractor/)** — Get the explanation, then run it through your voice profile so it sounds like you wrote it. Useful when you're going to repurpose the explanation in a blog post, newsletter, or talk.
- **[self-interview](/self-interview/)** — Use before this skill if you're not sure what you actually want to understand. Self-interview clarifies the question; explain-like answers it.
- **[mental-models](/mental-models/)** — When you want a framework to think with rather than an analogy to learn through. Different cognitive task, complementary tool.
- **[ask-me-the-questions](/ask-me-the-questions/)** — Use when even the two-question intake feels too directive. Ask-me handles the broader scoping; explain-like handles the focused mapping.

## What This Skill Does NOT Do

- Generic "explain like I'm 5" simplification (no domain grounding = not what this is)
- Mnemonics or memorization aids (different cognitive task)
- Full course material or lesson plans (this is single-concept explanation)
- Multi-domain mashups ("explain ML using cooking AND sailing AND chess")
- Force an analogy when no structural mapping exists — refuses instead
- Replace expertise — this is initial scaffolding, not the whole journey
