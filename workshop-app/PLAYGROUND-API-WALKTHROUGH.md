# You.com Platform Playground — API Walkthrough Examples

Facilitator reference for the **live playground demo** (slides 4–11).  
**Open:** https://you.com/platform → **API Playground**  
**Demo company:** AMD · **Attendees' goals:** defined later in Hermes (Renewal / Outbound / Competitive / Partner)

---

## Before you start

| Item | Value |
|------|--------|
| Playground | https://you.com/platform |
| API key | https://you.com/settings/api → paste into playground auth |
| Auth header (curl) | `X-API-Key: $YDC_API_KEY` |
| Workshop app (fallback) | `DEMO_MODE=true ./run.sh` if live APIs fail |

**Say once:** "Each API has one job. We run them manually here so you see the evidence chain. Hermes automates the same chain via MCP on `/account-action-brief`."

---

## 1. Web Search API

**Endpoint:** `GET https://ydc-index.io/v1/search`  
**Job:** Discover candidate sources — structured JSON, not a finished brief.

### Key parameters (playground / curl)

| Parameter | Type | Example | What it does |
|-----------|------|---------|--------------|
| `query` | string | see below | Search string — company + topic + goal keywords |
| `count` | int | `5` | Number of results (start with 5 in demo) |
| `freshness` | string | `year` | Recency filter — also try `month` for stricter freshness |
| `include_domains` | string[] | `["amd.com"]` | **Strict allowlist** — only these domains |
| `boost_domains` | string[] | `["amd.com", "reuters.com"]` | Prefer trusted sources; others still allowed |
| `exclude_domains` | string[] | `["reddit.com"]` | Block noisy or unsafe domains |
| `country` | string | `US` | Geo bias for results |
| `language` | string | `en` | Language filter |

### Example queries (AMD — pick one for live demo)

**General / opening query**
```text
AMD data center Instinct MI350 earnings partnerships
```

**By brief goal (use in Research too — preview for attendees)**

| Goal | Search query |
|------|----------------|
| **Renewal** | `AMD enterprise renewal data center GPU Instinct customer expansion 2025` |
| **Outbound** | `AMD Instinct MI350 enterprise AI data center customer wins announcements` |
| **Competitive** | `AMD vs NVIDIA data center AI GPU market share Instinct MI350` |
| **Partner** | `AMD cloud hyperscaler partnership Instinct EPYC ecosystem 2025` |

**Governance demo — trusted domain only**
```text
query: AMD AI data center Instinct EPYC investor product strategy
include_domains: amd.com
count: 5
freshness: year
```

### curl (View Code in playground)

```bash
export YDC_API_KEY="your-key"

curl -G https://ydc-index.io/v1/search \
  -H "X-API-Key: $YDC_API_KEY" \
  --data-urlencode "query=AMD data center Instinct MI350 earnings partnerships" \
  -d count=5 \
  -d freshness=year
```

**With domain allowlist:**
```bash
curl -G https://ydc-index.io/v1/search \
  -H "X-API-Key: $YDC_API_KEY" \
  --data-urlencode "query=AMD AI Instinct data center strategy" \
  -d count=5 \
  -d freshness=year \
  --data-urlencode "include_domains=amd.com"
```

### What to point at in the response

| Field | Where | Say |
|-------|--------|-----|
| `results.web[]` | Main web hits | "Structured candidates — not prose" |
| `results.news[]` | News bucket (if present) | "News vs web — both are evidence" |
| `title` | Each item | Headline for the brief |
| `url` | Each item | Goes into Claims & Sources later |
| `description` or `snippets` | Each item | Quick context — may not be enough for claims |
| `page_age` | Each item | Freshness — call out stale vs recent |

**Pick 1–2 URLs** from Search for the Contents step (prefer `amd.com` press release or tier-1 news).

---

## 2. Contents API

**Endpoint:** `POST https://ydc-index.io/v1/contents`  
**Job:** Read full page text from URLs you already selected — not a search.

### Key parameters

