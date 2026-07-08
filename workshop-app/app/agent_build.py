"""End-to-end Hermes agent build kit — attendees leave with a working /account-action-brief skill."""

from __future__ import annotations

from typing import Any

from app.brief import build_hermes_prompt, build_workflow_card

BUILD_STEPS: list[dict[str, Any]] = [
    {
        "id": "prereqs",
        "title": "1. Prerequisites",
        "minutes": 2,
        "in_room": True,
        "summary": "Hermes access + You.com API key (or org-provided keys).",
        "instructions": [
            "Open Hermes Agent desktop app (recommended) or Hermes Workflow Studio and sign in.",
            "Desktop path: use the Hermes Desktop Skill Pack panel below — skip manual skill creation.",
            "Studio path: create a new skill/playbook manually (steps 2–3).",
            "Get a You.com API key at https://you.com/settings/api (or use workshop-provided key).",
            "Have this workshop session filled in: company, connector map, workflow card generated.",
        ],
        "verify": "You can open Hermes and create a new skill/playbook.",
    },
    {
        "id": "create_skill",
        "title": "2. Create the skill",
        "minutes": 3,
        "in_room": True,
        "summary": "Install skill pack (desktop) or create skill manually (Studio).",
        "instructions": [
            "Desktop (recommended): run install.sh from hermes-desktop/ or Download Skill Pack (.zip) below.",
            "Desktop: skills install to ~/.hermes/skills/ — restart Hermes if needed.",
            "Studio: New skill named exactly /account-action-brief.",
            "Studio: Description: Source-backed account brief using You.com + approved team context.",
            "Studio: Trigger: slash command /account-action-brief",
        ],
        "verify": "Skill /account-action-brief appears in Hermes (installed or created).",
    },
    {
        "id": "paste_instruction",
        "title": "3. Paste the instruction",
        "minutes": 3,
        "in_room": True,
        "summary": "Desktop: skip (included in pack). Studio: paste packaging prompt.",
        "instructions": [
            "Desktop users: skip — instruction is already in the installed SKILL.md.",
            "Studio: open Packaging Prompt panel below (or Agent Kit download).",
            "Studio: paste the full prompt as the skill system instruction / behavior.",
            "Add required input: company_name (string, required).",
            "Optional inputs: company_url, workflow_goal (brief focus), internal_context, output_audience (internal | external draft).",
        ],
        "copy_key": "instruction",
        "verify": "Instruction includes all six output sections and 'Do not invent facts' rules.",
    },
    {
        "id": "wire_tools",
        "title": "4. Wire You.com tools",
        "minutes": 5,
        "in_room": True,
        "summary": "Connect MCP (recommended) or API tools — read-only only.",
        "instructions": [
            "Option A — MCP (recommended): Add You.com MCP server https://api.you.com/mcp",
            "Enable: you-search, you-contents, you-research (finance optional).",
            "Attach only these tools to /account-action-brief (least privilege).",
            "Option B — API: Add You.com connector with YDC_API_KEY; map Search, Contents, Research.",
            "Do not enable write/send tools in this step.",
        ],
        "copy_key": "mcp_config",
        "verify": "Test tool call: run a single Search for your workshop company; tool call visible in Hermes.",
    },
    {
        "id": "govern_connectors",
        "title": "5. Set connector permissions",
        "minutes": 3,
        "in_room": True,
        "summary": "Set connector permissions from your workshop connector map.",
        "instructions": [
            "In Hermes admin or skill settings, set allowed tools from your connector map.",
            "Read-only: You.com APIs, CRM read, internal docs.",
            "Draft-only: email, Slack review, CRM update draft — human sends.",
            "Blocked: auto-send, auto-CRM-update, sensitive data, unapproved legal language.",
            "Set default review status to Draft on every run.",
        ],
        "copy_key": "connector_map",
        "verify": "Skill settings document read vs draft vs blocked (matches workflow card).",
    },
    {
        "id": "test_run",
        "title": "6. Test run & verify",
        "minutes": 5,
        "in_room": True,
        "summary": "Define company + brief goal in the test command; confirm six sections + sources + Draft status.",
        "instructions": [
            "Define inputs in Hermes (not the workshop app): company, optional website, brief goal, output_audience.",
            "Brief goal examples — Renewal: 'Prepare for renewal…'; Outbound: 'Research for outbound…'; "
            "Competitive: 'Competitive positioning…'; Partner: 'Partner opportunity…'",
            "Run the test command below — use AMD or your own account.",
            "Watch for You.com tool calls (Search → Contents → Research).",
            "Confirm output has all six sections in order.",
            "Confirm Claims & Sources lists URLs, not invented links.",
            "Set review status to Draft; do not mark Approved for external use yet.",
        ],
        "copy_key": "test_command",
        "verify": "Output passes the verification checklist below.",
    },
]

VERIFICATION_CHECKLIST: list[str] = [
    "Skill /account-action-brief runs without errors",
    "You.com tool calls visible (or evidence pasted if MCP unavailable)",
    "Section 1 Snapshot — company named correctly",
    "Section 2 Current Signals — recent, sourced signals",
    "Section 5 Claims & Sources — URLs present for factual claims",
    "Section 6 Review Notes — weak claims flagged",
    "Review status starts as Draft",
    "No auto-send or CRM write occurred",
]


