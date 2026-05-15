# Career Experiment

**Stop deciding. Start testing.**

## The Problem

Career questions almost always show up as binary decisions: "Should I switch to PM?" "Should I leave for the startup?" "Should I quit and go solo?" Binary framing produces two failure modes — paralysis (months of thinking, no signal) or premature leaps (quit the job, then find out the new role looks nothing like the fantasy).

Most career advice makes both modes worse. Advice is asymmetric: cheap to give, expensive to follow, and impossible to falsify.

The Designing Your Life literature, Lean Startup applied to careers, and Dee McCrorey's Micro-Experiments toolkit all converge on the same diagnosis: people can't *think* their way to the right career. They have to build the cheapest possible test, run it, and read the result. Successful pivoters (Ina Garten cooked for friends for years before becoming the Barefoot Contessa; Will Brown weekended on a farm before leaving economics) didn't decide and then act. They ran dozens of small tests until the answer was obvious.

The gap in the tooling: there's no fast, structured way to translate "I'm thinking about leaving" into 3 concrete experiments you can run this month. ChatGPT generates advice. Career coaches charge hundreds. Books take weeks. This skill fills that gap.

## What It Does

You answer 3 questions. The skill produces 3 testable experiments — each with a falsifiable hypothesis, a specific action, a 14-day first-signal deadline, and pre-committed success/failure signals.

Every experiment is one of seven types:
1. Informational interview
2. Shadow day
3. Stretch assignment
4. Adjacent responsibility (a slice of the new role inside your current job)
5. Side project in the target domain
6. Write or speak publicly in the target field
7. Pro bono / volunteer work

The output is always 3 experiments at 3 effort levels: one low (≤3 hours total), one medium (~5 hrs/week × 2 weeks), one high-signal (~10+ hours over 2-4 weeks). Pick the one that fits your calendar this week.

The skill does not give advice. It does not coach. It produces experiments and stops. The experiments produce data. You make the decision.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Open the skill by saying: "Use the career-experiment skill" (if added to your Project) or paste the contents of `SKILL.md` as your first message
3. Answer 3 short questions: current role, target direction (or "open"), hours per week available
4. Receive 3 experiments
5. Pick one. Put it on your calendar this week.
6. Come back in 2 weeks with what happened — the skill generates the next experiment in the ladder

### In Claude Code

1. Add the skill to your Claude Code configuration:
   - Copy `SKILL.md` to `~/.claude/skills/career-experiment/SKILL.md`
   - Or reference it in your `.claude/CLAUDE.md`: `When designing career experiments, read path/to/career-experiment/SKILL.md`
2. Tell Claude Code: "Design 3 career experiments for me"
3. Answer the 3 intake questions
4. Get your experiments

### Tips for Better Results

- **Be honest about hours.** If you say 10 hrs/week and you have 4, the high-effort experiment will sit on your calendar untouched. Underestimate.
- **"Open" is a valid answer.** Most users don't actually know what they're testing yet. The skill has an exploration mode for this.
- **Don't pick all three.** Pick one. The whole point of the tiering is so you do something this week.
- **Come back with results.** The follow-up experiment is where most of the value compounds. The first round surfaces the question; rounds 2-3 surface the answer.

## What You Get

Each experiment looks like this:

```markdown
### Experiment 1: Run 4 informational interviews with PMs

**Hypothesis:** If I run 4 structured 30-min conversations with PMs at companies
I'd actually want to work at, I'll learn whether the day-to-day work sounds
energizing or draining to me.

**Action:** Pick 4 PMs at companies on your shortlist. Send a short LinkedIn DM
asking for 30 minutes. Use this question set: (1) Walk me through yesterday.
(2) What's the work you spend the most time on that nobody told you about?
(3) What energizes you about this role and what drains you? (4) Biggest mistake
in your first 6 months?

**Timeline:** Start Monday. All 4 conversations done within 14 days.

**Success signal:** After at least 3 of 4 conversations, you're still thinking
about what they said the next day — not the title, the actual work.

**Failure signal:** After 3 of 4 conversations, your dominant feeling is relief
that you're not doing that job.

**If success → next step:** Write a real PRD on your team within 4 weeks.

**If failure → next step:** Skip PM. Run informational interviews in a different
direction — staff+ IC, tech lead with broader scope, or a different field.

**Effort:** ~3 hours total.

**Risk to current role:** None.
```

