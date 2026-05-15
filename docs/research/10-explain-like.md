# Research Brief: explain-like

## Q1 [HIGH PRIORITY]: What makes a cross-domain analogy work vs. mislead?

### Findings

**Structure-mapping is the actual mechanism.** Dedre Gentner's structure-mapping theory (1983) is the de facto cognitive science account of analogy. The core claim: an analogy is a mapping of *relations* between objects from a base (familiar) domain to a target (unfamiliar) domain. It is NOT a mapping of object attributes. "An atom is like a solar system" works because both have a small central object (relation: orbited-by) with smaller objects (relation: orbits) bound by an attractive force (relation: pulled-toward) — not because nuclei are yellow like the sun. The systematicity principle says people prefer mappings that include higher-order relations (causal, hierarchical) over isolated surface features.

**Surface similarity retrieves analogies; structural similarity makes them useful.** Gentner & Markman's research separates two stages: people retrieve analogies based on surface features ("this looks like that"), but those analogies only produce understanding when deep structural relations align. A "near analogy" maps surface AND structure (cars and trucks). A "far analogy" maps only structure (heart and pump). Far analogies are harder to retrieve but produce more transferable understanding — which is exactly the territory this skill operates in.

**Analogies mislead in five specific ways:**
1. **Unattended breakdown.** When the teacher fails to mark where the analogy stops working, students extend the mapping past its valid range. (Stem cells as actors awaiting casting calls — but who's the casting director?) Brown (1992) and the University of Akron's pedagogy guide both flag this as the #1 source of misconception.
2. **Surface overgeneralization.** Younger learners and novices anchor on surface similarity. If bacterial conjugation is "like sex," students assume bacteria have sexes and reproduce sexually. Both wrong. The analogy mapped one relation (genetic material exchange) but the surface label (sex) imported nine others.
3. **Mechanical use.** Learners parrot the analogy without understanding the underlying relation, then can't apply it to new cases.
4. **Stretched metaphor.** Pushing the analogy past its useful limit. The water-flow analogy for electricity works for current and resistance; it breaks for capacitance and AC.
5. **Source-domain misconceptions transferred.** If the user misunderstands the source ("I think water in pipes accelerates around corners"), the analogy will encode that wrong belief into the target.

**The curse of knowledge is why experts explain badly.** Camerer, Loewenstein & Weber (1989) coined the term. Fisher & Keil (2016) showed experts have *miscalibrated* explanatory insight — they overestimate how clearly they can explain their domain because the intermediate steps have become unconscious. Telling experts about the bias does NOT reduce it. Financial incentives do NOT reduce it. The only thing that helps: forcing the explanation through a constraint (a specific audience, a specific medium, a specific analogy domain). This is why the Feynman Technique works — the constraint is "explain it to a child" — and why this skill's design works: the constraint is "explain it through THIS specific domain."

**Famous explanations that work share a pattern.** Feynman's flame from the sun (energy storage, slow release). Heath & Heath's "Disney cast members" (Made to Stick — generative analogy, inspires action). Dawkins' selfish gene (relational mapping: genes as agents optimizing for survival). All three: (a) one tight base→target mapping, (b) explicit acknowledgment of where the mapping ends, (c) the analogy is *generative* — it produces new inferences, not just labels an old idea.

**Famous explanations that mislead share a different pattern.** "The brain is like a computer" (overgeneralized — implies discrete memory, serial processing, both wrong). "DNA is the blueprint of life" (implies static plan; misses regulation, expression, environment). "Atoms are tiny solar systems" (Bohr model — abandoned in 1925, still taught). All three: surface similarity dominates, structural mapping is partial, no breakdown markers given.

### Sources
- [Gentner, D. (1983). Structure-Mapping: A Theoretical Framework for Analogy. Cognitive Science.](https://groups.psych.northwestern.edu/gentner/papers/Gentner83.2b.pdf)
- [Gentner & Markman. Structure Mapping in Analogy and Similarity.](https://courses.csail.mit.edu/6.803/pdf/gentner.pdf)
- [Improving University Life Science Instruction with Analogies (CBE-LSE 2023).](https://www.lifescied.org/doi/10.1187/cbe.22-07-0142)
- [Brown (1992). Using examples and analogies to remediate misconceptions in physics. JRST.](https://onlinelibrary.wiley.com/doi/abs/10.1002/tea.3660290104)
- [Fisher & Keil (2015). The Curse of Expertise. Cognitive Science.](https://onlinelibrary.wiley.com/doi/abs/10.1111/cogs.12280)
- [MIT Sloan: The curse of knowledge — why experts struggle to explain.](https://mitsloan.mit.edu/ideas-made-to-matter/curse-knowledge-why-experts-struggle-to-explain-their-work)
- [Heath & Heath, Made to Stick (SUCCES summary).](https://www.adaptconsultingcompany.com/2024/06/28/made-to-stick-succes-model/)
- [Feynman Technique guide (FS.blog).](https://fs.blog/feynman-technique/)

### Confidence
HIGH on the cognitive science core (structure-mapping is settled). HIGH on the misconception failure modes (consistent across pedagogy literature). MEDIUM on the specific "five failure patterns" framing — synthesized from sources, not pulled from a single paper.

---

## Q2 [HIGH PRIORITY]: What changes at each explanation level?

### Findings

**Bloom's revised taxonomy gives the cognitive scaffold but not the explanation diff.** The six levels (remember, understand, apply, analyze, evaluate, create) describe what a learner can DO with knowledge. They don't describe how the *explainer* should change the explanation. Useful for setting goals; not useful for writing the actual prose at level 3 vs. level 5.

**The WIRED "5 Levels" series is the closest empirical model.** WIRED's format (a neuroscientist, a computer scientist, a biologist explains the same concept to a child, teen, college student, grad student, expert) is a working model with 50+ episodes. Pattern review across episodes reveals what actually changes:

| Dimension | Level 1 (child) | Level 2 (teen) | Level 3 (informed adult) | Level 4 (peer) | Level 5 (expert) |
|---|---|---|---|---|---|
| Vocabulary | Common words only. No jargon. | Some technical terms with definition. | Field-standard terms used freely. | Insider shorthand. | Conceptual labels used as handles. |
| Assumed knowledge | Concrete sensory experience only. | Middle-school science/math. | Undergraduate-level concepts in adjacent fields. | Field fundamentals. | Current open problems and debates. |
| Analogy depth | One simple analogy that maps one relation. | Extended analogy that maps a few relations. | Analogy used to introduce, then formal model takes over. | Analogy compressed to a phrase ("it's basically X-like"). | Analogy as compression: one word stands in for a known structure. |
| Structural complexity | One node, one relation. | A few nodes, sequential relations. | Multiple interacting components. | Full mechanism. | Edge cases, exceptions, current limits. |
| Detail density | Low. One main point. | Medium. Three or four anchored points. | Higher. Mechanism + application. | Full mechanism + tradeoffs. | Mechanism + tradeoffs + open questions. |
| What's left out | Almost everything except the core relation. | Edge cases, math, history. | Current research debates. | Beginner-level scaffolding. | Almost nothing — but compressed. |

**The textbook diff supports this.** Comparing intro-textbook vs. graduate-textbook treatments of the same concept (e.g., transcription in molecular biology, gradient descent in ML), the consistent diffs are: intro uses one anchoring metaphor and walks through one canonical case; graduate uses formal notation, references multiple variants, discusses where the model breaks down, and assumes the reader has the canonical case loaded in working memory.

**Critical: levels are not "more vs. less detail" — they're different abstraction layers.** A common implementation mistake is to treat level 5 as "level 1 plus more detail." It isn't. Level 5 often uses *less* prose than level 3 because the explainer can compress concepts the reader already holds. The diff is what's *assumed*, not what's *added*.

**The skill needs to NOT confuse "level" with "audience age."** A 40-year-old chef who knows nothing about distributed systems is at level 1 for distributed systems but level 5 for kitchen workflows. Calibration is by *prior knowledge of the target domain*, not by chronological age or general intelligence. This is where most "ELI5" tools get it wrong — they conflate accessible language with childlike explanation, then patronize adult learners who just lack one specific domain.

### Sources
- [Bloom's Revised Taxonomy (Colorado College).](https://www.coloradocollege.edu/other/assessment/how-to-assess-learning/learning-outcomes/blooms-revised-taxonomy.html)
- [WIRED 5 Levels playlist.](https://www.youtube.com/playlist?list=PLibNZv5Zd0dyCoQ6f4pdXUFnpAIlKgm3N)
- [Reluctance to Simplify (Westgard / High Reliability).](https://westgard.com/lessons/high-reliability/lesson88.html)
- [When Oversimplification Obscures (Nightingale).](https://nightingaledvs.com/when-oversimplification-obscures/)

### Confidence
HIGH on the dimension list (cross-validated WIRED + textbook patterns). MEDIUM on the exact 5-level cutoffs — these are pragmatic divisions, not natural kinds. The skill should treat levels as a slider, not a strict bucket system.

---

## Q3 [MEDIUM PRIORITY]: How should the skill handle the user's background domain?

### Findings

**Ask explicitly. Don't infer.** Inferring the user's background from their phrasing is a high-variance operation. The cost of asking one extra question is low; the cost of building an analogy on a wrong domain assumption is high (the user gets a confused or condescending explanation and quits). Two questions handle this: "What's the concept you want explained?" and "What domain do you already know well that I should explain it through?"

**A library of pre-baked pairings is a trap.** The temptation is to maintain a lookup table: ML → cooking, distributed systems → restaurant kitchens, OAuth → hotel keycards. These get used as defaults, the analogy ossifies, and the skill stops doing structure-mapping and starts pattern-matching. Better: derive the mapping fresh each time from the user's specific domain expertise. The user who runs a bakery and the user who runs a fine-dining restaurant both "know cooking" but their available structural metaphors differ.

**Refusal is a feature, not a failure.** Some target concepts genuinely don't map well to a given source domain. Quantum entanglement does not have a good analogy in carpentry. The honest move is to say so. Three refusal patterns:

1. **No structural mapping exists.** "I can't find a clean structural analog in [domain] for [concept]. The closest is [weak attempt], but it would mislead in [specific way]. Want me to use a different domain, or explain it without the lens?"
2. **Mapping exists but only at the surface.** "I can map this to [domain] only at the surface — the words line up, the relations don't. Using this analogy would teach you the labels but not the mechanism. Want me to try a different domain?"
3. **Mapping requires importing concepts the user doesn't have.** "To make this analogy work in [domain], I'd need to assume you know [X, Y, Z]. Do you, or should I pick a different angle?"

**The skill should also flag when a near-good analogy needs a breakdown marker.** Most analogies work for some relations and break for others. The skill's job isn't just to construct the mapping — it's to mark explicitly: "This analogy holds for [these relations]. It breaks for [these relations]. Don't extend it past [this point]."

### Sources
- [Using Analogies (University of Akron K-12 outreach).](https://www.uakron.edu/polymer/agpa-k12outreach/best-teaching-practices/using-analogies)
- [Northeastern CATLR: Using Analogies to Help Others Learn.](https://learning.northeastern.edu/using-analogies-to-help-others-learn/)

### Confidence
MEDIUM-HIGH. The "ask, don't infer" rule and the "refuse rather than force" rule are pragmatic conclusions from the misconception literature. The pre-baked pairings warning is opinionated based on observed failures in existing AI explainer tools.

---

## Q4 [MEDIUM PRIORITY]: What exists and what's missing?

### Findings

Surveyed four "explain like" implementations:

1. **HyperWrite "Explain Like I'm 5" tool.** Uses GPT-4 to simplify any topic. Approach: dumb it down using simple language and generic everyday examples. Gap: no user-domain input. Every output uses the same generic analogies (kids, toys, animals). This is what this skill is explicitly NOT.

2. **AI for Education "Explain It to Me Like…" prompt.** Single-shot prompt template: "Explain X like I'm Y." Approach: lets the user specify the audience role (a chef, a lawyer, a 10-year-old). Gap: it's a one-shot template — no quality check on whether the analogy actually maps, no breakdown markers, no refusal logic. Often produces forced or surface-level analogies.

3. **DraftWithAI "AI Analogy Generator."** Generates analogies for marketing/presentation use. Approach: produces multiple candidate analogies for the user to pick from. Gap: optimizes for memorability and surprise, not for accuracy of mapping. Good for pitch decks, dangerous for actual learning.

4. **OpenAI GPT-4 / Claude raw prompt.** "Explain X using my background as a Y." Approach: the user does it manually. Gap: no structured handling of refusal cases, no level calibration, no breakdown marking. Quality depends entirely on prompt skill.

**What's missing across all four:**
- **Domain-grounded analogy** (not generic simplification)
- **Structural mapping check** (does the analogy actually map relations, or just labels?)
- **Refusal logic** (when the domain doesn't fit, say so)
- **Explicit breakdown markers** (where the analogy stops working)
- **Level calibration** (separate from the analogy domain — these are two independent dials)

This is the gap this skill fills.

### Sources
- [HyperWrite Explain Like I'm 5.](https://www.hyperwriteai.com/aitools/explain-like-im-5)
- [AI for Education: Explain It to Me Like.](https://www.aiforeducation.io/prompts/explain-it-to-me-like)
- [DraftWithAI Analogy Generator.](https://www.draftwithai.com/analogy-generator)
- [How to Use ChatGPT's Analogy Feature (Inc.)](https://www.inc.com/carmine-gallo/how-to-use-chatgpts-analogy-feature-to-turbocharge-your-presentations.html)

### Confidence
HIGH. The gap is real and consistent across the surveyed tools.

---

## Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| **Domain source: user-specified vs. auto-inferred** | **User-specified, asked explicitly** | Inferring background from phrasing is high-variance. One extra question prevents a wrong-domain analogy that erodes trust. |
| **Pre-baked domain pairings vs. fresh derivation** | **Fresh derivation every time** | Lookup tables ossify into pattern-matching, not structure-mapping. Two users who both "know cooking" have different available metaphors. |
| **One analogy vs. multiple candidates** | **One primary analogy, with optional alternates only if user asks** | Multiple analogies fragment attention and signal that none are great. Pick the strongest mapping and commit. |
| **Force an analogy vs. refuse when no good mapping exists** | **Refuse explicitly, with three named refusal patterns** | Forcing a bad analogy is worse than no analogy. The misconception literature is unanimous on this. |
| **Levels as fixed buckets vs. slider** | **5 named levels treated as a slider with explicit dimensions** | Five WIRED-style levels give a shared vocabulary, but the actual diff is across 6 dimensions (vocabulary, assumed knowledge, analogy depth, structural complexity, detail density, what's-left-out). Users can request "level 2.5." |
| **Breakdown markers: optional vs. mandatory** | **Mandatory at every output** | The single biggest source of misconception in pedagogy research. Every analogy must say where it stops working. |
| **Validation step: skip vs. offer** | **Offer a calibration check after delivery** | "Did this land? What was confusing?" One feedback loop catches the wrong-level or wrong-domain case before the user walks away with a bad model. |

---

## Explanation Level Spec

Same concept, all 5 levels. Concept: **gradient descent** (the optimization algorithm in machine learning). User's stated domain: **hiking in mountains**.

### Level 1 — Just-introduced novice
**Vocabulary:** common words only.
**Output:** "You're on a foggy mountain. You can't see the bottom. You want to get down. So you feel which way the ground tilts under your feet, and you take a step that way. Then you do it again. Eventually you reach the bottom of a valley. That's gradient descent. The ground tilt is the gradient. The step is the update."

**Breakdown marker:** "This works if there's only one valley. Real mountains have multiple valleys, and you might end up in a small one when there's a deeper one nearby."

### Level 2 — Curious beginner
**Vocabulary:** introduces "loss," "learning rate," "local minimum" with quick definitions.
**Output:** "Imagine you're hiking down a mountain in fog. The 'loss' is your altitude — you want it as low as possible. At each spot, you check the slope (the gradient), then take a step downhill. How big a step you take is the 'learning rate.' Too small and you take forever. Too big and you overshoot the valley and end up climbing the next ridge. Sometimes you end up in a small valley (a 'local minimum') when there was a deeper one a mile over. Gradient descent is just doing this same step over and over."

**Breakdown marker:** "The hiking analogy stops working when you have to imagine more than three dimensions. Real ML problems happen in millions of dimensions — you can't picture it, but the math works the same way."

### Level 3 — Informed adult (knows some math, no ML)
**Vocabulary:** uses "loss function," "partial derivative," "convex," "stochastic" — defines on first use.
**Output:** "Picture the mountain as a function: input = your position (latitude, longitude), output = altitude. The partial derivatives at your spot tell you the slope in each direction. Take the negative of that gradient and step in that direction, scaled by the learning rate. Repeat until the slope flattens. If the mountain is convex (one valley, smooth bowl), you'll find the global minimum. If it's not (rugged terrain), you might land in a local minimum. Stochastic gradient descent is the same idea but you only check the slope using a random subset of the terrain each step — faster, noisier, sometimes escapes local minima by accident."

**Breakdown marker:** "Hiking gives you intuition for the gradient and step size, but the analogy doesn't help you reason about momentum, adaptive learning rates (Adam, RMSprop), or why batch size matters. For those you need to leave the mountain."

### Level 4 — Practitioner peer
**Vocabulary:** uses field shorthand. Hiking analogy is now a single phrase ("the descent").
**Output:** "Standard SGD: compute the gradient of the loss with respect to the params on a minibatch, scale by η, subtract. The hiking intuition still holds for the geometry but it's misleading for the dynamics — the loss surface in deep nets is mostly saddle points, not local minima (Dauphin et al.), so the 'small valley trap' framing overcorrects. Momentum and Adam help by accumulating direction, which the static-mountain picture doesn't capture. Learning rate scheduling matters more than the rate itself in most modern setups."

**Breakdown marker:** "At this level the mountain is a metaphor handle, not an explanation. If you start reasoning about the optimizer through hiking, you'll miss why warmup, weight decay, and second-order effects matter."

### Level 5 — Expert
**Vocabulary:** conceptual labels as handles. Analogy is a one-word reference.
**Output:** "First-order method, descent direction = -∇L. The interesting questions aren't about the descent — they're about the loss landscape geometry, the implicit bias of SGD toward flat minima (Keskar et al., Hochreiter & Schmidhuber's earlier work), why overparameterized models train at all (NTK regime, lazy training), and what 'convergence' even means when the test loss keeps dropping past training-loss saturation."

**Breakdown marker:** "The hiking analogy is now compressed to a single word ('descent') and only useful as a shared reference between you and a non-expert. The actual conceptual work happens in the loss landscape, not in the step."

---

*Total length: ~2,200 words. Anchored on Q1 (structure-mapping) and Q2 (level calibration) per the priority stack.*
