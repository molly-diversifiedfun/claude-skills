# Followability Audit

**Point it at anything people are supposed to use — your landing page, onboarding flow, repo, course, habit tracker, internal process — and get a one-page diagnosis of where it's breaking down.**

The Color Check from [The Flamingo Effect](https://www.theflamingoeffect.com).

## The Problem

When people aren't doing the thing, the instinct is to assume they aren't motivated, didn't understand the value, or need better copy. That's almost always wrong. The system has a gap. The gap has a specific location. Generic "user research" doesn't surface it because it tells you what people felt, not where the friction sits in the flow.

## What It Does

Walks any system through 5 rungs and scores each 0–5:

| Rung | Question |
|------|----------|
| **Understand** | In 10 seconds, can a new person say what this is and what to do next? |
| **Believe** | Is there proof — not claims — at the moment of decision? |
| **Do** | Is the first action obvious, small, and completable right now? |
| **Repeat** | Is progress visible, and is there a system that makes coming back likely? |
| **Share** | Is the outcome packaged into something that travels? |

The output is:
- **A scored table** with one-sentence evidence per rung (cited from the actual system)
- **Primary + secondary problem named** — using the "fix the crack closest to the ground" rule (lower rungs gate higher rungs)
- **A ranked fix list** — smallest possible 48-hour interventions, not redesigns
- **A Monday plan** — the single first move, ordered for compounding effect

## How to Use It

### In Claude.ai

1. Open a Claude Project
2. Upload `SKILL.md` + the contents of `references/` as Project Knowledge
3. Start with: *"Use followability-audit on [paste the URL, README, course outline, flow description, or screenshot]"*

### In Claude Code

```bash
cp -r followability-audit ~/.claude/skills/followability-audit
```

Then: *"Audit this for followability: [paste]"* or *"Run a color check on [URL/file/process]"*

The skill activates on triggers like "audit this," "is this followable," "color check," "where does this break," "find the crack," "why aren't people doing the thing."

## What Makes This Different

- **Diagnostic, not prescriptive opinion.** The skill cites specific elements — quotes actual text, references actual UI, names actual file paths — so the output is auditable.
- **Closest-to-the-ground rule.** Won't recommend Share fixes when Do is broken. Won't recommend Believe fixes when Understand is broken.
- **48-hour fix bias.** No "you should rebuild the funnel" recommendations. Smallest possible interventions only.
- **Generous scoring is banned.** A "3" out of charity is a "1" in reality. The user is asking because something is broken — be honest.

## Pairs With

- **[devils-advocate](/devils-advocate/)** — Pair when you want adversarial review of the audit's conclusions
- **[ai-build-partner](/ai-build-partner/)** — When the audit reveals a deeper product problem, route there for scope cut + sprint plan
- **[mental-models](/mental-models/)** — When the diagnosis surfaces a structural problem (not just surface), use mental-models for the deeper analysis
- **[decision-maker](/decision-maker/)** — When the fix list forces a real choice, structure it as a one-page decision brief

## License

MIT. The Color Check methodology is from The Flamingo Effect by Molly Shelestak.
