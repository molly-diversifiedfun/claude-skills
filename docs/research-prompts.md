# Research Prompts for Skill PRDs

Run each prompt in a fresh Claude conversation with web search enabled. Bring the full output back.

**Per prompt:** Expect 10-15 minutes for thorough research. Run in fresh conversations (no cross-contamination).

**Batching:**
- Batch 1: Skills 1-3 (Voice & Authenticity) — highest pain cluster
- Batch 2: Skills 4-8 (Thinking & Decisions) — largest category
- Batch 3: Skills 9-12 (Learning & Research)
- Batch 4: Skills 13-14 (Editing & Productivity)
- Batch 5: Skills 15-16 (Career & Professional)

---

## Category 1: Voice & Authenticity

### Skill 1: voice-extractor

```
# Voice Extractor Skill — Research Prompt

## Goal

I'm building a Claude skill that takes 3-5 writing samples and produces a
reusable voice profile (.md file) a user can load into any Claude conversation
to get output that sounds like them.

## Critical Constraint

Describing voice with adjectives ("engaging, punchy, humorous") produces
generic output. Only sample-based extraction — analyzing actual writing
patterns — works. Every research direction below should assume this.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What dimensions of voice are extractable and reproducible?

Search for computational stylistics, stylometry, and authorship attribution
research. I need the specific, measurable features these systems use — not
abstract categories like "tone."

Cover at minimum: sentence length distribution, vocabulary tier/register,
rhetorical device frequency, paragraph structure patterns, opening/closing
patterns, transition mechanics, punctuation habits, humor/irony mechanics,
pronoun usage patterns, jargon density, and rhythm (stressed/unstressed cadence).

For each dimension: is it reliably extractable from 3-5 samples? Can Claude
reproduce it in generation? Rate each dimension on both axes.

Search: stylometry features, authorship attribution NLP, computational
stylistics writing dimensions, "writing DNA" analysis.

### Q2 [HIGH PRIORITY]: What do existing voice-matching implementations do, and where do they break?

Find the 5-8 strongest implementations across these categories:
- Claude skills (especially Daria Cupareanu's Voice DNA approach,
  haowjy/creative-writing-skills on GitHub)
- ChatGPT custom GPTs for voice matching
- GitHub repos or Substack/blog posts with voice-matching prompts
- Commercial tools (Jasper Brand Voice, Writer.com, etc.)

For each: summarize the approach in 2-3 sentences, then focus on **failure
modes** — user complaints, Reddit threads about "still doesn't sound like me,"
what dimensions break first. I care more about what fails than what works.

Search: voice matching Claude skill, writing style extractor prompt,
"voice profile" LLM, "sounds like me" AI writing, voice cloning prompt GitHub,
brand voice AI tool comparison, "voice DNA" writing.

### Q3 [MEDIUM PRIORITY]: Sample requirements — quantity, quality, and type

- Minimum viable sample count and optimal word count per sample
- Same-format samples (all blog posts) vs. varied formats — which produces
  a more robust profile?
- Do informal samples (emails, Slack messages, texts) improve or dilute
  the profile?
- Does mixing samples from different time periods cause problems?

Where possible, cite evidence rather than reasoning from first principles.

### Q4 [MEDIUM PRIORITY]: What should the voice profile .md file contain?

Find examples of voice profile files people have shared publicly (in GitHub
repos, Claude Projects discussions, blog posts about custom instructions).

For each example: what sections does it include, how long is it, and
(if reported) does the user say it works?

Then synthesize: what's the minimum viable profile structure? What sections
appear in profiles that work and are absent from profiles that don't?

Search: "voice profile" markdown, custom instructions writing style,
Claude project voice file, system prompt writing voice.

---

## Output Format

For each question:
- **Findings**: Substantive analysis, not a link dump. Prioritize depth on
  the most useful sources over breadth.
- **Sources**: Name and link each source. Flag which ones I should read
  myself vs. which you've fully captured.
- **Confidence**: High / Medium / Low, with a one-sentence explanation of
  what would change your assessment.

## Final Section: Key Design Decisions

End with the 5-7 binary or tradeoff decisions I need to make when building
this skill. Frame each as a choice with clear pros/cons:

> **Decision: Fixed dimensions vs. emergent dimensions**
> Option A: Pre-define 12 voice dimensions and score each from samples.
> Option B: Let the extraction prompt discover whatever patterns exist.
> Tradeoff: A is more consistent but may miss what makes a voice unique.
> B captures more but produces inconsistent profiles across users.

---

*Target length: 2,000-3,000 words total. Go deeper on Q1 and Q2, lighter
on Q3 and Q4.*
```

---

### Skill 2: ai-tell-killer

