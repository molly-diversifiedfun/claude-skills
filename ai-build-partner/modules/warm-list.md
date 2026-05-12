<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section B.1** (project + audience) if present
- If Section D.1 already has a warm list saved (from a prior pass or from Module 1 Day 5 validation), DRAFT the surfaced list from context + ask only the missing-quote sub-questions. Don't re-interview.
- If User Context is empty or Section B.1 has only an abstract audience description, run the full 5-question interview below.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "We're going to surface 10–15 humans who would plausibly pay for your product. Named people, not categories. Most builders get stuck here because the prep work says 'list 10 humans' and that triggers the blank-page problem.
>
> We're going to work backwards instead. Five sub-questions. Each surfaces 2–4 candidates. By the last one you'll have 10–15. Then we narrow.
>
> **One ground rule:** if a question makes you draw a blank, three ways out:
> - Type **`hint`** — I'll show another worked example
> - Type **`guide me`** — I'll ask narrower sub-questions to help you find the names
> - Type **`draft it`** — paste what you have so far; I'll fill in archetypes you can match real names to
>
> Ready?"

If the buyer invokes hint / guide me / draft it on any question, fire the corresponding sub-flow from `references/core.md` `<answer_assistance>`.

---

**Step 1 — The 5 surfacing questions (one at a time, wait between each)**

Each question is a *channel* the buyer's network reveals warm humans through. Most builders have all 5 channels active; they just haven't audited any of them deliberately.

### Q1 — The "asked you" channel

"In the last 90 days, who has asked you a question your product would answer? Open your DMs, your email replies, your LinkedIn comments, your Twitter / Threads mentions. Pull the names of anyone whose question maps to your product's outcome."

**Example of a 5/5 answer:**
> "Aamir DMd 'how do I do real strategy work as a junior PM' two weeks ago. Priya replied to my newsletter asking the same thing in different words. Three people in r/ProductManagement asked a variant of it. Marcus (a coworker) asked me about it over coffee."

Push back if the answer is a category ("junior PMs in my Slack") not names. Pin to specific humans.

---

### Q2 — The "talks about it without prompting" channel

"Who in your network has *brought up this problem to you unprompted* in the last 90 days? Not because you asked. They volunteered the pain. They're already evangelizing your product without knowing it exists."

**Example of a 5/5 answer:**
> "My friend Jen (PM at Vercel) has complained to me about backlog grooming three times in 90 days. My cohort-mate from my last bootcamp keeps texting me about junior PM frustrations. There's a guy on my running team — Tom — who's at Sentry and ranted about this for 20 min last month."

These are your strongest signals. People who bring up the pain without prompting are pre-sold.

---

### Q3 — The "buying inferior alternatives" channel

"Who is already paying real money for a worse version of your product? Course subscriptions, coaching, expensive books, mastermind memberships, Substack premium tiers. If they're paying, they have budget AND have already accepted the category."

**Example of a 5/5 answer:**
> "Lenny's Newsletter premium subscribers in my network: at least 4 I can name (Aamir, Priya, Jen, a 5th I'd need to confirm). People who paid for Reforge in the last year: 3 (Marcus + 2 ex-coworkers). One guy bought a $300 PM coaching package in January."

The intersection of (Q1/Q2 named pain) AND (Q3 already paying for inferior alternatives) = your highest-priority Day 26 list.

---

### Q4 — The "you'd be mad if you didn't tell them" channel

"Picture your closest 5 work friends, your closest 5 life friends, and your closest 5 networking contacts in the niche. Of those 15, who would be MAD at you if you launched without telling them?"

**Example of a 5/5 answer:**
> "Mad at me: Jen (best PM friend), Aamir (cohort-mate, has been asking about it), Sara (engineer friend, told her I was building this on Day 1), Marcus, Priya. Five mad-if-not-told humans."

This question surfaces the emotional cost of NOT messaging them. If they'd be mad you didn't tell them, they want to know on Day 26.

---

### Q5 — The "tested it for you" channel

"During your 30-day build, who said something like 'I'd want to try that' or 'tell me when it's ready' or 'I'd buy that today'? Even one casual comment counts. These are the warmest contacts of all — they've already self-identified as a buyer."

**Example of a 5/5 answer:**
> "Sara said 'I'd pay $50 for this if it works' when I described the workbook on Day 8. Aamir said 'send me the beta' on Day 14. Priya offered to be a friend-test on Day 22. Marcus said 'launch this and I'll share it' twice."

These are your Day 25 friend-test list AND your Day 26 first DMs.

---

**Step 2 — Synthesize + dedupe**

Take the names surfaced across Q1–Q5. Most appear in multiple questions (that's signal). Compile into a single list:

```
Compiled warm list (post-dedupe, in priority order):
1. [Name] — surfaced via Q1, Q2, Q5 (highest signal: asked AND volunteered AND offered to test)
2. [Name] — surfaced via Q2, Q3 (volunteered pain AND paying for alternatives)
3. [Name] — surfaced via Q1, Q4 (asked + would be mad)
...
```

Aim for 10–15. If fewer than 5, the buyer has a real audience problem — surface it honestly:

> "You named [N] humans across 5 channels. Below 5 is the gate Welcome warned about. Three options: (1) pick a different project where your audience is tighter, (2) spend 30 days building audience before starting the 30-day Ship It System, (3) start anyway, expect first sale from one of these [N] humans, and use Day 28 cold launch aggressively."

---

**Step 3 — Output to User Context Section D.1 (paste-ready)**

```
SECTION D.1 — Warm List (surfaced via /unstuck warm-list)
Locked: [Date]
Source: 5-question surfacing interview

| # | Name | Context | Channels | Pre-sold signal |
|---|---|---|---|---|
| 1 | Aamir Khan | Junior PM at Datadog, DMd 2026-04-28 | Q1, Q2, Q5 | "send me the beta" |
| 2 | Priya Sharma | PM at Vercel, newsletter reply 2026-05-01 | Q1, Q3 | Paid Lenny's premium |
| ... | ... | ... | ... | ... |
| 10 | Tom (last name?) | Sentry, running team, ranted 2026-04-20 | Q2 | Volunteered pain |

Pre-launch use:
- Day 25 evening — email these humans the landing page, get pre-launch feedback
- Day 26 — these are your warm-launch DM list (combine with Module 1 validation list)
- Day 27 — these humans amplify your Ship Announcement post
```

---

**Step 4 — Chain to next module**

- If the buyer is at Pre-Day 1: "Save this to your User Context, then run `/unstuck diagnose` (T01 Readiness Audit) and `/unstuck audit` (T02 Time Protection Plan) to close the rest of the prep gates."
- If the buyer is at Day 26 (mid-launch): "Open `/unstuck launch` to fire the personalized DM batch using this list."
- If the buyer surfaced fewer than 5 names: "We have an audience problem. Run `/unstuck discovery` Path 4 (Audience-First) to either pick a tighter project OR map 30 days of audience-building before starting the sprint."

</process>

<success_criteria>
This module is complete when:
- [ ] All 5 surfacing questions answered with named humans (not categories)
- [ ] At least 10 unique humans across the compiled list
- [ ] Each human has context (their relationship to the buyer) + at least one channel + a pre-sold signal where available
- [ ] Pasted into User Context Section D.1
- [ ] Next-module recommendation given (chain to diagnose / audit / launch / discovery)
</success_criteria>
