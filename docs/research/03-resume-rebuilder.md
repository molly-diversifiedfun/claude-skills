# Resume Rebuilder — Research Results

The single most important finding across all research: **no competing tool extracts evidence before generating content**. Every AI resume product — Teal, Jobscan, Rezi, Resume.io, Kickresume — runs a one-pass pipeline from job title to formatted bullet. That architectural choice is exactly why their output triggers the detection signals recruiters now recognize in under 20 seconds. An evidence-bank-first workflow is not just a differentiator; it's the only architecture that can produce resumes grounded in real experience rather than plausible-sounding templates.

---

## Q1 — Detection signals that get resumes rejected

### Findings

Recruiters don't detect AI resumes through sophisticated analysis. They detect them through **pattern fatigue** — seeing the same phrases, structures, and rhythms hundreds of times per week until the pattern becomes unmistakable. A 2025 TopResume survey of 600 U.S. hiring managers found **33.5% can identify AI-generated resumes in under 20 seconds**, and 19.6% would instantly reject a fully AI-written resume without further review. The commonly cited "74% detection rate" is a conflation of different surveys — the actual ResumeBuilder figure (2023) measured interview callback rates for ChatGPT users, not detection accuracy.

**Lexical signals — the words that trigger immediate suspicion.** The highest-risk category. The word "spearheaded" is now functionally radioactive — cited across six independent sources as an AI tell. The Willo blog published a list of 17 AI-flagged verbs: leverage, synergize, spearhead, facilitate, optimize, streamline, drive, execute, pioneer, champion, orchestrate, innovate, transform, catalyze, implement, enhance, strategize. But the real killer isn't individual words — it's **verb stacking**, where every bullet opens with the same grammatical pattern. One recruiting newsletter put it directly: "Avoid stacking five bullets that all start with 'Built' or 'Leveraged.' That's what AI detectors listen for — how predictable your sentence structure is." The skill must vary sentence openings, mix passive and active constructions, and occasionally lead with the result or context rather than an action verb.

Specific phrases that produce instant recognition: "Results-driven professional with a proven track record," "dynamic leader," "strategic thinker," "leveraged synergies to maximize efficiencies," and any summary opening with "Accomplished [role] with [number] years of experience in [gerund phrase]." Lisa Shaver at Toast summarized it: "Where AI falls flat is the often business-jargony, over-embellished language that brings no real texture to a job seeker's previous responsibilities."

**Structural signals — the formatting and rhythm tells.** AI produces unnervingly **uniform bullet points** — identical length, identical grammatical structure, identical information density. Human resumes have natural variation: some bullets are terse, others expand. Some use fragments, others use complete sentences. The skill should deliberately vary bullet length (one-line and two-line bullets in the same section) and mix sentence structures. A second structural tell is **tonal inconsistency between sections** — when a human-written education section sits next to an AI-polished experience section, the voice mismatch creates what one source called "cognitive dissonance that hiring managers notice immediately."

**Content signals — the substance failures that matter most.** Three content-level signals trigger the strongest negative reactions:

First, **generic achievements that could describe anyone in the role**. "Led cross-functional teams to deliver projects on time" is the canonical example — true of every project manager who ever lived. GPTZero's hiring team noted: "If a resume bullet could describe almost anyone in a similar role and still be accurate, it's probably AI-generated." The fix is company-specific detail: tool names, team sizes, product names, internal systems.

Second, **tone-experience mismatch** — entry-level candidates claiming to have "architected end-to-end solutions" or "driven organizational transformation." One source warned these claims "collapse under even light questioning. What model? What infra? What transformation?" The skill must calibrate language intensity to career level.

Third, and most damaging: **hallucinated credentials or skills**. AI tools routinely invent certifications, assume programming language proficiency, or fabricate metrics. Multiple hiring managers stated this is grounds for permanent disqualification. The skill's hard constraint — never invent experience or metrics — directly addresses the highest-severity detection signal.

**Formatting and technical signals.** Em-dash overuse is a minor but real AI fingerprint. Placeholder artifacts ("[Your Name]," "CompanyName") are instant disqualifiers. Hidden white text for keyword stuffing, if discovered, is treated as fraud. More subtly, **perfectly consistent formatting** from AI-generated templates can feel uncanny — human-created documents have slight imperfections that signal authenticity.

**ATS-level AI detection does not currently exist.** No major ATS platform (Workday, Greenhouse, Lever, Ashby) has built-in AI-content detection as of early 2026. ATS systems focus on keyword matching and candidate ranking. Some employers use external tools like GPTZero or Copyleaks as a separate screening step, and a few tech companies reportedly auto-reject detected AI content, but this is not standard practice. Modern ATS does penalize keyword stuffing and can detect copy-pasted job descriptions — both AI-adjacent signals.

