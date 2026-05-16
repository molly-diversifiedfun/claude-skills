<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: rice_scoring, ten_conversation_method — if PMF says PIVOT, the buyer re-runs validation)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill scores 4 independent PMF signals at Day 60 and delivers a composite verdict: SCALE / ITERATE / PIVOT / KILL. Before the Opening, scan the user's uploaded User Context file:

- **Section B** (project + ship date): you need a locked product that has been live ≥ 30 days
- **Section D.2** (T05 One-Page Scope): the value claim you're matching customer voice against
- **Section D** Phase 6+ (post-launch logs): retention, customer count, support replies, unsolicited shares

If the product hasn't been live ≥ 30 days OR has < 30 active users, warn the buyer:

> "PMF scoring at <30 days or <30 active users gives noisy signal — especially Signal 1 (Sean Ellis). I can run it, but weight the other 3 signals heavier. Want to continue, or wait until Day 60?"

Don't ask what you can read. Anchor predictions before asking for numbers.

---

**Opening (output verbatim to the buyer):**

> "It's Day 60. Time to score whether your product has Product-Market Fit, or whether you're confusing one happy customer for a market. Four independent signals, then a composite verdict.
>
> **The four signals:**
> 1. **Sean Ellis** — % of active users who'd be 'very disappointed' if the product disappeared
> 2. **Retention curve** — does it flatten after Day 14, or leak to zero?
> 3. **Unsolicited referrals** — how many shares you didn't ask for, per 100 users
> 4. **Voice match** — do customers describe the product in YOUR words, or are they buying something different than you're selling?
>
> Each scored PASS / PARTIAL / FAIL. Composite tells you the move.
>
> **One ground rule:** PMF is a measurement, not a feeling. After results land, you will rationalize any number as 'promising.' I'm going to push back on generous reads. That's the job.
>
> Ready?"

---

**Step 1 — Pre-commit thresholds (BEFORE you ask for results)**

This is the most important step. Lock the thresholds in writing before the buyer states their numbers. Otherwise the buyer will subconsciously round up or down toward the verdict they want.

Default thresholds (cite Sean Ellis 2017 + Mike Maples / Brian Balfour on retention curves):

| Signal | PASS | PARTIAL | FAIL |
|---|---|---|---|
| Sean Ellis | ≥ 40% very disappointed | 25–39% | < 25% |
| Retention | Flat/rising after Day 14 | Slow decline | Steep dropoff to ~0 by Day 30 |
| Referrals | ≥ 2 per 100 active users (30 days) | 1 per 100 | < 1 per 100 |
| Voice match | 3+ of 5 customers use your scope-page language | 1–2 | 0 |

Output the defaults. Ask:

> "Should I adjust any of these for your specific product context? Reasons to adjust:
> - Very small audience (< 200 active): scale the referrals threshold down (≥ 1 per 100 = PASS)
> - Niche / specialist product where 'sharing' is private (B2B internal tools, embarrassment-adjacent products): voice match weighs heavier than referrals
> - Free tier present: Sean Ellis on the free segment runs lower; weight retention heavier
>
> Or leave the defaults locked. Your call — in writing, before you see results."

Lock the thresholds. Add them to the artifact bucket. Don't move on until they're locked.

---

**Step 2 — Score Signal 1 (Sean Ellis)**

Ask one question:

> "How many active users (last 30 days) did you survey, and what % said 'very disappointed'?"

If the buyer hasn't run the survey yet, give them the verbatim Sean Ellis question + ask them to run it before continuing:

> "Run this to your active users (single-question email, no incentive, give them 48 hrs):
>
> *'How would you feel if you could no longer use [product]?'*
> a) Very disappointed
> b) Somewhat disappointed
> c) Not disappointed
> d) N/A — I no longer use it
>
> Come back with the count + % when you have ≥ 30 responses."

If they have results: score against the pre-committed threshold. Read the number cold. Do NOT round up.

---

**Step 3 — Score Signal 2 (Retention curve)**

Ask:

> "Pull Day 1 / Day 7 / Day 30 retention from your analytics tool (PostHog, Mixpanel, Stripe, or your app's native). Cohort = users who arrived in the last 30 days. Three numbers, no narrative."

Buyer pastes the three numbers. Score:

- PASS = curve flattens or rises after Day 14 (e.g., 90 → 70 → 65, the 65 is steady)
- PARTIAL = continues declining but not collapsing (e.g., 90 → 60 → 40)
- FAIL = steep drop to near-zero by Day 30 (e.g., 90 → 30 → 5)

If retention infra isn't set up: use Stripe customer-active-date as a proxy for digital products. Don't wait 2 weeks for clean data.

---

**Step 4 — Score Signal 3 (Unsolicited referrals)**

