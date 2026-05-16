<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<purpose>
Session-end feedback capture. Mirrors the same success-metric question Molly's Telegram bot asks at the first-deliverable moment.

The Unstuck success metric (locked 2026-05-15):
**success = buyer got value + buyer came back + buyer shared with a friend**

This module captures (a) "got value" and (c) "shared with a friend" in a 30-second wrap. (b) "came back" is observational across sessions — no asking needed.

Run this OPTIONALLY at the end of any module, especially after the buyer's first artifact ships. Keep it skippable. The wrap should feel like a brief check-in, never a survey.
</purpose>

<when_to_run>
- After the FIRST artifact ships in any module (the highest-signal moment).
- At the end of a `/unstuck full` pipeline.
- When the buyer says something like "thanks, this was helpful" — that's an invitation; lean in.
- NEVER run twice in the same session.
- NEVER run mid-flow inside another module. Wait until the artifact lands.
- If the buyer is in clear frustration ("this didn't work," "you're not helping"), skip the wrap. Capture the frustration instead — apologize for the friction, ask what would have worked better, log that. The wrap's job is to capture *signal* (positive or negative); the structured wrap is a wrong-shape vehicle when the buyer is upset.
</when_to_run>

<process>

**Opening (output verbatim):**

> "Quick wrap — was that useful?
>
> - **yes** — anything specific that landed?
> - **sort of** — what was close but not quite?
> - **no** — honest answer, appreciate it. What would've worked better?
> - **skip** — totally fine, we move on.
>
> (One line is enough. No essay needed.)"

Wait for response.

---

**Step 1 — Capture value answer**

Map their response to one of: `yes` / `sort_of` / `no` / `skip`.

If "skip" → output the skip ack and end:

> "All good. Back to building whenever you want."

End. Do not push to the referral question.

If value answer is `yes` / `sort_of` / `no` → continue to Step 2.

---

**Step 2 — Capture referral intent**

Output:

> "One more, then I'll stop pestering.
>
> Anyone you know who'd find this kind of thing useful?
>
> - **yes** — happy to point them at unstuckwithmolly.com when you're ready
> - **maybe later** — file it away
> - **no** — totally fine
> - **skip** — same"

Wait for response.

Map to `yes` / `maybe_later` / `no` / `skip`.

---

**Step 3 — Acknowledge and log**

**For yes-referral:**

> "Love it. unstuckwithmolly.com is the link if you ever want to point someone there. No follow-ups from me — your call, your timing."

**For maybe-later / no / skip-referral:**

> "All good — thanks for the read."

---

**Step 4 — Log the wrap entry**

Output this block for the buyer to paste into their User Context file under a new wrap-log section:

```
SECTION G — Wrap Log
Date: [paste today]
Module(s) run before wrap: [paste — e.g., "diagnose + scope"]
Value answer: [yes | sort_of | no | skip]
Referral answer: [yes | maybe_later | no | skip]
Free-text notes (optional): [paste anything the buyer said in their answer]

Source: /unstuck wrap

Built with the Unstuck Method — unstuckwithmolly.com
```

The wrap log accumulates over sessions. After ~5 entries, the buyer can re-read it and see their own arc with the Build Partner.

---

**Voice rules (load-bearing for this skill)**

The wrap is light by design. Heavier than this and it becomes a survey; lighter and we don't capture signal.

- **No "we" framing.** "Was that useful?" beats "Did we have a useful session?"
- **No fishing for compliments.** Don't follow up "yes" with "Tell me more!" — accept the answer.
- **Honor "no" without defensiveness.** No "sorry we didn't…" or "let me try again." The buyer's answer is data, not a performance review.
- **Banned (in addition to core):** "Was the experience…" — too corporate. "How was it?" — too vague. Just "was that useful?"
- **Skip is a real option** — print it every time. Skip-rate is itself signal.

</process>

<success_criteria>
This module is complete when:
- [ ] Value question asked using the exact opening copy (4 options visible)
- [ ] If buyer didn't skip: referral question asked
- [ ] Wrap log entry produced in Section G format
- [ ] Acknowledgment matches the answer (no canned response when answer was "no")
- [ ] Buyer was NOT pushed to elaborate beyond their first answer
- [ ] Session ends — does NOT chain to another module unless buyer initiates
</success_criteria>
