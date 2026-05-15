---
name: career-experiment
description: Design 3 low-stakes, time-bounded career experiments instead of giving career advice. Activate when the user is weighing a career change, asking "should I switch to X," considering a pivot to PM/management/founder/freelance/new field, feeling stuck between options, or saying things like "I'm thinking about leaving," "I don't know if I'd like X," "how do I test whether," "career pivot," "career change," "should I quit," or "how do I know if I'd be good at." Output is always 3 testable experiments with hypotheses, actions, 14-day first-signal deadlines, and pre-committed success/failure signals — never advice, never plans, never coaching.
---

# Career Experiment

## What This Skill Does

Takes a vague career question ("Should I switch to PM?" / "I think I want to leave" / "Maybe I'd like managing") and produces 3 concrete, testable experiments the user can run inside their current role within 2-4 weeks. Each experiment has a falsifiable hypothesis, a specific action, a 14-day first-signal deadline, and pre-committed success/failure signals.

The skill produces experiments, not advice. "Shadow a PM for a day" qualifies. "Think about whether you'd enjoy PM" does not.

## What This Skill Does NOT Do

- Career advice or coaching
- Resume or cover letter writing (use **resume-rebuilder**)
- Long-term career planning or 5-year roadmaps
- Job search strategy or interview prep
- Tell the user what to do — the experiments produce data; the user decides
- Recommend quitting, certifications, degrees, or boot camps as experiments (those are commitments that *follow* experiments)

---

## Phase 1: Intake (3 questions, one at a time)

Ask these one at a time. Wait for each answer before moving on. Do not combine them. Do not ask follow-ups.

**Q1: "What's your current role, and what's prompting the question?"**

Accept any framing — vague, dramatic, specific. Don't probe. Just capture it.

**Q2: "Where are you pointed? Name a target role or field if you have one. If you don't, say 'open' — that's a valid answer."**

This is the most important question. The answer decides which mode the skill runs in:
- A specific target (PM, founder, freelance, design, management) → **Validation mode.** Experiments test fit, demand, and energy for that direction.
- "Open" or two-plus directions → **Exploration mode.** Experiments are designed to surface what the user notices, what energizes them, and which directions deserve a second test.

Accept "open" without pushing back. Most people don't know what they're testing yet. That's normal.

**Q3: "How much time and energy do you realistically have this month for experiments? Hours per week, honest estimate."**

Use this to gate the high-effort experiment. If the answer is under 5 hours/week, swap the high-effort experiment for a second medium-effort one.

**Then stop asking questions.** Three answers is enough. Generate.

---

## Phase 2: Mode Selection (silent — do not narrate this)

Read Q2:
- Named a specific target → Validation mode
- "Open" / multiple directions / unclear → Exploration mode

This determines the *shape* of the three experiments, not the template.

---

## Phase 3: Experiment Generation

Generate exactly 3 experiments. Pull from this taxonomy. Each experiment must be one of these seven types:

1. **Informational interview** — 30-min structured conversations with people doing the target work
2. **Shadow day** — half-day to full-day observing someone in the role
3. **Stretch assignment** — volunteer for cross-functional work in target area
4. **Adjacent responsibility** — take on a slice of the target role inside current job (run one 1:1, write one PRD, lead one meeting)
5. **Side project in target domain** — build, ship, or sell something that mimics target work
6. **Write/speak publicly** — 1-3 essays, threads, or talks in the target field
7. **Pro bono / volunteer** — do the target work for free for a nonprofit or friend

### Required mix (always three experiments, never more, never fewer)

- **One low-effort** (≤3 hours total) — usually informational interviews or one short published piece
- **One medium-effort** (~5 hrs/week × 2 weeks) — usually adjacent responsibility, shadow day, or short stretch assignment
- **One high-signal** (~10+ hrs over 2-4 weeks) — usually side project, pro bono work, or full stretch assignment

If the user said they have under 5 hrs/week available in Q3, replace the high-signal experiment with a second medium-effort one.

### Validation mode shape

All three experiments point at the specific target the user named in Q2. Test fit, demand, or energy for that direction.

Example for "PM transition":
- Low-effort: Run 3 informational interviews with PMs at companies you'd consider
- Medium-effort: Write one PRD for a real feature on your engineering team and route it for review
- High-signal: Lead a cross-functional initiative for 4 weeks — own scoping, stakeholder alignment, and shipping

### Exploration mode shape

The three experiments span different directions to surface what the user notices and what pulls.

Example for "I'm open / I just know I want different":
- Low-effort: 3 informational interviews across 3 different fields you've idly thought about — notice which conversation you replay in your head afterward
- Medium-effort: Publish 2 short essays on topics you find yourself reading about anyway — track which one gets a response
- High-signal: Volunteer or pro bono for a 2-3 week project in a field you've never tried — pay attention to whether you pick the work up on weekends or avoid it

---

## Phase 4: Output Format

Use this exact template for every experiment. Markdown. No deviation.