```
# AI Tell Killer Skill — Research Prompt

## Goal

I'm building a Claude skill that takes AI-generated or AI-assisted text and
surgically removes identifiable AI patterns — WITHOUT rewriting the whole
piece. The user's voice and structure stay intact; only the tells get fixed.

## Critical Constraint

This is an editor, not a rewriter. It flags and fixes specific patterns.
If a sentence has no AI tells, it passes through untouched. The user should
be able to diff the before/after and see only targeted changes.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What are the documented, measurable AI writing tells?

I need a categorized taxonomy, not just a word list. For each tell:
frequency threshold that triggers detection, and severity (always flag vs.
flag if excessive).

Categories to cover:
- Vocabulary (specific words/phrases that spiked post-AI)
- Punctuation (em dash density, semicolon patterns)
- Structure (list formatting overuse, parallel construction)
- Rhythm (sentence length uniformity, "constant perplexity")
- Opening/closing patterns (preamble, summary paragraphs)
- Transitions ("Let's explore," "Now let's turn to," "It's worth noting")

Look at: Wikipedia's "Signs of AI Writing" guide, AI detection tool
documentation (GPTZero, Originality.ai), the Max Planck / Stanford vocabulary
frequency studies, community banned-word lists on Reddit and GitHub.

Search: AI writing tells taxonomy, AI text detection features, "signs of AI
writing," AI vocabulary frequency shift research, em dash AI detection,
GPTZero detection methodology.

### Q2 [HIGH PRIORITY]: Where's the line between "AI tell" and "good writing"?

Some AI patterns are fine in moderation (em dashes, parallel structure,
clear transitions). I need frequency thresholds and context sensitivity.

- At what density does em dash usage trigger "this is AI"? (Per 100 words?
  Per paragraph?)
- Does context matter? (Em dashes in literary fiction vs. business email)
- What research exists on what triggers human "this is AI" perception?
- Find 3-5 examples of human writing that would be falsely flagged — what
  makes them look AI-like?

Search: AI detection false positives, human writing AI tells, "my writing
sounds like AI" Reddit, em dash frequency natural writing, AI detection
threshold research.

### Q3 [MEDIUM PRIORITY]: What existing humanizer tools exist and what's their approach?

Find the 5-6 strongest across: Claude skills, ChatGPT GPTs, commercial tools
(Undetectable.ai, WriteHuman, etc.), and open prompts.

For each: approach (find-and-replace? scoring? full rewrite?), what works,
and the key failure — overcorrection that makes text worse.

### Q4 [MEDIUM PRIORITY]: What should the skill NOT fix?

Overcorrection risks: removing all structure makes text worse, some "tells"
are genuinely good writing, aggressive humanizing introduces awkwardness.
What guardrails exist in the best implementations?

---

## Output Format

For each question:
- **Findings**: Substantive analysis. Prioritize depth on Q1 and Q2.
- **Sources**: Name and link. Flag must-reads.
- **Confidence**: High / Medium / Low with reasoning.

## Final Section: Key Design Decisions

5-7 binary/tradeoff decisions in this format:

> **Decision: Taxonomy-based vs. scoring-based detection**
> Option A: Check against a fixed list of known tells.
> Option B: Score text on statistical features (sentence length variance,
> vocabulary diversity, etc.).
> Tradeoff: A is explainable but misses novel patterns. B catches more
> but is harder to explain to users.

---

*Target length: 2,000-2,500 words. Go deepest on Q1 (the taxonomy is the
skill's core IP).*
```

---

### Skill 3: resume-rebuilder

```
# Resume Rebuilder Skill — Research Prompt

## Goal

I'm building a Claude skill that produces resumes hiring managers can't
identify as AI-generated. It extracts the user's real achievements with
specific metrics first (an "evidence bank"), then restructures for a target
job description.

## Critical Constraints

- Never invents experience or metrics the user didn't provide.
- Never uses buzzwords (synergy, rockstar, dynamic, passionate).
- The output must read as human-written — not polished-AI.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What specifically makes recruiters flag a resume as AI-generated?

Find recruiter and hiring manager accounts of what they notice. I need the
specific signals, not general "it sounds too polished."

Look at: r/recruitinghell, r/resumes, r/jobs, LinkedIn posts from recruiters
about AI resumes, the ResumeBuilder survey (74% detection rate), recruiting
industry blogs.

Search: recruiter spots AI resume, "AI generated resume" hiring manager,
resume AI detection signals, "threw out" AI resume Reddit, ATS AI detection.

### Q2 [HIGH PRIORITY]: What does a resume that works in 2026 actually look like?

Current best practices — not 2023 advice:
- Format preferences by career level (entry, mid, senior, executive)
- Has the ATS landscape changed with widespread AI use?
- Quantified achievements: still gold standard, or has "increased revenue
  40%" become an AI tell itself?
- Length expectations now
- Any industry-specific differences worth encoding

Find 3-5 authoritative, recent sources (2025-2026).

### Q3 [MEDIUM PRIORITY]: The "evidence bank" extraction method

Several career coaches teach building an achievement inventory before
touching the resume. Find the 3-4 strongest methodologies:
- What questions extract the best achievement data?
- How do you help someone who says "I don't have metrics"?
- STAR vs CAR vs PAR frameworks — which works best for extraction?
- How many achievements constitute a useful bank?

### Q4 [MEDIUM PRIORITY]: What existing AI resume tools do and where they fail

Survey the top 5 tools (Teal, Jobscan, Resume.io, Kickresume, etc.) plus
community prompts. Focus on: what gap exists that a skill could fill that a
SaaS tool can't?

Also: should this skill handle cover letters, or is that a separate concern?

---

## Output Format

For each question:
- **Findings**: Substantive analysis. Depth on Q1 and Q2.
- **Sources**: Name, link, flag must-reads.
- **Confidence**: High / Medium / Low with reasoning.

## Final Section: Key Design Decisions

5-7 decisions in tradeoff format:

> **Decision: One-pass generation vs. evidence-bank-first workflow**
> Option A: Ask questions and generate resume in a single flow.
> Option B: Build evidence bank as a separate artifact, then generate.
> Tradeoff: A is faster but produces thinner content. B takes longer but
> the evidence bank is reusable across applications.

---

*Target length: 2,000-2,500 words. Deepest on Q1 — the detection signals
are the skill's defensive core.*
```

