<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill walks the demand-risk-primary smoke test: pre-commit thresholds, stand up the test, read the data against the locked thresholds. Day 10 of Module 2 (Scope) on the alternate path. Before the Opening, scan the user's uploaded User Context file:

- **Section B** (project + audience): product type, audience size, audience-driving channels
- **Section D.1** (T04 Validation Scorecard): if this gave 5+ paying-intent signals, the buyer is build-risk-primary, not demand-risk-primary — push back and route to Module 3 instead
- **Section D.2** (T05 One-Page Scope): hypothesis to test

If Section D.1 shows 5+ paying-intent signals already, push back:

> "Your Validation Scorecard already gave you 5+ paying-intent signals. You're build-risk-primary, not demand-risk-primary. T16/smoke-test is for the case where the biggest unknown is 'will anyone pay,' not 'can I build it.' Want to run smoke-test anyway, or jump to `/unstuck sprint` (Module 3)?"

Marketing OS detection: if loaded, `funnel-landing-page-designer` (Cialdini Pre-Suasion + landing-page architecture) is the right paid skill for Option A's smoke-test page. Note the deferral inline.

Don't ask what you can read. Anchor product type + audience size before asking thresholds.

---

**Opening (output verbatim to the buyer):**

> "Smoke-test time. Before you commit 10 days of build, we're testing whether real money moves at your proposed price. Three phases:
>
> 1. **Pre-commit your thresholds in writing** — PASS / PIVOT / KILL, locked BEFORE the test starts
> 2. **Stand up one smoke-test option** (waitlist / Stripe-intent / discovery-call / pre-order)
> 3. **Read results against the locked thresholds** — no retroactive softening
>
> **One ground rule:** the pre-commit is the most important step. After data lands, you will rationalize any number as 'promising.' Writing the threshold down before — with a witness, ideally — is what makes the test honest.
>
> Ready?"

---

**Step 1 — Pre-commit thresholds (BEFORE the test, Day 10)**

Ask:

> "Pick your product type:
> - **B2B / paid product** (selling to companies or professionals)
> - **B2C / freemium or paid app** (consumer product)
> - **Course / cohort** (paid education)
> - **Service / productized consulting** (your time, packaged)
> - **Other** (define your own thresholds)"

Output the default-threshold table for the picked type:

| Product type | PASS (enter Module 3) | PIVOT (re-scope) | KILL (return to Module 0) |
|---|---|---|---|
| B2B / paid | ≥ 3 Stripe-intent or pre-orders from non-friends, OR ≥ 10 qualified waitlist with price-ack | 1–2 Stripe-intent OR 4–9 waitlist | 0 Stripe-intent AND < 4 waitlist |
| B2C / freemium or paid | ≥ 30 waitlist in 5 days OR ≥ 5% conversion from cold visits | 15–29 waitlist OR 2–4% conversion | < 15 waitlist AND < 2% conversion |
| Course / cohort | ≥ 3 deposits or stated intent-to-pay at full price | 1–2 deposits | 0 deposits |
| Service / consulting | ≥ 2 booked discovery calls from cold prospects (not friends) | 1 discovery call | 0 discovery calls |

Then ask:

> "Now scale to YOUR audience. Defaults assume a generic audience size. What's your reachable audience for this test — newsletter / IG / LinkedIn / network total?"

If audience < 200: scale numbers down (≥ 1 Stripe-intent = PASS for B2B, etc.). If audience > 5K: scale numbers up. State the math:

> "At your audience size (___), I'd recommend PASS = ___, PIVOT = ___, KILL = ___. Reasoning: [one line]."

Lock the thresholds. Output them as a one-paragraph statement the buyer pastes into their journal:

```
PRE-COMMITTED SMOKE-TEST THRESHOLDS — locked [Date]
Product: [paste]
Product type: [paste]
Audience size: ~___

On Day 15, if the test shows [PASS number], I will enter Module 3 (Build).
If the test shows [PIVOT number], I will re-scope and re-run the smoke test ONCE.
If the test shows [KILL number] or worse, I will return to Module 0 with documented learnings.

Signed: [Date]
```

This is the artifact. Don't move on until it's pasted into the buyer's journal/User Context.

---

**Step 2 — Pick the smoke-test option (Day 10, ~2 hrs to set up)**

Ask:

> "Pick ONE option — don't run two simultaneously, signals get noisy:
>
> - **Option A — Landing page + Stripe intent.** Best for: paid products with a clear price, audience that converts from cold traffic. Build the landing page (use T11 or `/unstuck landing-page`), add Pre-order button → Stripe Checkout (intent only, no charge until you confirm), drive traffic for 5 days. Measure: payment intent + conversion rate.
>
> - **Option B — Waitlist with price acknowledgment.** Best for: products where you want signal without taking money yet. One-section landing page with offer + price stated. Waitlist form requires email + checkbox: *'I understand the launch price will be $X and I'd plan to buy.'* Measure: signups WITH the checkbox.
>
> - **Option C — Booked discovery call (service products only).** Best for: services priced > $500 where the buyer needs a conversation. One-section page describing engagement + price range + calendar link. Measure: booked calls from non-friends.
>
> - **Option D — Pre-order with full charge + refund guarantee.** Best for: high-conviction sellers. Charge in full at signup with public refund guarantee. Strongest demand signal. Use only if confident you'll ship within 30 days.
>
> Which option fits your product type and risk tolerance?"

