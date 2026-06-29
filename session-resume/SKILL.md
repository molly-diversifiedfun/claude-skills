# Session Resume

> Reconstruct working state in under 60 seconds. Pick up exactly where you left off.

## What this is

Every new Claude Code session starts cold. No memory of what you were building, what was decided, what's half-done. Session Resume reads the handoff artifacts from your last session and tells you — and Claude — exactly what's live, what's pending, and what to do first.

Run this at the start of any session where continuity matters.

## What to say

```
/session-resume
```

Or if the skill isn't installed as a slash command:

```
Read these files and reconstruct my working state:
- HANDOFF.md (what the last session left behind)
- TASKS.md (what's in progress and queued)
- Run: git log --oneline -10

Then tell me:
1. What was I working on?
2. What's the first thing to do right now?
3. Anything I should know before touching any file?

Be brief. I need orientation, not a summary.
```

## What Claude reads

In order of priority:

| File | What it tells you |
|------|------------------|
| `HANDOFF.md` | What the last session did, what's open, what the next session needs to know |
| `TASKS.md` | What's in progress, what's up next, what's done |
| `git log --oneline -10` | Whether anything landed since the last handoff was written |
| `.unstuck/context.md` | If you're working in `ai-build-partner` — your full project context |

If none of these files exist, Claude should say so and ask what you're working on before doing anything else.

## Output format

Claude's reconstruction should be short:

```
## Resuming: [project name or "this repo"]

**Last session** (HANDOFF.md, [date]):
[1-2 sentences on what happened]

**Open right now:**
- [Item 1 from TASKS.md in-progress section]
- [Item 2]

**First move:**
[Single most important thing to do — the obvious next action]

**Watch out for:**
[Only if there's something genuinely non-obvious — a pending PR, a broken state, a decision left hanging]
```

No filler. If the state is simple, the reconstruction should be 5 lines.

## Maintaining the artifacts this skill reads

Session Resume only works if the artifacts stay current. Two-part system:

**At the end of every session** — update HANDOFF.md with:
- What you did
- What's open
- What the next session needs to know before touching anything

**In TASKS.md** — keep it honest:
- Move items to Done when they're done
- Don't let In Progress accumulate items that haven't moved in weeks
- The point is orientation, not a complete project log

If neither file exists, Session Resume will tell you that and ask you to create them. The `weekly-ship-review` skill (coming) automates the HANDOFF.md update at session end.

## When you don't have HANDOFF.md or TASKS.md

Claude falls back to:

```
Read git log --oneline -20, ls the root directory, and read CLAUDE.md if it exists.

Give me:
1. What this repo is (3 words)
2. What changed most recently (last 3 commits)
3. What to check before I start working
```

Not as good as a real handoff, but better than starting completely blind.

## If you're in an ai-build-partner session

Add this to the resume prompt:

```
Also read .unstuck/context.md and tell me:
- What's my project?
- What module was I in?
- What was the last thing I did or decided?
```

The context file has the full project state — product name, audience, price, what's been built, what's been validated.