---

## Category 2: Thinking & Decisions

### Skill 4: devil's-advocate

```
# Devil's Advocate Skill — Research Prompt

## Goal

I'm building a Claude skill that challenges your ideas instead of validating
them. An adversarial thinking partner that steelmans counter-arguments,
identifies unstated assumptions, and rates confidence in its own critiques.

## Critical Constraint

Anti-sycophancy prompting ("be honest," "be critical") decays after 3-5
exchanges. This skill must maintain adversarial stance durably across an
entire conversation. The research direction should focus on WHY decay happens
and what structural approaches prevent it.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: Why does anti-sycophancy prompting decay, and what prevents it?

I need the mechanism, not just the observation. Look at:
- RLHF/RLAIF training dynamics that pull toward agreement
- Context pressure effects over conversation length
- Any research on maintaining persona/stance durability in LLMs
- Techniques that have been shown to resist decay (structural framing,
  role assignment, explicit scoring obligations)

Search: LLM sycophancy mechanism, anti-sycophancy prompt decay, maintaining
adversarial LLM stance, RLHF agreement bias, Claude sycophancy research
Anthropic, persona persistence long conversation.

### Q2 [HIGH PRIORITY]: What structured critique frameworks produce useful (not demoralizing) output?

Find the 5-6 strongest frameworks across domains:
- Steel-manning, pre-mortem, red teaming, dialectical thinking
- Edward de Bono's Black Hat
- VC due diligence question structures
- Academic peer review standards
- How do the best editors/VCs/debate coaches deliver hard truths?

For each: how does it structure critique, and what makes it constructive
rather than destructive?

Search: structured critique framework, steel man argument technique,
pre-mortem facilitation, red team methodology, "constructive criticism"
framework, VC due diligence questions.

### Q3 [MEDIUM PRIORITY]: What existing adversarial AI tools exist?

Find 4-5 implementations: custom GPTs, Claude skills, GitHub prompts, the
Assess-Decide-Do framework. For each: approach, what works, where the
adversarial stance breaks down.

### Q4 [MEDIUM PRIORITY]: What should the output artifact look like?

Inline conversational pushback? A structured "challenge report"? Severity
levels (fatal flaw / significant risk / minor concern)? Should it end with
strengths after the critique? How do the best implementations handle this?

---

## Output Format

Per question: Findings (depth on Q1-Q2), Sources (name, link, must-reads),
Confidence (H/M/L with reasoning).

## Final Section: Key Design Decisions

5-7 tradeoff decisions:

> **Decision: Always adversarial vs. calibrated adversarial**
> Option A: Skill challenges everything, every time.
> Option B: Skill assesses idea quality first, calibrates pushback intensity.
> Tradeoff: A is simpler and avoids sycophancy by design. B is more useful
> but risks the very decay we're trying to prevent.

---

*Target length: 2,000-2,500 words. Deepest on Q1 — durability is the entire
value proposition.*
```

---

### Skill 5: mental-models

```
# Mental Models Skill — Research Prompt

## Goal

I'm building a Claude skill with 10-12 thinking frameworks and a router
that matches your problem to the right one, then walks you through applying
it step-by-step. Not a reference library — a facilitated thinking session.

## Critical Constraint

The models must produce genuinely DIFFERENT insights from each other. If
two models lead to the same output on most problems, one gets cut. Breadth
of coverage matters less than distinctiveness of outcome.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: Which mental models produce distinct outcomes on real problems?

Start from the long list: First Principles, Pre-Mortem, Inversion, Second-
Order Thinking, Regret Minimization, SCAMPER, Opportunity Cost, Eisenhower
Matrix, OODA Loop, Systems Thinking, Bayesian Updating, Cynefin, Steel-
Manning, 5 Whys, 10/10/10.

For each: what TYPE of problem does it uniquely solve? Where does it produce
an insight that no other model on this list would? Rate each on:
breadth (how many problem types), distinctiveness (unique output),
teachability (can a non-expert follow the steps in a chat interface).

Sources to check: Farnam Street's model rankings, Charlie Munger's actual
usage patterns, the CC-Thinking-Skills repo (tjboudreaux — which 18 did
they pick and why?), decision science research on which frameworks improve
measured outcomes.

Search: mental models effectiveness research, decision framework comparison,
"which mental models" actually use, Farnam Street best mental models,
thinking framework outcomes study.

### Q2 [HIGH PRIORITY]: How should the router match problems to models?

Given a vague problem description ("I'm stuck on whether to hire or
outsource"), how do you route to the right framework?

- Is there a problem taxonomy that maps cleanly to models?
- Should it recommend 1 model or offer 2-3 with reasoning?
- How does CC-Thinking-Skills handle routing?
- What if the user picks the wrong one — how to gracefully redirect?

### Q3 [MEDIUM PRIORITY]: What does facilitated application look like per model?

For the top 5 candidates from Q1: sketch the step-by-step question flow.
How many steps? What artifact emerges? How long should each take?

### Q4 [MEDIUM PRIORITY]: What existing implementations exist and what's missing?

CC-Thinking-Skills, Superpowers brainstorming, any ChatGPT mental model
GPTs. For each: what they do well, what's the gap this skill should fill.

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: The Final 12

Your recommended 12 models. For each: one sentence on what it uniquely
solves, the problem type it matches, and whether it's HIGH or MEDIUM
priority for inclusion.

Then: 5-7 design decisions in tradeoff format.

---

*Target length: 2,500-3,000 words. Deepest on Q1 — the model selection IS
the skill.*
```

