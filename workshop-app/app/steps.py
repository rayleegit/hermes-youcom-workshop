"""Workshop step definitions aligned with audience-workflow-building-tutorial.md."""

from __future__ import annotations

from typing import Any

WORKSHOP_STEPS: list[dict[str, Any]] = [
    {
        "id": "welcome",
        "number": 0,
        "title": "Welcome — Two Platforms, One Workflow",
        "phase": "Setup",
        "minutes": 5,
        "platform_focus": "both",
        "facilitator": (
            "Open with the dual story: You.com provides live, source-grounded web intelligence. "
            "Hermes turns that intelligence into a governed, reusable workflow. "
            "This is not a chatbot demo — it is an evidence chain plus a workflow layer."
        ),
        "audience_action": "Read the Platform Spotlight panel. Note which features belong to You.com vs Hermes.",
        "youcom_highlight": "Real-time Search, Contents, Research, and MCP — structured evidence, not guesses.",
        "hermes_highlight": "Workflow Studio lifecycle: run, integrate, govern, package, and pilot.",
        "talking_points": [
            "You.com = live intelligence layer (discover, read, synthesize with citations)",
            "Hermes = workflow layer (orchestrate tools, govern access, package for reuse)",
            "Today in the app: You.com runs manually. In Hermes: same chain automates on /account-action-brief",
            "Together: source-grounded briefs your team can run, review, and reuse — not one-off prompts",
            "Flagship workflow: /account-action-brief · Demo company: AMD",
        ],
        "api_action": None,
    },
    {
        "id": "choose-job",
        "number": 1,
        "title": "Choose The Job",
        "phase": "Define",
        "minutes": 5,
        "platform_focus": "hermes",
        "facilitator": (
            "Hermes workflows start with a real job-to-be-done, not a clever prompt. "
            "Ask attendees: When I am [situation], I need [output], so I can [action]."
        ),
        "audience_action": "Fill in the workflow job sentence for your team.",
        "youcom_highlight": "You.com will supply the live evidence once the job is defined.",
        "hermes_highlight": "Named workflows (/account-action-brief) make repeated work repeatable and governable.",
        "talking_points": [
            "Hermes turns 'this prompt worked once' into a workflow your whole team can run",
            "Start with a job your team already does manually — account briefs, renewal prep, partner calls",
            "Avoid workflows needing private data or automatic writeback on day one",
        ],
        "api_action": None,
    },
    {
        "id": "define-inputs",
        "number": 2,
        "title": "Define Workflow Inputs",
        "phase": "Define",
        "minutes": 5,
        "platform_focus": "hermes",
        "facilitator": (
            "Hermes workflows need explicit inputs — required and optional — so admins know "
            "what data the workflow consumes and connectors know what to fetch."
        ),
        "audience_action": "Enter company name and brief goal — goal tailors You.com queries.",
        "youcom_highlight": "Company + brief goal become the Search and Research query seed.",
        "hermes_highlight": "Hermes collects required inputs before calling any tool — smallest useful set wins.",
        "talking_points": [
            "Hermes: company_name required; workflow_goal, website, segment optional",
            "You.com: company + goal drive Search queries and Research questions",
            "Stable inputs = predictable outputs = governable workflows",
        ],
        "api_action": None,
    },
    {
        "id": "define-output",
        "number": 3,
        "title": "Define Output Schema",
        "phase": "Define",
        "minutes": 5,
        "platform_focus": "hermes",
        "facilitator": (
            "Hermes enforces a stable six-section output format. This is what makes outputs "
            "comparable across accounts, inspectable by admins, and mappable from API responses."
        ),
        "audience_action": "Review the output schema preview — every brief follows this structure.",
        "youcom_highlight": "Research structured output_schema maps directly into Suggested Actions fields.",
        "hermes_highlight": "Hermes reuses the same output schema on every run — no format drift.",
        "talking_points": [
            "Hermes: Snapshot → Signals → Why They Care → Actions → Claims & Sources → Review Notes",
            "You.com: structured Research JSON fills predictable fields in the schema",
            "Separate sourced facts (You.com evidence) from recommendations (Hermes output rules)",
        ],
        "api_action": None,
    },
    {
        "id": "api-matrix",
        "number": 4,
        "title": "API Decision Matrix",
        "phase": "Discover",
        "minutes": 5,
        "platform_focus": "youcom",
        "facilitator": (
            "Before running APIs, teach the decision rule: each You.com API has one job. "
            "Search discovers, Contents reads, Research synthesizes, Finance Research adds financial context, "
            "MCP exposes all three to Hermes without custom integration code."
        ),
        "audience_action": "Review the API Decision Matrix. Match each need to the right You.com API.",
        "youcom_highlight": "Five modes: Search, Contents, Research, Finance Research, MCP — each with a distinct job.",
        "hermes_highlight": "Hermes orchestrates the chain: Search → filter → Contents → Research → brief.",
        "talking_points": [
            "You.com: 'I need sources' → Search · 'I have URLs' → Contents · 'I need synthesis' → Research",
            "You.com MCP: agents call web tools without writing integration code",
            "Hermes decides when to call each API based on workflow rules, not model improvisation",
        ],
        "api_action": None,
    },
    {
        "id": "web-search",
        "number": 5,
        "title": "Web Search API — Discover Sources",
        "phase": "Discover",
        "minutes": 10,
        "platform_focus": "youcom",
        "facilitator": (
            "Run Search live. Highlight You.com's structured JSON: results.web, titles, URLs, "
            "snippets, page_age. Show governance levers: include_domains, freshness, livecrawl. "
            "Then note: Hermes calls this as step 1 of the orchestrated chain."
        ),
        "audience_action": 'Click "Run Web Search" and inspect structured JSON. Try the domain-filtered search.',
        "youcom_highlight": "Structured web + news JSON with LLM-ready snippets and freshness metadata.",
        "hermes_highlight": "Hermes uses Search results as candidate sources — never asks the model to guess what's current.",
        "talking_points": [
            "You.com: snippets are already RAG context before fetching full pages",
            "You.com: include_domains, exclude_domains, freshness = governance at retrieval time",
            "Hermes: filters Search results by relevance, trust, and freshness before Contents",
        ],
        "api_action": "search",
    },
    {
        "id": "inspect-sources",
        "number": 6,
        "title": "Inspect & Score Sources",
        "phase": "Inspect",
        "minutes": 8,
        "platform_focus": "both",
        "facilitator": (
            "Teach the source inspection habit: You.com provides the evidence, "
            "but Hermes (and the human reviewer) decide which claims are allowed. "
            "Score 3=strong, 2=usable, 1=weak, 0=do not use."
        ),
        "audience_action": "Score each search result. Select URLs to read with Contents.",
        "youcom_highlight": "You.com returns the evidence — titles, URLs, snippets, dates.",
        "hermes_highlight": "Hermes enforces source policy: keep 2–3 in the brief, move 1 to Review Notes, drop 0.",
        "talking_points": [
            "You.com gives data; Hermes and humans give judgment",
            "Require: 1 official source, 1 news source, 1 product/investor source",
            "This habit is what separates a governed workflow from a confident-sounding guess",
        ],
        "api_action": None,
    },
    {
        "id": "contents",
        "number": 7,
        "title": "Contents API — Read Selected URLs",
        "phase": "Inspect",
        "minutes": 8,
        "platform_focus": "youcom",
        "facilitator": (
            "Run Contents on 1–3 URLs from Search. Show clean markdown and metadata. "
            "You.com reads pages; Hermes decides which page-level claims enter the brief."
        ),
        "audience_action": 'Click "Run Contents" on your selected URLs.',
        "youcom_highlight": "Clean markdown/HTML from specific URLs — page-level claim verification.",
        "hermes_highlight": "Hermes calls Contents only for high-value URLs the workflow trusts.",
        "talking_points": [
            "You.com: Contents takes URLs, not queries — max_age controls cache freshness",
            "You.com: response includes title, markdown, and metadata for source inspection",
            "Hermes: quotes or summarizes from page content, not just snippets",
        ],
        "api_action": "contents",
    },
    {
        "id": "research",
        "number": 8,
        "title": "Research API — Synthesize With Citations",
        "phase": "Synthesize",
        "minutes": 10,
        "platform_focus": "youcom",
        "facilitator": (
            "Run Research for multi-source synthesis. Show output.content and output.sources. "
            "Highlight research_effort and source_control. "
            "Hermes maps this into the brief's Claims & Sources section."
        ),
        "audience_action": 'Click "Run Research" and map sources into Claims & Sources.',
        "youcom_highlight": "Multi-source reasoning with inline citations — output.content + output.sources.",
        "hermes_highlight": "Hermes uses Research only when synthesis is needed, not for simple retrieval.",
        "talking_points": [
            "You.com: research_effort = lite/standard/deep/exhaustive (speed vs thoroughness)",
            "You.com: source_control boosts trusted domains without excluding others",
            "Hermes: merges Research into the brief schema, keeping facts separate from recommendations",
        ],
        "api_action": "research",
    },
    {
        "id": "structured-research",
        "number": 9,
        "title": "Structured Research Output",
        "phase": "Synthesize",
        "minutes": 5,
        "platform_focus": "both",
        "facilitator": (
            "Show You.com's output_schema for predictable JSON fields. "
            "Then show how Hermes maps those fields directly into workflow cards and CRM drafts."
        ),
        "audience_action": 'Click "Run Structured Research" and see signal/action fields.',
        "youcom_highlight": "output_schema returns predictable signal/why_it_matters/recommended_action fields.",
        "hermes_highlight": "Hermes maps structured API output into workflow cards without manual reformatting.",
        "talking_points": [
            "You.com: structured output bridges API responses to operational systems",
            "Hermes: predictable fields = CRM-ready drafts, review checklists, workflow cards",
            "Sources remain in output.sources for the Claims & Sources section",
        ],
        "api_action": "research_structured",
    },
    {
        "id": "team-context",
        "number": 10,
        "title": "Add Team Context (Hermes Connectors)",
        "phase": "Context",
        "minutes": 7,
        "platform_focus": "hermes",
        "facilitator": (
            "This is a Hermes strength: orchestrating CRM, docs, notes, and support context "
            "alongside You.com public evidence. Internal context is private — never cited as public proof."
        ),
        "audience_action": "Paste sample CRM or meeting notes into the internal context field.",
        "youcom_highlight": "You.com covers public evidence; it does not access your CRM or internal docs.",
        "hermes_highlight": "Hermes connects read-only GTM tools — CRM, docs, Slack, support — into one workflow.",
        "talking_points": [
            "Hermes: orchestrate multiple tools while keeping the workflow understandable",
            "You.com public claims and Hermes internal context must stay in separate sections",
            "Start read-only — no auto-writeback until the pilot proves quality",
        ],
        "api_action": None,
    },
    {
        "id": "connector-map",
        "number": 11,
        "title": "Create Connector Map",
        "phase": "Govern",
        "minutes": 7,
        "platform_focus": "hermes",
        "facilitator": (
            "Hermes admins define which tools each workflow can access. "
            "Walk the three buckets: read-only (fetch), draft-only (human approves before send), "
            "blocked (never). You.com Search/Contents/Research/MCP are read-only intelligence — "
            "they never write to CRM or email. CRM/Slack/email are draft-only in the first pilot: "
            "the workflow prepares output; a person sends it. Block auto-send, auto-CRM-update, "
            "and sensitive data explicitly."
        ),
        "audience_action": (
            "Fill in the connector map for your team's stack. "
            "Defaults are fine — adjust read/draft/blocked to match how your org actually works."
        ),
        "youcom_highlight": "You.com Search, Contents, Research, MCP = read-only intelligence connectors.",
        "hermes_highlight": "Hermes connector map: read-only, draft-only, and blocked tools per workflow.",
        "talking_points": [
            "Hermes: every integration maps to one job in the workflow",
            "Read-only = fetch only (You.com APIs, CRM read, docs) — no writes",
            "Draft-only = prepare output (email, Slack, CRM draft) — human sends after review",
            "Blocked = refuse even if asked (PII, sensitive data, auto-send, unapproved legal language)",
            "First pilot: read public web + approved context, draft reviews, no auto-send",
        ],
        "api_action": None,
    },
    {
        "id": "review-gates",
        "number": 12,
        "title": "Add Review Gates",
        "phase": "Govern",
        "minutes": 5,
        "platform_focus": "hermes",
        "facilitator": (
            "Hermes review gates make workflows usable without being reckless. "
            "Four states: Draft → Needs edits → Approved internal → Approved external. "
            "You.com citations feed the review — Hermes enforces the gate."
        ),
        "audience_action": "Run the review checklist. Set the review status for your brief.",
        "youcom_highlight": "You.com sources are the evidence reviewers inspect before approving claims.",
        "hermes_highlight": "Hermes blocks external-use output until a reviewer passes the approval gate.",
        "talking_points": [
            "Hermes: human review required before external use — not optional",
            "You.com: every factual claim should trace to a source URL or be marked uncertain",
            "Check: source backing, freshness, fact/recommendation separation, internal-only labels",
        ],
        "api_action": None,
    },
    {
        "id": "workflow-card",
        "number": 13,
        "title": "Generate Workflow Card",
        "phase": "Package",
        "minutes": 8,
        "platform_focus": "hermes",
        "facilitator": (
            "The workflow card is Hermes's packaging artifact — the handoff from 'this worked once' "
            "to 'our team can run this repeatedly.' It documents inputs, tools, output, review rules, and pilot plan."
        ),
        "audience_action": 'Click "Generate Workflow Card" and download the markdown.',
        "youcom_highlight": "Workflow card lists allowed You.com tools: Search, Contents, Research, MCP.",
        "hermes_highlight": "Workflow card = reusable Hermes skill/playbook spec with governance baked in.",
        "talking_points": [
            "Hermes: name, purpose, inputs, allowed/blocked tools, output format, review rules, metrics",
            "You.com: which APIs the workflow may call and with what source controls",
            "This card is what admins inspect and what teams reuse",
        ],
        "api_action": "generate_card",
    },
    {
        "id": "hermes-package",
        "number": 14,
        "title": "Build Your Agent End-to-End",
        "phase": "Package",
        "minutes": 20,
        "platform_focus": "hermes",
        "facilitator": (
            "This is the hands-on payoff — attendees build a working agent, not just watch. "
            "Walk the 6-step Agent Build Lab: create skill → paste instruction → wire MCP → "
            "set connector permissions → test run. Circulate while they build (~15 min). "
            "If someone lacks Hermes access, pair them or share Agent Kit for async build. "
            "Fallback: Evidence Bundle + paste if MCP unavailable."
        ),
        "audience_action": (
            "Follow the Agent Build Lab checklist. Complete all 6 steps in Hermes. "
            "Run the test command and check every verification item before moving on."
        ),
        "youcom_highlight": "Wire you-search, you-contents, you-research via MCP — read-only intelligence.",
        "hermes_highlight": "Attendees leave with /account-action-brief as a runnable, governed skill.",
        "talking_points": [
            "Hermes: skill name, instruction, tools, connector map, test run — five pieces, one agent",
            "You.com MCP: production path; no custom integration code",
            "Verify: six sections, source URLs, Draft status — not just 'it ran once'",
            "Blocked in pilot: auto-send, auto-CRM-update, external approval skipped",
        ],
        "api_action": None,
        "agent_build": True,
    },
    {
        "id": "test-three",
        "number": 15,
        "title": "Test With Three Accounts",
        "phase": "Pilot",
        "minutes": 5,
        "platform_focus": "both",
        "facilitator": (
            "Test the full chain — You.com evidence quality plus Hermes workflow consistency — "
            "with three accounts: lots of news, limited info, and internal-context-heavy."
        ),
        "audience_action": "Plan three test accounts and score using the quality scorecard.",
        "youcom_highlight": "Score citation support and freshness — You.com source quality metrics.",
        "hermes_highlight": "Score format compliance and review burden — Hermes workflow quality metrics.",
        "talking_points": [
            "You.com: are sources strong? (0–3) Are claims citation-backed?",
            "Hermes: does output match the schema? Is review burden low?",
            "Do not pilot until average scores are 2+ with no recurring unsupported-claim issues",
        ],
        "api_action": None,
    },
    {
        "id": "pilot-plan",
        "number": 16,
        "title": "Team Rollout Plan (Champions)",
        "phase": "Pilot",
        "minutes": 5,
        "platform_focus": "hermes",
        "champion_only": True,
        "post_event_recommended": True,
        "facilitator": (
            "Optional — for RevOps/GTM champions only, not every attendee. "
            "Say: 'Most people: join community and run 3 briefs this week. "
            "If you're taking this to your team, download the rollout template — "
            "fill it after Week 1, not tonight.' Walk the template in 60 sec if time; "
            "otherwise point to Download All and POST-EVENT-LEARNING."
        ),
        "audience_action": (
            "Champions only: skim the pre-filled template. Everyone else: skip — "
            "use Week 1 community challenge instead."
        ),
        "youcom_highlight": "Rollout metrics: % claims with strong sources, source freshness.",
        "hermes_highlight": "Rollout metrics: time saved, review edit rate, briefs used in real workflows.",
        "talking_points": [
            "Not homework for the room — this is for people pitching a small team pilot to their manager",
            "Recommended timing: after 3 personal briefs (Week 1), before asking for 5 users / 20 accounts",
            "Template ships in Download All — customize async with your owner and metrics",
            "Community path beats pilot forms for signups and retention; rollout plan wins internal budget",
        ],
        "api_action": None,
    },
    {
        "id": "wrap-up",
        "number": 17,
        "title": "Decide Next Action",
        "phase": "Close",
        "minutes": 5,
        "platform_focus": "both",
        "facilitator": (
            "Close with dual value recap. Community Continuation panel: join You.com Discord, "
            "introduce yourself (joined from this workshop). Download All optional."
        ),
        "audience_action": (
            "Join the You.com Discord (link below). Post an intro — mention you joined from this event."
        ),
        "talking_points": [
            "You.com answers 'what is true and current?' with source-backed evidence",
            "Hermes answers 'how does my team use this safely and repeatedly?' with workflows",
            "You.com Discord: introduce yourself in #introductions — role and what you're building",
            "Keep using /account-action-brief on your accounts",
        ],
        "youcom_highlight": "You.com: real-time web intelligence with citations, structure, and source controls.",
        "hermes_highlight": "Hermes: the layer that makes AI work repeatable, governable, and pilot-ready.",
        "api_action": None,
    },
]


