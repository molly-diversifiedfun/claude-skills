# PRD: devil's-advocate

## Problem

AI agrees with you 60% of the time (SycEval benchmark). When told to "be honest" or "be critical," the adversarial stance decays within 3-5 exchanges. This isn't a prompting failure — it's a three-layer training artifact: RLHF encodes agreement as quality, RL optimization amplifies the bias, and attention decay dilutes instructions over conversation length. Anthropic's own evaluation shows Opus 4.5 escapes a sycophantic pattern only 10% of the time. Every existing adversarial AI tool (Devil's Advocate GPTs, sparring partner prompts) fails at the same point: maintaining genuine pushback past turn 5.

## Solution

A durable adversarial thinking partner built on architectural prevention, not prompt-based delay. Uses a structured challenge report format that creates commitments the model can't retreat from, combined with per-turn mandate reinforcement. Offers multiple critique frameworks (steel-manning, pre-mortem, WWHTBT, red teaming) selected based on the user's situation.

## Design Decisions (from research)

| Decision | Choice | Why |
|----------|--------|-----|
| Always adversarial vs. calibrated | **Always adversarial** | Calibration introduces the mode-switching decision where sycophancy re-enters. The skill's entire job is to challenge — if you want agreement, use regular Claude. |
| Single-model vs. multi-agent | **Single-model with per-turn mandate reinforcement** | Multi-agent is the proven prevention technique, but this skill must work in Claude.ai (no tools). Compensate with: structured output format (creates commitments), per-turn mandate at end of context (recency bias exploitation), and the SCAN technique (generate instruction-linked tokens before responding). |
| Critique idea vs. critique thinking | **Both, labeled separately** | Section 1 critiques the proposal. Section 2 identifies the cognitive patterns behind it. Labeling prevents the psychoanalysis feeling — "Here's what's wrong with the plan" and "Here are the thinking patterns that might be steering you" are clearly different functions. |
| Structured report vs. conversation | **Structured report first, conversation second** | The report establishes the adversarial baseline with structural commitments. Follow-up conversation explores specific findings. This two-phase approach anchors the adversarial frame before any drift-prone dialogue. |
| End with strengths vs. questions | **End with stress-test questions** | Research consistently shows closing praise dilutes critique impact (Schwarz HBR, MacMillan Ivey 2025). End with 3 uncomfortable questions the user must answer. Strengths acknowledged earlier in the report, never at the end. |
| Confidence-rated critiques | **Yes, with guardrails** | Epistemic honesty increases credibility for domain experts. But to prevent confidence deflation as a sycophancy escape: minimum confidence of 5/10 for any included critique. Below 5/10 = don't include it, don't soften it. |
| User-invoked vs. always-on | **User-invoked** | This is a skill, not a mode. The user explicitly asks for adversarial analysis. Consent is important for something designed to be uncomfortable. |

## Architecture: Anti-Sycophancy by Design

The skill uses three reinforcing mechanisms to prevent decay:

### 1. Structured Output Commitments
The challenge report format forces the model to fill labeled sections:
- **Fatal Flaw** section MUST contain exactly one critical-severity critique
- **Significant Risks** section MUST contain 2-3 items
- **Stress-Test Questions** MUST end the report (never strengths)

These are structural commitments — the model can't produce an empty Fatal Flaw section without violating the format. The format IS the anti-sycophancy mechanism.

### 2. Per-Turn Mandate Reinforcement
The adversarial mandate appears at the END of the skill's instructions (exploiting recency bias, per Basyal et al. COLM 2024). Critical rules are stated twice — once at the beginning, once at the end — to counter "lost in the middle" attention dynamics.

### 3. Steel-Man-First Protocol
Before any critique, the skill MUST articulate the strongest possible version of the user's argument. This serves two functions:
- Proves understanding (user feels heard → reduced defensiveness)
- Creates a higher bar for critique (must challenge the strongest version, not a straw man)

If the steel-man is weak, the critique has no credibility. This forces quality.

## Interaction Model

### Step 1: Intake (1 min)
User presents their idea, plan, argument, or decision.

Skill responds with exactly one question:
"Before I challenge this, what's at stake? Is this a casual idea you're exploring, or something you're about to commit time/money/reputation to?"

This calibrates the depth of analysis without calibrating intensity (which stays high).

### Step 2: Framework Selection (automatic)
Based on the user's input, the skill selects the primary critique framework:

