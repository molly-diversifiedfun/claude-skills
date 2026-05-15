# Funnel Ad Creator

**Stop generating one ad at a time. Generate the whole ad bible in one session — 12-16 production-ready scripts across every funnel stage, plus the 4-week test plan to deploy them.**

## The Problem

Single-ad generation produces single-ad fatigue. By the time you've split-tested three creatives, your audience has seen each one 23 times and your CPM is climbing. Real ad performance comes from a system: multiple hooks per pain point, multiple pain points per persona, multiple personas per funnel stage, and a deployment schedule that rotates them before fatigue sets in.

## What It Does

Three-phase guided session:

**Phase 1 — Discovery.** Builds the persona × pain point matrix. You name your customer; the skill pressure-tests until pains are specific (not "they're frustrated" — "they spent six hours building a Notion dashboard that nobody on their team opened").

**Phase 2 — Hook bank.** Generates 8 categories of hooks — pattern interrupts, callouts, contrarian takes, before-and-afters, and four more. Each hook is assigned to specific persona × pain combinations.

**Phase 3 — Ad bible.** 12-16 storyboarded scripts across:
- **TOFU** — cold-traffic awareness ads
- **MOFU** — mid-funnel education + objection-handling
- **BOFU** — direct-response, decision-stage ads
- **Retargeting** — cart-abandon, view-content, lookalike

Each ad ships with: visual direction (frame by frame), scripted dialogue, text overlays with timing, caption copy, and a hook recommendation matched to your goal (DM conversions, sales, leads, opt-ins).

Plus: a **4-week testing protocol** for deployment — what to launch when, what to kill at what threshold, what to rotate.

## How to Use It

### In Claude.ai

1. Open a Claude Project
2. Upload `SKILL.md` as Project Knowledge
3. Start with: *"Use funnel-ad-creator for my [product]"* — be ready to answer the discovery questions

### In Claude Code

```bash
cp -r funnel-ad-creator ~/.claude/skills/funnel-ad-creator
```

Then: *"Use funnel-ad-creator on this product: [paste positioning + offer + target persona]"*

## What Makes This Different

- **System, not single-shot.** Generates a 4-week supply of ads, not one creative you'll burn through in a weekend
- **Hook + ad mapped to funnel stage** — no more running BOFU "buy now" ads to cold audiences
- **Storyboard format** — visual direction column means a junior editor can produce these without a creative brief

## Pairs With

- **[build-irresistible-offer](/build-irresistible-offer/)** — Lock the offer FIRST. Bad offer + great ads = expensive negative ROAS
- **[instagram-reels-framework](/instagram-reels-framework/)** — For organic short-form to support the paid funnel
- **[humanize-ai-writing](/humanize-ai-writing/)** — Mandatory pass on every script before filming — AI vocabulary tanks ad CTR
- **[nano-banana](/nano-banana/)** — Generate the visual asset variations called out in the storyboard

## License

MIT. Methodology integrates Hormozi value frameworks with standard direct-response funnel architecture.
