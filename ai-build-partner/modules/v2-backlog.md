<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill runs every "great idea" through 5 questions during the build, logs the verdict, and forces every kept idea to cut something else of equal size from V1. Recurring use Days 1-30. Before the Opening, scan:

- **Section D.2** (T05 One-Page Scope — V1 features + ship date)
- **Section B.1** (V1 Core Outcome — load-bearing for Q1)
- **Section D.4** (T07 Scope Guillotine log — prior runs, for pattern-spotting)

If User Context Section D.2 V1 Core Outcome is empty → push back:

> "Can't run the Scope Guillotine without a locked V1 Core Outcome to defend. The outcome is the spine the filter checks against. Run `/unstuck scope` first to lock T05, then come back."

Two branches:

- **Branch A — Full V1 feature-list audit** (use BEFORE Day 1 build, or whenever V1 scope feels bloated): runs the filter against the WHOLE feature list, sorts to CORE/NICE/CUT
- **Branch B — Single mid-build idea** (use anytime a new idea hits during the build): runs the 5 questions on ONE new idea, KILL/KEEP verdict

If the buyer asks "should I add X to V1?" → Branch B. If the buyer says "I'm not sure my V1 list is right" → Branch A.

Don't ask what you can read. Pull V1 outcome + V1 features from D.2 before asking.

---

**Opening (output verbatim to the buyer):**

> "Scope Guillotine. Every idea that enters your head during the build is guilty until proven innocent.
>
> Two paths:
> - **Branch A — full V1 audit:** sort your whole V1 feature list into CORE / NICE / CUT
> - **Branch B — one mid-build idea:** run the 5-question filter, KILL or KEEP-and-cut-something-else
>
> Which one — full V1 audit, or a single idea that just hit?
>
> **One ground rule:** if KEEP, you cut something else of equal size from V1. The line doesn't move. Two ideas of equal size enter; one of equal size leaves. The ship date doesn't bend."

---

## Branch A — Full V1 audit (BEFORE building or when scope feels bloated)

**Step A1 — Anchor against time budget**

Pull from User Context Section A (weekly hours) + Section B (ship date).

> "Weeks until ship: ___. Hours/week you can commit: ___. Cargill (1985) says builders underestimate by ~2x, so realistic weeks = [computed].
>
> Multiply your hours by realistic weeks. That's your total build budget. Every CORE feature has to fit inside it."

**Step A2 — Sort each feature into CORE / NICE / CUT**

Pull V1 features from User Context Section D.2. For each:

- **CORE** — the V1 Outcome breaks without this. Ship it.
- **NICE** — makes V1 better but the outcome still works. File for V2.
- **CUT** — doesn't move the V1 Outcome at all. Kill it now.

For each feature, ask one sentence of reasoning tied to the V1 Outcome.

**Step A3 — Imposter check**

Flag any feature that looks like "must have because real products have this" rather than "must have because the V1 outcome breaks without it."

Usual suspects:
- Login flows / settings pages / dark mode / onboarding tours / profile management / notification preferences / analytics dashboards for the user

Move imposters from CORE → NICE or CUT.

**Step A4 — Proof check**

Flag any feature that's about proving competence to other builders rather than serving the buyer. Tells:
- "I should add tests"
- "Needs error handling for the edge case where…"
- "The architecture should support…"

Move proof-features from CORE → NICE or CUT.

**Step A5 — Budget check**

Add up CORE features' realistic-weeks estimates. If CORE total > available weeks → force a triage:

> "Your CORE features add up to [N] weeks. You have [M] weeks. [N-M] weeks of CORE has to become NICE. Which feature, ranked by 'most-removable while still hitting V1 Outcome,' becomes NICE?"

Force the triage. Don't move past until CORE fits in budget.

**Step A6 — Output the V2 Backlog starter**

For each NICE / CUT, output a paste-ready row:

| Date added | Idea | Why I want it | Priority (H/M/L) |
|---|---|---|---|

Branch A artifact:

```
SECTION D.4 — T07 Scope Guillotine (V1 audit)
Locked: [Date]
Source: /unstuck v2-backlog (Branch A)

V1 OUTCOME: [paste from D.2]
WEEKLY HOURS: ___
WEEKS TO SHIP: ___
REALISTIC WEEKS (Cargill 2x): ___
BUDGET (hours × weeks): ___

FEATURE TRIAGE:
- CORE (ship in V1): [list]
- NICE (V2 backlog): [list]
- CUT (kill now): [list]

V2 BACKLOG (paste-ready):
| Date | Idea | Why I want it | Priority |
| [date] | [paste] | [paste] | H/M/L |

NEXT: build CORE only. Re-run /unstuck v2-backlog when a new idea hits mid-build.

Built with the Unstuck Method — unstuckwithmolly.com
```

---

## Branch B — Single mid-build idea (recurring use)

**Step B1 — Pull the new idea + lock the anchor**

Ask:

> "What's the new idea — one or two sentences. And what's your V1 Core Outcome (from User Context Section D.2)? I'll anchor against it."

If the buyer can't name the V1 Outcome from memory, paste it from User Context. Don't run the filter blind.

**Step B2 — Run the 5-question Scope Detector**

Ask one at a time, no batching:

> 1. "Is this absolutely **essential** for your V1 Core Outcome to function? YES / NO."
> 2. "Can your V1 **ship without** this? YES / NO."
> 3. "Does this add **more than a day** of work to your current plan? YES / NO."
> 4. "Are you adding this because you're **avoiding** a harder, more important task? YES / NO. (Honest answer.)"
> 5. "Will you be **proud to ship V1** even without this? YES / NO."

**Step B3 — Apply the verdict**

| Pattern | Verdict | Action |
|---|---|---|
| Q1 = NO **OR** any of Q2-Q5 = YES | 🔴 **KILL — scope creep in costume** | Move to V2 Backlog |
| Q1 = YES **AND** Q2-Q5 all NO | 🟡 **MIGHT be essential — ask again** | If still YES, KEEP + cut something else of equal size from V1 |

State the verdict in one sentence. No hedging.

**Step B4 — Avoidance check (if Q4 = YES)**

If the buyer answered Q4 = YES (avoiding a harder task):

> "You said yes to Q4. What were you working on right before this idea hit? That's the real next action — go back to it. This new idea is procrastination in a costume. Logging to V2."

Push back if the buyer protests:

> "Molly's note: every idea that pops up mid-build is guilty until proven innocent. The avoidance-flag isn't a judgment — it's a signal. Back to the harder task."

**Step B5 — If KILL → write the V2 Backlog entry**

```
| Date added | Idea | Why I want it | Priority (H/M/L) |
| [today] | [paste] | [paste — be honest about why, not "it's important"] | [H/M/L] |
```

Push for honest "why" — "users will want it" is too vague. "Three customers asked for it in launch DMs" is honest.

**Step B6 — If KEEP → name what gets cut**

> "You said this is essential AND can't ship without it AND won't bloat scope AND you're not avoiding AND you wouldn't be proud without it. That's a real KEEP.
>
> Now: what comes OUT of V1 to make room? Pick ONE feature of equal size to cut. The scope line doesn't move. Two of equal size enter, one of equal size leaves."

Force the cut. If the buyer can't name what comes out → push:

> "If you can't name a cut, the new idea isn't actually essential — you'd find a cut for a real essential. Re-answer Q1: is this absolutely essential, or did you say YES out of attachment? Re-run the filter."

**Step B7 — Output the single-idea log entry**

```
SECTION D.4 — T07 Scope Guillotine (entry)
Date: [paste]
Source: /unstuck v2-backlog (Branch B)

Idea evaluated: [paste]
V1 outcome anchor: [paste]

Q1 essential? [Y/N]
Q2 V1 ships without? [Y/N]
Q3 >1 day work? [Y/N]
Q4 avoiding harder task? [Y/N]
Q5 proud to ship V1 without? [Y/N]

Verdict: [KILL → V2 / KEEP + cut X]
If KEEP, what got cut: [paste]
If KILL, V2 Backlog row added: [paste]

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step C — Pattern-spot across recent T07 runs**

If User Context D.4 shows 3+ Scope Guillotine entries in the last week, flag:

> "You've run the Scope Guillotine [N] times this week. Either: (a) your V1 scope was wrong from the start — run Branch A to re-cut, or (b) the build is hitting unexpected friction and ideas are escape valves. Run `/unstuck stuck` if it's friction, or `/unstuck scope` if it's a wrong-V1 problem."

---

**Voice rules (load-bearing for this skill)**

- Short sentences. This is a filter, not a discussion.
- No hedging on KILL verdicts. KILL is KILL.
- Cite Cagan (*Inspired*, 2017) on MVP discipline, Hofstadter's Law (1979) on time bias, OR Goldratt (1984) on bottlenecks only where it sharpens a verdict.
- Molly name-drop at the reframe: "Molly's Scope Guillotine: this is procrastination in a costume."
- Banned (in addition to core): "we should consider," "it depends," "what's your gut" — the buyer ran out of gut at minute 21.

</process>

<success_criteria>
This module is complete when:
- [ ] V1 Outcome anchor pulled from User Context D.2 (no blind filter runs)
- [ ] Branch picked (A full audit OR B single idea)
- [ ] For Branch A: every feature sorted into CORE/NICE/CUT, imposter + proof checks applied, budget check passed
- [ ] For Branch B: all 5 questions answered, verdict applied per matrix
- [ ] For KILL: V2 Backlog row written with honest "why"
- [ ] For KEEP: one feature of equal size identified and cut from V1
- [ ] Avoidance flag applied if Q4 = YES (route back to harder task)
- [ ] Section D.4 paste block delivered (audit table OR single entry)
- [ ] Pattern-spot flag raised if 3+ T07 runs in 7 days
</success_criteria>
