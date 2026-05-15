---
name: meeting-distiller
description: Turn a meeting transcript or messy notes into a one-page project management artifact — decisions, action items, open questions, disagreements, parking lot, and the one thing that mattered most. Activate when the user pastes a transcript, asks for meeting notes, says "summarize this meeting" (then deliver an artifact, not a summary), mentions Otter/Fireflies/Fathom/Granola/Zoom transcripts, asks "what did we decide," "who owns what," "what are the action items," or wants notes someone who wasn't in the room can act on.
---

# Meeting Distiller

## What This Skill Does

Takes a meeting transcript, set of notes, or freeform description and produces a one-page project management artifact. Not a summary. An artifact: a contract for what happens next.

Output is built around the four things people actually scan for when they re-read meeting notes: what was decided, who owes what by when, what's still open, and where the team landed on the disagreement. Plus one editorial call — the single thing that mattered most.

The artifact passes the absent-attendee test: someone who wasn't in the meeting knows exactly what to do next from reading it.

## What This Skill Does NOT Do

- Live transcription or recording (it consumes existing transcripts; it doesn't capture audio)
- Sentiment analysis, talk-time ratios, engagement scores (these are vendor-differentiator theater — nobody re-reads notes for them)
- Generic prose "summaries of what was discussed"
- Calendar, CRM, or Asana integration (the artifact is markdown — route it manually)
- Multi-meeting synthesis (one meeting at a time)
- Voice/brand-tone overlay (the format is the format)

---

## The Banned Word

**"Summary" is the failure mode.** Don't use it in section headers. Don't use it in prose. Don't use it when offering follow-ups.

Every section header is a project management noun (Decisions, Action Items, Open Questions, Disagreements, Parking Lot). Never a narrative noun (Overview, Discussion, Highlights, Key Topics, Recap).

If the user asks for "a summary," produce the artifact anyway and say: "Built you the artifact instead of a summary — same input, version that's actually useful to act on."

---

## Phase 1: Input Intake

The user pastes a transcript, meeting notes, or describes the meeting. Do this:

1. **Count the words.** Rough is fine.
2. **Read for transcript quality** — clean, some gaps, or noisy.
   - Clean: full sentences, clear speaker attribution, no `[inaudible]` markers.
   - Some gaps: occasional `[inaudible]`, some mid-sentence speaker switches, mostly readable.
   - Noisy: frequent `[inaudible]`, word-salad ("we should the the the project"), heavy cross-talk, attribution unclear in 4+ person meetings.
3. **Check the volume:**
   - Under ~500 words: warn that the artifact will be thin. Ask: "Got more context — chat thread, agenda doc, your follow-up notes? More signal makes a better artifact."
   - 500 to 15,000 words: proceed.
   - Over 15,000 words: warn that compression will be aggressive. Ask: "This is a long one — want me to focus on a specific topic, or distill the whole thing?"
4. **Confirm receipt** in one line: word count, attendees if visible, transcript-quality read.

---

## Phase 2: Quick Context Questions

Skip this entire phase if the input answers everything. Most clean transcripts answer everything.

Ask only what the transcript can't reveal. Maximum 3 questions, asked together, never drip:

1. (If the meeting topic isn't clear): "What was this meeting actually about? One sentence."
2. (If attendees aren't named): "Who was in the room?"
3. (If the meeting clearly continues prior work but the input doesn't say what): "What was the state of play coming into this meeting?"

If everything is clear, jump straight to Phase 3 and produce the artifact.

---

## Phase 3: Extraction

Work through the transcript silently. Don't show this work to the user. Extract:

### Decisions

Two kinds:

**Explicit decisions:** someone said it. "We're going with option B." "Let's launch July 22." Quote the decision in your own clear sentence — don't quote the messy original.

**Implicit decisions:** the heuristic from the research. A decision was made when (a) one option was being debated, (b) someone proposed a path, (c) at least one other person agreed or no one objected, and (d) the conversation moved to a new topic. The "moved to a new topic" signal is the most reliable.

Implicit decisions are often the meeting's most important product. **Always include them.** Always mark `[implicit — confirm]` so the person who was there can validate.

For every decision, capture:
- The decision as a clear sentence
- One line of reasoning if useful ("because integration risk was lower")
- Who decided (named person, "group consensus," or specific dissents)

Decisions and Action Items are **separate sections.** Never merged. A decision can exist with no action ("we agreed not to pursue this"). An action can exist with no decision (someone volunteered to investigate). Conflating them loses both.

### Action Items

Locked formula: **verb + single owner + deadline.**

- **Verb-first.** "Send the revised proposal" not "Proposal." "Spike the Stripe rebuild" not "Stripe."
- **Single owner.** Multiple owners = no owner. If a transcript shows two people agreeing to share work, split it into two action items with split scope.
- **Deadline required.** If no deadline was discussed, write `[date TBD]` AND add it to Open Questions.
- **Enough context to remember in 3 days.** "Send revised proposal to Dahlia Group" not "Send proposal" — the owner won't remember which version.

**Owner attribution is conservative.** Only attribute when the transcript shows clear voluntary acceptance: "I'll take that," "Yes, I'll do it," "I'll send that by Friday." Ambiguous attribution = `[needs assignment]`. Never guess from role or seniority.

### Open Questions

Things that surfaced but didn't get answered. Two flavors:

- Questions that need an answer before the next meeting or before unblocking X
- Questions that require input from someone not in the room

Don't hallucinate answers. The job is to surface what someone needs to go find out, ask, or decide. AI tools fail this section the worst because answering questions feels more useful than admitting they're unanswered. It isn't.

### Disagreements (conditional section)

Include only when two or more people clearly held different positions. Skip the section entirely if the meeting was alignment-friendly.

For each disagreement, capture:
- Topic
- Who held what position (named when possible)
- Resolution status: resolved (and which way) or deferred

This is the section people actually look for when they re-read notes — they want to know "where did we land on the X debate?"

### Parking Lot

One-liner per deferred topic + when to revisit. The job is to prove the topic wasn't dropped, not to re-litigate it. "Vendor selection (revisit Q3)" — not three paragraphs.

### The One Thing

Mandatory. Editorial call required. One paragraph.

The single most important outcome from the meeting. Usually one of:
- The decision that unlocks the next chunk of work
- The disagreement that surfaced an unspoken assumption
- The constraint that just changed the timeline
- The realization that the original plan was wrong

This is the section every other tool refuses to produce because it requires judgment. Make the call.

If literally nothing meaningful happened: say so. "Nothing was decided. The One Thing is that this meeting should have been an email." That's a useful artifact too.

### Filtering Rules

- Group decisions and actions by **topic**, not by chronological order. The reader doesn't care what order things came up in.
- Filter aggressively: discussion threads under ~90 seconds that didn't produce a decision, action, or open question don't make the artifact.
- Cross-talk, side conversations, "we should grab lunch sometime" — cut.
- Don't recap the discussion. Capture the result.

---

## Phase 4: Artifact Production

Output the artifact in this exact template. No deviations. The template is the product.

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

### Length Discipline

- Target: 400-600 words.
- Hard ceiling: 800 words.
- One page when printed or pasted into Notion.

If you're over 800, cut the Context to 2 sentences, trim Parking Lot one-liners, and remove any decision that doesn't change behavior. Never solve length by deleting Open Questions or Disagreements — those are load-bearing.

---

## Phase 5: Refinement (offered, not forced)

After delivery, say once:

> Want me to adjust anything? Common fixes:
> - An action item I attributed to the wrong person
> - An implicit decision that should be a real one (or vice versa)
> - A parking lot item that should have been an action
> - An open question I missed

Don't chase refinements. If the user says "looks good," ship it.

If they correct an attribution: update silently and re-output. If they catch a missed decision: add it and re-output. If they push back on "The One Thing": rewrite it and ship.

---

## Hardcoded Rules

- The word **"summary"** appears nowhere in the output. Not in headers, not in prose, not in offers to refine.
- Section headers are project management nouns only. Never narrative nouns. Banned: Overview, Discussion, Highlights, Key Topics, Recap, Notes, Sentiment, Engagement, Energy.
- **Decisions and Action Items are separate sections.** Never merged.
- **Implicit decisions get marked `[implicit — confirm]`.** Never silently inferred. Never silently dropped.
- **Owner attribution requires clear voluntary acceptance** in the transcript. Ambiguous = `[needs assignment]`. Never guess from role.
- **Action items follow verb + single owner + deadline.** "Follow up" and "look into" are not verbs. If no deadline was discussed, write `[date TBD]` AND add to Open Questions.
- **Group by topic, not chronologically.**
- **The One Thing is mandatory.** Even if "nothing meaningful happened" is the answer.
- **No sentiment, no talk-time, no engagement scores.** The legitimate version of energy data is the Disagreements section.
- **Hard ceiling: 800 words.** Compression is the feature.
- **Never fabricate.** If the transcript doesn't say it, don't put it in the artifact. If you have to infer, mark the inference.

---

## Edge Cases

**Noisy transcript with frequent `[inaudible]` markers:** flag in the header (Transcript quality: Noisy), reduce confidence on extracted items, and add an Open Question asking the user to verify any decision that hung on an inaudible moment. Don't pretend to know what was said.

**Speaker attribution clearly wrong** (e.g., the transcript says "Molly" said something but the rest of the conversation makes that impossible): note it. "Action item attributed to Molly per transcript, but context suggests this was David — confirm." Better to flag than propagate the error.

**Meeting that was actually two meetings** (topic change halfway through): produce two artifacts. Say: "This was really two meetings — Q3 pricing in the first half, hiring in the second. Built you separate artifacts so each one is actionable on its own."

**Meeting where nothing was decided:** produce the artifact anyway. The One Thing is "Nothing was decided." Decisions section says "None — see Open Questions." This is a useful artifact: it tells the team to schedule a decision-forcing follow-up.

**Standup or status meeting** (no decisions, just updates): the format still works. Decisions = "None — status meeting." Action Items captures any commitments made in the round-robin. Open Questions captures blockers. The One Thing is usually whichever blocker matters most.

**1:1 meeting:** the format works but trim the Disagreements section unless real disagreement happened. Most 1:1s are alignment, not debate.

**User pastes a Slack thread or chat log instead of a meeting transcript:** the same logic applies. Threads have decisions, action items, open questions, and disagreements too. Use the same artifact template. Note in the Context that this came from async conversation, not a synchronous meeting.

**User pastes raw notes they took during the meeting:** treat as input. The notes already filtered most of the noise; your job is to enforce the format and surface implicit decisions the note-taker missed.

**User asks for "minutes" instead of "an artifact":** produce the artifact. Robert's Rules-style minutes record what was *done*, not what was *said* — the artifact format already does this. If the user specifically needs verbatim minutes for legal/regulatory reasons, decline and tell them: "Verbatim minutes are a different deliverable — those need a court reporter or full transcript, not this skill."

**Long meeting (60+ min) covering multiple topics:** group decisions and actions by topic. The artifact stays one page because compression is the feature, not because the meeting was short.

**The "One Thing" feels obvious or trivial:** push harder. Re-read the transcript looking for: the assumption that got challenged, the cost that surfaced late, the timeline that quietly shifted, the person whose silence mattered. There is almost always something. If genuinely nothing — say so honestly.
