"""Community continuation program — keep members on You.com API + Hermes after the workshop."""

from __future__ import annotations

import os
from typing import Any

YOU_COM_DISCORD_URL = "https://discord.gg/2C4WgryxSD"

DISCORD_INTRO_TEMPLATE = """Hi! I joined from the Account Action Brief workshop (Hermes + You.com).

- **Name / role:**
- **What I'm building:** /account-action-brief workflow
- **First company I'll brief:**
- **One thing I want to learn in this community:**
"""

COMMUNITY_CHALLENGES: list[dict[str, str]] = [
    {
        "week": "After the workshop",
        "title": "Join the You.com Discord",
        "task": "Join https://discord.gg/2C4WgryxSD, post your intro in #introductions, and say you joined from this workshop.",
    },
]

API_CONTINUATION_PATHS: list[dict[str, str]] = [
    {
        "path": "Bring your own key (BYOK)",
        "detail": "Members keep their own YDC_API_KEY in Hermes MCP or local .env. Best for long-term independence.",
    },
    {
        "path": "Community workshop credits",
        "detail": "Co-hosts arrange a You.com community/workshop key pool with usage caps and fair-use policy.",
    },
    {
        "path": "Org MCP in Hermes",
        "detail": "Shared Hermes org wires one You.com MCP connector; members run skills without managing keys individually.",
    },
]

FACILITATOR_BROADCAST_SKILL = """You are the community facilitator assistant for the Account Action Brief workshop alumni group.

Goal:
Produce a short, source-backed community update members can read in Slack/Discord or inside Hermes.

When the facilitator provides a topic, you must:
1. Use You.com Search and Research for current public signals on the topic.
2. Summarize 3–5 bullet points with source URLs.
3. Suggest one `/account-action-brief` exercise for members this week (company + why).
4. End with a community CTA: run the skill, share one learning, ask one question.
5. Keep tone practical — no hype. Mark uncertain claims.

Output format:
## Community Pulse — [DATE]
**Topic:** [TOPIC]

### Signals (sourced)
- ...

### This week's exercise
Run `/account-action-brief` for **[COMPANY]** because **[REASON]**.

### CTA
- Run your agent
- Reply with: company you tried, one source you trusted, one governance question

Review status: Draft — facilitator sends manually.
Do not auto-post to Slack, email, or CRM.
"""

FACILITATOR_BROADCAST_COMMAND = """/community-pulse

topic: AI agents in enterprise SaaS — what account teams should watch this month
audience: workshop alumni building account brief workflows
"""


def get_community_config() -> dict[str, str]:
    return {
        "name": os.environ.get("COMMUNITY_NAME", "").strip() or "You.com Discord",
        "join_url": os.environ.get("COMMUNITY_JOIN_URL", "").strip() or YOU_COM_DISCORD_URL,
        "discord_url": os.environ.get("COMMUNITY_DISCORD_URL", "").strip() or YOU_COM_DISCORD_URL,
        "hermes_org": os.environ.get("COMMUNITY_HERMES_ORG", "").strip(),
        "slack_url": os.environ.get("COMMUNITY_SLACK_URL", "").strip(),
        "contact": os.environ.get("COMMUNITY_CONTACT", "").strip(),
    }


def get_community_payload() -> dict[str, Any]:
    config = get_community_config()
    discord = config["discord_url"] or config["join_url"]
    return {
        "config": config,
        "configured": bool(discord or config["slack_url"] or config["hermes_org"]),
        "discord_intro_template": DISCORD_INTRO_TEMPLATE,
        "discord_intro_instructions": (
            f"Join the You.com Discord ({discord}), find #introductions or the welcome channel, "
            "and post the intro below — mention you joined from this workshop."
        ),
        "api_paths": API_CONTINUATION_PATHS,
        "challenges": COMMUNITY_CHALLENGES,
        "member_onboarding": [
            f"Join the You.com Discord: {discord}",
            "Introduce yourself in #introductions — say you joined from the Account Action Brief workshop",
            "Include: your role and what you're building with /account-action-brief",
        ],
        "facilitator_playbook": [
            "Share Discord link at workshop close",
            "Optional: occasional office hour for MCP debugging",
            "Optional: /community-pulse for facilitator-sourced digests",
        ],
        "hermes_messaging_model": {
            "summary": (
                "Hermes does not replace your community chat app — it powers the agent layer. "
                "Facilitators publish pulses via a skill; members run their own agents and reply in the community channel."
            ),
            "facilitator_skill": "/community-pulse",
            "member_skill": "/account-action-brief",
            "delivery": "Facilitator copies pulse output → posts to You.com Discord OR shares in Hermes shared library",
        },
        "broadcast_skill_instruction": FACILITATOR_BROADCAST_SKILL,
        "broadcast_run_command": FACILITATOR_BROADCAST_COMMAND,
    }


def build_community_playbook_markdown() -> str:
    payload = get_community_payload()
    config = payload["config"]
    lines = [
        "# Community Continuation Playbook",
        "",
        f"**Community:** {config['name']}",
        "",
        "## For members — stay on You.com + Hermes after the workshop",
        "",
    ]
    for i, step in enumerate(payload["member_onboarding"], 1):
        lines.append(f"{i}. {step}")
    discord = config.get("discord_url") or config.get("join_url")
    if discord:
        lines.append(f"\n**You.com Discord:** {discord}")
    lines.extend([
        "",
        "### Intro post (copy into #introductions)",
        "",
        "```text",
        payload["discord_intro_template"].strip(),
        "```",
    ])
    if config["hermes_org"]:
        lines.append(f"**Hermes org:** {config['hermes_org']}")
    if config["slack_url"]:
        lines.append(f"**Community chat:** {config['slack_url']}")

    lines.extend(["", "## API access — three paths", ""])
    for p in payload["api_paths"]:
        lines.append(f"- **{p['path']}:** {p['detail']}")

    lines.extend(["", "## After the workshop", ""])
    for c in payload["challenges"]:
        lines.append(f"- **{c['title']}:** {c['task']}")
        lines.append("")

    lines.extend([
        "## For facilitators — message the community via Hermes",
        "",
        payload["hermes_messaging_model"]["summary"],
        "",
        f"1. Create facilitator skill: `{payload['hermes_messaging_model']['facilitator_skill']}`",
        f"2. Members keep: `{payload['hermes_messaging_model']['member_skill']}`",
        f"3. Delivery: {payload['hermes_messaging_model']['delivery']}",
        "",
        "### Facilitator broadcast instruction (paste into Hermes)",
        "",
        "```text",
        payload["broadcast_skill_instruction"].strip(),
        "```",
        "",
        "### Example run command",
        "",
        "```text",
        payload["broadcast_run_command"].strip(),
        "```",
        "",
        "## Facilitator playbook",
        "",
    ])
    for step in payload["facilitator_playbook"]:
        lines.append(f"- {step}")

    return "\n".join(lines)
