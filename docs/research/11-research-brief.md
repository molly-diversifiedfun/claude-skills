# Research Brief — research-brief skill

Research synthesized from professional analytic-standards bodies (CIA, GRADE Working Group, Cochrane, RAND, Brookings) and 2025 LLM calibration literature. Goal: build a Claude skill that produces structured briefs with honest confidence ratings and zero fabricated citations.

---

## Q1 — What does a well-structured research brief look like?

### Findings

**ICD 203 (US Intelligence Community Analytic Standards).** Four standards govern every IC product: objectivity, political independence, timeliness, good tradecraft. Two language layers carry uncertainty: Words of Estimative Probability (WEP) for the *likelihood the claim is true*, and Levels of Confidence in Assessment (LCA) for *how strong the underlying evidence is*. These are kept separate on purpose — a claim can be "likely" but rest on "low confidence" sources, and the reader needs to see both. Sherman Kent's 1964 informal poll found analysts read "probable" as anything from 20% to 95%, which is exactly the failure mode a vague LLM brief reproduces.

The standardized WEP ladder used today (and adopted in CTI reporting via FIRST.org):

| Term | Approx. probability |
|---|---|
| Almost no chance / remote | 1–5% |
| Very unlikely / highly improbable | 5–20% |
| Unlikely / improbable | 20–45% |
| Roughly even chance | 45–55% |
| Likely / probable | 55–80% |
| Very likely / highly probable | 80–95% |
| Almost certain | 95–99% |

**GRADE (medicine).** Four-rung evidence quality scale — High, Moderate, Low, Very Low — applied to a *body of evidence*, not a single study. RCTs start High, observational studies start Low. Five downgrade factors (risk of bias, indirectness, inconsistency, imprecision, publication bias) and three upgrade factors (large effect, dose-response, plausible confounding pulling the other way). Critical structural insight: GRADE explicitly **separates certainty of evidence from strength of recommendation**. You can have low-certainty evidence supporting a strong recommendation if the alternative is worse, and vice versa. Endorsed by 100+ orgs including WHO, Cochrane, UpToDate.

**Cochrane Summary of Findings table.** Caps at seven outcomes (cognitive load), built around PICO (Population, Intervention, Comparison, Outcomes). Each row shows: the outcome, the magnitude of effect, the number of participants/studies behind it, and the GRADE certainty rating. The structural lesson: one row = one claim = one evidence rating. Don't bundle.

**RAND / Brookings briefs.** Both follow the same skeleton: title that conveys the finding, executive summary (the "boil-down" — often the only thing read), context, analysis, recommendations, methods/sources. RAND specifically frames briefs as "policy-oriented summaries of individual published, peer-reviewed documents or of a body of published work" — the brief is downstream of the research, not the research itself. Heavy use of headings, short sections, problem→solution flow.

### Sources

