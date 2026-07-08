# Agent Build Guide — Live in the 60-Minute Workshop

**Goal:** Every attendee leaves with a working `/account-action-brief` skill in Hermes.

**Format:** **Hands-on live** — all six steps in the room (~26 min). Slides have copy-paste commands.

**Define inputs in Hermes** — company, website, brief goal, and output_audience go in the test command (not the workshop app).

**Hermes desktop (recommended):** `HERMES-DESKTOP-SETUP.md` + slides 11–14.

---

## Before the build step

- [ ] You.com APIs seen in **platform playground**
- [ ] Hermes Agent desktop app installed and logged in
- [ ] `YDC_API_KEY` in Hermes MCP or org-provided key

---

## Six steps (all live in the 60-min session)

### 1. Prerequisites (~2 min)
- Hermes open and logged in
- You.com API key ready for MCP

### 2. Install skill pack (~3 min)

```bash
cd workshop-app/hermes-desktop
chmod +x install.sh
./install.sh
```

Restart Hermes. Confirm `/account-action-brief` appears.

### 3. Instruction (~1 min)
- **Desktop:** skip — included in installed `SKILL.md`
- **Studio path only:** paste Packaging Prompt from app

### 4. Wire You.com MCP (~5 min)

```
Server: https://api.you.com/mcp
Tools: you-search, you-contents, you-research
```

### 5. Connector permissions (~3 min)
- **Read-only:** You.com APIs, CRM read, docs
- **Draft-only:** email, Slack, CRM draft
- **Blocked:** auto-send, auto-CRM-update

### 6. Define inputs + test run (~8 min)

**Define in the Hermes command** — pick company and brief goal:

```
/account-action-brief

company: AMD
website: https://www.amd.com
goal: [Renewal | Outbound | Competitive | Partner — customize for your use case]
output_audience: internal
```

**Goal examples:**
- Renewal: "Prepare for renewal — recent signals, risks, expansion angles"
- Outbound: "Research for outbound — first meeting talking points"
- Competitive: "Competitive positioning vs [vendor]"
- Partner: "Partner opportunity — co-sell and ecosystem fit"

---

## Verification — minimum bar to leave

- [ ] Skill runs without errors
- [ ] You.com tool calls visible
- [ ] All **six output sections** present
- [ ] **Claims & Sources** has real URLs
- [ ] Review status = **Draft**

---

## Facilitator tips

- **Circulate** at step 4 (MCP) — most failures here
- **Pause at step 6** — give 2 min for attendees to write their goal before running
- **Slides** are the source of truth for copy-paste blocks
