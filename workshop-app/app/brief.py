"""Assemble account action brief and workflow card from workshop session data."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from app.youcom import summarize_search


def build_brief(session: dict[str, Any]) -> str:
    company = session.get("company", "Unknown Company")
    website = session.get("website", "")
    job = session.get("job", "")
    workflow_goal = session.get("workflow_goal", "")
    internal_context = session.get("internal_context", "")
    search = session.get("search_results")
    research = session.get("research_results")
    contents = session.get("contents_results")

    signals_section = _signals_section(search, research)
    claims_section = _claims_section(search, research, contents)
    review_section = _review_section(session)

    lines = [
        f"# Account Action Brief: {company}",
        "",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*",
        "",
        "## 1. Snapshot",
        f"- **Company:** {company}",
        f"- **Website:** {website or 'Not provided'}",
        f"- **Brief goal:** {workflow_goal or 'Not specified'}",
        f"- **Workflow job:** {job or 'Not specified'}",
        "- **Source confidence:** Based on public web sources gathered in this session",
        "",
        "## 2. Current Signals",
        signals_section,
        "",
        "## 3. Why This Account Might Care",
        _why_care_section(research, workflow_goal),
        "",
        "## 4. Suggested Actions",
        _actions_section(research, session.get("structured_research")),
        "",
        "## 5. Claims And Sources",
        claims_section,
        "",
        "## 6. Review Notes",
        review_section,
    ]

    if internal_context.strip():
        lines.extend(
            [
                "",
                "## Internal Context (Private — Do Not Cite As Public Evidence)",
                internal_context.strip(),
            ]
        )

    lines.extend(
        [
            "",
            "---",
            "*Status: Draft — requires human review before internal or external use.*",
        ]
    )
    return "\n".join(lines)


def build_workflow_card(session: dict[str, Any]) -> str:
    company = session.get("company", "[COMPANY]")
    owner = session.get("workflow_owner", "[WORKFLOW OWNER]")
    role = session.get("primary_user", "Account owner or customer-facing team")
    connectors = session.get("connector_map", {})

    read_tools = connectors.get("read_tools", "You.com Search, Contents, Research, approved internal context")
    draft_tools = connectors.get("draft_tools", "Email draft, Slack review request, CRM update draft")
    blocked = connectors.get("blocked", "Sensitive customer data, unapproved legal language, auto-send")

    return f"""# Workflow Card

**Workflow name:** `/account-action-brief`

**Purpose:** Create a current, source-backed action brief for a company, customer, prospect, or partner.

## Platform Roles

**You.com (intelligence layer):**
- Web Search API — discover candidate sources with structured JSON
- Contents API — read selected URLs as clean markdown
- Research API — multi-source synthesis with citations
- Finance Research API — optional public-company financial context
- MCP Server — agent tool access without custom integration code

**Hermes (workflow layer):**
- Orchestrate You.com APIs and GTM connectors in sequence
- Enforce output schema, review gates, and allowed/blocked tools
- Package as a reusable skill or playbook for the team
- Run a measured two-week pilot with quality scorecards

**Primary user:** {role}

**Workflow owner:** {owner}

**Trigger:** Preparing for a meeting, account review, outbound sequence, QBR, or partner call

**Required inputs:**
- Company or account name

**Optional inputs:**
- Website
- Brief goal / focus (tailors Search and Research queries)
- Segment / region
- Relationship stage
- Meeting date
- Opportunity context
- Internal notes (sanitized)

**Allowed tools (read-only):**
- {read_tools}

**Draft-only tools:**
- {draft_tools}

**Blocked tools or data:**
- {blocked}
- Auto-send outreach
- Auto-update CRM (pilot phase)

**Output format:**
1. Snapshot
2. Current Signals
3. Why This Account Might Care
4. Suggested Actions
5. Claims And Sources
6. Review Notes

**Review rules:**
- Every factual claim needs a source or must be marked as an assumption
- External-use content requires human approval
- Internal-only context must be labeled and never cited as public evidence
- Weakly sourced claims move to Review Notes

**Success metrics:**
- Time saved per brief
- Percent of briefs with reviewer edits
- Percent of claims with strong sources (score 2–3)
- Number of briefs used in real workflows
- Number of follow-up actions created

