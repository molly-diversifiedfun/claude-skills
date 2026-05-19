# AI Build Partner Kit

Canonical source for the 5 knowledge files clients drop into their Claude Project or ChatGPT custom GPT to turn it into an Unstuck Build Partner.

## What's in here

| File | Purpose |
|---|---|
| `00-master-system-prompt.md` | The 9-layer execution spec — identity, philosophy, methodology, output rules. Goes in as the system prompt / project instructions. |
| `01-brand-guide.md` | Tone, banned vocabulary, Unstuck-specific framing rules. |
| `02-voice-dna.md` | Sentence rhythm, voice patterns, examples — what Molly actually sounds like. |
| `03-audience-personas.md` | The 4 client archetypes (Overcommitter, Perfectionist, Burnout Cycler, Scattered Starter). |
| `04-user-context-template.md` | The blank template a client fills in with their own project specifics (handed off from templates T01–T05). |

## How clients get this

Clients never visit this repo. They download the packaged kit at:

```
https://www.unstuckwithmolly.com/portal/ai-build-partner-kit.zip
```

That URL is a normal static asset served from the unstuck repo's `public/portal/`. Pipeline:

1. Edit any file in `ai-build-partner-kit/` here and push to `master`
2. `.github/workflows/sync-kit-to-unstuck.yml` checks out the unstuck repo, copies the .md files into `unstuck/public/portal/ai-build-partner-kit/`, builds the zip, and opens a PR
3. Review and merge the PR in unstuck → Vercel deploys → kit is live at the public URL

The PR step is intentional — every kit change gets a one-click QA gate before clients see it.

## Initial setup (one-time, already done)

The sync Action needs a Personal Access Token (PAT) to push to the private unstuck repo.

**To create / rotate the PAT:**

1. Go to https://github.com/settings/personal-access-tokens/new
2. Token name: `ship-it-system → unstuck kit sync`
3. Expiration: 1 year (set a calendar reminder to rotate)
4. Repository access: **Only select repositories** → `molly-diversifiedfun/unstuckwithmolly`
5. Repository permissions:
   - **Contents:** Read and write
   - **Pull requests:** Read and write
   - **Metadata:** Read-only (auto-selected)
6. Generate token, copy it
7. In ship-it-system: Settings → Secrets and variables → Actions → New repository secret
   - Name: `UNSTUCK_REPO_PAT`
   - Value: paste the token

Action also needs a workflow setting in the unstuck repo:
- Settings → Actions → General → Workflow permissions → enable **"Allow GitHub Actions to create and approve pull requests"**

## Editing rules

- This dir is the single source of truth. The Notion mirrors (under the AI Build Partner page) get re-synced from here.
- Numbered prefixes (`00-`, `01-`, ...) drive the upload order clients see when they unzip.
- Master System Prompt structure is locked at 9 layers (L1–L9). Don't add new top-level sections without revisiting the spec.
- The README in this dir is excluded from the client zip — keep it for editor docs only.

## Editing rules

- This dir is the single source of truth. The Notion mirrors (under the AI Build Partner page) get re-synced from here.
- Numbered prefixes (`00-`, `01-`, ...) drive the upload order clients see when they unzip.
- Master System Prompt structure is locked at 9 layers (L1–L9). Don't add new top-level sections without revisiting the spec.
