# Research Brief: learn-anything

A skill that teaches any topic through active recall instead of lecturing. The user asks "what is X?" and the skill refuses to just answer — it surfaces what they already know, fills gaps through questioning, and confirms understanding through teach-back.

This brief synthesizes ~25 sources across cognitive science, intelligent tutoring systems, and existing learning tools to ground the design.

---

## Q1 [HIGH]: Which learning science principles are encodable in a chat interface?

### Findings

A single chat session can credibly implement five of the seven techniques the prompt asked about. Two require multi-session infrastructure the skill won't have.

**Testing effect (retrieval practice).** The strongest evidence in the entire learning-science literature. Rowland's 2014 meta-analysis pegged the effect at g = 0.50; Schwieren et al. (2017) at d = 0.56; Karpicke & Blunt (2011) reported d = 1.50 for concept-mapping-vs-retrieval comparisons. Roediger & Karpicke's seminal 2006 study: students who took practice tests remembered 50% more than students who repeatedly studied. Robust across samples, materials, formats, and retention intervals. **Translation to chat: every session must end with the learner producing answers from memory, not recognizing them on a page.**

**Feynman Technique (teach-back / learning by teaching).** No single large RCT, but the components are heavily evidenced. Self-explanation (Chi et al. 1994) significantly improves problem-solving. Studying with the expectation of teaching (Nestojko et al. 2014) produces better organization of knowledge. Fiorella & Mayer (2013): students who learned by teaching developed deeper understanding than those who learned for themselves. The "teach an inanimate object" variant works — the audience doesn't have to be real. **Translation: the skill plays the role of "the person being taught" and the user does the explaining.**

**Elaborative interrogation.** Dunlosky et al.'s 2013 meta-review rated this "moderate utility" — strong but with a narrow applicability ceiling. The mechanism: prompting learners to generate "why is this true?" or "why does this make sense?" explanations. Effects are larger when (a) elaborations are precise rather than vague, (b) prior knowledge is higher, and (c) the learner generates the explanation rather than receiving it. **Translation: after every concept the user encounters, ask "why does that work?" or "why isn't it the opposite?" before moving on.**

**Desirable difficulty (Bjork).** The umbrella principle that effortful recall, spacing, and interleaving create stronger storage even though they feel harder in the moment. Meta-analysis of 29 studies: effect size g = 0.74. The interleaving result is striking: when learning volume formulas for 3D shapes, the interleaving group hit 63% accuracy on a delayed test versus 20% for the blocked-practice group. **Translation: the skill must resist the user's preference for easy questions and smooth answers. Discomfort is the mechanism, not a bug.**

**Zone of proximal development (Vygotsky).** The band of tasks the learner cannot do alone but can do with help. Operationalized via scaffolding: contingent (offered when needed), graduated (minimal hints first), reversible (withdrawn as competence consolidates). Modern intelligent tutoring systems calibrate difficulty to keep learners in this zone. **Translation: when the user gets stuck, don't reveal the answer — drop one rung of the scaffolding ladder (hint → leading question → partial answer → full answer only as last resort).**

**Spaced repetition.** Massive evidence base, but the unit of analysis is days/weeks, not minutes. A single session can't space anything. **Punted: the skill produces a "next session" plan and asks the user to come back, but doesn't pretend to manage spacing itself.**

**Interleaving.** Same problem at the strict definition (mixing distinct skills across sessions). A weak version is feasible inside a session — interleave question types within a topic rather than blocking all "definitions" then all "applications." **Partial implementation: vary question type, not subject.**

### Sources

