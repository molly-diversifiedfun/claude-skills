# PRD: career-experiment

## Problem

Career questions almost always show up as binary decisions: "Should I switch to PM?" "Should I leave for the startup?" "Should I quit and go solo?" Binary framing produces two failure modes — paralysis (months of thinking, no signal collected) or premature leaps (quit the job, then discover the new role looks nothing like the fantasy). Most career advice makes both modes worse, because advice is asymmetric: cheap to give, expensive to follow, and impossible to falsify.

The Designing Your Life literature (Burnett & Evans), Lean Startup applied to careers (Ries → MovingWorlds, Roberto Seif), and Dee McCrorey's Micro-Experiments toolkit all converge on the same diagnosis: people can't *think* their way to the right career. They have to build the cheapest possible test, run it, and read the result. Successful pivoters (Ina Garten, Will Brown, every case study in the literature) didn't decide and then act — they ran dozens of small tests over months or years until the answer was already obvious.

The gap in the tooling: there's no fast, structured way to translate a vague career question into 3 concrete experiments you can run this month, with success/failure signals defined in advance. ChatGPT generates advice. Career coaches charge hundreds. Books require weeks. The skill fills that gap.

## Solution

A skill that takes a vague career question and produces 3 testable, time-bounded experiments — each with a falsifiable hypothesis, a specific action, a 2-week first-signal deadline, and pre-committed success/failure criteria. The output is never advice. It's always experiments the user can put on a calendar.

Default output: three experiments at three effort levels (one ≤3 hrs total, one ~5 hrs/wk × 2 wks, one ~10+ hrs over 2-4 wks). Each ends with "if success → next step" and "if failure → next step" so the user always knows the move regardless of the result.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Output format: experiments vs. plan vs. advice | **Experiments only — three of them** | Advice produces inaction, plans produce overwhelm. Three concrete experiments produce one Monday move. The whole point of the skill is the gap between "career advice" (useless) and "career experiment" (testable). |
| Number of experiments | **Three by default** — explicitly tiered by effort: low (≤3 hrs), medium (~5 hrs/wk × 2 wks), high (~10+ hrs over 2-4 wks) | One feels arbitrary. Five+ overwhelms. Three covers the user's risk-appetite range. The tiering guarantees one is doable this week. |
| Time bound | **Hard cap: first signal within 14 days.** Total experiment can run 2-4 weeks. | Career questions have a half-life. A 90-day experiment that produces no signal until day 89 is indistinguishable from procrastination. The 2-week first-signal rule forces resolution. |
| Hypothesis required vs. optional | **Required.** Every experiment opens with "Hypothesis: If I [action], I will learn whether [specific thing]." | The hypothesis is the experiment. Without it, you're just doing tasks. Stating the hypothesis often surfaces that the user doesn't know what they're testing — which is itself diagnostic. |
| Success/failure signals | **Specifics only.** Concrete behaviors, energy patterns, observable external responses. | "See how it feels" is unfalsifiable. The skill refuses to produce vague signals and rewrites them. This is the single hardest constraint to enforce. |
| Personal advice vs. structured output | **Structured output, no advice.** Skill produces experiments; user produces decisions. | Career advice from an LLM is the bottom quartile of useful career advice. Experiments produce data the user trusts because they generated it. Stay in the experiment-design lane. |
| Intake | **Three questions max.** Current role, target direction (or "open"), time/energy available this month. | Long intake signals "I'm here to coach you." Short intake signals "I'm here to design experiments." |
| Vague targets ("I want something different") | **Accept it.** Generate 3 *exploration* experiments instead of 3 *validation* experiments — informational interviews across different fields, a short writing test to surface what the user naturally notices, one shadow day. | Most users don't know what they're testing yet. Forcing premature specificity loses them. Exploration mode is a first-class mode of the skill. |

## Interaction Model

**Phase 1: Intake (3 questions, asked one at a time)**

1. "What's your current role and what's prompting the question?" — accept any framing
2. "Where are you pointed? Name a target role/field if you have one. If you don't, say 'open' — that's a valid answer." — branches the rest of the skill
3. "How much time and energy do you realistically have this month for experiments? Hours per week, honest estimate." — gates the high-effort experiment

Apply the 70% rule: don't ask follow-ups. With three answers, generate.

**Phase 2: Mode Selection (silent)**

- If Q2 named a specific target → **Validation mode.** Experiments test fit/demand/energy for that specific direction.
- If Q2 was "open" or named two+ directions → **Exploration mode.** Experiments are designed to surface what the user notices, what energizes them, and which directions deserve a second look.

**Phase 3: Experiment Generation (no further user input)**

