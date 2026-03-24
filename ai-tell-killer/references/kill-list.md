# AI Vocabulary Kill List v2

Sources: Wikipedia WikiProject AI Cleanup field guide (2025), Max Planck Institute ACL 2025 paper, Pangram Labs detection database (560+ terms), GPTZero detection model documentation, conorbronsdon/avoid-ai-writing 43-entry replacement table, blader/humanizer 25-pattern system, academic paper "Detecting Stylistic Fingerprints of Large Language Models" (March 2025), Sabrina Ramonov humanization framework.

## How the Tier System Works

**Tier 1 — Always flag.** These words appear 50%+ more frequently in AI text than human text. Replace on sight regardless of context. A single Tier 1 word won't get you caught, but detectors weight these heavily and they cluster.

**Tier 2 — Flag when clustered.** Normal English words that become AI tells when 3+ appear in the same section (~200 words). One "crucial" is fine. "Crucial" + "dynamic" + "innovative" in the same paragraph is a detection signal.

**Tier 3 — Flag at density.** Common words that only signal AI when they appear at unusually high frequency relative to the text length. Track these across the full document, not per-section.

---

## Tier 1: Always Replace

### Verbs
| AI Word | Replacement |
|---------|-------------|
| delve | dig into, look at, explore |
| leverage | use |
| utilize | use |
| harness | use, put to work |
| foster | build, grow, encourage |
| navigate (figurative) | deal with, figure out, work through |
| facilitate | help, run, make easier |
| optimize | improve, fix, tune |
| streamline | simplify, clean up |
| showcase | show, highlight |
| elevate | raise, improve |
| curate | pick, choose, put together |
| cultivate | build, grow |
| embark | start, begin |
| revolutionize | change, overhaul |
| transcend | go beyond, exceed |
| unleash | release, unlock |
| spearhead | lead, run |
| elucidate | explain, clarify |
| exemplify | show, demonstrate |
| reimagine | rethink, redesign |
| bolster | strengthen, support |
| underscore | show, prove, make clear |
| empower | enable, let, give the tools to |
| illuminate | show, reveal, explain |
| catalyze | trigger, start, cause |
| galvanize | push, motivate, drive |
| propel | push, drive, move |
| ignite | start, spark, trigger |
| encompass | include, cover |
| epitomize | represent, typify |
| encapsulate | capture, sum up |
| ascertain | find out, determine |
| commence | start, begin |

### Adjectives
| AI Word | Replacement |
|---------|-------------|
| robust | strong, solid, reliable |
| comprehensive | full, complete, thorough |
| multifaceted | complex, layered |
| nuanced | subtle, complicated |
| pivotal | key, important, big |
| seamless | smooth, easy |
| cutting-edge | new, latest, advanced |
| holistic | whole, complete, full-picture |
| bespoke | custom, tailored |
| ever-evolving | changing |
| groundbreaking | new, first-of-its-kind |
| transformative | big, significant |
| invaluable | very useful, essential |
| meticulous | careful, detailed, thorough |
| profound | deep, major |
| unparalleled | unique, best, top |
| unprecedented | new, first, never-before-seen |
| quintessential | classic, typical, defining |
| indispensable | essential, necessary |
| paramount | top priority, most important |

### Adverbs
| AI Word | Replacement |
|---------|-------------|
| moreover | also, and, plus |
| furthermore | also, and |
| additionally | also, plus |
| notably | especially |
| significantly | a lot, meaningfully, by [X]% |
| fundamentally | at its core, basically |
| meticulously | carefully |
| seamlessly | smoothly |
| inherently | by nature, naturally |
| arguably | possibly, some say |
| ostensibly | supposedly, on the surface |
| undeniably | clearly |
| remarkably | surprisingly, very |
| intriguingly | interestingly (but also avoid "interestingly") |
| conversely | on the other hand, but |
| nevertheless | still, even so, but |
| notwithstanding | despite, even with |

### Nouns
| AI Word | Replacement |
|---------|-------------|
| tapestry | mix, combination, blend |
| landscape (metaphorical) | space, world, market, field |
| realm | area, world, space |
| beacon | example, signal, guide |
| symphony | blend, mix, coordination |
| testament | proof, evidence, sign |
| paradigm | model, approach, way of thinking |
| synergy | overlap, combo, working together |
| ecosystem (non-tech) | community, network, market |
| interplay | relationship, interaction, tension |
| resilience | toughness, staying power |
| endeavor | effort, project, attempt |
| complexities | challenges, complications, details |
| intricacies | details, complications |
| resonance | impact, connection |
| versatility | flexibility, range |
| cornerstone | foundation, base, core |
| linchpin | key piece, critical part |
| bedrock | foundation, base |
| nexus | center, hub, connection point |
| confluence | meeting point, combination |
| trajectory | path, direction, trend |
| gamut | range, full set |
| ramifications | effects, consequences |
| manifestation | result, sign, example |

---

## Tier 2: Flag When 3+ Cluster in ~200 Words

### Verbs
resonate, amplify, pioneer, embrace, craft (pretentious use), unlock, unravel, underpin, commemorate, juxtapose

