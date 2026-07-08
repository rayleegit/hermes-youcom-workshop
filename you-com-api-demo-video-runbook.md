# You.com API Demo Video Runbook

Google Doc:
https://docs.google.com/document/d/17P8T-hZiOReVCFptaYdNGgMGSePsCsRIT0aN_AdH-BM/edit?usp=drivesdk

## Purpose

Use this to record a short API-focused demo for the Hermes Workflow Studio workshop.

The video should show the audience that You.com is not a black box. It is a set of APIs that Hermes can call in sequence: discover sources, read source content, synthesize with citations, optionally add financial context, and then package the result as a reusable workflow.

## Recommended Length

5 to 7 minutes.

## Demo Account

Use one account throughout the video.

```text
Company: ServiceNow
Workflow: /account-action-brief
Audience: Account owner, customer success lead, partnerships lead, or marketer
```

## Setup Shot

Show the terminal or notebook.

```bash
export YDC_API_KEY="your-key"
```

Narration:

```text
We are going to build the evidence path before we show the final AI output. That means each API call has a job: Search discovers sources, Contents reads selected sources, Research synthesizes across sources, and Hermes packages the result into a reusable workflow.
```

## Scene 1: Web Search API

Goal:
Find current candidate sources.

Command:

```bash
curl -G https://ydc-index.io/v1/search \
  -H "X-API-Key: $YDC_API_KEY" \
  --data-urlencode "query=ServiceNow recent AI agents announcements partnerships" \
  -d count=5 \
  -d freshness=year
```

Callouts:

- Show `results.web`.
- Show any `results.news` if present.
- Show `title`, `url`, snippets, and `page_age`.
- Explain that snippets are already useful RAG context.

Narration:

```text
The Search API gives Hermes structured web and news results. This is the source discovery step. We are not asking the model to guess what is current. We are giving the workflow fresh candidate sources with titles, URLs, snippets, and freshness metadata.
```

## Scene 2: Search With Domain Control

Goal:
Show governance and source control.

Command:

```bash
curl -G https://ydc-index.io/v1/search \
  -H "X-API-Key: $YDC_API_KEY" \
  --data-urlencode "query=ServiceNow AI agents announcements investor product strategy" \
  -d count=5 \
  --data-urlencode "include_domains=servicenow.com"
```

Callouts:

- `include_domains` is a strict allowlist.
- `boost_domains` can prefer trusted sources without excluding others.
- `exclude_domains` can block noisy or unsafe sources.
- `freshness`, `country`, and `language` are also workflow controls.

Narration:

```text
These parameters are governance controls. For a workflow, source policy matters. We can decide whether Hermes should search broadly, prefer certain domains, or restrict itself to approved domains.
```

## Scene 3: Contents API

Goal:
Read selected URLs as clean source text.

Command:

```bash
curl -X POST https://ydc-index.io/v1/contents \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": [
      "https://www.servicenow.com/company/media/press-room.html"
    ],
    "formats": ["markdown", "metadata"],
    "crawl_timeout": 15,
    "max_age": 86400
  }'
```

Callouts:

- Contents takes URLs, not a query.
- The response includes clean `markdown`, optional `html`, and `metadata`.
- Use this when snippets are not enough.
- `max_age` helps control cache freshness.

Narration:

```text
Once Search gives us candidate URLs, Contents lets us read selected pages cleanly. This is the source inspection step. The workflow can now quote or summarize from page content rather than relying only on a snippet.
```

## Scene 4: Research API

Goal:
Show citation-backed synthesis.

Command:

```bash
curl -X POST https://api.you.com/v1/research \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "What are the most important recent strategic signals for ServiceNow, and what should an account team consider before a customer conversation?",
    "research_effort": "standard",
    "source_control": {
      "freshness": "year",
      "boost_domains": ["servicenow.com"]
    }
  }'
```

Callouts:

- Research runs multiple searches and synthesizes an answer.
- `research_effort` controls speed/depth.
- `source_control` can guide domains, freshness, and geography.
- Show `output.content` and `output.sources`.

Narration:

```text
Research is the synthesis layer. We use it when the question needs reasoning across sources. The key fields for the workflow are the answer content and the source list, because Hermes will map those into the brief and review checklist.
```

## Scene 5: Structured Research Output

Goal:
Show API output that maps cleanly into a workflow card.

Command:

```bash
curl -X POST https://api.you.com/v1/research \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Extract the top three recent ServiceNow strategic signals for an enterprise account team.",
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

Callouts:

- Structured output is useful when another system needs predictable fields.
- Sources remain available separately in `output.sources`.
- This is the bridge into Hermes workflow packaging.

Narration:

```text
Structured output makes the API output easier to operationalize. Instead of only getting prose, we can ask for predictable fields that map into a workflow card, CRM draft, or review checklist.
```

## Scene 6: Optional Finance Research API

Goal:
Show API breadth for public-company account intelligence.

Command:

```bash
curl -X POST https://api.you.com/v1/finance_research \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "What financial or market signals should an enterprise account team know before meeting with ServiceNow?",
    "research_effort": "deep"
  }'
```

Callouts:

- Use this only when financial context matters.
- The response shape is similar to Research.
- The index is finance-optimized.
- Treat citations as starting points for verification in regulated contexts.

Narration:

```text
Finance Research is optional in this workshop, but it is a strong add-on for public-company account briefs. It lets the same Hermes workflow pull in earnings, filings, market context, and financially relevant signals.
```

## Scene 7: Hermes Workflow Packaging

Goal:
Show the same evidence becoming a reusable workflow.

Prompt:

```text
Create `/account-action-brief` using the API evidence below.

Use the Search results for source discovery.
Use the Contents output for source inspection.
Use the Research output for synthesis.
Use Finance Research only as optional public-company context.

Return:
- Snapshot
- Current Signals
- Why This Account Might Care
- Suggested Actions
- Claims And Sources
- Review Notes
- Workflow Card
```

Narration:

```text
This is where Hermes matters. The APIs provide live intelligence. Hermes turns that intelligence into a workflow with inputs, tools, output schema, review rules, and a pilot plan.
```

## Closing Shot

Show the final workflow card.

Closing line:

```text
The output is useful, but the workflow is the product. Once the API path works, package it, govern it, and pilot it with a small team for two weeks.
```

## Backup Plan

Prepare saved JSON responses for:

- Search
- Contents
- Research
- Finance Research

Use the saved responses if a live API call is slow, rate-limited, or blocked by network setup.

## Assets To Prepare

- Terminal or notebook with commands ready.
- API key set in the environment.
- One saved Search response.
- One saved Contents response.
- One saved Research response.
- Optional saved Finance Research response.
- Hermes prompt ready to paste.
- Final workflow card ready to display.
