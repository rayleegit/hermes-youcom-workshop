# Tutorial: Build Your First Reusable Hermes Workflow With You.com

Google Doc:
https://docs.google.com/document/d/1t_KiDWtM7v6A1LDEr2joZqkHwiKqtMW7GXDGE6WFDSk/edit?usp=drivesdk

**Workshop package (live + self-paced):**

- **60-minute live track:** `workshop-app/` → `./run.sh` → http://localhost:8080 (8 app steps)
- **90-minute deep dive:** http://localhost:8080?full=1 (all 18 app steps)
- **Facilitator script:** `workshop-app/FACILITATOR-60MIN.md`
- **After the event:** `workshop-app/POST-EVENT-LEARNING.md`
- **This tutorial:** full written depth — use in the room only if you have extra time; otherwise assign as homework

**Core story:** You.com = live evidence. Hermes = governed workflow. The app shows APIs manually; `/account-action-brief` automates the same chain.

## What You Will Build

In this tutorial, you will create a reusable workflow called `/account-action-brief`.

The workflow takes one account, company, customer, prospect, or partner name and produces a source-backed action brief that a team can review, reuse, and pilot.

By the end, you should have:

1. A working workflow prompt.
2. A source inspection habit.
3. A structured output format.
4. A connector map for the tools your team already uses.
5. Admin and review rules.
6. A reusable Hermes skill or playbook (install the 4-skill desktop pack or author in Studio).
7. A community habit (You.com Discord + Week 1: 3 briefs).
8. Optional: a two-week pilot plan (champions only — team rollout).
9. Optional Week 2+: `/meeting-prep` for calendar-triggered briefs before meetings.

This tutorial uses You.com for live web intelligence and Hermes as the workflow layer that turns a useful prompt into a repeatable, governed process.

The workshop should make the You.com APIs visible. The audience should see that the workflow is not just "an AI answer." It is a chain of API-backed retrieval, extraction, synthesis, and review.

## Who This Is For

This is designed for:

- GTM, sales, customer success, partnerships, and marketing teams.
- Operators who repeatedly prepare account, customer, partner, or market briefs.
- Product, solutions, and AI teams building internal workflows.
- Admins who need to make AI workflows reusable without making them uncontrolled.

You do not need to be a software engineer. If your team has developer support, there is an optional technical implementation path near the end.

## Recommended Workshop Format

### 60-minute live session (default)

Use the workshop app at http://localhost:8080. See `workshop-app/FACILITATOR-60MIN.md`.

| Min | App step | Tutorial steps (depth = after) |
|-----|----------|--------------------------------|
| 0–3 | Welcome | Framing (this doc, Steps 1–3) |
| 3–7 | Define | Step 1–2 |
| 7–10 | API Map | API Spotlight + API Choice Matrix |
| 10–29 | Full Demo Chain | Steps 4–8 (manual APIs — Hermes automates same chain) |
| 29–34 | Govern | Steps 10–11 |
| 34–37 | Workflow Card | Step 12 |
| 37–50 | Agent Build | Step 13 + Hermes Desktop Skill Pack (install steps 1–4 live) |
| 50–55 | Wrap-up | Community Continuation — Discord + Week 1 challenge |

**Say at Full Demo Chain:** "We run APIs manually here so you see each step. In Hermes, `/account-action-brief` runs this chain automatically — you review the Draft."

**Say at close:** "Join the You.com Discord, introduce yourself from this workshop, run three briefs. Week 2+: try `/meeting-prep` for calendar-triggered briefs."

### 90-minute deep dive (optional)

Open http://localhost:8080?full=1 and walk more tutorial steps in the room (connector depth, quality scorecard, optional Finance Research).

### Self-paced after the event

Use this full tutorial (17 steps) plus `workshop-app/POST-EVENT-LEARNING.md`. Champions who want team rollout: Step 16 + rollout template in Download All.

Suggested timing for a **full 75–90 minute self-paced session**:

- 0–10 min: Pick the workflow and define the job (Steps 1–2).
- 10–25 min: Gather live sources with You.com (Steps 4–5).
- 25–40 min: Draft the first brief (Steps 6–8).
- 40–55 min: Add tool and team context (Steps 9–10).
- 55–70 min: Add governance and review rules (Step 11).
- 70–85 min: Package the workflow and install skill pack (Steps 12–13).
- 85–90 min: Join Discord, run first test brief, decide next action (Steps 14, 17, Community).

## Before You Start

Pick one workflow your team already runs manually.

Good candidates:

- Account brief before a customer meeting.
- Prospect brief before outbound.
- Partner brief before a co-selling discussion.
- Renewal risk brief before a QBR.
- Competitive update before a deal review.
- Executive briefing before a strategic meeting.

Avoid starting with workflows that:

- Require private or sensitive data you cannot safely use in the workshop.
- Need automatic writeback before anyone has reviewed the result.
- Depend on undocumented business rules.
- Have no clear owner.

For this tutorial, the default example is:

```text
Workflow: /account-action-brief
Input: Company name
Output: Source-backed account brief plus suggested next actions
Primary user: Account owner, CSM, partnerships lead, or marketer
Reviewer: Manager, deal owner, or workflow owner
Pilot length: 2 weeks
```

## Materials

You will need:

