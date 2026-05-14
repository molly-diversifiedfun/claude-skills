<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill decides when + how to change the V1 price — once per quarter, not every month. Day 38+ of the sprint, OR triggered by refund/conversion/WTP signals. Before the Opening, scan:

- **Section D.3** (T06 Pricing Calculator — V1 price + reasoning)
- **Section D.7.5** (T24 Support / Refund — current refund rate)
- **Section D.9** (T12 5-Email Launch — conversion data from launch sequence)
- **Section D — Phase 7** (any prior T25 iteration entries — enforce one-change-per-quarter rule)

If days-since-launch < 30 → push back:

> "You don't have enough data yet. Pricing signal is noisy below ~30 days / 30 sales. Wait. Most likely the price is in the right zone and the noise is just small-sample variance."

If a previous T25 iteration ran in the last 90 days → push back:

> "You changed price [N] days ago. The one-change-per-quarter discipline is the moat — buyers stop trusting you if you raise in March and again in April. Wait until [date]."

Don't ask what you can read. Anchor against the V1 price + refund rate before asking the 5 signal numbers.

---

**Opening (output verbatim to the buyer):**

> "You priced V1 with T06. Now you have 30-60 days of data. This skill decides whether to change the price — once. Not twice in 6 weeks. Once.
>
> The flow:
> 1. **Score 5 pricing signals** (conversion · refund · 'paid more' · 'too expensive' · time-on-page)
> 2. **Apply the decision matrix** — RAISE / LOWER / HOLD / DON'T MOVE (fit problem)
> 3. **If RAISE/LOWER:** lock the new price + grandfather existing buyers + announce BEFORE the change
> 4. **Set the next review date** (no earlier than +90 days from this change)
>
> **One ground rule:** if refund rate > 10%, we DON'T move price. We investigate fit. Lowering price doesn't fix wrong audience.
>
> Ready?"

---

**Step 1 — Score the 5 signals (last 14 days)**

Ask:

> "Pull these 5 numbers from your last 14 days. Don't guess — open Stripe, your ESP, your DMs:
>
> 1. **Conversion rate** — landing-page visits → checkout completes. (%)
> 2. **Refund rate** — refunds ÷ purchases. (%)
> 3. **'Would have paid more' mentions** — unprompted customer comments saying price felt low. (count)
> 4. **'Too expensive' mentions** — prospects (pre-purchase, in DMs/replies) flagging price as blocker. (count)
> 5. **Time-on-page before checkout** — median seconds/minutes. (from analytics)
>
> If you can't pull one number, say so — I'll mark it as unknown."

Read against industry baselines:

| # | Signal | Healthy | Concerning | Read direction |
|---|---|---|---|---|
| 1 | Conversion | 3-6% warm / 1-3% cold | > 8% | ↑ raise / ↓ lower / → hold |
| 2 | Refund | 2-5% | > 8% / crisis > 15% | ↑ raise / ↓ lower / → hold |
| 3 | "Paid more" | 0-2 / 14 days | 3+ | ↑ raise / → hold |
| 4 | "Too expensive" | 0-2 / 14 days | 5+ | ↓ lower / → hold |
| 5 | Time-on-page | 2-5 min median | > 5 min OR < 2 min | ↑ raise / ↓ lower / → hold |

---

**Step 2 — Apply the decision matrix**

| Pattern | Verdict | Move |
|---|---|---|
| Conversion ≥ 6% + refund ≤ 5% + "paid more" ≥ 3 | **RAISE** | +20-30% |
| Conversion ≥ 8% + refund ≤ 3% + "paid more" ≥ 5 | **RAISE bigger** | +40-60% |
| Conversion ≤ 2% + "too expensive" ≥ 5 + refund ≤ 5% | **LOWER** | -20-30% OR add payment-plan option |
| Conversion ≤ 1% + "too expensive" ≥ 8 | **LOWER + investigate** | -30% AND investigate audience-fit (not just price) |
| **Refund rate > 10%** (any conversion) | **DON'T MOVE PRICE** | Investigate fit. Lowering won't fix wrong audience. |
| Conversion 3-6%, refund 3-8%, mixed | **HOLD** | Wait 30 more days. Price is in the right zone. |

State the verdict in one sentence. Don't hedge.

If 3+ signals don't point the same direction → HOLD by default:

> "Not enough signal agreement. Wait 30 more days. Most likely the price is correct and the variance is noise. Re-run T25 then."

---

**Step 3 — If verdict is RAISE or LOWER, apply the 3 rules**

**Rule 1 — Existing buyers grandfather at V1 price. Always.**

