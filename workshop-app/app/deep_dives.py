"""Contextual deep-dive content for the workshop UI."""

from __future__ import annotations

from typing import Any

# step id -> ordered list of deep-dive topic ids
STEP_DEEP_DIVES: dict[str, list[str]] = {
    "welcome": ["workflow_pattern", "hermes_automation_loop", "resources"],
    "choose-job": ["workflow_pattern"],
    "define-output": ["output_schema_guide"],
    "api-matrix": ["api_chain_overview", "api_mcp_setup", "resources"],
    "web-search": ["api_setup_env", "api_search_setup", "api_chain_overview", "hermes_automation_loop"],
    "inspect-sources": ["source_scoring"],
    "contents": ["api_contents_setup"],
    "research": ["api_research_setup"],
    "structured-research": ["api_structured_research"],
    "team-context": ["internal_context_rules"],
    "connector-map": ["connector_map", "draft_connectors"],
    "review-gates": ["review_gates"],
    "workflow-card": ["workflow_card_guide"],
    "hermes-package": ["hermes_automation_loop", "agent_build_e2e", "hermes_desktop_setup", "hermes_live_setup", "api_mcp_setup"],
    "test-three": ["quality_scorecard"],
    "pilot-plan": ["pilot_plan_guide"],
    "wrap-up": ["community_continuation", "resources"],
}

