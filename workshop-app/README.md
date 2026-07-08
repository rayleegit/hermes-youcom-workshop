# Account Action Brief Workshop App

A runnable, step-by-step teaching app for the Hermes + You.com `/account-action-brief` workshop.

**Core story:** You.com provides the live evidence. Hermes provides the governed workflow.

Walk attendees through 18 workshop steps, run live You.com API calls (Search → Contents → Research), **build a working Hermes agent hands-on**, and leave with a workflow card plus agent build kit.

## Quick Start

```bash
cd workshop-app
chmod +x run.sh
./run.sh
```

Open **http://localhost:8080** in your browser.

**60-minute live workshop?** Open http://localhost:8080 (default). See `FACILITATOR-60MIN.md`.  
**You.com APIs in session:** https://you.com/platform (platform playground — facilitator-led)  
**Hermes desktop app?** See `HERMES-DESKTOP-SETUP.md` — everyone installs live via `install.sh`.  
**Google Slides (60-min)?** Import `60-min-workshop-slides.pptx` — see `60-MIN-GOOGLE-SLIDES.md`.  
**Full 18-step deep dive?** http://localhost:8080?full=1 (self-paced reference)

The app works immediately in **demo mode** (saved sample data). For live API calls:

```bash
cp .env.example .env
# Edit .env and set YDC_API_KEY=your-key-here
./run.sh
```

## What It Does

The app teaches both platforms side by side throughout the workshop — not just APIs at the start and Hermes at the end.

### You.com features highlighted

| Feature | Where in the app |
|---------|------------------|
| Structured JSON web/news results | Step 5 — Web Search |
| Domain & freshness governance | Steps 4–5 — API matrix + Search |
| Clean page content (Contents) | Step 7 |
| Cited multi-source synthesis (Research) | Step 8 |
| Structured output_schema | Step 9 |
| Finance Research (optional) | Step 8 button |
| MCP for zero-code agent integration | Steps 4, 14 |

### Hermes features highlighted

| Feature | Where in the app |
|---------|------------------|
| Named reusable workflows (`/account-action-brief`) | Steps 1–3 |
| Stable inputs & output schema | Steps 2–3 |
| Tool orchestration (You.com + GTM connectors) | Steps 10–11 |
| Connector map (read/draft/blocked) | Step 11 |
| Review gates (4 approval states) | Step 12 |
| Workflow card packaging | Step 13 |
| Hermes skill/playbook prompt | Step 14 |
| **Hermes desktop skill pack** | Step 14 — install.sh or zip download |
| Quality scorecard & team rollout template | Steps 15–16 (champions) |
| Full lifecycle: Run → Integrate → Govern → Package → Pilot | Lifecycle panel |

### Workshop phases

| Phase | Steps | You.com focus | Hermes focus |
|-------|-------|---------------|--------------|
| **Define** | 1–3 | Company name seeds API queries | Job, inputs, output schema |
| **Discover** | 4–5 | API decision matrix + Web Search | Orchestrates Search as step 1 |
| **Inspect** | 6–7 | Source scoring + Contents | Enforces inspection habit |
| **Synthesize** | 8–9 | Research + structured output | Maps API output to brief schema |
| **Context** | 10 | Public evidence only | GTM connector orchestration |
| **Govern** | 11–12 | Source controls complement gates | Connector map + review gates |
| **Package** | 13–14 | APIs listed as allowed tools | Workflow card + Hermes skill |
| **Pilot** | 15–16 | Citation/freshness metrics | Scorecard + rollout plan |

## Facilitator Guide

### Before the workshop (15 min)

1. Clone or copy this package to the presentation machine.
2. Run `./run.sh` and confirm http://localhost:8080 loads.
3. Decide: **demo mode** (no key needed) or **live mode** (set `YDC_API_KEY`).
4. Project the app on a second screen or share your screen.
5. Default company is **AMD** — change it live during Step 2.

### Workshop timing (75–90 min)

| Min | Step | Title | Focus |
|-----|------|-------|-------|
| 0–5 | 0 | Welcome | Platform Spotlight + opening script |
| 5–14 | 1–3 | Define | Job, inputs, output schema |
| 14–18 | 4 | API Matrix | You.com API decision rule |
| 18–28 | 5 | Web Search | Live Search or Full Demo Chain |
| 28–40 | 6–7 | Inspect | Source scoring + Contents |
| 40–52 | 8–9 | Synthesize | Research + structured output |
| 52–58 | 10 | Team Context | Load sample context |
| 58–67 | 11–12 | Govern | Connector map + review gates |
| 67–77 | 13–14 | Package | Workflow card + Hermes prompt |
| 77–85 | 15–16 | Pilot | Scorecard + pilot plan |
| 85–90 | 17 | Wrap-Up | Download all artifacts |