> "Existing buyers paid $[OLD]. They keep that price forever — no expiry, no claw-back, no 'we're raising for everyone.' The next time you raise, existing-considering-buyers convert on the announcement (~30-50% of fence-sitters buy). Clawing back what people already paid breaks that mechanism. Don't."

**Rule 2 — Announce the change BEFORE you do it.**

> "Email subject template: 'Price goes up to $[NEW] on [DATE].' Compresses 30 days of decision-friction into 7 days. ~30-50% of fence-sitters buy on the announcement. (For LOWER: 'Lowered the price on [PRODUCT]' — slightly different mechanics, see Step 4.)"

**Rule 3 — One change per quarter.**

> "Lock the calendar: next pricing review = [today + 90 days]. Two moves in 6 weeks signals you don't know the price. Buyers stop trusting you on it. The discipline is the moat."

---

**Step 4 — Draft the announcement (RAISE)**

```
Subject: Price goes up to $[NEW] on [DATE]

[PRODUCT] launched at $[OLD]. Since then, [N] customers have shipped. 
The product is better than at launch — [specific addition from V1.1 — pull from User Context Section D — Phase 7 if T18 ran].

Starting [DATE], the price is $[NEW]. If you've been thinking about it, 
the window closes at midnight Pacific.

If you're already a customer, your price is locked. No action needed.

[Buy link]
```

≤ 250 words. Make the V1.1 improvement specific — vague "the product is better" reads like a justification, not a fact.

---

**Step 5 — Draft the announcement (LOWER)**

```
Subject: Lowered the price on [PRODUCT]

Honest update: I priced [PRODUCT] at $[OLD]. The math at that price didn't 
work for enough of the [persona] this is meant for. New price is $[NEW].

If you bought at $[OLD] in the last 14 days, you get a $[DIFF] refund — 
already sent to your card. No action needed.

[Buy link]
```

The 14-day refund-for-recent-buyers maintains trust. The buyer who paid $[OLD] 6 days ago will tell their friends if you make it right. The one who paid $[OLD] 200 days ago is already past the sting.

≤ 220 words.

---

**Step 6 — Don't move multiple levers in the same week**

> "If you're also shipping V1.1, changing the landing-page hero, or relaunching to a new audience — DON'T also change price in the same week. You won't know which lever moved the result. Pick ONE lever, hold the others, measure 30 days, then decide the next."

Push back if the buyer wants to move multiple levers at once.

---

**Step 7 — Output the Pricing Iteration artifact**

```
SECTION D.6.3 — T25 Pricing Iteration
Locked: [Date]
Source: /unstuck pricing-iteration

V1 PRICE: $[OLD]
DAYS SINCE LAUNCH: ___
TOTAL V1 SALES: ___

THE 5 SIGNALS (last 14 days):
- Conversion: ___% [direction]
- Refund: ___% [direction]
- "Paid more" mentions: ___ [direction]
- "Too expensive" mentions: ___ [direction]
- Time-on-page: ___ min median [direction]

VERDICT: [RAISE / RAISE bigger / LOWER / LOWER + investigate / DON'T MOVE / HOLD]

IF RAISE/LOWER:
- New price: $[NEW]
- Change date: [DATE]
- Existing-buyer grandfather: yes
- Recent-14-day refund (if LOWER): $[DIFF] per buyer
- Announcement email: drafted (Step 4 or 5)
- Landing-page update: [one sentence above buy button]
- Social post: [150 chars max]

NEXT REVIEW: [today + 90 days]

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step 8 — Chain to next module**

- "Price locked. If RAISE: announce today, change date in 7 days. If LOWER: announce + apply refunds today. If HOLD or DON'T MOVE: re-run T25 in 30 days. At Day 60, refund rate from `/unstuck support-refund` feeds `/unstuck pmf` as part of the PMF Scorecard. If you raised, watch conversion for the next 30 days — if it drops below your previous baseline by more than 25%, the raise was wrong; re-run T25."

</process>

<success_criteria>
This module is complete when:
- [ ] Days-since-launch ≥ 30 (otherwise wait)
- [ ] No T25 run in the last 90 days (one-change-per-quarter enforced)
- [ ] All 5 signals scored with real numbers (no guesses)
- [ ] Decision matrix applied — verdict stated in one sentence
- [ ] If refund > 10% → DON'T MOVE verdict; fit-investigation directed
- [ ] If RAISE/LOWER → 3 rules applied (grandfather + pre-announce + one-per-quarter)
- [ ] Announcement email drafted in the correct template
- [ ] Landing-page + social copy generated
- [ ] Section D.6.3 paste block delivered
- [ ] Next review date locked at +90 days
</success_criteria>
