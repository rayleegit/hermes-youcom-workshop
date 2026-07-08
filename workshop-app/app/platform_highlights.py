"""Platform value props and teaching aids for You.com and Hermes."""

from __future__ import annotations

from typing import Any

YOU_COM_STRENGTHS: list[dict[str, str]] = [
    {
        "title": "Live web intelligence",
        "detail": "Real-time Search, Contents, and Research APIs — not stale training data.",
    },
    {
        "title": "Structured JSON for agents",
        "detail": "LLM-ready snippets, metadata, freshness signals, and URLs in one response.",
    },
    {
        "title": "Source-grounded synthesis",
        "detail": "Research returns cited answers with output.content and output.sources.",
    },
    {
        "title": "Governance at retrieval",
        "detail": "Domain allowlists, freshness filters, boost/exclude controls, and livecrawl.",
    },
    {
        "title": "MCP for zero-code integration",
        "detail": "Agents call you-search, you-contents, and you-research without custom wiring.",
    },
    {
        "title": "Finance Research add-on",
        "detail": "Finance-optimized index for earnings, filings, and market context.",
    },
]

HERMES_STRENGTHS: list[dict[str, str]] = [
    {
        "title": "Beyond one-off prompts",
        "detail": "Turn a useful AI task into a named, reusable workflow your team can run again.",
    },
    {
        "title": "Full workflow lifecycle",
        "detail": "Run → Integrate → Govern → Package → Pilot — not just chat.",
    },
    {
        "title": "Tool orchestration",
        "detail": "Coordinate You.com, CRM, docs, Slack, and outreach in one governed flow.",
    },
    {
        "title": "Reusable skills & playbooks",
        "detail": "Package /account-action-brief with inputs, tools, output schema, and review rules.",
    },
    {
        "title": "Admin governance",
        "detail": "Define allowed tools, blocked data, roles, and approval gates per workflow.",
    },
    {
        "title": "Production pilot readiness",
        "detail": "Workflow cards, connector maps, scorecards, and two-week rollout plans.",
    },
]

API_DECISION_MATRIX: list[dict[str, str]] = [
    {
        "need": "Discover candidate sources",
        "api": "Web Search API",
        "why": "Structured web + news results with snippets, URLs, and freshness metadata.",
    },
    {
        "need": "Read full page text from known URLs",
        "api": "Contents API",
        "why": "Clean markdown/HTML from specific pages for source inspection.",
    },
    {
        "need": "Multi-source synthesis with citations",
        "api": "Research API",
        "why": "Searches, reads, and reasons across sources — returns content + sources.",
    },
    {
        "need": "Public-company financial context",
        "api": "Finance Research API",
        "why": "Finance-optimized index for earnings, filings, and market signals.",
    },
    {
        "need": "Agent tool access without integration code",
        "api": "You.com MCP Server",
        "why": "Expose search, contents, and research tools to Hermes or any MCP agent.",
    },
]

HERMES_LIFECYCLE: list[dict[str, str]] = [
    {"stage": "Run", "detail": "Execute the workflow with defined inputs and source requirements."},
    {"stage": "Integrate", "detail": "Connect You.com APIs, CRM, docs, and team context as read-only tools."},
    {"stage": "Govern", "detail": "Set allowed/blocked tools, review gates, roles, and data boundaries."},
    {"stage": "Package", "detail": "Save as a reusable Hermes skill or playbook with a workflow card."},
    {"stage": "Pilot", "detail": "Run a measured two-week pilot with quality scorecards and feedback."},
]

YOU_COM_PRODUCTS: list[dict[str, str]] = [
    {
        "id": "search",
        "name": "Web Search API",
        "job": "Discover candidate sources as structured JSON (web + news, snippets, freshness).",
        "where": "Platform playground → Search endpoint (you.com/platform)",
    },
    {
        "id": "contents",
        "name": "Contents API",
        "job": "Read selected URLs as clean markdown for page-level claim verification.",
        "where": "Platform playground → Contents endpoint",
    },
    {
        "id": "research",
        "name": "Research API",
        "job": "Multi-source synthesis with citations (output.content + output.sources).",
        "where": "Platform playground → Research endpoint",
    },
    {
        "id": "structured",
        "name": "Structured Research (output_schema)",
        "job": "Predictable JSON fields for CRM, workflow cards, and Suggested Actions.",
        "where": "Optional — playground or app ?full=1",
    },
    {
        "id": "finance",
        "name": "Finance Research API",
        "job": "Finance-optimized index for earnings, filings, and market context (public companies).",
        "where": "Optional — playground if time allows (2–5 min)",
    },
    {
        "id": "mcp",
        "name": "You.com MCP Server",
        "job": "Expose search, contents, and research to Hermes/agents without custom integration code.",
        "where": "Live Hermes setup — wire MCP in Agent Build Lab",
    },
]

