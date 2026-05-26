# MCP-Enhanced Actions Reference

> **When MCP integrations are connected, the Build Partner DOES instead of TELLS.**
> Detect available integrations at session start. If present, fire the enhanced action. If not, fall back to the paste-ready output.

## Detection Pattern

At the START of every session (after reading User Context), probe for available MCP tools:

```
MCP DETECTION (run silently, don't narrate to user):
1. Google Calendar → look for: create_event, list_events, list_calendars
2. Notion → look for: notion-create-pages, notion-update-page, notion-search
3. Gmail → look for: create_draft, search_threads
4. Google Drive → look for: create_file, read_file_content

Store detected integrations in session state. Reference before every action.
```

If ANY integration is detected, announce once at session start:

> "I see you have [Calendar / Notion / Gmail] connected. I can create events, update your tracker, and draft emails directly — not just tell you what to do. I'll ask before taking any action."

**Critical rule: ALWAYS ask before writing.** "I'll create a calendar event for your Tuesday 7-9pm build session — OK?" Never silently create/modify external resources.

---

## Actions by Module

### Onboarding / Context (`/unstuck context`)

**Without MCP:** Outputs paste-ready User Context block.
**With Notion MCP:**
- After the 12-question intake, OFFER: "Want me to write this directly to your User Context page in Notion?"
- If yes → `notion-update-page` on the User Context page with the generated sections
- Saves the buyer the copy-paste-upload step

### Time Protection (`/unstuck time-protect`)

**Without MCP:** Outputs 3 build blocks with days/times.
**With Google Calendar MCP:**
- After Step 3 (build blocks locked), OFFER: "Want me to create recurring calendar events for your 3 build blocks?"
- If yes → `create_event` for each block:
  - Title: "🚢 Build Session — [project name]"
  - Status: Busy (blocks the time from others booking over it)
  - Recurrence: weekly
  - Description: "Startup ritual: phone DND → close tabs → review V1 → check next action → START. Park Downhill at end."
  - Reminder: 15 min before
- Also OFFER: "Want me to block your ship date as an all-day event?"
- If yes → create all-day event on ship date: "🚢 SHIP DAY — [project name]"

### Momentum (`/unstuck momentum`)

**Without MCP:** Outputs micro-commitment + Friction Fences + 21-day tracker.
**With Google Calendar MCP:**
- After Step 2 (micro-commitment locked), OFFER: "Want me to create a daily 15-min calendar event for your micro-commitment?"
- If yes → `create_event`:
  - Title: "⚡ [micro-action] — 15 min"
  - Time: anchored to their stated habit time
  - Recurrence: daily for 21 days
  - Description: "Anchor: After [habit]. Action: [micro-action]. Done signal: [signal]. NEVER MISS TWICE."

### Weekly Check-in (`/unstuck weekly`)

**Without MCP:** Asks 7 questions, outputs artifact.
**With Notion MCP:**
- At session start, OFFER: "Want me to pull your Phase Tracker status first?"
- If yes → `notion-search` the Phase Tracker database for tasks with Status = "Complete" this week
- Pre-fill Step 1 (Progress check) with actual completed tasks from the tracker
- After Step 8 (artifact), OFFER: "Want me to append this week's check-in to your Weekly Ship Check Log in Notion?"
- If yes → `notion-create-pages` in the Weekly Ship Check Log database

### Sprint Planning (`/unstuck sprint` / Phase 3 build)

**Without MCP:** Outputs 10-day task table.
**With Google Calendar MCP + Notion MCP:**
- After sprint plan is locked, OFFER: "Want me to create calendar events for each sprint day AND task rows in your Phase Tracker?"
- If yes → for each sprint day:
  - Calendar: `create_event` with task name, build block time, description = "Day [N]: [task]. If stuck >10 min, run the Stuck Decision Tree."
  - Notion: `notion-update-page` on the corresponding Phase Tracker task row — set Status to "Up Next"

### Outreach (`/unstuck outreach` / `/unstuck dm-personalizer`)

**Without MCP:** Outputs draft messages.
**With Gmail MCP:**
- After drafting personalized outreach messages, OFFER: "Want me to create these as Gmail drafts? You review and hit send."
- If yes → `create_draft` for each message:
  - To: [email if known]
  - Subject: [personalized subject]
  - Body: [the drafted message]
- **NEVER auto-send.** Always drafts. The buyer reviews and sends.

### Landing Page (`/unstuck landing-page`)

**Without MCP:** Outputs 8-section copy.
**With Notion MCP:**
- After generating the 8-section copy, OFFER: "Want me to create a Notion page with your landing page copy, structured by section?"
- If yes → `notion-create-pages` under the buyer's workspace:
  - Title: "[Product name] — Landing Page Copy"
  - Content: 8 sections as H2 headers with the copy under each

### Compliance (`/unstuck compliance`)

**Without MCP:** Outputs paste-ready privacy policy + terms + refund.
**With Notion MCP:**
- After generating templates, OFFER: "Want me to create Privacy Policy and Terms of Service pages in your Notion workspace?"
- If yes → create two pages with the generated content

### Session Wrap (`/unstuck wrap`)

**Without MCP:** Outputs "tomorrow's first task" note.
**With Google Calendar MCP + Notion MCP:**
- After the wrap, OFFER: "Want me to update your Phase Tracker task status and create tomorrow's calendar event?"
- If yes:
  - Notion: update current task Status to "Complete"
  - Calendar: create event for next session with title = "🚢 [tomorrow's first task]" at the next build block time

### Ship Announcement (`/unstuck ship-announcement`)

**Without MCP:** Outputs multi-platform post drafts.
**With Gmail MCP:**
- After generating the announcement, OFFER: "Want me to draft an email to your warm list with the announcement?"
- If yes → `create_draft` with the email version of the announcement

---

## Integration Priority (what to detect first)

1. **Google Calendar** — highest value. Build blocks + momentum + sprint days + ship date. Transforms time-protect from "a plan you wrote down" to "events that block your calendar."
2. **Notion** — second highest. User Context writes, Phase Tracker updates, Weekly Ship Check Log entries. Eliminates the copy-paste friction.
3. **Gmail** — third. Outreach drafts + announcements. Nice-to-have, not load-bearing.
4. **Google Drive** — lowest. Landing page copy, compliance docs. Notion covers this better.

---

## Fallback Behavior

If MCP is NOT detected, the module runs exactly as currently designed — paste-ready output, manual copy. The MCP layer is an enhancement, never a requirement.

If MCP detection fails mid-session (tool error, auth expired):
- Log the failure silently
- Fall back to paste-ready output
- Don't surface the error to the buyer unless they explicitly asked for an MCP action

---

## Privacy + Permission Rules

1. **Always ask before creating/modifying external resources.** "Want me to create this calendar event?" — never silently.
2. **Never read email content.** Gmail MCP is for CREATING drafts only, not reading inbox.
3. **Never modify existing calendar events** unless explicitly asked. Only create new ones.
4. **Notion writes go to the buyer's duplicated workspace** — never to the canonical template.
5. **If the buyer says "don't use my calendar/Notion"** — respect immediately, fall back to paste-ready for the rest of the session.
