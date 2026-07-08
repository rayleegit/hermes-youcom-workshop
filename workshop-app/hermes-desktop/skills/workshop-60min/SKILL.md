---
name: workshop-60min
description: 60-min You.com + Hermes workshop guide inside Hermes desktop
version: 1.0.0
metadata:
  hermes:
    tags: [youcom, workshop, training, hermes]
    category: youcom-workshop
---

# 60-Minute Workshop Guide (Hermes Desktop)

## When to Use

- Facilitator coaching attendees through the live workshop from Hermes
- Attendee self-paced replay
- Community office hours

For the browser app (inputs, govern, agent build lab): run `workshop-app` locally at http://localhost:8080

## Live Agenda (60 min)

| Min | Topic | Action |
|-----|-------|--------|
| 0–3 | Welcome | You.com = evidence, Hermes = workflow |
| 3–18 | Playground | Walk Search → Contents → Research at you.com/platform (AMD demo) |
| 18–23 | Govern | Connector map + review gates → Draft |
| 23–26 | Workflow card | Generate + download (optional) |
| 26–52 | Hermes live | install.sh → MCP → **define inputs** → test `/account-action-brief` |
| 52–57 | Close | Join You.com Discord + intro post |

## In-room agent build (all 6 steps live)

1. Install skill pack: `references/install.md` or `install.sh`
2. Wire You.com MCP: `https://api.you.com/mcp`
3. Run `/account-action-brief` — verify six sections + Draft

## Slash commands after install

- `/account-action-brief` — run the workflow
- `/community-pulse` — facilitator weekly digest (optional)
- `/workshop-60min` — this guide

## After the workshop

Join the You.com Discord: https://discord.gg/2C4WgryxSD — introduce yourself in #introductions.

Optional self-paced depth: `references/post-event.md`

## Verification (minimum bar to leave workshop)

- [ ] `/account-action-brief` skill installed
- [ ] You.com MCP connected (tool calls visible)
- [ ] Test run: six sections + sources + Draft status
- [ ] Discord join link saved
