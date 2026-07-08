---
name: meeting-prep
description: Calendar-triggered account briefs delivered before customer meetings
version: 1.0.0
metadata:
  hermes:
    tags: [youcom, calendar, meeting-prep, sales, workshop]
    category: youcom-workshop
    requires_toolsets: [web]
---

# Meeting Prep

## When to Use

Use when you want an account brief **before a customer meeting** without manually running `/account-action-brief` each time.

Requires:
- `/account-action-brief` skill installed (or equivalent procedure)
- Calendar connector wired **read-only** (Google Calendar, Outlook, or CalDAV)
- You.com MCP enabled (`you-search`, `you-contents`, `you-research`)

Trigger examples:
- `/meeting-prep lookahead_hours: 24`
- "Prep briefs for my customer meetings tomorrow"
- "Meeting prep for my 2pm AMD call"

## Required Inputs

- **lookahead_hours** (optional, default: 24) — how far ahead to scan calendar
- **calendar** (optional, default: primary) — which calendar to read
- **delivery** (optional: `hermes_thread` | `slack_dm` | `email_self` | `doc_draft`) — where Draft lands
- **meeting_filter** (optional) — e.g. "customer-facing only", domain allowlist

## Procedure

1. Read upcoming calendar events within `lookahead_hours` (read-only — never write to calendar).
2. Filter to customer-facing meetings — skip internal-only unless explicitly requested.
3. For each meeting, extract `company_name` from title, attendees, description, or CRM link.
4. If company is ambiguous, ask once — do not guess.
5. For each company, run the **account-action-brief** procedure via You.com MCP.
   - Load `references/account-action-brief-delegate.md` for the delegated steps.
6. Prefix every output:
   `Meeting prep — [DATETIME] — [MEETING TITLE] — [COMPANY]`
7. Deliver each brief to the configured **draft-only** channel — owner only, never external attendees.
8. Set review status: **Draft** on every brief.
9. Do not modify calendar events, meeting invites, or CRM records.

## Output Format

Per meeting, return the standard six-section account brief (see account-action-brief output schema) plus:

```markdown
## Meeting context
- **When:** [DATETIME]
- **Title:** [MEETING TITLE]
- **Company:** [COMPANY]
- **Delivery:** [CHANNEL]
- **Review status:** Draft
```

For multiple meetings in one run, use a digest header:

```markdown
# Meeting prep digest — [DATE]
[N] customer meetings in next [lookahead_hours]h
```

## Governance

Load connector rules: `references/calendar-connectors.md`

**Read-only:** Calendar list/read, You.com APIs, CRM read  
**Draft-only:** Slack DM to self, email to self, prep doc, CRM note draft  
**Blocked:** Calendar write, invite edits, email to attendees, auto-CRM-update

## Delivery

See `references/delivery-options.md`. Default: `hermes_thread` (brief waiting in Hermes before the call).

## Pitfalls

- Do not brief every calendar event — filter customer-facing meetings only
- Do not deliver to external attendees — owner review first
- Do not skip You.com evidence because calendar metadata exists
- Re-run if meeting time changed significantly (stale brief risk)

## Verification

- [ ] Correct company per meeting
- [ ] Six sections + Claims & Sources with URLs
- [ ] Delivered only to owner (draft-only channel)
- [ ] Calendar event unchanged
- [ ] Review status = Draft
