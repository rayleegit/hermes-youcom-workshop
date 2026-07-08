# Calendar connectors — meeting-prep

## Read-only (required for /meeting-prep)

| Connector | Access | Use for |
|-----------|--------|---------|
| Google Calendar | Read events | Title, time, attendees, description |
| Microsoft Outlook | Read events | Same |
| CalDAV | Read events | Org calendar systems |

## Read-only (optional enrichment)

| Connector | Use for |
|-----------|---------|
| CRM read | Link meeting → account → company name |
| Internal docs | Sanitized context (never cite as public evidence) |

## Draft-only delivery

| Channel | Use for |
|---------|---------|
| `hermes_thread` | Brief in Hermes before the call (default) |
| `slack_dm` | DM to workflow owner |
| `email_self` | Email Draft to owner's work address |
| `doc_draft` | Notion/Google Doc prep page |

## Blocked (pilot phase)

- Calendar write, invite edits, attendee changes
- Email or Slack to external attendees
- Auto-CRM-update, auto-send outreach
- Attaching brief to external calendar invite without human approval

## First pilot rule

Calendar read + deliver to **owner only**. One meeting, one brief, one review.
