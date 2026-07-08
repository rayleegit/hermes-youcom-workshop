# Hermes Live Setup — 60-Minute Workshop

**Default path:** Everyone installs Hermes desktop, **defines inputs in the test command**, and runs `/account-action-brief` **live in the room** (26–52 min).

**Facilitator pre-work:** Run through install + MCP + define inputs + test once before the session.

---

## Facilitator pre-flight (~15 min, day before or morning of)

1. Confirm `install.sh` works on your machine
2. Wire You.com MCP: `https://api.you.com/mcp`
3. Test with defined inputs:
   ```
   /account-action-brief
   company: AMD
   website: https://www.amd.com
   goal: Prepare for renewal conversation — recent signals and risks
   output_audience: internal
   ```
4. Confirm: tool calls visible, six sections, Draft status

---

## During the workshop (26–52 min)

**Slides 11–14 are the script.**

| Min | Activity | What attendees do |
|-----|----------|-------------------|
| 26–34 | `install.sh` | Install skill pack |
| 34–41 | Wire MCP | Add server + enable three tools |
| 41–45 | **Define inputs** | Pick company + brief goal (slide 11) |
| 45–52 | Test brief | Run `/account-action-brief` with their inputs |

**Say at define inputs:**
- "Company and goal go in the Hermes command — this is how you tailor every brief."
- "Pick Renewal, Outbound, Competitive, or Partner — then customize the goal line."
- "Six sections every run — Snapshot through Review Notes."

---

## Room setup

- [ ] Slides on **display 1** (define inputs slide 11 before install slides)
- [ ] Workshop app on **display 2** (govern, agent build lab reference)
- [ ] Hermes open on each attendee machine
- [ ] Playground tab: https://you.com/platform

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Skill not visible | Restart Hermes after `install.sh` |
| No tool calls | MCP not connected |
| Weak brief | Check goal line — vague goals produce vague briefs |

---

## What NOT to do

- Don't use workshop app inputs form in the 60-min express track — define in Hermes
- Don't skip the goal line — it tailors You.com Search and Research queries
