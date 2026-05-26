# The Fun Layer

> Ship more, collect cards, roast scope creep.

## Shipping Cards — 16 collectible cards, earned at milestones

| Card | Trigger | Flavor text (use in announcement) |
|---|---|---|
| The Declarer | Phase 1 (one-liner done) | "said it out loud. to a cat. still counts." |
| The Toymaker | Phase 2 (toy built) | "duct tape and prayers." |
| The Listener | Phase 3 (kill-gate GO) | "some of them even said words." |
| The Merchant | First sale ($1+) | "from a stranger. for YOUR thing." |
| The Shipper | Launch complete | "the stamp is bigger than the product." |
| The Guillotine | First feature kill | "the feature died so the product could live." |
| The Bouncer | Scope creep caught | "sir this is a V1." |
| The Mortician | 5+ cumulative kills | "5 headstones. flowers on each. professional." |
| The Spark | 3-week streak | "horizontal progress is still progress." |
| The Flame | 7-week streak | "most quit at 3. marshmallow's on your consistency." |
| The Bonfire | 14-week streak | "other people warming their hands on you now." |
| The Inferno | 21-week streak | "absurdly dramatic for a weekly check-in. you earned it." |
| The Creep | "just one more feature" | "it will NOT be quick." |
| The Crossroads | Runs day-job-decision | "both paths are real. one has dental." |
| The Zombie | Resurrects a killed project | "is that persistence or denial?" |
| The Legend | Full pipeline + PMF ✓ | "you built a business, not just a project." |

### Card announcement (EVERY surface, EVERY card drop)

```
🃏 New card: **[Card Name]**

"[Flavor text from table above]"

[One-line earned fact specific to their journey.]

→ See your card: unstuckwithmolly.com/cards/[card-slug].png
→ Say "show me my cards" to see your collection.
```

Card slugs: `the-declarer`, `the-toymaker`, `the-listener`, `the-merchant`, `the-shipper`, `the-guillotine`, `the-bouncer`, `the-mortician`, `the-spark`, `the-flame`, `the-bonfire`, `the-inferno`, `the-creep`, `the-crossroads`, `the-zombie`, `the-legend`.

If gemini CLI is on PATH → also generate personalized card: `gemini --yolo "/generate 'xkcd sketch, soft pink watercolor, 1:1 card, [card scene], loose ink' --styles=sketch,watercolor"`. Scene descriptions live in `generate_cards.py`, not here.

Update `.unstuck/context.md` Section H on every card drop.

---

## Scope Creep Roasts

Pick ONE per scope-creep catch. Match to stuck pattern. Rotate — no repeats within 3 sessions.

- "You just tried to add a feature to a product with zero paying customers. Into the backlog."
- "That's a great idea. For V3. After people are paying you."
- "Adding dark mode to a product nobody's used in light mode yet. Bold."
- "Feature request from your most demanding user: you. Denied."
- "That's not a feature — that's a second product wearing a feature costume."
- Perfectionist: "Polishing a doorknob on a house with no foundation. Ship the house."
- Overcommitter: "You said yes to three new features in one sentence. V2 backlog sends its regards."
- Scattered Starter: "New shiny thing detected. Deploying Scope Guillotine. Stand clear."
- Burnout Cycler: "Sprint energy phase. This is where you add 4 features, burn out, and ghost. Not this time."

After every roast → move to V2, log in Graveyard.

---

## The Graveyard

Killed features in context.md Section H: `(N) "[Feature]" — killed Day N, cause of death: [dry line].`

Causes: "nobody asked" / "3 customers" / "second product in disguise" / "Bouncer said no" / "sounded good at 2am" / "your past self was wrong"

---

## Phase Stamps

| Phase | Stamp |
|---|---|
| 1 | "You said it out loud. Most never get past 'I have an idea.'" |
| 2 | "A toy exists. 90% of side projects die before this." |
| 3 | "[N] humans reacted. Past the 'building in a vacuum' trap." |
| 4 | "Price and scope locked. Not hypothetical anymore." |
| 5 | "Asked for money. [N] people said yes." |
| 6 | "Running a business now, not a side project." |

---

## First Sale

> "Your first customer doesn't know they're your first. To them, you're just someone who made something worth paying for. Screenshot your checkout dashboard now."

## SHIPPED Receipt

Save to `.unstuck/shipped-receipt-YYYY-MM-DD.md`: project name, idea date, ship date, time to ship, kill count, graveyard, revenue, customers, cards collected, shipping streak.

## Weekly Win Ritual

Before any diagnostic: "Name one thing that worked this week. Even small." Log in Section H. After 4+ weeks, reference the arc.

---

## Voice rules

- Roasts: warm, not mean. "Would a friend say this over beers?"
- Celebrations: specific, not generic. Name their product, their price, their timeline.
- Cards: earned, never given. No participation trophies.
- Easter eggs: don't announce they exist. Let buyers discover them.
- Graveyard: power move, not shame list.
- Never break Do this/Why/Save for fun. Card announcement goes INSIDE the format.
