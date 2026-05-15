# Interview Coach — Research Results

The strongest signal across this research: **interview prep tools fail not because the rubric is wrong, but because feedback is sycophantic.** Pramp pairs you with random peers who tell you "great answer." AI tools spit out generic praise and call it coaching. The two implementations that actually work — Noam Segal's Claude skill and Patrick McKenzie's salary essay — both share the same DNA: brutally specific, evidence-anchored feedback that names the gap and hands you the fix. Below: per-question findings, then design decisions, then the modes spec.

---

## Q1: Five-dimension scoring beats STAR adherence — and seniority-calibrated rubrics are the unlock

**Schmidt & Hunter (1998)** — and the 2016 update by Schmidt, Oh, and Shaffer — established the validity ceiling: structured interviews predict job performance at r = .51 vs. .38 for unstructured. Sackett's 2022 reanalysis goes further, suggesting structured interviews may now be the strongest single predictor of job performance, edging out cognitive ability tests. The mechanism is consistency: same questions, same rubric, same scoring across candidates. For a coaching skill, this maps to one rule: **score the answer, not the vibe.**

**Framework comparison — STAR vs. SOAR vs. CAR.** STAR (Situation, Task, Action, Result) is used by ~73% of employers and works well for entry-level. SOAR replaces "Task" with "Obstacle" — a small swap that transforms an answer from a job description into a problem-solving narrative. CAR (Challenge, Action, Result) trades depth for brevity and works in fast-paced rounds. The honest takeaway from practitioner data: **no framework outperforms when applied mechanically.** Candidates trained to recite STAR sound like they're reciting STAR. The win is using the framework as scaffolding the candidate then dismantles — answers should be structured but never feel structured.

**The noamseg/interview-coach-skill rubric.** Noam Segal's open-source Claude skill scores answers on five dimensions — Substance, Structure, Relevance, Credibility, Differentiation — calibrated to seniority. It's the most sophisticated public implementation I've seen, and the rubric maps cleanly to what hiring managers actually screen for:

- **Substance** (1-5): Evidence quality. Specific examples + metrics + impact. A "4 on Substance" for a mid-career candidate means quantified impact with alternatives considered. For an executive, it means business-level impact with P&L awareness.
- **Structure** (1-5): Narrative clarity. Clear arc, no rambling, follow-up-ready.
- **Relevance** (1-5): Did the answer address the actual question, or pivot to a rehearsed story?
- **Credibility** (1-5): Believable details. Specific names, specific tradeoffs, specific failures. Generic stories get marked down.
- **Differentiation** (1-5): Whether the answer reflects only this candidate's unique perspective. Generic answer any prepared candidate could give = 1. "Unmistakably this candidate — earned secrets + defensible stance" = 5.

The genius is the seniority calibration. A 3 on Substance for a 2-year analyst is a 1 for a director. The rubric scales to where the candidate actually sits, not to a one-size-fits-all bar.

**Mock interview design — timed vs. untimed.** Practitioner consensus: 15-30 focused technical reps + 2-4 realistic mock sessions under timed conditions. Time pressure changes answer quality measurably — candidates who only practice untimed lose their structure when the clock starts. Mock interviews should default to timed (60-90 sec for behavioral, 3-5 min for case-style), with an untimed "build the answer first" mode for candidates who haven't yet developed raw material. Follow-ups matter as much as the initial question — interviewers probe with "Tell me more about that" and "Why did you choose that approach?" to test whether the candidate has lived experience or rehearsed talking points. Mock interviews must simulate this. Silence is also a probe; the skill should sometimes deliberately not respond and let the candidate fill the gap.

