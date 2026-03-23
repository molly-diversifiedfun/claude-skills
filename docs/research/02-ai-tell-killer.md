# AI Tell Killer — Research Results

**The strongest AI writing signals aren't individual words — they're statistical fingerprints.** While "delve" became the poster child of AI vocabulary, peer-reviewed research shows that sentence-length uniformity, structural repetition, and co-occurring vocabulary clusters are far more reliable markers than any single lexical item. A tell killer built on word bans will overcorrect; one built on pattern recognition and statistical awareness will surgically remove the machine signature while leaving the writer's voice intact.

This document provides the taxonomy of tells, the thresholds where normal writing becomes suspicious, the false-positive danger zones, and the lessons from existing tools — most of which make text worse **74% of the time**.

---

## Q1: A categorized taxonomy of documented AI tells

### Vocabulary: the most studied category, and the most misunderstood

Two landmark studies anchor this category. **Kobak et al. (2025)** in *Science Advances* analyzed 15.1 million PubMed abstracts and found **454 words with excess frequency** post-ChatGPT, using an "excess mortality" statistical framework. The word "delves" appeared at **28× its predicted frequency**; "underscores" at 13.8×; "showcasing" at 10.7×. Separately, **Liang et al. (2025)** in *Nature Human Behaviour* analyzed 1.1 million papers across arXiv, bioRxiv, and Nature, finding up to **22% of computer science papers** showed LLM modification. Their top markers: *pivotal, intricate, showcasing, realm*.