- Access to Hermes (desktop app with skill pack, or Workflow Studio).
- Access to You.com tools through Hermes MCP, API, or your workshop facilitator.
- **Workshop app** (facilitator): `cd workshop-app && ./run.sh` → http://localhost:8080.
- **Hermes desktop skill pack** (attendees): `workshop-app/hermes-desktop/` — 4 installable skills; see `HERMES-DESKTOP-SETUP.md`.
- One public company, prospect, customer, or partner to research.
- Optional: read-only sample context from CRM, notes, docs, support tickets, or call summaries.
- A place to save the final workflow card.
- Optional for the API demo: terminal, Postman, or a notebook with a `YDC_API_KEY`.
- **You.com Discord** (post-workshop): https://discord.gg/2C4WgryxSD — see `COMMUNITY-CONTINUATION.md`.

If you do not have live access during the workshop, use placeholder sources and still complete the workflow design. The design work is useful even before connectors are fully wired.

## You.com API Spotlight

Use this section as the API explainer before the hands-on build.

You.com gives the workflow four useful API modes:

```text
Web Search API:
Find current web and news results as structured JSON.
Best when you need candidate sources, snippets, freshness signals, and URLs.

Contents API:
Fetch clean Markdown, HTML, or metadata from URLs you already trust.
Best when snippets are not enough and Hermes needs the full source text.

Research API:
Ask a complex question and get a synthesized, citation-backed answer.
Best when the workflow needs multi-source reasoning, not just retrieval.

Finance Research API:
Ask financial questions against a finance-optimized index.
Best for public-company account briefs, earnings, filings, market context, and investor-facing signals.
```

The core workshop can use Search, Contents, and Research. Finance Research is an optional add-on for public-company examples.

## API Choice Matrix

Use this decision rule:

```text
I need to discover sources.
-> Use Web Search API.

I already have URLs and need clean page text.
-> Use Contents API.

I need a short, cited synthesis across multiple sources.
-> Use Research API.

I need public-company financial context, earnings, filings, or market data synthesis.
-> Use Finance Research API.

I want Hermes or another agent to call web tools without writing integration code.
-> Use the You.com MCP server.
```

For the `/account-action-brief` workflow, the recommended flow is:

```text
1. Web Search API finds candidate sources.
2. Contents API reads the best URLs.
3. Research API synthesizes the strategic implications.
4. Optional Finance Research API adds public-company financial context.
5. Hermes packages the final workflow and applies review rules.
```

## API Demo Setup

Use this setup when showing the APIs in a demo video or live workshop.

```bash
export YDC_API_KEY="your-key"
```

Use one example account throughout the recording:

```text
Company: AMD
Workflow: /account-action-brief
Question: What are the most important recent strategic signals for AMD, and what actions should an account team consider?
```

Show the API response shape, not just the final answer. The point is for the audience to see why the workflow is source-grounded.

## The Workflow Pattern

Every reusable workflow needs the same basic shape:

```text
Trigger -> Inputs -> Tools -> Draft -> Review -> Reuse -> Pilot
```

For `/account-action-brief`, that becomes:

```text
User asks for an account brief
-> Hermes collects required inputs
-> You.com gathers current web sources
-> Hermes drafts a structured brief
-> User inspects sources and edits weak claims
-> Hermes packages the prompt as a reusable workflow
-> Team pilots the workflow for two weeks (champions only — see Step 16)
```

## Manual App Demo Vs Hermes Automation

The workshop app and this tutorial teach the **same evidence chain** in two modes:

| Mode | Where | What attendees see |
|------|-------|-------------------|
| **Manual** | Workshop app Full Demo Chain | Each You.com API call — Search → Contents → Research — run step by step |
| **Automated** | Hermes `/account-action-brief` | Same chain via MCP; output starts as **Draft**; human reviews sources |

```text
Manual (app):     User clicks → Search → Contents → Research → brief
Automated (Hermes): User runs /account-action-brief → MCP chain → Draft brief → review
```

**Why both matter:** Manual demo builds trust in the evidence. Automation makes the workflow repeatable. Governance (connector map + review gates) applies in both modes — every output starts as Draft until a human approves external use.

Install path: `workshop-app/hermes-desktop/install.sh` copies four skills to `~/.hermes/skills/`. Wire You.com MCP (`https://api.you.com/mcp`) before your first automated run.

## Step 1: Choose The Job

Start by writing the job in one sentence.

Template:

```text
When I am [situation], I need [workflow output], so I can [decision or action].
```

Examples:

```text
When I am preparing for a customer meeting, I need a current account brief, so I can enter the call with relevant business context and suggested next actions.
```

```text
When I am preparing outbound to a target account, I need a source-backed company brief, so I can write a relevant message without inventing claims.
```

```text
When I am preparing for a partner conversation, I need a partner brief, so I can identify shared priorities, risks, and collaboration angles.
```

Your turn:

```text
When I am ______________________________________,
I need ________________________________________,
so I can _______________________________________.
```

## Step 2: Define The Workflow Input

Do not start with a giant prompt. Start with the smallest input set that makes the workflow useful.

For the first version, use:

```text
Required input:
- Account or company name

Optional inputs:
- Website URL
- Region
- Segment
- Relationship type
- Upcoming meeting date
- Current opportunity or project
- Internal notes or constraints
```

Recommended workshop input:

```text
Company: [COMPANY NAME]
Website: [OPTIONAL WEBSITE]
Use case: Prepare an account action brief
Audience: Account owner or customer-facing team
```

