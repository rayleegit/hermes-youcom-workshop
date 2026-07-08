# Calendar-Triggered Meeting Prep

**Use case:** Deliver an account brief **before** a customer meeting — without manual triggering every time.

**Status:** Post-workshop extension (not built in the 60-min app). Document the pattern; wire in Hermes when ready.

---

## Why this helps

| Manual today | With calendar integration |
|--------------|---------------------------|
| Remember to run `/account-action-brief` | Brief runs when a meeting appears on your calendar |
| Copy brief into meeting notes | Draft lands in inbox, Slack, or a prep doc before the call |
| Stale prep if you forget | Fresh You.com evidence on a schedule (e.g. 24h or 2h before) |

This is the natural “automation payoff” after attendees finish the base `/account-action-brief` skill.

---

## The pattern (governed)

```
Calendar (read-only)
  → detect upcoming customer meetings
  → extract company name (title, attendees, CRM link, description)
  → run /account-action-brief (You.com MCP)
  → deliver Draft brief to you (not to the customer)
  → you review before the meeting
```

**Hermes automates:** detect meeting → run evidence chain → format brief → deliver to you.  
**You still do:** review sources, approve for internal use, decide what to bring into the call.

---

## Connector map (add to your workflow card)

| Bucket | Calendar integration |
|--------|----------------------|
| **Read-only** | Google Calendar, Outlook, CalDAV — list events, read title/attendees/description |
| **Draft-only** | Email to self, Slack DM, Notion/Docs prep page, CRM meeting note **draft** |
| **Blocked** | Auto-edit meeting invite, auto-email attendees, auto-CRM-update without review |

**First pilot rule:** Calendar read + brief delivered to **you only** — never to external attendees automatically.

---

## Suggested triggers

| Trigger | Best for |
|---------|----------|
| **24 hours before** | Strategic accounts — time to review and edit |
| **2 hours before** | High meeting volume — same-day freshness |
| **Daily digest (7am)** | “Tomorrow’s customer meetings” — one message, multiple briefs |
| **On-demand** | `/account-action-brief` when calendar MCP unavailable |

---

## Hermes skill extension

Install `/meeting-prep` from the desktop skill pack (`./install.sh` — included with account-action-brief).

Prerequisites:
- `/account-action-brief` working with You.com MCP
- Calendar connector **read-only** (Google Calendar or Outlook)

### Example with calendar wired

```text
/meeting-prep

lookahead_hours: 24
calendar: primary
delivery: slack_dm
```

### Example single meeting (no calendar MCP yet)

```text
Prep brief for my AMD call tomorrow at 2pm
```

Skill reference: `hermes-desktop/skills/meeting-prep/SKILL.md`

---

## Delivery options (draft-only)

1. **Slack DM to self** — fastest for reps living in Slack  
2. **Email to self** — good for calendar-heavy exec workflows  
3. **Notion / Google Doc** — link pinned in internal meeting prep folder  
4. **Hermes thread** — brief waiting when you open the app before the call  

Never attach the brief to the external calendar invite without human approval.

---

## Week 2+ community challenge

After you've run 3 manual briefs (Week 1):

1. Wire calendar **read-only** in Hermes (Google or Outlook connector)  
2. Run one brief triggered from a real upcoming meeting  
3. Post in You.com Discord: meeting type, delivery channel, one thing you caught in review  

---

## Facilitator one-liner (wrap-up or post-event)

> "The skill you built today is manual-on-demand. The next upgrade is calendar-triggered prep — same governed brief, delivered before your meetings. Read-only calendar, draft-only delivery, you review every time."

---

## Related

- `hermes-desktop/skills/meeting-prep/` — dedicated `/meeting-prep` skill  
- `account-action-brief/references/calendar-trigger.md` — lightweight variant