### Adjectives
vibrant, intricate, commendable, noteworthy, myriad, compelling, formidable, instrumental, substantive, discernible, burgeoning, overarching, salient, cogent, dynamic, crucial, vital, innovative

### Nouns
catalyst, hallmark, ethos, facet, spectrum (of opinions), implications, embodiment, juxtaposition, framework (overused)

---

## Tier 3: Flag at Document-Level Density

These are fine individually. Flag when they appear 5+ times per 1,000 words:

significant, effectively, potential, approach, framework, context, enhance, ensure, contribute, address, critical, essential, key (adjective), important, various, specific, overall, particular, relevant, impact (noun/verb), aspect, element

---

## Era-Specific Vocabulary Tracking

Detectors now correlate word clusters to specific model generations. If your text reads like a particular era of AI, it gets flagged even if individual words aren't on kill lists.

### 2023 to mid-2024 (GPT-4 era)
Cluster words: additionally, boasts, bolstered, crucial, **delve**, emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape, meticulous/meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant

### Mid-2024 to mid-2025 (GPT-4o era)
Cluster words: align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant

### Mid-2025+ (GPT-5 era)
Cluster words: emphasizing, enhance, highlighting, showcasing (plus heavy "notability" language — citing media sources to prove something matters)

### Claude-specific (all eras)
Cluster words/phrases: nuanced, straightforward, genuinely, thoughtful, I'd be happy to, it's worth noting, broadly speaking, that said, to be fair, I should note, from my understanding, it seems, I think it's important to

---

## Phrases to Delete Entirely

### Opening Clichés
- In today's fast-paced world
- In an ever-evolving landscape
- In the realm of [topic]
- As we navigate the complexities of
- In an era defined by
- At the intersection of X and Y
- The landscape of X is rapidly changing
- In today's rapidly evolving [anything]

### Hedging Filler
- It's important to note that
- It's worth mentioning that
- It should be noted that
- One cannot overstate the importance of
- There is no denying that
- It goes without saying that
- Needless to say
- That being said / With that said / Having said that
- Generally speaking / Broadly speaking

### Transition Crutches
- Let's dive in
- Without further ado
- With that in mind
- Taking a step back
- Looking at the bigger picture
- When it comes to
- In terms of (usually deletable)
- At the end of the day
- Moving forward

### Closing Clichés
- In conclusion
- To sum up / All in all
- I hope this helps
- I hope that clarifies things
- Please don't hesitate to reach out
- I look forward to hearing from you
- Feel free to reach out if you have any questions
- Let me know if you'd like me to expand on any section
- The future looks bright
- Exciting times lie ahead
- Only time will tell

### Performative Enthusiasm
- Great question!
- Absolutely!
- That's a fantastic point!
- What an exciting opportunity!
- This is truly remarkable
- How exciting!
- I'm thrilled to announce

### Fake Empathy / Validation
- I completely understand your concern
- That's a valid point
- I appreciate you sharing that
- Thank you for bringing this up
- I hear you

### Structural Clichés
- Not only X but also Y
- It's not just X — it's Y
- Pave the way for
- At the forefront of
- Bridge the gap between
- Unlock the potential of
- Foster a culture of
- Navigate the complexities of
- Shed light on
- A testament to
- Serves as a reminder that
- Plays a crucial role in
- A [adj] step towards [adj] [noun]

### Copula Avoidance Phrases (Replace with "is" or "has")
- serves as
- functions as
- acts as
- stands as
- features (when meaning "has")
- boasts
- presents (when meaning "has" or "includes")
- offers (when just meaning "has")

---

## Structural Patterns to Recognize and Break

**Synonym Cycling:** AI rotates through related words for the same concept. "Platform" → "solution" → "ecosystem" → "framework." Pick one. Repeat it.

**Present Participial Endings:** "...highlighting the importance of continued innovation" / "...underscoring the need for greater collaboration" / "...reflecting broader industry trends." These clause-endings appear 2-5x more in AI text. End sentences directly.

**The Compliment Sandwich:** Positive → acknowledge challenges → pivot back to positive. This is the default structure for any AI description. Break it.

**The Rule of Three:** Triple-item lists as rhetorical shorthand. "Smart, strategic, and scalable." Vary your list lengths.

**Uniform Paragraph Length:** AI paragraphs cluster at 3-5 sentences, all roughly the same size. Vary dramatically.

**Perfect Grammar Everywhere:** No typos, no fragments, no run-ons, no sentences starting with conjunctions. This perfection is itself a flag. Break a rule.

**Hourglass Structure:** Broad synthesis → narrow details → broad synthesis again. Human writing doesn't reliably follow this. Vary the shape.

**Even Information Distribution:** AI spreads information evenly across paragraphs. Humans front-load, back-load, or dump everything into one paragraph and move on.

**Vague Marketing Language in Descriptions:** Everything scenic, breathtaking, clean, modern, vibrant, nestled. As Wikipedia editors note: "it sounds like a TV commercial transcript." Be specific or be boring — boring beats promotional.