| Parameter | Type | Example | What it does |
|-----------|------|---------|--------------|
| `urls` | string[] | see below | 1–3 URLs from Search results |
| `formats` | string[] | `["markdown", "metadata"]` | Return clean markdown + metadata |
| `crawl_timeout` | int | `15` | Seconds to wait per page |
| `max_age` | int | `86400` | Cache max age in seconds (86400 = 24h) |

### Example URLs (AMD — use URLs from your Search run)

If Search returned official AMD newsroom links, use those. Examples:

```json
{
  "urls": [
    "https://www.amd.com/en/newsroom/press-releases/2025-06-12-amd-expands-instinct-mi350-series.html"
  ],
  "formats": ["markdown", "metadata"],
  "crawl_timeout": 15,
  "max_age": 86400
}
```

**Multi-URL (compare press release + news):**
```json
{
  "urls": [
    "https://www.amd.com/en/newsroom/press-releases/2025-06-12-amd-expands-instinct-mi350-series.html",
    "https://www.reuters.com/technology/..."
  ],
  "formats": ["markdown", "metadata"],
  "crawl_timeout": 15,
  "max_age": 86400
}
```

### curl

```bash
curl -X POST https://ydc-index.io/v1/contents \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://www.amd.com/en/newsroom/press-releases/2025-06-12-amd-expands-instinct-mi350-series.html"],
    "formats": ["markdown", "metadata"],
    "crawl_timeout": 15,
    "max_age": 86400
  }'
```

### What to point at in the response

| Field | Say |
|-------|-----|
| `markdown` (per URL) | "Page-level evidence — verify claims here" |
| `metadata` | Title, dates, domain |
| `url` | Must match what you requested |

**Say:** "Search gave snippets. Contents gives the full page. Hermes calls `you-contents` after Search picks URLs."

---

## 3. Research API

**Endpoint:** `POST https://api.you.com/v1/research`  
**Job:** Multi-source synthesis with citations — `output.content` + `output.sources`.

### Key parameters

| Parameter | Type | Example | What it does |
|-----------|------|---------|--------------|
| `input` | string | see below | The question — include company + goal |
| `research_effort` | string | `standard` | `lite` · `standard` · `deep` · `exhaustive` (deeper = slower) |
| `source_control.freshness` | string | `year` | Limit source recency |
| `source_control.boost_domains` | string[] | `["amd.com"]` | Prefer official / trusted domains |
| `source_control.include_domains` | string[] | `["amd.com"]` | Strict allowlist for research sources |
| `output_schema` | object | optional | Structured JSON fields (advanced — skip in 60-min) |

### Example `input` strings (AMD — match brief goal)

**Renewal**
```text
What are the most important recent strategic signals for AMD that matter for an enterprise renewal conversation — product roadmap, data center GPU adoption, and expansion risks? What should an account team prepare before the renewal call?
```

**Outbound**
```text
What are the most important recent AMD signals for outbound prospecting — Instinct MI350, data center AI wins, and enterprise buying triggers? What should a rep research before a first meeting?
```

**Competitive**
```text
What are AMD's recent competitive positioning signals in data center AI GPUs versus NVIDIA — Instinct MI350, ecosystem, and customer workload fit? What should an account team highlight in a competitive deal?
```

**Partner**
```text
What are AMD's recent partnership and ecosystem signals — hyperscaler, OEM, and software stack — relevant to a co-sell or partner opportunity?
```

**Default (if not picking a preset)**
```text
What are the most important recent strategic signals for AMD, and what should an account team consider before a customer conversation?
```

### Request body (playground JSON)

```json
{
  "input": "What are the most important recent strategic signals for AMD that matter for an enterprise renewal conversation? What should an account team prepare before the call?",
  "research_effort": "standard",
  "source_control": {
    "freshness": "year",
    "boost_domains": ["amd.com"]
  }
}
```

**Stricter sources (official only):**
```json
{
  "input": "Summarize AMD's latest data center AI strategy from official and primary sources.",
  "research_effort": "standard",
  "source_control": {
    "freshness": "month",
    "include_domains": ["amd.com"]
  }
}
```

