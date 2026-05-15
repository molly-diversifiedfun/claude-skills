# PRD: interview-coach

## Problem

Interview prep tools fail in the same way: sycophantic feedback. Pramp pairs you with another candidate who tells you "great answer." AI mock interview platforms transcribe your response and respond with "Strong structure! Try adding more specifics." Both miss the entire point. Specific, evidence-anchored feedback is what changes behavior — and almost no tool delivers it.

Meanwhile, candidates leave money on the table at offer time. Patrick McKenzie's 2012 essay on salary negotiation is responsible for ~$9M/year in measured comp uplift, by his own tracking. The advice has been public for 14 years. Most candidates still don't apply it because the moment of negotiation is high-stakes, low-rep, and emotionally loaded — and they have no script.

The gap: a single skill that runs the full interview loop — JD decode, question prep with real story scaffolding, mock interviews with actual rubric scoring (not "good job"), and ready-to-use negotiation scripts — anchored in research, hostile to flattery, and calibrated to the candidate's actual seniority.

## Solution

A multi-mode skill: `jd-analysis`, `question-prep`, `mock`, `negotiate`. The user declares which mode they're in. Each mode does one thing well.

The load-bearing design constraint: **anti-sycophantic by hard rule.** The skill cannot say "great answer." Every score must be anchored to specific evidence. Every weakness must come with a specific rewrite using the candidate's actual experience.

Mock interview scoring uses the noamseg 5-dimension rubric (Substance, Structure, Relevance, Credibility, Differentiation), seniority-calibrated. Negotiation combines Patrick McKenzie's strategy with Chris Voss's tactical moves, with specific scripts for the five most common scenarios.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| One mega-mode vs. distinct modes | **Four explicit modes** with declared entry: `jd-analysis`, `question-prep`, `mock`, `negotiate` | Forces clarity. User and skill both know which behaviors to load. Avoids the "Claude tries to do everything at once" failure pattern that plagues general interview tools. |
| Rubric design | **Adopt noamseg/interview-coach-skill's 5-dimension rubric** with seniority calibration | Already validated and mature. Reinventing it would be vanity. Substance/Structure/Relevance/Credibility/Differentiation maps to what hiring managers actually screen for (Schmidt-Hunter structured-interview validity research). |
| Feedback format | **Anti-sycophantic by hard rule** — no "great answer" allowed; every score requires evidence + a specific rewrite | The universal failure mode of every other tool. Sycophancy feels good and changes nothing. The skill should refuse to deliver praise without specifics. |
| Framework recommendation | **STAR as default, SOAR for senior+, CAR for fast rounds** — but never enforced mechanically | Frameworks are scaffolding, not scripts. Best answers structure underneath but feel conversational. The skill flags when an answer sounds rehearsed. |
| Mock interview format | **Default timed** (60-90s behavioral, 3-5 min case) with untimed "build raw material" mode | Time pressure surfaces real performance gaps. Untimed mode exists for the prep step. Always include 1-2 follow-up probes per question to test depth vs. rehearsed lines. |
| Negotiation philosophy | **Patio11 + Voss combined** — McKenzie for principles (never first, agreement-in-principle, fully-loaded cost), Voss for tactics (mirroring, labeling, calibrated questions) | Two most evidence-rich sources. They layer cleanly: McKenzie is strategy, Voss is the in-conversation moves. |
| Negotiation outputs | **Specific scripts for five common scenarios**, not general theory | "Here's a script for the recruiter screen" beats "remember to anchor high." The skill produces ready-to-use language calibrated to the user's situation. |

## Target User

- Mid-career to senior IC or manager preparing for an interview loop where the comp will matter (~$120K+ total)
- Has 1-2 weeks of prep time, not 1-2 days
- Has interviewed before but never got feedback this specific
- Will use the negotiation mode whether or not they use the prep modes
- Reads Lenny's Newsletter, Patrick McKenzie, Lattice/Lenny-style writing — appreciates direct, evidence-anchored advice over inspirational LinkedIn-speak

Secondary user: early-career candidate (0-3 years) preparing for their second or third "real" interview loop. The seniority calibration matters here — their bar is different from a director's, and the skill respects that.

## Interaction Model

### Mode declaration (Phase 0, every session)

The skill opens by asking which mode the user wants. If the user describes a situation that maps to a mode, the skill names it explicitly: "Sounds like you're in `negotiate` mode — you have an offer in hand. Confirm?" Once declared, all behavior is scoped to that mode.

### Mode 1: `jd-analysis` — Decode the JD (10 min)