**Pilot plan:**
- **Week 0:** Setup — 5 users, 20 accounts, confirm owner and review rules
- **Week 1:** Controlled runs — 10 briefs, require human review, track unsupported claims
- **Week 2:** Measured pilot — 20 briefs, score quality, decide expand/hold/fix

**Example account tested:** {company}

**Demo mode:** {session.get('demo_mode', False)}
"""


def build_hermes_prompt(session: dict[str, Any]) -> str:
    company = session.get("company", "[COMPANY]")
    workflow_goal = session.get("workflow_goal", "").strip()
    goal_line = (
        f"Tailor the brief to this goal: {workflow_goal}"
        if workflow_goal
        else "Tailor the brief to the user's stated goal when provided."
    )
    return f"""You are running the `/account-action-brief` workflow.

Goal:
Create a concise, source-backed account action brief for {company} that helps a team decide what to do next.
{goal_line}

Required behavior:
1. Confirm the account or company name.
2. Ask for or confirm the brief goal if not provided — use it to focus Search and Research.
3. Search for current public sources using You.com.
4. Prefer official, recent, and directly relevant sources.
5. Use Contents to inspect important URLs when snippets are not enough.
6. Use Research only when synthesis is needed.
7. Separate sourced facts from recommendations.
8. Include source URLs for factual claims.
9. Mark weak evidence and assumptions.
10. Label internal-only context.
11. Produce the brief in the approved output format.
12. End with review status and next action.

Do not:
- Invent facts.
- Treat old sources as current.
- Mix private internal context into external messaging.
- Auto-send messages or write to systems unless explicitly approved.