---

### Skill 6: decision-maker

```
# Decision Maker Skill — Research Prompt

## Goal

I'm building a Claude skill that produces a one-page decision brief when
you're stuck between 2-4 options. The brief is an artifact you can sleep
on, hand to a co-founder, or reference later.

## Critical Constraint

This is distinct from devil's-advocate (which challenges) and mental-models
(which teaches frameworks). This skill is specifically for: "I have options
and I can't choose." The output is a DOCUMENT, not a conversation.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What makes a great decision document?

Find the 4-5 strongest decision document formats used in practice:
- Amazon's 6-pager structure and philosophy
- Bezos's "one-way door vs. two-way door" framework
- Bain/McKinsey decision frameworks
- Military decision-making process (MDMP)
- Farnam Street's decision journal format

For each: what sections, what's the core principle, and what makes it
actually useful (vs. just thorough)?

Search: Amazon 6-pager decision format, decision document template
McKinsey, "decision brief" format, decision journal Farnam Street,
military decision-making process structure.

### Q2 [HIGH PRIORITY]: What sections belong in a ONE-PAGE brief?

Amazon's 6-pager is too long. I need the minimum viable decision document.
Candidates: decision statement, options, weighted criteria, analysis per
option, pre-mortem per option, hidden assumptions, recommendation with
confidence, reversibility assessment, "what would change your mind."

Which of these are essential vs. nice-to-have? What do people actually
reference when they revisit a decision?

### Q3 [MEDIUM PRIORITY]: What decision traps should the skill actively counter?

Analysis paralysis, anchoring, sunk cost, status quo bias, framing effects.
For each: how can a structured document format specifically counteract it?
Not just "be aware of bias" — structural countermeasures.

### Q4 [MEDIUM PRIORITY]: What existing decision-support tools exist?

Find 4-5 across apps, prompts, skills. Focus on: what format do they
produce, and what's the gap?

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then include a "Decision Brief Template v1" —
your best attempt at the output format with section descriptions.

---

*Target length: 2,000-2,500 words. Deepest on Q1 and Q2 — the template
IS the skill.*
```

---

### Skill 7: ask-me-the-questions

```
# Ask Me the Questions Skill — Research Prompt

## Goal

I'm building a Claude skill that inverts the typical AI interaction. Instead
of the user writing a good prompt, they describe their situation vaguely and
Claude interviews them to extract the context it needs, THEN produces the
deliverable.

## Critical Constraint

This must be the simplest skill in the collection. If the intake process
itself feels burdensome, it defeats the purpose. The skill solves "I know
Claude could help but I can't articulate what I need" — blank prompt paralysis.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What makes a good rapid intake interview?

I need the question design, not the theory. Look at:
- How do consultants run efficient discovery sessions? (Specifically:
  what do they ask in the FIRST 5 minutes?)
- Design thinking interview techniques (IDEO, Stanford d.school)
- Jobs-to-be-Done interview methodology — the "switch interview"
- How do the best Claude skills handle intake? (Analyze the question
  flow in: unstuck-coach, build-irresistible-offer, interview-coach-skill
  on GitHub)

For each: what's the first question, how do subsequent questions adapt,
and how many questions before production?

Search: consultant discovery session questions, design thinking interview
guide, JTBD switch interview, "ask me the questions" AI prompt, intake
interview best practices, rapid requirements gathering.

### Q2 [HIGH PRIORITY]: How many questions before people lose patience?

Find data, not opinions:
- Form completion rates by field count (UX research)
- Chatbot conversation length tolerance (any studies?)
- What's the drop-off curve? (3 questions vs 5 vs 8 vs 12)
- Should it adapt: fewer for simple tasks, more for complex?

Search: form completion rate by fields, chatbot conversation length
dropout, survey abandonment rate questions, optimal intake questions UX.

### Q3 [MEDIUM PRIORITY]: How should it decide WHAT to ask?

Given "I need help with my business plan," how does the skill determine
which 3-5 questions extract the most useful context? Is there a universal
priority: purpose > audience > constraints > format > tone? Or does it
depend on the task type?

### Q4 [MEDIUM PRIORITY]: Scope — standalone skill or pattern for other skills?

Could this be a mode that other skills invoke ("start with intake")? Or is
it more valuable as its own entry point? How should it hand off to domain-
specific skills when it recognizes the task type?

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "The Universal Intake Protocol" — the optimal
question flow for extracting what Claude needs from a vague request.

---

*Target length: 1,500-2,000 words. This is the simplest skill — the research
should be proportionally focused. Deepest on Q1 and Q2.*
```

---

### Skill 8: self-interview