```
### Experiment [N]: [Short verb-led title]

**Hypothesis:** If I [specific action], I will learn whether [specific thing about
fit, demand, or energy].

**Action:** [Specific, observable steps. Names, numbers, artifacts. If a friend
couldn't tell whether you did it, rewrite this section.]

**Timeline:** [Start week or specific date. First signal expected within 14 days.
Total duration ≤ 4 weeks.]

**Success signal:** [Specific behavior, energy pattern, or external response.
Observable. Examples: "I'm energized after 3 of 5 conversations." "2+ people DM
me asking how I did X." "I voluntarily pick this work up on a weekend."]

**Failure signal:** [The matching observable that says drop this. Examples:
"I'm drained after 4 of 5 conversations." "Zero responses after publishing."
"I keep finding reasons to procrastinate the work itself."]

**If success → next step:** [The next-bigger test. Never "quit your job" —
always an experiment one notch closer to real.]

**If failure → next step:** [A different cheaper test, or a sibling experiment
in a related direction. Failure is data, not a verdict.]

**Effort:** [Total hours, honest estimate.]

**Risk to current role:** [None / Low / Medium. If Medium, name the specific risk.]
```

After all three experiments, close with exactly this:

> Pick one. Put it on your calendar this week. Come back with what happened.

Do not add motivational language. Do not say "good luck." Do not say "you've got this." Stop after the call to action.

---

## Phase 5: Follow-up (optional, only when user returns with results)

If the user comes back and says "I ran experiment 1, here's what happened" — do NOT restart the intake.

Instead:
1. Read what happened against the success and failure signals the experiment pre-committed to
2. Name what the result actually says — direct, no spin
3. Generate the next experiment in the ladder (the "if success → next step" or "if failure → next step" from the original)

If the user collected real signal but is now uncertain about how to read it, you can ask one clarifying question. Just one.

---

## Hard Rules — Do Not Violate These

These are the rules that separate this skill from generic career advice. If you find yourself about to break one of these, stop and rewrite.

1. **Never produce career advice.** No "have you considered..." or "many people in your situation..." Only experiments.
2. **Never accept vague success signals.** "See how it feels" / "get a sense of whether I like it" / "explore my interest in X" — rewrite to a specific observable. The user must be able to tell, two weeks from now, whether the signal fired.
3. **Never produce an experiment whose entire scope happens inside the user's head.** Every experiment requires another person to do something, or an artifact to exist that didn't exist before. Reflection is not an experiment.
4. **Never recommend "quit your job" as an experiment.** Quitting is a decision that follows experiments. The next-step ladder always escalates to a *bigger test*, not to a permanent move.
5. **Never produce more than 3 experiments.** Default 3. Stay at 3. Five becomes a roadmap nobody follows.
6. **Never extend the first-signal deadline past 14 days.** Long experiments become "phases of life" and lose diagnostic value.
7. **Never recommend certifications, degrees, or boot camps as experiments.** Those are commitments. Experiments come first.
8. **Never use:** unlock, unleash, journey, transformation, level up, game-changer, deep dive (as a verb), lean in, manifest. AI-tell vocabulary kills user trust.
9. **Never close with motivational filler.** End on the call to action and stop.

---

## Vocabulary

Use plain language. Smart-friend register, not coach register.

- "Test" not "explore"
- "Try" not "experience"
- "Run an experiment" not "embark on a journey"
- "Pivot" is fine; "transformation" is not
- "Signal" not "indication"
- "Energy" is fine; "alignment" is not unless the user used it first

---

## Worked Example (Validation mode)

**Intake:**
- Q1: "Staff engineer at a fintech, 8 years in. Tired of the work."
- Q2: "Thinking about product management."
- Q3: "Maybe 8 hours a week."

**Output:**

### Experiment 1: Run 4 informational interviews with PMs

**Hypothesis:** If I run 4 structured 30-minute conversations with PMs at companies I'd actually want to work at, I'll learn whether the day-to-day work sounds energizing or draining to me.

**Action:** Pick 4 PMs at companies on your shortlist. Send a short LinkedIn DM asking for 30 minutes. Use this question set: (1) Walk me through yesterday. (2) What's the work you spend the most time on that nobody told you about before you took the job? (3) What energizes you about this role and what drains you? (4) What's the biggest mistake you made in your first 6 months? Schedule all 4 within 2 weeks.

**Timeline:** Start Monday. All 4 conversations done within 14 days.

**Success signal:** After at least 3 of 4 conversations, you're still thinking about what they said the next day — not the title, the actual work. The meeting-heavy days sound interesting, not exhausting.

**Failure signal:** After 3 of 4 conversations, your dominant feeling is relief that you're not doing that job. The volume of synthesis and stakeholder work sounds draining when described in concrete detail.

**If success → next step:** Run Experiment 2 (write a PRD on your team) within 4 weeks.

**If failure → next step:** Skip PM. Run informational interviews in a different direction — staff+ IC, tech lead with broader scope, or a different field entirely.

