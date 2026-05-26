<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: rice_scoring)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, read `.unstuck/context.md`:
- Check **Section D.1** (hypothesis RICE) — this module REQUIRES a hypothesis to compare against. If D.1 is empty, route to `/unstuck hypothesis` first.
- Check **Section D.7** (warm list) or **Section D.15** (cold discovery channels) — at least one must exist. If both empty, route to `/unstuck outreach` first.
- Count previous kills: search context for `Status: KILLED` entries. If **3+ kills found**, activate serial-kill protocol (see Step 3b).
- Read outreach results: the user should be coming here AFTER showing the toy to people. If no outreach evidence exists, ask: "Have you shown the toy to anyone yet? This module scores real reactions, not plans."

→ Next: **Opening** — frame the gate.

---

**Opening (output verbatim to the buyer):**

> "You showed the toy. Now we score what happened — and decide: keep going, iterate, or kill.
>
> I'll ask you what signals you got back. Then we'll compare reality to your hypothesis and make a call. 
>
> One rule: we score what HAPPENED, not what you HOPED would happen."

→ Next: **Step 1** — collect signals.

---

**Step 1: Collect signals**

**What we're gathering:** Every response from outreach, categorized by signal type.

"Walk me through what happened. For each person you showed the toy to, tell me: who, what they said/did, and how they reacted."

Categorize each response into one of four signal types:

| Signal type | Weight | What counts |
|---|---|---|
| **Money** | 3x | They offered to pay, pre-ordered, sent money, asked "how much?", said "I'd buy this" |
| **Usage** | 2x | They actually tried/used the toy, attended the event, read the chapter, installed the tool |
| **Pull** | 2x | They shared it without being asked, referred someone, starred it on GitHub, asked "can I show my team?" |
| **Trust** | 1x | They signed up, followed, said "cool," RSVPed but didn't show, bookmarked, downloaded but didn't use |

Help them categorize: "When Priya said 'this is exactly what I needed' — did she actually USE the template, or just say nice things?" Usage beats trust.

**Example of a 5/5 signal collection:**
> | Person | Reaction | Signal type |
> |---|---|---|
> | Aamir | Used the template for a real spec, EM loved it | Usage (2x) |
> | Priya | Said "I'd pay for the full course" | Money (3x) |
> | Marcus | Downloaded, no response | Trust (1x) |
> | Jen | Used it, asked "when is the next one?" | Usage (2x) |
> | Dev | Shared with her team Slack without being asked | Pull (2x) |
> | 4 others | No response | (not counted) |

→ Next: **Step 2** — score.

---

**Step 2: Calculate the weighted score**

**What we're producing:** A single number from the signal weights.

Calculate: sum of (each signal × its weight).

**Show the math to the buyer:**

> "Here's your score:
> - Money signals: [N] × 3 = [total]
> - Usage signals: [N] × 2 = [total]
> - Pull signals: [N] × 2 = [total]
> - Trust signals: [N] × 1 = [total]
> - **Weighted total: [sum]**"

**Capping rules for cold/public signals:**
- GitHub stars: cap at 5 pull signals (10 points) regardless of actual count
- Reddit upvotes: cap at 5 pull signals (10 points)
- Social media likes: cap at 3 trust signals (3 points)
- Rationale: these are ambient interest, not committed engagement

→ Next: **Step 3** — the verdict.

---

**Step 3: Verdict**

| Weighted score | Verdict | What happens |
|---|---|---|
| **10+** | **GO** | You have signal. Move to Phase 4. |
| **4-9** | **ITERATE** | Signal exists but isn't strong enough. Try again (max 2 iterations). |
| **0-3** | **KILL** | After genuine effort, not enough signal. Kill or start over. |

**3a — GO verdict (score 10+):**

> "You have [score] points of real signal. [Summarize the strongest signals — name the people, quote what they said.] This is worth building.
>
> **Next step:** Phase 4 — iterate on feedback, set a price, and build V1. You'll need the Ship It Kit (`/unstuck` paid tier) to continue, or you can DIY the next steps."

**3b — ITERATE verdict (score 4-9):**

Check for serial-kill history first.

**If 3+ previous kills (serial-kill protocol):**

> "You scored [score]. Normally this means 'iterate and try again.' But I need to surface something: you've killed [N] ideas before this one. Each one had [range] people who showed interest.
>
> That's not bad ideas — that's a quitting pattern. The signal you got here is NORMAL for a first outreach.
>
> **I'm not letting you kill this one yet.** You get 2 iterations before that's on the table. Here's what to try:"

**Standard iterate (no serial-kill):**

> "You scored [score]. There's something here, but the signal isn't strong enough to bet on yet. You get 2 more attempts before we make the final call.
>
> **Pick ONE to try next:**
> 1. **Different people** — show the toy to a completely different segment. Your warm list might not be the right audience.
> 2. **Different positioning** — same toy, different pitch. Change how you describe what it does.
> 3. **Add one thing** — add ONE feature or piece to the toy that addresses the most common feedback.
>
> Which one? Pick one, execute it, then come back to `/unstuck gate` with the new results."

Track iteration count in context: `gate_iteration: 1` (then `gate_iteration: 2`).

