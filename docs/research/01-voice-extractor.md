# Voice Extractor — Research Results

The strongest signal from this research is a paradox: **the features most powerful for identifying an author's style are precisely those an LLM cannot deliberately reproduce.** Function word frequencies and character n-grams dominate authorship attribution, but they're emergent statistical properties — you can't instruct Claude to use "the" at 6.8% instead of 7.2%. The extractable-and-reproducible sweet spot lies in a narrower band: sentence length distribution, punctuation habits, pronoun patterns, active/passive voice ratio, and vocabulary register. Everything else requires workarounds. What follows is the dimension-by-dimension breakdown, the implementation landscape, and the design decisions that flow from both.

---

## Q1: Eleven dimensions, but only five are reliably extractable AND reproducible

Computational stylistics has a rich taxonomy. Writeprints (Abbasi & Chen, 2008) catalogues **239 features** across lexical, syntactic, structural, and content-specific categories. Lagutina et al. (2019) systematizes features at character, word, syntax, semantic, and structural levels. Burrows' Delta operates on the most frequent ~100-300 words. But for a 3-5 sample extraction system feeding an LLM, most of these features are either unextractable from small corpora or unreproducible in generation.

Here's the dimension-by-dimension verdict, rated on two axes — extractability from 3-5 samples and LLM reproducibility:

**Tier 1 — High extractability, high reproducibility (build your profile around these):**

**Sentence length distribution** is the strongest foundation. Mean length, standard deviation, min/max, and the ratio of short sentences (<10 words) to long ones (>30 words) are trivially computable from even three samples and directly instructable. Claude follows "average 12 words per sentence, varying between 5 and 25" reliably. **Pronoun usage patterns** are nearly as strong — Pennebaker's work demonstrates pronouns are among the least consciously controlled linguistic choices, making them authentic markers. I/we/you ratios and direct-address frequency stabilize quickly in small samples and are straightforward to instruct. **Punctuation habits** round out the top tier. Sapkota et al. (2015) found punctuation patterns "account for almost all of the power of character n-grams." Em-dash frequency, semicolon usage, parenthetical density, and exclamation mark rate are trivially countable and approximately controllable. **Active/passive voice ratio** is a standard NLP detection task and one of the most reliable instructions an LLM can follow.

**Tier 2 — Medium on both axes (include but expect approximation):**

**Vocabulary register** (type-token ratio, average word length as a Latinate/Germanic proxy, rare word frequency) requires length-normalization and doesn't produce precise numerical matches, but Claude can approximate "prefer Anglo-Saxon monosyllables" versus "favor Latinate polysyllables." **Paragraph structure** (length, sentence count, topic-sentence placement) yields reasonable statistics from 15-40 paragraphs across samples but is genre-dependent. **Transition mechanics** — discourse connective density, conjunction frequency — are extractable but matching specific transition-word frequency is imprecise. **Jargon density** carries a critical caveat from Stamatatos (2009): content words risk "overfitting to topic rather than capturing style."

**Tier 3 — Low extractability or low reproducibility (handle with care):**

**Rhetorical device frequency** has no dedicated stylometric feature set. Anaphora and rhetorical questions are detectable with heuristics, but 3-5 samples rarely contain enough instances to establish frequency patterns. Ironically, LLMs reproduce these well when instructed — the bottleneck is extraction, not generation. **Opening/closing patterns** suffer from a sample-size ceiling: you get exactly 3-5 openings to analyze, too few for reliable pattern detection, though they're highly instructable ("begin with an anecdote, end with a callback"). **Rhythm and cadence** are measurable through sentence-length variation sequences and syllable patterns (Plecháč et al., 2018 achieved 84-99% precision combining stress patterns with Burrows' Delta), but LLMs have no mechanism for controlling syllable-level prosody. **Humor and irony mechanics** are the weakest dimension — no major stylometry survey includes them as measurable, extraction requires semantic understanding that resists quantification, and LLMs default to earnest delivery even when instructed otherwise.

A critical finding from Wang et al. (2025), "Catch Me If You Can?": across **40,000+ generations and 400+ authors**, LLMs struggled with nuanced informal writing but approximated style better in structured formats like news and email. Jemama (2025) found that statistical style summaries were "incapable of style mimicry" while actual writing examples yielded dramatically better results. This directly supports the project's premise — sample-based extraction over adjective descriptions — but suggests the profile should include raw excerpts alongside extracted metrics.

**Sources:** Lagutina et al. (2019) survey, Writeprints (Abbasi & Chen, 2008), Pennebaker (2011) *The Secret Life of Pronouns*, Sapkota et al. (2015), Wang et al. (2025), Jemama (2025), Plecháč et al. (2018). Read yourself: Wang et al. (2025) and Jemama (2025) — they directly address LLM style reproduction and aren't fully captured above.

**Confidence: Medium-High.** The extractability ratings are well-supported by decades of stylometry research. The LLM reproducibility ratings are my synthesis from fewer, more recent sources. A systematic benchmark of Claude specifically reproducing each dimension would raise this to High.

---

