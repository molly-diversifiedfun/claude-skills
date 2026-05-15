---
name: research-brief
description: Produce a structured research brief on a question with explicit confidence ratings on every claim and search-handles instead of fabricated citations. Use when the user asks for research, wants a "rundown on X," asks "what do you know about Y," needs to scope a topic before deep diving, or asks for evidence on a contested question. Also trigger on phrases like "research brief," "summarize the evidence," "what does the research say," "give me the lay of the land," "is X actually true," or "help me get up to speed on Y." NEVER fabricates citations — only generates verifiable search-handles. Separates trained-knowledge from inference from speculation. Does NOT do real-time research (use Perplexity/Elicit), single-fact lookups (just answer), or original research.
---

# Research Brief

## What This Skill Does

Takes a research question and produces a structured brief — TL;DR, what's well-supported, what's contested, what's inference, what's unknown, and what to read next. Every substantive claim carries a confidence rating. Every "source" is a search-handle the user can verify in 30 seconds, not a fabricated citation.

The skill exists to prevent the failure mode that produced 700+ court cases of AI-fabricated citations: fluent-sounding output that the reader has no way to fact-check.

## What This Skill Does NOT Do

- **Real-time research** — no web access, training cutoff is the ceiling. Recommend Perplexity, Elicit, or browse-enabled tools for current info.
- **Original research** — no interviews, no fieldwork, no primary data collection.
- **Definitive answers on high-stakes legal/medical/financial decisions** — always scoping, never the final word.
- **Single-fact lookups** — "population of Estonia" doesn't need a brief. Just answer.
- **Continuous research-assistant mode** — one brief per request. The user drives any follow-up.
- **Formal academic citations** — search-handles only, by design.

---

## Phase 1: Scope Check

Before producing anything, run two checks. Out loud, briefly.

### Check 1: Is this in scope?

If the question requires real-time data — current prices, breaking news, anything from the last few weeks — say so plainly:

> "This needs current data and I'm working from training data with a cutoff. For [question type], try Perplexity, Elicit, or a browse-enabled tool. I can brief you on the *background* — the structural context behind the question — if that's useful. Want that?"

Don't fake it. The skill's whole value is honesty about what you know.

### Check 2: Is this brief-shaped?

| Question shape | Response |
|---|---|
| Single fact ("population of Estonia") | Answer it directly. Note that a brief is overkill. |
| Synthesis ("what does the evidence say about intermittent fasting") | Brief. |
| Scoping ("I want to learn about X") | Brief. |
| Contested-evidence ("is X actually true") | Brief — these are the highest-value cases. |
| Decision-support ("should we adopt X") | Brief. The decision-maker skill handles the actual choice; this scopes the evidence. |
| Vague ("tell me about AI") | Ask one targeted clarifier. Just one. |

If you need to clarify, ask exactly one question:
> "Are you asking about [scope A] or [scope B]? I'll brief whichever."

Never ask three questions when one will do.

---

## Phase 2: Internal Source-Type Pass

Before generating the brief, walk through the question silently and categorize what you're about to claim. This is the calibration step. Don't skip it.

For every substantive claim you're considering, ask:

1. **Is this trained-knowledge?** Multiple independent sources in your training corpus, low ambiguity. You'd bet on it.
2. **Is this inference?** You're combining two or more trained facts to reach a conclusion. Often right, sometimes subtly wrong. Tag it.
3. **Is this speculation?** Extrapolation beyond what you have evidence for. Should be rare. Flag it explicitly or cut it.
4. **Is this contested in the field?** If experts disagree, name the actual positions. Don't manufacture fake debates and don't pretend consensus exists when it doesn't.

This pass is what separates the brief from "Claude's first instinct." 2025 calibration research shows that models that are *prompted to name source type before rating confidence* are meaningfully better-calibrated than models that just produce a number cold.

---

## Phase 3: Generate the Brief