### curl

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

### What to point at in the response

| Field | Say |
|-------|-----|
| `output.content` | Synthesized answer — maps to brief sections 2–4 |
| `output.sources[]` | Citations — every key claim should trace here |
| Source URL in each citation | "This becomes Claims & Sources in Hermes" |
| Wait time (30–90s) | Narrate: "Research searches, reads, reasons — not instant retrieval" |

**Say:** "Same question shape you'll use in Hermes — company + goal in the `input`. MCP tool `you-research` wraps this."

---

## 4. Finance Research API (optional — slide 10)

**Endpoint:** `POST https://api.you.com/v1/finance_research`  
**Job:** Finance-optimized index — earnings, filings, market context.  
**Timing:** Often **2–5 minutes** — skip live demo in 60-min unless buffer.

| Parameter | Notes |
|-----------|--------|
| `input` | Finance-focused question |
| `research_effort` | **`deep` or `exhaustive` only** — `standard` returns 422 |

### Example

```json
{
  "input": "What financial and market signals should an account team know before meeting with AMD — data center revenue, Instinct adoption, analyst outlook?",
  "research_effort": "deep"
}
```

```bash
curl -X POST https://api.you.com/v1/finance_research \
  -H "X-API-Key: $YDC_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": "What financial signals matter for AMD data center GPU growth and enterprise accounts?",
    "research_effort": "deep"
  }'
```

---

## 5. Structured Research (optional — mention only)

Add `output_schema` when you need predictable fields (CRM, workflow card, Suggested Actions).

```json
{
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
          "required": ["signal", "why_it_matters", "recommended_action"]
        }
      }
    },
    "required": ["signals"]
  }
}
```

**Say:** "Structured output maps cleanly into Suggested Actions — Hermes skill can consume this via MCP."

---

## 6. Recommended live walkthrough (15 min)

| Min | Step | Action |
|-----|------|--------|
| 0–2 | Search | Query: `AMD data center Instinct MI350 earnings` · count=5 · freshness=year |
| 2–4 | Search + governance | Repeat with `include_domains=amd.com` — compare broader vs allowlist |
| 4–7 | Contents | Paste 1 URL from Search · show markdown |
| 7–12 | Research | Renewal or Outbound `input` · boost_domains amd.com · show content + sources |
| 12–13 | View Code | Flash curl for Search or Research |
| 13–15 | Bridge | Slides 8–9: MCP automates you-search → you-contents → you-research |

---

## 7. Response → brief mapping

| API output | Brief section |
|------------|----------------|
| Search titles, URLs, snippets | Current Signals (candidates) |
| Contents markdown | Claims verification |
| Research `output.content` | Snapshot, Signals, Why They Care, Actions |
| Research `output.sources` | Claims And Sources |
| Weak / missing citations | Review Notes |

---

## 8. Troubleshooting in the room

| Issue | Fix |
|-------|-----|
| 401 / auth error | Check API key in playground settings |
| Empty Search results | Broaden query; remove `include_domains` |
| Contents timeout | Try different URL; increase `crawl_timeout` |
| Research slow | Narrate; use `standard` not `deep` in playground |
| Finance 422 | Use `research_effort`: `deep` or `exhaustive` only |
| Network blocked | Workshop app `DEMO_MODE=true` for govern section only |

---

## 9. MCP tool mapping (bridge to Hermes)

| Playground step | MCP tool | Hermes moment |
|-----------------|----------|---------------|
| Search | `you-search` | Tool call visible on `/account-action-brief` |
| Contents | `you-contents` | After Search selects URLs |
| Research | `you-research` | Synthesis with citations |
| Finance (optional) | finance MCP tool | Public companies only |

**Server:** `https://api.you.com/mcp`

---

## Related docs

- `you-com-api-demo-video-runbook.md` — full curl scenes
- `walk_slides.py` / `SLIDE-PRESENTER-SCRIPT.md` — slide-by-slide say/do
- `FACILITATOR-60MIN.md` — timing
