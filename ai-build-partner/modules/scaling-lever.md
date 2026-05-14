<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill diagnoses the funnel bottleneck and picks the ONE scaling lever for the next 30 days. Day 75 (after PMF says SCALE). Before the Opening, scan the user's uploaded User Context file:

- **Section D — Phase 7** (T17 PMF Scorecard): SCALE verdict required. If verdict was ITERATE / PIVOT / KILL, route to the appropriate module (`/unstuck v1.1` / `/unstuck discovery`) instead.
- **Section B** (project + audience): customer count, revenue, audience size
- **Section D — Phase 8** (prior lever cycles, if any): which levers have been pulled, what worked, what didn't

If PMF verdict was anything other than SCALE, push back:

> "T17 PMF said ITERATE / PIVOT / KILL — not SCALE. Pulling a scaling lever before PMF is the classic founder mistake: you scale leaky-bucket churn, not a working product. Run `/unstuck v1.1` first if ITERATE, or `/unstuck discovery` if PIVOT/KILL. Want to override and proceed anyway? Tell me why."

Don't ask what you can read. Anchor funnel numbers before asking for diagnostics.

---

**Opening (output verbatim to the buyer):**

> "T17 said SCALE. Now we pick the ONE lever for the next 30 days. Five possible levers, one bottleneck — and the lever that matches the bottleneck isn't the one you're best at.
>
> The flow:
> 1. **Funnel diagnostic** — 4 questions, one bottleneck named in one sentence
> 2. **Score the 5 levers** — bottleneck match × leverage multiplier × can-I-actually-pull-this
> 3. **Anti-pattern check** — does your highest-scored lever match your professional comfort zone? If yes, force a re-examination
> 4. **30-day campaign plan** — for the winning lever, with a success metric locked before you start
>
> **One ground rule:** the lever you're best at ≠ the lever to pull if it's not your bottleneck. Marketers default to Traffic. Engineers default to Retention. PMs default to Pricing. I'm going to call out the comfort-zone pull every time.
>
> Ready?"

---

**Step 1 — Funnel diagnostic (4 questions, sequential)**

Ask one at a time.

**Q1: What does your funnel actually look like (last 30 days, real numbers)?**

| Stage | Number |
|---|---|
| Awareness (impressions / visits / mentions) | ___ |
| Interested (email signups / free-trial starts / installs) | ___ |
| First purchase (paying customers) | ___ |
| Retained at Day 30 | ___ |
| Referring (unsolicited shares + referred signups) | ___ |

Compute the conversion rates between stages. Don't ask the buyer to compute — do it yourself.

**Q2: Where does the funnel drop most steeply?**

Based on Q1, identify the steepest drop. One of:

- Awareness → Interested = **Traffic / messaging gap**
- Interested → First purchase = **Conversion gap**
- First purchase → Retained = **Retention gap**
- Retained → Referring = **Spread / referral gap**

State the gap in one sentence. Don't hedge.

**Q3: Where does revenue concentrate?**

Ask: "Plot your customer revenue — power-law (top 10% = 50%+ of revenue), flat (evenly spread), or inverted (long-tail of low-price, no top tier)?"

