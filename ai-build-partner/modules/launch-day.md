<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/mcp-actions.md (for Calendar + Gmail enhanced actions)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This module runs on LAUNCH DAY (or the night before). Everything upstream should be done. Before the Opening, read `.unstuck/context.md`:

- **Section B.1** (product + audience + ship date): confirm today IS launch day (or tomorrow)
- **Section D.3** (T06 Pricing): locked price — used in checkout test
- **Section D.6** (Launch Plan): the ONE ACTION — what someone does when this works, and the first person by name. Since `/unstuck launch` moved onto the five, D.6 holds a behaviour rather than a sales number, and the behaviour is the better signal: "Priya replies about work" tells you more on the day than "eight signups".
- **Section D.7** (warm list): the humans getting DMs today
- **Section D.8** (landing page): the URL going live
- **Section D.9** (launch emails): the sequence that fires today
- **Section D.11** (personalized DMs): the batch ready to send

**Readiness check (BLOCKING).** Scan for missing prerequisites:

| Prerequisite | Where to check | If missing |
|---|---|---|
| Landing page live + checkout working | D.8 + manual check | STOP. Run `/unstuck landing-page` first. |
| Price locked | D.3 | STOP. Run `/unstuck pricing` first. |
| DMs drafted | D.11 | Not blocking — can draft today. Run `/unstuck dm-personalizer` inline. |
| Email sequence armed | D.9 | Not blocking — can send manually. Note the gap. |
| The one action set | D.6 | Not blocking — set it now (Step 1). |

If landing page OR price is missing, DO NOT proceed. Route back. Everything else can be patched on the fly.

