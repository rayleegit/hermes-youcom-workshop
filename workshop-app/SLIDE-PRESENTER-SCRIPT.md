# Slide Presenter Script — 60-Minute Workshop

Detailed say / do / details / copy blocks for each slide in `60-min-workshop-slides.pptx`.

**Rehearse interactively:** `./walk_slides.py`

| Resource | URL |
|----------|-----|
| Playground | https://you.com/platform |
| Workshop app | http://localhost:8080 |
| Discord | https://discord.gg/2C4WgryxSD |
| GitHub repo | https://github.com/rayleegit/hermes-youcom-workshop |

---

## Slide 1 — Title — Account Action Brief Workshop

**Time:** 0:00–0:30

### Say

Welcome to the Account Action Brief workshop. Over the next 60 minutes you'll do three things: walk the You.com APIs live in the platform playground, install Hermes desktop and wire You.com MCP, and run a governed account brief on a real company. This is not a slide-deck lecture — you'll leave with a working /account-action-brief skill in Hermes. One follow-up after today: join the You.com Discord. No 30-day homework, no rollout plan tonight.

### Key details

- Core story: You.com = evidence. Hermes = governed workflow.
- Workflow name: /account-action-brief
- Slides = script + copy-paste blocks. App = govern step + agent build lab reference.
- Repo (if asked): https://github.com/rayleegit/hermes-youcom-workshop

### Do