| Situation | Framework | Why |
|-----------|-----------|-----|
| Business plan or strategy | **Pre-Mortem** | "This failed spectacularly — here's why" depersonalizes critique |
| Decision between options | **WWHTBT** | Maps conditions for success, tests weakest assumptions |
| Argument or position | **Steel-Man + Red Team** | Understand the strongest version, then attack it |
| Creative work or pitch | **Named Adversary Personas** | Critique from the skeptical customer, hostile reviewer, competitor |
| "I'm not sure about this" | **Socratic** | Questions that surface the user's own doubts |

The skill announces the framework: "I'm going to run a pre-mortem on this. The crystal ball says this failed. Let's figure out why."

### Step 3: Steel-Man (mandatory)
Before any critique:

> **Your argument at its strongest:**
> [2-3 paragraph articulation of the best possible version of the user's position, filling gaps, adding the best available evidence, interpreting ambiguities charitably]
>
> Does this capture your position? If I'm missing something, tell me now — I want to challenge the strongest version, not a straw man.

Wait for confirmation. If user corrects, update the steel-man. Only proceed to critique after confirmation.

### Step 4: Challenge Report

```
## Fatal Flaw
[The single biggest reason this fails. One paragraph. Direct.]
Confidence: [5-10]/10 — [one sentence on reasoning basis]

## Significant Risks
1. [Risk name]: [2-3 sentences. Specific, not generic.]
   Confidence: [5-10]/10
2. [Risk name]: [2-3 sentences]
   Confidence: [5-10]/10
3. [Risk name]: [2-3 sentences]
   Confidence: [5-10]/10

## Thinking Patterns to Watch
[1-2 cognitive patterns identified in the user's reasoning:
confirmation bias, anchoring, sunk cost, motivated reasoning,
availability bias, etc. Named and explained without psychoanalyzing.]

## What Would Have to Be True
[3-5 conditions that must hold for this to succeed.
Flag which ones the user is least confident about.]

## Stress-Test Questions
1. [Uncomfortable question the user must answer honestly]
2. [Question that probes the weakest assumption]
3. [Question about what they're avoiding thinking about]
```

### Step 5: Follow-Up Discussion
After the report, the user can:
- Ask to go deeper on any risk ("Expand on Risk 2")
- Challenge a critique ("I think your Fatal Flaw is wrong because...")
- Request a different framework ("Run the red team version instead")
- Ask for mitigation strategies ("How would I address Risk 1?")

Follow-up stays in adversarial mode. If the user challenges a critique and makes a strong case, the skill can revise — but MUST replace it with a different critique, never leave the Fatal Flaw empty.

### Anti-Sycophancy Rules (hardcoded)

1. **Never open with praise.** The steel-man serves this function. Additional affirmation is sycophancy.
2. **Never use "Great question!" or "That's a really interesting point."** These are filler affirmations.
3. **Never apologize for being critical.** The user invoked this skill specifically for critique. "I apologize for my oversight" is the documented apology loop (JD Meier).
4. **Never end with strengths.** The report ends with stress-test questions. Always.
5. **Never produce an empty or trivially weak Fatal Flaw.** If the idea genuinely has no fatal flaw, say: "I can't find a fatal flaw — which concerns me. Here's what I'd want to verify: [specific tests]."
6. **If the user pushes back on all critiques, DO NOT FOLD.** Restate the strongest critique with additional evidence. If the user makes a genuinely strong case, revise — but replace, never remove.
7. **Minimum confidence for any included critique: 5/10.** Below 5 = don't include it. This prevents confidence deflation as a sycophancy escape.
8. **Never say "You make a valid point" as a transition to agreement.** This is the documented sycophancy entry phrase.

## Success Criteria

- Maintains genuine adversarial stance through at least 10 exchanges (vs. 3-5 for existing tools)
- Fatal Flaw section always contains a substantive critique (never empty, never trivially weak)
- Users report the critique changed their thinking or plan (not just "interesting")
- The stress-test questions are specific enough that the user can't answer them in one word
- The skill never produces the apology loop ("You're right, I apologize for my oversight")

## What This Skill Does NOT Do

- Provide balanced analysis (that's regular Claude — this skill is adversarial by design)
- Replace domain expertise (it challenges thinking patterns, not technical claims)
- Work as an always-on mode (user must explicitly invoke it)
- Guarantee its critiques are correct (confidence ratings are epistemic honesty, not accuracy claims)

## Pairs With

- **decision-maker**: devil's-advocate challenges the idea → decision-maker structures the choice between options
- **self-interview**: devil's-advocate challenges externally → self-interview clarifies internally
- **mental-models**: devil's-advocate is one model (adversarial) → mental-models offers 12 different lenses
