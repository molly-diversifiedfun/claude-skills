# Resume Rebuilder

## The Problem

67% of job seekers now use AI for resumes. The result: 33.5% of hiring managers can spot AI-generated resumes in under 20 seconds, and 57% are less likely to hire when they do. The word "spearheaded" is functionally radioactive. "Results-driven professional with a proven track record" is an instant rejection trigger.

Every AI resume tool on the market — Teal, Jobscan, Rezi, Resume.io, Kickresume — runs the same broken pipeline: job title in, formatted bullets out. No evidence. No interview. No verification. That one-pass architecture is exactly why the output triggers every detection signal recruiters have learned to recognize.

The gap is structural. No competing tool has an evidence bank concept. No tool conducts a structured interview. No tool stores raw achievements separately from formatted resume text. No tool asks "you said you improved satisfaction — by how much? How did you measure it?"

## What It Does

Resume Rebuilder uses an **evidence-bank-first architecture** that no competitor has implemented.

**Phase 1: Structured Interview (10-20 min)** — Extracts your real achievements through targeted questions. Uses the "So What?" cascade to push vague answers into specific, measurable claims. Applies six diagnostic questions to every achievement: Who? How many? How often? How long? What tools? What examples?

**Phase 2: Resume Generation (automatic)** — Builds a tailored resume from your evidence bank matched to a target job description. Every bullet traces to something you actually said. Every metric includes the mechanism (how you did it), the timeframe, and the tools.

**Phase 3: Review + Tailoring** — You verify accuracy, adjust emphasis, and optionally request a cover letter from the same evidence bank.

The evidence bank is reusable. Interview once, generate resumes for multiple roles by re-ranking and re-selecting — no new claims, just different prioritization.

### Cover Letters

Optional second output from the same evidence bank. 83% of hiring managers read cover letters even when not required. The bank already contains the specific stories cover letters need. Different achievements than the resume's top bullets when the bank is large enough.

## How to Use It

### In Claude.ai

Start a conversation and say:
- "Help me with my resume"
- "I need to update my resume for [role]"
- "Tailor my resume for this job description"
- "Write me a cover letter"

The skill triggers automatically on resume-related requests. It will walk you through the interview before generating anything.

### In Claude Code

Reference the skill directly:

```
claude "Read ~/github/claude-code-toolkit/skills/resume-rebuilder/SKILL.md and help me rebuild my resume for [target role]"
```

Or add to your project's `CLAUDE.md`:

```markdown
# Skills
- When working on resumes, read ~/github/claude-code-toolkit/skills/resume-rebuilder/SKILL.md
```

### Returning Users

If you already have an evidence bank from a previous session, paste it in. The skill skips the interview and goes straight to generation with a new JD.

## The 10 Detection Signals

These are the patterns that get AI resumes rejected. The skill prevents all of them by design.

1. **Hallucinated credentials** — fabricated metrics or certifications (career-ending)
2. **Hidden keyword stuffing** — white text or dedicated keyword sections (treated as fraud)
3. **Buzzword summaries** — "Results-driven professional with a proven track record" (instant recognition)
4. **Generic achievements** — bullets that could describe anyone in the role (most common AI tell)
5. **Tone-experience mismatch** — entry-level candidates "architecting end-to-end solutions" (collapses in interviews)
6. **Identical sentence structures** — every bullet opens Verb + Object (what detectors flag algorithmically)
7. **Robotic phrasing** — language no human would speak aloud (fails the read-aloud test)
8. **JD mirroring** — near-verbatim copy of job description language (flagged by some ATS)
9. **Keyword overrepetition** — same term crammed in 5+ times (43% of recruiters call it dishonest)
10. **Uniform bullet rhythm** — identical length and density across all bullets (subtle but cumulative)

Full details with prevention mechanisms: [`detection-signals.md`](detection-signals.md)

## The Research Behind It

Research conducted across 8+ sources including the TopResume AI in Hiring Survey (n=600), Resume Now's 2025 AI and the Applicant Report (n=925 HR professionals), and practitioner interviews with certified professional resume writers.

**Key findings:**

- **The evidence-bank gap is real.** Every competitor generates from job titles, not evidence. That is why their output is detectable.
- **"Increased revenue 40%" is now an AI tell** — but only without mechanism, context, or timeframe. "Grew enterprise pipeline from $2.1M to $2.9M over two quarters by restructuring outbound in Outreach.io" is believable. The difference: specificity of method.
- **The manager verification test.** The single best heuristic for resume quality: "If the recruiter called your old manager and asked if this is true, would your old manager laugh — or say 'yes, that's fair'?" Every bullet must pass this test.
- **Recruiters detect through pattern fatigue, not analysis.** They see the same phrases hundreds of times per week. Detection is recognition, not investigation.
- **ATS has evolved.** Modern ATS uses contextual understanding, not keyword counting. It penalizes stuffing and rewards keywords embedded in authentic achievement statements.
- **Perfection is now suspicious.** AI made "perfect" resumes trivially easy. Recruiters are now more attuned to authenticity signals than polish. Deliberate variation (mixed bullet lengths, occasional fragments, industry shorthand) reads as human.

Full research: [`docs/research/03-resume-rebuilder.md`](../docs/research/03-resume-rebuilder.md)

## Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Generation architecture | Evidence bank first, not one-pass | Every competitor does one-pass. Every detection signal traces to lack of real evidence. This is the entire differentiator. |
| Anti-detection logic | Baked into defaults, not exposed as controls | Avoids adversarial "cheating tool" frame. Hardcoded constraints on hallucinations, buzzwords, and structure. |
| Industry specificity | Generic pipeline with level-calibration | The evidence bank handles industry specificity naturally. Level-calibration (entry vs. senior language intensity) matters more than industry templates. |
| ATS vs. human readability | Human-first language, ATS-safe formatting | Modern ATS rewards contextual keyword usage. Single column, standard fonts, no tables as non-negotiable baseline. |
| Metric presentation | Mixed quantified + qualitative | Every-bullet-has-a-percentage is an AI tell. Humans don't measure everything. 50-70% quantification target. Manager verification test on every metric. |
| Interview depth | Tiered: fast pass to minimum, optional deepening | Minimum viable: 3 achievements/role (6-9 total). Ideal: 5-7/role (25-30 total). Protects against user dropout. |
| Cover letter | Optional second output from same bank | 83% of hiring managers read them. Same evidence base, different storytelling format. Never auto-generated. |

## Pairs With

| Skill | How It Connects |
|-------|----------------|
| **voice-extractor** | Load a voice profile so the resume matches the user's natural writing style instead of defaulting to resume-speak. |
| **ai-tell-killer** | Run on the generated resume as a final pass to catch any remaining AI fingerprint the built-in checks might miss. |
| **interview-coach** | The evidence bank feeds directly into interview prep. Same achievements, reframed for behavioral and situational questions. |
