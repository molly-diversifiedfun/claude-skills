# Interview Coach

**Interview prep without the sycophancy. Four modes: decode the JD, build the storybank, run a scored mock, and walk into the negotiation with scripts.**

## The Problem

Every other interview prep tool fails the same way: sycophantic feedback. Pramp pairs you with another candidate who tells you "great answer." AI mock platforms transcribe your response and reply "Strong structure! Try adding more specifics." Both miss the point. Generic praise doesn't change behavior — and "add more specifics" without showing what specifics is a non-instruction.

Patrick McKenzie's 2012 essay on salary negotiation is responsible for ~$9M/year in measured comp uplift. The advice has been public for 14 years. Most candidates still don't apply it because the moment of negotiation is high-stakes, low-rep, and emotionally loaded — and they have no script in the moment.

This skill exists to do what other tools won't: tell you Substance was 2/5 because you named no metrics, then hand you a rewrite using your actual experience. Then drill it again. Then prep your negotiation language so you walk into the offer call with paste-ready scripts.

## What It Does

Four modes. Declare the one you want, and the skill runs that loop:

1. **`jd-analysis`** — Paste a job description. Get back: stated requirements, implied priorities (what the patterns reveal), red flags (decoded HR-speak), skills match, and a likely interview question bank organized by round.
2. **`question-prep`** — Pick a question (often from the bank above). Get back: framework recommendation (STAR/SOAR/CAR), story scaffolding prompts, draft answer in your voice, likely follow-up probes, and anti-pattern flags.
3. **`mock`** — Run a simulated interview. Each answer scored 1-5 on five dimensions (Substance, Structure, Relevance, Credibility, Differentiation), calibrated to your seniority. Every score has specific evidence. Every weakness comes with a rewrite.
4. **`negotiate`** — Tell the skill where you are in the offer arc. Get back: diagnosis, anchor recommendation grounded in your market data, paste-ready scripts for the five common scenarios, and the calibrated questions to deploy in conversation.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Paste the contents of `SKILL.md` as your first message — or add the skill to a Claude Project
3. Tell Claude which mode you want: "Run `jd-analysis`" or "I have an offer, I need `negotiate` mode"
4. Follow the skill's prompts

### In Claude Code

1. Drop `SKILL.md` into `~/.claude/skills/interview-coach/SKILL.md`
2. Tell Claude Code: "Use the interview-coach skill — `mock` mode, mid-career"
3. The skill takes over

### Tips for Better Results

- **Bring real material.** The skill is only as good as what you feed it. Generic stories produce generic feedback. Bring specific projects, real metrics, actual conflicts.
- **Declare your seniority.** `mock` mode requires it. A 4 on Substance for a 2-year analyst is a 1 for a director.
- **Run `jd-analysis` first.** The question bank it generates is what you should drill in `question-prep` and `mock`.
- **Bring market data to `negotiate`.** Levels.fyi, Glassdoor, peer disclosures (Blind, Reddit). Without data, you're guessing the anchor. The skill will push you to gather it.
- **Don't ask for praise.** The skill will refuse. That's the design.

## What You Get

### From `jd-analysis`

A 600-1,200 word decoded brief with five sections (Stated Requirements, Implied Priorities, Red Flags, Skills Match, Likely Question Bank). The question bank has 10-15 questions organized by likely round (recruiter screen, hiring manager, cross-functional, leadership). Each question is tagged to the JD requirement it tests.

### From `question-prep`

For each question: framework recommendation, 4-6 story scaffolding prompts (you fill in the raw material), a 150-250 word draft answer in your voice, 2-3 likely follow-up probes with how to handle each, and anti-pattern flags.

### From `mock`

For each answer:
```
SCORES (calibrated to mid):
- Substance:     2/5
- Structure:     4/5
- Relevance:     3/5
- Credibility:   3/5
- Differentiation: 2/5

EVIDENCE:
- Substance: You spent 90 seconds on the situation and 10 on the result. No metric. No team size.
- Structure: Clear arc, follow-up-ready.
- Relevance: You answered an adjacent question (project leadership) instead of the actual one (handling conflict).
- ...

WEAKEST DIMENSION REWRITE:
Try this using your actual experience: "When the design lead and the eng lead disagreed on the
checkout flow, I ran a 30-minute alignment session, framed the tradeoff as 'ship in 2 weeks
with the simpler flow vs. ship in 5 with the redesign,' and the team chose ship-fast. Conversion
held at 4.2% post-launch. Six months later we shipped the redesign and lifted to 5.1%."

FOLLOW-UP PROBES:
1. What did you do when the design lead pushed back on the framing?
2. How did you measure whether the simpler flow was actually working?
3. Looking back, would you have run the alignment session differently?
```

After 3+ questions: aggregate diagnosis ("Substance is your bottleneck across 4 of 5 answers — you tell stories without metrics") and a drill recommendation.