## Q2: Eight implementations, one universal failure pattern

The implementations cluster into three approaches: sample analysis (extract metrics from writing), interview-based (ask about preferences), and hybrid. Every single one shares the same core failure: **static profiles that don't learn from corrections.**

**Daria Cupareanu's Voice DNA** is the most sophisticated Claude-specific approach. Her key insight is analyzing **absences** — words you avoid, structures you skip, places where AI would "correct" your intentional choices — then building override rules. She produces a ~4,500-word profile but splits it across **three separate skills** (overall voice, audience-specific, intro-specific) because "one giant voice skill trying to handle everything produces generic output." Even so, she describes the result as a polished first draft requiring human revision, not a finished product.

**The "Taste Interviewer" method** takes the opposite approach: instead of analyzing samples, Claude conducts a 40-100 question interview covering "Aesthetic Crimes" (what makes you cringe), structural preferences, and hard nos. The insight that "most of a good voice profile is about what you reject" aligns with Cupareanu's absences. Users report it works but needs iterative refinement — "your first voice file won't be perfect."

**haowjy/creative-writing-skills** (GitHub, 31 stars) contributes a crucial formatting insight: style must be expressed as **directives for AI**, not analysis about the author. "Use short sentences during action" works; "The author tends to use short sentences" doesn't. The distinction between instruction and description appears across every successful implementation.

Among commercial tools, **Jasper Brand Voice** has the most documented failures. Trustpilot reviews describe voice that "does NOT carry through, it reverts back to AI speak." One review crystallizes the caricature problem: "Every time I used my 'brand voice,' it started sentences with 'Hey there!' — Jasper latched onto 'casual and conversational' and produced a caricature." **Writer.com** uses dedicated voice extraction and generation models but still suffers voice drift in long-form content and has no learning from user corrections.

**The LobeHub Voice-Matched Content skill** offers the most detailed open-source template, capturing "Transition Signatures" (8-12 actual phrases the author uses), "Authority Zones" versus "Learning Zones," and explicit self-edit checklists. It's the closest to a comprehensive extraction framework.

Ten universal failure modes emerged across all implementations. The most consequential: **voice drift in long-form content** (instructions lose influence as generation proceeds), **structural homogenization** (vocabulary and tone transfer but paragraph rhythm and information ordering stay generic), **the caricature problem** (tools amplify the most obvious features rather than capturing nuance), and **humor breaking first** (sarcasm, irony, and wit are essentially impossible to profile). One OpenAI Community user solved Custom GPT voice failure only by switching to a **fine-tuned GPT-3.5 model** — suggesting prompt-based approaches hit a ceiling that fine-tuning can breach.

**Sources:** Cupareanu's Substack (aiblewmymind.substack.com, paywalled), haowjy GitHub repo, LobeHub skill page, Jasper Trustpilot reviews, Writer.com analysis at atomwriter.com, OpenAI Community forums. Read yourself: Cupareanu's articles (even the free previews reveal her methodology) and the LobeHub skill source code (most complete open-source template).

**Confidence: Medium.** Implementation documentation is self-reported, not independently verified. Failure modes are well-documented through user complaints, but success claims lack controlled evaluation. Would increase to High with systematic A/B testing of each approach.

---

## Q3: 3-5 samples works, barely — but total word count matters more

Eder's landmark 2015 study ("Does Size Matter?") established **5,000 running words** as the minimum for reliable authorship attribution across languages and methods. His 2017 follow-up reduced this to **2,000 words** in favorable conditions. Ramnial et al. (2016) achieved >90% accuracy at just 1,000-word segments. The practical implication: 3-5 samples of 500-1,000 words each (1,500-5,000 total words) is marginal for statistical stylometry but viable for LLM-based extraction, which is more forgiving. **The optimal target is 5-10 samples totaling 10,000+ words.**

Same-format samples produce cleaner signal for a specific use case; varied formats capture more dimensions of voice. The best approach is **primarily same-format (3-5 blog posts) plus 1-2 varied samples** to capture range. Informal samples (emails, Slack) carry authentic signal — LobeHub's guidance that "the ones you wrote fast without overthinking are often the most useful" aligns with Pennebaker's research on unconscious style markers — but should be separated into context-specific profiles rather than mixed with formal writing. Temporal drift is real: the PMC forensic stylometry review recommends reference material "as contemporary as possible," so samples should come from the **most recent 1-2 years**.

**Confidence: Medium-High.** The word-count thresholds are from rigorous academic studies but apply to statistical attribution, not LLM extraction. The format and recency guidance is practitioner consensus with limited controlled evidence.

---

## Q4: Working profiles share seven sections; failing ones rely on adjectives

Across all publicly shared voice profiles, the pattern is stark. Working profiles contain: specific structural patterns (sentence length targets, paragraph style), **vocabulary rules with concrete examples** (banned words, always-used words, favorite transitions), anti-patterns ("never write like THIS"), and at least one sample paragraph as a calibration reference. Failing profiles rely on vague adjectives ("friendly, professional, conversational") without concrete anchors.

