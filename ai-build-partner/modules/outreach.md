<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, read `.unstuck/context.md`:
- Check **Section E.1** (toy definition) — this module REQUIRES a toy to show. If E.1 is empty, route to `/unstuck toy` first.
- Check **Section C.3** (one-liner) — used in outreach messages.
- Check **Section A** (who they are) — personalizes the outreach tone.

→ Next: **Opening** — frame the outreach.

---

**Opening (output verbatim to the buyer):**

> "Your toy exists. Now we find 10 people to show it to.
>
> The goal: show, don't pitch. You're not selling — you're asking 'what do you think?' The toy does the talking. You collect the reactions.
>
> First question: can you name 10 people who have the problem your toy solves?"

→ Next: **Step 1** — route warm vs. cold.

---

**Step 1: Route warm vs. cold**

Wait for their answer. Then route:

| Their answer | Path | What happens |
|---|---|---|
| Names 10+ people | **Warm path** — proceed to Step 2 | They have a network. Use it. |
| Names 3-9 people | **Warm + Cold hybrid** — Step 2 for the names they have, then Step 3 for cold discovery to fill the gap | Partial network. Supplement. |
| "I can't name anyone" / names 0-2 | **Cold path** — skip to Step 3 | No network for this problem. Find strangers. |

→ Next: **Step 2** (warm) or **Step 3** (cold), per routing.

---

**Step 2: Warm path — name and contextualize**

**What we're producing:** A list of 10+ named humans with one line of context each.

"For each person, tell me: their name, how you know them, and why THEY specifically have this problem."

**Example of a 5/5 warm list:**
> | # | Name | Connection | Why them |
> |---|---|---|---|
> | 1 | Aamir | Former coworker, DM'd about spec writing | Complained about PRDs nobody reads |
> | 2 | Priya | Lenny's Slack, replied to my post | Asked for a spec template |
> | 3 | Marcus | LinkedIn connection, comments on my PM posts | New PM at a Series B, struggling with stakeholders |
> | ... | ... | ... | ... |

If they can only name 3-9, capture those and move to Step 3 for the rest.

→ Next: **Step 3** (if cold/hybrid needed) or **Step 4** (if 10+ warm).

---

**Step 3: Cold discovery — find strangers with the problem**

**What we're producing:** 3 communities/channels where the target audience hangs out + a plan to show the toy there.

"Your audience isn't in your contact list — we need to find them in the wild. Let's identify 3 places where people with this problem gather."

Help them brainstorm based on their product type:

| Product type | Likely communities |
|---|---|
| PM / tech course | Lenny's Slack, r/ProductManagement, Product School community, Twitter PM circles |
| Dev tool | r/commandline, r/programming, Hacker News (Show HN), relevant GitHub topics |
| Design templates | r/SideProject, Indie Hackers, Dribbble, Twitter design community |
| Community / membership | LinkedIn groups, existing Slack communities in the niche, conference alumni |
| Newsletter | Twitter, Substack Notes, relevant subreddits |
| Physical product | r/[niche] (r/MechanicalKeyboards, r/audiophile, etc.), Instagram, niche Discord servers |
| Ebook | LinkedIn, relevant Substack/newsletter communities, professional Slack groups |

**Example of a 5/5 cold discovery plan:**
> | # | Community | Size | Entry strategy |
> |---|---|---|---|
> | 1 | r/SideProject | 120K members | Post build log + link to toy, ask for feedback |
> | 2 | Indie Hackers forum | 80K members | Post in "Show IH" section |
> | 3 | ADHD Tech Discord | 200 members | Share in #projects channel, ask for testers |

**Cold outreach rules (NOT spam):**
- Participate in the community BEFORE posting your toy (at least read the norms)
- Frame as "I made this, want feedback" — not "check out my product"
- Give value first: share the toy for free, ask for honest reactions
- Don't post in 3 communities the same day — space it out (1 per day)

→ Next: **Step 4** — draft outreach messages.

---

**Step 4: Draft outreach messages**

