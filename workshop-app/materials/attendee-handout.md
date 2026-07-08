# Account Action Brief Workshop — Attendee Handout

**Workflow:** `/account-action-brief`  
**Platforms:** You.com (live intelligence) + Hermes (governed workflow)  
**Live session:** 60 minutes — playground API walk + live Hermes setup + Discord close

---

## The Story

> **You.com provides the evidence. Hermes provides the workflow.**

| You.com does… | Hermes does… |
|---------------|--------------|
| Discovers sources (Search) | Names and packages the workflow |
| Reads page content (Contents) | Orchestrates tools in sequence |
| Synthesizes with citations (Research) | Enforces output schema and review gates |
| Controls domains & freshness | Connects CRM, docs, Slack (read/draft) |
| Exposes tools via MCP | Runs `/account-action-brief` as a governed skill |

---

## API Decision Matrix

| I need… | Use… |
|---------|------|
| Discover candidate sources | **Web Search API** |
| Read full text from known URLs | **Contents API** |
| Multi-source synthesis with citations | **Research API** |
| Public-company financial context | **Finance Research API** |
| Agent tool access without custom code | **You.com MCP Server** |

**In this workshop:** walk these APIs in the **You.com platform playground** at https://you.com/platform

---

## Output Schema (every brief)

1. **Snapshot** — company, industry, confidence
2. **Current Signals** — news, strategy, partnerships
3. **Why This Account Might Care** — priorities, triggers
4. **Suggested Actions** — next step, owner, angle
5. **Claims And Sources** — claim → URL → freshness
6. **Review Notes** — weak claims, assumptions, external-use warnings

---

## Workflow inputs (define in Hermes)

| Input | Required | What it does |
|-------|----------|--------------|
| Company name | Yes | Seeds Search and Research |
| **Brief goal / focus** | Recommended | Tailors API queries — Renewal, Outbound, Competitive, Partner |
| Website | Optional | Boosts official-domain sources |
| output_audience | Optional | `internal` or `external draft` |

**In the 60-min workshop:** define these in the `/account-action-brief` test command in Hermes (slides 11 & 14) — not in the workshop app.

---

## Source Scoring

| Score | Meaning | Action |
|-------|---------|--------|
| 3 | Strong — official, recent, direct | Keep in main brief |
| 2 | Usable — credible but indirect | Keep in main brief |
| 1 | Weak — old, vague, secondhand | Move to Review Notes |
| 0 | Do not use | Remove |

---

## Review Gates (Hermes)

1. **Draft** — no human review yet
2. **Needs edits** — unsupported claims or weak sources
3. **Approved for internal use** — safe for meeting prep
4. **Approved for external use** — safe for outreach/customer comms

---

## Connector Map (Hermes)

| Bucket | What it means | Examples for `/account-action-brief` |
|--------|---------------|--------------------------------------|
| **Read-only** | Fetch data only | You.com Search, Contents, Research; CRM read; internal docs |
| **Draft-only** | Prepare output for a human | Email draft, Slack review, CRM update draft |
| **Blocked** | Must refuse | Auto-send, auto-CRM-update, sensitive data, unapproved legal language |

**Why block auto-send / auto-CRM-update?** Briefs start as **Draft** — humans approve before anything goes out or writes to systems of record.

---

## How Hermes automates the brief

**In the workshop:** you walked the API chain in the **platform playground**, then installed Hermes and wired MCP live.

**After the workshop:** trigger `/account-action-brief` and Hermes runs Search → Contents → Research via MCP, formats six sections, and sets review status to **Draft**.

**Hermes automates:** API chain, synthesis, schema, connector rules.  
**You still do:** trigger, review sources, approve gates, send drafts.

---

## Your Take-Home Artifacts

- [ ] Account action brief (markdown)
- [ ] Workflow card (markdown)
- [ ] **Working `/account-action-brief` skill in Hermes** (built during workshop)
- [ ] Agent build kit + Hermes packaging prompt
- [ ] Connector map (your tools)

---

## Build your agent (live in workshop)

All 6 steps happen in the room:

1. Prerequisites — Hermes + You.com API key
2. Install skill pack (`install.sh`) or create skill in Studio
3. Instruction included in pack (Studio: paste packaging prompt)
4. Wire You.com MCP (`you-search`, `you-contents`, `you-research`)
5. Set connector permissions (read / draft / blocked)
6. Test run — verify six sections + Draft status

Reference: `workshop-app/AGENT-BUILD-GUIDE.md`

---

## After the workshop

1. **Join the You.com Discord** — https://discord.gg/2C4WgryxSD
2. **Introduce yourself** in #introductions — say you joined from the Account Action Brief workshop
3. **Keep using** `/account-action-brief` on your accounts

---

## Resources

- Full tutorial: `audience-workflow-building-tutorial.md`
- Agent build: `workshop-app/AGENT-BUILD-GUIDE.md`
- Community: `workshop-app/COMMUNITY-CONTINUATION.md`
- You.com playground: https://you.com/platform
- You.com docs: https://you.com/docs/welcome
- Workshop app: `workshop-app/` (runnable locally)