- Display 1: slides. Display 2: workshop app at http://localhost:8080 (express track, default).
- Confirm your tab is open: https://you.com/platform (API Playground).
- Demo company for the API walk: AMD (https://www.amd.com). Attendees use their own company in Hermes later.

### Facilitator notes

- Do NOT open with a long platform overview — get to hands-on quickly.
- If You.com key issues arise later, attendees can BYOK at you.com/settings/api.

---

## Slide 2 — Two platforms, one workflow

**Time:** 0:30–1:00

### Say

Two platforms, one workflow. You.com is the live intelligence layer — Search discovers sources, Contents reads pages, Research synthesizes with citations. That's real-time web evidence, not stale training data. Hermes is the workflow layer — a named skill called /account-action-brief with stable inputs, a fixed six-section output, connector permissions, and review gates. You.com answers: what is true and current? Hermes answers: how does my team use this safely and repeatedly? Together they replace 'ask AI and hope' with a source-grounded, reviewable process.

### Key details

- You.com: structured JSON, URLs, snippets, freshness, citations.
- Hermes: slash command, SKILL.md, connector map, Draft-first review.
- Not a chatbot demo — a repeatable workflow your team can run before every account meeting.

### Do

- Point to left column (You.com) — evidence chain.
- Point to right column (Hermes) — skill + governance.
- Preview: MCP connects the two; they'll wire it live today.

### Facilitator notes

- If someone asks 'why not just ChatGPT?': citations, freshness, and governance.

---

## Slide 3 — Agenda (60 min)

**Time:** 1:00–3:00

### Say

Here's the arc for the hour. Minutes 0 to 3: welcome and story. 3 to 18: we walk You.com APIs together in the platform playground — Search, Contents, Research — using AMD as the demo company. 18 to 23: govern — connectors and review gates in the workshop app. 23 to 26: optional workflow card download. 26 to 52: the main event — Hermes install, define your inputs in the test command, wire MCP, and run your first brief. 52 to 57: close with Discord only. Last few minutes: buffer for MCP debugging or Q&A.

### Key details

- Playground: https://you.com/platform
- App: http://localhost:8080
- If running long, cut: workflow card (3 min), Finance demo (3–5 min).
- Never cut: playground walk, Hermes install + MCP + one test brief, Discord.

### Do

- Walk each agenda line — set expectation that playground AND Hermes are live.
- Call out: inputs are defined in Hermes, not the workshop app.
- Call out: we install the skill pack (not build from scratch) to save time for MCP + test.

### Facilitator notes

- Keep this under 2 minutes — attendees want to get hands-on.

---

## Slide 4 — You.com APIs — which one when?

**Time:** 3:00–3:30

### Say

Each You.com API has exactly one job — don't mix them. Search discovers candidate sources: structured JSON with titles, URLs, snippets, and freshness metadata. Contents reads full page text from URLs you already selected — clean markdown for claim verification. Research does multi-source synthesis with citations — output.content plus output.sources. Finance Research is optional — earnings, filings, market signals for public companies like AMD. MCP is how Hermes calls Search, Contents, and Research as tools without writing custom integration code. One API, one job — Hermes orchestrates the chain.

### Key details

- Search → discover | Contents → read | Research → synthesize | Finance → optional
- MCP → you-search · you-contents · you-research
- Endpoints: GET ydc-index.io/v1/search · POST ydc-index.io/v1/contents · POST api.you.com/v1/research
- Full query/parameter examples: PLAYGROUND-API-WALKTHROUGH.md

### Do

- Flash this slide — 60 seconds max.
- Open https://you.com/platform → API Playground in browser.

### Facilitator notes

- Do not use workshop app Full Demo Chain as primary demo — playground is the hero.
- Keep this slide under 60 seconds — examples on slides 5–7 and live block 11.

---

## Slide 5 — Web Search API

**Time:** 3:30–6:00

### Say

Search discovers current web and news sources. Structured JSON — titles, URLs, snippets, page_age — not a prose answer. Parameters: query, count, freshness, include_domains, boost_domains, exclude_domains. We'll run AMD broad first, then optionally include_domains=amd.com to show source governance.

### Key details

- GET https://ydc-index.io/v1/search
- Params: query, count (5), freshness (year|month), include_domains, boost_domains, exclude_domains
- Goal-specific queries (PLAYGROUND-API-WALKTHROUGH.md):
-   Renewal: AMD enterprise renewal data center GPU Instinct expansion 2025
-   Outbound: AMD Instinct MI350 enterprise AI data center customer wins
-   Competitive: AMD vs NVIDIA data center AI GPU Instinct MI350
-   Partner: AMD cloud hyperscaler partnership Instinct EPYC ecosystem
- Response: results.web, results.news, title, url, description/snippets, page_age

### Copy / show on screen

```
Search (live):
query: AMD data center Instinct MI350 earnings partnerships
count: 5
freshness: year

Governance demo:
include_domains: amd.com
```

### Do

- Playground → Search endpoint.
- Run: AMD data center Instinct MI350 earnings partnerships · count=5 · freshness=year
- Point at results.web[] and results.news[] — title, url, snippet, page_age.
- Optional 2nd run: add include_domains=amd.com — compare broader vs allowlist.
- Pick 1–2 URLs for Contents.

### Facilitator notes

- include_domains = strict allowlist. boost_domains = prefer without excluding others.

---

## Slide 6 — Contents API

**Time:** 6:00–9:00

### Say

Contents takes URLs — not a query. Paste URLs from Search. Parameters: urls array, formats markdown and metadata, crawl_timeout 15, max_age 86400 for cache control. Returns page-level markdown for claim verification.

### Key details

- POST https://ydc-index.io/v1/contents
- Example URL: amd.com/en/newsroom/press-releases/...-instinct-mi350...
- Takes URLs not queries — always run Search first
- Response fields: markdown, metadata, url per page

### Copy / show on screen

```
{
  "urls": ["<paste URL from Search>"],
  "formats": ["markdown", "metadata"],
  "crawl_timeout": 15,
  "max_age": 86400
}
```

### Do

- Copy 1–2 URLs from Search (prefer amd.com press release or tier-1 news).
- Playground → Contents → paste URLs.
- Set formats=[markdown, metadata], crawl_timeout=15, max_age=86400.
- Show markdown — headings, quotes, dates.

### Facilitator notes

- If Contents fails, pick another URL — don't debug long on stage.

---

## Slide 7 — Research API

**Time:** 9:00–12:00

### Say

Research POST to api.you.com/v1/research. Parameters: input (question with company + goal), research_effort standard for demo, source_control with freshness and boost_domains amd.com. Response: output.content and output.sources. Use goal-shaped inputs — renewal, outbound, competitive, or partner.

### Key details

- POST https://api.you.com/v1/research
- research_effort: lite | standard | deep | exhaustive
- Renewal input: AMD signals for enterprise renewal — roadmap, GPU adoption, risks?
- Outbound input: AMD signals for outbound — MI350 wins, buying triggers?
- Competitive input: AMD vs NVIDIA positioning — MI350, ecosystem?
- Partner input: AMD partnership/ecosystem for co-sell?
- source_control: freshness, boost_domains, include_domains

### Copy / show on screen

```
{
  "input": "What are the most important recent strategic signals for AMD that matter for an enterprise renewal conversation? What should an account team prepare before the call?",
  "research_effort": "standard",
  "source_control": {
    "freshness": "year",
    "boost_domains": ["amd.com"]
  }
}
```

### Do

- Playground → Research.
- Use Renewal or Outbound input from copy block.
- research_effort: standard · boost_domains: [amd.com]
- Show output.content then output.sources — trace one claim to URL.
- Narrate 30–90s wait.

### Facilitator notes

- Research input shape = what attendees encode as goal in Hermes.

---

## Slide 8 — MCP — how Hermes calls You.com

**Time:** 12:00–13:00

### Say

Bridge from playground to Hermes. MCP — Model Context Protocol — is an open standard for AI agents to call tools. Think of it as USB-C for agent integrations: one protocol, many tools. In the playground you called APIs manually with forms or curl. With MCP, Hermes calls the same capabilities as named tools: you-search, you-contents, you-research. The You.com MCP server URL is https://api.you.com/mcp. Your API key authenticates. These tools are read-only web intelligence — they never write to CRM, email, or Slack.

### Key details

- MCP = Model Context Protocol (agent tool standard).
- You.com MCP URL: https://api.you.com/mcp
- Core tools: you-search · you-contents · you-research
- Optional: finance tool for public companies.
- Read-only — no writes, no sends.
- API key: you.com/settings/api (BYOK) or org-provided key in Hermes.

### Copy / show on screen

```
MCP server URL:
https://api.you.com/mcp

Tools to enable:
• you-search
• you-contents
• you-research
```

### Do

- Stay on slides — conceptual, 2–3 minutes.
- Left column: what MCP is. Right column: You.com MCP server + tool names.
- Emphasize: same evidence chain as playground, different interface.

### Facilitator notes

- Someone will ask 'why MCP vs direct API?' — less custom wiring in Hermes; tools show up in agent UI.

---

## Slide 9 — How You.com MCP works in /account-action-brief

**Time:** 13:00–14:00

### Say

Walk the production flow step by step. One: you run /account-action-brief with company and brief goal in the command. Two: the Hermes skill decides which tools to call and in what order. Three: Hermes calls MCP you-search to discover sources aligned to your goal. Four: you-contents reads selected URLs. Five: you-research synthesizes with citations. Six: the skill formats the six-section brief and sets review status to Draft. You manually did steps three through five in the playground — MCP automates them inside Hermes. We'll wire https://api.you.com/mcp live in about fifteen minutes.

### Key details

- 1. Trigger: /account-action-brief + inputs
- 2. Skill orchestrates tool order (SKILL.md procedure)
- 3. you-search → discover
- 4. you-contents → read pages
- 5. you-research → synthesize + cite
- 6. Six-section output + Draft status
- Tool calls should be visible in Hermes during the test run.

### Do

- Trace each numbered bullet on the slide with your pointer.
- Repeat: Draft is default — human review before internal or external use.

### Facilitator notes

- If MCP fails in room: paste playground evidence into Hermes as fallback — say production uses MCP.

---

## Slide 10 — Finance Research API (optional)

**Time:** 14:00 (optional)

### Say

Finance Research is optional — a finance-optimized index for earnings, filings, and market signals. Excellent for AMD and other public companies. It's often slow — two to five minutes — so in the 60-minute track we usually skip the live demo. If you enable it via MCP, use research_effort deep or exhaustive only — standard is not valid and will error.

### Key details

- POST https://api.you.com/v1/finance_research
- research_effort: deep | exhaustive ONLY (standard → 422 error)
- Example input: What financial signals matter for AMD data center GPU growth and enterprise accounts?
- Often 2–5 min latency — skip live in 60-min unless buffer.
- Enable via MCP finance tool only if brief needs earnings/filings context.

### Copy / show on screen

```
{
  "input": "What financial and market signals should an account team know before meeting with AMD — data center revenue, Instinct adoption, analyst outlook?",
  "research_effort": "deep"
}
```

### Do

- Skip this slide unless you have 3–5 minutes buffer.
- If demoing: playground Finance endpoint, AMD, expect wait.

### Facilitator notes

- AMD is a strong Finance example — mention even if you skip live demo.

---

## Slide 11 — Platform playground walkthrough (LIVE)

**Time:** 3:00–18:00 (LIVE block)

### Say

Full chain live. Search AMD broad, then optionally Search with include_domains amd.com. Contents on one URL. Research with a goal-shaped input — renewal or outbound. View Code optional. Full query/parameter cheat sheet: PLAYGROUND-API-WALKTHROUGH.md.

### Key details

- Minute budget: ~15 min for this block (part of 3–18 min segment).
- Search params to set in playground UI: query, count, freshness, include_domains
- Contents params: urls, formats, crawl_timeout, max_age
- Research params: input, research_effort, source_control.boost_domains
- Goal-specific query table → PLAYGROUND-API-WALKTHROUGH.md §1–3
- API output → brief mapping: Search→Signals, Contents→verify, Research→content+sources

### Copy / show on screen

```
Quick chain:
1. Search: AMD data center Instinct MI350 earnings
2. Contents: <URL from step 1>
3. Research input: What AMD signals matter for [renewal/outbound]?
   research_effort: standard
   boost_domains: [amd.com]
```

### Do

- LIVE — facilitator drives browser.
- 1. Search — AMD data center Instinct MI350 earnings · count=5 · freshness=year
- 2. Search (optional) — same + include_domains=amd.com — governance compare
- 3. Contents — 1 URL from Search · formats markdown+metadata
- 4. Research — Renewal or Outbound input · research_effort=standard · boost_domains amd.com
- 5. Point at output.content + output.sources
- 6. View Code — 30 sec curl flash
- 7. Bridge slides 8–9: MCP tools mirror these three steps

### Facilitator notes

- Don't rush JSON inspection — citations in Research matter more than finishing every param.
- If API fails: narrate from slides; use app demo mode for govern only.

---

## Slide 12 — Hermes — skills & connectors

**Time:** 18:00

### Say

Before we touch Hermes desktop: skills versus connectors. A Hermes skill is a named, reusable workflow — today /account-action-brief. SKILL.md holds required inputs, the procedure, the six-section output schema, and governance rules. You trigger it with a slash command plus company and brief goal. Connectors are permissions — how the skill may touch each system. Read-only: You.com MCP, CRM read, internal docs. Draft-only: email draft, Slack review, CRM update draft — human sends. Blocked: auto-send, auto-CRM-update, sensitive data. Skills define WHAT the agent does every run. Connectors define WHAT's ALLOWED. You.com via MCP is always read-only.

### Key details

- Skill pack installs: /account-action-brief, /workshop-60min, /community-pulse, /meeting-prep
- Install path: ~/.hermes/skills/ via install.sh
- Read-only: fetch data only (You.com, CRM read, docs)
- Draft-only: prepare for human (email, Slack, CRM draft)
- Blocked: auto-send, auto-CRM-update, PII, unapproved legal language

### Do

- Show slide while switching to workshop app for govern (next).
- Say: after install.sh we'll open SKILL.md for one minute — the pack is not a black box.

### Facilitator notes

- Studio users without install.sh: create skill manually + paste prompt from Agent Build Lab.

---

## Slide 13 — Govern — review gates (app)

**Time:** 18:00–23:00

### Say

Governance sits on three layers: skills, connectors, and review gates. Every brief starts as Draft — no human review yet. Needs edits means weak sources or unsupported claims. Approved for internal use means safe for meeting prep and planning inside your team. Approved for external use means claims, wording, and sources were verified for customer outreach — a higher bar. We block auto-send and auto-CRM-update in the pilot: Hermes may draft, humans approve and send. Internal use is not external use — don't put customer-facing language in email until external approval.

### Key details

- Draft — default every run; no human review yet.
- Needs edits — unsupported claims, weak sources, tone issues.
- Approved for internal use — meeting prep, internal planning.
- Approved for external use — outreach, customer comms (verify claims + wording).
- Why block auto-send/CRM write? Briefs are intelligence + drafts — systems of record need human approval.
- You.com APIs are always read-only; governance applies to GTM connectors (email, CRM, Slack).

### Do

- Workshop app → Govern step (http://localhost:8080, express track step 4).
- Walk connector defaults on screen (read / draft / blocked).
- Walk four review states — set status to Draft.
- Optional 23–26 min: Workflow card → Generate → Download (cut if long).

### Facilitator notes

- Spend ~5 min here — don't turn it into a compliance lecture.
- Workflow card cut saves 3 min if behind schedule.

---

## Slide 14 — Define inputs in Hermes (live)

**Time:** 26:00

### Say

Inputs are defined in Hermes when you run the skill — not in the workshop app. Required: company name — AMD for demo or your own account. Optional: website — https://www.amd.com boosts official-domain sources. Brief goal is strongly recommended — it tailors Search and Research queries. Pick a preset and customize: Renewal, Outbound, Competitive, or Partner. Optional output_audience: internal or external draft. Every brief follows six sections in order: Snapshot, Current Signals, Why This Account Might Care, Suggested Actions, Claims And Sources, Review Notes.

### Key details

- Required input: company_name
- Optional: company_url, workflow_goal, internal_context, output_audience
- Six sections:
-   1. Snapshot — company, industry, confidence
-   2. Current Signals — news, strategy, partnerships
-   3. Why This Account Might Care — priorities, triggers
-   4. Suggested Actions — next step, owner, angle
-   5. Claims And Sources — claim → URL → freshness
-   6. Review Notes — weak claims, assumptions, external warnings
- Goal presets:
-   • Renewal — renewal prep, risks, expansion
-   • Outbound — first meeting, sequence research
-   • Competitive — displacement, positioning
-   • Partner — co-sell, ecosystem

### Do

- Ask the room: 'What's your brief goal for today?'
- Preview slides 15–17 — install, MCP, test command.
- Point at six-section list on slide.

### Facilitator notes

- Vague goals produce vague briefs — push attendees to write one concrete sentence.

---

## Slide 15 — Hermes desktop — install skill pack (LIVE)

**Time:** 26:00–34:00

### Say

Everyone installs the skill pack now. We use install.sh so we can focus on MCP and your first brief — not paste a prompt from scratch. The script copies four skills to ~/.hermes/skills/: account-action-brief, workshop-60min, community-pulse, and meeting-prep. Restart Hermes if /account-action-brief doesn't appear. After install, optionally open SKILL.md for one minute — you'll see the same inputs, procedure, and governance we discussed. This is packaged workflow, not magic.

### Key details

- Skills install to: ~/.hermes/skills/
- Pack includes: /account-action-brief (main), /workshop-60min, /community-pulse, /meeting-prep
- Alternative: Download Skill Pack (.zip) from app Agent Build Lab.
- Prereqs: Hermes desktop open, logged in, You.com API key ready for MCP step.

### Copy / show on screen

```
cd workshop-app/hermes-desktop
chmod +x install.sh
./install.sh
# Restart Hermes if needed
```

### Do

- LIVE — everyone runs install command (project on screen).
- Circulate: chmod +x, correct path, restart Hermes.
- Confirm: /account-action-brief visible in skill list.
- Optional: show ~/.hermes/skills/account-action-brief/SKILL.md

### Facilitator notes

- Pair anyone without Hermes access — they can follow along and install later.
- Most common issue: forgot to restart Hermes after install.

---

## Slide 16 — Wire You.com MCP (LIVE)

**Time:** 34:00–41:00

### Say

Wire MCP now — this is where most room failures happen, so raise your hand if you're stuck. Add MCP server https://api.you.com/mcp in Hermes settings. Enable three tools: you-search, you-contents, you-research. Attach only these to /account-action-brief — least privilege. Do not attach email, Slack send, or CRM write tools to this skill in the pilot. Authenticate with your You.com API key. Optional: finance tool for public companies. Test with a single Search tool call if your build supports it.

### Key details

- Server: https://api.you.com/mcp
- Required tools: you-search, you-contents, you-research
- Optional: finance research MCP tool
- API key: https://you.com/settings/api
- Attach tools to /account-action-brief only — not global admin if avoidable.
- Read-only — MCP never sends email or writes CRM.

### Copy / show on screen

```
You.com MCP Server:
https://api.you.com/mcp

Enable on /account-action-brief:
• you-search
• you-contents
• you-research

(Optional) finance for public companies
```

### Do

- LIVE — display MCP config from slide; attendees copy server URL + tool names.
- Circulate actively — this step needs facilitators walking the room.
- Verify: tool call visible (Search for AMD or workshop company).

### Facilitator notes

- Budget 5–7 minutes of circulation time here.
- Fallback: paste playground Research output into Hermes if MCP won't connect.

---

## Slide 17 — Define inputs + test /account-action-brief (LIVE)

**Time:** 41:00–52:00

### Say

Define inputs in the command, then run. Give yourself two minutes to write your brief goal — Renewal, Outbound, Competitive, or Partner — customize the goal line. Use AMD or your own company. Watch Hermes while it runs: you should see tool calls for Search, Contents, Research. Narrate: 'Hermes is calling Search… now Contents on selected URLs… now Research for synthesis.' Confirm output: all six sections, real URLs in Claims And Sources — not invented links — and review status Draft. No auto-send, no CRM write.

### Key details

- Verification checklist:
-   ☐ Skill runs without errors
-   ☐ You.com tool calls visible
-   ☐ All six sections present in order
-   ☐ Claims & Sources has real URLs
-   ☐ Review status = Draft
-   ☐ No auto-send or CRM write
- Do not mark Approved for external use in the room — Draft is correct for first run.

### Copy / show on screen

```
/account-action-brief

company: AMD
website: https://www.amd.com
goal: Prepare for an upcoming customer meeting — understand recent strategic signals and decide what actions the account team should consider.
output_audience: internal
```

### Do

- LIVE — 2 min silent: attendees write their goal.
- Display test command on slide; everyone runs in Hermes.
- Narrate tool calls during the run.
- After run: spot-check one attendee screen for six sections + URLs + Draft.

### Facilitator notes

- Example goals to suggest if attendees are stuck:
-   Renewal: 'Prepare for renewal — recent signals, risks, expansion angles'
-   Outbound: 'Research for outbound — first meeting talking points'
-   Competitive: 'Competitive positioning vs [incumbent] for data center AI'

---

## Slide 18 — Minimum success before you leave

**Time:** 52:00

### Say

Quick checkpoint before we close. You should leave with: skill /account-action-brief installed, You.com MCP connected with tool calls you saw during the run, a completed test with all six sections, real URLs in Claims And Sources, review status Draft, and no auto-send or CRM write. If any of that failed, catch me now — we'll debug in the buffer minutes.

### Key details

- Minimum bar = working skill + MCP + one Draft brief with sources.
- Not required tonight: external approval, workflow card, Finance tool, meeting-prep skill.
- Success = you can run /account-action-brief again tomorrow on your own accounts.

### Do

- Show of hands or quick room scan.
- Help stragglers during buffer (57–60 min).

### Facilitator notes

- Celebrate visible tool calls — that's the 'aha' that connects playground to Hermes.

---

## Slide 19 — Close — join You.com Discord

**Time:** 52:00–57:00

### Say

One required follow-up: join the You.com Discord. Link on screen: discord.gg/2C4WgryxSD. Post in introductions — say you joined from the Account Action Brief workshop. Use the intro template on the slide or copy from the app Community panel. Include your role and what you're building with /account-action-brief. No 30-day plan, no rollout homework — the community is where you keep going.

### Key details

- Discord: https://discord.gg/2C4WgryxSD
- Channel: #introductions (or welcome channel)
- Only required post-workshop action.

### Copy / show on screen

```
https://discord.gg/2C4WgryxSD

Post in #introductions:

Hi! I joined from the Account Action Brief workshop (Hermes + You.com).

- Name / role:
- What I'm building: /account-action-brief workflow
- First company I'll brief:
- One thing I want to learn in this community:
```

### Do

- Display Discord link and intro template.
- App wrap-up step → Community panel → Copy intro button.

### Facilitator notes

- Do not assign 3-brief challenge or pilot template — Discord intro only.

---

## Slide 20 — Close script (read aloud)

**Time:** 57:00

### Say

You walked the You.com APIs in the playground — Search, Contents, Research — and saw structured evidence with citations. You installed Hermes, wired MCP, defined your inputs, and ran a governed account brief that starts as Draft. You.com answered what is true and current. Hermes answered how your team uses it safely and repeatedly. Join the You.com Discord — link on screen — introduce yourself and say you came from this workshop. Keep using /account-action-brief on your accounts. See you in the server.

### Key details

- Dual value recap: You.com = evidence, Hermes = workflow.
- No homework beyond Discord.

### Do

- Read aloud — warm close, not rushed.
- Pause for applause / questions if buffer remains.

### Facilitator notes

- If Q&A: common topics are MCP debugging, API key billing, Hermes Studio vs desktop.

---

## Slide 21 — Resources

**Time:** — (Q&A / leave up)

### Say

Resources are on the slide and in the GitHub repo. Platform playground for API experiments. Workshop app for govern reference and agent build lab. Facilitator docs: FACILITATOR-60MIN.md, HERMES-DESKTOP-SETUP.md, SLIDE-PRESENTER-SCRIPT.md. Community: COMMUNITY-CONTINUATION.md — Discord only. Preflight before your next session: ./preflight.sh in workshop-app.

### Key details

- Playground: https://you.com/platform
- App: http://localhost:8080 (?full=1 for 18-step self-paced track)
- Docs: https://you.com/docs/welcome
- Repo: https://github.com/rayleegit/hermes-youcom-workshop
- Presenter script: ./walk_slides.py

### Do

- Leave slide up during Q&A.
- Share repo if asked: https://github.com/rayleegit/hermes-youcom-workshop

### Facilitator notes

- Thank co-hosts / You.com / Hermes if applicable.

---