def get_step(step_id: str) -> dict[str, Any] | None:
    for step in WORKSHOP_STEPS:
        if step["id"] == step_id:
            return step
    return None


# 60-minute live workshop track (default in app)
EXPRESS_50: dict[str, Any] = {
    "total_minutes": 60,
    "label": "60-Minute Live Workshop",
    "cuts": [
        "You.com APIs → platform playground at you.com/platform (not app Full Demo Chain)",
        "Agent build → all 6 steps live; define inputs in Hermes test command (not app form)",
        "Close → join Discord only (no 30-day or rollout plan)",
        "Source scoring exercise → optional if time",
        "Full 18-step track → app ?full=1 for self-paced reference",
    ],
    "post_event_doc": "workshop-app/AGENT-BUILD-GUIDE.md",
    "track": [
        {
            "id": "welcome",
            "minutes": 3,
            "facilitator": (
                "60-second opening: You.com = evidence, Hermes = workflow. "
                "Slides are the script — playground, then live Hermes setup (inputs defined in Hermes). "
                "Close = Discord only."
            ),
            "show_post_event": False,
        },
        {
            "id": "api-matrix",
            "minutes": 3,
            "title": "You.com API Map (60 sec each)",
            "facilitator": (
                "Flash API matrix on slides. Open https://you.com/platform — "
                "'We'll walk Search, Contents, Research in the playground next.'"
            ),
        },
        {
            "id": "web-search",
            "minutes": 15,
            "title": "You.com APIs — Platform Playground",
            "facilitator": (
                "Lead playground walk for AMD: Search → Contents → Research. "
                "Use slides 5–11 (APIs + MCP bridge). Attendees pick their own goal later in Hermes. "
                "Flash slides 8–9 before or after playground: MCP automates the chain. "
                "Do not use app Full Demo Chain as the primary API demo."
            ),
            "use_full_chain": False,
            "show_product_checklist": True,
            "playground_url": "https://you.com/platform",
        },
        {
            "id": "connector-map",
            "minutes": 5,
            "title": "Govern — Connectors & Review",
            "facilitator": (
                "Connector defaults OK. One sentence: internal context is private, never public evidence. "
                "Four review states in 60 sec. Set Draft."
            ),
            "include_review": True,
        },
        {
            "id": "workflow-card",
            "minutes": 3,
            "facilitator": (
                "Generate Workflow Card → Download. "
                "'One-off prompt → team workflow spec.'"
            ),
        },
        {
            "id": "hermes-package",
            "minutes": 26,
            "title": "Hermes Desktop — Install, Define Inputs & Test",
            "facilitator": (
                "Everyone: install.sh → restart Hermes → wire MCP → define inputs in test command → run /account-action-brief. "
                "Show slide 12 (skills + connectors) before install. Slides 15–17: install, MCP, test. "
                "Open SKILL.md briefly after install — not a black box. Circulate at MCP."
            ),
            "hermes_live": False,
            "agent_build": True,
            "agent_build_in_room_only": False,
            "show_schema": True,
        },
        {
            "id": "wrap-up",
            "minutes": 5,
            "facilitator": (
                "Discord only — join link + intro template. Copy from slides or Community panel. "
                "Download artifacts optional. No 30-day plan or rollout homework."
            ),
            "skip_pilot_form": True,
            "show_post_event": False,
        },
    ],
}


def get_express_steps() -> list[dict[str, Any]]:
    """Return express-track steps merged with full step definitions."""
    result: list[dict[str, Any]] = []
    for i, entry in enumerate(EXPRESS_50["track"]):
        base = get_step(entry["id"])
        if not base:
            continue
        step = {**base, **{k: v for k, v in entry.items() if k != "id"}}
        step["express_number"] = i
        step["express_total"] = len(EXPRESS_50["track"])
        step["minutes"] = entry.get("minutes", base["minutes"])
        if entry.get("title"):
            step["title"] = entry["title"]
        if entry.get("facilitator"):
            step["facilitator"] = entry["facilitator"]
        result.append(step)
    return result

