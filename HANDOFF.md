# Handoff

Most recent entry first.

---

## 2026-06-29

**What happened this session:**
- Created TASKS.md and HANDOFF.md (these files)
- Extracted Prompt Factory into standalone skill: `prompt-factory/SKILL.md` + `README.md`
- Created `session-resume/SKILL.md` + `README.md`
- Updated root README.md and CHANGELOG.md with new skills
- Weekly report delivered to Notion (Gmail MCP still send-only label tools — no send capability)

**Active branch:** `claude/youthful-johnson-eag594` — pushed to remote, needs PR to main

**State of the library:**
- 27 skills total (was 25; added prompt-factory + session-resume)
- All 27 have SKILL.md; prompt-factory and session-resume also have README.md
- `ai-build-partner` is the active paid-tier skill; all free library skills are stable

**Open item:**
- ADR 003 close-out: detection contracts landed (`b131fb1`). Need to verify Kit first-sale integration — check that Kit's first-sale webhook/trigger is wired to the contracts defined in ABP. This is verification, not new code.

**Next session should:**
1. Open `TASKS.md` and pick up ADR 003 close-out
2. Run `git log --oneline -10` to see if anything landed since this session
3. Check if the `claude/youthful-johnson-eag594` PR merged
