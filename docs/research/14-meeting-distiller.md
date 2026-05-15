# Meeting Distiller — Research Results

The strongest signal across all four research questions is the same: **the failure mode of every meeting tool on the market is treating the output as a record of what was said instead of a contract for what happens next.** Otter, Fireflies, Fathom, and Granola are all good transcribers and competent summarizers — and that's the problem. A summary is a shorter version of the meeting. An artifact is the meeting's deliverable. Most meeting notes are never read again ("not once, not ever" per Lindy Hale's Medium post that gets cited across the productivity space) — and the ones that *are* read get scanned for exactly four things: what was decided, who owes what by when, what's still open, and what's about to fall through the cracks. Everything else is noise dressed up as thoroughness. The template that follows is built around those four things and ruthless about the rest.

---

## Q1: What does a great post-meeting artifact look like?

**Five reference formats, one shared DNA.**

**Amazon's six-pager** is the philosophical anchor, even though it's an *input* document, not an output. Bezos's 2004 directive killed PowerPoint because slides hide bad thinking — "there is no way to write a six-page narratively structured memo and not have clear thinking." The relevance for meeting outputs: **prose forces the writer to know what they actually mean.** Bullet lists let you pretend a half-thought is a decision. The six-pager is read in silence for the first 20-30 minutes of the meeting. The output equivalent — what gets written *after* — should hold to the same standard: if you can't write it as a clear sentence, you didn't actually decide it.

**Robert's Rules of Order** gives the legal foundation: *minutes record what is **done**, not what is **said.*** This is a 150-year-old rule that 90% of modern meeting tools ignore. "Action minutes" (also called decision-only minutes) document only the decisions reached and the actions derived from them — not the discussion. Verbatim minutes are the opposite extreme and are explicitly reserved for legal/regulatory contexts. For knowledge work, action minutes win.

**Fellow.app's template** (the dominant SaaS in this space) lands on a four-section model: agenda items, decisions, action items, and next steps. Their best-practice doc nails the action-item formula: **verb + single owner + deadline.** "Follow up with client" is useless. "@Monica: Send revised proposal to Dahlia Group by Friday Aug 20" is an action. They also flag the realtime-clarification move: end the meeting by saying "Just to confirm — David is taking this, deadline Monday?" That clarification step is what AI tools miss because they have no live agency.

**Executive assistant practice** (per Asana, Wrike, Convene, and the Umbrex partner-meeting guide) adds two things AI summaries consistently lose: **the reasoning behind a decision** ("we picked vendor B because the integration risk was lower, not because they were cheaper") and **the explicit owner-confirmation step** ("Just to confirm — is David taking this?"). EAs also distinguish between *commitments* (someone said they'd do X) and *decisions* (the group agreed X is the path). AI tools blur the two.

**Agile retrospective formats** — Start/Stop/Continue, Mad/Sad/Glad, 4Ls, Pluses/Deltas — are technically meeting outputs, but they're optimized for *team learning*, not project execution. Their useful contribution: every retro format ends with a small set (3-5 max) of SMART action items with named owners. The discipline of *small set* is critical. A meeting that produces 17 action items produced zero action items.

The shared DNA: every effective format separates **what was decided** from **what someone now owes** from **what's still open**. AI summaries blob them together into prose paragraphs and the reader has to do the parsing work themselves — which is why they don't.

**Sources:** [Amazon's narrative memo (Anecdote)](https://www.anecdote.com/2018/05/amazons-six-page-narrative-structure/), [The Amazon 6-Pager (Visme)](https://visme.co/blog/amazon-6-pager/), [Action Minutes (MRSC)](https://mrsc.org/stay-informed/mrsc-insight/august-2023/action-minutes), [Fellow action items guide](https://fellow.app/blog/meetings/how-to-manage-meeting-tasks-and-action-items/), [Asana meeting notes tips](https://asana.com/resources/meeting-notes-tips), [Umbrex capturing actions](https://umbrex.com/resources/how-to-run-effective-meetings/capturing-action-items-and-decisions/), [Atlassian retrospective playbook](https://www.atlassian.com/team-playbook/plays/retrospective).

**Confidence: High.** Convergent across five independent traditions (executive culture, parliamentary procedure, SaaS PM practice, EA craft, agile facilitation). The four-section spine is the closest thing to a universal pattern in meeting documentation.

---

## Q2: What's the optimal output structure?

The candidate sections from the prompt evaluated against actual usage:

**Decisions made (with who decided): ESSENTIAL.** Robert's Rules-level requirement. Without this, the document fails its only job. Should include reasoning ("because integration risk was lower"), not just the decision.

**Action items (owner + deadline + context): ESSENTIAL.** Fellow's formula is correct: verb + one owner + date. Multiple owners = no owner. Vague verbs ("look into," "explore") = no action. Context matters — "Send revised proposal" is better than "Send proposal" because three days later the owner won't remember which version.

**Open questions (unanswered, needs follow-up): ESSENTIAL.** This is the section AI summaries hallucinate the most badly because answering questions feels more useful than admitting they're unanswered. The actual job: surface what someone needs to go find out, ask, or decide before next meeting.

**Key disagreements (who, what, resolved or not): ESSENTIAL when present, omitted when absent.** Lindy Hale's "Be Honest — How Often Do You Reread Your Meeting Notes?" piece argues this is what people actually look for when they *do* go back to notes — they want to know "where did we land on the X debate?" Don't force this section if there were no real disagreements; do include it when two people clearly held different positions.

**Parking lot (raised but deferred): ESSENTIAL but compressed.** One-liner per item. "Vendor selection (revisit Q3)" not three paragraphs. The job is to prove the topic wasn't dropped, not to re-litigate it.

**The one thing that mattered most: ESSENTIAL.** This is editorial judgment and AI tools refuse to do it. Every other tool produces a flat list of bullets where everything looks the same weight. A real meeting has one thing that mattered most — usually the decision that unlocks the next two weeks of work, or the disagreement that surfaced an unspoken assumption. Naming it is the highest-value-per-word section in the entire artifact.

**Sentiment/energy read: GIMMICKY. CUT.** Fireflies and Sembly both ship sentiment analysis. No EA-tradition or agile-tradition document includes it. Nobody re-reads notes three weeks later to learn the team felt "moderately positive" in the Q2 planning meeting. It's vendor-differentiator theater. The closest legitimate version is "key disagreements" — which captures the *useful* part of energy data (where did people disagree?) without the useless part (how did they feel about it on a scale of -1 to +1?).

**Discussion summary / topics covered: GIMMICKY. CUT (with one exception).** This is what every AI tool defaults to and it's exactly the failure mode. The exception: a 2-3 sentence *context* paragraph at the top that frames *why this meeting happened* — useful for the person who wasn't there. Anything more is summary-trap.

**Attendees / date / duration: ESSENTIAL but minimal.** Header metadata, not body content. Single line.

**Verdict: 6 sections.** Header → Context (2-3 sentences) → Decisions → Action Items → Open Questions → Disagreements (conditional) → Parking Lot → The One Thing.

**Sources:** [Be Honest — How Often Do You Reread Your Meeting Notes? (Lindy Hale)](https://medium.com/@lindyhale/be-honest-how-often-do-you-go-back-and-read-your-meeting-notes-09b2d0099fb0), [Action Minutes (MRSC)](https://mrsc.org/stay-informed/mrsc-insight/august-2023/action-minutes), [Fireflies summary guide](https://fireflies.ai/blog/how-to-write-a-meeting-summary/), [Granola pricing comparison](https://www.granola.ai/blog/meeting-note-tool-pricing-granola-vs-fireflies-fathom-otter), [How to Write a Meeting Summary (Claap)](https://www.claap.io/blog/meeting-summary).

**Confidence: High.** The reread-behavior data is compelling: people scan for decisions, owners, deadlines, open items, and "where did we land on X." Sentiment analysis appears in zero re-read scenarios.

---

## Q3: How to handle messy real-world transcripts?

Four problems, four playbooks.

**Speaker identification errors.** Otter, Granola, and Fathom all mis-attribute lines, especially in 4+ person meetings and on cross-talk. The skill cannot fix the transcript — but it can *not amplify the error.* Rule: when assigning an action item, only attribute when the transcript shows a clear "I'll do X" or "Yes, I'll take that" pattern from a named speaker. When attribution is ambiguous, the action item gets owner: `[needs assignment]` with a flag, not a guess. Guessing creates accountability fraud.

**Implicit decisions** (nobody said "decided" but everyone moved on). This is the single hardest extraction problem. Heuristic: a decision was made when (a) one option was being debated, (b) someone proposed a path, (c) at least one other person agreed or no one objected, and (d) the conversation moved to a new topic. The "moved to a new topic" signal is the most reliable — if the next 30 lines of transcript are about something else, the prior thing got resolved (or aggressively avoided, which is itself worth flagging). Every implicit decision gets marked `[implicit — confirm]` so the person who was there can validate or correct.

**Cross-talk, tangents, side conversations.** Filter aggressively. If a line of discussion lasted under ~90 seconds and didn't produce a decision, action, or open question, it doesn't make the artifact. The "we should grab lunch sometime" comments are signal in social contexts and noise in operational ones. Default to noise-cutting.

**Long meetings (60+ min).** A 60-minute meeting at ~150 words/minute is ~9,000 words / ~12,000 tokens — fits in Claude's context window without chunking. The real challenge isn't the input length, it's that long meetings cover multiple topics that each deserve their own decision/action grouping. Solution: group decisions and actions by *topic* not by chronological order in the transcript. Most AI tools chronologize — which is useless because the reader doesn't care what order things came up in.

**Varying transcript quality.** Width.ai's research found that when transcripts have >10% error rate, even excellent summarization produces wrong or misleading output. Detection signal: if the transcript has frequent `[inaudible]` markers, repeated speaker switches mid-sentence, or obvious word-salad ("we should the the the project go forward"), warn the user upfront and reduce confidence on every extracted item. Don't pretend to know what was decided when the transcript doesn't.

**Sources:** [Action-Item-Driven Summarization of Long Meeting Transcripts (arXiv)](https://arxiv.org/html/2312.17581v2), [GPT-4 Meeting Summarization (Width.ai)](https://www.width.ai/post/gpt-4-for-meeting-summarization), [How AI Processes Podcast Audio (sipsip.ai)](https://sipsip.ai/blog/learn/how-ai-processes-podcast-audio), [Granola vs Otter vs Fireflies vs Fathom (Luminix)](https://www.useluminix.com/reports/industry-analysis/ai-meeting-notes-comparison-granola-vs-otter-vs-fireflies-vs-fathom-2026).

**Confidence: Medium-High.** The implicit-decision heuristic is the most novel part and the least battle-tested — worth iterating after real-user testing.

---

## Q4: Existing tools and where they fall short

**Fathom.** Largest user base. Wins on reliability and friction-elimination, not innovation. Output is a clean-but-generic transcript + summary + action item list. Complaint pattern: action items get extracted but "don't move anywhere" — the artifact is read once and abandoned. No editorial judgment about what mattered most.

**Otter.ai.** Pending class-action lawsuit (Brewer v. Otter, filed Aug-Sept 2025) over unauthorized recording and AI-training data use. Trustpilot complaint patterns: unauthorized recurring charges and unreachable support. Output quality: solid transcription, generic summary template that reads like every other Otter summary regardless of meeting type.

**Fireflies.** Ships sentiment analysis and talk-time-ratio metrics. User complaint: "dashboard has so many features it took a while to find what was actually needed" — feature creep at the expense of focus. The sentiment data is exactly the kind of thing that looks impressive in a screenshot and gets ignored by every actual reader of the notes.

**Granola.** Newer entrant, design-darling. Complaint: weaker transcription accuracy and speaker attribution vs. Gemini or Notion-AI. Strong on UI, weaker on accuracy.

**Glebis Meeting Analyzer skill** (referenced in the prompt, harder to find direct documentation on). Anthropic-ecosystem skill, similar shape to other AI summary tools.

The universal failure pattern, in one sentence: **all of these tools are good at transcribing meetings and competent at summarizing them, but none of them produce a project management artifact you'd want to ship to the team.** They optimize for the meeting being recorded; the meeting-distiller optimizes for the next two weeks of work being clear.

**Sources:** [The 10 Best AI Note Takers (meetingnotes.com)](https://meetingnotes.com/blog/best-ai-note-takers), [Granola vs Otter vs Fireflies vs Fathom (Luminix)](https://www.useluminix.com/reports/industry-analysis/ai-meeting-notes-comparison-granola-vs-otter-vs-fireflies-vs-fathom-2026), [AI Meeting Assistants: I Tested 8 (Medium)](https://mrsproductivity.medium.com/ai-meeting-assistants-i-tested-otter-fireflies-fathom-and-5-others-116d10ebbfce).

**Confidence: High** on the failure pattern, **Medium** on individual tool details (some review data is recent and shifting fast).

---

## Key Design Decisions

| Decision | Choice | Why |
|----------|--------|-----|
| **Summary vs. artifact framing** | **Artifact only.** The word "summary" is banned from skill output and prompts. Every section header is a *project management noun* (Decisions, Action Items, Open Questions) not a *narrative noun* (Overview, Discussion, Highlights). | Summary is the failure mode every existing tool falls into. The framing of the output shapes what the model produces. Banning the word at the prompt level prevents drift. |
| **Decision/action separation** | **Decisions and Action Items are separate sections, never merged.** A decision can exist with no action item ("we agreed not to pursue this"). An action item can exist with no decision (someone volunteered to investigate). Conflating them loses both. | Robert's Rules-level distinction. EA tradition consistently separates these. AI tools blob them, which makes both harder to act on. |
| **Implicit decision marking** | **Mark `[implicit — confirm]` on any decision the transcript doesn't explicitly state.** Don't omit them (they're often the most important). Don't pretend they were stated (creates false-confidence problems). | The implicit decision is the meeting's actual product. Surfacing it AND admitting the inference is the only honest path. |
| **Owner attribution policy** | **Only attribute action items when the transcript shows clear voluntary acceptance.** Ambiguous = `[needs assignment]`. Never guess based on role or seniority. | Fake attribution creates accountability fraud and erodes trust in the artifact. Better to flag than to fabricate. |
| **Sentiment, energy, talk-time** | **Cut entirely.** | Vendor differentiator theater. Zero evidence anyone re-reads notes for this data. Adds noise to the four things people actually scan for. |
| **"The One Thing" section** | **Mandatory editorial call.** One paragraph. Names the single most important thing from the meeting — usually the decision that unlocks the next sprint, or the disagreement that revealed a hidden assumption. | This is the section every existing tool refuses to produce because it requires judgment. It's also the section the reader uses to orient. The willingness to make the call is the skill's differentiator. |
| **Length discipline** | **One-page artifact. ~400-600 words. Hard ceiling: 800 words.** Compression is the feature. | A two-page artifact gets skimmed and abandoned. The discipline of fitting it on one page forces the model to make editorial choices instead of dumping everything. |

---

## Meeting Artifact Template v1

```
### MEETING ARTIFACT

**Date:** [meeting date] · **Topic:** [single-line subject]
**Attendees:** [comma-separated names]
**Transcript quality:** [Clean / Some gaps / Noisy — affects confidence on items below]

---

**CONTEXT**
[2-3 sentences. Why this meeting happened. What had to be resolved or moved
forward. Written for someone who wasn't there.]

---

**THE ONE THING**
[One paragraph. The single most important outcome — usually the decision that
unlocks the next chunk of work, or the disagreement that surfaced an unspoken
assumption. Make the editorial call.]

---

**DECISIONS**

1. **[Decision stated as a clear sentence].** [One line of reasoning if useful.]
   *Decided by: [name or "group consensus"]* · *[implicit — confirm]* if applicable

2. **[Next decision].** ...

---

**ACTION ITEMS**

| Owner | Action | Deadline |
|-------|--------|----------|
| @Name | [Verb-first action with enough context to remember in 3 days] | [date] |
| @Name | [Action] | [date] |
| [needs assignment] | [Action] | [date] |

---

**OPEN QUESTIONS**

- [Question that needs an answer before next meeting / before unblocking X]
- [Question that requires a decision from someone not in the room]

---

**DISAGREEMENTS** *(omit section if none)*

- **[Topic]:** [Person A] argued [position]; [Person B] argued [counter-position].
  Resolved: [Yes — chose X / No — deferred to next meeting]

---

**PARKING LOT**

- [One-liner per deferred topic + when to revisit]
- [...]
```

### Brief example

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
