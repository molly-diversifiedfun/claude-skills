---
name: resume-rebuilder
description: Build resumes from real evidence, not templates. Use when a user wants to create, improve, or tailor a resume — mentions job hunting, resume help, applying for roles, updating their CV, or writing a cover letter. Phase 1 extracts an evidence bank through structured interview (achievements, metrics, tools, context). Phase 2 generates a tailored resume from that bank. The output passes recruiter scrutiny because every claim traces to real experience. Also generates cover letters from the same evidence bank. Trigger on phrases like "help me with my resume," "I need to update my resume," "write me a cover letter," "I'm applying for a job," "tailor my resume for this role," or any request involving job application documents.
---

# Resume Rebuilder

## What This Skill Does

Builds resumes from an evidence bank of real achievements — not from templates, not from job descriptions, not from thin air. Phase 1 extracts your actual accomplishments through a structured interview. Phase 2 generates a resume tailored to a target role using only what you told it. Optional Phase 3 produces a cover letter from the same bank.

The output reads as human-written because it IS human experience, structured and presented well. No competing tool does evidence extraction before generation. That is the entire differentiator.

## How It Works

Three phases, one conversation. Total time: 20-30 minutes.

1. **Evidence Bank Extraction** — Structured interview pulls real achievements with metrics, tools, and context
2. **Resume Generation** — Produces a tailored resume from the evidence bank, matched to target JD
3. **Review + Tailoring** — User verifies accuracy, adjusts emphasis, optionally requests a cover letter

---

## Phase 1: Evidence Bank Extraction (10-20 min)

Reference: `evidence-extraction-questions.md` for the full question bank.

### Conduct the Interview

Ask questions one at a time. Wait for the user's answer before continuing. Never batch questions.

**Step 1: Basic context (2 questions)**

1. Ask for the target role. Request the job description if they have one.
2. Ask for work history — most recent first. Job title, company, duration, one sentence on what they did.

**Step 2: Achievement extraction per role (3-5 questions per role)**

For each role, starting with the most recent:

1. Ask what they're proudest of. Follow up with the "So What?" cascade — push for business impact and numbers.
2. Ask what they built, fixed, or changed that someone else would notice. Apply the six questions: Who? How many? How often? How long? What tools? What examples?
3. Ask what their manager would say was their biggest contribution.
4. If the user says "I don't have metrics" — do NOT accept this. Use the metric recovery questions from `evidence-extraction-questions.md`. Everyone has metrics; most people just haven't framed their work that way.
5. If time allows and the user is engaged, ask about level-breaking achievements.

**Handling resistance:**
- If answers are vague, ask for a specific example. "Can you walk me through one time that happened?"
- If they minimize their work, reframe: "You said you 'just' did X — but that sounds like [restate with appropriate scale]. Is that accurate?"
- If a role genuinely has no quantifiable achievements, use the four alternative categories: innovation/change, influence/strategy, recognition, relationships.

**Minimum viable bank:** 3 achievements per role, 2-3 roles = 6-9 achievements.
**Ideal bank:** 5-7 per role = 25-30 achievements.

After reaching minimum viable, ask: "We have enough for a solid resume. Want to go deeper on any role, or should I generate?"

### Step 3: Store the Evidence Bank

After extraction, produce the evidence bank as a structured artifact. Format:

```markdown
# Evidence Bank — [User Name]
Generated: [Date]
Target Role: [Role title]

## [Company Name] — [Title] ([Dates])

### Achievement 1
- **What:** [Description]
- **Impact:** [Business outcome]
- **Metrics:** [Numbers, if available]
- **Tools/Tech:** [Specific tools used]
- **Context:** [Team size, scope, stakeholders]
- **Source quote:** [User's exact words that anchor this]

### Achievement 2
...

## [Next Company]
...
```

Tell the user: "This is your evidence bank. Save it — you can reuse it to generate resumes for different roles without repeating the interview."

---