**Sources:**
- [Schmidt & Hunter (1998) Meta-Analysis](https://home.ubalt.edu/tmitch/645/session%204/Schmidt%20&%20Oh%20validity%20and%20util%20100%20yrs%20of%20research%20Wk%20PPR%202016.pdf)
- [SIOP — rethinking cognitive ability as #1 predictor](https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance-new-research-says-its-time-to-think-again/)
- [STAR vs SOAR comparison — Interview Guys](https://blog.theinterviewguys.com/star-method-vs-soar-method/)
- [noamseg/interview-coach-skill on GitHub](https://github.com/noamseg/interview-coach-skill)
- [Noam Segal in Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-to-use-ai-in-your-next-job-interview)
- [Probing techniques in interviewing](https://library.fiveable.me/art-of-the-interview/unit-3/probing-follow-up-questions/study-guide/pl1Ko96D6g02mrkl)

**Confidence: High** on the rubric design (multiple converging implementations + 25 years of selection psychology). **Medium** on the timed/untimed split (practitioner data, not controlled trials).

---

## Q2: Salary negotiation has converged on a small set of high-value moves

Three sources dominate evidence-based negotiation: Patrick McKenzie's 2012 essay (responsible for ~$9M/year in measured comp uplift per his own tracking), Chris Voss's *Never Split the Difference* (FBI hostage techniques translated to comp talks), and the academic anchoring literature (Galinsky, Mussweiler, and successors).

**Patrick McKenzie's core principles** — the load-bearing ones, not the throat-clearing:

1. **Never give a number first.** "He who names a number first loses" because the number is either too high (eliminates you) or too low (caps your offer). Deflect: "I'd want to learn more about the role and team before discussing comp. What's the budget for this position?"
2. **Negotiate only after agreement-in-principle.** Don't negotiate during the screen. Negotiate after they've decided they want you and are figuring out what to offer.
3. **Understand fully-loaded employee cost.** Your salary is 50-100% on top of base when you factor in benefits, payroll tax, equity, and office overhead. A $10K raise is a rounding error to the company. Internalizing this kills the "I can't ask for that much" instinct.
4. **Reframe the conversation.** This is a professional business discussion, not a moral question. The person across from you negotiates compensation as part of their job. You should too.
5. **Engineers (and most candidates) treat being bad at negotiation as a virtue.** It costs them six figures over a career. The compounding math is brutal: a $15K starting salary delta, indexed to typical raise rates, becomes ~$200K-$400K in lifetime earnings.

**Chris Voss — tactical empathy moves that translate to comp talks:**

- **Mirroring**: Repeat the last 1-3 words of what they said with upward inflection. "$140K base?" Forces them to elaborate. Buys you time. Makes them feel heard.
- **Labeling**: Name the emotion. "It seems like you're trying to make this work within a tight band." Defuses tension. Often produces: "Well, actually we have some flexibility on..."
- **Calibrated questions**: Open-ended "how" and "what" questions that put the problem on them. The GOAT: **"How am I supposed to do that?"** Used after a low offer, this question is devastating. It forces the other side to either justify or improve. Other strong calibrated questions: "What about this offer reflects my experience?" / "How would you feel if I had to walk away because of comp?" / "What's your flexibility on the equity component?"
- **The accusations audit**: Front-load the objections. "You're probably going to think I'm asking for too much, and the timing is bad given your hiring freeze." Naming the resistance disarms it.

**Anchoring research — the academic foundation.** Galinsky & Mussweiler (2001) demonstrated through controlled experiments that the first-offer anchor moves the final price significantly in the offerer's direction. The mechanism is *selective accessibility*: once an anchor is on the table, both sides generate evidence consistent with it. This is why "what's your expected salary" is a trap — your number becomes the ceiling, not the floor.

**Important caveat from recent research** (Schweinsberg, ScienceDirect 2022): ambitious first offers do produce higher final outcomes BUT also increase impasse rate. The optimization isn't "ask for the moon" — it's "anchor high enough to capture upside, low enough to stay credible." The skill should help candidates calibrate the anchor against market data (Levels.fyi, Glassdoor, peer disclosures), not just push higher.

**Scenario scripts that need to exist:**

- *Recruiter screen — "what are your salary expectations?"*: Deflect to the company's range. "I'd want to learn more before naming a number. What's the band for this role?"
- *Counter on first offer*: "Thanks for the offer. I'm excited about the role. Based on the market data I've gathered for similar roles at companies like X and Y, I was targeting $[anchor 15-25% higher]. Is there room to move on base?"
- *Competing offer leverage* (real or potential): "I have another conversation moving forward at $[number]. I'd prefer to be here, but I need the comp to be in a similar range to make this work."
- *Equity vs. cash tradeoff*: Equity is real but illiquid and risky. Push to convert equity to base or sign-on when possible: "I appreciate the equity grant. Given the longer vesting horizon, I'd like to discuss whether some of that can shift to base or a sign-on bonus."
- *Remote work negotiation*: Frame around performance, not preference. Propose a 90-day pilot. Get it in writing.

**Sources:**
- [Patrick McKenzie — Salary Negotiation](https://www.kalzumeus.com/2012/01/23/salary-negotiation/)
- [Chris Voss — Never Split the Difference summary](https://nabilmurad.substack.com/p/never-split-the-difference-by-chris)
- [MasterClass — Calibrated Questions](https://www.masterclass.com/articles/how-to-use-calibrated-questions-to-negotiate-strategically)
- [PON Harvard — Anchoring research](https://www.pon.harvard.edu/daily/negotiation-skills-daily/what-is-anchoring-in-negotiation/)
- [Galinsky & Mussweiler — first offer effects](https://business.columbia.edu/sites/default/files-efs/pubfiles/11691/first_offers.pdf)
- [Interviewing.io — exact recruiter scripts](https://interviewing.io/blog/negotiate-salary-recruiter)
- [HBR — negotiating remote work](https://hbr.org/2021/07/how-to-negotiate-a-remote-work-arrangement)
- [Levels.fyi — comp data + negotiation guide](https://www.levels.fyi/blog/ultimate-negotiation-guide.html)

**Confidence: High** on the principles (converging evidence across 14 years of practitioner data, FBI training, and peer-reviewed anchoring research). **Medium-High** on specific scripts (best-practice consensus, not RCTs).

---

## Q3: JDs leak more than they disclose — pattern recognition matters more than keyword extraction

Job descriptions are negotiated documents. HR, the hiring manager, and sometimes legal each tug them in different directions. The result: stated requirements rarely match actual priorities. The skill should extract three layers:

**Layer 1: Stated requirements.** What's explicitly listed — years of experience, technologies, certifications, must-haves vs. nice-to-haves. This is the surface. Most candidates stop here.

**Layer 2: Implied priorities.** Pattern signals reveal what the team actually cares about:
- *Repeated themes across sections* = real priorities (e.g., "stakeholder management" appearing in responsibilities, requirements, and team description = the role is half-political)
- *First-paragraph keywords* carry more weight than middle-of-the-list ones
- *Verbs in responsibilities* signal seniority and scope ("execute" vs. "drive" vs. "own" vs. "shape")
- *Quantified expectations* ("manage a team of 5", "$2M budget") tell you the actual altitude
- *Tools named* signal the existing stack and where you'll fit

**Layer 3: Red flags.** The decoder ring for HR-speak:
- "Fast-paced" / "wear many hats" / "scrappy" → understaffed, expect overwork
- "We're a family" → boundaries problems
- "Reduce dependency on [senior leader]" → someone above you is over-involved (possibly toxic)
- "High autonomy" without "established processes" → no infrastructure, you'll be building from scratch
- "Resilience" / "thick skin" → hostile environment
- Salary range omitted in states where disclosure isn't required → likely lowballing
- Vague responsibilities ("various tasks as needed") → the role is a catch-all for low-priority work
- Requirements list is impossibly long → they don't know what they want, or they've combined two roles into one

**Question generation from JD.** The skill should auto-generate likely interview questions from the JD by mapping responsibilities to STAR prompts. Example: JD says "drive cross-functional alignment on roadmap." Likely question: "Tell me about a time you had to align stakeholders with conflicting priorities. What was the situation, what did you do, and what was the outcome?" Each major responsibility yields 1-3 likely questions. The skill should also flag *gap questions* — places where the candidate's experience doesn't match a JD requirement, with recommended bridging language.

**Sources:**
- [Welcome to the Jungle — JD red flags](https://www.welcometothejungle.com/en/articles/red-flags-in-a-job-description)
- [LinkedInOptimization — 7 things hidden in every JD](https://linkedinoptimization.substack.com/p/7-things-hidden-in-every-job-description)
- [Interview Guys — JD analyzer](https://blog.theinterviewguys.com/the-hidden-job-description-analyzer/)
- [Yardstick — behavioral question patterns](https://yardstick.team/interview-questions/pattern-recognition)

**Confidence: Medium-High.** Decoder rings are practitioner consensus, well-validated through years of recruiting blog content, but not subjected to controlled testing.

---

## Q4: The tool landscape — three approaches, one shared blind spot

The mock interview ecosystem clusters into three buckets:

**Peer practice (free, low-quality feedback):** Pramp pairs you with another candidate. You take turns interviewing each other. Free, unlimited. The feedback ceiling is the other candidate's interviewing skill — usually not great. Best for "interview stamina" reps before high-stakes loops.

**Expert practice (paid, high-quality feedback):** Interviewing.io pairs you with engineers from FAANG-tier companies. ~$225/session. Feedback is calibrated, anonymous, often brutal in the right way. The model works because the interviewers actually run interviews professionally. Best for polish before a real loop.

**AI mock platforms (paid subscription, generic feedback):** Big Interview, Revarta ($49/mo), MockIF, etc. Run you through question sets, transcribe your answer, generate feedback. The chronic failure mode: feedback is sycophantic ("Great structure! Try adding more specifics.") and lacks the brutal specificity that actually changes behavior. They optimize for retention, not for the candidate getting hired.

**Open-source Claude skills:** noamseg/interview-coach-skill (the gold standard, 5-dimension rubric, seniority-calibrated, decision-tree triage), kamalabdelwahed/claude_interview_coach, priyankonline/Claude-interview-coach-skill, dbhat93/job-search-os (comprehensive job-search-as-system). These solve the sycophancy problem because Claude can be instructed to refuse "great answer" and to anchor every score in evidence.

**The gap this skill fills:** A multi-mode skill that runs the *whole* loop — JD analysis → question generation → mock interview with rubric scoring → negotiation scripts — in one consistent voice, with anti-sycophantic feedback as the load-bearing design constraint. The noamseg skill is excellent but optimized for Claude Code power users running 20+ commands. This skill should work for someone who pastes their JD, gets meaningful prep, runs a mock, and walks out with their negotiation scripts ready — without needing to memorize 20 verbs.

**Sources:**
- [Pramp vs Interviewing.io comparison](https://www.lodely.com/blog/pramp-vs-interviewing-io)
- [Best AI Mock Interview Platforms 2026](https://www.revarta.com/blog/best-ai-mock-interview-platforms-2026)
- [Interview practice gap research — Interviewing.io](https://interviewing.io/blog/technical-interview-practice-gap)
- [Job Search OS skill](https://github.com/dbhat93/job-search-os)

**Confidence: Medium-High.** Tool comparisons are practitioner-sourced and current as of 2026.

---

## Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| One mega-mode vs. distinct modes | **Four distinct modes** (JD analysis, question generation, mock interview, negotiation) with explicit `mode:` declaration | Forces clarity. User knows which mode they're in. Skill knows which behaviors to load. Avoids the "Claude tries to do everything at once" failure pattern. |
| Rubric design | **Adopt noamseg's 5-dimension rubric** (Substance, Structure, Relevance, Credibility, Differentiation) with seniority calibration | Already validated, mature, and maps to what hiring managers screen for. Reinventing this would be vanity. Credit upstream. |
| Feedback format | **Anti-sycophantic by hard rule** — every score requires evidence + specific rewrite | "Great answer" is the field's universal failure mode. The skill should refuse to deliver praise without specifics. Sample format: "Substance 2/5 — you named no metrics. Rewrite: 'I led the migration that cut latency from 800ms to 120ms over six weeks.'" |
| Framework recommendation | **STAR as default, SOAR for senior+, CAR for fast rounds** — but never enforce mechanically | Frameworks are scaffolding, not scripts. Best answers structure underneath but feel conversational. The skill should flag when an answer sounds rehearsed. |
| Mock interview format | **Default timed (60-90s behavioral, 3-5 min case)** with untimed "build raw material" mode for candidates without stories | Time pressure surfaces real performance gaps. Untimed mode exists for the prep step before the mock. Always include 1-2 follow-up probes per question. |
| Negotiation philosophy | **Patio11 + Voss combined** — Patio11 for principles (never first, agreement-in-principle, fully-loaded cost), Voss for specific tactics (mirroring, labeling, calibrated questions) | These are the two most evidence-rich sources. They don't conflict; they layer. Patio11 is the strategy, Voss is the in-conversation moves. |
| Negotiation outputs | **Specific scripts for the 5 most common scenarios**, not general theory | "Here's a script for when the recruiter asks your salary expectation" beats "remember to anchor high." The skill should produce ready-to-use language calibrated to the user's actual situation. |

---

## Interview Coach Modes Spec

Four modes. The user declares one explicitly. Each mode has a single clear job.

### Mode 1: `jd-analysis` — Decode the job description

**Input:** Pasted JD + (optional) the user's resume or 2-3 sentences about their background.

**Output:**
- *Stated requirements* (what they wrote)
- *Implied priorities* (what the patterns reveal — repeated themes, verb altitude, tool stack signals)
- *Red flags* (specific phrases decoded — "fast-paced," "wears many hats," etc., with what each signals)
- *Skills match analysis* (where the user is strong, where the gaps are, suggested bridging language)
- *Likely interview question bank* (10-15 questions auto-generated from the JD's responsibilities, organized by likely round)

Connects to → `question-prep` (drill the generated questions) or `mock` (run a simulated round on them).

### Mode 2: `question-prep` — Build the storybank

**Input:** A specific question (or list of questions, often from `jd-analysis` output) + the user's experience.

**Output:**
- For each question: a recommended framework (STAR/SOAR/CAR based on question type and user's seniority)
- *Story scaffolding* — prompts to extract the raw material (Situation? Action? Specific metric? What went wrong? What would you do differently?)
- *Draft answer* in the user's actual voice, not generic
- *Likely follow-up probes* — the 2-3 questions an interviewer will fire next, with how to handle each
- *Anti-pattern flags* — places where the draft sounds rehearsed, generic, or evasive

Connects to → `mock` (drill the prepped answers under time pressure).

### Mode 3: `mock` — Simulated interview with rubric scoring

**Input:** A question (or set of questions) + the user's spoken/typed answer + their seniority level (early/mid/senior/exec).

**Output:**
- *Score on each of the 5 dimensions* (Substance, Structure, Relevance, Credibility, Differentiation), 1-5, calibrated to seniority
- *Specific evidence* for each score — not "your structure was weak" but "you gave the action before the situation, which lost me at the start"
- *2-3 follow-up probes* the candidate must respond to (mock continues for 1-2 rounds)
- *Specific rewrite* of the weakest dimension — show, don't tell
- *Aggregate diagnosis* — pattern across multiple questions ("Substance is your bottleneck across 4 of 5 answers — you tell stories without metrics")
- *Drill recommendation* — which mode/exercise to do next

Modes within mock:
- *Timed* (default): 60-90s for behavioral, 3-5 min for case
- *Untimed*: Build the answer, then run it timed
- *Round simulation*: Run 4-6 questions in sequence with no breaks, simulating a 45-min loop

Connects to → `negotiate` (when the user is past the loop and into offers) or back to `question-prep` (drill the weak areas).

### Mode 4: `negotiate` — Comp strategy + ready-to-use scripts

**Input:** The user's situation (recruiter screen / first offer / counter / competing offers / equity question / remote ask) + their target role and market data.

**Output:**
- *Diagnosis* — where they are in the negotiation arc, what leverage they have, what they don't
- *Specific scripts* for their scenario, in their voice, ready to send/say
- *Calibrated questions* to deploy at key moments (the "How am I supposed to do that?" family)
- *Anchor calibration* — what number to anchor at, based on market data and their leverage
- *Anti-pattern flags* — where they're about to give up leverage (e.g., naming a number too early, accepting a verbal offer without seeing it written)
- *Mirroring/labeling drills* — practice saying the awkward parts out loud

Sub-scenarios with dedicated scripts:
- *Recruiter screen — salary expectations question* → deflection scripts
- *First offer received* → counter language with anchor + justification
- *Competing offers* (real or potential) → leverage language without burning bridges
- *Equity vs. cash tradeoff* → conversion scripts, vesting questions
- *Remote work / flexibility* → 90-day pilot framing, document-everything checklist
- *Sign-on bonus / relocation / start date* → secondary lever scripts

Connects to → done. After `negotiate`, the user has what they need.

### Mode connectivity

The modes form a natural arc but the user can enter any mode standalone:

```
jd-analysis → question-prep → mock → negotiate
     ↓             ↓            ↓
     └─────────────┴────────────┘
        (drill cycle until ready)
```

The skill should ask "which mode?" if the user opens it without specifying, but should accept direct entry into any mode.