Use this template exactly. Every section. Every confidence tag. No skipping.

```markdown
# Research Brief: [Question]

## TL;DR
[2-3 sentences. The single most important thing the user should know.]
**Overall confidence: [High / Moderate / Low / Very Low]**

## What We Know (well-supported)
- **[Claim].** [1-2 sentence elaboration.]
  - *Confidence: High | Source type: [peer-reviewed research / industry data / widely-reported / etc.]*
  - *Verify: search "[specific handle]"*
- [Another claim, same format]

## What's Contested
- **[Position A]:** [Who holds it, what they argue, why.]
  - *Source type: [type] | Verify: search "[handle]"*
- **[Position B]:** [Who holds it, what they argue, why.]
  - *Source type: [type] | Verify: search "[handle]"*
- *My read: [optional one-line synthesis, explicitly tagged as inference]*

## What's Inference (my synthesis, not direct knowledge)
- **[Claim].** [Why you're inferring this — what facts you're combining.]
  - *Confidence: Moderate | Tag: inference from [A] + [B]*
  - *Verify: [what to check that would confirm or break the inference]*

## What's Unknown / Speculation
- **[Open question].** [What we'd need to know.]
  - *Confidence: Very Low — speculation only*
  - *Verify: [what kind of source would settle this]*

## What to Read Next
- For the strongest "yes" case: search "[handle]" — type: [source type]
- For the strongest "no" case: search "[handle]" — type: [source type]
- For methodology debates: search "[handle]" — type: [source type]
- For a recent overview: search "[handle]" — type: [source type]

## Confidence Scale (reference)
- **High** — multiple independent well-documented sources in training data, low ambiguity, recent enough to trust
- **Moderate** — supported but limited sources, or older, or some ambiguity
- **Low** — partial evidence, indirect inference, significant unknowns
- **Very Low / Speculation** — extrapolation beyond evidence; treat as a hypothesis to investigate

---
*Want me to dig deeper on the contested section, brief a sub-question, or change the scope? Just ask.*
```

---

## Confidence Rating Rules

The confidence tag on each claim is the heart of the brief. Get this right or the whole artifact loses its point.

### High
- Multiple independent sources in training data
- Widely accepted in the field
- Not time-sensitive, or recent enough to trust
- You'd defend the claim under questioning

### Moderate
- Supported but with limited sources, OR
- Older sources where the field may have moved, OR
- Some genuine ambiguity in the evidence
- You believe it but you'd want a check before acting

### Low
- Partial evidence
- You're inferring from indirect sources
- Significant unknowns surround the claim
- You wouldn't bet on the specifics

### Very Low / Speculation
- Extrapolating beyond evidence
- "If the pattern held, then…"
- Should be rare. If you're using this often, the question is out of scope.
- Treat as a hypothesis to test, never as an answer

### Auto-downgrade triggers

Always downgrade when:
- The claim is time-sensitive (markets, current events, recent research, anything that drifts) — note the training cutoff explicitly
- You're aggregating across regions or eras (averaging hides the variance)
- The source field is dominated by a single methodology (publication bias risk)
- You can't name a specific source type, only "I think I've seen something on this"

---

## Source-Handle Protocol (NEVER FABRICATE CITATIONS)

This is the non-negotiable rule. The skill exists to prevent fabricated citations. If you violate this, the artifact is worse than nothing.

### The rule

**Never** generate a citation in the form `Author (Year), Journal, p. NN`. Even if it sounds right. Even if you're "pretty sure." That format is what gets people sanctioned in court.

### What to write instead

A search-handle is a phrase the user can paste into Google, Google Scholar, or PubMed and find the source — *if it exists*. Pair it with a source-type tag.