Return sections:
1. Snapshot
2. Current Signals
3. Why This Account Might Care
4. Suggested Actions
5. Claims And Sources
6. Review Notes
"""


def build_hermes_live_run(session: dict[str, Any]) -> dict[str, str]:
    """Generate copy-paste artifacts for a live Hermes demo within the workshop."""
    company = session.get("company", "AMD")
    website = session.get("website", "")
    job = session.get("job", "")
    workflow_goal = session.get("workflow_goal", "")

    run_command = f"/account-action-brief\n\ncompany: {company}\nwebsite: {website or 'optional'}"
    if workflow_goal.strip():
        run_command += f"\ngoal: {workflow_goal.strip()}"

    evidence_lines = [
        f"# API Evidence Bundle for Hermes Live Run",
        f"",
        f"**Company:** {company}",
        f"**Brief goal:** {workflow_goal or 'not set'}",
        f"**Workflow job:** {job}",
        f"",
        f"Use this evidence if Hermes is not calling You.com MCP live. "
        f"Otherwise run the skill and let Hermes fetch fresh sources via MCP.",
        f"",
    ]

    search = session.get("search_results")
    if search:
        evidence_lines.append("## You.com Search Results (summary)")
        for item in summarize_search(search)[:5]:
            evidence_lines.append(f"- **{item['title']}** — {item['url']}")
            if item.get("snippet"):
                evidence_lines.append(f"  - {item['snippet'][:180]}")
        evidence_lines.append("")

    research = session.get("research_results")
    if research:
        content = _research_content(research)
        evidence_lines.append("## You.com Research Synthesis")
        evidence_lines.append(content[:2000] if content else "(no content)")
        sources = research.get("output", {}).get("sources", [])
        if sources:
            evidence_lines.append("")
            evidence_lines.append("**Sources:**")
            for s in sources[:5]:
                evidence_lines.append(f"- {s.get('title', 'Source')}: {s.get('url', '')}")
        evidence_lines.append("")

    finance = session.get("finance_research")
    if finance:
        evidence_lines.append("## You.com Finance Research")
        evidence_lines.append(_research_content(finance)[:1000])
        evidence_lines.append("")

    internal = session.get("internal_context", "").strip()
    if internal:
        evidence_lines.append("## Internal Context (private — do not cite as public evidence)")
        evidence_lines.append(internal)
        evidence_lines.append("")

    evidence_lines.append(build_hermes_prompt(session))

    return {
        "run_command": run_command,
        "evidence_bundle": "\n".join(evidence_lines),
        "setup_checklist": "\n".join([
            "Hermes Live Demo — pre-workshop setup (do once, ~20 min)",
            "",
            "[ ] Hermes Workflow Studio open and logged in",
            "[ ] Skill /account-action-brief created (paste packaging prompt from app)",
            "[ ] You.com MCP connected in Hermes (you-search, you-contents, you-research)",
            "[ ] OR You.com API tools wired in Hermes with YDC_API_KEY",
            "[ ] Test run completed once for AMD before attendees arrive",
            "[ ] Hermes window ready on second monitor or split screen",
            "",
            "Live run (during workshop, ~7 min):",
            f"1. Type: /account-action-brief",
            f"2. Input company: {company}",
            "3. Narrate: Hermes calls You.com → drafts brief → review gate",
            "4. Show output matches six-section schema",
        ]),
    }


def _signals_section(search: dict | None, research: dict | None) -> str:
    lines: list[str] = []
    if search:
        for item in summarize_search(search)[:5]:
            age = f" ({item['page_age']})" if item.get("page_age") else ""
            lines.append(f"- **{item['title']}**{age}")
            if item.get("snippet"):
                lines.append(f"  - {item['snippet'][:200]}")
    if research:
        content = _research_content(research)
        if content:
            lines.append("")
            lines.append("**Research synthesis:**")
            lines.append(content[:1500])
    return "\n".join(lines) if lines else "- No signals gathered yet. Run Web Search and Research."


def _why_care_section(research: dict | None, workflow_goal: str = "") -> str:
    if not research:
        goal_hint = f" for: {workflow_goal}" if workflow_goal.strip() else ""
        return f"- Run Research to generate strategic implications{goal_hint}."
    content = _research_content(research)
    if content:
        goal_hint = f" (goal: {workflow_goal})" if workflow_goal.strip() else ""
        return (
            f"- Based on current public signals{goal_hint}, review the research synthesis for priority themes.\n"
            "- See Research output for detailed implications."
        )
    return "- Insufficient synthesis. Run Research API."


def _actions_section(research: dict | None, structured: dict | None) -> str:
    lines: list[str] = []
    if structured:
        try:
            import json

            output = structured.get("output", {})
            raw = output.get("content", "")
            if isinstance(raw, str):
                parsed = json.loads(raw)
                for sig in parsed.get("signals", []):
                    lines.append(f"- **{sig.get('signal', '')}**")
                    if sig.get("recommended_action"):
                        lines.append(f"  - Action: {sig['recommended_action']}")
        except (json.JSONDecodeError, TypeError):
            pass
    if not lines:
        lines = [
            "- Review top signals with account owner before next customer touchpoint",
            "- Prepare 2–3 sourced talking points from Claims & Sources section",
            "- Resolve open questions listed in Review Notes",
        ]
    return "\n".join(lines)


def _claims_section(
    search: dict | None,
    research: dict | None,
    contents: dict | None,
) -> str:
    lines: list[str] = []
    if search:
        for item in summarize_search(search)[:5]:
            lines.append(f"- **Claim source:** {item['title']}")
            lines.append(f"  - URL: {item['url']}")
            if item.get("page_age"):
                lines.append(f"  - Freshness: {item['page_age']}")
            lines.append(f"  - Confidence: Review required")
    if research:
        sources = research.get("output", {}).get("sources", [])
        for src in sources[:5]:
            title = src.get("title", src.get("url", "Source"))
            url = src.get("url", "")
            lines.append(f"- **Research source:** {title}")
            if url:
                lines.append(f"  - URL: {url}")
    if contents:
        for page in contents.get("results", contents.get("pages", []))[:3]:
            title = page.get("title", page.get("url", "Page"))
            url = page.get("url", "")
            lines.append(f"- **Page inspected:** {title}")
            if url:
                lines.append(f"  - URL: {url}")
    return "\n".join(lines) if lines else "- No claims documented yet."


def _review_section(session: dict[str, Any]) -> str:
    notes = [
        "- All factual claims require human verification before external use",
        "- Review source scores (keep 2–3 in main brief, move 1 to here, remove 0)",
    ]
    if session.get("demo_mode"):
        notes.append("- **Demo mode:** API responses are sample data for teaching")
    if not session.get("search_results"):
        notes.append("- Missing: Web Search results not yet gathered")
    if not session.get("research_results"):
        notes.append("- Missing: Research synthesis not yet run")
    return "\n".join(notes)


def _research_content(research: dict) -> str:
    output = research.get("output", {})
    content = output.get("content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, dict):
        import json

        return json.dumps(content, indent=2)
    return ""
