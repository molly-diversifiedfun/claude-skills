# session-resume

Reconstruct working state at the start of a session. Pick up exactly where you left off.

## The problem it solves

Every Claude Code session starts cold. No memory of what was built, what's pending, what was decided. Without a resume pattern, you spend the first 10 minutes of every session reconstructing state — or worse, you start working before you have the full picture and break something.

## How it works

Point Claude at `HANDOFF.md`, `TASKS.md`, and `git log`. It reads them and gives you a concise orientation: what was happening, what's open, and the first thing to do. Takes under 60 seconds.

## Usage

```
/session-resume
```

Or paste the prompt from `SKILL.md` directly.

## What it reads

- `HANDOFF.md` — what the last session left behind
- `TASKS.md` — what's in progress and queued
- `git log --oneline -10` — what's actually landed
- `.unstuck/context.md` — if you're in an `ai-build-partner` session

## Keeping it working

Session Resume is only as good as the artifacts it reads. At the end of each session, update `HANDOFF.md` with what you did and what's open. The upcoming `weekly-ship-review` skill automates this.