## Phase 2: Resume Generation

Input: Evidence bank + target job description (if provided).

### Content Rules (Hardcoded — Not Configurable)

**Never invent.** Every claim must trace to a specific evidence bank entry. If the bank doesn't contain it, the resume doesn't claim it. No exceptions.

**Never use banned phrases.** Reference: `banned-phrases.md`. This list is a hard filter, not a suggestion.

**Embed keywords authentically.** Map JD requirements to evidence bank entries. Paraphrase — never copy JD language verbatim. Use each keyword 1-2 times in context. Never create keyword sections or skill dumps.

**Calibrate language to career level.**
- Entry-level (0-3 years): Straightforward verbs, concrete tasks, learning signals. No "architected" or "drove strategy."
- Mid-career (3-8 years): Moderate scope language, ownership signals, cross-functional work.
- Senior (8-15 years): Leadership language, business impact, strategic framing — but only for things they actually led.
- Executive (15+ years): Organizational impact, P&L language, transformation scope — backed by real evidence only.

**Apply the manager verification test.** For every bullet: would their former manager confirm this is a fair characterization? If not, soften or remove.

**Include mechanism with every metric.** Wrong: "Increased revenue 40%." Right: "Grew enterprise pipeline from $2.1M to $2.9M over two quarters by restructuring outbound in Outreach.io." The mechanism (how), the timeframe (when), and the tool (where) make metrics believable.

**Mix quantified and qualitative bullets.** Not every bullet needs a number. Humans don't measure everything. A resume where every bullet has a percentage is an AI tell. Aim for 50-70% of bullets with some form of quantification.

### Structural Rules (Hardcoded)

**Vary bullet length.** Mix one-line and two-line bullets within the same role section. Never produce 5 bullets of identical length.

**Vary sentence openings.** Use RAC (Result-Action-Context) as the default but not the only pattern:
- Some bullets lead with the result: "Cut deployment time from 4 hours to 20 minutes by..."
- Some lead with context: "During the Series B push, built..."
- Some lead with action: "Redesigned the onboarding flow, which..."
- No more than 2 consecutive bullets starting with the same word class (e.g., two verbs in a row is fine; three is not).

**Vary grammatical structure.** Mix fragments and complete sentences. Occasionally use passive voice. Use different clause patterns across bullets.

**Use RAC for bullet format.** Front-load the outcome, then method. This matches how recruiters scan — result first, mechanism second.

### Format Rules (Hardcoded)

**Reverse chronological only.** Functional resumes are viewed with suspicion by recruiters.

**Length by experience:**
- 0-5 years: 1 page, firm
- 5-10 years: 1-2 pages (prefer 1 if the content fits)
- 10+ years: 2 pages
- Never 1.25 pages. Commit to 1 or 2.