**After 2 iterations, still 4-9:** Force the final decision.

> "Two iterations in. Score: [N] (was [original]). You've made [specific changes]. The signal moved [up/flat/down].
>
> **Decision time — no more iterations:**
> - **GO ANYWAY** — you believe in this despite moderate signal. You accept the risk. Some products need more time to prove out.
> - **KILL** — the signal isn't there. Start over with a new idea.
>
> There's no wrong answer here. But there IS a wrong move: iterating forever without deciding."

**3c — KILL verdict (score 0-3):**

**If serial-kill protocol is active (3+ prior kills) AND score is 1-3:** Do NOT auto-kill. Override to ITERATE:

> "Your score is [N] — normally that's a kill. But you've killed [N] ideas before, and I need you to try ONE more thing before we call it. This is the forced-iteration exception: try a completely different audience segment. If that also scores below 4, then we kill with confidence."

Set `gate_iteration: 1` in context. This gives ONE iteration before the kill is allowed.

**If NO serial-kill protocol (normal user) OR score is literally 0:**

> "You showed the toy to [N] people. [Describe what happened — or didn't.] The signal just isn't there.
>
> This doesn't mean YOU failed. It means this specific idea, for this specific audience, didn't resonate enough to build a business around. That's valuable information — most people never get this clarity.
>
> **Your move:** back to Phase 1. `/unstuck idea-bank` to surface the next idea, or `/unstuck one-liner` if you already have one."

Mark the kill in context: `Status: KILLED — [date]. Score: [N]. Reason: [summary].`

→ Next: **Step 4** — Validation RICE (compare to hypothesis).

---

**Step 4: Validation RICE — compare to hypothesis**

**What we're producing:** A side-by-side comparison of hypothesis vs. reality.

Re-score RICE with real data:

| Dimension | Hypothesis | Validation | Delta |
|---|---|---|---|
| **Reach** | [original] | Actual response rate on outreach | +/- |
| **Impact** | [original] | What they said, how they reacted | +/- |
| **Confidence** | [original] | Real evidence from [N] data points | +/- |
| **Effort** | [original] | You built the toy — actual hours spent | +/- |

**Present the comparison:**

> "Here's how your assumptions held up:
>
> **Reach:** You estimated [X]. Reality: [Y]. [Your reach assumption was right / Your audience is smaller than expected / Your audience is bigger than expected — you found engagement in [unexpected channel].]
>
> **Impact:** You estimated [X]. Reality: [Y]. [People cared more/less than expected. Quote the strongest reaction.]
>
> **Confidence:** You estimated [X]. Reality: [Y]. You now have [N] real data points instead of guesses.
>
> **Effort:** You estimated [X]. Reality: [Y]. The toy took [actual hours]. [On track / harder than expected / easier than expected.]
>
> **Biggest surprise:** [Name the assumption that was most wrong — this is the most valuable learning.]"

→ Next: **Step 5** — save and route.

---

**Step 5: Save artifact + update context**

Save to `.unstuck/gate-<YYYY-MM-DD>.md` using the Write tool. Include:
- Signal collection (every person + reaction + category)
- Weighted score calculation (show the math)
- Verdict (GO / ITERATE / KILL)
- Validation RICE comparison
- If iterate: which option chosen, iteration count
- If kill: kill memo (idea, score, what was tried)

Update `.unstuck/context.md`:
- **D.1:** Replace hypothesis status with: `Validation RICE: R=[X] I=[X] C=[X] E=[X]. Score: [weighted]. Verdict: [GO/ITERATE/KILL]. [Date].`
- If KILL: increment kill_count metadata. Add killed idea to **Section H Graveyard** with cause-of-death line. If this is the FIRST kill, drop **🃏 The Guillotine** card (read `references/fun.md` for card generation). If kill count reaches 5, drop **🃏 The Mortician** card.
- If GO: drop **🃏 The Listener** card (Phase 3 complete — they showed it to 10 people and passed the gate).
- If ITERATE: set gate_iteration count

---

**After completing this module:**

| Verdict | Next module | Why | When |
|---|---|---|---|
| **GO** | Phase 4 begins: `/unstuck prioritize` (Kit) then `/unstuck pricing` (Kit) | Turn signal into a product | Next session |
| **ITERATE** | Re-run outreach, then `/unstuck gate` again | Need more/better signal | After executing the iteration |
| **KILL** | `/unstuck idea-bank` or `/unstuck one-liner` | Start fresh | When ready |

↩ Come back to `/unstuck gate` when: you have new outreach results to score.

</process>

<success_criteria>
This module is complete when:
- [ ] All signals collected and categorized (money/usage/pull/trust)
- [ ] Weighted score calculated and shown
- [ ] Verdict delivered (GO / ITERATE / KILL)
- [ ] Serial-kill detection ran (if applicable)
- [ ] Iterate playbook delivered with specific options (if iterate)
- [ ] Validation RICE compared to hypothesis
- [ ] Artifact saved to `.unstuck/gate-<date>.md`
- [ ] Context updated (D.1 with validation status)
- [ ] Next module recommended per verdict
</success_criteria>
