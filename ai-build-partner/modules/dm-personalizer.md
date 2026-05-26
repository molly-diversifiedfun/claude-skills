<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

This skill is hours-aware AND context-heavy. Before the Opening, read `.unstuck/context.md`:
- Read **Section B.1** (project + audience), **Section D.1** (warm list from `/unstuck warm-list` or Module 1 validation), **Section D.2** (One-Page Scope), **Section D.3** (Pricing)
- If Section D.1 is populated (warm list with names + context + pre-sold signals), DRAFT all 20 DMs directly without asking. Present the batch + ask the user to spot-check 2–3 for voice + edit before sending.
- If Section D.1 is empty, route the buyer to `/unstuck warm-list` first. Don't generate DMs to abstract categories — generic DMs are spam, not warm launch.

Don't ask what you can read. Draft what you can infer.

→ Next: **Step 1** — confirm batch parameters (warm list count, product, price, date, voice, channels).

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

→ Next: **Step 2** — draft one personalized DM per warm-list human.

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

→ Next: **Step 3** — present the full batch for voice check.

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

→ Next: **Step 4** — spot-fix any flagged DMs.

---

**Step 4 — Spot-fix loop**

If the buyer flags a specific DM:
- Regenerate that ONE — don't redo the batch
- Ask what specifically was off (too salesy / wrong voice / generic / wrong context)
- Apply the correction to JUST that DM
- Surface the fix so they can spot it in future regenerations

→ Next: **Step 5** — save the DM batch artifact.

---

**Step 5 — Save the DM batch artifact**

<mcp_actions>
**With Gmail MCP detected:**
- OFFER: "Want me to create Gmail drafts for the email-channel DMs? You review and hit send."
- If yes → `create_draft` for each DM where Channel = Email:
  - To: [email from warm list]
  - Subject: [personalized — pull from Hook line, e.g. "Re: the spec writing thing"]
  - Body: [the drafted DM from Step 2]
- **NEVER auto-send.** Always drafts. The buyer reviews and sends.
- For DM-channel messages (Twitter DM, LinkedIn): skip Gmail draft, keep in artifact only
**Without Gmail MCP:** paste-ready DMs in the artifact (default path below)
</mcp_actions>

After the buyer confirms the batch is ready, save the artifact to `.unstuck/dm-personalizer-YYYY-MM-DD.md` via the Write tool.

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

→ Next: **Step 6** — update context with DM batch status.

---

**Step 6 — Update context**

Read `.unstuck/context.md`. Append to Section D:

```
D.11 — Personalized DMs
Status: drafted
Artifact: .unstuck/dm-personalizer-YYYY-MM-DD.md
DMs ready: [N]
Sending pace: 5/day across Days 26-28
```

Save the updated context via the Write tool.

→ Next: **Step 7** — exit to Ship Announcement module.

---

**Step 7 — Exit**

Output verbatim:

> **Module complete: DM Personalizer**
> Artifact saved: `.unstuck/dm-personalizer-YYYY-MM-DD.md`
> Context updated: `.unstuck/context.md` Section D.11
>
> **What to do now:** DMs are drafted and ready. Don't send yet — launch-day ops will tier them and set the timeline.
>
> **Next module:** `/unstuck launch-day` — hour-by-hour launch ops: pre-launch checklist, DM tiering, response playbook, silence protocol.
> **When to run it:** The night before or morning of launch day.
↩ Come back to `/unstuck dm-personalizer` when: launching a new product and need fresh personalized DMs.

</process>

<success_criteria>
This module is complete when:
- [ ] User Context Section D.1 was populated (warm list locked); if not, routed to `/unstuck warm-list`
- [ ] Batch of [N] DMs drafted, one per warm-list human
- [ ] Each DM has 4 lines: Hook (their exact words) / Bridge (you built it) / Offer (price + link) / Out (low-pressure)
- [ ] Voice check passed on 3-sample (or buyer-flagged DMs regenerated)
- [ ] Artifact saved to `.unstuck/dm-personalizer-YYYY-MM-DD.md`
- [ ] `.unstuck/context.md` updated with D.11 DM batch status
- [ ] Exit block delivered with next-module recommendation (`/unstuck ship-announcement`)
</success_criteria>
