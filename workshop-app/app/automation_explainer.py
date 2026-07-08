"""How Hermes automates /account-action-brief — workshop explainer content."""

from __future__ import annotations

from typing import Any

AUTOMATION_LOOP: list[dict[str, str]] = [
    {
        "step": "1. You trigger",
        "detail": "Run `/account-action-brief` in Hermes with a company name (and optional URL).",
    },
    {
        "step": "2. Hermes orchestrates",
        "detail": "The skill calls You.com via MCP: Search → pick sources → Contents → Research.",
    },
    {
        "step": "3. Evidence → brief",
        "detail": "Hermes maps live API results into the six-section schema every time.",
    },
    {
        "step": "4. Human reviews",
        "detail": "Output starts as Draft. You approve before internal or external use — no auto-send.",
    },
]

AUTOMATED_VS_HUMAN: dict[str, list[str]] = {
    "hermes_automates": [
        "Running the You.com API chain (no manual curl or copy-paste)",
        "Picking and reading high-value URLs from Search results",
        "Synthesizing multi-source research with citations",
        "Formatting all six output sections consistently",
        "Applying connector rules (read vs draft vs blocked tools)",
        "Defaulting review status to Draft on every run",
    ],
    "human_still_does": [
        "Trigger the workflow (slash command or natural language)",
        "Review claims, sources, and tone before use",
        "Approve internal-use or external-use gates",
        "Send email, Slack, or CRM updates (draft-only — you click send)",
        "Decide when to expand from personal use to team rollout",
    ],
}

FACILITATOR_ONE_LINER = (
    "In the app we run You.com manually so you see each API. In Hermes, the same chain runs "
    "automatically when you type /account-action-brief — Hermes orchestrates, you review."
)


def get_automation_payload() -> dict[str, Any]:
    return {
        "headline": "How Hermes automates the account brief",
        "summary": (
            "The workshop app demonstrates You.com step-by-step. Your Hermes agent runs that same "
            "evidence chain on demand — then formats a governed brief you review before use."
        ),
        "facilitator_one_liner": FACILITATOR_ONE_LINER,
        "loop": AUTOMATION_LOOP,
        "automated": AUTOMATED_VS_HUMAN["hermes_automates"],
        "human": AUTOMATED_VS_HUMAN["human_still_does"],
        "before_after": {
            "manual": "Search tabs → copy snippets → paste into doc → format → hope sources are current",
            "automated": "/account-action-brief Acme Corp → Hermes calls You.com → six-section Draft brief",
        },
        "test_command": "/account-action-brief\n\ncompany: AMD\nwebsite: https://www.amd.com",
    }


def build_automation_markdown() -> str:
    p = get_automation_payload()
    lines = [
        "# How Hermes Automates /account-action-brief",
        "",
        p["summary"],
        "",
        "## The automation loop",
        "",
    ]
    for item in p["loop"]:
        lines.append(f"**{item['step']}** — {item['detail']}")
    lines.extend(["", "## Hermes automates", ""])
    for item in p["automated"]:
        lines.append(f"- {item}")
    lines.extend(["", "## You still do (by design)", ""])
    for item in p["human"]:
        lines.append(f"- {item}")
    lines.extend(
        [
            "",
            "## Before vs after",
            "",
            f"**Manual today:** {p['before_after']['manual']}",
            f"**With Hermes:** {p['before_after']['automated']}",
            "",
            "## Test command",
            "",
            "```text",
            p["test_command"],
            "```",
        ]
    )
    return "\n".join(lines)