**ATS-safe baseline.** Single column. Standard fonts. No tables or graphics. No columns or text boxes. No headers/footers (ATS often can't read them).

**Sections in order:**
1. Name + contact info (email, phone, LinkedIn, location — city/state only)
2. Professional summary (2-3 sentences, optional — skip if it would be generic)
3. Experience (reverse chronological)
4. Skills (brief, grouped by category, only skills from the evidence bank)
5. Education
6. Certifications (only real ones from the evidence bank)

**Output as plain text or markdown.** The user formats in their tool of choice. Do not attempt visual design.

### Anti-Detection Check

Reference: `detection-signals.md` for all ten signals.

Before delivering the resume, silently verify:
- No banned phrases present
- No content that isn't in the evidence bank
- Bullet lengths vary within each section
- Sentence openings vary (no 3+ consecutive same-pattern starts)
- Keywords appear in context, not stuffed
- Language intensity matches career level
- Every metric includes mechanism

Do not narrate this check to the user. Just do it.

---

## Phase 3: Review + Tailoring

Present the generated resume and ask:

1. "Anything here that isn't true or that you'd phrase differently?"
2. If they provided a JD: "Want me to adjust emphasis for this role? I'll re-rank from your evidence bank — no new content, just different prioritization."
3. "I can also generate a tailored cover letter from your evidence bank. Want one?"

Make requested changes. Re-run the anti-detection check after edits.

### Tailoring for a Different Role

If the user wants to target a new JD with the same evidence bank:
- Re-map evidence bank entries to the new JD's requirements
- Re-rank achievements by relevance to the new role
- Adjust professional summary (if present) to speak to the new role
- Swap or reorder bullets — do NOT invent new ones
- Deliver as a new resume, not a diff

---

## Cover Letter Generation (If Requested)

Uses the evidence bank. Never invents beyond it.

### Structure

1. **Opening:** Why THIS company or role specifically. Requires user input or JD context — ask if you don't have it. Never use "I am writing to express my interest in" or any template opener.
2. **Body (1-2 paragraphs):** Tell 1-2 specific achievement stories from the bank that connect to the role's core needs. Use different achievements than the resume's top bullets when possible — the bank should be large enough to support this.
3. **Connection:** Explain the bridge between past work and target role. Be specific — name the skills, the context, the overlap.
4. **Close:** Concrete next step. Not "I look forward to hearing from you" — something specific like "I'd welcome 20 minutes to discuss how [specific experience] applies to [specific challenge from JD]."

### Cover Letter Rules

- Match the voice register of the resume. If the resume is direct and technical, the cover letter should be too.
- Under one page. 3-4 paragraphs maximum.
- Never repeat the resume. The cover letter tells stories; the resume lists facts.
- Apply the same banned phrase list.
- Apply the same anti-detection check.

---

## Returning Users

If the user already has an evidence bank from a previous session:
- Skip Phase 1 entirely
- Ask: "Want to add any new achievements, or should I generate from your existing bank?"
- Proceed to Phase 2 with the existing bank + new JD

If the user has a resume they want to improve (not starting from scratch):
- Still do Phase 1 — use their existing resume as a starting point for the interview, but extract deeper
- "I see you have [X] on your resume. Tell me more — what specifically did you do there?"
- Build the evidence bank from their answers, not from their existing resume text

---

## Rules

- **Never invent.** If the evidence bank doesn't contain it, the resume doesn't claim it. This is the single most important rule. Violating it produces the highest-severity AI detection signal (hallucinated credentials) and can end careers.
- **Never skip the interview.** Even if the user says "just write me a resume for a PM role" — the evidence bank is mandatory. Explain why: "I need your real achievements to build something that doesn't read like every other AI resume. It takes 10-15 minutes and the result is dramatically better."
- **Never use banned phrases.** See `banned-phrases.md`. Hard filter, not suggestion.
- **Never produce uniform structure.** Varied bullet length, varied openings, varied grammar. This is a non-negotiable generation constraint.
- **Always apply the manager verification test.** Every bullet, every metric. Would their old manager say "yes, that's fair"?
- **Always produce the evidence bank as a reusable artifact.** The user should be able to save it and return later for new roles.
- **Always ask before generating a cover letter.** Don't auto-produce one.
- **Treat the evidence bank as the single source of truth.** Tailoring for a new role means re-ranking and re-selecting from the bank, never adding new claims.

## What This Skill Does NOT Do

- Write resumes without real input ("generate a resume for a project manager" — needs YOUR evidence)
- Guarantee ATS scores (ATS optimization is table-stakes formatting, not the focus)
- Design visual resume layouts (text output — user formats in their tool)
- Prepare for interviews (interview prep is a separate workflow that can consume the evidence bank)
- Write LinkedIn profiles (different format, different constraints)

## Pairs With

- **voice-extractor**: Load voice profile to match the user's natural writing style
- **ai-tell-killer**: Final pass on generated resume to catch remaining AI fingerprint
- **interview-coach**: Evidence bank feeds directly into interview prep — same achievements, different format
