# PRD: resume-rebuilder

## Problem

67% of job seekers use AI for resumes. 33.5% of hiring managers can spot them in under 20 seconds. 57% are less likely to hire candidates with obviously AI-generated applications. The word "spearheaded" is functionally radioactive. Every AI resume tool — Teal, Jobscan, Rezi, Resume.io — runs a one-pass pipeline from job title to formatted bullet, which is exactly why the output triggers detection. No competing tool extracts real evidence before generating content.

## Solution

An evidence-bank-first resume skill. Phase 1: structured interview extracts the user's real achievements with specific metrics, tools, and context. Phase 2: generates a resume from that evidence bank, tailored to a target job description. The output reads as human-written because it's built from real, specific, verifiable data — not template language. Never invents experience. Never uses buzzwords. Includes cover letter as optional second output from the same evidence base.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| One-pass vs. evidence-bank-first | **Evidence bank first** | Every competitor does one-pass. Every detection signal traces to lack of real evidence. This is the entire differentiator. |
| Anti-detection logic | **Baked into defaults, not exposed as controls** | Hardcode constraints (no hallucinations, no buzzword stacking, varied structure). Stylistic variation is default behavior, not a toggle. Avoids adversarial "cheating tool" frame. |
| Industry-specific vs. generic | **Generic pipeline with level-calibration** | The evidence bank handles industry specificity naturally — finance achievements sound like finance. Level-calibration (entry vs. senior language intensity) matters more than industry templates. |
| ATS vs. human optimization | **Human-first on language, ATS-safe on formatting** | Modern ATS rewards contextual keyword usage, penalizes stuffing. Standard formatting (single column, standard fonts, no tables/graphics) as non-negotiable baseline. Optimize language for the 6-second recruiter scan. |
| Metric presentation | **Mixed quantified + qualitative, metrics only with real data** | "Increased revenue 40%" without mechanism is now an AI tell. Mix measured and unmeasured bullets like humans actually write. Apply the Sperry "manager verification test" to every metric. |
| Interview depth | **Tiered: fast pass to minimum viable, option to deepen** | Minimum: 3 achievements per role (6-9 total). Ideal: 5-7 per role (25-30 total). Design for fast completion with deepening as an opt-in. |
| Cover letter | **Optional second output from same evidence bank** | 83% of hiring managers read cover letters. The evidence bank naturally contains the stories cover letters need. Prompt: "Want a tailored cover letter from your evidence bank?" |

## Interaction Model

### Phase 1: Evidence Bank Extraction (10-20 min)

**Step 1: Basic context** (2 questions)
1. "What role are you targeting? Paste the job description if you have one."
2. "Walk me through your work history — most recent first. Job title, company, how long, one sentence on what you did."

**Step 2: Achievement extraction per role** (3-5 questions per role)

For each role, use the "So What?" cascade + Karissa Justice's six questions:

1. "What's the thing you're proudest of in this role?"
   → Follow up: "So what? Why did that matter to the business?"
   → Follow up: "Can you put a number on it? Revenue, time saved, users affected, team size?"

2. "What did you build, fix, or change that someone else would notice?"
   → Apply six questions: Who was it for? How many? How often? How long? What tools? What examples?

3. "What would your manager say was your biggest contribution?"

4. (If user says "I don't have metrics"): "Let's find them. How big was the team? The budget? The customer base? How much time did something take before vs. after? Did anything get faster, cheaper, or bigger?"

5. (If quantifiable): "One more — is there anything you did that was unusual for your level? Something a typical [title] wouldn't have done?"

**Minimum viable bank:** 3 achievements per role, 2-3 roles = 6-9 achievements.
**Ideal bank:** 5-7 per role = 25-30 achievements.

After minimum viable reached: "We have enough for a solid resume. Want to go deeper on any role, or should I generate?"

**Step 3: Store evidence bank as artifact**
- Raw achievement data with metrics, tools, context
- This bank is reusable across multiple job applications
- Output format: structured markdown the user can save

### Phase 2: Resume Generation (automatic)

**Input:** Evidence bank + target job description