### The ten signals the skill must avoid, ranked by severity

1. Hallucinated credentials or fabricated metrics (career-ending)
2. Hidden keyword stuffing via white text (treated as fraud)
3. "Results-driven professional" and similar buzzword summaries (recognized instantly)
4. Generic achievements without company-specific detail (most common AI tell)
5. Tone-experience level mismatch (collapses in interviews)
6. Identical sentence structures across bullets (what detectors flag algorithmically)
7. Robotic phrasing no human would speak aloud (fails the read-aloud test)
8. Near-verbatim job description mirroring (flagged by some ATS)
9. Keyword repetition beyond natural usage (43% of recruiters call it dishonest)
10. Uniform bullet length and rhythm (subtle but cumulative)

### Sources
- TopResume AI in Hiring Survey, May 2025 (n=600) — topresume.com
- Willo "How to Detect AI-Generated Resumes," Aug 2025 — willo.video/blog
- Nate's Newsletter "AI Resume Survival Guide," Dec 2025 — natesnewsletter.substack.com
- GPTZero "AI Resume Detector" guide — gptzero.me
- Resume Pilots "Spotting the AI Tells" — resumepilots.com
- Rezi.ai detection guide — rezi.ai/posts
- Dice.com recruiter interviews — dice.com
- ResumeBuilder ChatGPT survey, Feb 2023 (n=1,000) — resumebuilder.com

### Confidence: High
Multiple independent sources converge on the same signal categories. Survey methodologies have limitations (self-reported, online panels), but practitioner accounts are remarkably consistent.

---

## Q2 — What effective resumes look like now

### Findings

**Yes, "increased revenue 40%" has become an AI tell** — but only when presented without mechanism, context, or timeframe. Executive search consultant Kristof Schoenarts observed that "recruiters are drowning in CVs inflated with fake skills, overblown claims, and slick verbiage." A 2025 Resume Now survey of **925 HR professionals** found 62% reject resumes without personalization and 90% report increased "low-effort or spammy applications" driven by AI.

The distinction between believable and suspicious metrics comes down to **specificity of method**. A suspicious metric: "Increased revenue 40%." A believable metric: "Grew enterprise pipeline from $2.1M to $2.9M over two quarters by restructuring the outbound sequence in Outreach.io to target VP-level buyers." The difference: tool names, timeframes, mechanism, reasonable scale for the role. Cole Sperry's useful test: "If the recruiter called your old manager and asked if it's true, would your old manager laugh? Or would they say 'yes, that's fair'?" The skill should generate metrics that pass this test and flag any that don't.

**Format expectations remain stratified by level but stable.** Reverse chronological dominates — functional resumes are actively viewed with suspicion. Entry-level through five years: one page, firm. Five to ten years: one page preferred, two acceptable if content warrants. Ten-plus years: two pages standard. Executive: two pages, rarely three. Former Google recruiter Keanna Carter: "People think the more they include, the more chances they'll get the interview. But there's no correlation." Harvard Business School's practical advice: never submit 1.25 pages — commit to one or two.

**ATS systems have evolved significantly.** Modern platforms now use contextual understanding rather than pure keyword counting. They evaluate whether experience genuinely matches requirements, penalize keyword stuffing, and some track identical content across multiple applications to the same company. Steph Cartwright (CPRW) confirmed: "Instead of just looking at keywords, it's looking at everything you're saying in your resume and drawing conclusions about your skills and experience." The implication: the skill should embed keywords through authentic achievement statements, not through dedicated keyword sections or forced repetition.

**The 2025 AI Resume Paradox.** The most strategic finding: AI makes "perfect" resumes trivially easy to produce, which has made recruiters **more suspicious of perfection and more attuned to authenticity signals**. The differentiator is no longer polish — everyone has that. It's specificity, verifiable context, and a voice that sounds like a real person wrote it. Recruiter Kristen Zavo: "AI-generated 'slop' resumes usually look overly polished but oddly generic. They're packed with buzzwords, vague claims, and copy-and-paste phrasing that could apply to anyone." The skill should deliberately preserve imperfection — occasional sentence fragments, varied rhythm, industry-specific shorthand that only an insider would use.