- Power-law → pricing/packaging gap (whales who'd pay more)
- Flat → pricing roughly right, scale = more customers
- Inverted → pricing ceiling gap (upsell tier missing)

**Q4: Dominant complaint/compliment in last 20 customer interactions?**

Ask: "Read your last 20 customer DMs / support replies / podcast mentions. Which theme repeats most?"

- "It's great but I wish it did X" → breadth gap
- "It's exactly what I needed" → scale existing surface
- "I'd pay more if it also did Y" → pricing gap
- "How do I tell my friends?" / "What's your referral link?" → spread gap

---

**Step 2 — Reconcile and name the bottleneck**

Synthesize Q2 (funnel drop) + Q3 (revenue shape) + Q4 (dominant theme).

If all three point at the same bottleneck: "Your gap is [X → Y]." High confidence.

If they point at different bottlenecks: "Two competing bottlenecks: [A] and [B]. Q2 says [A]; Q4 says [B]. Pick one to attack first."

Push the buyer to pick. Multi-front campaigns produce unattributable results.

---

**Step 3 — Score the 5 levers (1–5 each)**

For each lever:

| Lever | What it does | Best when bottleneck is |
|---|---|---|
| **Traffic / acquisition** | More eyeballs at top of funnel | Awareness → Interested gap |
| **Conversion** | More purchasers from existing traffic | Interested → First purchase gap |
| **Retention** | Existing customers come back / stay / expand | First purchase → Retained gap |
| **Pricing / packaging** | Same customers, more revenue per customer | Power-law revenue OR "I'd pay more for Y" |
| **Spread / referral** | Happy customers recruit new ones | Retained → Referring gap OR "how do I tell my friends" |

Three scores per lever:

- **Bottleneck match (1–5):** 5 = directly fixes diagnosed bottleneck. 1 = irrelevant.
- **Leverage multiplier (1–5):** 5 = compounding return (referral loop that runs itself). 1 = linear (one-time ad spend).
- **Can-I-actually-pull-this (1–5):** 5 = skill + time + data + budget. 1 = aspirational.

Multiply for total. Highest score wins.

| Lever | Bottleneck match | Leverage | Can-pull | Total |
|---|---|---|---|---|
| Traffic | | | | |
| Conversion | | | | |
| Retention | | | | |
| Pricing | | | | |
| Spread | | | | |

Push back on "Can-I-actually-pull-this" generosity — are they claiming they can do something they haven't done before?

---

**Step 4 — Anti-pattern check (load-bearing)**

Before locking the lever:

> 🚨 **The lever you're best at ≠ the lever to pull if it's not your bottleneck.**

Ask: "What's your professional background — marketer / engineer / PM / sales / designer / founder / other?"

| Background | Default lever | Often-missed bottleneck |
|---|---|---|
| Marketer | Traffic | Conversion or Retention |
| Engineer | Retention (better product) | Conversion or Spread |
| PM | Pricing / packaging | Spread / referral |
| Sales | Conversion | Pricing or Retention |
| Designer | Conversion (better LP) | Traffic or Spread |

If the buyer's highest-scored lever matches their default → force a re-examination:

> "Your top lever is [X], which happens to be your professional comfort zone. Walk me through Q2 (funnel drop) and Q4 (customer theme) again — did you score honestly, or did you score where you want to spend the next 30 days? If the bottleneck genuinely is [X], proceed. If you'd score differently as a [different background], we re-pick."

If the highest score does NOT match the default → proceed. Honest scoring.

---

**Step 5 — Lock the lever + design the 30-day campaign**

For the winning lever, output the 30-day campaign plan:

**Traffic / acquisition:**
- Top channel (pick ONE: paid ads / content / partnerships / PR / SEO)
- Daily / weekly cadence
- End-of-30-day awareness target
- Marketing OS skills: `funnel-ad-creator`, `viral-hook-generator`, `instagram-reels-framework`, `build-content-repurposing-pipeline`

**Conversion:**
- Biggest landing-page weakness from your funnel data
- A/B test OR rewrite (pick ONE)
- Marketing OS skills: `funnel-landing-page-designer`, `build-conversion-sales-letter`, `generate-faq-from-objections`, `audit-design-tells`

**Retention:**
- Day-7 or Day-30 churn signal you're targeting
- Onboarding fix vs. ongoing-engagement fix (pick ONE)
- Marketing OS skills: `design-onboarding-sequence`, `build-email-story-engine`, `build-win-back-system`

**Pricing / packaging:**
- The packaging change (price raise / tier addition / bundle / annual option)
- Grandfathering plan: which existing customers get the old price, who pays the new
- Marketing OS skills: `design-pricing-architecture`, `design-offer-ladder`, `build-irresistible-offer`

**Spread / referral:**
- Referral mechanic (cash incentive / double-sided benefit / public recognition / native virality)
- Marketing OS skills: `build-referral-engine`, `create-tag-based-funnel-system`

---

**Step 6 — Lock the success metric BEFORE the campaign starts**

Pre-commit the number. After 30 days, this is how you know whether the lever worked.

> "What number, by Day 105, says this lever worked? Be specific — '+30% conversion rate Interested → First purchase' beats 'more sales.' Write it down before you start."

If the buyer can't name a specific metric → push:

> "If you can't define the success metric, you can't tell if the campaign worked. Pick one: [3 candidate metrics for the chosen lever, with realistic 30-day deltas]."

Lock the metric. Add to artifact.

---

**Step 7 — Output the Scaling Lever artifact**

```
SECTION D — Phase 8 — T19 Scaling Lever Filter
Locked: [Date — Day 75]
Source: /unstuck scaling-lever
Cycle: [first / second / third]

FUNNEL DIAGNOSTIC:
- Awareness: ___
- Interested: ___
- First purchase: ___
- Retained Day 30: ___
- Referring: ___
- Steepest drop: [stage]
- Revenue shape: [power-law / flat / inverted]
- Dominant theme: [paste]

DIAGNOSED BOTTLENECK: [one sentence]

LEVER SCORING:
- Traffic: __ × __ × __ = __
- Conversion: __ × __ × __ = __
- Retention: __ × __ × __ = __
- Pricing: __ × __ × __ = __
- Spread: __ × __ × __ = __

ANTI-PATTERN CHECK: [background] · default lever = [X] · winner = [Y] · re-examined? [yes/no]

WINNING LEVER: [paste]

30-DAY CAMPAIGN:
- Channel / mechanic: [paste]
- Cadence: [paste]
- Marketing OS skills used: [2-4 from the list]

SUCCESS METRIC (locked before campaign):
- [specific number] by Day 105

RE-SCORE DATE: Day 105 (re-run /unstuck scaling-lever)

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step 8 — Chain to next module**

- "Lever locked. Day 80 → run `/unstuck automate` (T20) to figure out what to automate so the campaign doesn't break your 10-hour week. Day 105 → re-run `/unstuck scaling-lever` to check the metric and pick the next lever. Meanwhile: `/unstuck weekly` every Sunday to keep the campaign honest."

</process>

<success_criteria>
This module is complete when:
- [ ] PMF SCALE verdict confirmed (or override reason logged)
- [ ] Funnel diagnostic complete (4 questions, conversion rates computed)
- [ ] Bottleneck named in one sentence
- [ ] All 5 levers scored (bottleneck match × leverage × can-pull)
- [ ] Anti-pattern check applied — comfort-zone lever flagged if matched
- [ ] Winning lever locked
- [ ] 30-day campaign plan drafted with channel + cadence + Marketing OS skill picks
- [ ] Success metric pre-committed (specific number, Day 105 target)
- [ ] Section D — Phase 8 paste block delivered
- [ ] Re-score date locked at Day 105
</success_criteria>