```
# Self-Interview Skill — Research Prompt

## Goal

I'm building a Claude skill where Claude asks the user progressive questions
to help them clarify their OWN thinking. Not a quiz, not feedback — a
structured self-interrogation that surfaces what you believe but haven't
articulated.

## Critical Constraint

The skill's job is to EXTRACT, not to ADD. Claude should never inject its
own opinions or steer toward a conclusion. The output is the user's thinking,
crystallized — not Claude's analysis of the user's thinking.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What questioning techniques surface unarticulated thinking?

Find the 5-6 strongest methodologies. For each: the core technique, example
questions, and when it works vs. when it fails.

Look at:
- Socratic method (the actual Platonic technique, not the buzzword)
- Clean Language (David Grove) — questions that carry zero assumptions
- Motivational interviewing's open-ended question structure
- Coaching frameworks (ICF powerful questioning competency)
- Journalist techniques for getting people past rehearsed answers

Search: Socratic questioning technique examples, Clean Language David Grove,
motivational interviewing open questions, coaching powerful questions ICF,
journalist interview technique authentic answers, "clarify your thinking"
questioning framework.

### Q2 [HIGH PRIORITY]: How should questions progress, and when should they stop?

- Start broad → narrow, or start specific → broaden?
- How to handle "I don't know" — dig deeper or move on?
- When to push on one thread vs. open a new area?
- What signals that the user has reached clarity?
- Total question count: what's the sweet spot?

Find evidence from coaching or therapy research on session pacing, not
just first principles.

### Q3 [MEDIUM PRIORITY]: What's the right output artifact?

Options: a transcript with highlighted insights, a structured document
(thesis + supporting points + gaps), a "clarity map" showing solid vs.
fuzzy areas, or just the conversation itself. What do existing
implementations produce, and what do users find most valuable?

### Q4 [MEDIUM PRIORITY]: What exists and where does it break?

Nick Quick's Self-Interview skill, rubber duck debugging, any AI coaching
tools. For each: approach, what works, failure mode.

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Question Architecture" — the optimal
progression structure for a self-interview session.

---

*Target length: 1,500-2,000 words. Deepest on Q1 — the question design is
the entire skill.*
```

---

## Category 3: Learning & Research

### Skill 9: learn-anything

```
# Learn Anything Skill — Research Prompt

## Goal

I'm building a Claude skill that teaches any topic through active recall —
it makes you explain back, catches misconceptions, and adapts to your level.
Not a lecture. A tutor that refuses to just tell you the answer.

## Critical Constraint

The core mechanism is the REFUSAL to lecture. If the user asks "what is X?"
the skill doesn't explain X — it asks what the user already knows, fills
gaps through questioning, and confirms understanding through teach-back.
Passive consumption is the failure mode this skill exists to prevent.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: Which learning science principles are encodable in a chat interface?

I need techniques that work in a text conversation, not just a classroom.
For each: the principle, evidence of effectiveness, and how it translates
to a Claude skill.

Cover: the testing effect (retrieval practice), elaborative interrogation,
the Feynman Technique, interleaving, desirable difficulty (Bjork), zone of
proximal development (Vygotsky), spaced repetition.

Which of these are feasible in a single chat session vs. requiring multiple
sessions? Which have the strongest evidence?

Search: testing effect retrieval practice Roediger, Feynman Technique
learning, elaborative interrogation effectiveness, desirable difficulty
Bjork, active recall vs passive review research, tutoring effectiveness
Bloom two sigma.

### Q2 [HIGH PRIORITY]: How should it assess current knowledge and calibrate difficulty?

- Self-assessment is unreliable (Dunning-Kruger). What works instead?
- Diagnostic questions: how many, what format, how to avoid discouraging
  beginners?
- Can it calibrate dynamically from responses mid-session?
- How does Bloom's two-sigma tutoring achieve calibration?

### Q3 [MEDIUM PRIORITY]: How should it structure a learning session?

- Chunk size: how much per "lesson" in a chat context?
- Syllabus: show upfront or reveal progressively?
- Session length: 15 min? 30 min? Open-ended?
- How to handle "I just want the answer" pushback?

### Q4 [MEDIUM PRIORITY]: What existing learning tools/skills exist?

Learn FASTER Kit (cheukyin175), Claude's Learning Mode, Duolingo's model,
Khan Academy's mastery progression. For each: approach, what works, gap.

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Learning Loop Design" — the optimal cycle
for one learning session (assess → teach → recall → correct → advance).

---

*Target length: 2,000-2,500 words. Deepest on Q1 — the learning science
is the skill's foundation.*
```

---

### Skill 10: explain-like

```
# Explain Like Skill — Research Prompt

## Goal

I'm building a Claude skill that explains any concept at a user-chosen
level using analogies from the user's OWN domain. "Explain Kubernetes like
I'm a chef who understands kitchen stations." Not simplification — genuine
cross-domain reframing.

## Critical Constraint

The analogy must come from the user's stated domain, not a generic
simplification. "Explain it simply" is not what this skill does. "Explain
it through the lens of [something I already understand]" IS.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What makes a cross-domain analogy work vs. mislead?

Find cognitive science research on analogical reasoning:
- Gentner's structure-mapping theory
- When do analogies create understanding vs. misconceptions?
- How deep must the structural mapping be before an analogy breaks?
- The "curse of knowledge" problem — why experts explain badly

Look at 3-5 famous explanations that work (Feynman, "Made to Stick" SUCCES
framework) and 2-3 that mislead. What differentiates them?

Search: analogical reasoning cognitive science Gentner, cross-domain analogy
effectiveness, analogy misconceptions learning, structure mapping theory,
Feynman explanation technique, "Made to Stick" analogy.

### Q2 [HIGH PRIORITY]: What changes at each explanation level?

Define 4-5 levels (beginner → expert). For each level, what specifically
changes: vocabulary, assumed knowledge, structural complexity, analogy
depth, abstraction level, detail density?

Find evidence from educational research on how textbooks at different
levels treat the same topic. What's the actual diff between an intro
textbook and a graduate textbook on the same concept?

### Q3 [MEDIUM PRIORITY]: How should the skill handle the user's background domain?

- Ask explicitly or infer from context?
- What if the user's domain doesn't map well to the target concept?
- Should it maintain a library of common domain pairings?
- When should it say "this concept doesn't have a good analogy in
  your domain" rather than force a bad one?

### Q4 [MEDIUM PRIORITY]: What exists and what's missing?

Find 3-4 "explain like" implementations. For each: approach and gap.

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Explanation Level Spec" — what changes at
each level with a concrete example (same concept at all levels).

---

*Target length: 1,500-2,000 words. Deepest on Q1 and Q2 — the analogy
quality and level calibration are the skill.*
```

