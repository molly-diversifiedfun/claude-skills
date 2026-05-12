# Kit files — supporting knowledge for the AI Build Partner

These four files are companion knowledge for the AI Build Partner. They get uploaded to a Claude.ai Project (or ChatGPT Project) **alongside** the main system prompt (`exports/claude-project.md`):

| File | Purpose |
|---|---|
| `01-brand-guide.md` | Voice rules, banned vocabulary, framework canon. The Build Partner reads this to know what words to never use. |
| `02-voice-dna.md` | Molly's sentence rhythm + style fingerprint — used when the Build Partner produces output in Molly's voice (Standalone + Ship It Kit modes, never in Marketing OS mode where the buyer's own voice is used). |
| `03-audience-personas.md` | The 4 client archetypes (Overcommitter, Perfectionist, Burnout Cycler, Scattered Starter) × tech persona frames. Used for diagnosis. |
| `04-user-context-template.md` | The blank template you fill in with your own project specifics. This is *your* file — edit it as your project progresses, re-upload to the Project after every Phase 0–3 template. |

## Where these came from

These files originate in `ship-it-system/ai-build-partner-kit/` (the IP source-of-truth repo). They're copied into this skill folder so the skill is a complete install bundle — one folder, all the pieces.

When you update the canonical source files in `ship-it-system/ai-build-partner-kit/`, regenerate the copies here. (TODO: automate this sync.)

## Install paths

**Claude Code (developers):**
```bash
git clone https://github.com/molly-diversifiedfun/claude-skills.git
cp -r claude-skills/ai-build-partner ~/.claude/skills/
```
The skill is now installed. Everything — SKILL.md, modules, templates, exports, kit-files — is in one place.

**Claude.ai or ChatGPT Project (no-code):**
1. Open `exports/claude-project.md` from this folder (or the matching Notion page in The Ship It System)
2. Copy contents → paste into your Project's Custom Instructions
3. Upload these 4 kit files into your Project Knowledge
4. Customize `04-user-context-template.md` with your project info before uploading

That's the install. Total time: ~5 minutes.
