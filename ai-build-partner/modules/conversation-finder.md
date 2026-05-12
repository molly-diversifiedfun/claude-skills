<required_reading>
**Read these reference files NOW:**
1. references/core.md
2. references/frameworks.md (sections: rice_scoring, ten_conversation_method)
</required_reading>

<process>

**Step 0 — Check User Context first (Mode 1 behavior)**

Before the Opening, scan the user's uploaded User Context file:
- Read **Section B.1** (project + audience + pain/product hypothesis), **Section D.0** (outreach batch + responses tracker if present)
- If the buyer has been tracking conversation transcripts elsewhere (Notion, Google Doc, voice memo folder), ask once for paste-in or link.

This is a pattern-recognition skill, not an interview skill. Buyer provides the raw transcripts; AI surfaces the patterns.

---

**Opening (output verbatim to the buyer):**

> "You ran 7–10 customer conversations. Paste the raw notes / transcripts / voice memo snippets below — one person per block, separated by `---`. Don't summarize yet. Raw is better.
>
> I'll surface:
> - Top 3 pain quotes (verbatim, in their words)
> - Willingness-to-pay signals (who would buy, at what price, with what conviction)
> - Repeated language patterns (the words that show up across multiple conversations)
> - The Kill / Pivot / Go verdict with evidence
>
> 20 minutes instead of 90. Paste when ready."

---

**Step 1 — Receive the transcripts**

Wait for the buyer to paste. Accept any format:
- Live call notes (typed during call)
- Voice memo transcripts (Otter, Whisper, etc.)
- Async written responses (the 5-question survey from `/unstuck outreach-batch`)
- LinkedIn DM threads
- Mixed format across 10 humans

Expect 7–10 blocks separated by `---` (or some delimiter). If less than 5 responses, surface honestly:

> "You have [N] responses. Below 5 = the sample is too small for a confident Kill/Pivot/Go call. Recommend either (1) extend Day 3-4 by 48 hours and chase 3 more responses, or (2) run pattern analysis on what you have and note 'low-confidence' on the verdict."

---

**Step 2 — Pattern analysis (4 dimensions)**

For each transcript, internally extract:
- Specific pain language (verbatim — their words, not yours)
- Willingness-to-pay signals (mentioned price points, paid-alternatives, "I'd pay X for...")
- Solution language (what they wished existed; what they've tried)
- Disqualifiers (the pain isn't real for them; they don't have budget; the audience is different)

Then cross-reference patterns ACROSS transcripts.

---

**Step 3 — Output the verdict + evidence**

Output structured analysis:

### A. Top 3 pain quotes (verbatim)

> The 3 quotes that surfaced the strongest, most-cited version of the pain. Use the buyer's exact words. Cite the person.

**Example output:**
```
1. "Tuesday afternoon backlog grooming is the moment I think 'I didn't sign up for this.'"
   — Aamir Khan, Datadog PM, async response
2. "I'd pay $200 for someone to tell me what good strategy work actually looks like."
   — Priya Sharma, Vercel PM, live call
3. "I keep doing PRD work I know is admin theater. I want to do roadmap-level thinking."
   — Marcus Lee, Stripe PM, voice memo
```

### B. Repeated language patterns

Words / phrases that showed up in 3+ conversations:

```
- "JIRA grooming" / "backlog admin" / "ticket admin" (7 of 10)
- "real strategy work" / "actual PM work" (6 of 10)
- "want to be a staff PM" / "promotion gap" (5 of 10)
- "EM buy-in" / "convincing my manager" (4 of 10)
```

These are the words that go in your landing page. Verbatim. Not paraphrased.

### C. Willingness-to-pay signal

Score the 10 conversations on a 1–5 willingness-to-pay scale:

```
- 5 (would buy at proposed price, asked when ready): 3 of 10
- 4 (would buy at lower price or with proof): 2 of 10
- 3 (interested but uncommitted): 3 of 10
- 2 (curious but no urgency): 1 of 10
- 1 (not the right person): 1 of 10
```

Weighted signal: high if 5+ scored ≥4. Weak if mostly 2s and 3s.

### D. Kill / Pivot / Go verdict + evidence

Apply the framework from `references/frameworks.md`:

**KILL** if:
- Fewer than 3 of 10 described real, specific pain
- The dominant response was polite interest
- "Maybe" / "interesting" / "tell me when it's done" without urgency

**PIVOT** if:
- People described real pain BUT your proposed solution doesn't match
- Multiple people said "I don't need X, but I desperately need Y"
- Audience is real but different than the one you targeted

**GO** if:
- 6+ of 10 described the same core pain in specific terms
- 3+ already paid money trying to solve it
- 3+ said they'd buy at the proposed price

**Output the verdict + the specific evidence:**

```
VERDICT: GO (high confidence)

Evidence:
- 7 of 10 described JIRA grooming / backlog admin as the source of frustration
- 4 of 10 are already paying for partial solutions (Lenny's premium, Reforge, coaching)
- 5 of 10 said they'd pay $200+ for a real solution
- The audience name matches: junior + mid PMs at B2B SaaS, 1-3 years in
- Repeated language is consistent ("real strategy work," "EM buy-in")

Risks flagged:
- Only 2 of 10 explicitly committed to a price (most said "interesting" without naming a number)
- Audience may be slightly narrower than your hypothesis (B2B SaaS specifically, not all PMs)
```

---

**Step 4 — Save analysis to User Context Section D.1**

```
SECTION D.1 — Validation Conversation Analysis
Locked: [Date]
Source: /unstuck conversation-finder

Verdict: [KILL / PIVOT / GO] ([confidence: high/medium/low])
Sample size: [N] responses

Top 3 pain quotes (use verbatim in landing page copy):
1. "[quote]" — [name], [context]
2. "[quote]" — [name], [context]
3. "[quote]" — [name], [context]

Repeated language (use in copy):
- "[phrase 1]" (N of 10)
- "[phrase 2]" (N of 10)
...

Willingness-to-pay distribution:
- 5: N people | 4: N | 3: N | 2: N | 1: N

Refined audience (from data, not hypothesis):
[1 sentence — the specific subset of your original audience that the data points to]

Risks flagged:
- [risk 1]
- [risk 2]
```

This block feeds directly into Module 2's One-Page Scope (T05) on Day 6.

---

**Step 5 — Chain to next**

- **GO:** "Proceed to Module 2 / Day 6. Open `/unstuck scope` — your One-Page Scope draft will reference the refined audience + verbatim language from this analysis."
- **PIVOT:** "Hold on Module 2. Rewrite your hypothesis using the [pivot direction] surfaced above. Re-validate with 3–5 more conversations targeting that hypothesis. Then back here."
- **KILL:** "Hard call but the right one. Open `/unstuck discovery` Path 1 (Decide Already) and surface the next candidate. Your validation skill stays sharp; just point it at a project with a better signal."

</process>

<success_criteria>
This module is complete when:
- [ ] All transcripts received and analyzed (7+ for high-confidence verdict)
- [ ] Top 3 pain quotes surfaced verbatim with attribution
- [ ] Repeated language patterns identified across conversations
- [ ] Willingness-to-pay distribution scored
- [ ] Kill / Pivot / Go verdict delivered with evidence
- [ ] Section D.1 paste block produced (feeds Module 2 Day 6)
- [ ] Day 6 next-module recommendation given (or pivot/kill alternative)
</success_criteria>