---

### Skill 11: research-brief

```
# Research Brief Skill — Research Prompt

## Goal

I'm building a Claude skill that takes a question and produces a structured
research brief with findings, conflicting evidence, confidence levels per
claim, and what's still unknown. It will NOT fabricate citations — instead
it tells you what to search to verify each claim.

## Critical Constraint

Every claim gets a confidence rating. The skill explicitly separates "I know
this from training data" from "I'm inferring" from "I'm speculating." The
#1 failure mode it prevents: presenting inferences as established facts
(the problem that produced 800+ legal cases with fabricated citations).

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What does a well-structured research brief look like?

Find the 4-5 strongest brief/report formats from professional research:
- Intelligence community analytic standards (ICD 203, especially "Words
  of Estimative Probability")
- GRADE evidence quality framework (medicine)
- Think tank brief formats (RAND, Brookings)
- Cochrane systematic review structure (simplified)

For each: sections, how they handle uncertainty, and how they signal
evidence quality. I need structural patterns, not just descriptions.

Search: ICD 203 analytic standards, GRADE evidence framework, intelligence
brief format, research brief template think tank, "words of estimative
probability," evidence quality framework.

### Q2 [HIGH PRIORITY]: How should confidence scoring work in an LLM context?

- What scale? (High/Med/Low? Numeric? Probability language?)
- How should Claude differentiate between knowledge from training data,
  inference, and speculation?
- Is this actually feasible — can LLMs reliably self-assess confidence?
  Find any research on LLM calibration.
- The ICD 203 probability language ("almost certain," "likely," "roughly
  even") — applicable here?

Search: LLM confidence calibration research, LLM self-assessment accuracy,
AI epistemic humility, language model uncertainty estimation.

### Q3 [MEDIUM PRIORITY]: How to handle citations honestly?

The "don't fabricate, tell me what to Google" approach — find anyone doing
this well. Should it cite source TYPE ("peer-reviewed research," "industry
reporting," "anecdotal evidence")? How to flag thin evidence?

### Q4 [MEDIUM PRIORITY]: Highest-value use cases?

Which types of research questions produce the best briefs? Market research,
health questions, technical evaluations, policy questions, fact-checking?
Where does this format shine vs. where should users just use Perplexity?

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Research Brief Template v1" — sections,
confidence scale, and source-handling protocol.

---

*Target length: 2,000-2,500 words. Deepest on Q1 and Q2 — the brief
structure and confidence system are the skill's core.*
```

---

### Skill 12: book-distiller

```
# Book Distiller Skill — Research Prompt

## Goal

I'm building a Claude skill that produces opinionated book analysis — not
summaries. Given a book title: core thesis (2 sentences), 5 genuinely new
ideas, what's recycled from other thinkers, who should read it vs. skip it,
and 3 questions the book doesn't answer.

## Critical Constraint

This is the ANTI-summary. Compression preserves everything proportionally;
this skill makes JUDGMENTS about what matters and what doesn't. The output
should be more useful than the book's own table of contents for deciding
whether/how to engage with it.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What makes book criticism useful vs. just shorter?

Find the 3-4 strongest models of useful book analysis:
- How do the best reviewers (NYRB, LRB, New Yorker) structure reviews?
- What makes a review useful for deciding whether to read the book?
- The "contribution to the conversation" frame — what does this book ADD?
- How do podcast hosts prep for book interviews? (Tim Ferriss, Tyler Cowen)

For each: what structural elements make the analysis actionable rather than
just informative?

Search: NYRB book review structure, "how to review a book" literary
criticism, book analysis framework, intellectual contribution assessment,
book review vs summary difference.

### Q2 [HIGH PRIORITY]: Can Claude reliably identify original vs. recycled ideas?

This is the hardest feature. Test cases:
- Can Claude trace "Thinking Fast and Slow" ideas back to earlier
  Kahneman/Tversky papers?
- Can it identify when a business book recycles Jim Collins concepts?
- How reliable is this for well-known vs. niche books?
- What's the failure mode — false attribution? Missed borrowing?

This determines whether "intellectual genealogy" is a viable feature or
should be cut.

### Q3 [MEDIUM PRIORITY]: How should it handle books with thin training data?

- Well-known bestsellers: Claude has deep knowledge. Easy.
- Niche/recent books: partial knowledge. How to handle gracefully?
- Should it warn when knowledge is thin?
- Should it accept user-provided notes/highlights as input?

### Q4 [MEDIUM PRIORITY]: What existing book analysis tools exist?

Blinkist, Shortform, AI summary tools. What do users complain about?
What's missing that "opinionated" analysis would fill?

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Book Distillation Template v1" — the output
sections with descriptions and example content for one well-known book.

---

*Target length: 1,500-2,000 words. Deepest on Q1 and Q2 — the analysis
framework and intellectual genealogy feasibility are the key questions.*
```