The mechanism matters for context-gating. Juzek & Ward (2025) confirmed experimentally that RLHF drives word overuse — annotators (many based in Kenya and Nigeria, per reporting on OpenAI's Sama partnership) preferred outputs matching their own formal English register. "Delve" is common in Nigerian business English. This means these words aren't inherently wrong; they're overrepresented because of a training artifact.

**High-confidence vocabulary markers** (10×+ frequency increase in Kobak's data): *delves, underscores, showcasing, commendable, meticulous, intricate, multifaceted, pivotal, realm, tapestry, landscape, foster, harness, nuanced, seamless, groundbreaking, transformative, robust*. **Context gate**: any of these in domain-appropriate use (archaeology for "delve," engineering for "robust") should pass. The signal is **co-occurrence** — three or more of these words in proximity is a stronger marker than any single instance.

**Hedging phrases** function differently. "It's important to note," "It bears mentioning," and "It's worth considering" are RLHF artifacts — the model is trained to sound thorough and cautious. These lack the quantitative rigor of the vocabulary studies but are widely documented by detection companies (GPTZero, Pangram Labs) and educators. **Confidence: medium.** These phrases appear in human academic writing, but their clustering density and formulaic deployment are the tell, not their mere presence.

**Filler affirmations** ("Great question!", "Absolutely!", "That's a fascinating point") are direct sycophancy artifacts from RLHF's optimization for user satisfaction. OpenAI acknowledged this in early 2025 and rolled back the behavior. **Confidence: high for conversational AI output; low for polished text** — these get edited out before publication.

### Punctuation: the em dash is famous but statistically weak

The em dash became a cultural meme as "the ChatGPT hyphen," but the evidence is more nuanced than the meme. Goedecke (2025) traced two plausible causes: training data skewed toward 19th-century public-domain books (which used **~30% more em dashes** than contemporary prose), and Sam Altman's admission that "they added more em dashes because people liked them" during RLHF. The em dash serves as a syntactic wildcard — it can replace commas, colons, or parentheses without requiring precise grammatical commitment, which suits probabilistic text generation.

However, a study cited in the *Indiana Capital Chronicle* found people who identified em dashes as AI tells had detection accuracy "only marginally better than chance." The *New Yorker* is notoriously em-dash-heavy. **This is a perceived tell more than a reliable tell** — a weak individual signal that only strengthens in combination. A tell killer should flag em dash density only when it exceeds roughly **3-4 per 500 words** alongside other markers.

Other punctuation patterns: AI **underuses semicolons and parenthetical asides** (Pangram Labs), maintains perfect Oxford comma consistency, and defaults to American English spelling. The broader tell is **sterile grammatical perfection** — no fragments, no sentences starting with "And" or "But," few contractions. This absence of imperfection is itself a signal.

### Structure: where AI is most reliably detectable

Structural tells have the strongest practitioner consensus even though they lack the quantitative precision of vocabulary studies. Zhang et al. (2024, arXiv) documented that LLMs overuse **lists and boldface** as a direct RLHF artifact — annotators preferred organized-looking outputs during preference training. The pattern catalog includes:

- **Heading inflation**: excessive subheadings, every section with identical sub-structure, Title Case on all headings
- **The rule of three**: reflexive tricolon ("keynote sessions, panel discussions, and networking opportunities") applied mechanically rather than rhetorically
- **Parallel construction overdose**: "not only X but also Y," "whether X or Y," repeated participial phrases — individually legitimate, collectively robotic
- **Summary paragraphs that restate everything**: AI conclusions beginning with "Overall" or "In summary" that contain zero new information
- **Elegant variation artifacts**: the repetition penalty forces unnatural synonym cycling — a character becomes "the protagonist," then "the key player," then "the eponymous figure"

**Confidence: high for pattern co-occurrence, medium for any individual structural feature.** The tell killer should flag structural tells only when multiple co-occur.

### Rhythm: the deepest statistical signal

GPTZero's core methodology rests on **burstiness** (sentence-length variance) and **perplexity** (word-choice predictability). Human writing mixes punchy fragments with sprawling complex sentences; AI maintains remarkably uniform sentence lengths. **Desaire et al. (2023)** in *Cell Reports Physical Science* found that standard deviation of words per paragraph was a "valuable differentiator" — a threshold of **SD > 25 words per paragraph = human; SD < 25 = AI** achieved >99% accuracy on academic science writing. One detector (Zovo) uses **SD < 4 words per sentence** across multi-paragraph text as an AI flag.

The "flat surprisal curve" concept — AI maintaining even predictability throughout, while human text has spikes and valleys of surprise — is well-established in computational linguistics but lacks a single clean quantitative benchmark. It manifests as the subjective sense that AI text "flows too smoothly with zero statistical surprises."

**Confidence: high for sentence-length variance as a detection feature; medium for specific thresholds** (the SD < 4 and SD < 25 numbers come from domain-specific studies that may not generalize).

### Transitions, openings, and semantic patterns

These are the most recognizable tells to human readers: "In today's fast-paced world," "Let's dive in," "Let's unpack this," "With that in mind." The VERMILLION framework (2025) notes that "uniform, formulaic transitions at fixed intervals are atypical of expert human style." AI paragraphs disproportionately open with "Furthermore," "Moreover," "Additionally" (Steere 2024, *Inside Higher Ed*).

Semantic tells include **false balance** ("While X, it's also true that Y" when the second clause is unwarranted), **excessive signposting** ("In this section, we will discuss..."), and **the Challenges + Future Prospects formula** documented in LLM-generated Wikipedia articles. These stem from RLHF's optimization for appearing thorough and balanced.

**Sources to read directly**: Kobak et al. (2025) in *Science Advances* (the definitive vocabulary study), Wikipedia's "Signs of AI writing" article (community-maintained, surprisingly thorough), Pangram Labs' detection guide (practitioner-focused taxonomy).

**Confidence: high.** The taxonomy is well-established across peer-reviewed, industry, and practitioner sources. The main uncertainty is **temporal instability** — "delve" dropped sharply in ChatGPT output by 2025, and all tells shift as models update.

---

## Q2: Detection thresholds and the false-positive minefield

### Hard numbers are scarce but converging

The RAID benchmark (Dugan et al., ACL 2024) — testing 12 detectors on 10M+ documents — is the gold standard. At **5% false-positive rate**, most detectors show reasonable accuracy. But most become **near-inoperative below 1% FPR**. ZeroGPT couldn't go below **16.9% FPR**. OpenAI's own classifier managed only **26% true-positive rate** at 9% FPR before being discontinued. Van Oijen (2023) found overall tool accuracy at just **27.9%**.

For the tell killer, these numbers mean: current AI detection is unreliable, so the goal isn't "fool detectors" but "remove patterns that make text *feel* AI-generated to human readers."

### Five documented false-positive cases reveal the danger zones

**Case 1: Non-native English speakers.** Liang et al. (2023, *Patterns*) found 7 GPT detectors misclassified **>61% of TOEFL essays** as AI-generated, with 19% unanimously flagged by all seven detectors. The root cause: lower perplexity from constrained vocabulary and simpler syntax. **This is the single most important false-positive risk.**

**Case 2: Texas A&M University (2023).** A professor accused his entire class of using ChatGPT by pasting essays into ChatGPT and asking "Did you write this?" — illustrating fundamental misunderstanding of detection, but the students' formal academic register was what initially raised suspicion.

**Case 3: UC Davis (2024).** Of 17 students flagged, **15 were false positives** (88% FPR in flagged cases), disproportionately non-native speakers and students who had worked with writing tutors — whose "cleaned up" prose triggered detection.

**Case 4: Behavioral health journals.** Testing 100 pre-AI research articles, free detectors flagged a median **27.2%** of genuinely human academic text as AI-generated.

**Case 5: Racial disparities.** A Common Sense survey found Black students were more likely to be falsely accused, and neurodivergent students flagged at higher rates due to reliance on repeated phrases.

### What humans actually notice isn't what detectors measure

Jakesch et al. (2023, *PNAS*, N=4,600) found humans detect AI text at **chance level (~50%)**. People rely on flawed heuristics: first-person pronouns and personal content signal "human," while lack of personal details signals "AI." The actual reliable cues (repetitiveness, nonsensical content) get overlooked. Critically, AI text optimized to exploit these heuristics was rated as **more human than actual human text** (65.7% human rating).

Clark et al. (2021, ACL) confirmed: GPT-3 text detected at random chance. Even with training, accuracy improved only to ~55%. Evaluators gave **contradictory reasons** for their judgments.

The counterpoint: Dugan et al. (2025) found that **frequent ChatGPT users** substantially outperformed commercial detectors, achieving near-perfect detection through expert majority vote. Their top giveaways: AI vocabulary clusters, formulaic structures, and lack of originality.

**Implications for the tell killer**: The "AI feel" is driven primarily by **structural formulaicness and vocabulary clustering**, not by any single feature. Overcorrecting vocabulary while leaving structure untouched will fail. Fixing structure while leaving a few vocabulary markers may be sufficient.

**Sources to read**: Liang et al. (2023) non-native speaker study (*Patterns*), Jakesch et al. (2023, *PNAS*), RAID benchmark (Dugan et al., ACL 2024).

**Confidence: high for false-positive patterns; medium for specific thresholds** — most quantitative thresholds come from domain-specific studies.

---

## Q3: Existing humanizer tools mostly make things worse

The DAMAGE paper (Masrour et al., ACL GenAIDetect 2025) studied 19 AI humanizer tools and found the best improved fluency in only **26% of cases** — meaning **74% of rewrites degraded text quality**. This is the defining problem of the space.

**Commercial tools** (Undetectable.ai, WriteHuman, StealthGPT, HIX Bypass) share a common failure mode: full-rewrite black boxes that trade quality for detection evasion. Undetectable.ai deliberately introduces grammatical errors; when corrected with Grammarly, AI detection scores rise again, proving the bypass is damage-dependent. WriteHuman's signature complaint is inconsistency — running the same text twice produces wildly different outputs, sometimes "unreadable."

**StealthWriter** stands out for offering **Easy/Medium/Aggressive modes** — the only major commercial tool with user-controlled aggression. **Grammarly's 2025 humanizer** adds voice learning from writing samples, the strongest guardrail against flattening the writer's style.

The best implementation found is the **blader/humanizer Claude skill** (10.5k GitHub stars). It uses a pattern-catalog approach targeting 20+ named AI tells, with a critical two-pass architecture: first pass rewrites based on the catalog, second pass asks "What makes this still obviously AI-generated?" and fixes remaining tells. This is the closest existing tool to the surgical, explain-then-fix model the user wants to build. Its explicit guidance to "have opinions," "let some mess in," and "use 'I' when it fits" directly addresses the overcorrection problem.

**The key lesson across all tools**: synonym swapping doesn't work because detectors measure perplexity and burstiness, not specific words. Effective humanization must change **sentence rhythm, information density, and structural variety** — the statistical fingerprint, not the surface vocabulary.

**Confidence: high.** The tool landscape is well-documented, and the failure patterns are consistent across sources.

---

## Key design decisions

> **Decision: Detection scope**
> Option A: Target detector evasion (optimize for fooling GPTZero, Originality.ai, etc.)
> Option B: Target human perception (remove patterns that make text *feel* AI-generated to readers)
> Tradeoff: A chases a moving target as detectors retrain; B produces durably better writing but won't guarantee detector scores drop.

> **Decision: Edit granularity**
> Option A: Sentence-level replacement (replace entire sentences containing tells)
> Option B: Sub-sentence surgical editing (swap only the specific tell phrase, preserving surrounding text)
> Tradeoff: A produces more natural rewrites but changes more of the writer's voice; B preserves voice but may leave awkward seams where the fix meets the original.

> **Decision: Single-pass vs. two-pass architecture**
> Option A: One pass — identify and fix tells simultaneously
> Option B: Two passes — first fix known tells, then audit the result for remaining AI feel (as blader/humanizer does)
> Tradeoff: B catches more tells and is self-correcting but doubles processing time and may overcorrect on the second pass.

> **Decision: Default aggression level**
> Option A: Conservative default — flag only high-confidence tells (co-occurring vocabulary clusters, structural patterns with 3+ markers)
> Option B: Moderate default — flag anything above medium confidence, including individual vocabulary markers
> Tradeoff: A will miss some tells but almost never overcorrect; B catches more but risks flagging legitimate vocabulary in academic, ESL, and formal writing contexts.

> **Decision: Explanation model**
> Option A: Silent editing — apply fixes and return clean text
> Option B: Annotated editing — show each flagged tell with its category and confidence before applying
> Tradeoff: A is faster and simpler; B builds user trust, enables learning, and lets the user override bad calls — but adds friction.

> **Decision: Context-gating implementation**
> Option A: Genre presets (academic, blog, business, creative) with different tell thresholds per genre
> Option B: Dynamic context inference — the skill reads the text's register and adjusts thresholds automatically
> Tradeoff: A is more predictable and debuggable; B is more flexible but may misjudge register, especially in mixed-tone writing.

> **Decision: Structural vs. lexical priority**
> Option A: Prioritize fixing vocabulary tells (the visible, meme-able markers like "delve" and "tapestry")
> Option B: Prioritize fixing structural and rhythm tells (sentence-length uniformity, heading inflation, list overuse)
> Tradeoff: A addresses what readers consciously notice and produces visible changes; B addresses what detectors actually measure and produces more fundamental improvement. The research strongly favors B — synonym swapping alone doesn't change the statistical fingerprint.
