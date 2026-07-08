# 60-Minute Workshop — Facilitator Run-of-Show

**Slides:** `60-min-workshop-slides.pptx` (import to Google Slides) — **primary script + copy-paste**  
**App:** http://localhost:8080 — govern, workflow card, agent build lab (reference)  
**You.com APIs:** https://you.com/platform → **API Playground** (facilitator-led walkthrough)  
**Define inputs:** in **Hermes** during install + test — not the workshop app

---

## Rule: slides + playground + live Hermes setup. Close = Discord only.

| In the room (60 min) | Not in this workshop |
|----------------------|----------------------|
| You.com API playground walk (Search → Contents → Research) | App Full Demo Chain as primary API demo |
| Live Hermes desktop install + define inputs + MCP + test | Workshop app inputs form (express track) |
| Join [You.com Discord](https://discord.gg/2C4WgryxSD) + intro post | 30-day / 90-day community plans |

---

## Timing (55 min content + 5 min buffer = 60)

| Min | Step | Action |
|-----|------|--------|
| 0–3 | Welcome | Story on slides. Demo company in playground: **AMD**. |
| 3–18 | **You.com Playground** | Open https://you.com/platform. Walk Search → Contents → Research. **Slides 5–11** (APIs + MCP bridge). |
| 18–23 | Govern | App: review gates. Reference **slide 12** (skills + connectors) and **slide 13**. |
| 23–26 | Workflow Card | Generate → Download (optional if short on time). |
| 26–52 | **Hermes Live Setup** | `install.sh` → MCP → define inputs → test. **Slides 14–18**. |
| 52–57 | Close | **Discord only** — join link + intro post. |
| 57–60 | Buffer | MCP debugging |

---

## You.com Platform Playground (3–18 min)

**Open:** https://you.com/platform → API Playground

Use **AMD** as the demo company. Attendees pick their own company and **brief goal** later when they run `/account-action-brief` in Hermes.

| API | What to show | Example |
|-----|--------------|---------|
| **Search** | Structured JSON — titles, URLs, snippets | `AMD data center Instinct MI350 earnings` |
| **Contents** | Markdown from a URL from Search | AMD press release URL |
| **Research** | `output.content` + `output.sources` | "What are key AMD strategic signals for a renewal conversation?" |

**Say:** "We run APIs manually in the playground so you see each step. Slides 8–9 show how MCP automates the same chain in Hermes."

**Before Hermes install:** Show **slide 12** — skills define WHAT; connectors define what's ALLOWED. After `install.sh`, optionally open `SKILL.md` for 1 min.

---

## Hermes Desktop — live setup (26–52 min)

**Everyone completes in the room:**

```bash
cd workshop-app/hermes-desktop
chmod +x install.sh
./install.sh
```

1. Restart Hermes — confirm `/account-action-brief` appears
2. Add MCP: `https://api.you.com/mcp` — enable `you-search`, `you-contents`, `you-research`
3. **Define inputs** in the test command (**slides 14 + 17**):

```
/account-action-brief

company: AMD
website: https://www.amd.com
goal: Prepare for an upcoming customer meeting — understand recent strategic signals and decide what actions the account team should consider.
output_audience: internal
```

**Brief goal presets** — ask attendees to pick one and customize:
- **Renewal** — prepare for renewal conversation, risks, expansion angles
- **Outbound** — research for outbound sequence or first meeting
- **Competitive** — competitive positioning and displacement triggers
- **Partner** — partner opportunity, co-sell, ecosystem fit

4. Run the command — watch tool calls and six-section output

**Minimum success:** six sections, source URLs, Draft status, tool calls visible.

**Circulate at MCP wiring** — most failures happen here.

---

## Close (52–57 min) — Discord only

**Say:**

> "You walked the You.com APIs in the playground, installed Hermes, defined your inputs, and ran a governed account brief. Join the You.com Discord — introduce yourself and say you came from this workshop."

**Discord:** https://discord.gg/2C4WgryxSD

---

## If running long

| Cut first | Saves |
|-----------|-------|
| Workflow card → "download from app later" | 3 min |
| Finance Research in playground | 3–5 min |

| **Never cut** | |
|---------------|--|
| Playground API walk | |
| Hermes install + define inputs + MCP + one test brief | |
| Discord join | |

---

## Pre-workshop

```bash
cd workshop-app
./preflight.sh
python build_60min_slides.py
./run.sh
```

- Import `60-min-workshop-slides.pptx` into Google Slides
- Confirm https://you.com/platform playground loads
- Confirm attendees have Hermes desktop installed or can install
