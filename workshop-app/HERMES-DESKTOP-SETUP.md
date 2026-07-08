# Hermes Desktop Setup

Install the workshop skill pack into **Hermes Agent** (desktop app or CLI) — **live in the workshop room**.

## What's included (4 skills)

| Skill | Slash command | Purpose |
|-------|---------------|---------|
| account-action-brief | `/account-action-brief` | Main workflow — You.com evidence → six-section brief |
| meeting-prep | `/meeting-prep` | Optional — calendar-triggered briefs (not covered in 60-min close) |
| community-pulse | `/community-pulse` | Facilitator weekly digest for alumni community |
| workshop-60min | `/workshop-60min` | 60-min agenda inside Hermes |

## Install (everyone runs live — slide 12)

```bash
cd workshop-app/hermes-desktop
chmod +x install.sh
./install.sh
```

Skills copy to `~/.hermes/skills/`. Restart Hermes if needed.

## Wire You.com MCP (live — slide 13)

1. Add MCP server: `https://api.you.com/mcp`
2. Enable: `you-search`, `you-contents`, `you-research`
3. Attach only these tools to `/account-action-brief`

## Define inputs + test run (live — slides 11 & 14)

**Inputs are defined in Hermes** when you run the skill — not in the workshop app.

```
/account-action-brief

company: AMD
website: https://www.amd.com
goal: Prepare for an upcoming customer meeting — understand recent strategic signals and decide what actions the account team should consider.
output_audience: internal
```

**Brief goal presets** (customize for your use case):
- **Renewal** — renewal conversation prep
- **Outbound** — first meeting / sequence research
- **Competitive** — positioning vs competitors
- **Partner** — partner / co-sell opportunity

Confirm: six sections, real URLs in Claims & Sources, review status = Draft.

## Related

- `FACILITATOR-60MIN.md` — minute-by-minute live flow
- `AGENT-BUILD-GUIDE.md` — step-by-step agent build reference
- `COMMUNITY-CONTINUATION.md` — Discord close (only required follow-up)
