<required_reading>
**Read these reference files NOW:**
1. references/core.md
</required_reading>

<process>

**Step 0 — Context check**

This module is called FROM `/unstuck outreach` (warm path). It helps users name and contextualize the people they already know who have the problem their toy solves.

Read `.unstuck/context.md`:
- **Section C.3** (one-liner) — needed to know what problem to filter for
- **Section C.5** (audience) ��� the target buyer description

→ Next: **Opening**

---

**Opening (output verbatim to the buyer):**

> "Let's name the people. Not 'my LinkedIn network' — specific humans you could text right now who have the problem your toy solves.
>
> Think: coworkers, ex-colleagues, people who've DMed you, people you've seen post about this problem, people in your communities who complain about this."

→ Next: **Step 1** — mine their network.

---

**Step 1: Mining prompts**

Ask these one at a time until they hit 10+ names:

1. "Who at your current or past companies has this problem?"
2. "Who's DMed or emailed you about something related to this?"
3. "Who have you seen post about this problem on social media?"
4. "Who in your Slack/Discord communities talks about this?"
5. "Who have you mentored or helped with this informally?"
6. "Who would you text right now to say 'I made a thing — try it'?"

After each answer, capture names and one line of context. Keep pushing until they have 10+.

**If they stall at 3-9:** "That's a start. For the rest, we'll use cold discovery — finding strangers with the problem. But these [N] are your foundation."

**If they truly can't name anyone:** Route to `/unstuck cold-discovery`. Their audience isn't in their network — it's in communities.

→ Next: **Step 2** — contextualize each name.

---

**Step 2: Add context per person**

**What we're producing:** A list with enough context to personalize outreach.

For each name, capture:
- How you know them
- Why THEY specifically have this problem
- Best channel to reach them (DM, email, text, LinkedIn)

**Example of a 5/5 warm list:**
> | # | Name | Connection | Why them | Channel |
> |---|---|---|---|---|
> | 1 | Aamir Khan | Ex-coworker at Stripe | Complained about spec writing in a 1:1 | Slack DM |
> | 2 | Priya Sharma | Lenny's Slack | Replied to my post asking for a template | Slack DM |
> | 3 | Marcus Chen | LinkedIn | Comments on every PM post I write | LinkedIn DM |
> | 4 | Jen Park | Conference 2025 | Said "tell me when you build this" | Text |
> | ... | ... | ... | ... | ... |

→ Next: **Step 3** — save and return to outreach.

---

**Step 3: Save + update context**

Save to `.unstuck/warm-list-<YYYY-MM-DD>.md` using the Write tool. Include the full table.

Update `.unstuck/context.md`:
- **D.7:** Warm list — [N] named humans, channels identified. See `.unstuck/warm-list-<date>.md` for full list.

**Return to `/unstuck outreach`** — this module is a sub-step, not a standalone endpoint. The outreach module uses this list to draft personalized messages.

</process>

<success_criteria>
This module is complete when:
- [ ] 10+ names surfaced (or clear signal that cold-discovery is needed)
- [ ] One line of context per person (connection + why them + channel)
- [ ] Artifact saved to `.unstuck/warm-list-<date>.md`
- [ ] Context updated (D.7)
- [ ] Returns to outreach flow
</success_criteria>