**Input:** Pasted JD + 2-3 sentences of context (user's role, target seniority, optionally their resume).

**Skill behavior:**
1. Parse the JD into stated requirements, implied priorities, and red flags
2. Run the decoder ring on common HR-speak phrases
3. Generate a likely interview question bank organized by round (recruiter screen / hiring manager / cross-functional / leadership)
4. Flag skill match strengths and gaps; suggest bridging language for gaps

**Output:**
- *Stated Requirements* — bullet list, what they wrote
- *Implied Priorities* — what the patterns reveal (repeated themes, verb altitude, tools named, missing topics)
- *Red Flags* — specific phrases decoded with what each typically signals
- *Skills Match* — strengths, gaps, suggested bridging language
- *Likely Question Bank* — 10-15 questions organized by round, with priority ranking

**Anti-pattern:** Don't restate the JD. Don't say "this looks like a great opportunity." Decode it.

### Mode 2: `question-prep` — Build the storybank (15-30 min)

**Input:** A specific question (or list, often from `jd-analysis`) + the user's experience.

**Skill behavior:**
1. For each question, recommend a framework (STAR/SOAR/CAR) based on question type and user's seniority
2. Walk the user through story scaffolding via targeted prompts: Situation? Action? Specific metric? What went wrong? What would you do differently?
3. Draft an answer in the user's voice, not generic
4. Anticipate 2-3 likely follow-up probes and how to handle each
5. Flag anti-patterns: rehearsed-sounding lines, generic framing, places where the answer dodges

**Output:**
- For each question: framework recommendation + scaffold prompts + draft answer + likely follow-ups + anti-pattern flags

**Anti-pattern:** Don't write the answer for the user. Walk them through extracting their own raw material first, then draft.

### Mode 3: `mock` — Simulated interview with rubric scoring (30-60 min)

**Input:** A question (or set of questions) + the user's seniority level (early/mid/senior/exec) + their answer (typed or pasted from voice transcription).

**Skill behavior:**
1. Score each answer on the 5-dimension rubric, calibrated to seniority:
   - **Substance** (1-5): Evidence quality. Specific examples, metrics, impact.
   - **Structure** (1-5): Narrative clarity. Clear arc, no rambling.
   - **Relevance** (1-5): Did they answer the actual question, or pivot to a rehearsed story?
   - **Credibility** (1-5): Believable details. Specific names, tradeoffs, failures.
   - **Differentiation** (1-5): Reflects only this candidate's unique perspective vs. generic.
2. For each score, provide specific evidence — not "your structure was weak" but "you led with the action before the situation, which lost me for the first 20 seconds"
3. Fire 2-3 follow-up probes; mock continues for 1-2 rounds
4. Provide a specific rewrite of the weakest dimension, using the candidate's own experience
5. After 3+ questions, diagnose the pattern: "Substance is your bottleneck — you tell stories without metrics in 4 of 5 answers"
6. Recommend the next drill

**Sub-modes within mock:**
- *Timed* (default): 60-90s for behavioral, 3-5 min for case-style
- *Untimed*: Build the answer, then re-run it timed
- *Round simulation*: 4-6 questions in sequence, no breaks, simulating a 45-min loop

**Output per question:**
- Score table (5 dimensions, 1-5, calibrated to seniority)
- Specific evidence for each score
- 2-3 follow-up probes
- Specific rewrite of weakest dimension

**Output after round:**
- Aggregate diagnosis (pattern across questions)
- Drill recommendation (which mode/exercise to do next)

**Anti-pattern:** Never use "great," "good job," "nice answer," or any praise without an anchor. If the user nailed it, name what specifically — "Substance 5/5 — you named the team, the metric, the tradeoff, and the alternative path you considered."

### Mode 4: `negotiate` — Comp strategy + ready-to-use scripts (15-45 min)

**Input:** User's situation (recruiter screen / first offer / counter / competing offers / equity / remote ask) + target role + market data they've gathered (or skill helps them find it).

**Skill behavior:**
1. Diagnose where they are in the negotiation arc and what leverage they actually have
2. Produce specific scripts for their scenario, in their voice, ready to send or say
3. Provide calibrated questions to deploy at key moments
4. Calibrate the anchor (what number, based on market data + their leverage)
5. Flag where they're about to give up leverage (e.g., naming a number too early, accepting a verbal offer without it in writing)
6. Drill the awkward parts — mirroring, labeling, the "How am I supposed to do that?" delivery

**Sub-scenarios with dedicated scripts:**
- Recruiter screen — salary expectations question (deflection)
- First offer received (counter with anchor + justification)
- Competing offers, real or potential (leverage without burning bridges)
- Equity vs. cash tradeoff (conversion scripts, vesting questions)
- Remote work / flexibility (90-day pilot framing, document-everything checklist)
- Sign-on bonus / relocation / start date (secondary levers)

**Output:**
- Diagnosis (1-2 paragraphs on situation, leverage, risks)
- Anchor recommendation with reasoning
- 2-4 specific scripts (paste-ready)
- Calibrated questions to use in conversation
- Anti-pattern flags
- One follow-up question for the skill to refine the scripts

**Anti-pattern:** Don't give general theory ("remember to anchor high"). Produce specific language.

## Anti-Patterns to Avoid in Implementation

- **Never say "great answer," "good job," "nice work," or any sycophantic praise.** This is the load-bearing rule. If the answer was strong, name what specifically — Substance 5/5 with evidence.
- **Never deliver a score without specific evidence.** "Substance: 2" is not feedback. "Substance: 2 — you named no metrics in a 90-second answer about leading a team migration" is feedback.
- **Never deliver a critique without a rewrite.** "Add more specifics" is the failure mode of every other tool. The skill must produce: "Try this instead: 'Over six weeks, I migrated 12 services from REST to gRPC, cutting p99 latency from 800ms to 120ms.'"
- **Never enforce a framework mechanically.** STAR is scaffolding, not a script. Best answers feel conversational and have structure underneath. Flag rehearsed-sounding answers.
- **Never use "47" or any specific filler number as the example metric.** Use varied, plausible numbers.
- **Never write the candidate's stories for them.** Walk them through extracting their own raw material via prompts; then draft.
- **Never skip seniority calibration.** A 4 on Substance for an early-career candidate is a 2 for an executive. The bar shifts.
- **Never give negotiation theory when scripts are needed.** "Here's the language to use" beats "remember the principles."
- **Never recommend a specific anchor number without grounding it in market data.** If the user hasn't gathered comp data, push them to Levels.fyi / Glassdoor / peer disclosures first.
- **Never let the skill be useful for cheating.** This skill is for prep, not for live interview assistance. If a user asks for help during a live interview, decline.

## Output Specs

### `jd-analysis` mode
- Word count: 600-1,200 words
- Sections: Stated Requirements, Implied Priorities, Red Flags, Skills Match, Likely Question Bank
- Markdown formatted
- Question bank has minimum 10 questions, organized by round, with priority

### `question-prep` mode
- Per question: framework recommendation, 4-6 scaffold prompts, draft answer (150-250 words), 2-3 follow-up probes, anti-pattern flags
- User can request multiple questions in one session

### `mock` mode
- Per answer: 5-dimension score table, evidence per dimension, 2-3 follow-up probes, specific rewrite of weakest dimension
- Per round (3+ questions): aggregate diagnosis paragraph + drill recommendation
- Scoring strictly 1-5 integers, calibrated to declared seniority

### `negotiate` mode
- Diagnosis: 1-2 paragraphs
- Scripts: 2-4 paste-ready, voice-matched if voice profile available
- Anchor calibration with reasoning
- One follow-up question to refine

## Success Criteria

- User completes a mock interview round and can name their #1 weakness with evidence
- User can paste a script from `negotiate` mode directly into an email or use it verbatim in a conversation
- User reports the feedback was specific enough to change behavior on the next attempt
- Skill never produces "great answer" or equivalent sycophancy across 100 mock answers
- Negotiation scripts produce measurable comp uplift (anecdotal tracking, not RCT)

## What This Skill Does NOT Do

- Real-time assistance during a live interview (this is for prep only)
- Technical interview practice (LeetCode-style coding) — out of scope; use Pramp or Interviewing.io
- Resume writing — use `resume-rebuilder`
- Cover letter drafting — use copywriting skills
- Career coaching ("should I take this offer?") — use `decision-maker`
- Interviewer-side training (preparing to interview candidates) — different skill, different rubric

## Technical Notes

- Pure prompt-based; no tools required
- Works in Claude.ai (paste SKILL.md or add to a Project) and Claude Code (drop into `~/.claude/skills/`)
- Pairs naturally with `voice-extractor` (so negotiation scripts sound like the user, not generic)
- Pairs with `resume-rebuilder` (resume-rebuilder produces the experience inventory; this skill drills it under interview pressure)
- Pairs with `decision-maker` (when the user has multiple offers and needs to choose)