## Step 3: Define The Output Before You Run The Workflow

A workflow is easier to govern when the output format is stable.

Use this output schema:

```text
# Account Action Brief

## 1. Snapshot
- Company:
- Website:
- Industry:
- Size or scale:
- Business model:
- Source confidence:

## 2. Current Signals
- Recent company news:
- Product or strategy updates:
- Executive or leadership changes:
- Funding, financial, or market signals:
- Partnership or ecosystem signals:

## 3. Why This Account Might Care
- Likely priorities:
- Likely pain points:
- Possible buying triggers:
- Relevant transformation themes:

## 4. Suggested Actions
- Recommended next step:
- Suggested internal owner:
- Suggested outreach angle:
- Open questions to resolve:

## 5. Claims And Sources
- Claim:
- Source:
- Date or freshness:
- Confidence:

## 6. Review Notes
- Claims that need human review:
- Missing sources:
- Assumptions:
- Do not use externally until reviewed:
```

This structure matters because Hermes can reuse it, admins can inspect it, and users can compare outputs across accounts.

## Step 4: Run The First Draft In Hermes

In Hermes, start a new workflow, skill, playbook, or agent run.

Use this first prompt:

```text
Create a source-backed account action brief for [COMPANY NAME].

Use current public web sources through You.com.

Return the brief in this exact structure:

1. Snapshot
2. Current Signals
3. Why This Account Might Care
4. Suggested Actions
5. Claims And Sources
6. Review Notes

Rules:
- Do not make unsupported claims.
- Include source URLs for factual claims.
- Prefer official company pages, recent news, investor relations pages, product pages, and credible industry sources.
- Mark uncertain claims as uncertain.
- Separate sourced facts from recommendations.
- If evidence is weak or missing, say so.
```

Run it once.

Do not polish the wording yet. First, inspect the sources.

## Step 5: Use You.com Search For Current External Signals

Use You.com Search when you need current web and news results.

Ask Hermes or your You.com-connected tool to search for:

```text
[COMPANY NAME] recent announcements
[COMPANY NAME] product strategy
[COMPANY NAME] investor relations recent results
[COMPANY NAME] partnerships
[COMPANY NAME] AI automation data cloud security customer experience
```

If your workshop uses APIs directly, the conceptual call is:

```text
Search query: "[COMPANY NAME] recent announcements product strategy partnerships"
Count: 5-10 results
Return: title, URL, snippets, date/freshness if available
```

API demo command:

```bash
curl -G https://ydc-index.io/v1/search \
  -H "X-API-Key: $YDC_API_KEY" \
  --data-urlencode "query=AMD recent AI data center Instinct MI350 earnings partnerships" \
  -d count=5 \
  -d freshness=year
```

API demo command with trusted-domain focus:

```bash
curl -G https://ydc-index.io/v1/search \
  -H "X-API-Key: $YDC_API_KEY" \
  --data-urlencode "query=AMD AI data center Instinct EPYC investor product strategy" \
  -d count=5 \
  --data-urlencode "include_domains=amd.com"
```

What to point out in the video:

- `results.web` and `results.news` are separated but returned in one response.
- Each result includes a `title`, `url`, description or snippets, and often freshness metadata such as `page_age`.
- The snippets are already LLM-ready context, so Hermes can use them before fetching full pages.
- The `include_domains`, `exclude_domains`, `boost_domains`, `freshness`, `country`, and `language` parameters are governance levers, not just search tweaks.

Optional livecrawl moment:

```bash
curl -G https://ydc-index.io/v1/search \
  -H "X-API-Key: $YDC_API_KEY" \
  --data-urlencode "query=AMD Instinct MI350 data center AI" \
  -d count=3 \
  -d livecrawl=all \
  -d livecrawl_formats=markdown
```

Use `livecrawl` when you want the search result and the page content in one call. Use Contents when you already know exactly which URLs should be read.

Source selection rule:

Use at least:

- 1 official company source.
- 1 recent news or announcement source.
- 1 product, investor, partner, or industry source.

Avoid:

- Unsourced listicles.
- Old articles presented as current.
- Pages with unclear authorship when better sources exist.
- Social posts unless the workflow explicitly allows them.

## Step 6: Inspect The Sources

Before trusting the answer, inspect the evidence.

For each important source, capture:

```text
Source title:
Source URL:
Publisher:
Date or freshness:
What claim does this support?
Is this source strong enough for internal use?
Is this source strong enough for external use?
What is missing?
```

Use this quick score:

```text
3 = Strong source. Official, recent, directly supports the claim.
2 = Usable source. Credible but indirect or incomplete.
1 = Weak source. Old, vague, secondhand, or only partially relevant.
0 = Do not use. Unsupported, unreliable, or not relevant.
```

Keep only claims with score 2 or 3 in the main brief.

Move score 1 claims to "Review Notes."

Remove score 0 claims.

## Step 7: Use Contents For Source Reading

Use You.com Contents when you already have URLs and need clean page text.

This is useful for:

- Product pages.
- Press releases.
- Investor relations pages.
- Pricing pages.
- Documentation pages.
- Partner pages.

Prompt:

```text
Read these URLs and extract the clean page content:

[URL 1]
[URL 2]
[URL 3]

For each page, return:
- Title
- URL
- Last visible date, if present
- Key claims relevant to [WORKFLOW GOAL]
- Exact section or passage summary supporting each claim
```

Then ask Hermes:

```text
Update the account action brief using only the source content above.

For every factual claim, include a source URL.
If the source content does not support a claim, remove it or move it to Review Notes.
```

API demo command:

```bash
curl -X POST https://ydc-index.io/v1/contents \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": [
      "https://www.amd.com/en/newsroom/press-releases/2025-06-12-amd-expands-instinct-mi350-series.html"
    ],
    "formats": ["markdown", "metadata"],
    "crawl_timeout": 15,
    "max_age": 86400
  }'
```

What to point out in the video:

- Contents takes specific URLs, not a search query.
- The response returns source URL, title, clean `markdown` or `html`, and optional metadata.
- This is the best moment to show the "source inspection" habit: the API gives Hermes page text, but the workflow still decides which claims are allowed.
- `max_age` can force fresher fetches when stale cached content is a risk.

## Step 8: Use Research When The Question Requires Synthesis

Use You.com Research when the workflow needs a deeper synthesized answer, not just raw search results.

Good Research questions:

```text
What are the most important recent strategic signals for [COMPANY NAME], and what do they imply for a customer-facing team?
```

```text
What has changed in [COMPANY NAME]'s market position over the last 12 months?
```

```text
What are the strongest sourced reasons [COMPANY NAME] might care about [YOUR PRODUCT CATEGORY] right now?
```

Prompt:

```text
Use You.com Research to answer this question:

[QUESTION]

Return:
- A concise answer
- Inline citations or source references
- A source list
- Uncertainties
- Claims that should not be used externally without human review
```

Then fold the result back into the workflow:

```text
Merge this research into the account action brief.

Rules:
- Keep the brief short.
- Preserve source URLs.
- Remove duplicate claims.
- Keep recommendations separate from sourced facts.
- Mark assumptions clearly.
```

API demo command:

```bash
curl -X POST https://api.you.com/v1/research \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "What are the most important recent strategic signals for AMD, and what should an account team consider before a customer conversation?",
    "research_effort": "standard",
    "source_control": {
      "freshness": "year",
      "boost_domains": ["amd.com"]
    }
  }'
```

What to point out in the video:

- Research does more than return results. It searches, reads, and synthesizes a cited answer.
- `research_effort` controls depth and latency. Use `lite` for fast answers, `standard` for the default workshop demo, and `deep` or `exhaustive` when thoroughness matters more than speed.
- `source_control` lets the workflow prefer, include, exclude, or filter sources by freshness and geography.
- The response includes `output.content` and `output.sources`, which Hermes can turn into the account brief's "Claims And Sources" section.

Structured Research demo:

```bash
curl -X POST https://api.you.com/v1/research \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Extract the top three recent AMD strategic signals for an enterprise account team.",
    "research_effort": "standard",
    "output_schema": {
      "type": "object",
      "properties": {
        "signals": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "signal": { "type": "string" },
              "why_it_matters": { "type": "string" },
              "recommended_action": { "type": "string" }
            },
            "required": ["signal", "why_it_matters", "recommended_action"],
            "additionalProperties": false
          }
        }
      },
      "required": ["signals"],
      "additionalProperties": false
    }
  }'
```

Use this in the workshop to show why structured output matters: Hermes can take the API output and map it directly into a workflow card or CRM update draft.

## Optional API Add-On: Use Finance Research For Public Companies

Use Finance Research only when the account brief needs financial or market context.

Good Finance Research questions:

```text
What were the key drivers of [PUBLIC COMPANY]'s most recent earnings results?
What financial or market signals should an enterprise account team know before meeting with [PUBLIC COMPANY]?
What risk factors or strategic priorities appeared in [PUBLIC COMPANY]'s latest annual report?
```

API demo command:

```bash
curl -X POST https://api.you.com/v1/finance_research \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "What financial or market signals should an enterprise account team know before meeting with AMD?",
    "research_effort": "deep"
  }'
```

What to point out in the video:

- Finance Research uses a finance-optimized index rather than the open web.
- It returns the same high-level shape as Research: `output.content`, `content_type`, and `sources`.
- It is useful for public-company account briefs, earnings summaries, filings, and market-sensitive account context.
- It should not replace primary-source verification for investment, compliance, or regulated decisions.

## Step 9: Add Your Team Context

The first useful version can run on public sources only. The more valuable version connects public intelligence to team context.

Add context carefully. Start read-only.

Possible context sources:

- CRM account fields.
- Open opportunity notes.
- Customer success notes.
- Support themes.
- Call summaries.
- Internal account plans.
- Approved messaging docs.
- Product documentation.
- Competitive notes.

For the workshop, use sample or sanitized context:

```text
Internal context:
- Account segment:
- Relationship stage:
- Current opportunity:
- Known initiatives:
- Known objections:
- Existing products used:
- Recent meeting notes:
- Approved positioning:
- Data that must not be used externally:
```

Prompt:

```text
Update the account action brief using the internal context below.

Internal context:
[PASTE SANITIZED CONTEXT]

Rules:
- Treat internal context as private.
- Do not cite internal context as public evidence.
- Label internal-only recommendations clearly.
- Do not create external messaging from private information unless it has been approved for external use.
- Keep public-source claims and internal observations separate.
```

## Step 10: Create The Connector Map

A workflow becomes real when you know which tools it reads from, writes to, and asks humans to review.

Fill this out:

```text
Workflow name:
Primary user:
Workflow owner:

Read-only tools:
- You.com Search:
- You.com Contents:
- You.com Research:
- You.com Finance Research, optional for public-company financial context:
- CRM:
- Docs:
- Notes:
- Support:

Draft-only tools:
- Email draft:
- Slack or Teams review request:
- CRM update draft:
- Meeting brief:

Write-enabled tools:
- None for pilot, unless explicitly approved.

Blocked tools or data:
- Sensitive customer data:
- Unapproved legal/compliance language:
- Personal data not needed for the workflow:
- Anything outside pilot scope:
```

Recommended first pilot:

```text
Read from public web and approved internal context.
Draft review messages and CRM updates.
Do not auto-send outreach.
Do not auto-update CRM.
Require a human to approve external use.
```

## Step 11: Add Review Gates

Review gates make the workflow usable without making it reckless.

Use four states:

```text
Draft:
The workflow produced an output, but no human has reviewed it.

Needs edits:
A reviewer found unsupported claims, weak sources, tone issues, or missing context.

Approved for internal use:
The brief is safe to use for planning, meeting prep, or internal discussion.

Approved for external use:
The claims, sources, and wording are safe for outreach, customer communication, or public-facing use.
```

Add this review prompt:

```text
Review this account action brief.

Check:
- Are all factual claims source-backed?
- Are sources recent enough?
- Are recommendations separated from facts?
- Are internal-only details clearly marked?
- Are there claims that should not be used externally?
- Is the suggested next action reasonable?

Return:
- Status: Draft, Needs edits, Approved for internal use, or Approved for external use
- Required edits
- Weak or missing sources
- External-use concerns
- Final reviewer notes
```

## Step 12: Create The Workflow Card

The workflow card is the handoff between "this prompt worked once" and "our team can run this repeatedly."

Copy this template:

```text
# Workflow Card

Workflow name:
/account-action-brief

Purpose:
Create a current, source-backed action brief for a company, customer, prospect, or partner.

Primary user:
[ROLE]

Workflow owner:
[PERSON OR TEAM]

Trigger:
[Example: preparing for a meeting, account review, outbound sequence, QBR, partner call]

Required inputs:
- Company or account name

Optional inputs:
- Website
- Segment
- Region
- Relationship stage
- Meeting date
- Opportunity context
- Internal notes

Allowed tools:
- You.com Search
- You.com Contents
- You.com Research
- Approved internal context sources

Blocked tools or data:
- [LIST]

Output format:
- Snapshot
- Current Signals
- Why This Account Might Care
- Suggested Actions
- Claims And Sources
- Review Notes

Review rules:
- Every factual claim needs a source or must be marked as an assumption.
- External-use content requires human approval.
- Internal-only context must be labeled.
- Weakly sourced claims move to Review Notes.

Success metrics:
- Time saved per brief
- Percent of briefs with reviewer edits
- Percent of claims with strong sources
- Number of briefs used in real workflow
- Number of follow-up actions created

Pilot plan:
- Week 0: setup
- Week 1: small test
- Week 2: measured pilot
```

## Step 13: Turn The Prompt Into A Reusable Hermes Workflow

Once the prompt works, package it.

In Hermes, create a reusable skill, playbook, or workflow with:

```text
Name:
/account-action-brief

Description:
Creates a current, source-backed account action brief using You.com web intelligence and approved team context.

Inputs:
- company_name: required
- company_url: optional
- workflow_goal: optional
- internal_context: optional
- output_audience: internal or external draft

Tools:
- You.com Search
- You.com Contents
- You.com Research
- You.com Finance Research, optional for public-company financial context
- Approved internal read-only sources
- Draft-only communication tools, if approved

Output:
Account Action Brief

Review:
Human review required before external use.
```

Use this reusable instruction:

```text
You are running the `/account-action-brief` workflow.

Goal:
Create a concise, source-backed account action brief that helps a team decide what to do next.

Required behavior:
1. Confirm the account or company name.
2. Search for current public sources using You.com.
3. Prefer official, recent, and directly relevant sources.
4. Use Contents to inspect important URLs when snippets are not enough.
5. Use Research only when synthesis is needed.
6. Separate sourced facts from recommendations.
7. Include source URLs for factual claims.
8. Mark weak evidence and assumptions.
9. Label internal-only context.
10. Produce the brief in the approved output format.
11. End with review status and next action.

Do not:
- Invent facts.
- Treat old sources as current.
- Mix private internal context into external messaging.
- Auto-send messages or write to systems unless the workflow has explicit approval.
```

### Faster path: Hermes Desktop skill pack

Instead of authoring from scratch in Workflow Studio, install the workshop skill pack:

```bash
cd workshop-app/hermes-desktop
chmod +x install.sh
./install.sh
```

| Skill | Command | When to use |
|-------|---------|-------------|
| account-action-brief | `/account-action-brief` | Main workflow — Week 1 |
| meeting-prep | `/meeting-prep` | Calendar-triggered briefs — Week 2+ |
| community-pulse | `/community-pulse` | Facilitator weekly digest for alumni |
| workshop-60min | `/workshop-60min` | Agenda + post-event pointers inside Hermes |

Wire You.com MCP (`you-search`, `you-contents`, `you-research`), restart Hermes, then test:

```text
/account-action-brief

company: AMD
website: https://www.amd.com
```

See `workshop-app/HERMES-DESKTOP-SETUP.md` for full install and test commands.

