<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill is a diagnostic, not a discussion. The buyer has been stuck for 20+ minutes — they need a decision in 5-15 min, not a conversation. Before the Opening, scan:

- **Section D.2** (T05 One-Page Scope) — the V1 outcome that scope-creep checks against
- **Section D.5** (T08 Sprint Plan) — what was supposed to ship this week
- **Section A** (voice) — match register

Two tools live inside this skill. Pick ONE based on symptom:

- **Tool 1 — Scope Creep Detector:** project feels bigger than last week
- **Tool 2 — Stuck Decision Tree:** staring at one specific problem for 20+ min

If the buyer's first description sounds like both ("everything feels stuck, plus this one thing won't work"), default to Tool 1 first — scope creep is usually upstream.

Don't ask what you can read. Pull V1 outcome from D.2 before asking what's stuck.

---

**Opening (output verbatim to the buyer):**

> "Stuck Toolkit. Two tools — pick the symptom that matches:
>
> - **Tool 1 — Scope Creep Detector** if the *project* feels bigger than last week (you've added features, you're redesigning things that worked, ship date moved without re-scoping)
> - **Tool 2 — Stuck Decision Tree** if you've been staring at *one specific problem* for 20+ minutes
>
> Which one? (If both — we run Tool 1 first. Scope creep is usually upstream of decision paralysis.)
>
> **One ground rule:** this is a diagnostic, not a discussion. Short answers, no batching. End with one decision + one next action. Verb first."

---

## Tool 1 — Scope Creep Detector

**Step T1.1 — Run the 5-check sniff test**

Ask, one at a time, NO batching:

> "Right now, today — check every one that's true:
> 1. I've added a feature that wasn't in my Product Scope (T05 One-Page Scope)
> 2. I'm redesigning something that already works
> 3. I've said 'while I'm at it…' in the last 48 hours
> 4. My ship date has moved and I haven't formally re-scoped
> 5. I'm building something I haven't validated with a real person"

Count the checks.

**Step T1.2 — Read the score**

- 🟢 **0 checks — Clean.** "Keep building. The friction isn't scope. Run Tool 2 instead — there's a specific problem stuck."
- 🟡 **1 check — Yellow flag.** "Write down what changed and why. If the reason isn't 'a customer told me this matters,' revert it. Specifically — what changed?"
- 🟠 **2 checks — Orange flag.** "Stop building for 15 min. Re-read T05 One-Page Scope. Remove anything that wasn't on it."
- 🔴 **3+ checks — Red flag. Full stop.** "Go back to T05. Re-read your V1 features. Cut everything that isn't on that list. Everything you cut goes to V2 Backlog. Don't move forward until the scope matches T05."

**Step T1.3 — Log what changed**

| What I added / changed | In original scope? | Why I added it | Verdict |
|---|---|---|---|

Force every change into a verdict — KEEP / REVERT / V2. No "I'll decide later."

If buyer says "I'll decide later" → push back:

> "'Decide later' is how scope creep wins. The cost of deferring is rebuilding around it for another 3 days, then having to cut it anyway. Verdict now: KEEP it (and cut something else of equal size) / REVERT it (delete now) / V2 (move to backlog, stop building it today)."

**Step T1.4 — Output decision**

```
SECTION D.7 — T10 Stuck Toolkit (entry)
Tool used: Tool 1 — Scope Creep Detector
Date: [paste]

Sniff-test score: ___ / 5 (color: 🟢/🟡/🟠/🔴)

What changed (logged):
- [paste each item + verdict]

Next action (verb-first, 1 sentence): [paste]
Source: /unstuck stuck

Built with the Unstuck Method — unstuckwithmolly.com
```

Then chain: "Back to building. Next time scope feels bigger, run Tool 1 again — it should take 2 minutes once you know the pattern. If it's a specific problem next time (not whole-project bloat), use Tool 2."

---

## Tool 2 — Stuck Decision Tree

**Step T2.1 — Define the problem in one sentence**

Ask:

> "In one sentence: what's the problem? Not 'I'm stuck on the auth flow' — that's the topic. The PROBLEM is: 'I can't decide between server-side Stripe verification or client-side webhook polling, and I've tried both for 25 minutes.'"

If the buyer can't define it in one sentence → that's the diagnosis:

> "You're not stuck on a problem. You're stuck on a fog. Set a 5-min timer. Write everything you're thinking about this task — stream of consciousness, don't edit. When the timer goes off, read it back. The problem is usually in there. Paste it when you have it."

