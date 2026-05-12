<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: ten_hour_business_week, infrastructure_as_lifestyle, daily_build_protocol)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section B.1** (project + audience), **Section D.5** (T08 Sprint Plan), **Section D.6** (T15 Weekly Ship Check) if present.
- If the user has post-launch evidence (paying customers, traffic, support inbox), DRAFT their 10-Hour Operating Plan: pull current weekly hours from `Section B.2` (T02 Time Protection), audit which work blocks are still earning vs. just running, and propose a 10-hour redistribution across **maintenance / marketing / next-build / kill-list**. Present the draft + ask the user to refine.
- If User Context shows the user is still pre-launch, route them back to `/unstuck sprint` or `/unstuck launch` — don't run this module yet.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "You shipped. Real customers, real money, real metrics in the inbox. Now the interesting question — how does this run forever without you burning out or quietly abandoning it?
>
> The 10-Hour Operating Mode is the answer. You'll redistribute your weekly hours across four buckets so V1 keeps running, V2 starts building, and you stay sane.
>
> **One ground rule:** if any question feels too abstract, three ways out:
> - Type **`hint`** — another worked example
> - Type **`guide me`** — I'll interview you to the answer
> - Type **`draft it`** — paste what you have, I'll polish
>
> Ready?"

If the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

**Step 1: Where you are now**

**What we're capturing:** A 60-second post-launch state-of-the-business — what V1 actually did, what V1 still needs.

"What's V1 looking like 1–4 weeks after launch? Customers, revenue, support load, any feedback patterns?"

**Example of a 5/5 answer:**
> "Junior PM Career Compass shipped June 13 with 11 paying customers at $497. By week 3 post-launch: 9 still active in the Slack, 2 ghosted. $5,467 total. Two patterns from the cohort sessions — (1) Module 1 felt too theoretical, three people asked for more concrete first-week-in-role examples; (2) the 1:1s I included are eating ~2 hrs each (budgeted 30 min). Otherwise: clean."

The 5/5 has: customer count, revenue, retention signal, top 1–2 feedback patterns, time leaks.

---

**Step 2: Your hour budget**

**What we're locking:** A real weekly hour budget for ongoing work. Push back hard on "as many as it takes."

"How many hours per week can you commit to this thing, post-launch, sustainably, without resentment? Pretend your future self has to honor this every week for 12 months."

**Example of a 5/5 answer:**
> "10 hours. Tuesdays 7–9pm (2 hrs), Saturdays 9am–noon (3 hrs), Sundays 4–6pm (2 hrs), plus 3 hrs slack for support / weekly check. Day job is unchanged. Anything above 10 = I'm robbing my partner, my dog, or my sleep."

Push back on "15 to 20 hours" — that's not sustainable, it's launch-week energy creep. The 10-Hour week is the canonical Molly number; deviate only if the buyer has hard evidence of slack capacity (sabbatical, sold company, etc.).

---

**Step 3: The four-bucket split**

**What we're producing:** Your hours allocated to **Maintenance / Marketing / Next-build / Kill-list**, each with a percentage cap.

Walk them through allocating their 10 hours:
- **Maintenance (target 20%, ~2 hrs)** — customer support, infrastructure ops, bug fixes, the things V1 needs to keep working.
- **Marketing (target 30%, ~3 hrs)** — ongoing content, newsletter, social, customer-acquisition motion.
- **Next-build (target 40%, ~4 hrs)** — V2 of this product OR a new product entirely. The compounding asset.
- **Kill-list (target 10%, ~1 hr)** — reviewing what's actually working vs. running on inertia. Closing things deliberately.

**Example of a 5/5 split (Aamir, week 4 post-launch):**
> | Bucket | Hours | Tasks |
> |---|---|---|
> | Maintenance | 2 hrs | Slack support, Stripe reconciliation, refund handling |
> | Marketing | 3 hrs | 1 LinkedIn post/week + 1 newsletter every 2 weeks |
> | Next-build | 4 hrs | Module 1 v2 rewrite (concrete examples), validating Cohort 2 demand via DMs |
> | Kill-list | 1 hr | Tracking: is the 1:1 still worth 2 hrs each? At what cohort size do I drop the 1:1 entirely? |