## Step 14: Test The Workflow With Three Accounts

Do not pilot after one good run. Test with three different examples.

Use:

```text
Account 1: A company with lots of public news.
Account 2: A company with limited public information.
Account 3: A company where your internal context matters.
```

For each run, score:

```text
Account:
Was the output useful? yes/no
Were the sources strong? 0-3
Were there unsupported claims? yes/no
Did the workflow separate facts from recommendations? yes/no
Did the output match the required format? yes/no
Would you use this in a real workflow? yes/no
What should change before pilot?
```

## Step 15: Create A Quality Scorecard

Use this lightweight scorecard:

```text
Correctness:
0 = Important claims are wrong.
1 = Some claims are questionable.
2 = Mostly correct with minor edits.
3 = Correct based on available sources.

Citation support:
0 = No useful sources.
1 = Sources are weak or mismatched.
2 = Most key claims have sources.
3 = Every important factual claim has a strong source.

Freshness:
0 = Sources are stale or undated.
1 = Some sources are current.
2 = Most important sources are current.
3 = Sources are clearly current for the decision.

Usefulness:
0 = Not actionable.
1 = Some useful context.
2 = Useful with edits.
3 = Clear next action.

Review burden:
0 = Too much cleanup.
1 = Heavy edits required.
2 = Light edits required.
3 = Ready after quick review.
```

Pilot rule:

```text
Do not expand the workflow until average scores are 2 or higher and there are no recurring unsupported-claim issues.
```

## Step 16: Plan The Two-Week Pilot (Champions Only)

**Not required in the 60-minute workshop.** Default homework is: join Discord + run 3 briefs (Week 1). Use this step only if you are a champion pitching team adoption — rollout template is in Download All.

Keep the pilot small enough to learn from.

Use this plan:

```text
Week 0: Setup
- Pick 5 users.
- Pick 20 accounts.
- Confirm workflow owner.
- Confirm allowed tools.
- Confirm blocked data.
- Confirm review rules.
- Create feedback form.

Week 1: Controlled runs
- Run 10 briefs.
- Require human review.
- Track unsupported claims.
- Track source quality.
- Track time saved.
- Capture user edits.

Week 2: Real workflow use
- Run 25 briefs.
- Use briefs in real meetings, outbound prep, or account reviews.
- Draft CRM updates or review handoffs, but do not auto-write unless approved.
- Review metrics.
- Decide whether to expand, revise, or stop.
```

## Step 17: Decide What Happens After The Pilot

At the end of the pilot, choose one of three paths:

```text
Expand:
The workflow is useful, source-backed, and reviewable. Add more users or adjacent workflows.

Revise:
The workflow is promising but needs better sources, clearer outputs, tighter governance, or better integrations.

Stop:
The workflow does not save time, does not improve quality, or requires too much review.
```

Decision template:

```text
Pilot decision:
Expand / Revise / Stop

Evidence:
- Usage:
- Time saved:
- Source quality:
- User satisfaction:
- Review burden:
- Business impact:

Next owner:
Next milestone:
```

## Community Continuation (You.com Discord)

**Default close for every attendee** — not just champions.

1. **Join:** https://discord.gg/2C4WgryxSD
2. **Introduce yourself** in `#introductions` — say you joined from the Account Action Brief workshop
3. Include: your role, what you're building, first company you'll brief
4. **Week 1 challenge:** run 3 briefs; share one learning in Discord

Suggested intro:

```text
Hi! I joined from the Account Action Brief workshop (Hermes + You.com).

- Name / role:
- What I'm building: /account-action-brief workflow
- First company I'll brief:
- One thing I want to learn in this community:
```

Facilitators run `/community-pulse` weekly and post digests to Discord. Members run their own agents and reply in the server.

See `workshop-app/COMMUNITY-CONTINUATION.md` for Week 2–5+ challenges.

## Calendar-Triggered Meeting Prep (Week 2+)

After `/account-action-brief` works, the natural upgrade is **briefs before meetings** without manual triggering every time.

Pattern:

```text
Calendar (read-only)
  → detect upcoming customer meetings
  → extract company name
  → run /account-action-brief via You.com MCP
  → deliver Draft brief to you (not to the customer)
  → you review before the meeting
```

The `/meeting-prep` skill in the desktop pack documents this flow. Calendar read-only wiring is post-workshop Hermes connector work — not built in the 60-min app.

See `workshop-app/CALENDAR-MEETING-PREP.md` for connector map additions and test commands.

## Optional: Add A Review Handoff

If your team uses Slack, Teams, email, or a ticketing system, add a review handoff.

Draft-only handoff prompt:

```text
Create a review request for this account action brief.

Audience:
[REVIEWER OR CHANNEL]

Include:
- Account name
- Why the brief was created
- 3-bullet summary
- Claims that need review
- Suggested next action
- Link to the full brief
- Requested decision: approve, edit, reject, or request more research

Do not send automatically. Return as a draft.
```

Review request format:

```text
Review request: [ACCOUNT NAME] action brief

Why this exists:
[ONE SENTENCE]

Top signals:
- [SIGNAL 1]
- [SIGNAL 2]
- [SIGNAL 3]

Needs review:
- [CLAIM OR RECOMMENDATION]

Requested decision:
Approve / Edit / Reject / More research needed

Brief:
[LINK]
```

## Optional: Add A CRM Update Draft

For the first pilot, draft CRM updates instead of writing automatically.