def _connector_block(session: dict[str, Any]) -> str:
    connectors = session.get("connector_map", {})
    return (
        f"Read-only tools:\n{connectors.get('read_tools', 'You.com Search, Contents, Research; CRM read; docs')}\n\n"
        f"Draft-only tools:\n{connectors.get('draft_tools', 'Email draft, Slack review, CRM update draft')}\n\n"
        f"Blocked:\n{connectors.get('blocked', 'Sensitive data, PII, auto-send, unapproved legal language')}"
    )


def _mcp_config_block() -> str:
    return (
        "You.com MCP Server: https://api.you.com/mcp\n\n"
        "Enable tools for /account-action-brief:\n"
        "- you-search\n"
        "- you-contents\n"
        "- you-research\n\n"
        "Optional: finance research for public companies.\n\n"
        "Do not attach draft/send tools to this skill in the pilot phase."
    )


def _skill_metadata(session: dict[str, Any]) -> dict[str, Any]:
    company = session.get("company", "AMD")
    return {
        "name": "/account-action-brief",
        "description": (
            "Creates a current, source-backed account action brief using You.com web intelligence "
            "and approved team context."
        ),
        "inputs": {
            "company_name": {"required": True, "example": company},
            "company_url": {"required": False, "example": session.get("website", "")},
            "workflow_goal": {
                "required": False,
                "example": session.get(
                    "workflow_goal",
                    "Prepare for an upcoming customer meeting with actionable next steps.",
                ),
            },
            "internal_context": {"required": False},
            "output_audience": {"required": False, "enum": ["internal", "external draft"]},
        },
        "tools_mcp": ["you-search", "you-contents", "you-research"],
        "mcp_server": "https://api.you.com/mcp",
        "output_sections": [
            "Snapshot",
            "Current Signals",
            "Why This Account Might Care",
            "Suggested Actions",
            "Claims And Sources",
            "Review Notes",
        ],
        "default_review_status": "Draft",
    }


def get_agent_build_payload(session: dict[str, Any]) -> dict[str, Any]:
    company = session.get("company", "AMD")
    website = session.get("website", "")
    workflow_goal = session.get("workflow_goal", "").strip()
    instruction = build_hermes_prompt(session)
    test_command = f"/account-action-brief\n\ncompany: {company}\nwebsite: {website or 'optional'}"
    if workflow_goal:
        test_command += f"\ngoal: {workflow_goal}"

    copies = {
        "instruction": instruction,
        "mcp_config": _mcp_config_block(),
        "connector_map": _connector_block(session),
        "test_command": test_command,
        "skill_metadata": _skill_metadata(session),
    }

    steps = []
    for step in BUILD_STEPS:
        item = {**step}
        if step.get("copy_key"):
            item["copy_content"] = copies[step["copy_key"]]
        steps.append(item)

    return {
        "title": "Build Your Agent — End to End",
        "subtitle": "Leave with a working /account-action-brief skill in Hermes",
        "in_room_minutes": sum(s["minutes"] for s in BUILD_STEPS if s.get("in_room")),
        "async_minutes": sum(s["minutes"] for s in BUILD_STEPS if not s.get("in_room")),
        "total_minutes": sum(s["minutes"] for s in BUILD_STEPS),
        "steps": steps,
        "verification_checklist": VERIFICATION_CHECKLIST,
        "copies": copies,
        "fallback_note": (
            "If MCP is not available in your Hermes build: use evidence from the platform playground, "
            "paste into Hermes with the test command. "
            "Say clearly this is a workshop fallback — production uses MCP."
        ),
        "desktop_path": True,
        "desktop_note": (
            "Hermes desktop users: install the skill pack (install.sh or zip download) "
            "instead of creating the skill manually — then wire MCP in step 4."
        ),
    }


def build_agent_kit_markdown(session: dict[str, Any]) -> str:
    payload = get_agent_build_payload(session)
    company = session.get("company", "AMD")
    lines = [
        "# Agent Build Kit — /account-action-brief",
        "",
        f"**Company tested in workshop:** {company}",
        f"**Estimated build time:** {payload['total_minutes']} minutes",
        "",
        "Follow steps 1–6 in order. You should leave with a **working Hermes skill**.",
        "",
    ]

    for step in payload["steps"]:
        lines.append(f"## {step['title']}")
        lines.append("")
        lines.append(step["summary"])
        lines.append("")
        for inst in step.get("instructions", []):
            lines.append(f"- {inst}")
        lines.append("")
        if step.get("copy_content"):
            lines.append("```text")
            lines.append(step["copy_content"].strip())
            lines.append("```")
            lines.append("")
        lines.append(f"**Verify:** {step['verify']}")
        lines.append("")

    lines.append("## Verification checklist")
    lines.append("")
    for item in payload["verification_checklist"]:
        lines.append(f"- [ ] {item}")
    lines.append("")

    lines.append("## Workflow card (reference)")
    lines.append("")
    lines.append(build_workflow_card(session))
    lines.append("")

    lines.append("## Fallback (no MCP)")
    lines.append("")
    lines.append(payload["fallback_note"])
    lines.append("")

    lines.append("## Hermes Desktop skill pack")
    lines.append("")
    lines.append(payload.get("desktop_note", ""))
    lines.append("")
    lines.append("See `HERMES-DESKTOP-SETUP.md` or run:")
    lines.append("")
    lines.append("```bash")
    lines.append("cd workshop-app/hermes-desktop && ./install.sh")
    lines.append("```")
    lines.append("")

    return "\n".join(lines)