**Generation rules (hardcoded, not configurable):**

Content constraints:
- Never invent experience, metrics, tools, or certifications
- Never use: spearheaded, leverage, synergize, dynamic, passionate, rockstar, results-driven, proven track record, strategic thinker
- Never open summary with "Accomplished [role] with [N] years of experience in [gerund]"
- Every achievement must include company-specific detail (tool names, team sizes, product names)
- Calibrate language intensity to career level (no "architected end-to-end solutions" for entry-level)
- Apply "manager verification test": would their old manager confirm this is fair?

Structural constraints:
- Vary bullet length (mix one-line and two-line bullets in same section)
- Vary sentence openings (not all "Verb + object" — some lead with result, some with context)
- Mix active and passive voice occasionally
- Vary grammatical structure across bullets (fragments, complete sentences, different clause patterns)
- No more than 2 consecutive bullets starting with the same word class

Format constraints:
- Reverse chronological (functional format is viewed with suspicion)
- Length: 1 page (0-5 years), 1-2 pages (5-10 years), 2 pages (10+ years)
- Single column, standard fonts, no tables or graphics (ATS-safe baseline)
- Keywords embedded in authentic achievement statements, never in dedicated keyword sections

Metric constraints:
- Include mechanism with every metric ("Grew pipeline from $2.1M to $2.9M over two quarters by restructuring outbound in Outreach.io")
- Not every bullet needs a metric — mix quantified and qualitative like humans write
- Flag any generated metric that didn't come from the evidence bank (should never happen, but safeguard)

**Output format:** Use RAC (Result-Action-Context) for bullets — front-load the outcome, then method, matching how recruiters scan.

### Phase 3: Review + Tailoring (2-3 min)

- Present generated resume
- "Anything here that isn't true or that you'd phrase differently?"
- If user has a specific JD: "Want me to adjust emphasis for this role? I'll re-rank from your evidence bank."
- Offer cover letter: "I can also generate a tailored cover letter from your evidence bank. Want one?"

### Cover Letter Generation (if requested)

Uses the evidence bank to produce a cover letter that:
- Opens with why THIS company (requires user input or JD context)
- Tells 1-2 specific achievement stories from the bank
- Explains the connection between past work and target role
- Closes with a concrete next step
- Matches the voice register of the resume
- Never uses "I am writing to express my interest in" or similar template openers

## The Ten Signals This Skill Prevents

1. **Hallucinated credentials** → Hard constraint: only uses evidence bank data
2. **Hidden keyword stuffing** → Keywords embedded in achievements only
3. **Buzzword summaries** → Banned phrase list hardcoded
4. **Generic achievements** → Evidence bank forces company-specific detail
5. **Tone-experience mismatch** → Level-calibrated language intensity
6. **Identical sentence structures** → Structural variation rules
7. **Robotic phrasing** → Natural language with deliberate imperfection
8. **JD mirroring** → Paraphrases rather than echoes JD language
9. **Keyword overrepetition** → Contextual embedding, not repetition
10. **Uniform bullet rhythm** → Varied length and structure mandated

## Success Criteria

- Resume passes the "manager verification test" — every claim is something the user's former manager would confirm
- A recruiter who reviews 100+ resumes weekly cannot identify the output as AI-generated
- The evidence bank is reusable — user can generate multiple tailored resumes from the same bank
- Total time from start to finished resume: under 30 minutes (including evidence extraction)
- Cover letter uses different achievement stories than the resume (draws from the full bank)

## What This Skill Does NOT Do

- Write resumes without real input (no "generate a resume for a project manager" — needs YOUR evidence)
- Guarantee ATS scores (ATS optimization is table-stakes formatting, not the skill's focus)
- Design visual resume layouts (text output only — user formats in their tool of choice)
- Prepare for interviews (interview-coach handles that, and can consume the evidence bank)

## Pairs With

- **voice-extractor**: Load voice profile to ensure resume matches the user's natural writing style
- **ai-tell-killer**: Run on the generated resume as a final pass to catch any remaining AI fingerprint
- **interview-coach**: The evidence bank feeds directly into interview prep — same achievements, different format
