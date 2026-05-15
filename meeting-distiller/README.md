# Meeting Distiller

**Stop producing meeting summaries. Start producing meeting artifacts.**

## The Problem

Most meeting notes never get re-read. Not once, not ever. The ones that do get re-read get scanned for exactly four things: what was decided, who owes what by when, what's still open, and where did we land on the disagreement. Everything else is noise dressed up as thoroughness.

Otter, Fireflies, Fathom, and Granola are all good transcribers and competent summarizers — and that's the failure. A summary is a shorter version of the meeting. The thing people actually need is a project management artifact: a contract for what happens next.

The universal failure pattern of every existing tool, in one sentence: they're optimized for the meeting being recorded. They should be optimized for the next two weeks of work being clear.

## What It Does

You paste a meeting transcript (Otter, Fireflies, Zoom, Granola, raw notes — whatever). The skill produces a one-page artifact built around the four things people actually scan for, plus one mandatory editorial call: the single thing that mattered most.

Output is locked to a template. ~400-600 words. Hard ceiling 800. One page.

The word "summary" appears nowhere. Section headers are project management nouns (Decisions, Action Items, Open Questions, Disagreements, Parking Lot) — never narrative nouns (Overview, Discussion, Highlights, Recap).

The artifact passes the absent-attendee test: someone who wasn't in the meeting knows exactly what to do next from reading it.

## How to Use It

### In Claude.ai

1. Start a new conversation
2. Open the skill: "Use the meeting-distiller skill" (if added to your Project) or paste the contents of `SKILL.md` as your first message
3. Paste your meeting transcript or notes
4. Answer at most 3 quick context questions (skipped entirely if the input is clean)
5. Receive your one-page artifact
6. Paste it into Notion, Slack, an email, or a GitHub issue

### In Claude Code

1. Add the skill to your config:
   - Copy `SKILL.md` to `~/.claude/skills/meeting-distiller/SKILL.md`
   - Or reference it in your `.claude/CLAUDE.md`: `When distilling meetings, read path/to/meeting-distiller/SKILL.md`
2. Tell Claude Code: "Distill this meeting" and paste the transcript (or pass a file path)
3. Save the output as a `.md` file in your project notes folder

### Tips for Better Artifacts

- **Cleaner transcripts produce better artifacts.** Otter and Fireflies tend to be cleaner than Granola for speaker attribution.
- **Include attendee names** in the input if the transcript doesn't name them. The artifact gets sharper when owners are real people, not "Speaker 2."
- **If the meeting was actually two meetings** (topic change halfway through), the skill will produce two artifacts. Don't try to force one.
- **Standups and status meetings work.** The format adapts — Decisions becomes "None — status meeting," Action Items captures the round-robin commitments.
- **Async-friendly:** paste a Slack thread or long async chat log. Threads have decisions, actions, and open questions too.

## What You Get

```
### MEETING ARTIFACT

**Date:** May 13, 2026 · **Topic:** Q3 pricing model decision
**Attendees:** Molly, David, Priya, Tom
**Transcript quality:** Clean

---

**CONTEXT**
Pricing for the Q3 launch is undecided 6 weeks out. Two models on the table —
flat $99/mo vs. usage-based with $49 floor. Goal of meeting: pick one and
commit so engineering can start the billing build.

---

**THE ONE THING**
We picked usage-based pricing — but the real outcome is that David surfaced
that our current Stripe integration can't do metered billing without a 3-week
rebuild. That hidden cost reframes the launch timeline more than the pricing
decision itself.

---

**DECISIONS**

1. **Q3 launches with usage-based pricing ($49 floor + metered overage).**
   Higher LTV potential and matches how the top 3 competitors price.
   *Decided by: group consensus* (Tom dissented but didn't block)

2. **Launch timeline shifts from July 1 → July 22** to accommodate the Stripe
   metered-billing rebuild. *[implicit — confirm]* — David named the 3-week
   estimate and nobody pushed back; the new date wasn't said aloud.

---

**ACTION ITEMS**

| Owner | Action | Deadline |
|-------|--------|----------|
| @David | Spike the Stripe metered-billing rebuild and confirm 3-week estimate | May 17 |
| @Priya | Update the pricing page mockups for usage-based model | May 20 |
| @Molly | Email the design partners with the pricing change + new launch date | May 15 |
| [needs assignment] | Draft customer-facing FAQ on metered billing | May 24 |

---

**OPEN QUESTIONS**

- What's the cap on overage charges? (Tom flagged but didn't get answered)
- Do existing free-tier users get grandfathered into flat pricing, and for how long?

---

**DISAGREEMENTS**

- **Pricing model:** Tom argued flat $99 reduces customer anxiety and shortens
  the sales cycle; group went with usage-based for LTV.
  Resolved: Yes — usage-based, with Tom's anxiety concern logged for the
  pricing-page copy.

---

**PARKING LOT**

- Annual prepay discount structure (revisit after first 30 days of usage data)
- Enterprise tier pricing (defer to Q4)
```

