<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Check User Context first**

This module is called FROM `/unstuck outreach` when the user can't name 10 people. It can also be run standalone if the user explicitly asks for help finding their audience.

Read `.unstuck/context.md`:
- **Section C.3** (one-liner) — REQUIRED. We need to know who the audience is.
- **Section C.3** format — product type helps determine where the audience hangs out.
- **Section E.1** (toy) — ideal. Having a toy to reference makes community posts more concrete.

→ Next: **Step 1** — identify the audience's watering holes.

---

**Step 1: Where does your audience actually hang out?**

**What we're producing:** 3-5 specific communities where the target audience gathers and talks about the problem the toy solves.

"Your audience isn't in your contact list. Let's find where they congregate. Based on your one-liner, here are my guesses — tell me which feel right and what I'm missing."

**Draft community suggestions based on product type + audience:**

| Audience type | Likely watering holes |
|---|---|
| Software engineers | HN, r/programming, r/[language], dev Discord servers, relevant GitHub discussions |
| Product managers | Lenny's Slack, r/ProductManagement, Product School Slack, Mind the Product |
| Designers | Dribbble, r/UI_Design, Figma Community, design Twitter/Threads |
| Indie hackers / builders | Indie Hackers forum, r/SideProject, r/Entrepreneur, Ship 30 for 30 |
| Creators / writers | Substack Notes, Twitter writing circles, r/writing, specific niche Substacks |
| Niche hobbyists | r/[hobby] (r/MechanicalKeyboards, r/audiophile, r/homelab, etc.), niche Discord servers |
| Career changers | Blind, Levels.fyi discussions, r/cscareerquestions, niche LinkedIn groups |
| Parents / wellness | Facebook groups (still the #1 community platform for non-tech audiences), IG hashtag communities |

"Which 3 of these feel right? And are there any I'm missing — communities you lurk in where your audience already talks about this problem?"

→ Next: **Step 2** — assess each community.

---

**Step 2: Assess the communities**

**What we're evaluating:** Is this community a good place to show a toy — or will you get ignored/banned?

For each community, assess:

| Factor | What to check |
|---|---|
| **Size** | How many active members? (>500 for meaningful signal) |
| **Norms** | Do they allow self-promo? Show-and-tell? Feedback requests? Read the rules. |
| **Activity** | Is the community alive? Posts in the last week? |
| **Relevance** | Do people talk about the PROBLEM your toy solves (not just the topic)? |

**Example of a 5/5 community assessment:**
> | Community | Size | Norms | Fit |
> |---|---|---|---|
> | r/SideProject | 120K | Self-promo OK, feedback posts welcomed | High — exactly our audience |
> | Indie Hackers | 80K | "Show IH" section exists for this | High |
> | r/webdev | 2M | Self-promo banned in posts, OK in weekly threads | Medium — only weekly thread |

**Cut any community where:**
- Self-promo is banned and there's no feedback thread
- The community is dead (<10 posts/week)
- The audience doesn't match (too broad or wrong niche)

Lock 3 communities. More than 3 = scattered effort.

→ Next: **Step 3** — plan the entry.

---

**Step 3: Plan the entry**

**What we're producing:** A specific plan for each community — what to post, when, and how to engage authentically.

**Rule: participate before you post.** Spend 15-30 minutes reading the community, upvoting/commenting on others' posts, understanding the tone. Then post.

For each community, draft:
1. **Pre-post engagement** (1-2 days): comment on 3-5 existing posts. Be helpful. Build a tiny reputation.
2. **The post** (Day 2-3): Share the toy as a feedback request, not a launch announcement.
3. **Follow-up** (Day 4-5): Reply to every comment. DM anyone who expressed strong interest.

**Example of a 5/5 cold discovery post:**
> "I made a free [toy description] for [audience]. It does [one thing]. Looking for 10 people to try it and tell me what's missing. [Link — free, no signup]. What would you add?"

**Tone calibration by platform:**
- **Reddit:** casual, self-deprecating OK, "I made this dumb thing" plays well
- **Indie Hackers:** builder-to-builder, progress framing, "here's what I learned building this"
- **Twitter/Threads:** concise, visual, thread or single post with image/GIF
- **Discord:** conversational, ask in the right channel, don't DM people unprompted
- **LinkedIn:** professional but human, "I've been working on something" framing

→ Next: **Step 4** — define pull signals to track.

---

**Step 4: Define pull signals**

**What we're tracking:** Inbound interest that you didn't push for. These are the strongest signals.

| Pull signal | Weight in kill gate | How to track |
|---|---|---|
| Someone shared your post without being asked | 2x (pull) | Check shares/reposts/cross-posts |
| Someone DM'd you asking for more | 2x (pull) | Track DMs |
| Someone filed an issue or PR (dev tools) | 2x (pull) | GitHub notifications |
| GitHub stars | 2x (pull), capped at 5 signals | Star count |
| Someone tagged a friend in the comments | 2x (pull) | Comment monitoring |
| Upvotes / likes | 1x (trust), capped at 5 | Post analytics |
| Comments that say "cool" without trying it | 1x (trust) | Comment monitoring |

"Set up a simple tracker — I'll give you the format. Check it daily."

```
| Day | Community | Post link | Upvotes | Comments | DMs | Shares | People who TRIED it |
|---|---|---|---|---|---|---|---|
| Day 1 | r/SideProject | [link] | 0 | 0 | 0 | 0 | 0 |
```

→ Next: **Step 5** — save and route.

---

**Step 5: Save artifact + update context**

Save to `.unstuck/cold-discovery-<YYYY-MM-DD>.md` using the Write tool. Include:
- 3 communities selected (with assessment)
- Entry plan per community (pre-post, post, follow-up)
- Post drafts
- Pull signal tracker (empty template)

Update `.unstuck/context.md`:
- **D.15:** Cold discovery channels — [3 communities], strategy: [summary], target: 10+ signals by [date]

---

**After completing this module:**

This module feeds back into `/unstuck outreach` (the cold portion). After posting and collecting responses for 5-7 days, run `/unstuck gate` to score the signal.

↩ Come back to `/unstuck cold-discovery` when: you need to find new audiences (cohort-2 in Phase 5) or your warm list is exhausted.

</process>

<success_criteria>
This module is complete when:
- [ ] 3 communities identified and assessed
- [ ] Entry plan created per community (pre-post + post + follow-up)
- [ ] Post drafts written and tone-calibrated
- [ ] Pull signal tracker created
- [ ] Artifact saved to `.unstuck/cold-discovery-<date>.md`
- [ ] Context updated (D.15)
- [ ] Feeds back into outreach → gate flow
</success_criteria>