WORKSHOP_STORY = {
    "headline": "You.com provides the evidence. Hermes provides the workflow.",
    "youcom_role": (
        "You.com is the live intelligence layer — structured retrieval, source reading, "
        "cited synthesis, and governance controls at the API level."
    ),
    "hermes_role": (
        "Hermes is the workflow layer — it orchestrates tools, enforces review rules, "
        "packages the prompt as a reusable skill, and gets teams to production pilot."
    ),
    "together": (
        "Together they replace 'ask AI and hope' with a source-grounded, governed, "
        "repeatable process any team can run, review, and pilot."
    ),
}

PHASE_PLATFORM_FOCUS: dict[str, dict[str, Any]] = {
    "Setup": {
        "focus": "both",
        "youcom": "Four API modes + MCP give agents real-time, cited web intelligence.",
        "hermes": "Hermes Workflow Studio turns repeated tasks into governed, reusable workflows.",
    },
    "Define": {
        "focus": "hermes",
        "youcom": "You.com APIs will supply the evidence once inputs are defined.",
        "hermes": "Named workflows with stable inputs and output schemas are governable and reusable.",
    },
    "Discover": {
        "focus": "youcom",
        "youcom": "Search API returns structured JSON — titles, URLs, snippets, freshness.",
        "hermes": "Hermes calls Search as step 1 of the orchestrated evidence chain.",
    },
    "Inspect": {
        "focus": "youcom",
        "youcom": "Contents API reads selected URLs as clean markdown for claim verification.",
        "hermes": "Hermes enforces the source inspection habit before claims enter the brief.",
    },
    "Synthesize": {
        "focus": "youcom",
        "youcom": "Research API synthesizes across sources with citations and structured output.",
        "hermes": "Hermes maps Research output into the brief schema and Claims & Sources section.",
    },
    "Context": {
        "focus": "hermes",
        "youcom": "Public evidence stays separate from private team context.",
        "hermes": "Hermes orchestrates CRM, docs, and notes as read-only context connectors.",
    },
    "Govern": {
        "focus": "hermes",
        "youcom": "API source controls (domains, freshness) complement workflow-level governance.",
        "hermes": "Hermes defines roles, review gates, allowed/blocked tools, and approval states.",
    },
    "Package": {
        "focus": "hermes",
        "youcom": "API evidence feeds into the packaged workflow card.",
        "hermes": "Hermes skills/playbooks make /account-action-brief repeatable across the team.",
    },
    "Pilot": {
        "focus": "both",
        "youcom": "Source quality and citation support are pilot success metrics.",
        "hermes": "Workflow owner, scorecards, and rollout plan make the pilot measurable.",
    },
    "Close": {
        "focus": "both",
        "youcom": "You.com = live, source-grounded intelligence at scale.",
        "hermes": "Hermes = governed, reusable workflows your team can actually ship.",
    },
}

REVIEW_STATES = [
    {
        "state": "Draft",
        "detail": "Output produced, no human review yet.",
        "hermes_note": "Default state for every workflow run.",
    },
    {
        "state": "Needs edits",
        "detail": "Unsupported claims, weak sources, or tone issues found.",
        "hermes_note": "Hermes routes back to the runner with required edits.",
    },
    {
        "state": "Approved for internal use",
        "detail": "Safe for planning, meeting prep, and internal discussion.",
        "hermes_note": "Hermes records reviewer and approval timestamp.",
    },
    {
        "state": "Approved for external use",
        "detail": "Claims, sources, and wording verified for outreach or customer comms.",
        "hermes_note": "Hermes blocks external drafts until this gate is passed.",
    },
]

QUALITY_SCORECARD: list[dict[str, str]] = [
    {"dimension": "Correctness", "scale": "0=wrong, 1=questionable, 2=mostly correct, 3=correct"},
    {"dimension": "Citation support", "scale": "0=no sources, 1=weak, 2=most key claims sourced, 3=all key claims sourced"},
    {"dimension": "Freshness", "scale": "0=stale, 1=some current, 2=mostly current, 3=clearly current"},
    {"dimension": "Usefulness", "scale": "0=not actionable, 1=some context, 2=useful with edits, 3=clear next action"},
    {"dimension": "Review burden", "scale": "0=too much cleanup, 1=heavy edits, 2=light edits, 3=ready after quick review"},
]