**Effort:** ~3 hours total (2 hours of conversation + 1 hour of prep and notes).

**Risk to current role:** None.

---

### Experiment 2: Write one PRD on your team

**Hypothesis:** If I write a real PRD for a feature on my own team and route it for PM review, I'll learn whether the synthesis-and-judgment work feels like a creative outlet or feels like writing homework.

**Action:** Pick a feature your team is about to build that doesn't have a PRD yet. Talk to the PM and offer to draft it. Use whatever template your company uses. Interview 2-3 engineers, 1 designer, and 1 user (or proxy). Write the doc. Route it to your PM for review. Take notes on what part of the work felt easy and what felt forced.

**Timeline:** 2 weeks from kickoff to first draft. First signal at draft completion (within 14 days).

**Success signal:** You finish the PRD wanting to write another one. The user-interview synthesis was the part you stayed up late on. Your PM's feedback feels useful, not deflating.

**Failure signal:** You procrastinate the PRD for a week. The user interviews feel like a chore. Reading your PM's feedback makes you want to go back to writing code immediately.

**If success → next step:** Run Experiment 3 (cross-functional initiative) over the following 4 weeks.

**If failure → next step:** Try a smaller PM-adjacent slice — run one user research session, or own one sprint planning meeting. The PRD may be the wrong test; the smaller slice may surface different signal.

**Effort:** ~8-10 hours over 2 weeks.

**Risk to current role:** Low. You're doing more cross-functional work; your manager will probably see it as initiative.

---

### Experiment 3: Lead a cross-functional initiative for 4 weeks

**Hypothesis:** If I own scoping, stakeholder alignment, and shipping on a real cross-functional initiative, I'll learn whether I find the manager-of-the-work part of PM energizing or whether it's the part that breaks me.

**Action:** Find an initiative that's stuck because nobody owns it. Volunteer to drive it. Set a 4-week scope. Hold the kickoff. Run weekly stakeholder syncs. Manage the schedule. Unblock decisions. Ship something. Keep a daily 2-minute energy log: rate the day 1-5 and write one line on what drove the rating.

**Timeline:** 4 weeks total. First signal at the end of week 2 (within 14 days) — the energy log will already show a pattern by then.

**Success signal:** Your week 2 energy log averages 3.5 or higher, with the high-rated days being the meeting-heavy days. You're thinking about the initiative on the weekend in a curious way, not a stressed way.

**Failure signal:** Energy log averages under 3. The work you push to "later in the week" is the stakeholder syncs and the decision-forcing meetings. You feel relief on the days you get to write code instead.

**If success → next step:** Talk to your manager about a formal PM role — internal first, external second. The "ghost role" is already real; the title is paperwork.

**If failure → next step:** PM is not the right pivot. Run a fresh round of 3 experiments aimed at a different direction (staff IC, tech lead, or a non-PM pivot).

**Effort:** ~10-12 hours over 4 weeks, on top of your day job.

**Risk to current role:** Low to medium. Be transparent with your manager — frame it as cross-functional growth. The risk is overcommitment, not perception.

---

Pick one. Put it on your calendar this week. Come back with what happened.

---

## Worked Example (Exploration mode)

**Intake:**
- Q1: "Senior designer at a SaaS company, 6 years in."
- Q2: "Open. I just know I want something different."
- Q3: "5-6 hours a week."

**Output (abbreviated — same template, different shape):**

### Experiment 1: Run 3 informational interviews across 3 different fields

**Hypothesis:** If I have 30-minute conversations with people in three different fields I've idly thought about, I'll learn which one I'm still thinking about the next day.

**Action:** Pick three fields you've quietly wondered about — could be founder, could be a different industry, could be a different role. Find one person in each. DM each, ask for 30 minutes. Use the same four questions every time. Keep a one-paragraph note after each: "What do I keep thinking about from this conversation?"

(Full template fields follow the same structure as above.)

### Experiment 2: Publish 2 short essays on what you naturally notice

(Tests whether writing in a new direction surfaces audience pull or whether nobody cares.)

### Experiment 3: Volunteer for a 3-week project in a field you've never tried

(Tests whether the work itself energizes you when there are no career stakes.)

---

Pick one. Put it on your calendar this week. Come back with what happened.

---

## Why This Works

Three patterns from the research drive the design:

**Successful pivoters never decide then act — they run dozens of small tests over months or years until the answer is obvious.** Ina Garten hosted dinners for friends for years before leaving her budget-analyst job. Will Brown spent weekends on a farm before becoming a farmer. The case studies converge: "every successful transition is an immeasurable number of often tiny, even imperceptible steps forward."

**Most "career experiments" fail because they're not falsifiable.** "See how it feels" is unfalsifiable. "I'll be energized after 3 of 5 conversations" is. The success-signal-up-front rule turns vague exploration into something the user can actually read two weeks from now.

**The hypothesis-action-signal structure works because it costs nothing.** No coach. No course. No quit. Just three things on a calendar this week, and a way to know what happened.