Generate exactly 3 experiments using the template below. Pull from the seven-type taxonomy in the research doc:
1. Informational interview
2. Shadow day
3. Stretch assignment
4. Adjacent responsibility (slice of new role inside current job)
5. Side project in target domain
6. Write/speak publicly
7. Pro bono / volunteer

Required mix:
- One **low-effort** (≤3 hrs total) — usually informational interview or one published essay
- One **medium-effort** (~5 hrs/wk × 2 wks) — usually adjacent responsibility, shadow day, or short stretch assignment
- One **high-signal** (~10+ hrs over 2-4 wks) — usually side project, pro bono work, or full stretch assignment

If the user said they have <5 hrs/wk available, replace the high-signal experiment with a second medium-effort one.

**Phase 4: Output**

Three experiments, each in the exact template format. Closing line: "Pick one. Put it on your calendar this week. Come back with what happened."

No follow-up advice. No "good luck." No "you've got this." End on the call to action.

**Phase 5 (optional, only if user returns with results)**

If the user comes back and says "I ran experiment 1, here's what happened" — read the result against the success/failure signal they pre-committed to, and generate the next experiment. Don't restart the intake.

## Experiment Template (output spec)

Every experiment in the output uses this exact structure. Markdown, no exceptions.

```
### Experiment [N]: [Short verb-led title]

**Hypothesis:** [One sentence: "If I [action], I will learn whether [specific thing
about fit, demand, or energy]."]

**Action:** [Specific, observable steps. Who you'll talk to / what you'll build /
what you'll publish. If a friend can't tell whether you did it, rewrite.]

**Timeline:** [Start date or week-of. First signal within 14 days.
Total duration ≤ 4 weeks.]

**Success signal:** [Specific behavior, energy pattern, or external response.
Observable. No "see how it feels."]

**Failure signal:** [The matching observable that says "drop this."]

**If success → next step:** [Cheapest next experiment that escalates commitment.
Never "quit your job" — always the next-bigger test.]

**If failure → next step:** [A specific cheaper or different test. Failure is
data, not a verdict.]

**Effort:** [Total hours, honest estimate.]

**Risk to current role:** [None / Low / Medium. If Medium, name the specific risk.]
```

## Anti-Patterns to Avoid in Implementation

- **Never produce career advice.** No "have you considered..." or "many people in your situation..." The skill produces experiments, not opinions.
- **Never accept vague success signals.** "See how it feels" / "get a sense of whether I like it" / "explore my interest in X" — all rewrites required. Force a specific observable behavior.
- **Never produce an experiment whose entire scope happens inside the user's head.** If no other person is involved, no calendar entry exists, and no artifact gets produced — it's not an experiment, it's reflection.
- **Never recommend "quit your job" as an experiment.** Quitting is a decision that follows experiments, not an experiment itself. The next-step ladder always escalates to a *bigger test*, not to a permanent move.
- **Never produce more than 3 experiments per request.** The skill defaults to 3 and stays at 3. Five experiments produce a roadmap nobody will follow.
- **Never produce experiments longer than 4 weeks.** First signal at 14 days, total duration capped. Long experiments become "phases of life" and lose all diagnostic value.
- **Never recommend certifications, degrees, or boot camps as experiments.** Those are commitments that follow experiments. They're not the test.
- **Never use the word "journey," "unlock," "transformation," or "deep dive."** AI-tell vocabulary; user-trust killer.
- **Never close with motivational language.** End on the call to action ("Pick one. Put it on your calendar.") and stop.

## Success Criteria

- User receives 3 experiments within 5 minutes of starting the skill
- Every experiment has a hypothesis, an observable action, a 14-day first-signal deadline, and a specific success + failure signal
- User can pick one and put it on their calendar without asking the skill anything else
- The output works in both Claude.ai (no tools required) and Claude Code (no tools required) — pure prompt-based design
- User who returns 2 weeks later with results gets the next experiment in the ladder, not a fresh intake

## What This Skill Does NOT Do

- Career advice or coaching (it produces experiments; the user makes decisions)
- Resume or cover letter writing (use **resume-rebuilder**)
- Skill assessment or strengths analysis
- Long-term career planning or 5-year roadmaps
- Job search strategy or interview prep
- Salary negotiation
- Validation that a specific career change is "right" — that's the user's job after the experiments produce data

## Pairs With

- **decision-maker** — when experiments have produced enough data and the user needs to actually make the call
- **self-interview** — to surface what the user already knows but hasn't articulated about what they want
- **mental-models** — for the meta-question of how to think about the broader career trajectory
- **resume-rebuilder** — once the direction is set, build the artifact

## Technical Notes

- Pure prompt-based — works in Claude.ai and Claude Code with zero tools
- No file I/O required; output is markdown the user can paste anywhere
- Intake total: 3 questions; generation: instant
- Recommended cadence for repeat use: every 2-4 weeks, after running the previous experiment