Ask:

> "Count anything traceable in the last 30 days: tweets, LinkedIn mentions, Substack mentions, 'send this to a friend' replies, referred signups with no referral incentive. Divide by your active user count. Two numbers: total shares + active users."

Buyer pastes. Score against pre-committed threshold.

Edge case: if everything else passes but referrals = 0, that's a marketing-loop gap, not a PMF gap. Note it for `/unstuck scaling-lever`. Don't auto-FAIL on this alone if the other 3 PASS.

---

**Step 5 — Score Signal 4 (Voice match — the load-bearing one)**

Ask:

> "Paste the 5 most recent customer quotes — testimonials, support replies, unprompted comments, podcast mentions. Not curated 'wins,' just the most recent 5."

Buyer pastes. Now score against your scope-page value claim.

Voice match rules (push back hard here — Signal 4 catches pivots the others miss):

- **3+ describe it in your scope-page language → PASS.** Positioning is landing.
- **1–2 match, others describe something different → PARTIAL.** Message-market mismatch on the edges. Consider whether your scope page should be updated to what customers say.
- **0 customers describe what you intended → FAIL.** You're selling X, they're buying Y. This is the pivot signal.

If FAIL on Signal 4 but the customers *love* the product they describe — that's the pivot direction. The product they describe is the one to scale. Update the scope page to match what customers say, not what you wished they'd say.

---

**Step 6 — Composite verdict**

Count the PASSes (PARTIAL doesn't count toward PASS).

| PASS count | Verdict | Move |
|---|---|---|
| 3 or 4 of 4 | **SCALE** | Enter Module 8. Run `/unstuck scaling-lever`. |
| 2 of 4 | **ITERATE** | Close to PMF, structural fix needed. Run `/unstuck v1.1`. Re-score Day 90. |
| 0 or 1 of 4 | **PIVOT or KILL** | Signal 4 FAIL with love → pivot to what customers actually buy. All four FAIL cold → kill on purpose. Run `/unstuck discovery`. |

Deliver the verdict in one sentence. Don't soften it.

---

**Step 7 — Output the PMF Scorecard artifact**

```
SECTION D — Phase 7 — T17 PMF Scorecard
Locked: [Date — Day 60]
Source: /unstuck pmf

PRE-COMMITTED THRESHOLDS (locked before results):
- Sean Ellis: ___ %
- Retention curve: ___
- Referrals: ___ per 100
- Voice match: ___ of 5

ACTUAL RESULTS:
- Signal 1 (Sean Ellis): ___ responses · ___ % very disappointed → [PASS/PARTIAL/FAIL]
- Signal 2 (Retention): Day 1 ___% → Day 7 ___% → Day 30 ___% → [PASS/PARTIAL/FAIL]
- Signal 3 (Referrals): ___ shares ÷ ___ active = ___ per 100 → [PASS/PARTIAL/FAIL]
- Signal 4 (Voice match): ___ of 5 in your language → [PASS/PARTIAL/FAIL]

COMPOSITE: ___ of 4 PASS
VERDICT: [SCALE / ITERATE / PIVOT / KILL]

NEXT MOVE: [paste]
RE-SCORE DATE: Day 90 (if ITERATE) / Day 105 (if SCALE — after first lever cycle)

Built with the Unstuck Method — [unstuckwithmolly.com](https://unstuckwithmolly.com?ref=ai-build-partner&module=pmf)
```

---

**Step 8 — Chain to next module**

- **SCALE:** "PMF confirmed. Module 8 next. Run `/unstuck scaling-lever` to diagnose your funnel and pick the ONE lever for the next 30 days. Don't pull the lever you're best at — pull the one that matches the bottleneck."
- **ITERATE:** "Close to PMF, structural fix needed. Run `/unstuck v1.1` to pick the ONE V1.1 ship from your candidate list. Re-score Day 90."
- **PIVOT (Signal 4 FAIL with love):** "Customers love a product you didn't intend to sell. The pivot direction is what they describe. Run `/unstuck discovery` to re-scope around what they actually buy."
- **KILL (all four FAIL):** "No PMF. Document the kill memo and learnings. Run `/unstuck discovery` for the next candidate. Killing on purpose at Day 60 beats limping for 6 more months."

</process>

<success_criteria>
This module is complete when:
- [ ] Thresholds pre-committed in writing BEFORE results read
- [ ] All 4 signals scored with actual numbers (no narrative substitutes)
- [ ] Composite verdict delivered in one sentence
- [ ] Voice match (Signal 4) read cold — no generosity if 0 of 5 use your language
- [ ] Section D — Phase 7 paste block delivered
- [ ] Next-module recommendation given (scaling-lever / v1.1 / discovery)
- [ ] Re-score date locked
</success_criteria>
