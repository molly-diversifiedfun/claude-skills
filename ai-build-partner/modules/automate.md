<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill maps weekly activities into 4 buckets (Automate / Delegate / Kill / Keep) and picks ONE automation to ship in 7 days. Day 80 of the sprint, after the scaling-lever campaign is locked. Before the Opening, scan:

- **Section D — Phase 8** (T19 Scaling Lever Filter): the 30-day campaign tells you which activities to LEAVE manual on purpose for the next 30 days
- **Section D.12** (Weekly Ship Check log): if total business hours are creeping above 10/wk, Module 6 is broken — re-route to `/unstuck ten-hour-week` first
- **Section D** (any prior T20 entries): killed/parked items from prior cycles

Two branches depending on where the buyer is:

- **Branch A — Setup (Days 73-79):** the audit isn't done yet. Help configure the 7-day audit before the categorization.
- **Branch B — Categorize + pick (Day 80):** audit log in hand. Run the 4-bucket sort + pick THE ONE.

If the buyer arrives without an audit log AND hasn't started one, route to Branch A. Don't run categorization on memory — it underweights "background" activities.

Don't ask what you can read. Pull the locked Lever from D — Phase 8 before asking about categories.

---

**Opening (output verbatim to the buyer):**

> "Time to make the 10-Hour Business Week real. The pattern:
>
> 1. **Log one week of real activity** (Days 73-79) — every operating task, time-stamped
> 2. **Sort into 4 buckets** — 🤖 Automate · 👥 Delegate · 🔪 Kill · ✋ Keep manual on purpose
> 3. **Score automate candidates** on hours-saved ÷ setup-hours
> 4. **Pick THE ONE to ship this week.** Not three. ONE.
>
> **One ground rule:** the Hard Cap is one automation in 7 days. Three at once = three potential breaks, three rollback paths, three places to forget to update env vars. One per week is sustainable. Three is how you take down your Stripe webhook on a Friday afternoon.
>
> Tell me: have you logged a week of audit yet, or are we setting that up?"

---

## Branch A — Audit setup (Days 73-79, before the template runs)

**Step A1 — Set the granularity**

> "Audit-log entries should be specific enough to categorize but coarse enough that you don't quit by Wednesday. The right grain:
> - ✅ '20 min — answered 3 Gumroad refund DMs'
> - ✅ '45 min — wrote Tuesday newsletter draft'
> - ❌ '2 hrs — customer support' (too coarse — can't categorize)
> - ❌ '4 min — re-sent the welcome email to one customer who didn't get it' (too granular — you'll stop logging)
>
> Aim for 15-90 min chunks, with one specific activity per row."

**Step A2 — Pre-list the "background" activities**

These get forgotten because they feel like "just doing my job." Pre-list them so you catch them:

- Reading your inbox while drinking coffee
- Posting on social manually
- Re-sending broken receipts / lost-access links
- Manually applying tags in your ESP
- Updating Notion when product copy changes
- Reading competitor newsletters / "research" rabbit holes
- One-off 1:1 Zooms with prospects who never buy
- Editing your own video clips

Pull from User Context Section A (creator profile) — if the buyer's a designer, pre-list "tweaking design" type activities. If they're an engineer, pre-list "adding logging / refactoring for fun" type activities.

**Step A3 — Midweek check-in prompt**

> "On Wednesday afternoon, paste 'wednesday audit check' into the chat. I'll re-engage and ask you what you've logged + what you forgot."

**Step A4 — The broken-deeper signal**

> "If your audit week totals > 25 hrs of product work, T20 isn't the fix. The 10-Hour Business Week is broken at a deeper level. Re-route to `/unstuck ten-hour-week` to re-architect the operating cadence. T20 trims edges; ten-hour-week resets the spine.
>
> Watch for these signals during the audit week:
> - You're stopping V2 work to do support
> - Your build sessions are eaten by ops
> - You're working weekends to keep the audit week 'normal'
>
> Any of these = stop the audit. Run `/unstuck ten-hour-week` first."

End Branch A. Tell the buyer to return Day 80 with the log.

---

## Branch B — Categorize + pick (Day 80, audit log in hand)

**Step B1 — Pull the locked Scaling Lever**

Read User Context Section D — Phase 8.

> "Your 30-day Lever is: [paste]. Before we categorize, this matters: some activities I'd auto-suggest as 'delegate' or 'automate' are actually load-bearing for this campaign and need to stay manual another 30 days. I'll flag them as 'keep manual — campaign-load-bearing' during categorization. After the 30 days, they re-categorize."

**Step B2 — Categorize each activity**

Walk the buyer through the log row by row. For each:

> "[Activity, hours]. Which bucket?
> - 🤖 **Automate** — repetitive, rule-based, low judgment. Software does it.
> - 👥 **Delegate** — judgment yes, *you* specifically no. A VA / contractor can do it.
> - 🔪 **Kill** — doesn't move the business forward. Stop doing it. World won't end.
> - ✋ **Keep manual** — high-leverage, customer-facing, requires YOU specifically. Automating lowers signal.
> - 🚨 **Campaign-load-bearing** — would normally be Delegate/Automate, but the Step B1 Lever needs it manual for 30 more days."

Push back on rationalization:

- "Reply to every social comment within an hour" → that's Kill, not Keep manual. Comment volume isn't customer signal.
- "Polish landing-page copy" → that's Kill if the page is already shipped. Stop polishing.
- "Read competitor newsletters daily" → Kill. Once a week is enough.
- "Tier-1 'where's my link' replies" → Delegate (eventually), not Keep manual.

Force every activity into one bucket. No "maybe."

**Step B3 — The hidden category check**

Any activity that doesn't fit cleanly is usually carrying weight that shouldn't be in the business. Examples:

- A favor for a friend you said you'd help with months ago
- A "we should also do X" project you started and never finished
- An old feature you keep maintaining that nobody uses

> "Anything in the log that doesn't fit a bucket? Default-move it to Kill unless you can defend why it's Keep manual."

**Step B4 — Score automate candidates**

Among the 🤖 Automate items, score top 3 by hours-returned-per-setup-effort.

| Activity | Hours/wk saved | Setup hrs | Setup cost ($) | Ratio (saved ÷ setup) |
|---|---|---|---|---|

Highest ratio = top candidate by efficiency. But — strategic override allowed.

**Step B5 — Pick THE ONE to ship this week (strategic override allowed)**

> "Top by ratio: [paste]. But — is there a buyer-experience priority that should override? Common overrides:
> - **Day 0 break** (customer doesn't get the welcome email): override; ship that first even if ratio is lower
> - **PMF measurement gap** (you can't measure retention because tracking is broken): override
> - **Compliance / legal** (you're storing data in a way that needs to stop): override
>
> If none of those apply, ship by ratio. Pick: [paste]."

Lock the pick. Cap at ONE.

**Step B6 — 7-day shipping plan**

For the ONE:

- Day-by-day plan (~1 hr/day × 7 days)
- End-of-week verification: how do I know it works?
- Rollback condition: if it breaks, how do I restore manual?

Specific. Not "Day 3: build the thing." Day 3: "Wire the Gumroad → Kit webhook with a single tag rule. Test with one fake purchase. Verify the welcome email lands within 30 seconds."

**Step B7 — Park the rest**

| Automation candidate | Backlog priority (1 = next, 3 = later) | Why deferred |
|---|---|---|

Don't leave automation candidates floating — park them with a priority and a 30-day re-score note.

---

**Step B8 — Output the Automation Map artifact**

```
SECTION D — Phase 8 — T20 Automation Map
Locked: [Date — Day 80]
Source: /unstuck automate
Audit week: [paste]

TOTAL OPERATING HOURS: ___ /wk
(if > 10: re-route to /unstuck ten-hour-week BEFORE this map)

CATEGORIZATION (hours/wk per bucket):
- 🤖 Automate: ___ hrs/wk
- 👥 Delegate (target): ___ hrs/wk
- 🔪 Kill: ___ hrs/wk
- ✋ Keep manual (incl. campaign-load-bearing): ___ hrs/wk

KILLED PERMANENTLY: [paste list]

SHIPPING THIS WEEK (THE ONE): [paste activity]
- Estimated hours/wk returned: ___ starting Day 87
- 7-day plan: [paste day-by-day]
- Rollback condition: [paste]

PARKED BACKLOG:
- Priority 1 (next cycle, Day 110): [paste]
- Priority 2 (cycle-after-next, Day 140): [paste]

NEXT T20 RE-RUN: Day 110 (re-audit, re-categorize)

Built with the Unstuck Method — unstuckwithmolly.com
```

---

**Step B9 — Chain to next module**

- "Automation locked. Day 81 → start the 7-day build. Use `/unstuck weekly` next Sunday to verify scope creep didn't sneak in. Day 87 → confirm the automation works (verification step). Day 110 → re-run `/unstuck automate` with a fresh audit week."

</process>

<success_criteria>
This module is complete when:
- [ ] Audit week logged with specific 15-90 min entries
- [ ] Total operating hours noted (if > 25, re-routed to /unstuck ten-hour-week)
- [ ] All activities sorted into exactly ONE bucket (no "maybe")
- [ ] Campaign-load-bearing activities flagged via Section D — Phase 8 lever lookup
- [ ] Automate candidates scored by ratio (hours saved ÷ setup hrs)
- [ ] THE ONE picked — strategic override applied only if buyer-experience priority justifies it
- [ ] 7-day day-by-day shipping plan locked
- [ ] Rollback condition + end-of-week verification defined
- [ ] Unselected candidates parked with priority + re-score date
- [ ] Section D — Phase 8 paste block delivered
- [ ] Day 110 re-run scheduled
</success_criteria>