---

## Category 4: Editing & Productivity

### Skill 13: precision-editor

```
# Precision Editor Skill — Research Prompt

## Goal

I'm building a Claude skill with explicit editing levels. The user picks a
level BEFORE the skill touches their text:
1. Flag issues only (no changes)
2. Suggest fixes as comments
3. Light copy edit preserving voice
4. Heavy developmental edit

## Critical Constraint

At levels 1-3, the user's sentences SURVIVE. The skill works around them,
not through them. "I asked for a light edit, not a rewrite" is the #1
complaint this skill exists to solve.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: How do professional editors define and enforce editing levels?

Find the industry-standard tier definitions:
- Developmental editing, line editing, copy editing, proofreading — what
  specifically does each touch vs. leave alone?
- Chicago Manual of Style definitions
- How do publishers scope and price editing work?
- What does "preserve the author's voice" mean in practice — which
  elements are off-limits at each level?

For each level: concrete examples of what gets changed and what doesn't.

Search: editing levels defined publishing, developmental vs copy editing
difference, Chicago Manual editing standards, "preserve author voice"
editing, professional editing scope definition.

### Q2 [HIGH PRIORITY]: How should AI editing differ from AI rewriting?

The core technical challenge: what constraints make Claude stay in "editing"
mode rather than defaulting to rewrite?

- The "react to it, don't rewrite it" principle — how to encode this?
- Should it show changes (track-changes style)?
- What specific instructions prevent Claude from "improving" things
  that aren't wrong?
- Any research or community experience with constraining AI to
  edit-not-rewrite?

Search: AI editing vs rewriting, "don't rewrite" AI prompt, constrained
AI editing, track changes AI, "light edit" AI writing, preserve voice
AI editing technique.

### Q3 [MEDIUM PRIORITY]: What should each level's output format look like?

- Level 1 (flag only): numbered issue list? inline annotations?
- Level 2 (suggest): original with comments? side-by-side?
- Level 3 (copy edit): edited text with highlights? diff view?
- Level 4 (developmental): restructured text with editorial notes?

What formats work best in a chat interface vs. as downloadable artifacts?

### Q4 [MEDIUM PRIORITY]: What existing AI editing tools exist?

Grammarly, ProWritingAid, Hemingway — what level are they operating at?
Any Claude/GPT editing prompts that successfully constrain to levels?
The "identify issues, fix them yourself" workflow — anyone systematized it?

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Editing Level Spec" — what each level
touches and doesn't, with before/after examples.

---

*Target length: 2,000-2,500 words. Deepest on Q1 and Q2 — the level
definitions and rewrite-prevention are the skill's core.*
```

---

### Skill 14: meeting-distiller

```
# Meeting Distiller Skill — Research Prompt

## Goal

I'm building a Claude skill that turns meeting transcripts into action
artifacts — not summaries. Decisions made, action items with owners, open
questions, key disagreements, and the one thing that mattered most. A
document you drop into Slack or your project management tool.

## Critical Constraint

"Summary" is the failure mode. The output is a PROJECT MANAGEMENT ARTIFACT,
not a shorter version of what was said. The test: can someone who wasn't in
the meeting know exactly what to do next from reading this?

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What does a great post-meeting artifact look like?

Find 4-5 strong meeting output formats from different contexts:
- Amazon's meeting memo culture
- Fellow.app, 15Five meeting templates
- What do executive assistants capture that AI summaries miss?
- Agile standup/retro output formats
- The difference between "what was said" and "what was decided"

For each: sections, level of detail, and what makes it actionable.

Search: meeting notes best practices, meeting action items template,
Amazon meeting memo format, post-meeting artifact, "meeting minutes"
vs "meeting actions," executive assistant meeting notes.

### Q2 [HIGH PRIORITY]: What's the optimal output structure?

Evaluate these candidate sections — which are essential, which are optional?
- Decisions made (with who decided)
- Action items (owner + deadline + context)
- Open questions (unanswered, needs follow-up)
- Key disagreements (who, what, resolved or not)
- Parking lot (raised but deferred)
- The one thing that mattered most (editorial judgment)
- Sentiment/energy read (useful or gimmicky?)

What do people actually reference when they go back to meeting notes?

### Q3 [MEDIUM PRIORITY]: How to handle messy real-world transcripts?

- Speaker identification errors
- Implicit decisions (nobody said "decided" but everyone moved on)
- Cross-talk, tangents, side conversations
- Very long meetings (60+ min) — different approach needed?
- Varying transcript quality (Otter vs Fathom vs manual notes)

### Q4 [MEDIUM PRIORITY]: What existing meeting tools produce and where they fall short?

Fathom, Otter.ai, Granola, Fireflies, glebis Meeting Analyzer skill.
For each: what they output, what's missing, what users complain about.

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Meeting Artifact Template v1" — the
output structure with section specs and a brief example.

---

*Target length: 1,500-2,000 words. Deepest on Q1 and Q2 — the template
IS the skill.*
```