DEEP_DIVES: dict[str, dict[str, Any]] = {
    "workflow_pattern": {
        "title": "Workflow pattern",
        "intro": "Every reusable Hermes workflow follows the same shape — from one-off prompt to governed pilot.",
        "blocks": [
            {
                "type": "code",
                "label": "Generic pattern",
                "content": (
                    "Trigger → Inputs → Tools → Draft → Review → Reuse → Pilot\n\n"
                    "For /account-action-brief:\n"
                    "User asks for an account brief\n"
                    "→ Hermes collects inputs\n"
                    "→ You.com gathers web sources (Search → Contents → Research)\n"
                    "→ Hermes drafts the six-section brief\n"
                    "→ Human inspects sources and sets review status\n"
                    "→ Hermes packages as a reusable skill + workflow card\n"
                    "→ Team pilots for two weeks"
                ),
            },
        ],
    },
    "hermes_automation_loop": {
        "title": "How Hermes automates the account brief",
        "intro": (
            "This app runs You.com APIs manually so you see each step. Your Hermes agent runs the same "
            "chain automatically when you trigger /account-action-brief — then you review the Draft."
        ),
        "blocks": [
            {
                "type": "list",
                "items": [
                    "1. You trigger — /account-action-brief + company name",
                    "2. Hermes orchestrates — You.com Search → Contents → Research via MCP",
                    "3. Evidence → brief — six sections formatted every run",
                    "4. Human reviews — Draft by default; no auto-send or CRM write",
                ],
            },
            {
                "type": "text",
                "content": (
                    "Hermes automates: API chain, source selection, synthesis, schema formatting, connector rules. "
                    "You still do: trigger, review claims/sources, approve gates, send drafts."
                ),
            },
            {
                "type": "code",
                "label": "Before vs after",
                "content": (
                    "Manual: search tabs → copy snippets → format doc → hope sources are current\n\n"
                    "Automated: /account-action-brief Acme Corp → Hermes + You.com → Draft brief with URLs"
                ),
                "copy": False,
            },
            {
                "type": "code",
                "label": "Test command",
                "content": (
                    "/account-action-brief\n\n"
                    "company: AMD\n"
                    "website: https://www.amd.com"
                ),
                "copy": True,
            },
        ],
    },
    "output_schema_guide": {
        "title": "Why the output schema matters",
        "intro": "Hermes enforces the same six sections every run so outputs are comparable, inspectable, and mappable from API responses.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Snapshot — company identity and source confidence",
                    "Current Signals — sourced news, strategy, partnerships",
                    "Why This Account Might Care — priorities and triggers (may include assumptions)",
                    "Suggested Actions — next step, owner, angle",
                    "Claims And Sources — claim → URL → freshness (You.com evidence lands here)",
                    "Review Notes — weak claims, missing sources, external-use warnings",
                ],
            },
            {
                "type": "text",
                "content": (
                    "Rule: separate sourced facts (You.com) from recommendations and internal context (Hermes). "
                    "Structured Research output_schema maps directly into Suggested Actions fields."
                ),
            },
        ],
    },
    "api_chain_overview": {
        "title": "API chain — how to wire it",
        "intro": "The workshop app runs this chain for you. To build it yourself (or show attendees in terminal), follow this sequence.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "1. Web Search — discover candidate sources (results.web, results.news)",
                    "2. Filter — relevance, freshness, trust (Hermes or human)",
                    "3. Contents — read 1–3 high-value URLs as markdown",
                    "4. Research — multi-source synthesis with citations",
                    "5. Structured Research (optional) — predictable JSON via output_schema",
                    "6. Finance Research (optional) — public-company financial context",
                    "7. Map API outputs into the six-section brief schema",
                    "8. Human review — set gate before internal or external use",
                ],
            },
            {
                "type": "text",
                "content": (
                    "Show the API response shape, not just the final answer. "
                    "Attendees should see why the workflow is source-grounded."
                ),
            },
        ],
    },
    "api_setup_env": {
        "title": "API setup — environment",
        "intro": "One-time setup before running curl commands or live API calls.",
        "blocks": [
            {
                "type": "code",
                "label": "Get your key",
                "content": (
                    "# Get a key at https://you.com/settings/api\n"
                    "export YDC_API_KEY=\"your-key-here\"\n\n"
                    "# Workshop app: add to workshop-app/.env\n"
                    "YDC_API_KEY=your-key-here\n"
                    "DEMO_MODE=false"
                ),
                "copy": True,
            },
            {
                "type": "code",
                "label": "Start the workshop app (live mode)",
                "content": "cd workshop-app\n./run.sh\n# Open http://localhost:8080",
                "copy": True,
            },
        ],
    },
    "api_search_setup": {
        "title": "Web Search API — setup & curl",
        "intro": "Search discovers structured web and news results. Hermes uses this as step 1 — never asks the model to guess what's current.",
        "blocks": [
            {
                "type": "code",
                "label": "Basic search",
                "content": (
                    'curl -G https://ydc-index.io/v1/search \\\n'
                    '  -H "X-API-Key: $YDC_API_KEY" \\\n'
                    '  --data-urlencode "query=AMD recent AI data center Instinct MI350 earnings partnerships" \\\n'
                    "  -d count=5 \\\n"
                    "  -d freshness=year"
                ),
                "copy": True,
            },
            {
                "type": "code",
                "label": "Trusted-domain search (governance)",
                "content": (
                    'curl -G https://ydc-index.io/v1/search \\\n'
                    '  -H "X-API-Key: $YDC_API_KEY" \\\n'
                    '  --data-urlencode "query=AMD AI data center Instinct EPYC investor product strategy" \\\n'
                    "  -d count=5 \\\n"
                    '  --data-urlencode "include_domains=amd.com"'
                ),
                "copy": True,
            },
            {
                "type": "list",
                "items": [
                    "Inspect results.web and results.news separately",
                    "Each item: title, url, description/snippets, page_age",
                    "include_domains / exclude_domains / boost_domains = source policy",
                    "freshness, country, language are workflow controls",
                ],
            },
        ],
    },
    "api_contents_setup": {
        "title": "Contents API — setup & curl",
        "intro": "Contents reads specific URLs as clean markdown. Use after Search — not instead of it.",
        "blocks": [
            {
                "type": "code",
                "label": "Read selected URLs",
                "content": (
                    'curl -X POST https://ydc-index.io/v1/contents \\\n'
                    '  -H "X-API-Key: $YDC_API_KEY" \\\n'
                    '  -H "Content-Type: application/json" \\\n'
                    "  -d '{\n"
                    '    "urls": [\n'
                    '      "https://www.amd.com/en/newsroom/press-releases/2025-06-12-amd-expands-instinct-mi350-series.html"\n'
                    "    ],\n"
                    '    "formats": ["markdown", "metadata"],\n'
                    '    "crawl_timeout": 15,\n'
                    '    "max_age": 86400\n'
                    "  }'"
                ),
                "copy": True,
            },
            {
                "type": "list",
                "items": [
                    "Takes URLs, not a search query",
                    "Returns url, title, markdown, metadata per page",
                    "max_age controls cache freshness",
                    "Live API may return a JSON array — normalize to {results: [...]} in your code",
                ],
            },
        ],
    },
    "api_research_setup": {
        "title": "Research API — setup & curl",
        "intro": "Research runs multi-step synthesis with citations. Use when the workflow needs an answer, not just raw search hits.",
        "blocks": [
            {
                "type": "code",
                "label": "Standard research",
                "content": (
                    'curl -X POST https://api.you.com/v1/research \\\n'
                    '  -H "X-API-Key: $YDC_API_KEY" \\\n'
                    '  -H "Content-Type: application/json" \\\n'
                    "  -d '{\n"
                    '    "input": "What are the most important recent strategic signals for AMD, and what should an account team consider before a customer conversation?",\n'
                    '    "research_effort": "standard",\n'
                    '    "source_control": {\n'
                    '      "freshness": "year",\n'
                    '      "boost_domains": ["amd.com"]\n'
                    "    }\n"
                    "  }'"
                ),
                "copy": True,
            },
            {
                "type": "list",
                "items": [
                    "Show output.content and output.sources in the response",
                    "research_effort: lite / standard / deep / exhaustive",
                    "source_control guides domains, freshness, geography",
                    "Map sources into Claims And Sources in the brief",
                ],
            },
        ],
    },
    "api_structured_research": {
        "title": "Structured Research — output_schema",
        "intro": "Add output_schema when you need predictable fields for CRM drafts, workflow cards, or review checklists.",
        "blocks": [
            {
                "type": "text",
                "content": (
                    "The workshop app sends a schema with signals[].signal, why_it_matters, and recommended_action. "
                    "Hermes maps these fields directly into Suggested Actions without manual reformatting."
                ),
            },
            {
                "type": "list",
                "items": [
                    "Same Research endpoint — add output_schema to the JSON body",
                    "content may be JSON (object) instead of plain text",
                    "Sources still appear in output.sources",
                    "Use for operational handoff, not just narrative synthesis",
                ],
            },
        ],
    },
    "api_mcp_setup": {
        "title": "You.com MCP — agent setup",
        "intro": "Expose Search, Contents, and Research to Hermes without custom integration code.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Add You.com MCP server in Hermes: https://api.you.com/mcp",
                    "Enable tools: you-search, you-contents, you-research",
                    "Optional: finance research tool for public-company context",
                    "Restrict to only the tools this workflow needs (principle of least privilege)",
                ],
            },
            {
                "type": "text",
                "content": (
                    "MCP is the production path: Hermes calls You.com automatically during /account-action-brief. "
                    "If MCP isn't wired in the room, paste the Evidence Bundle from the Hermes Live step."
                ),
            },
            {
                "type": "links",
                "items": [
                    {
                        "label": "You.com MCP docs",
                        "url": "https://you.com/docs/capabilities/mcp-server-for-web-search",
                    },
                ],
            },
        ],
    },
    "source_scoring": {
        "title": "Source scoring — full guide",
        "intro": "You.com provides evidence; humans and Hermes decide what enters the brief.",
        "blocks": [
            {
                "type": "table",
                "headers": ["Score", "Meaning", "Action"],
                "rows": [
                    ["3", "Strong — official, recent, direct", "Keep in main brief"],
                    ["2", "Usable — credible but indirect", "Keep in main brief"],
                    ["1", "Weak — old, vague, secondhand", "Move to Review Notes"],
                    ["0", "Do not use", "Remove"],
                ],
            },
            {
                "type": "list",
                "items": [
                    "Require: 1 official source, 1 news source, 1 product/investor source",
                    "Avoid: unsourced listicles, stale pages, unclear authorship",
                    "Score 0–1 before trusting any claim in Suggested Actions",
                ],
            },
        ],
    },
    "internal_context_rules": {
        "title": "Internal context rules",
        "intro": "Hermes orchestrates CRM, docs, and notes alongside You.com public evidence.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Internal context is private — never cited as public proof",
                    "Keep public-source claims and internal observations in separate sections",
                    "Do not create external messaging from private info without approval",
                    "Start read-only — no auto-writeback until the pilot proves quality",
                ],
            },
        ],
    },
    "connector_map": {
        "title": "Connector map — full guide",
        "intro": (
            "Lists every tool the workflow may touch and how it is allowed to touch it. "
            "You.com is always read-only; GTM tools are draft-only in the first pilot."
        ),
        "blocks": [
            {
                "type": "table",
                "headers": ["Bucket", "Rule", "Examples"],
                "rows": [
                    ["Read-only", "Fetch only — no writes, no sends", "You.com Search/Contents/Research, CRM read, docs"],
                    ["Draft-only", "Prepare output — human sends", "Email draft, Slack review, CRM update draft"],
                    ["Blocked", "Refuse even if asked", "PII, sensitive data, auto-send, unapproved legal language"],
                ],
            },
            {
                "type": "code",
                "label": "Full template (copy for your team)",
                "content": (
                    "Workflow name: /account-action-brief\n"
                    "Primary user: [ROLE]\n"
                    "Workflow owner: [PERSON OR TEAM]\n\n"
                    "Read-only tools:\n"
                    "- You.com Search, Contents, Research\n"
                    "- CRM (read-only)\n"
                    "- Docs, notes, support (read-only)\n\n"
                    "Draft-only tools:\n"
                    "- Email draft\n"
                    "- Slack or Teams review request\n"
                    "- CRM update draft\n"
                    "- Meeting brief\n\n"
                    "Write-enabled tools:\n"
                    "- None for pilot, unless explicitly approved\n\n"
                    "Blocked tools or data:\n"
                    "- Sensitive customer data\n"
                    "- Unapproved legal/compliance language\n"
                    "- Personal data not needed for the workflow\n"
                    "- Auto-send outreach\n"
                    "- Auto-update CRM"
                ),
                "copy": True,
            },
            {
                "type": "code",
                "label": "Recommended first pilot",
                "content": (
                    "Read from public web (You.com) + approved internal context.\n"
                    "Draft review messages and CRM updates — human sends.\n"
                    "Do NOT auto-send outreach or auto-update CRM.\n"
                    "Require Approved for external use before customer-facing language."
                ),
                "copy": True,
            },
        ],
    },
    "draft_connectors": {
        "title": "Draft-only connector examples",
        "intro": "Sample outputs above show what draft-only means in practice — nothing sends until a human approves.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Slack review request — asks teammates to check claims before internal use",
                    "CRM update draft — prepared fields, not auto-saved to CRM",
                    "Outreach draft — blocked until Approved for external use",
                    "Connector map + review gates work together: tools define what can run; gates define when output is safe",
                ],
            },
        ],
    },
    "review_gates": {
        "title": "Review gates — full guide",
        "intro": "Four states make the workflow usable without making it reckless.",
        "blocks": [
            {
                "type": "table",
                "headers": ["State", "Meaning"],
                "rows": [
                    ["Draft", "Output exists; no human has reviewed it"],
                    ["Needs edits", "Unsupported claims, weak sources, tone issues, or missing context"],
                    ["Approved for internal use", "Safe for meeting prep and internal discussion"],
                    ["Approved for external use", "Safe for outreach, customer comms, or public-facing use"],
                ],
            },
            {
                "type": "code",
                "label": "Review checklist (run on every brief)",
                "content": (
                    "Review this account action brief.\n\n"
                    "Check:\n"
                    "- Are all factual claims source-backed?\n"
                    "- Are sources recent enough?\n"
                    "- Are recommendations separated from facts?\n"
                    "- Are internal-only details clearly marked?\n"
                    "- Are there claims that should not be used externally?\n"
                    "- Is the suggested next action reasonable?\n\n"
                    "Return:\n"
                    "- Status: Draft | Needs edits | Approved for internal | Approved for external\n"
                    "- Required edits\n"
                    "- Weak or missing sources\n"
                    "- External-use concerns\n"
                    "- Final reviewer notes"
                ),
                "copy": True,
            },
        ],
    },
    "workflow_card_guide": {
        "title": "Workflow card — what it captures",
        "intro": "The handoff between 'this prompt worked once' and 'our team can run this repeatedly.'",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Workflow name, purpose, primary user, owner, trigger",
                    "Required and optional inputs",
                    "Allowed tools (from connector map) and blocked data",
                    "Output format (six-section schema)",
                    "Review rules and success metrics",
                    "Two-week pilot plan outline",
                ],
            },
            {
                "type": "text",
                "content": "Generate the card from this app, then download — it includes your connector map and session inputs.",
            },
        ],
    },
    "agent_build_e2e": {
        "title": "End-to-end agent build (attendee path)",
        "intro": (
            "Goal: leave with a working /account-action-brief skill in Hermes — not just prompts and cards. "
            "Hermes desktop users: install the skill pack (fastest). Studio users: follow Agent Build Lab (~15–20 min)."
        ),
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Desktop path: install skill pack → wire MCP → test /account-action-brief",
                    "Studio path: create skill → paste prompt → wire MCP → govern → test",
                    "Minimum success: six sections, source URLs, Draft status",
                ],
            },
            {
                "type": "text",
                "content": (
                    "See HERMES-DESKTOP-SETUP.md for install.sh and zip download. "
                    "No MCP? Use Evidence Bundle + test command as workshop fallback."
                ),
            },
        ],
    },
    "hermes_desktop_setup": {
        "title": "Hermes Desktop skill pack",
        "intro": (
            "Four installable SKILL.md files for Hermes Agent: /account-action-brief, /meeting-prep, /community-pulse, "
            "/workshop-60min. Faster than manual skill authoring in Workflow Studio."
        ),
        "blocks": [
            {
                "type": "code",
                "label": "Install (from workshop package)",
                "content": (
                    "cd workshop-app/hermes-desktop\n"
                    "chmod +x install.sh\n"
                    "./install.sh"
                ),
                "copy": True,
            },
            {
                "type": "list",
                "items": [
                    "Skills install to ~/.hermes/skills/",
                    "Wire You.com MCP: https://api.you.com/mcp",
                    "Enable: you-search, you-contents, you-research",
                    "Restart Hermes if skills do not appear",
                ],
            },
            {
                "type": "text",
                "content": (
                    "Download personalized zip from Agent Build Lab — includes workshop-session.md "
                    "with your company and connector map."
                ),
            },
        ],
    },
    "hermes_live_setup": {
        "title": "Facilitator pre-stage (optional demo-only track)",
        "intro": "For demo-only sessions where attendees watch rather than build. Attendees building hands-on should use Agent Build Lab instead.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "1. Create skill /account-action-brief in Hermes Workflow Studio",
                    "2. Paste the Hermes Packaging Prompt from this app as the skill instruction",
                    "3. Set inputs: company_name (required), company_url (optional)",
                    "4. Wire You.com MCP (https://api.you.com/mcp) or API keys in Hermes",
                    "5. Test run with AMD before attendees arrive",
                    "6. Room: workshop app on display 1, Hermes on display 2",
                ],
            },
            {
                "type": "code",
                "label": "Test run command",
                "content": (
                    "/account-action-brief\n\n"
                    "company: AMD\n"
                    "website: https://www.amd.com"
                ),
                "copy": True,
            },
            {
                "type": "text",
                "content": (
                    "Fallback without MCP: Run Full Demo Chain here, then Copy Evidence Bundle into Hermes. "
                    "Say: 'In production, Hermes calls You.com via MCP — we're pasting evidence today because of [reason].'"
                ),
            },
        ],
    },
    "quality_scorecard": {
        "title": "Quality scorecard",
        "intro": "Score each dimension 0–3 during the three-account test. Pilot only when averages are 2+.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Source quality — are claims backed by strong, recent sources?",
                    "Relevance — does the brief match the account and meeting context?",
                    "Actionability — are suggested next steps specific and reasonable?",
                    "Governance — are review rules followed; internal vs external separated?",
                    "Time saved — is the workflow faster than the manual process?",
                ],
            },
        ],
    },
    "pilot_plan_guide": {
        "title": "Team rollout plan (champions only)",
        "intro": (
            "Optional — for attendees who will pitch a small team pilot to their manager. "
            "Not required for most people. Default path: join community, finish your agent, run 3 briefs. "
            "Use this template after Week 1 when you have evidence the workflow works for you personally."
        ),
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Who it's for: RevOps, enablement, or GTM leads — not every workshop attendee",
                    "When: Week 2+ after you've run 3 briefs and joined the community",
                    "What: 5 users, 20 accounts, 2 weeks — measured rollout with scorecard",
                    "Week 0: owner, review rules, allowed tools, feedback form",
                    "Week 1: ~10 briefs, every one human-reviewed",
                    "Week 2: ~20 briefs; track time saved, source quality, briefs used in real work",
                    "Expand when quality scores average 2+ and unsupported claims stop recurring",
                ],
            },
            {
                "type": "text",
                "content": (
                    "Download the pre-filled template from Download All (pilot-plan.md). "
                    "Full track step 16 has the editable form. Facilitators: do not make the room fill this in — "
                    "it does not drive signups; community + agent build do."
                ),
            },
        ],
    },
    "resources": {
        "title": "Package resources (full depth)",
        "intro": "This app summarizes key concepts. These files in the workshop package have the full written depth.",
        "blocks": [
            {
                "type": "links",
                "items": [
                    {"label": "Full tutorial (17 steps + API path)", "path": "audience-workflow-building-tutorial.md"},
                    {"label": "API demo video runbook (curl scripts)", "path": "you-com-api-demo-video-runbook.md"},
                    {"label": "Agent build guide (hands-on)", "path": "workshop-app/AGENT-BUILD-GUIDE.md"},
                    {"label": "Hermes live setup (facilitator demo-only)", "path": "workshop-app/HERMES-LIVE-SETUP.md"},
                    {"label": "50-min facilitator script", "path": "workshop-app/FACILITATOR-50MIN.md"},
                    {"label": "90-min facilitator script", "path": "workshop-app/FACILITATOR.md"},
                    {"label": "Attendee handout", "path": "workshop-app/materials/attendee-handout.md"},
                    {"label": "Integration blueprint", "path": "flagship-account-workflow-integration-blueprint.md"},
                ],
            },
            {
                "type": "links",
                "items": [
                    {"label": "You.com API docs", "url": "https://you.com/docs/welcome"},
                    {"label": "You.com MCP docs", "url": "https://you.com/docs/capabilities/mcp-server-for-web-search"},
                ],
            },
        ],
    },
    "calendar_meeting_prep": {
        "title": "Calendar integration — briefs before meetings",
        "intro": (
            "Natural next step after /account-action-brief works manually: read your calendar (read-only), "
            "detect customer meetings, run the same You.com chain, deliver a Draft brief before the call."
        ),
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Read-only: Google Calendar / Outlook — upcoming events",
                    "Trigger: 24h before, 2h before, or daily digest of tomorrow's meetings",
                    "Hermes extracts company → runs /account-action-brief → You.com MCP",
                    "Draft-only delivery: Slack DM, email-to-self, prep doc — not to attendees",
                    "Blocked: auto-edit invites, auto-email customers, auto-CRM-write",
                ],
            },
            {
                "type": "text",
                "content": (
                    "Full pattern: workshop-app/CALENDAR-MEETING-PREP.md. "
                    "Skill: /meeting-prep in desktop pack (install.sh). "
                    "Week 2+ after 3 manual briefs."
                ),
            },
        ],
    },
    "community_continuation": {
        "title": "Community continuation — API + Hermes after the workshop",
        "intro": (
            "The workshop is day one. The community is where members keep calling You.com APIs "
            "and running their Hermes agent — with weekly challenges and facilitator pulses."
        ),
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Join You.com Discord: https://discord.gg/2C4WgryxSD",
                    "Introduce yourself in #introductions — say you joined from the Account Action Brief workshop",
                    "Shared Hermes org (optional): publish /account-action-brief + /community-pulse skill pack",
                    "API: BYOK (own YDC_API_KEY) or org MCP or workshop credit pool",
                    "Facilitators run /community-pulse weekly → post digest to Discord",
                    "Members run /account-action-brief; share learnings in the server",
                ],
            },
            {
                "type": "text",
                "content": (
                    "Hermes messaging model: facilitators don't DM from Hermes — they run a broadcast skill, "
                    "copy the sourced pulse, and post to the community. Members reply in chat and run their own agents."
                ),
            },
        ],
    },
    "post_event_learning": {
        "title": "Self-paced depth (optional)",
        "intro": (
            "The 60-minute workshop is complete in the room. For extra practice, use the full 18-step track "
            "and reference docs — not required for attendees."
        ),
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Full 18-step replay → app ?full=1",
                    "API curl setup → you-com-api-demo-video-runbook.md",
                    "Agent reference → AGENT-BUILD-GUIDE.md",
                    "Community → COMMUNITY-CONTINUATION.md (Discord)",
                ],
            },
        ],
    },
    "next_steps": {
        "title": "After the workshop",
        "intro": "One step: join the You.com Discord and introduce yourself.",
        "blocks": [
            {
                "type": "list",
                "items": [
                    "Join https://discord.gg/2C4WgryxSD",
                    "Post in #introductions — say you joined from the Account Action Brief workshop",
                    "Keep using /account-action-brief on your accounts",
                ],
            },
        ],
    },
}


def get_deep_dives_payload() -> dict[str, Any]:
    return {
        "dives": DEEP_DIVES,
        "step_map": STEP_DEEP_DIVES,
    }