| Don't write | Do write |
|---|---|
| "Smith et al. (2023), *Journal of Pediatric Medicine*, p. 47" | `Search: "Smith pediatric outcome study 2023"` — *type: peer-reviewed clinical research* |
| "According to McKinsey's 2024 report" | `Search: "McKinsey AI adoption report 2024"` — *type: industry consultancy report* |
| "Per the FDA's 2022 guidance" | `Search: "FDA guidance [topic] 2022"` — *type: regulatory document* |
| "A landmark 2018 study found…" | `Search: "[topic] study 2018"` — *type: likely peer-reviewed; specific source uncertain* |

### When you're not sure the source exists

Be honest. Write:

> *"There is likely work on [X] from [field/era] — search '[handle]' to find current sources. I can't name a specific paper without risking fabrication."*

This is the truthful default. Use it whenever you'd otherwise be tempted to invent.

### Source type taxonomy

Pick one of these for every claim that needs a source:

- **peer-reviewed research** — academic journals, conference proceedings
- **industry data** — surveys, market research, company reports
- **government / regulatory** — agency guidance, official statistics, court rulings
- **trade press** — industry publications, specialist journalism
- **mainstream press** — newspapers, magazines (use cautiously for technical claims)
- **expert commentary** — specialist blogs, well-known practitioners
- **anecdotal / case study** — single-incident reports
- **inference** — your synthesis, not from a single source
- **speculation** — extrapolation; flag explicitly

---

## Anti-Patterns (Things to Never Do)

- **Never fabricate a citation in any format.** Not author-year, not URL, not "according to [organization]" if you're inventing the report. Search-handles only.
- **Never bury uncertainty in hedge words.** "Some studies suggest" without a confidence tag is the failure this skill exists to prevent. Every claim gets an explicit rating.
- **Never present inference as fact.** If you combined two trained facts to reach a conclusion, tag it as inference. The reader needs to know which conclusions came from your synthesis.
- **Never skip "What's contested."** If the question is genuinely settled, say so explicitly. If you don't have enough source material to identify positions, say so. Don't manufacture a fake debate, but don't quietly drop the section.
- **Never produce a brief without "What to read next."** The brief is a scoping artifact. Without next-steps it becomes a final answer, which is the wrong frame.
- **Never mix probability words and confidence words.** Pick GRADE-style ("High," "Moderate," "Low") and stay there. Don't say "almost certainly likely" — that's how this becomes meaningless.
- **Never claim confidence in time-sensitive claims without flagging the cutoff.** Markets, current events, recent research — auto-downgrade and note it.
- **Never default to "balanced both sides" on questions where the evidence isn't balanced.** If most of the evidence supports one position, say so with a confidence rating. Artificial both-sides framing is its own dishonesty.
- **Never produce a brief on something out of scope.** If the question needs real-time data or original research, say so and recommend the right tool. Don't fake it.

---

## Quality Check (Before You Hand It Over)

Run through this before you finalize:

- [ ] Every substantive claim has a confidence tag
- [ ] Every source reference is a search-handle, not a fabricated citation
- [ ] Source-type tag is on every claim that needs one
- [ ] "What's contested" names actual positions (or explicitly states the question is settled)
- [ ] "What's inference" exists if you synthesized anything
- [ ] "What to read next" has 3-5 search-handles, each tagged by source type
- [ ] Time-sensitive claims are auto-downgraded with a cutoff note
- [ ] No "almost certainly likely" or other confidence-word salad
- [ ] Brief is 600-1,200 words (longer for genuinely complex topics; shorter for narrow ones)
- [ ] You'd bet on every High-confidence claim

If any check fails, fix it before you ship. The skill's value is in the discipline.

---

## When to Hand Off to Another Skill

- **Real-time data needed:** Perplexity, Elicit, or browse-enabled tools.
- **The user wants you to make the decision, not just scope the evidence:** decision-maker.
- **The user wants you to argue against a position you just established:** devils-advocate.
- **The user wants to think through implications, not gather evidence:** mental-models.
- **The user is trying to clarify their own view, not get external research:** self-interview.
