# Calendar-Triggered Meeting Prep

## When to use

- You have `/account-action-brief` working manually
- You want briefs **before customer meetings** without remembering to run the skill
- Calendar connector is wired **read-only**

## Procedure

1. Read upcoming calendar events (lookahead: 24h or 2h — org policy).
2. Filter to customer-facing meetings (title patterns, attendee domains, CRM link).
3. Extract `company_name` from event title, description, or linked account.
4. If ambiguous, ask once — do not guess.
5. Run standard account-action-brief procedure (You.com Search → Contents → Research).
6. Prefix output: `Meeting prep — [DATETIME] — [TITLE]`.
7. Deliver to configured **draft-only** channel (Slack DM, email to self, doc).
8. Set review status: **Draft**. Do not edit the calendar event or email attendees.

## Connector rules

| Access | Allowed |
|--------|---------|
| Calendar read | Yes |
| Calendar write / invite edit | No (pilot) |
| Email/Slack to self | Draft-only |
| Email to external attendees | Blocked |

## Delivery config (examples)

- `delivery: slack_dm` — DM brief to workflow owner
- `delivery: email_self` — email Draft to owner's work address
- `delivery: hermes_thread` — leave in Hermes for pre-meeting review

## Pitfalls

- Do not brief every internal meeting — filter customer-facing only
- Do not use stale briefs — respect freshness; re-run if meeting moved
- Do not skip human review because it was "automatic"

## Verification

- [ ] Brief references correct company for the meeting
- [ ] Delivered only to owner (not external attendees)
- [ ] Review status = Draft
- [ ] Calendar event unchanged