- [Roediger & Karpicke 2006 — Test-Enhanced Learning](https://journals.sagepub.com/doi/10.1111/j.1467-9280.2006.01693.x)
- [Schwieren et al. 2017 — Testing Effect Meta-Analysis](https://journals.sagepub.com/doi/10.1177/1475725717695149)
- [Dunlosky et al. 2013 — Improving Students' Learning With Effective Learning Techniques](https://pubmed.ncbi.nlm.nih.gov/26173288/)
- [Bjork & Bjork 2011 — Making Things Hard on Yourself](https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/EBjork_RBjork_2011.pdf)
- [Fiorella & Mayer 2013 — The Relative Benefits of Learning by Teaching](https://www.researchgate.net/publication/358237141_Feynman_Technique_as_a_Heutagogical_Learning_Strategy_for_Independent_and_Remote_Learning)
- [Vygotsky ZPD — Educational Technology summary](https://educationaltechnology.net/vygotskys-zone-of-proximal-development-and-scaffolding/)

### Confidence: **HIGH** — testing effect and desirable difficulty are among the most replicated findings in cognitive psychology. Feynman/elaborative interrogation are derivative but the underlying mechanisms are evidenced. Spacing/interleaving correctly punted to multi-session.

---

## Q2 [HIGH]: How should it assess current knowledge and calibrate difficulty?

### Findings

**Self-assessment is unreliable, especially for novices.** The Dunning-Kruger effect (Kruger & Dunning 1999) shows low performers systematically overestimate their ability. Students doing poorly on tests less accurately predict which questions they will get right than do high-performers. So asking "rate your knowledge of X from 1-10" produces noise. The signal is in **performance**, not in self-report.

**Use diagnostic questions as the primary signal.** A diagnostic question is a focused multiple-choice or short-answer item with distractors written around the most common misconceptions. The wrong answer reveals which mental model the learner is operating with. Craig Barton's diagnostic-questions methodology (used in UK math education) and Carpentries' lesson-development training both converge on the same structure: one concept per question, distractors mapped to specific known errors, no ambiguity. The distractors carry the diagnostic value, not the correct answer.

**Bloom's two-sigma — handle with care.** Bloom's 1984 paper claimed 1:1 mastery tutoring produced a 2.0 standard-deviation improvement over classroom instruction. This number is the foundational mythology of AI tutoring (Khanmigo, every "AI tutor" pitch deck). But: it has never been replicated. The original studies were largely unpublished dissertation work. The Education Next 2024 review concluded most of the d=2.0 was driven by holding tutees to a 90% mastery threshold before advancing, not the 1:1 format itself. Recent replications in real-world settings (Ukraine 2023-24, ~10,000 students) found tutoring effects of 0.40-0.49 SD — real and substantial, but not two sigma. **The actionable lesson from the two-sigma literature is mastery-before-advance, not the magic of 1:1.**

**Calibrate dynamically from response quality, not from response correctness alone.** Khanmigo and other Socratic tutors use response *patterns* (hesitation, partial correctness, the specific wrong answer chosen) to update difficulty. The skill should treat every user response as a calibration signal: if the explanation is fluent and complete, raise difficulty. If the explanation is fragmented or hits the wrong distractor, drop one rung of scaffolding.

**The Khanmigo lesson.** 700K users by 2024-25, mastery gains comparable to human tutors in pilots. But the documented failure mode: the Socratic method "requires patience" — younger learners and those who just want help can find question-after-question annoying. **Implication: the skill must give the user an explicit escape hatch ("just tell me") and respect it after one challenge, not refuse repeatedly.**

### Sources

- [Kruger & Dunning 1999 — Unskilled and Unaware of It](https://sites.lsa.umich.edu/sasi/wp-content/uploads/sites/275/2015/11/krugerdunning99.pdf)
- [Bloom 1984 — The 2 Sigma Problem](https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf)
- [Education Next 2024 — Two-Sigma Tutoring: Separating Science Fiction from Science Fact](https://www.educationnext.org/two-sigma-tutoring-separating-science-fiction-from-science-fact/)
- [Nintil — Systematic Review of Mastery Learning, Tutoring, Direct Instruction](https://nintil.com/bloom-sigma/)
- [Carpentries — Diagnosing Misconceptions with MCQs](https://carpentries.github.io/lesson-development-training/misconceptions-mcqs.html)
- [Gierl et al. 2017 — Developing Distractors for MCQs](https://journals.sagepub.com/doi/10.3102/0034654317726529)
- [Khanmigo Review 2025 — AIModelsRank](https://www.aimodelsrank.com/reviews/khan-academy-khanmigo)

### Confidence: **HIGH** on Dunning-Kruger and diagnostic-question methodology. **MEDIUM** on dynamic calibration — the mechanism is sound but the specific thresholds (when to step up, when to drop a rung) are skill-design choices, not empirical findings.

---

## Q3 [MEDIUM]: How should it structure a learning session?

### Findings

**Chunk size: 3-5 concepts per session, max.** Working memory holds about 7 chunks but can only actively work on 4 (Miller 1956). Cognitive load research consistently shows attention drops sharply after ~10 minutes of continuous input and again at 60-90 minutes. Translation: one "lesson" = one concept, broken into 3-5 sub-points, with retrieval checkpoints between sub-points.

**Syllabus: reveal progressively, with the first checkpoint visible.** Showing a 30-step roadmap upfront triggers overwhelm. Showing nothing produces "are we there yet" anxiety. Compromise: name the destination ("by end of session you'll be able to explain X"), name the next checkpoint ("first we figure out what you already know about Y"), keep the rest hidden until earned.

**Session length: 20-30 minutes optimal for chat.** Long enough for the testing-effect cycle to play out (introduce → recall → correct → re-recall). Short enough to fit the cognitive-load ceiling. The skill should propose a length upfront and offer an explicit "we're at a good stopping point" callout around the 20-minute mark.

**Handling "just tell me the answer" pushback.** This is the load-bearing UX problem. Khanmigo's documented failure mode is being annoying about it. The pattern that works:
1. **First push**: redirect once. "I'd rather you try first — even a wrong guess gives me information about where to scaffold."
2. **Second push**: give a hint, not the answer.
3. **Third push**: give the answer and immediately follow with a recall-back question 30 seconds later.

The user has to feel the skill is on their side, not gatekeeping. The phrase "even a wrong guess gives me information" is honest about *why* the refusal helps them — it isn't withholding for its own sake.

### Sources

- [Cognitive Load Theory — MCW Faculty Quick Guide](https://www.mcw.edu/-/media/MCW/Education/Academic-Affairs/OEI/Faculty-Quick-Guides/Cognitive-Load-Theory.pdf)
- [Content Chunking — Conestoga TLC](https://tlconestoga.ca/content-chunking/)
- [Chunking Lectures — Times Higher Ed Campus](https://www.timeshighereducation.com/campus/chunking-lectures-its-no-brainer)

### Confidence: **MEDIUM** — chunk-size and session-length numbers are well-evidenced for classroom contexts; their direct mapping to chat is reasoned, not empirically tested.

---

## Q4 [MEDIUM]: What existing learning tools/skills exist?

### Findings

**Learn Faster Kit (cheukyin175 / hluaguo on GitHub).** Claude Code skill. Uses a "FASTER" acronym (Forget, Act, State, Teach, Enter, Review). Ships personalized syllabi, spaced-repetition scheduling, and auto-generated exercises. Strength: actually integrates spaced repetition because Claude Code can write to disk. Gap for our purposes: heavy dev-tool framing (built for "technical skills"), assumes you'll come back daily, and produces a syllabus first rather than starting from interrogation. Doesn't have the hard refusal-to-lecture mechanism — it leans on workflow scaffolding rather than dialog discipline.

**Claude Learning Mode (Anthropic, April 2025 → general release).** Built into Claude.ai as a style preset. Asks clarifying questions, breaks ideas into sub-prompts, delays final answers until the user engages. Drew Bent (Anthropic education lead): designed to combat "brain rot" from passive copy-paste use. Strength: ships in the product, no install. Gap: it's a style, not a structured protocol — no diagnostic questions, no teach-back checkpoint, no calibration loop. It nudges Socratically but doesn't *enforce* retrieval.

**Khanmigo (Khan Academy + GPT-4).** ~700K users by 2024-25. Socratic-by-design: refuses to give direct answers, asks "what's your first step?" Documented mastery gains comparable to human tutors in pilots. Documented failure: too patient — frustrates younger users and those who just want a quick answer. Closed product, math-and-school-subject focused.

**Duolingo.** Owns the spaced-repetition + gamification slot. Not a model. Wrong shape for our skill (drill-based, not concept-based; vocabulary, not understanding).

**Khan Academy Mastery Progression.** Pre-AI. The "must hit 5-in-a-row before advancing" pattern. This is essentially the Bloom mastery-threshold mechanism that drove most of the original 2-sigma effect. Worth borrowing structurally even though the AI skill version has to relax "5-in-a-row" to something more flexible.

### The gap our skill fills

Learn Faster Kit assumes a dev workflow. Claude Learning Mode is a vibe, not a protocol. Khanmigo is closed, K-12, and math-shaped. Nothing in the public Claude-skill ecosystem implements the **"refuse to lecture, force teach-back, calibrate from misconceptions"** loop as an explicit, structured protocol that works in a single ad-hoc 20-minute session for any topic.

### Sources

- [Learn Faster Kit on GitHub](https://github.com/hluaguo/learn-faster-kit)
- [Anthropic — Introducing Claude for Education / Learning Mode](https://www.anthropic.com/news/introducing-claude-for-education)
- [VentureBeat — Claude Learning Mode Makes Students Do the Thinking](https://venturebeat.com/ai/anthropic-flips-the-script-on-ai-in-education-claude-learning-mode-makes-students-do-the-thinking)
- [Khanmigo Review 2025](https://www.aimodelsrank.com/reviews/khan-academy-khanmigo)

### Confidence: **HIGH** on the gap analysis. Existing options are real and useful, but none implement the refusal-loop protocol explicitly.

---

## Key Design Decisions

| Decision | Choice | Why |
|---|---|---|
| **Lecture vs. interrogate by default** | **Always interrogate first.** Even if the user says "just teach me X," the first move is "what do you already know about X — even a vague hunch?" | Active recall has 2x the retention of passive review (Roediger & Karpicke). The skill exists to prevent the passive-consumption failure mode. |
| **Self-assessment vs. diagnostic questions** | **Diagnostic questions only.** "Rate your knowledge 1-10" is banned. Replace with a 1-2 question diagnostic whose distractors map to common misconceptions. | Dunning-Kruger: low performers can't accurately self-assess. Distractors carry diagnostic value (Carpentries, Gierl et al.). |
| **Single-session vs. multi-session** | **Optimize for one 20-30 min session.** Produce a "come back tomorrow for X" plan but don't pretend to manage spacing. | Spacing requires infrastructure the skill doesn't have. Honest punt > fake spacing. |
| **Show full syllabus vs. progressive disclosure** | **Progressive.** Name destination + next checkpoint only. Reveal next chunk after the current one is recalled successfully. | Cognitive load (Miller's 4±1) + Khanmigo finding that overwhelm produces dropout. |
| **Hard refusal vs. graduated escape hatch** | **Three-strike escape: redirect → hint → answer-then-recall.** Never refuse three times in a row. | Khanmigo's documented failure: refusing too long feels like gatekeeping. The honest framing ("a wrong guess tells me where to scaffold") works better than dogma. |
| **Generic "teach me" vs. specific outcome** | **Always pin a concrete outcome upfront.** "By the end you'll be able to [explain / apply / debug] X." | ZPD requires knowing the target. Concrete outcomes also enable the teach-back checkpoint at the end (you teach back the *outcome*). |
| **Mastery threshold vs. time-box** | **Mastery-before-advance, with explicit "good stopping point" callouts.** | This is the actual mechanism behind the 2-sigma effect (Education Next 2024). Time-boxing alone produces the classroom failure mode the skill is built to fix. |

---

## Learning Loop Design

The optimal cycle for a single session:

```
1. PIN THE TARGET (1 min)
   - "What specifically do you want to be able to do by the end?"
   - If vague: offer 2-3 concrete outcome options. User picks one.
   - State session length: "Roughly 20-30 minutes. Sound right?"

2. DIAGNOSE (3-5 min)
   - 1-2 diagnostic questions with distractors mapped to common misconceptions.
   - Open with the easier one; the second adapts based on the first answer.
   - DO NOT ask "rate your knowledge 1-10."
   - Goal: identify (a) what they know, (b) what misconception they hold, (c) where the ZPD edge is.

3. TEACH IN CHUNKS (10-15 min, looped 3-5 times)
   For each chunk:
   a. Introduce ONE sub-concept in 2-4 sentences.
   b. Ask an elaborative-interrogation question: "Why would that be true?" / "Why isn't it the opposite?"
   c. If user can answer: advance to next chunk.
   d. If user is stuck: drop one rung — hint, then leading question, then partial answer.
      Never give the full answer on the first stuck moment. Give it on the third escalation if needed,
      then immediately re-ask 30 seconds later.

4. TEACH-BACK CHECKPOINT (3-5 min)
   - "Now teach it back to me. Pretend I'm a smart friend who's never heard of this.
     Use your own words, not mine."
   - Listen for: jargon they're parroting without grounding, missing causal links, residual misconception.
   - If teach-back is fluent and accurate: advance.
   - If teach-back has gaps: name the specific gap, ask one more elaboration, re-do teach-back.

5. STOPPING POINT + NEXT (2 min)
   - Confirm the original outcome is met (or not — both are honest).
   - Suggest one next session topic + one between-session retrieval prompt
     (e.g., "Tomorrow, before opening this again, try to explain X out loud. Then come back.").

ESCAPE HATCH (active throughout):
   - User says "just tell me": redirect once with the honest framing.
   - User pushes again: give a hint.
   - User pushes a third time: give the answer + immediately ask a recall-back question.
   - Never refuse three times in a row.
```

The whole protocol has one design principle: **every concept the user encounters must pass through their own production at least once before the session ends.** Recognition is not learning. Production is.
