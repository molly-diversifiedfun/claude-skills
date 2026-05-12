<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill is hours-aware AND context-heavy. Before the Opening, scan the user's uploaded User Context file:
- Read **Section B.1** (project + audience), **Section D.1** (warm list from `/unstuck warm-list` or Module 1 validation), **Section D.2** (One-Page Scope), **Section D.3** (Pricing)
- If Section D.1 is populated (warm list with names + context + pre-sold signals), DRAFT all 20 DMs directly without asking. Present the batch + ask the user to spot-check 2–3 for voice + edit before sending.
- If Section D.1 is empty, route the buyer to `/unstuck warm-list` first. Don't generate DMs to abstract categories — generic DMs are spam, not warm launch.

Don't ask what you can read. Draft what you can infer.

---

**Opening (output verbatim to the buyer):**

> "We're going to draft your Day 26 warm-launch DMs as a batch. Each one personalized to the specific human, referencing their exact pain in their own words, ending with a low-pressure CTA.
>
> Normally this is 2–3 hours of writing. With your warm list + product context loaded, it's a 2-minute draft + 30 minutes of editing for voice.
>
> **One ground rule:** if any draft sounds off — too generic, too salesy, wrong tone for that specific human — flag it. I'll regenerate just that one rather than tweak the whole batch."

---

**Step 1 — Confirm the batch parameters**

Pull from User Context. Confirm with the buyer:
- Warm list count (Section D.1) — should be 10–20 humans
- Product name + one-sentence outcome (Section B.1)
- Price (Section D.3)
- Launch date (Section B.1 or D.6 if launch plan exists)
- Buyer's voice / register (Section A or kit-files/02-voice-dna.md)
- Channels per person (DM, email, LinkedIn message, text)

If anything's missing, ask once:

> "Quick check — your warm list has [N] humans. Product is [product name] at \$[price], launching [date]. Voice is [Molly's register / buyer's voice if Marketing OS loaded with brand-voice-router]. Channels per person from your list. Confirm or correct?"

---

**Step 2 — Draft the batch (one DM per human)**

For each person in the warm list, generate ONE DM following this structure:

**Structure (4 lines max, ~80 words per DM):**

1. **Hook (1 line):** personal acknowledgment — reference the specific pain they expressed OR the moment they expressed interest. Use their exact words where available.
2. **Bridge (1 line):** "I built the thing." One sentence about what you shipped. Plain language. No "excited to announce."
3. **Offer (1 line):** What it is + price + link. Direct.
4. **Out (1 line):** Low-pressure exit. "No pressure to buy — but [secondary ask: feedback / share / curiosity]."

**Example of a 5/5 DM (for Aamir Khan, who said "send me the beta" on Day 14):**

> "Aamir — remember when you said 'send me the beta' for the strategy work thing? It's live.
>
> The Junior PM Career Compass — 5-week paid cohort + workbook for PMs who want to do real strategy work, not JIRA grooming. Doors close Friday June 13.
>
> Cohort 1 is \$497 (price-test discount). Stripe link: [URL].
>
> No pressure to buy — but if it resonates, you're the first I told. Honest feedback would mean more than the sale."

**Example for Priya Sharma (newsletter reply, paid Lenny's premium):**

> "Priya — you replied to my newsletter a few weeks back asking when this would exist. Today's that day.
>
> Junior PM Career Compass: live 5-week cohort + workbook, modeled after the framework I shared in the post.
>
> \$497 launch price (cheaper than Lenny's premium for a reason — first cohort I'm running). Link: [URL].
>
> No ask — if it's not for you, send to one junior PM in your life who'd want it. I'd be grateful."

**Per-DM personalization rules:**
- Reference the specific moment / quote / pain — never generic
- Adjust tone per channel (DM = casual, email = slightly more formal, LinkedIn = professional-casual)
- Adjust the Out per buyer relationship (closer = more honest ask for feedback; further = share-friendly)
- Never use "Hope you're well" / "Excited to share" / "Just wanted to reach out" — the buyer's voice should be direct

---

**Step 3 — Present the batch + voice check**

Output all DMs in a single message, numbered, with each person's context noted at the top of their block:

```
DM #1 — Aamir Khan (Datadog PM, said 'send me the beta' on Day 14)
Channel: Twitter DM

[draft]

---

DM #2 — Priya Sharma (Vercel PM, newsletter reply 2026-05-01, paid Lenny's premium)
Channel: Email

[draft]

---

DM #3 — ...
```

After the batch, ask:

> "Voice check: read DMs #1, #5, and #10 (random sample). Do they sound like you, or do they sound like a generic launch broadcast? If any feel off — too salesy, wrong register, generic phrasing — call out which one and I'll regenerate. If they pass voice check, edit any specifics (name typos, dates, links) and send. Recommended pace: 5 per day across Days 26–28 so responses don't pile up all at once."

---

**Step 4 — Spot-fix loop**

If the buyer flags a specific DM:
- Regenerate that ONE — don't redo the batch
- Ask what specifically was off (too salesy / wrong voice / generic / wrong context)
- Apply the correction to JUST that DM
- Surface the fix so they can spot it in future regenerations

---

**Step 5 — Output to User Context Section D.6 (T15 Weekly Ship Check feeds this)**

After the buyer confirms the batch is ready:

```
SECTION D.6 — Day 26 Warm Launch DM Batch
Locked: [Date]
Source: /unstuck dm-personalizer

DMs ready to send: [N]
Sending pace: 5/day across Days 26-28 (track responses + adjust pace)
Channels: [breakdown — e.g., 8 Twitter DM, 5 Email, 7 LinkedIn]
First send: [Day 26, time]

Response tracker:
- DM #1 Aamir — sent [date/time] — response: [pending/yes/no/share]
- DM #2 Priya — sent [date/time] — response: [pending/yes/no/share]
- ...
```

---

**Step 6 — Chain to next module**

- "Day 26 done. Send the first batch (5 DMs) today. Track responses in Section D.6. Tomorrow Day 27 → write your Ship Announcement public post. Run `/unstuck ship-announcement` (or use Marketing OS `viral-hook-generator` + `build-conversion-sales-letter`) to draft it."

</process>

<success_criteria>
This module is complete when:
- [ ] User Context Section D.1 was populated (warm list locked); if not, routed to `/unstuck warm-list`
- [ ] Batch of [N] DMs drafted, one per warm-list human
- [ ] Each DM has 4 lines: Hook (their exact words) / Bridge (you built it) / Offer (price + link) / Out (low-pressure)
- [ ] Voice check passed on 3-sample (or buyer-flagged DMs regenerated)
- [ ] Section D.6 paste block delivered with response tracker
- [ ] Day 27 next-module recommendation given
</success_criteria>