Map to product type + audience: B2B/Course → A or D. B2C → A or B. Service → C. If the buyer's pick contradicts the obvious match for their product type, push back once.

Marketing OS callout: "If Marketing OS is loaded, fire `funnel-landing-page-designer` for the smoke-test page architecture (Cialdini Pre-Suasion + privileged-moments framing). If not, use `/unstuck landing-page` for the 8-section frame."

---

**Step 3 — Run the test (5 days, ~0 hrs of buyer time)**

Tell the buyer:

> "Drive traffic. Don't fiddle with the landing page mid-test — you'll contaminate the signal. Just watch. Log daily."

Give them the daily log template:

| Day | Visits | Conversions / signups | Cumulative |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

End the session here. Tell the buyer:

> "Come back on Day 15 with the daily log + total signal count. Don't read results before Day 15 — partial-day reads make you panic-tune the page and you lose the controlled test."

---

**Step 4 — Read results against pre-committed thresholds (Day 15)**

When the buyer returns:

> "Paste your daily log + total signal. I'll match against the threshold you pre-committed on Day 10."

Read the numbers cold. Compare to the LOCKED threshold from Step 1. No softening allowed:

- Matches PASS → **PASS verdict.** Module 3 next.
- Matches PIVOT → **PIVOT verdict.** Re-scope and re-run ONCE.
- Matches KILL → **KILL verdict.** Module 0 with documented learnings.

If the buyer pushes back ("but it was almost the PASS number, can we count it?"), push back harder:

> "The threshold was [X]. The signal is [Y]. The whole point of pre-committing was to prevent retroactive softening when results land. The data is the data. Honor it."

---

**Step 5 — Decision branches**

**If PASS → Module 3:**

> "Demand validated. Enter Module 3. Run `/unstuck sprint` next to set up the 10-day build sprint. Your smoke-test landing page becomes the V1 landing-page seed — don't throw it away."

**If PIVOT → re-scope:**

> "Product is close but not landing. Pivot ONE lever:
> - **Price** (try ±20% — sometimes pivot = wrong price)
> - **Audience** (tighter niche)
> - **Deliverable** (smaller V1 within same problem space)
>
> Pick ONE. Re-run T05 The One-Page Scope with the adjusted hypothesis. Then re-run `/unstuck smoke-test` with new thresholds. ONE pivot attempt — if it fails again, KILL."

**If KILL → Module 0:**

> "No demand at proposed price. Write the kill memo:
> - What was the actual learning? [one paragraph]
> - What would have to change for this candidate to come back? [audience access / technical capability / market shift]
>
> Return to Module 0. Run `/unstuck discovery` for the next candidate. Killing on purpose at Day 15 beats limping for 6 months on a no-demand idea."

---

**Step 6 — Output the Smoke-Test artifact**

```
SECTION D — Phase 2 — T16 Smoke-Test Decision
Locked: [Date — Day 15]
Source: /unstuck smoke-test

PRE-COMMITTED THRESHOLDS (locked Day 10):
- Product type: [paste]
- PASS: [paste]
- PIVOT: [paste]
- KILL: [paste]

SMOKE-TEST RUN:
- Option chosen: [A / B / C / D]
- Traffic driven: ___ visits over 5 days
- Signal count: ___ [stripe-intent / waitlist with price-ack / booked calls / pre-orders]
- Conversion rate: ___ % (if applicable)

VERDICT: [PASS / PIVOT / KILL]

DAY 16 FIRST ACTION: [paste]

LEARNINGS (if PIVOT or KILL): [paste — what would change for the candidate to come back]

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step 7 — Chain to next module**

- PASS → "`/unstuck sprint` for the Module 3 10-Day Sprint Plan. Smoke-test page becomes V1 landing-page seed."
- PIVOT → "`/unstuck scope` to re-scope with the pivoted lever. Then re-run `/unstuck smoke-test` with new thresholds. ONE more pivot allowed."
- KILL → "`/unstuck discovery` for the next candidate. Write the kill memo first."

</process>

<success_criteria>
This module is complete when:
- [ ] Thresholds pre-committed in writing BEFORE the test (signed + dated paragraph in journal/User Context)
- [ ] Smoke-test option picked (one of A/B/C/D) matching product type
- [ ] 5-day daily log filled out
- [ ] Verdict read cold against locked thresholds (no retroactive softening)
- [ ] Decision branch executed (PASS/PIVOT/KILL with appropriate next-module routing)
- [ ] Section D — Phase 2 paste block delivered
- [ ] Kill memo written (if KILL) — what would have to change for the candidate to come back
</success_criteria>