Wait for the one-sentence problem before moving on.

**Step T2.2 — Have you tried the simplest possible solution?**

> "The simplest possible version. The dumb version you'd be embarrassed to show someone. Have you tried that?"

**If YES + worked:** "Ship it. Move on. Stop optimizing. Next action: [verb-first]."

**If YES + didn't work:** "Go to Step T2.3."

**If NO:**
> "Try the dumb version first. The version that handles only the happy path, no edge cases, hardcoded values where needed. Build that. 30-min time-box. If it works, you're done. If it doesn't, you'll know exactly what's actually broken — and that's a smaller problem than 'the whole thing.'"

Lock the 30-min time-box. Pause the session. Return when done.

**Step T2.3 — Is this a skill gap or a decision gap?**

Ask:

> "Skill gap = 'I don't know HOW to do this.' Decision gap = 'I don't know WHICH option to pick.' Which one?"

**🔧 SKILL GAP — three options, pick ONE:**

1. Ask AI for help (give context, not just the question — paste the error + 3 lines around it + what you've already tried)
2. Find a tutorial that's **under 15 min** (longer = rabbit hole; if every tutorial is 45+ min, you need a different teacher, not more time)
3. Hire someone on Fiverr for **under $50** (e.g., a 30-min Calendly call with someone who's done this specific thing)

Pick ONE. Set a **30-min time-box**. If you can't solve it in 30, skip the problem and come back tomorrow with fresh eyes.

**🤔 DECISION GAP — the truth:**

> "If both options are close, it doesn't matter which one you pick. Pick the one you can undo more easily. Ship it. Get feedback. Then decide."

Ask:

> "Which is more reversible? Pick that. Write your decision in one sentence."

If the buyer keeps debating → push:

> "You've been debating for [N] minutes. The decision IS the next action. Pick the reversible one. We move on."

**Step T2.4 — Still stuck after Step T2.3?**

> 🚶 "Walk away. Literally. Outside for 10 minutes. Your brain solves problems better when it's not staring at them. Set a reminder to come back in 1 hour."
>
> "If you're still stuck after the walk + 1 hour: post in your accountability community OR DM your build partner. The pattern is: solo for 20 min → tool for 15 min → walk for 10 min → ask another human. Each step is shorter than the last because the more stuck you are, the more outside-input matters."

**Step T2.5 — Output decision**

```
SECTION D.7 — T10 Stuck Toolkit (entry)
Tool used: Tool 2 — Stuck Decision Tree
Date: [paste]

Problem (one sentence): [paste]
Tried simplest version? [yes / no — applied 30-min time-box]
Gap diagnosis: [skill / decision]
Option chosen: [paste]
30-min time-box ends at: [paste time]

What I decided: [paste]
Next action (verb-first, 1 sentence): [paste]
Source: /unstuck stuck

Built with the Unstuck Method — unstuckwithmolly.com
```

Chain: "Back to building. If you're stuck again on the same kind of problem within 48 hrs, that's a Skill-gap pattern — book the Fiverr / longer tutorial / paired session. Same problem 3x = invest in the skill, don't keep wrestling."

---

**Voice rules (load-bearing for this skill)**

This is a diagnostic, not a discussion. Diagnostic rules override the usual conversational tone:

- Short sentences only
- No "let me know if that helps"
- No batching — one question, one answer
- No hedging on verdicts — RED is RED, KILL is KILL
- Molly name-drop at the "walk away" moment ("Molly's note: walk away. Literally. Go outside for 10 minutes.")
- Banned (in addition to core): "let's explore," "thinking through," "considering" — the buyer is past considering
- Cite Conway (1968) on system gaps OR Goodhart's Law (1975) on misaligned metrics only where it sharpens a verdict

</process>

<success_criteria>
This module is complete when:
- [ ] Tool picked (Tool 1 OR Tool 2, with default-to-Tool-1 if both apply)
- [ ] For Tool 1: 5-check sniff test run + score read + every change has a KEEP/REVERT/V2 verdict
- [ ] For Tool 2: problem defined in one sentence (or fog-clearing exercise run first)
- [ ] For Tool 2: simplest-version step run with 30-min time-box
- [ ] For Tool 2: gap diagnosed (skill vs. decision) and ONE option picked
- [ ] Output is a decision + verb-first next action — NOT a discussion
- [ ] Section D.7 log entry delivered
- [ ] Pattern flag raised if same problem appeared 3x in 7 days
</success_criteria>
