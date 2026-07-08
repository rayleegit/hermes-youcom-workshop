# Facilitator Run-of-Show

**Duration:** 75–90 minutes  
**App:** `cd workshop-app && ./run.sh` → http://localhost:8080  
**Default company:** AMD (change live in Step 2)

---

## 30 Minutes Before

```bash
cd workshop-app
./preflight.sh          # Must pass all checks
./run.sh                # Or already running
```

- [ ] Projector / screen share tested
- [ ] Toggle **Presenter Mode** (top-right) if audience should not see facilitator notes
- [ ] Decide: **demo mode** (no key) or **live** (`YDC_API_KEY` in `.env`)
- [ ] If live: run **Run Full Demo Chain** once privately to confirm APIs work
- [ ] Confirm attendees have **Hermes access** for Step 14 hands-on agent build
- [ ] Share `AGENT-BUILD-GUIDE.md` as optional pre-read

---

## Opening (read aloud — Step 0)

> Welcome to the Account Action Brief Workshop.
>
> Today we're building one workflow — `/account-action-brief` — that shows how two platforms work together:
>
> **You.com** provides live, source-grounded web intelligence.  
> **Hermes** turns that intelligence into a governed, reusable workflow your team can pilot.
>
> This is NOT a chatbot demo. You'll see each You.com API call do one job: Search discovers, Contents reads, Research synthesizes. Then Hermes packages the result with review rules and a reusable workflow card.

---

## Minute-by-Minute (18 steps)

| Min | Step | Title | Do this |
|-----|------|-------|---------|
| 0–5 | 0 | Welcome | Show Platform Spotlight. Explain dual story. |
| 5–8 | 1 | Choose The Job | Audience writes job sentence. |
| 8–11 | 2 | Define Inputs | Enter company (try a real account). Click **Save Inputs**. |
| 11–14 | 3 | Output Schema | Walk through six sections. "Hermes enforces this every run." |
| 14–18 | 4 | API Decision Matrix | Teach: each API = one job. Mention MCP. |
| 18–28 | 5 | Web Search | **Run Web Search** live. Point at titles, URLs, snippets, page_age. Try domain-filtered search. |
| 28–34 | 6 | Source Scoring | Audience scores 3 sources. Explain 3/2/1/0 rubric. |
| 34–40 | 7 | Contents | **Run Contents**. Show markdown. "Page-level claim verification." |
| 40–48 | 8 | Research | **Run Research**. Show output.content + output.sources. Optional: Finance Research. |
| 48–52 | 9 | Structured Research | **Run Structured Research**. Map fields to Suggested Actions. |
| 52–58 | 10 | Team Context | Click **Load Sample Context**. Explain public vs private separation. |
| 58–63 | 11 | Connector Map | Fill read/draft/blocked tools. Show sample Slack + CRM drafts. |
| 63–67 | 12 | Review Gates | Walk four states. Set status to Draft. Run review checklist on brief. |
| 67–72 | 13 | Workflow Card | **Generate Workflow Card** → Download. |
| 72–92 | 14 | Build Your Agent End-to-End | Agent Build Lab: attendees create skill, wire MCP, test run (~20 min). |
| 77–80 | 15 | Test Three Accounts | Fill scorecard. Plan 3 test accounts. |
| 80–85 | 16 | Team Rollout (champions) | Optional — show template 60 sec. Say: fill after Week 1, not tonight. |
| 85–90 | 17 | Wrap-Up | **Download All**. Community + 3 briefs. Champions: rollout template optional. |

---

## Teaching Cheat Sheet

### You.com — say this
- "Search discovers, Contents reads, Research synthesizes — each API has one job."
- "Snippets are already LLM-ready context."
- "Domain and freshness controls are governance levers, not search tweaks."
- "Structured output_schema maps directly into CRM and workflow cards."
- "MCP lets Hermes call web tools without custom integration code."

### Hermes — say this
- "Hermes is not a place to run prompts — it's where useful AI tasks become governed workflows."
- "Named workflows, stable inputs, stable output schema — that's what makes reuse possible."
- "Review gates block external use until a human approves."
- "The workflow card is the handoff from 'worked once' to 'our team can run this.'"
- "Run → Integrate → Govern → Package → Pilot."

---

## If Something Breaks

| Problem | Fix |
|---------|-----|
| API call fails | Click **Run Full Demo Chain** won't help if live fails — switch to demo mode: `DEMO_MODE=true ./run.sh` |
| Research is slow | Say: "research_effort controls depth — we're on standard. In production you'd choose lite vs deep." Cut to demo mode if >60s. |
| Attendees lost | Return to Platform Spotlight. Restate: "You.com = evidence, Hermes = workflow." |
| No Hermes access | Steps 13–14 still work — they copy the prompt and card for later. |
| Running short on time | Skip Steps 9 (structured research) and 15 (scorecard). Never skip 5 (Search), 12 (review), 13 (card). |
| Running long | Use **Run Full Demo Chain** at Step 5 to pre-populate, then walk results instead of waiting live. |

---

## Closing (read aloud — Step 17)

> You.com answered: what is true and current? — with cited, structured evidence.  
> Hermes answered: how does my team use this safely and repeatedly? — with governance and packaging.
>
> Your next step: join the community, finish your agent, run 3 briefs this week. Champions: optional rollout template in Download All.
>
> Download your artifacts before you leave.

---

## After the Workshop

- Send attendees link to `audience-workflow-building-tutorial.md`
- Follow up with high-intent attendees on API/MCP access; offer rollout template only to champions asking about team adoption
- Capture feedback: Was the dual-platform story clear? Which step was most valuable?