### From `negotiate`

Diagnosis of where you are in the arc, anchor recommendation with reasoning, 2-4 paste-ready scripts calibrated to your scenario, the calibrated questions to deploy in conversation, and anti-pattern flags specific to your situation. Scripts cover: recruiter screen deflection, first-offer counter, competing offers (real or potential), equity-vs-cash conversion, remote work negotiation, and the Voss "How am I supposed to do that?" deployment.

## The Anti-Sycophancy Rule

The single most important rule in the skill, and the one that separates it from every other tool:

> "Great answer" is banned. Every score requires evidence. Every critique requires a rewrite using the candidate's actual material.

If you nail an answer, the skill will say so — and tell you exactly what made it land. If you bombed, it'll say so — and hand you the rewrite. Either way, you walk out knowing what changed and why.

## The Research Behind It

Five findings shaped the design:

**Structured interviews predict performance at r = .51** (Schmidt & Hunter, 1998; Sackett et al., 2022 update). Same questions, same rubric, same scoring across candidates — that's what makes the predictive power real. The skill mirrors the structure: rubric-based scoring, not vibes.

**The noamseg/interview-coach-skill 5-dimension rubric (Substance, Structure, Relevance, Credibility, Differentiation) is the most validated open-source rubric for this work.** It maps cleanly to what hiring managers actually screen for and scales by seniority. This skill adopts it, with credit upstream.

**Patrick McKenzie's salary negotiation principles produce measured comp uplift in the millions** (per his own tracking from 14 years of reader correspondence). The five load-bearing principles — never name a number first, negotiate after agreement-in-principle, understand fully-loaded employee cost, reframe as a business discussion, get it in writing — are non-negotiable in this skill's `negotiate` mode.

**Chris Voss's tactical empathy moves (mirroring, labeling, calibrated questions) translate cleanly to comp talks.** The "How am I supposed to do that?" calibrated question is devastating after a low offer. The skill teaches the move and drills the delivery.

**Anchoring research (Galinsky & Mussweiler, 2001) shows the first-offer anchor moves the final settlement significantly toward the offerer.** But ambitious anchors increase impasse rate (Schweinsberg et al., 2022). The skill calibrates anchors against market data, not just "ask for more."

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| One mega-mode vs. distinct modes | Four explicit modes — `jd-analysis`, `question-prep`, `mock`, `negotiate` | Forces clarity. User and skill both know which behaviors to load. Avoids the "Claude tries everything at once" failure pattern. |
| Rubric design | Adopt noamseg's 5-dimension rubric with seniority calibration | Already validated, mature, and mapped to what hiring managers screen for. Reinventing it would be vanity. |
| Feedback format | Anti-sycophantic by hard rule — no "great answer" allowed; every score requires evidence + rewrite | The universal failure mode of every other tool. The skill refuses to deliver praise without specifics. |
| Framework recommendation | STAR default, SOAR for senior+, CAR for fast rounds — never enforced mechanically | Frameworks are scaffolding. Best answers structure underneath but feel conversational. The skill flags rehearsed-sounding answers. |
| Mock format | Default timed (60-90s behavioral, 3-5 min case) with untimed "build raw material" mode | Time pressure surfaces real performance gaps. Always include 1-2 follow-up probes per question to test depth vs. rehearsed lines. |
| Negotiation philosophy | Patio11 + Voss combined — McKenzie for principles, Voss for in-conversation tactics | Two most evidence-rich sources. They layer cleanly: McKenzie is strategy, Voss is the moves. |
| Negotiation outputs | Specific paste-ready scripts for five common scenarios, not general theory | "Here's the language" beats "remember to anchor high." The skill produces ready-to-use scripts calibrated to the user's situation. |

## Pairs With

- **[voice-extractor](/voice-extractor/)** — Extract your voice profile first, then `negotiate` mode produces scripts that sound like you, not generic
- **[resume-rebuilder](/resume-rebuilder/)** — Rebuild your resume to surface the experience inventory; this skill drills it under interview pressure
- **[decision-maker](/decision-maker/)** — When you have multiple offers and need to choose, hand the comparison to decision-maker
- **[devils-advocate](/devils-advocate/)** — Stress-test your answers before the real interview by having an adversarial agent attack them

## Credits

The 5-dimension rubric (Substance, Structure, Relevance, Credibility, Differentiation) and the seniority calibration design pattern were pioneered by [Noam Segal's interview-coach-skill](https://github.com/noamseg/interview-coach-skill) and [his Lenny's Newsletter writeup](https://www.lennysnewsletter.com/p/how-to-use-ai-in-your-next-job-interview). This skill adopts the rubric and adds JD analysis, question prep with story scaffolding, and a dedicated negotiation mode built on Patrick McKenzie and Chris Voss.