- [ICD 203 (DNI)](https://www.dni.gov/files/documents/ICD/ICD-203.pdf)
- [WEP and Analytic Confidences (CIS)](https://www.cisecurity.org/ms-isac/services/words-of-estimative-probability-analytic-confidences-and-structured-analytic-techniques)
- [Sherman Kent, Words of Estimative Probability (CIA)](https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf)
- [GRADE — Cochrane](https://www.cochrane.org/learn/courses-and-resources/cochrane-methodology/grade)
- [GRADE guidelines: 3. Rating the quality of evidence (PubMed)](https://pubmed.ncbi.nlm.nih.gov/21208779/)
- [Cochrane Handbook Ch. 3 — defining inclusion criteria](https://training.cochrane.org/handbook/current/chapter-03)
- [RAND Research Briefs](https://www.rand.org/pubs/research_briefs.html)
- [Brookings Policy Brief Series](https://www.brookings.edu/tags/brookings-policy-brief-series/)
- [FIRST.org CTI Reporting curriculum](https://www.first.org/global/sigs/cti/curriculum/cti-reporting)

### Confidence: **HIGH**
Primary documents from the standards bodies themselves. Decades of operational use. Multiple independent fields converged on the same architectural pattern (separate likelihood from evidence quality).

---

## Q2 — How should confidence scoring work in an LLM context?

### Findings

**LLMs are bad at this out of the box.** A 2025 ICLR paper ("Do LLMs Estimate Uncertainty Well?") found average AUROC for instruction-following uncertainty estimation hovers between 0.43 and 0.53 — chance. A JMIR Medical Informatics 2025 benchmark across 12 models and 5 medical specialties found that even the best models showed "minimal variation in confidence between right and wrong answers." Biomedical NLP calibration scores ranged from 23.9% to 46.6%. Translation: a model's raw "I'm 90% sure" is almost meaningless without help.

**But self-reported confidence beats alternatives.** Despite poor absolute calibration, the same body of work finds self-reported confidence achieves the *best relative* calibration across methods — average ECE 0.166 versus 0.229 for self-consistency sampling. The catch: confidence is heavily top-skewed. Models say "high" most of the time, creating what researchers call a "confidence floor." So you can't trust the absolute numbers, but the *ordinal ranking* (this claim is more confident than that one) carries real signal.

**Critique-based calibration helps.** 2025 work on Critique-Based Calibration teaches models patterns of over/under-confidence and yields meaningful ECE reduction even out of domain. The skill-design implication: if we *prompt* the model to explicitly distinguish source types before assigning confidence, we get better calibration than asking for a number cold.

**Three-source taxonomy is the right primitive.** Across the calibration literature, the cleanest signal comes from making the model name the *source* of its claim before rating it. The natural categories for a no-tools brief:
1. **Trained-knowledge** — "I learned this from documents in my training corpus." Verifiable but stale.
2. **Inference** — "I'm combining two trained facts to reach a new conclusion." Often right, often subtly wrong.
3. **Speculation** — "I'm extrapolating beyond what I have evidence for." Should be rare and always flagged.

**ICD 203 language is directly applicable.** WEP terms map cleanly onto Claude's natural hedging vocabulary, and they force the model to commit to a band rather than waffle. The GRADE four-rung scale (High/Moderate/Low/Very Low) is more practical than a 7-point WEP ladder for a consumer skill — fewer cognitive bins, faster to read. Recommend: GRADE-style four-rung scale for evidence quality, plus an inline tag for source type (training / inference / speculation).

### Sources

- [Do LLMs Estimate Uncertainty Well? (ICLR 2025)](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf)
- [Benchmarking the Confidence of LLMs (JMIR Medical Informatics 2025)](https://medinform.jmir.org/2025/1/e66917)
- [Calibration as a measurement of trustworthiness in biomedical NLP (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12249208/)
- [Confidence Calibration for Multimodal LLMs (MICCAI 2025)](https://papers.miccai.org/miccai-2025/paper/1840_paper.pdf)
- [Survey on the Honesty of LLMs (TMLR 2025)](https://github.com/SihengLi99/LLM-Honesty-Survey)
- [Know When You're Wrong: Aligning Confidence with Correctness (arXiv)](https://arxiv.org/html/2603.06604)

### Confidence: **HIGH** for the qualitative finding (LLMs underperform on self-confidence but ordinal rankings carry signal), **MODERATE** for the specific design recommendation (no head-to-head trial of "source-type prompting" vs. raw confidence requests in a research-brief context).

---

## Q3 — How to handle citations honestly?

### Findings

**The fabrication problem is huge and growing.** Stanford's 2024 study found general-purpose LLMs hallucinated in 58–88% of answers about randomly selected federal court cases. By 2026, over 700 court cases involve AI-fabricated citations, with monetary penalties averaging $4,713 (range $100–$31,100), public reprimands, and bar referrals. This isn't a lawyer-only problem — pro se litigants account for a similar share, meaning anyone treating LLM output as research is exposed.

**Why it happens.** LLMs are optimized for plausibility, not accuracy. They pattern-match the *shape* of a citation (case name + court + year + reporter) and fill it in from the latent space. The output looks right because it was generated from "what right looks like."

**The honest-citation pattern that works.** Don't generate citations. Generate **search-handles**: the exact phrase, author name, study name, or institution that — if it exists — would let the user find the source in 30 seconds. Pair with a source *type* tag ("peer-reviewed primary research," "industry survey," "trade press reporting," "anecdotal / single case study"). This is how Wikipedia's "citation needed" works, and how some retrieval-grounded tools (Perplexity, Elicit) flag low-evidence claims.

**Concrete rule for the skill.** Replace `[Smith et al. 2023, Journal of X, p. 47]` with `Search: "Smith outcome study 2023 healthcare" — type: peer-reviewed clinical trial`. The user can verify in seconds; the model can't fabricate something that's structurally not a citation. This also forces the model to admit when it can only describe a *type* of source rather than a specific one — which is the truthful state most of the time.

### Sources

- [Large Legal Fictions (Oxford Journal of Legal Analysis)](https://academic.oup.com/jla/article/16/1/64/7699227)
- [AI Hallucinations in Legal Work (The Legal Prompts, 2026)](https://thelegalprompts.com/blog/ai-hallucinations-legal-work-avoid-sanctions-2026)
- [GenAI's Legal Fictions (DC report)](https://websitedc.s3.amazonaws.com/documents/Hallucinations.pdf)
- [AI Hallucination Examples (Morph)](https://www.morphllm.com/ai-hallucination-examples)

### Confidence: **HIGH** on the problem (multiple primary studies, court records). **MODERATE** on the specific search-handle solution (logically sound and used by retrieval tools, but no controlled trial of "search-handles vs. fake citations" in a brief format).

---

## Q4 — Highest-value use cases?

### Findings

The brief format pays off when **structure and uncertainty matter more than freshness**. Specifically:

- **Strategy and decision support.** "Should we adopt X?" — the user needs the lay of the land, the strongest counter-arguments, and what to investigate further. Brief structure forces the model to surface the strongest cases for and against, not just the model's first instinct.
- **Pre-research scoping.** Before a deep-dive (consultant work, journalism, product spec), the brief tells you what's known, what's contested, and what to actually go read. Saves hours of unfocused googling.
- **Technical/medical/legal questions where users tend to over-trust LLM output.** The explicit confidence tags act as a circuit breaker — every "Low confidence" line is a "go verify" prompt.
- **Synthesis of contested topics.** "What does the evidence say about intermittent fasting?" Brief format surfaces conflicting studies instead of picking a winner.

**Where it underperforms:**
- **Real-time / current events.** No web access, training cutoff is the ceiling. Use Perplexity, Elicit, or browse-enabled tools.
- **Single-fact lookup.** "Population of Estonia." A brief for that is overkill.
- **Original research questions.** The skill summarizes; it doesn't replace primary research, fieldwork, or interviews.
- **High-stakes legal/medical decisions.** Useful as scoping, never as the final word.

### Sources
Inferred from Q1–Q3 sources; no single primary study on "best use cases for LLM-generated briefs" exists. This synthesis combines the honest-citation literature (Q3) and the tool-use literature on LLMs.

### Confidence: **MODERATE.** Logically grounded but not directly studied. Treat as a starting heuristic, refine with user feedback.

---

## Key Design Decisions

| # | Decision | Choice | Tradeoff |
|---|---|---|---|
| 1 | Confidence scale | **GRADE 4-rung (High / Moderate / Low / Very Low)** at the claim level | WEP's 7-point ladder is more precise but cognitively heavier. GRADE is the global medical standard for a reason — four bins is what humans can hold. We lose probability granularity; we gain readability and faster pattern-recognition by users. |
| 2 | Source type tag | **Three primitives: trained-knowledge / inference / speculation** | Adds visual noise to every claim. But the literature is clear that source-type prompting is what actually moves calibration — and it's the specific countermeasure to the lawyer-fabrication problem. Worth the noise. |
| 3 | Citations | **No fabricated citations. Generate search-handles + source-type only.** | Users may want plug-and-play references. We force them to verify, which is slower. The alternative is the 700-court-cases failure mode. Non-negotiable. |
| 4 | Separating likelihood from evidence quality | **Combine into a single Confidence rating** (instead of ICD's two-dimensional WEP × LCA) | The IC's two-axis system is more rigorous but produces output like "likely (low confidence)" that confuses non-analyst readers. Collapse to one axis at the cost of rigor. Power users can ask for the split. |
| 5 | Brief length / structure | **Fixed sections: TL;DR → What we know → What's contested → What's unknown → What to verify** | Could be more freeform. But "what's contested" and "what's unknown" are the highest-leverage sections (where most LLM output fails) and dropping them defeats the purpose. Force the structure. |
| 6 | Iteration model | **Single-pass with explicit "ask me to dig deeper on section X"** | Could be multi-turn by default like a research assistant. But most uses are scoping, and multi-turn balloons context. One-shot output, optional follow-up. |
| 7 | Domain coverage | **General-purpose, not domain-specialized** | Medical/legal/financial briefs would benefit from domain-specific quality scales. But the calibration research suggests the generic three-source taxonomy travels well across domains. Specialize later if data supports it. |

---

## Output Template v1

```markdown
# Research Brief: [Question]

## TL;DR
[2-3 sentences. The single most important thing the user should know.
End with a confidence tag for the overall picture.]
**Overall confidence: [High / Moderate / Low / Very Low]**

## What We Know (well-supported)
- **[Claim].** [1-2 sentence elaboration.]
  - *Confidence: High* | *Source type: peer-reviewed research / industry data / widely-reported*
  - *Verify with: search "[specific phrase or author + topic]"*

## What's Contested (genuine disagreement in the field)
- **[Position A]:** [Who holds it, what they argue, why]
  - *Source type: [type] | Verify: search "[handle]"*
- **[Position B]:** [Who holds it, what they argue, why]
  - *Source type: [type] | Verify: search "[handle]"*
- *My read: [optional one-line synthesis, tagged as inference]*

## What's Inference (my synthesis, not direct knowledge)
- **[Claim].** [Why I'm inferring this — what facts I'm combining.]
  - *Confidence: Moderate* | *Source type: inference from [A] + [B]*
  - *Verify with: [what to check that would confirm or break the inference]*

## What's Unknown / Where I'd Speculate
- **[Open question].** [What we'd need to know.]
  - *Confidence: Low — speculation only*
  - *Verify with: [what kind of source would settle this]*

## What to Read Next
- For the strongest "yes" case: search "[handle]" — type: [source type]
- For the strongest "no" case: search "[handle]" — type: [source type]
- For the methodology debate: search "[handle]" — type: [source type]
- For a recent overview: search "[handle]" — type: [source type]

## Confidence Scale (reference)
- **High** — multiple independent well-documented sources in training data, low ambiguity, recent
- **Moderate** — supported by training data but limited sources, or older, or some ambiguity
- **Low** — partial evidence, indirect inference, or significant unknowns
- **Very Low / Speculation** — extrapolation beyond evidence; treat as hypothesis only
```

### Source-handling protocol (always applied)

1. **Never** generate a citation in the form `Author (Year), Journal, p. NN`. Always generate a search-handle the user can paste into a search bar.
2. **Always** tag source type when making a substantive claim. Categories: peer-reviewed research, industry/government data, trade press reporting, expert commentary, anecdotal / single case, inference, speculation.
3. **Always** distinguish trained-knowledge from inference from speculation in-line, not in a footnote the user might miss.
4. **When unsure whether a specific source exists**, write: *"There is likely work on [X] from [field/era] — search '[handle]' to find current sources"* rather than naming a specific paper.
5. **Treat freshness as a confidence-reducer.** Anything time-sensitive (markets, current events, recent research) gets a confidence downgrade with an explicit note about training cutoff.
