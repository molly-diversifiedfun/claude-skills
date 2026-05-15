# PRD: meeting-distiller

## Problem

Meeting notes don't get re-read. "Not once, not ever," per the Lindy Hale piece that gets cited across the productivity space. Otter, Fireflies, Fathom, and Granola produce competent transcripts and generic summaries — and that's the failure. A summary is a shorter version of the meeting. The thing people actually need is a project management artifact: a contract for what happens next.

When notes do get re-read, people scan for exactly four things: what was decided, who owes what by when, what's still open, and where did we land on the disagreement. Everything else is noise dressed up as thoroughness. Existing tools blob decisions, action items, and discussion into prose paragraphs and make the reader do the parsing work — which is why the notes get abandoned.

## Solution

A skill that takes a meeting transcript (or messy notes) and produces a one-page artifact built around the four things people actually scan for. Banned word: "summary." Every section header is a project management noun (Decisions, Action Items, Open Questions) — never a narrative noun (Overview, Discussion, Highlights). Editorial judgment is mandatory: the artifact must name "the one thing that mattered most" instead of producing a flat list where everything looks the same weight.

The output passes the absent-attendee test: someone who wasn't in the meeting knows exactly what to do next from reading it.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Summary vs. artifact framing | **Artifact only.** The word "summary" is banned from skill output and prompts. Section headers are project management nouns, never narrative nouns. | Summary is the failure mode every tool falls into. The framing of the output shapes what the model produces. Banning the word at the prompt level prevents drift. |
| Decision/action separation | **Decisions and Action Items are separate sections, never merged.** | Robert's Rules-level distinction: minutes record what is *done*, not what is *said*. A decision can exist with no action ("we agreed not to pursue this"). An action can exist with no decision (someone volunteered to investigate). Conflating them loses both. |
| Implicit decision marking | **Mark `[implicit — confirm]` on any decision the transcript doesn't explicitly state.** Don't omit them. Don't pretend they were stated. | The implicit decision is often the meeting's actual product. Surfacing it AND admitting the inference is the only honest path. |
| Owner attribution policy | **Only attribute action items when the transcript shows clear voluntary acceptance** ("I'll take that," "Yes, I'll do it"). Ambiguous = `[needs assignment]`. Never guess from role or seniority. | Fake attribution creates accountability fraud and erodes trust in the artifact. Better to flag than fabricate. |
| Sentiment, energy, talk-time | **Cut entirely.** | Vendor-differentiator theater. Zero evidence anyone re-reads notes for this data. Adds noise to the four things people actually scan for. The legitimate version of energy data is "Disagreements" — capture *where* people split, not how they felt about it. |
| "The One Thing" section | **Mandatory editorial call.** One paragraph naming the single most important outcome. | This is the section every existing tool refuses to produce because it requires judgment. It's also the section the reader uses to orient. The willingness to make the call is the differentiator. |
| Length discipline | **One-page artifact. ~400-600 words. Hard ceiling: 800.** | A two-page artifact gets skimmed and abandoned. Compression forces editorial choices instead of bullet-dumping everything. |
| Topic grouping vs. chronological | **Group decisions and actions by topic, not by transcript order.** | Most AI tools chronologize. Useless because the reader doesn't care what order things came up in. They care what's now true and what they owe. |
| Transcript quality flag | **Surface noise level in the header** (Clean / Some gaps / Noisy). Reduce confidence on extracted items when the transcript is rough. | Width.ai research: at >10% transcript error rate, even good summarization produces wrong output. Pretending the source was clean is dishonest. |

## Interaction Model

**Phase 1: Input Intake** (30 sec)
- User pastes a transcript, meeting notes, or describes the meeting
- Skill confirms what it received: rough word count, detected attendees if visible, transcript-quality read (clean / some gaps / noisy)
- If under ~500 words: warn that the artifact will be thin, ask if there's more context (chat thread, agenda doc, follow-up notes)
- If over ~15,000 words (>90 min meeting): warn that the artifact will compress aggressively and ask if there's a specific topic to focus on

**Phase 2: Quick Context Questions** (60 sec, only when needed)
Ask only what the transcript can't reveal. Skip the question if the answer is obvious from the input. Maximum 3 questions, asked all at once:

1. (If meeting topic isn't clear): "What was this meeting actually about? One sentence."
2. (If attendees aren't named in the transcript): "Who was in the room?"
3. (If the meeting clearly continues prior work): "What was the state of play coming into this meeting?"

If everything is clear from the input, skip Phase 2 entirely.

**Phase 3: Extraction** (automatic, no user input)
Work through the transcript and extract:

- **Decisions:** explicit ("we're going with option B") and implicit (one option debated, someone proposed it, no one objected, conversation moved on). Mark implicit decisions clearly.
- **Action items:** verb + single owner + deadline. Only attribute when the transcript shows clear acceptance. Flag ambiguous ownership as `[needs assignment]`.
- **Open questions:** things that surfaced but didn't get answered, or that require input from someone not in the room.
- **Disagreements:** where two or more people clearly held different positions. Note resolution status.
- **Parking lot:** topics raised, deferred, with a one-liner on when to revisit.
- **The One Thing:** the editorial call. Usually the decision that unlocks the next chunk of work, or the disagreement that surfaced an unspoken assumption.

Group decisions and actions by topic, not by chronological order in the transcript.

Filter aggressively: discussion threads under ~90 seconds that didn't produce a decision, action, or open question don't make the artifact.

**Phase 4: Artifact Production** (automatic)
Output the one-page artifact in the locked template format. No deviations. The template is the product.

**Phase 5: Refinement** (offered, not forced)
After delivery, say:
> Want me to adjust anything? Common fixes: an action item I attributed wrong, an implicit decision you want re-flagged, a parking lot item that should have been an action.

Don't push it. The artifact should land right the first time more often than not.

## Output Spec

One artifact. Locked template. ~400-600 words. Hard ceiling 800.

```
### MEETING ARTIFACT

**Date:** [date] · **Topic:** [single-line subject]
**Attendees:** [comma-separated names]
**Transcript quality:** [Clean / Some gaps / Noisy]

---

**CONTEXT**
[2-3 sentences. Why this meeting happened. Written for someone who wasn't there.]

---

**THE ONE THING**
[One paragraph. The single most important outcome. Editorial call required.]

---

**DECISIONS**

1. **[Decision as a clear sentence].** [One line of reasoning if useful.]
   *Decided by: [name or "group consensus"]* · *[implicit — confirm]* if applicable

---

**ACTION ITEMS**

| Owner | Action | Deadline |
|-------|--------|----------|
| @Name | [Verb-first, enough context to remember in 3 days] | [date] |
| [needs assignment] | [Action] | [date] |

---

**OPEN QUESTIONS**

- [Question that needs an answer before next meeting / before unblocking X]

---

**DISAGREEMENTS** *(omit section if none)*

- **[Topic]:** [A] argued [position]; [B] argued [counter].
  Resolved: [Yes — chose X / No — deferred]

---

**PARKING LOT**

- [One-liner per deferred topic + when to revisit]
```

## Success Criteria

- The absent-attendee test: someone who wasn't in the meeting knows exactly what to do next from reading the artifact.
- Action items follow the verb + single owner + deadline formula. No "follow up" or "look into" verbs.
- Implicit decisions are surfaced AND flagged — never silently inferred, never silently dropped.
- The artifact fits on one page. ~400-600 words typical. 800 max.
- "Summary" appears nowhere in the output, the prompts, or the section headers.
- The "One Thing" paragraph names a real outcome — not a recap of the topic.

## What This Skill Does NOT Do

- Live transcription or recording (consumes existing transcripts/notes; doesn't capture audio)
- Sentiment analysis, talk-time ratios, engagement scores
- Generic prose summaries of "what was discussed"
- Calendar/CRM/Asana integration (it produces a markdown artifact; routing it lives elsewhere)
- Multi-meeting synthesis (one meeting at a time; longitudinal patterns are a different skill)
- Voice/personality matching for the artifact tone (the format is the format — no brand-voice overlay needed)

## Anti-Patterns to Avoid in Implementation

- Never output a section called "Summary," "Overview," "Discussion," "Highlights," or "Key Topics."
- Never produce paragraph-style prose instead of the locked template.
- Never attribute an action item to someone who didn't clearly accept it. Use `[needs assignment]` and move on.
- Never silently infer a decision. Mark `[implicit — confirm]` or omit.
- Never include sentiment scores, engagement metrics, or talk-time data.
- Never chronologize. Group by topic.
- Never let the artifact exceed 800 words. Compression is the feature.
- Never end the artifact without naming "The One Thing." If nothing meaningful happened, say that explicitly: "Nothing was decided. The One Thing is that this meeting should have been an email."
- Never fabricate a deadline because the verb-owner-deadline format demands one. If no deadline was discussed, write `[date TBD]` and add it to Open Questions.
- Never combine Decisions and Action Items into a merged list.

## Technical Notes

- Input format: plain text transcript, meeting notes, bullet-list notes, or a freeform description. The skill normalizes.
- Optimal input: 1,500-9,000 words (10-60 min meeting at typical talk speeds).
- Maximum reasonable input: ~15,000 words (90 min meeting). Above this, ask for a topic focus.
- Minimum input: ~500 words. Below this, warn the user.
- Works in Claude.ai (no tools required) and Claude Code (no tools required). Pure prompt-based.
- Output is plain markdown — paste anywhere (Notion, Slack, email, doc, GitHub issue).
- No transcript quality detection beyond surface signals: `[inaudible]` markers, mid-sentence speaker switches, word-salad. Surface what's visible; don't pretend to deeper QA.