If all prerequisites are met, DRAFT the full launch-day timeline (Step 2) from context and present it. Ask the buyer to confirm or adjust. Skip the question-by-question intake.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "Launch day. Not the plan — the day itself.
>
> In the next 20 minutes we'll lock: a pre-launch checklist you run before anything goes live, an hour-by-hour timeline for today, a response playbook for every kind of message you'll get, and a silence protocol for when nothing happens (it will feel like nothing is happening even when it's working).
>
> **One ground rule:** you're going to want to refresh the page every 3 minutes. I'm going to give you specific check-in times instead. Between those times, you do something else. Watching the numbers doesn't move them.
>
> Ready?"

---

**Step 1 — Pre-launch checklist (run BEFORE anything goes live)**

Walk through each item. Don't skip. Every item that fails gets fixed NOW, not after you've sent 10 DMs to a broken checkout.

> "Run through these with me. Yes/no for each."

**The checklist:**

- [ ] **Checkout test:** Open your checkout link in an incognito window. Can you reach the payment page? Does the price match what you locked? If Stripe: do a $1 test purchase (refund yourself after). If Gumroad: verify the product page renders correctly.
- [ ] **Delivery test:** After your test purchase, did you receive what the buyer receives? PDF downloaded? Email arrived? Course access granted? Login works? If you can't test delivery, fix it before going live.
- [ ] **Landing page loads:** Open the URL in incognito. Does it load in under 3 seconds? Is the CTA button visible without scrolling? Does the checkout link from the CTA work?
- [ ] **Email sequence armed:** If you have a launch-day email queued, is it scheduled? Correct send time? Correct segment? Preview it one more time.
- [ ] **DMs ready to send:** Are your personalized DMs from `/unstuck dm-personalizer` in your drafts (Gmail or copy-paste)? If not, we'll draft them in Step 3.
- [ ] **Announcement posts ready:** Are your platform announcements from `/unstuck ship-announcement` drafted? If not, we'll use them in the timeline.
- [ ] **The one action remembered:** "I'll know today worked if ___." Pull the one action from D.6. If not set: "Name it now. What does ONE person have to DO in the first 48 hours for this to have worked?" Take a behaviour, and take a number only if they give one - a first subscriber, member, reader or reply counts the same as a first customer.

**If checkout or delivery fails:** STOP. Fix it. Do not send a single DM until the purchase flow works end to end. Sending people to a broken checkout is worse than launching a day late.

**If everything passes:**

> "Checkout works. Delivery works. Page loads. You're clear to go live. Here's your timeline."

→ Next: **Step 2** — the hour-by-hour launch timeline.

---

**Step 2 — The launch-day timeline**

Draft a timeline anchored to the buyer's actual schedule. Pull build-block times from Section A / F.1 if available. Adapt to their timezone and day-job constraints.

**Default timeline (adjust per buyer's reality):**

> **T-1 hour (before anything goes live):**
> - Run the pre-launch checklist above (if not already done)
> - Put phone on Do Not Disturb EXCEPT for DM notifications from warm list
> - Close all non-launch tabs. You need: landing page, checkout dashboard, email/DM app, this conversation
>
> **T+0 — Go live:**
> - Landing page is public (flip the switch if it was unlisted)
> - Send the first 5 personalized DMs (your closest warm-list contacts — the ones who said "send me the beta" or "I'd buy that")
> - DO NOT post the public announcement yet. Warm list gets a head start.
>
> **T+1 hour — Second wave:**
> - Send the next 5 DMs
> - Check your checkout dashboard: any purchases? Any abandoned carts?
> - If someone replied to a DM: respond immediately. Warm, personal, not salesy. Answer their question, link the checkout if they ask.
> - If no one replied yet: NORMAL. DMs take 2-8 hours to get read. Do not panic.
>
> **T+2 hours — Public announcement:**
> - Post your announcement on your primary platform (LinkedIn, Twitter, Instagram — whichever has your audience). One platform first, not all at once.
> - If your email sequence is armed, trigger it now (or confirm it fired on schedule).
>
> **T+3 hours — Second platform:**
> - Post on your second platform (if applicable)
> - Check DM responses. Reply to every one — even "congrats" gets a "thank you, means a lot" back.
>
> **T+4-6 hours — The quiet zone:**
> - This is where most launchers spiral. The DMs are sent. The posts are up. Now... silence.
> - **DO SOMETHING ELSE.** Go for a walk. Do your day job. Cook dinner. The numbers will be there when you come back.
> - Set ONE check-in alarm: 6 hours after your first DM. That's your next look.
>
> **T+6 hours — Evening check-in:**
> - Check: DM responses, sales count, email opens (if available), comments on announcement posts
> - Reply to EVERY response (DMs, comments, emails). The day-1 buyers are your ambassadors. Treat them like it.
> - If you have sales: screenshot it. You'll want this for the testimonial ask in 7 days.
> - If you have zero sales but DM responses: that's signal. Read Step 5 (the response playbook).
> - If you have zero sales and zero responses: read Step 6 (the silence protocol).
>
> **T+24 hours — Day 2 morning:**
> - Send remaining DMs (if you didn't send all on Day 1)
> - Post on any remaining platforms
> - Reply to overnight messages
> - If you have a "last chance" or "doors closing" trigger: schedule it for Day 3 or Day 5 (not Day 2 — too early)
>
> **T+48 hours — Score:**
> - Run Step 7 (the 48-hour assessment)

Customize this timeline based on:
- **Day job:** If launching on a workday, shift DMs to morning (before work) and announcement to lunch break. Evening check-in stays.
- **Timezone:** If warm list spans timezones, send West Coast DMs 3 hours after East Coast.
- **Product type:** Courses/cohorts with a close date → add urgency language. Evergreen → no artificial urgency.

→ Next: **Step 3** — DM sending order (if not already done).

---

**Step 3 — DM sending order**

If `/unstuck dm-personalizer` already ran, the batch is ready. Help the buyer prioritize the send order.

**Tier the warm list:**

| Tier | Who | When to send | Why first |
|---|---|---|---|
| **Tier 1 — Pre-sold** | People who said "send me the beta" / "I'd buy that" / engaged with your build-in-public posts | T+0 (first 5 DMs) | Highest conversion probability. First sales create momentum. |
| **Tier 2 — Warm** | People who know you + have the problem, but haven't expressed buying intent | T+1 hour (next 5) | Know you, might buy, might share. |
| **Tier 3 — Friendly** | Supporters, friends, colleagues who'd share even if they won't buy | T+2 hours (after public post) | Amplifiers. "Would you share this with anyone who fits?" |

> "Who are your Tier 1 — the 3-5 people most likely to buy today? Name them. Those DMs go first."

If DMs haven't been drafted yet, fire `/unstuck dm-personalizer` inline — the batch can be drafted in 10-15 minutes.

→ Next: **Step 4** — the response playbook.

---

**Step 4 — Response playbook**

Pre-write responses for the 7 messages you'll get today. Draft these NOW so you're not composing under adrenaline.

**Message type 1: "Congrats!"**
> Response: "Thank you — means a lot that you saw it. If you know anyone who [has the problem], send them the link? [URL]"
> Job: turn congratulations into a share.

**Message type 2: "This looks cool, tell me more"**
> Response: "It's [one sentence — your Section 3 answer]. Built it for people who [specific pain]. Want to see the page? [URL]"
> Job: bridge curiosity to the landing page. Don't oversell in the DM.

**Message type 3: "How much?"**
> Response: "$[price]. [One sentence on what's included]. Link: [URL]"
> Job: answer directly. Don't hedge. Don't apologize for the price.

**Message type 4: "I'm interested but [objection]"**
> Common objections + responses:
> - "Too expensive" → "Totally get it. If it's not the right time, no pressure. The page has the full breakdown of what's included if you want to revisit later."
> - "Not sure it's for me" → "Fair. Here's who it's built for: [persona]. If that's not you, no hard feelings."
> - "Can I get a discount?" → "The launch price IS the discount — it goes up after [date/number of sales]. But I won't pressure you."
> Job: be direct, don't chase, don't discount on Day 1.

**Message type 5: "I bought it!"**
> Response: "You just made my day. Check your email — [delivery method]. If anything's confusing in the first 10 minutes, message me directly. I want your first experience to be smooth."
> Job: celebrate + ensure delivery + open the feedback channel.

**Message type 6: "I shared it with [someone]"**
> Response: "That means more than a sale, honestly. Thank you. If they have questions, point them my way."
> Job: reinforce sharing behavior.

**Message type 7: Silence (no response)**
> Response: NOTHING. Do not follow up on Day 1. If still no response by Day 3, one gentle nudge: "Hey — no pressure on the [product] thing. Just wanted to make sure you saw it. Either way, hope you're good."
> Job: patience. Most warm-list DMs get read within 48 hours.

Output all 7 as a paste-ready reference card the buyer can keep open during launch.

→ Next: **Step 5** — the silence protocol.

---

**Step 5 — The silence protocol**

> "The scariest part of launch day isn't rejection. It's silence. Here's what silence actually means at each stage."

**0-2 hours of silence:** NORMAL. DMs haven't been read yet. Your announcement post hasn't been seen by most followers. There is literally nothing to learn from this silence. Do not change anything.

**2-6 hours of silence:** STILL NORMAL. Most people read DMs during breaks or after work. If you sent DMs at 9am, the earliest realistic response window is 12pm-6pm. LinkedIn messages often take 24-48 hours.

**6-12 hours — no responses at all:** Worth a diagnostic, but not a panic:
- Re-read your DMs. Did you actually ask a question they need to answer, or did you just announce? If just announced, they may have read it and bookmarked for later.
- Check if the announcement post got any engagement (likes, comments, shares). Engagement without DM responses = people are seeing it but not ready to act.
- Check your checkout analytics (if available). Visits to the page without purchases = interest but the page isn't converting. Visits = 0 → your links aren't working or nobody clicked.

**24 hours — zero sales, zero responses:** Signal, but not a death sentence:
- Did the DMs land? (Check "seen" status on platforms that show it.)
- Did anyone visit the landing page? (Check analytics if set up.)
- If visits but no sales: the page or the price is the issue, not the product.
- If zero visits: the DMs/posts didn't drive traffic. The distribution is the issue.
- **DO NOT:** slash the price, rewrite the landing page, add features, or send panicked follow-ups. All of those are Day 1 anxiety moves that make things worse.

**48 hours — zero sales:** This is meaningful signal. Run `/unstuck gate` or the 48-hour assessment (Step 7) to diagnose.

→ Next: **Step 6** — emotional management (optional but important).

---

**Step 6 — Emotional management (the real talk)**

> "Launch day anxiety is not a bug — it's universal. Here's what's happening in your brain and what to do about it."

**The refresh trap:** You will want to refresh the checkout dashboard / email / DMs every 90 seconds. Each refresh with no change triggers a micro-disappointment. 30 refreshes in an hour = 30 micro-disappointments = "this is failing" narrative, even if it's 10am and your DMs were sent at 9am.

**The fix:** Set 3 check-in alarms (T+2, T+6, T+24). Between alarms, close the tabs. Not minimize — CLOSE. Do something physical between check-ins: walk, cook, gym, errands. Your body needs to move when your brain is spinning.

**The comparison trap:** You will see someone else's launch post today that got 500 likes. You will feel like your 3 likes is a failure. Their 500 likes is 3 years of audience building. Your 3 likes is your actual audience right now. Both numbers are real. Only yours matters today.

**The premature pivot:** The urge to change something on Day 1 (price, copy, features, audience) is almost always wrong. Day 1 data is noise, not signal. You need 48-72 hours of data before any change is justified. If you feel the urge to pivot, write down what you'd change and why — then wait 48 hours. If the idea still holds, make the change on Day 3.

**The one thing to remember:** You shipped. Most people who start side projects never get here. Whatever happens with sales today, you have a live product that real humans can buy. That's the hardest part, and it's done.

→ Next: **Step 7** — the 48-hour assessment.

---

**Step 7 — The 48-hour assessment**

Run this at T+48 hours. Not before.

> "Two days in. Let's read the scoreboard — not to judge, to diagnose."

**Collect the numbers:**

| Metric | Your number | What it means |
|---|---|---|
| DMs sent | ___ | Distribution effort |
| DM responses | ___ | Message quality + relationship strength |
| Landing page visits | ___ | Traffic from DMs/posts (check analytics if available) |
| Checkout page visits | ___ | Interest level (visitors who clicked the CTA) |
| Purchases | ___ | Conversion |
| Revenue | $___ | The number that matters |
| Announcement engagement | ___ likes/comments | Reach of public posts |
| Shares/forwards | ___ | Organic amplification |

**Read the signal:**

| Pattern | Diagnosis | Next move |
|---|---|---|
| DMs sent, no responses | Messages didn't land OR wrong channel | Nudge Tier 1 on Day 3. Try a different channel for Tier 2. |
| Responses but no page visits | They replied but didn't click | Your DM CTA is weak. Resend with a direct link + one sentence. |
| Page visits but no checkout clicks | Page isn't converting | Landing page problem. Re-read hero + CTA. Run `/unstuck landing-page` to revise. |
| Checkout clicks but no purchases | Price or trust issue | Consider adding a guarantee. Check if checkout flow is confusing. |
| 1-3 purchases | WORKING. Scale distribution. | Send remaining DMs. Post on more platforms. Ask buyers for a testimonial in 7 days. **First-sale moment:** if Section H has no prior revenue, fire the First-Sale celebration from `references/fun.md` + drop **🃏 The Merchant** card. |
| 5+ purchases | Strong signal | You have product-market fit signal for this warm audience. Run `/unstuck cohort-2` to find strangers. Drop **🃏 The Merchant** if not already earned. |
| Zero everything after 48 hours | Distribution or product-market issue | Run `/unstuck gate` with this data. Honest assessment: go / iterate / kill. |

→ Next: **Step 8** — save the artifact.

---

**Step 8 — Save the launch-day artifact**

Save to `.unstuck/launch-day-YYYY-MM-DD.md` via the Write tool.

```
LAUNCH DAY OPS — [Product Name] — [Date]
Source: /unstuck launch-day

PRE-LAUNCH CHECKLIST:
- Checkout tested: [PASS/FAIL]
- Delivery tested: [PASS/FAIL]
- Landing page live: [URL]
- Email sequence armed: [YES/NO]
- DMs ready: [N drafted]
- The one action: [paste from D.6]

TIMELINE (customized):
[paste the buyer's adjusted timeline from Step 2]

DM SEND ORDER:
- Tier 1 (pre-sold): [names]
- Tier 2 (warm): [names]
- Tier 3 (friendly): [names]

RESPONSE PLAYBOOK:
[paste the 7 pre-written responses from Step 4]

CHECK-IN ALARMS: [T+2: time], [T+6: time], [T+24: time]

48-HOUR ASSESSMENT (fill after T+48):
- DMs sent: ___
- Responses: ___
- Page visits: ___
- Purchases: ___
- Revenue: $___
- Diagnosis: ___
- Next move: ___

Built with the Unstuck Method — unstuckwithmolly.com
```

**Context update:** Read `.unstuck/context.md`. Append to Section G:

```
G.1 — Launch Day
Date: [paste]
Status: [launched / in-progress]
Artifact: .unstuck/launch-day-YYYY-MM-DD.md
48-hour result: [pending — fill after assessment]
```

<mcp_actions>
**With Google Calendar MCP detected:**
- OFFER: "Want me to create your 3 check-in alarms as calendar events?"
- If yes → `create_event` for each:
  - T+2: "📊 Launch check-in #1 — check DM responses + checkout dashboard"
  - T+6: "📊 Launch check-in #2 — evening assessment, reply to all messages"
  - T+24: "📊 Launch check-in #3 — Day 2 morning, send remaining DMs"
  - Reminder: 5 min before each
- Also OFFER: "Want me to block a 30-min slot at T+48 for your assessment?"
- If yes → create event: "📊 48-Hour Launch Assessment — run /unstuck launch-day Step 7"

**With Gmail MCP detected:**
- OFFER: "Want me to create your 7 response templates as Gmail drafts so you can copy-paste during the day?"
- If yes → `create_draft` for each of the 7 message types (subject = "Launch Day — [message type]", body = the pre-written response)
- **NEVER auto-send.**

**Without MCP:** paste-ready playbook in the artifact (default path above)
</mcp_actions>

---

**Step 9 — Exit**

> **Module complete: Launch Day Ops**
> Artifact saved: `.unstuck/launch-day-YYYY-MM-DD.md`
> Context updated: `.unstuck/context.md` Section G.1
>
> **What to do now:** Run the timeline. Send Tier 1 DMs. Close the tabs between check-ins. Breathe.
>
> **Next module (at T+48):** Come back and run Step 7 (48-hour assessment) in this same conversation or a new one.
>
> **After the assessment:**
> - Sales coming in → `/unstuck cohort-2` (find strangers)
> - Need to iterate → `/unstuck gate` (go / iterate / kill with real data)
> - Ready to sustain → `/unstuck ten-hour-week` (set operating rhythm)
>
> ↩ Come back to `/unstuck launch-day` when: launching a new product.

</process>

<success_criteria>
This module is complete when:
- [ ] Pre-launch checklist run — checkout + delivery tested and passing
- [ ] Hour-by-hour timeline customized to buyer's schedule and timezone
- [ ] DM send order tiered (pre-sold → warm → friendly)
- [ ] 7 response templates pre-written and ready to paste
- [ ] Silence protocol communicated (0-2hr / 2-6hr / 6-12hr / 24hr / 48hr stages)
- [ ] 3 check-in alarms set (T+2, T+6, T+24)
- [ ] Emotional management addressed (refresh trap, comparison trap, premature pivot)
- [ ] 48-hour assessment framework delivered (fill after T+48)
- [ ] Artifact saved to `.unstuck/launch-day-YYYY-MM-DD.md`
- [ ] `.unstuck/context.md` updated with G.1 launch day status
- [ ] Exit block delivered with branching next-module recommendation
</success_criteria>

<anti_patterns>
**Things this module must NOT do:**

1. Tell the buyer to change price, copy, or features on Day 1. Day 1 data is noise. Changes happen at T+48 earliest.
2. Encourage refreshing dashboards. Set check-in times and enforce them.
3. Generate artificial urgency ("LAST CHANCE!") on Day 1. If there's a real close date, it goes in the timeline. If not, don't manufacture one.
4. Suggest paid ads on launch day. Warm list + organic first. Paid comes after product-market fit signal.
5. Skip the pre-launch checklist. A broken checkout destroys launch-day momentum — fixing it after 10 DMs are sent is worse than launching a day late.
6. Pile on multiple platform posts simultaneously. Stagger by 1-2 hours so you can respond to each wave.
7. Let the buyer send a panicked follow-up DM to someone who hasn't responded in 4 hours. The nudge comes at Day 3, not Hour 4.
</anti_patterns>