Three of these. Then a one-line call to action: "Pick one. Put it on your calendar this week. Come back with what happened."

That's it. No coaching. No "you've got this." No 5-year roadmap.

## The Research Behind It

Three findings shaped the design:

**Successful pivoters run dozens of small tests, not one brave leap.** Every case study in the literature (Burnett & Evans, *Designing Your Life*; Roberto Seif's "90-day career experiment"; Wharton's career pivot guide) converges on the same pattern: "every successful transition is an immeasurable number of often tiny, even imperceptible steps forward." The skill enforces small, time-bounded steps by hard-capping experiments at 4 weeks and requiring a first signal within 14 days.

**The hypothesis-action-signal structure is what separates an experiment from a journal entry.** Karl Popper's falsifiability criterion ports directly to careers: if you can't imagine a result that would change your mind, you're not running an experiment. The skill refuses to accept vague success signals like "see how it feels" and forces a specific observable behavior, energy pattern, or external response.

**Inside-role experiments produce 80% of the signal at 5% of the risk.** The seven-type taxonomy is built from career-services literature (Wellesley, MIT, MSU), the IC-to-manager transition guides (LeadDev, Mind The Product), and the Lean Startup adaptation (MovingWorlds, Filament). Stretch assignments, adjacent responsibilities, and shadow days all let you do the work before you have the title — which is the only way to know if you actually want it.

Full research synthesis: [`docs/research/16-career-experiment.md`](../docs/research/16-career-experiment.md).
Design decisions and tradeoffs: [`docs/prds/16-career-experiment.md`](../docs/prds/16-career-experiment.md).

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Output format | Experiments only — three of them | Advice produces inaction. Plans produce overwhelm. Three concrete experiments produce one Monday move. |
| Number of experiments | Three by default — tiered by effort | One feels arbitrary. Five+ overwhelms. Three covers your risk-appetite range and guarantees one is doable this week. |
| Time bound | First signal within 14 days. Total ≤ 4 weeks. | Career questions have a half-life. A 90-day experiment that produces no signal until day 89 is indistinguishable from procrastination. |
| Hypothesis required | Always | The hypothesis is the experiment. Without it, you're just doing tasks. Stating it often surfaces that you don't actually know what you're testing — which is itself diagnostic. |
| Success/failure signals | Specifics only — observable behaviors, energy patterns, or external responses | "See how it feels" is unfalsifiable. The skill refuses vague signals and rewrites them. |
| Intake length | 3 questions max | Long intake signals "I'm here to coach you." Short intake signals "I'm here to design experiments." |
| Vague targets ("I want different") | Accept it — switch to exploration mode | Most users don't know what they're testing yet. Forcing premature specificity loses them. |

## Pairs With

- **[decision-maker](/decision-maker/)** — when your experiments have produced enough data and you actually need to make the call
- **[self-interview](/self-interview/)** — to surface what you already know but haven't articulated about what you want
- **[mental-models](/mental-models/)** — for the meta-question of how to think about the broader trajectory
- **[resume-rebuilder](/resume-rebuilder/)** — once the direction is set, build the artifact

## What This Skill Does NOT Do

- Career advice or coaching (it produces experiments; you make the decision)
- Resume or cover letter writing
- Long-term career planning or 5-year roadmaps
- Job search strategy or interview prep
- Validate that a specific career change is "right" — that's your job after the experiments produce data
- Recommend quitting, certifications, degrees, or boot camps as experiments (those are commitments that follow experiments, not the test itself)