Push back if any bucket exceeds 50% of total hours — that's a sign of unbalanced operating, usually a leak from a pre-launch habit that didn't get retired.

---

**Step 4: The kill-list**

**What we're surfacing:** What you're going to STOP doing now that V1 is done. The hardest part of sustainable operating is killing what's no longer earning its keep.

"What are you currently doing that was useful pre-launch but is now overhead?"

**Example of a 5/5 kill-list (Aamir):**
> 1. Daily check-ins on the build sprint Telegram bot — kill, no longer relevant
> 2. The Validation Scorecard re-run every Sunday — kill, V1 is validated, this was sprint-mode habit
> 3. Hand-coded cohort invites — automate via Calendly + Stripe webhook, save 30 min/week
> 4. Reading every comment on every social post — kill, sample weekly instead

Push for at least 3 specific things. Generic "I should stop being so reactive" doesn't count. Name the thing + the verb.

---

**Step 5: The next-product question**

**What we're locking:** A decision frame for V2 vs. new-product.

"Is the next 4 hours of next-build time going to V2 of this product, or to a NEW product? Or are you not sure yet?"

**Decision framework:**
- **V2** — V1 has clear traction (>10 paying customers, retention signal, 5+ feature requests with overlapping pain), AND the marginal customer is in the same audience.
- **New product** — V1 sold ok but the audience exhaust signal is real (you've already messaged all the buyers you know), OR you've lost personal energy for the V1 topic.
- **Not sure yet** — Run `/unstuck validate` on 2–3 next-product ideas before committing. Don't drift.

**Example of a 5/5 answer:**
> "V2. Three of the 11 buyers DM'd asking 'do you have a follow-on cohort for senior→staff prep?' That's an unmissable signal. Module 1 rewrite + new Cohort 2 V2 with a 'Strategy → Staff Promo' track. Same audience. New advanced offering."

---

**Step 6: Park downhill — Monday morning, week 1 of operating mode**

**What we're producing:** A concrete first-action that starts the new operating rhythm.

"What's the exact thing you'll do Monday morning, week 1, that locks in the 10-Hour Operating Mode?"

**Example of a 5/5 answer:**
> "Monday June 22, 9:00am. Open the new Notion 'Ops Week' page. Time-block all 10 hours on calendar through end-of-year — Tuesday 7–9, Sat 9–12, Sun 4–6. Send Slack message to cohort: 'V2 starts Tuesday — Module 1 is being rewritten. New cohort coming. Want a preview?' Park downhill: have one DM thread open with Priya, ask her if she's a yes on Cohort 2."

The 5/5 answer has: exact day + time, specific action, named human or artifact, park-downhill note for tomorrow.

---

**Step 7: Present the 10-Hour Operating Plan**

Use the template at `templates/ten-hour-operating-plan.md` (or build the artifact in-message if template missing). The plan includes:
- Current state (week N post-launch, customers, revenue, top patterns)
- Hour budget (total + by-day)
- 4-bucket allocation with named tasks per bucket
- Kill list (3+ items, verb + specific)
- Next-product decision (V2 vs. new vs. validate-3)
- Monday morning first-action with park-downhill

Hand the buyer a clean paste-ready block for User Context Section G (Operating Mode).

---

**Step 8: Chain to next module**

- If they chose V2 → recommend `/unstuck scope` to lock V2's V1.
- If they chose new product → recommend `/unstuck discovery` (Path 1 or Path 4 depending on audience state).
- If they chose validate-3 → recommend `/unstuck validate` on each candidate.

</process>

<success_criteria>
This module is complete when:
- [ ] Post-launch state captured (customers, revenue, patterns)
- [ ] Sustainable weekly hour budget locked (default 10 hrs)
- [ ] 4-bucket allocation done (Maintenance / Marketing / Next-build / Kill-list)
- [ ] Kill list has 3+ specific items
- [ ] Next-product decision made (V2 / new / validate-3)
- [ ] Monday morning first-action set (day + time + verb + park-downhill)
- [ ] 10-Hour Operating Plan artifact delivered
- [ ] Next module recommended
</success_criteria>