---

## Category 5: Career & Professional

### Skill 15: interview-coach

```
# Interview Coach Skill — Research Prompt

## Goal

I'm building a multi-mode Claude skill for interview preparation: JD
analysis, question generation, mock interviews with real scoring, and salary
negotiation scripts. Anti-sycophantic by design — "Great answer!" is banned.

## Critical Constraint

Mock interview feedback must be SPECIFIC and ACTIONABLE. "Good structure but
weak on specifics" is not enough. "Your answer to 'Tell me about a time you
led a team' scored 2/5 on Substance because you named no metrics. Here's a
rewrite using your actual experience: [specific rewrite]." That's the bar.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What predicts interview success, and how should mock scoring work?

- Research on what actually predicts interview performance
- The noamseg/interview-coach-skill scores on Substance, Structure,
  Relevance, Credibility, Differentiation — is this the right rubric?
  Analyze the repo if accessible.
- STAR vs SOAR vs CAR answer frameworks — which produces the strongest
  answers according to interviewer research?
- Should mock interviews be timed? How to simulate follow-up questions?

Search: interview performance predictors research, mock interview scoring
rubric, STAR method effectiveness, behavioral interview answer quality,
noamseg interview-coach-skill GitHub, interview scoring framework.

### Q2 [HIGH PRIORITY]: Salary negotiation — what frameworks produce results?

Find the 3-4 strongest evidence-based negotiation approaches:
- Chris Voss techniques (Never Split the Difference)
- Patrick McKenzie's salary negotiation advice
- Research on first-offer anchoring effects
- Scripts for specific scenarios: countering first offer, competing offers,
  equity negotiation, remote work negotiation

For each: the technique, example language, and evidence of effectiveness.

Search: salary negotiation script, Chris Voss negotiation technique,
counter offer language, "never split the difference" salary, negotiation
anchoring research, Patrick McKenzie salary.

### Q3 [MEDIUM PRIORITY]: JD analysis — what hidden signals should the skill extract?

- What do JDs reveal about actual priorities (not just listed requirements)?
- Red flags in JDs
- How to generate likely interview questions from JD language
- Skills-match analysis: emphasis strategy when gaps exist

### Q4 [MEDIUM PRIORITY]: What existing interview tools exist and what's the gap?

noamseg/interview-coach-skill, Pramp, Interviewing.io, Big Interview,
community prompts. For each: approach and what's missing.

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Interview Coach Modes Spec" — the distinct
modes, what each produces, and how they connect.

---

*Target length: 2,000-2,500 words. Deepest on Q1 and Q2 — the scoring
rubric and negotiation scripts are the highest-value outputs.*
```

---

### Skill 16: career-experiment

```
# Career Experiment Skill — Research Prompt

## Goal

I'm building a Claude skill that designs low-stakes career experiments.
Instead of binary career decisions ("should I switch to product management?"),
it produces 3 testable experiments you can run in your current role within
2 weeks.

## Critical Constraint

The output must be EXPERIMENTS, not advice. Each experiment has: a testable
hypothesis, a specific action, a time bound, and clear success/failure
signals. "Shadow a PM for a day" is an experiment. "Think about whether
you'd enjoy PM" is not.

## Research Questions (in priority order)

### Q1 [HIGH PRIORITY]: What does experiment-based career exploration look like in practice?

Find the 3-4 strongest methodologies:
- "Designing Your Life" (Burnett & Evans, Stanford d.school) — their
  "prototype experiences" concept. What specific experiment types do
  they recommend?
- Lean Startup applied to careers — who's written about this?
- How do successful career pivoters actually test before committing?
  (Case studies, not theory)
- Dee McCrorey's Micro-Experiments skill — analyze the approach

For each: experiment types, time frames, and how they define "signal."

Search: Designing Your Life prototype experience, career experiment
lean startup, "test career" before switching, career pivot experiment,
micro-experiments career, low-risk career exploration.

### Q2 [HIGH PRIORITY]: What experiments can you actually run INSIDE a current role?

Build a taxonomy of experiment types:
- Volunteering for cross-functional projects
- Informational interviews (structured how?)
- Shadow days
- Side projects in the target domain
- Writing/speaking about the target area
- Taking on adjacent responsibilities
- Pro bono or volunteer work in the target field

For each: effort level, signal quality, and risk to current role.

### Q3 [MEDIUM PRIORITY]: Common career transitions and their experiment patterns

For these 5 common transitions, what experiments work?
- IC → manager
- Technical → product
- Corporate → startup/freelance
- Career change to new field
- Employee → founder

Do patterns differ meaningfully, or is there a universal experiment
structure?

### Q4 [MEDIUM PRIORITY]: What makes a good experiment vs. a useless one?

- Testable hypothesis (what specifically are you testing?)
- Time-bounded (how long before you have a signal?)
- Clear success/failure criteria (not "see how it feels")
- Reversible (low downside if it doesn't work)
- What distinguishes a genuine experiment from "just thinking about it"?

---

## Output Format

Per question: Findings, Sources, Confidence.

## Final Section: Key Design Decisions

5-7 tradeoff decisions. Then: "Experiment Design Template" — the structure
for one career experiment (hypothesis, action, timeline, success signal,
failure signal, next step either way).

---

*Target length: 1,500-2,000 words. Deepest on Q1 and Q2 — the experiment
taxonomy is the skill's core IP.*
```