### Sources
- Resume Now "2025 AI and the Applicant Report" (n=925 HR professionals) — resume-now.com
- Artisan Talent "The Rise of AI Resume Slop," Sept 2025 — creative.artisantalent.com
- The Connors Group "50 Resume Buzzwords to Avoid," Oct 2025 — theconnorsgroup.com
- Huntress "AI-Enhanced Candidate Fraud," late 2025 — huntress.com/blog
- Jobscan 2025, quoting Keanna Carter (former Google recruiter) — jobscan.co

### Confidence: High
Survey data from 925 HR professionals is unusually robust for this category. Practitioner quotes from named recruiters with hiring authority add strong qualitative support.

---

## Q3 — Evidence extraction methods

### Findings

The most effective extraction technique for people who claim they have no metrics is the **"So What?" cascade** — repeatedly asking "so what? why did that matter?" until bottom-line impact surfaces. A resume consultant at DistinctiveWeb demonstrated the method: a client's "redesigned marketing materials" becomes, after four rounds of "so what?", a quantified story about recovering lost sales. Pair this with **Karissa Justice's six questions** applied to every bullet: Who was it for? How many? How often? How long? What type? What examples? These questions transform vague descriptions into specific, measurable statements without requiring the user to have pre-existing metrics.

**CAR (Challenge-Action-Result) is the optimal output framework for resume bullets.** It's the dominant framework among certified professional resume writers because it produces tight, one-line bullets. STAR (Situation-Task-Action-Result) is better suited as an *intake* framework during evidence gathering — the Situation and Task components capture context that CAR compresses away. The skill should use STAR-like prompting during extraction and CAR/RAC formatting during generation. Kamara Toffolo's **RAC variant** (Result-Action-Context) is particularly effective because it front-loads the outcome, matching how recruiters scan — result first, method second.

For people with genuinely non-quantifiable work, Toffolo provides four alternative categories: innovation and change (processes automated, tools adopted), influence and strategy (change management, thought leadership), recognition (promotions earned and why), and relationships (trust built and its business value). Cole Sperry's **Context vs. Results taxonomy** is the cleanest framework for the skill to use internally: Context Metrics provide scale (team size, budget, geographic scope) while Results Metrics provide evidence of performance (what improved, saved, or prevented).

**Target evidence bank size: 25-30 achievements total, minimum 3 per role.** Irina Pichura (professional resume writer) recommends 3-5 measurable accomplishments per position on the final resume. For a bank that enables tailoring across multiple job applications, practitioners recommend collecting roughly double the final output — **5-7 achievements per role for senior professionals, 3-5 for mid-career**. The bank should be larger than any single resume to enable selection by relevance.

### Sources
- Kamara Toffolo RAC methodology — kamaratoffolo.com
- Cole Sperry/Optim Careers Context-Results framework — optimcareers.com
- Karissa Justice/Work Can Be Better — workcanbebetter.com
- Cultivated Culture "Brag Sheet" method — cultivatedculture.com
- A Portland Career C-cAR method — aportlandcareer.com

### Confidence: Medium-High
Frameworks are well-established among career professionals. The specific bank-size numbers are practitioner estimates rather than empirical research, but they converge across sources.

---

## Q4 — Competitive landscape and gaps

### Findings

Every major AI resume tool shares the same architectural flaw: **they generate from job titles and descriptions, not from extracted evidence**. Teal's bullet generator writes "notes for an award speech" — over-indexed on metrics, under-indexed on how results were achieved. Jobscan's "One Click Optimize" inflated a score from 52 to 100 by stuffing keywords the user never claimed — a recruiter seeing that resume "will immediately spot the generic, AI-generated language." Resume.io's AI was described on Product Hunt as "absolutely useless — it just summarizes your job descriptions in a simplistic, generic way." Rezi's AI bullet writer produced output that "read more like job-description responsibilities than resume achievements" and actually *removed* key details when asked to improve existing text. Kickresume was characterized as "misplaced AI-bandaids" bolted onto a graphic design tool.

The gap is clear and structural. **No tool has an evidence bank concept.** No tool conducts a structured interview. No tool stores raw achievements separately from formatted resume text. No tool asks follow-up questions like "You said you improved customer satisfaction — by how much? How did you measure it?" Rezi's "AI Agent" comes closest with a conversational interface but functions as a navigation layer for existing features, not a true interviewing system.

**Cover letters should be included as a natural extension, not a separate skill.** 83% of hiring managers read them even when not required, and 45% read them *before* the resume. The evidence bank approach is uniquely suited to cover letters because they require specific stories — why this role, why this company, why now — that a well-populated bank already contains. Position it as a second output from the same evidence base rather than a distinct workflow.