The operational sweet spot is **1,000-2,000 words**. Liu et al.'s "Lost in the Middle" research shows models retrieve best from the beginning and end of long inputs — in a 4,000-word profile, the middle 2,000 words get reduced attention. The minimum viable structure:

- Identity and audience (2-3 sentences)
- Structural patterns (sentence length, paragraph style, formatting preferences)
- Vocabulary rules (words to use, words to ban, transition phrases — with examples)
- Anti-patterns (AI-isms to never produce, stylistic moves to avoid)
- Tone as measurable dimensions, not adjectives
- 1-2 sample paragraphs showing the voice in action

A longer analysis document (3,000-5,000 words) is valuable as a source artifact but should be **distilled into a 1,000-2,000 word operational version** with critical rules front-loaded and repeated at the end.

**Confidence: Medium.** Profile structure guidance comes from practitioner experience, not controlled experiments. The "lost in the middle" finding is rigorous but applied here by inference, not direct testing with voice profiles.

---

## Key design decisions

**Decision 1: Fixed dimensions vs. emergent dimensions**
Option A: Pre-define ~12 voice dimensions (sentence length, punctuation, pronouns, etc.) and score each from samples. Option B: Let the extraction prompt discover whatever patterns exist in each user's writing.
*Tradeoff:* A produces consistent, comparable profiles and focuses extraction on dimensions known to be reproducible. B captures what makes each voice unique — including dimensions you didn't anticipate — but produces inconsistent profiles and may extract features Claude can't reproduce. **Recommendation from the research:** Hybrid. Use fixed Tier 1 dimensions as the skeleton, then add an open-ended "distinctive patterns" section for emergent features.

**Decision 2: Metrics-based profile vs. example-based profile**
Option A: Express the profile as extracted metrics ("avg sentence length: 14 words, em-dash frequency: high, pronouns: heavy first-person"). Option B: Include 2-3 raw writing excerpts as few-shot examples alongside lighter framing instructions.
*Tradeoff:* Jemama (2025) found statistical summaries "incapable of style mimicry" while examples worked dramatically better. But pure examples consume context window and provide no explicit rules for edge cases. **The evidence strongly favors a hybrid** — metrics as guardrails, examples as calibration anchors. Atomwriter reports **25-35% better adherence** with transformation pairs (before/after examples) versus rules alone.

**Decision 3: Directive format vs. analytical format**
Option A: "Use short, punchy sentences in openings. Never exceed 20 words in your first sentence." Option B: "The author tends to use short sentences in openings, averaging 12 words."
*Tradeoff:* There is no real tradeoff. Every successful implementation uses directives. haowjy's creative-writing-skills makes this explicit: analysis ("the author tends to...") is treated as an error in their system. **Use directives.**

**Decision 4: Single monolithic profile vs. chunked context-specific profiles**
Option A: One comprehensive .md file covering all writing contexts. Option B: Separate profiles for different contexts (blog posts, emails, LinkedIn, technical writing).
*Tradeoff:* Cupareanu found that a single skill "kept mixing up audiences" and split into three. But multiple profiles increase complexity and require users to select the right one. For a general-purpose skill, **start with one profile but architect it to support chunking** — the extraction prompt should tag patterns by context when samples span formats.

**Decision 5: What-you-do vs. what-you-never-do weighting**
Option A: Focus the profile on positive patterns ("uses em-dashes frequently, opens with questions"). Option B: Weight the profile toward prohibitions and absences ("never uses 'delve' or 'leverage,' avoids semicolons entirely, never opens with 'In today's...'").
*Tradeoff:* Both Cupareanu and the Taste Interviewer method converge on absences being more powerful. AI has strong defaults; telling it what NOT to do overrides those defaults more reliably than telling it what to do. **Weight toward anti-patterns** — perhaps 40% positive patterns, 60% prohibitions and absences.

**Decision 6: Profile length — compact operator vs. comprehensive reference**
Option A: A dense ~500-word "voice block" optimized for pasting into any conversation. Option B: A detailed ~3,000-word profile designed for Claude Projects or Skills (persistent context).
*Tradeoff:* The "lost in the middle" effect means longer profiles lose influence in their middle sections. But shorter profiles can't capture enough specificity. **Generate both** — a comprehensive extraction artifact (3,000+ words) that the skill automatically distills into a 1,000-1,500 word operational profile with critical rules at the beginning and end.

**Decision 7: Pure sample extraction vs. hybrid extraction + interview**
Option A: Analyze only the writing samples, extracting all patterns computationally. Option B: Combine sample analysis with 5-10 targeted questions ("What writing do you cringe at? What's your relationship to humor in writing?").
*Tradeoff:* Samples capture unconscious patterns (the most authentic markers per Pennebaker), but miss intentional choices and preferences. Interviews capture self-awareness about voice but suffer from the self-description gap — people describe the writer they wish they were, not the writer they are. **Use samples as the primary source, then ask 3-5 targeted questions only about dimensions that are hard to extract** (humor intent, audience awareness, topics to avoid). Weight sample evidence over self-report when they conflict.