Prompt:

```text
Create a CRM update draft from this account action brief.

Fields:
- Account summary
- Current signal
- Suggested next step
- Open question
- Source URL
- Review status

Rules:
- Keep it concise.
- Do not include private reasoning that should not live in CRM.
- Do not write to CRM automatically.
- Mark as draft pending human approval.
```

## Optional: Build A Trusted Answer Workflow

Once the account brief works, you can reuse the same pattern for trusted answer experiences.

Workflow:

```text
/trusted-answer
```

Input:

```text
User question
Audience
Required freshness
Allowed sources
Desired depth
```

Output:

```text
Short answer
Sources
Confidence
Follow-up questions
Go-deeper path
Review notes
```

Prompt:

```text
Answer this question using source-backed web intelligence:

[QUESTION]

Return:
- Short answer
- Source-backed claims
- Source URLs
- Freshness notes
- Confidence level
- Follow-up questions
- When to escalate to deeper research

Rules:
- If raw search results are enough, keep the answer short.
- If synthesis is required, use Research.
- If sources disagree, say so.
- If evidence is weak, do not overstate the answer.
```

## API Implementation Path

Use this section when your audience includes developers or solutions engineers.

You.com currently documents three core APIs for real-time web intelligence plus a finance-specific research API:

- Web Search API for structured web and news results.
- Contents API for clean Markdown or HTML from specified URLs.
- Research API for multi-step research and citation-backed synthesis.
- Finance Research API for citation-backed answers over a finance-optimized index.

Recommended implementation pattern:

```text
1. User submits workflow input in Hermes.
2. Hermes calls Web Search to discover candidate sources.
3. Hermes filters sources by relevance, freshness, and trust.
4. Hermes calls Contents for the highest-value URLs.
5. Hermes calls Research when synthesis is needed.
6. Hermes optionally calls Finance Research for public-company financial context.
7. Hermes maps API outputs into the account brief schema.
8. Human reviews the output.
9. Workflow stores the final card, metrics, and feedback.
```

Environment variable:

```bash
export YDC_API_KEY="your-key"
```

Pseudo-code:

```python
import os
import requests

YDC_API_KEY = os.environ["YDC_API_KEY"]

company_name = "AMD"
workflow_goal = "Create a source-backed account action brief."

headers = {
    "X-API-Key": YDC_API_KEY,
    "Content-Type": "application/json",
}

# 1. Discover candidate sources.
search_response = requests.get(
    "https://ydc-index.io/v1/search",
    headers={"X-API-Key": YDC_API_KEY},
    params={
        "query": f"{company_name} recent AI data center Instinct earnings partnerships",
        "count": 5,
        "freshness": "year",
    },
)
search_response.raise_for_status()
search_results = search_response.json()

# 2. Select URLs for source inspection.
urls = [
    result["url"]
    for result in search_results.get("results", {}).get("web", [])
    if "url" in result
][:3]

# 3. Fetch clean page content for the best URLs.
contents_response = requests.post(
    "https://ydc-index.io/v1/contents",
    headers=headers,
    json={
        "urls": urls,
        "formats": ["markdown", "metadata"],
        "crawl_timeout": 15,
        "max_age": 86400,
    },
)
contents_response.raise_for_status()
pages = contents_response.json()

# 4. Ask for deeper synthesis only when the workflow needs it.
research_response = requests.post(
    "https://api.you.com/v1/research",
    headers=headers,
    json={
        "input": f"What are the most important recent strategic signals for {company_name}, and what should an account team consider?",
        "research_effort": "standard",
        "source_control": {
            "freshness": "year",
            "boost_domains": ["amd.com"],
        },
    },
)
research_response.raise_for_status()
research = research_response.json()

# 5. Hand the structured evidence to Hermes.
hermes_context = {
    "company_name": company_name,
    "workflow_goal": workflow_goal,
    "search_results": search_results,
    "source_pages": pages,
    "research": research,
}

# Hermes then maps this context into:
# - Snapshot
# - Current Signals
# - Why This Account Might Care
# - Suggested Actions
# - Claims And Sources
# - Review Notes
```

MCP implementation pattern:

```text
If Hermes has MCP-based tool access, expose only the You.com tools this workflow needs:

- you-search
- you-contents
- you-research

Optional:
- finance research tool or API connector for public-company financial context

Admin rule:
Expose discovery and reading tools first. Keep writeback tools draft-only until the pilot proves quality and review behavior.
```

## API Demo Video Module

Use this module to record a five- to seven-minute demo video.

Video promise:

```text
In this demo, we will turn one company name into a governed account workflow by calling the You.com APIs directly, then handing the evidence to Hermes.
```

Recommended screen sequence:

```text
1. Show the workflow goal.
2. Show the API key environment variable.
3. Run Web Search and inspect structured results.
4. Run Contents on one or more selected URLs.
5. Run Research for synthesis.
6. Optional: run Finance Research for public-company context.
7. Show Hermes converting the API evidence into `/account-action-brief`.
8. Show the review checklist and pilot card.
```

Narration:

```text
The important thing to notice is that each API has a distinct job.

Search discovers candidate sources.
Contents reads the sources we choose.
Research synthesizes the strategic answer with citations.
Finance Research adds financial context when the account is public or market-sensitive.
Hermes turns those API calls into a workflow that a team can run again.
```

Demo output to show:

```text
Search:
- title
- URL
- snippets
- page_age or freshness metadata

Contents:
- URL
- title
- markdown
- metadata

Research:
- output.content
- output.sources

Hermes:
- final account action brief
- claims and sources
- review notes
- workflow card
```

Fallback if an API call fails live:

```text
If Search fails, show a saved JSON response and continue.
If Contents fails for one URL, choose another URL from the Search response.
If Research takes longer than expected, explain effort levels and cut to a saved response.
If Finance Research is not relevant, skip it and say it is optional for public-company or financial workflows.
```

## Common Failure Modes

Watch for these:

```text
The workflow sounds confident but has weak sources.
Fix: Require source URLs and move weak claims to Review Notes.

The workflow produces a beautiful brief that is too long.
Fix: Enforce the output structure and word limits.

The workflow mixes internal context with public claims.
Fix: Label internal-only context and separate recommendations from facts.

The workflow works for one company but fails for another.
Fix: Test three accounts before piloting.

The workflow creates action items nobody owns.
Fix: Add owner, trigger, and next-step fields to the workflow card.

The workflow is useful but not reusable.
Fix: Package it as a Hermes skill or playbook with stable inputs and outputs.

The workflow is too risky to expand.
Fix: Keep the pilot draft-only and require human review before external use.
```

## Facilitator Script

### 60-minute live (default)

Use `workshop-app/FACILITATOR-60MIN.md` and the app at http://localhost:8080. Key lines:

**Opening:**

```text
You.com gives us live evidence. Hermes turns that into a governed workflow you can reuse.
Depth is in the app after today — this hour is the complete story.
```

**At Full Demo Chain:**

```text
We run APIs manually here so you see each step.
In Hermes, /account-action-brief runs this same chain automatically — you review the Draft.
```

**At Agent Build:**

```text
Install the 4-skill pack or create the skill in Studio. Wire MCP tonight if you don't finish in the room.
```

**Close:**

```text
Join the You.com Discord — introduce yourself from this workshop.
Week 1: run three briefs. Week 2+: try /meeting-prep for calendar-triggered prep.
Rollout template in Download All is for champions only.
```

### Full tutorial (90-min or self-paced)

Use this script to run the written tutorial.

Opening:

```text
Today we are not trying to build a perfect AI answer.
We are building a reusable workflow.

The difference is that a workflow has inputs, tools, review rules, owners, metrics, and a pilot plan.
```

Before the first run:

```text
Pick one workflow your team already does manually.
If you cannot name the manual workflow, do not automate it yet.
```

When sources appear:

```text
Pause here.
Before we improve the writing, we inspect the sources.
The source inspection step is what separates a useful workflow from a confident guess.
```

When adding integrations:

```text
Start read-only.
Then allow draft-only outputs.
Only add writeback after the team trusts the workflow and knows where review belongs.
```

When packaging:

```text
The prompt is not the product.
The reusable workflow is the product.
Package the inputs, allowed tools, output format, review rules, owner, and success metrics.
```

Close:

```text
Join the You.com Discord and run three briefs this week.
If you are a champion, pick five users and run the two-week pilot.
Otherwise leave with one workflow card and a working /account-action-brief skill.
Measure whether it saved time, improved quality, and created better next actions.
```

## Final Checklist

Before sharing or piloting your workflow, confirm:

```text
[ ] The workflow has a clear job.
[ ] Required inputs are minimal.
[ ] Output format is stable.
[ ] You.com sources are inspected.
[ ] Factual claims have source URLs.
[ ] Internal context is labeled.
[ ] Allowed tools are explicit.
[ ] Blocked data is explicit.
[ ] Draft-only and write-enabled actions are separated.
[ ] Human review gates are defined.
[ ] The workflow is packaged in Hermes (skill pack installed or Studio skill created).
[ ] You.com MCP is wired (or Evidence Bundle fallback documented).
[ ] Three test runs have been scored.
[ ] Joined You.com Discord and posted intro.
[ ] Week 1: ran at least one test brief (target: 3).
[ ] Two-week pilot owner assigned (champions only).
[ ] Success metrics defined (champions only).
[ ] /meeting-prep explored (Week 2+, optional).
```

## Source Notes For You.com

The You.com documentation describes three core APIs for real-time web intelligence: Web Search, Contents, and Research. The docs position Web Search as structured web and news results, Contents as clean Markdown or HTML retrieval from URLs, and Research as multi-step source-backed synthesis. You.com also documents MCP setup for connecting web search to MCP-compatible tools and a citation-grounding pattern based on source URLs, titles, and snippets.

References:

- You.com Quickstart: https://you.com/docs/quickstart
- You.com Web Search API guide: https://you.com/docs/guides/search
- You.com Search API reference: https://you.com/docs/api-reference/search/v1-search
- You.com Contents API guide: https://you.com/docs/guides/contents
- You.com Contents API reference: https://you.com/docs/api-reference/contents
- You.com Research API guide: https://you.com/docs/guides/research
- You.com Research API reference: https://you.com/docs/api-reference/research/v1-research
- You.com Finance Research API guide: https://you.com/docs/guides/finance-research
- You.com Finance Research API reference: https://you.com/docs/api-reference/finance-research/v1-finance_research
- You.com MCP Server for Web Search: https://you.com/docs/capabilities/mcp-server-for-web-search
- You.com Grounding With Citations: https://you.com/docs/capabilities/grounding-llm-responses-with-citations