### Sources
- Cole Sperry/Optim Careers review of Teal — optimcareers.com
- LandThisJob review of Jobscan — landthisjob.com
- Product Hunt reviews of Resume.io (1.5/5, 195 reviews)
- Resume Genius CPRW review of Rezi
- HBR "Cover Letters Still Matter," March 2025

### Confidence: Medium
Tool reviews are a mix of professional evaluators and user complaints; selection bias toward negative reviews is inherent. Feature assessments are reliable; user sentiment ratios may not be representative.

---

## Design decisions

**Decision 1: One-pass generation vs. evidence-bank-first workflow**
Option A: Generate resume directly from JD + user's existing resume — prioritizes speed.
Option B: Extract evidence bank first through structured interview, then generate — prioritizes quality.
Tradeoff: Option A ships faster and handles the "I need a resume tonight" use case. Option B produces fundamentally better output but requires 15-30 minutes of user engagement.
Signal from research: Every competitor does Option A. Every detection signal traces back to the lack of real evidence behind generated text. Option B is the entire differentiator.

**Decision 2: How much anti-detection logic to make explicit vs. bake into defaults**
Option A: Expose anti-detection as visible controls (e.g., "vary sentence rhythm," "reduce buzzword density") — prioritizes user understanding and control.
Option B: Bake all anti-detection into default generation behavior — prioritizes simplicity and avoids an adversarial frame.
Tradeoff: Option A risks the skill feeling like a "cheating tool." Option B risks users not understanding why output reads the way it does.
Signal from research: The most damaging signals (hallucinations, buzzword stacking, uniform structure) should be hardcoded constraints. Stylistic variation should be a default behavior, not a toggle.

**Decision 3: Generic best practices vs. industry-specific generation**
Option A: One generation pipeline with universal resume principles — prioritizes simplicity and maintenance.
Option B: Industry-specific templates and vocabulary (e.g., finance vs. creative vs. engineering) — prioritizes output accuracy.
Tradeoff: Industries have genuinely different norms (banking still expects one page at 10+ years; creative roles tolerate design elements). But maintaining industry templates adds significant complexity.
Signal from research: The evidence bank itself handles most industry specificity — real achievements from finance naturally sound like finance. The skill needs level-calibration (entry vs. senior language intensity) more than it needs industry templates.

**Decision 4: Optimize for ATS parsing or human readability when they conflict**
Option A: ATS-first — single column, no formatting, keyword-dense — prioritizes passing automated screens.
Option B: Human-first — readable, natural language, strategic formatting — prioritizes the 6-second recruiter scan.
Tradeoff: Modern ATS is context-aware and penalizes keyword stuffing. But 75% of qualified candidates are still filtered by ATS formatting issues.
Signal from research: The conflict is smaller than it was. ATS now rewards contextual keyword usage embedded in real achievements. Use standard formatting (single column, standard fonts, no tables/graphics) as a non-negotiable baseline, then optimize language for human readers.

**Decision 5: Metric presentation strategy**
Option A: Include quantified metrics on every bullet — prioritizes impact density.
Option B: Mix quantified and qualitative bullets, with metrics only where the user has real data — prioritizes authenticity.
Tradeoff: Option A produces AI-detectable uniformity. Option B matches how humans actually write — some things they measured, others they didn't.
Signal from research: "Increased revenue 40%" without mechanism is now an AI tell. Option B with the Sperry "manager verification test" applied to every metric is the safer approach.

**Decision 6: Evidence bank interview depth**
Option A: Quick extraction — 5-8 questions per role, ~10 minutes total — prioritizes completion rate.
Option B: Deep extraction — 15-20 questions per role using "So What?" cascades and the six-question framework — prioritizes bank quality.
Tradeoff: Deeper interviews produce better raw material but risk user dropout. A 20-minute interview for three roles is an hour of engagement.
Signal from research: The minimum viable bank is 3 achievements per role (6-9 total). Ideal is 5-7 per role (25-30 total). Design for a tiered approach: fast pass to reach minimum viable, with option to deepen any role.

**Decision 7: Cover letter as bundled output vs. separate invocation**
Option A: Always generate a cover letter alongside the resume — prioritizes completeness.
Option B: Offer cover letter as an optional second output from the same evidence bank — prioritizes user control.
Tradeoff: Bundling increases perceived value but may produce unwanted output. Separating requires the user to know they can ask.
Signal from research: 83% of hiring managers read cover letters. The evidence bank naturally contains the stories cover letters need. Option B with a clear prompt ("I can also generate a tailored cover letter from your evidence bank — want one?") captures both benefits.