**What we're producing:** Personalized messages for warm contacts + a post template for cold communities.

**Warm outreach template (customize per person, ~100 words):**

Structure:
1. **Personal reference** (1 line) — why you're reaching out to THEM
2. **The toy** (1 line) — what you made
3. **The ask** (1 line) — "would you try it and tell me what you think?"
4. **Low pressure** (1 line) — "no pitch, just want honest feedback"

**Example:**
> "Hey Aamir — you mentioned spec writing being painful a few weeks back. I made a one-page spec framework as a Notion template + Loom walkthrough. Would you try it this week and tell me if it's useful? Not selling anything — just want to know if this is worth building out."

Draft ALL warm messages in batch. Present them for the buyer to edit.

**Cold post template (customize per community):**

> "[I built/made] a [toy description] for [audience]. It [does one thing]. Looking for 10 people to try it and give honest feedback — free, obviously. [Link]. What would you add?"

**Example for r/SideProject:**
> "I made a free Figma landing page template for indie hackers — one page, 2 color schemes, full auto-layout. Looking for 10 people to try it and tell me what's missing. Gumroad link (free): [link]. What would you add?"

→ Next: **Step 5** — set the timeline and tracking.

---

**Step 5: Timeline + tracking**

**What we're locking:** When to send, how to track, when to score.

> "**Pacing:** Send warm messages today. Post to first cold community tomorrow. Second community Day 3. Third Day 4.
>
> **Track responses** in this format:"

```
| # | Name/Source | Sent | Response | Signal type | Notes |
|---|---|---|---|---|---|
| 1 | Aamir (warm) | Day 1 | Used it, loved it | Usage | "This is exactly what I needed" |
| 2 | r/SideProject (cold) | Day 2 | 23 upvotes, 3 DMs | Pull + Trust | ... |
```

> "**Score day:** Run `/unstuck gate` after 5-7 days (or when you have 10+ responses, whichever comes first)."

→ Next: **Step 6** — save and route.

---

**Step 6: Save artifact + update context**

Save to `.unstuck/outreach-<YYYY-MM-DD>.md` using the Write tool. Include:
- Warm list (names + context)
- Cold communities (if applicable)
- All drafted messages (warm + cold)
- Response tracker table (empty, for them to fill)
- Timeline

<mcp_actions>
**With Gmail MCP detected:**
- OFFER: "Want me to create these as Gmail drafts? You review and hit send."
- If yes → `create_draft` for each warm outreach message:
  - To: [email if known from warm list context — leave blank if DM/LinkedIn only]
  - Subject: [personalized subject derived from the personal reference line]
  - Body: [the drafted message from Step 4]
- **NEVER auto-send.** Always drafts. The buyer reviews and sends.
- For DM-channel messages (Twitter, LinkedIn): skip Gmail draft, keep in artifact only
**Without Gmail MCP:** paste-ready messages in the artifact (default path above)
</mcp_actions>

Update `.unstuck/context.md`:
- **D.5:** Outreach plan — [N warm + N cold communities], target 10+ responses by [date]
- **D.7:** Warm list (names) — if not already populated
- **D.15:** Cold discovery channels (if applicable)

---

**After completing this module:**

**→ Kill Gate (`/unstuck kill-gate`)**
After 5-7 days of collecting responses, score the signal and decide: go, iterate, or kill.
Run it: when you have 10+ responses OR after 7 days (whichever comes first).

↩ Come back to `/unstuck outreach` when: you need to reach more people (iteration from kill gate) or expand to new channels.

</process>

<success_criteria>
This module is complete when:
- [ ] Warm/cold routing determined
- [ ] 10+ outreach targets identified (warm, cold, or hybrid)
- [ ] All warm messages drafted and personalized
- [ ] Cold community posts drafted (if applicable)
- [ ] Response tracker created
- [ ] Timeline set (send dates + score date)
- [ ] Artifact saved to `.unstuck/outreach-<date>.md`
- [ ] Context updated (D.5, D.7, D.15)
- [ ] Next module recommended (gate)
</success_criteria>