That's the whole artifact. One page. Anyone who wasn't in the meeting now knows what to do.

## The Research Behind It

Four findings shaped the design:

**Minutes record what is done, not what is said.** Robert's Rules of Order — a 150-year-old principle that 90% of modern meeting tools ignore. Action minutes (decision-only minutes) document only the decisions reached and the actions derived from them. Verbatim minutes are reserved for legal/regulatory contexts. For knowledge work, action minutes win every time.

**The shared DNA of every effective meeting format.** Amazon's six-pager, Robert's Rules action minutes, Fellow's four-section template, EA tradition, and agile retrospectives all converge: separate what was decided from what someone now owes from what's still open. AI summaries blob them together; the reader has to do the parsing work themselves; that's why notes get abandoned.

**The one thing every existing tool refuses to do.** Every tool produces a flat list of bullets where everything looks the same weight. A real meeting has one thing that mattered most — usually the decision that unlocks the next two weeks of work, or the disagreement that surfaced an unspoken assumption. Naming it requires editorial judgment. AI tools won't do it. The skill mandates it.

**Implicit decisions are the meeting's actual product.** The hardest extraction problem: nobody said "decided" but everyone moved on. Heuristic: one option debated, someone proposed a path, no one objected, conversation moved to a new topic. The "moved to a new topic" signal is the most reliable. The skill surfaces these AND marks them `[implicit — confirm]` so the person who was there can validate. Pretending they were stated creates false confidence; omitting them loses the meeting's most valuable output.

## Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| Summary vs. artifact framing | Artifact only. "Summary" is banned from output. | Summary is the failure mode every tool falls into. The framing of the output shapes what the model produces. |
| Decision/action separation | Always separate sections, never merged | A decision can exist with no action. An action can exist with no decision. Conflating them loses both. |
| Implicit decision marking | Always surface AND always flag `[implicit — confirm]` | The implicit decision is often the meeting's most important product. Surfacing it AND admitting the inference is the only honest path. |
| Owner attribution | Conservative. Clear acceptance only. Ambiguous = `[needs assignment]` | Fake attribution creates accountability fraud. Better to flag than fabricate. |
| Sentiment, talk-time, engagement | Cut entirely | Vendor-differentiator theater. Zero evidence anyone re-reads notes for this. The legitimate version is the Disagreements section. |
| "The One Thing" section | Mandatory editorial call | Every other tool refuses to produce this because it requires judgment. The willingness to make the call is the differentiator. |
| Length | One page. ~400-600 words. Hard ceiling 800. | Compression is the feature. A two-page artifact gets skimmed and abandoned. |
| Topic vs. chronological grouping | Topic. Always. | Most AI tools chronologize. Useless because the reader doesn't care what order things came up in. |

## Pairs With

- **[ask-me-the-questions](/ask-me-the-questions/)** — Use before a meeting to clarify what you actually need to decide. Use after the meeting to interrogate any artifact item that feels half-baked.
- **[decision-maker](/decision-maker/)** — When the meeting artifact surfaces an unresolved decision, route it to decision-maker for a structured choice.
- **[devils-advocate](/devils-advocate/)** — When "The One Thing" is a decision the team made too easily, run it through devils-advocate before the next meeting.
- **[mental-models](/mental-models/)** — When a recurring meeting keeps producing the same Open Questions, mental-models can diagnose the underlying pattern.