**Full facilitator script:** see `FACILITATOR.md`

### Teaching moments to emphasize

**You.com:**
- Search discovers, Contents reads, Research synthesizes — each API has one job
- Snippets are LLM-ready; domain/freshness controls are governance levers
- Structured output_schema bridges API responses to CRM and workflow cards
- MCP exposes tools to Hermes without custom integration code

**Hermes:**
- Not just prompts — named workflows with inputs, tools, schema, and review rules
- Orchestrates You.com + GTM connectors; enforces source inspection before claims enter the brief
- Review gates block external use until a human approves
- Workflow card = the handoff from "worked once" to "team can run this repeatedly"

**Together:**
- You.com answers "what is true and current?" with cited evidence
- Hermes answers "how does my team use this safely and repeatedly?"

### Sample internal context (Step 9)

Paste this for attendees who don't have their own:

```text
Internal context (sanitized):
- Account segment: Enterprise
- Relationship stage: Active customer, 3-year contract
- Current opportunity: Platform expansion into HR workflows
- Known initiatives: AI agent pilot in IT department
- Known objections: Security review required for AI features
- Existing products used: ITSM, HR Service Delivery
- Approved positioning: "Workflow automation with governance controls"
- Do not use externally: Specific contract values, internal security audit findings
```

### If live APIs fail

The app falls back gracefully:

1. Set `DEMO_MODE=true` in `.env` and restart.
2. Or: show the saved fixtures in `app/fixtures/` directly.
3. Continue with workflow design steps — the design work is valuable without live APIs.

## Manual Setup (without run.sh)

```bash
cd workshop-app
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export DEMO_MODE=true   # or export YDC_API_KEY=your-key
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

## Project Structure

```text
workshop-app/
├── run.sh                  # One-command startup
├── requirements.txt
├── .env.example
├── README.md               # This file
├── HERMES-DESKTOP-SETUP.md # Install skills into Hermes Agent desktop
├── hermes-desktop/         # Installable SKILL.md pack + install.sh
│   ├── install.sh
│   └── skills/
│       ├── account-action-brief/
│       ├── meeting-prep/
│       ├── community-pulse/
│       └── workshop-60min/
├── app/
│   ├── main.py             # FastAPI routes
│   ├── hermes_desktop.py   # Skill pack API + zip export
│   ├── youcom.py           # You.com API client + demo fallback
│   ├── steps.py            # 18 workshop step definitions
│   ├── materials.py        # Templates, scripts, samples
│   ├── platform_highlights.py
│   ├── brief.py            # Brief + workflow card builder
│   └── fixtures/           # Sample API responses for demo mode
├── materials/
│   └── attendee-handout.md # Printable attendee reference
├── FACILITATOR.md          # Minute-by-minute run-of-show
├── preflight.sh            # Pre-workshop verification
└── static/
    ├── index.html          # Workshop UI
    ├── style.css
    └── app.js
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Demo mode status, API key check |
| `/api/steps` | GET | All workshop steps |
| `/api/session` | GET/PATCH | Workshop session state |
| `/api/run/search` | POST | Web Search API |
| `/api/run/contents` | POST | Contents API |
| `/api/run/research` | POST | Research API |
| `/api/run/research-structured` | POST | Structured Research |
| `/api/run/finance-research` | POST | Finance Research (optional) |
| `/api/brief` | GET | Generated account action brief |
| `/api/workflow-card` | GET | Workflow card markdown |
| `/api/hermes-prompt` | GET | Hermes packaging prompt |
| `/api/hermes-desktop` | GET | Desktop skill pack info + install commands |
| `/api/hermes-desktop/download` | GET | Personalized skill pack zip |
| `/api/hermes-desktop/preflight` | GET | Skill pack file validation (503 if incomplete) |

## Related Materials

- `../audience-workflow-building-tutorial.md` — Full 17-step written tutorial (synced with 60-min + post-event)
- `../you-com-api-demo-video-runbook.md` — API demo video script
- `../hermes-workshop-execution-playbook.md` — Facilitator playbook
