"""Hermes desktop skill pack — installable SKILL.md bundle for Hermes Agent."""

from __future__ import annotations

import io
import os
import zipfile
from pathlib import Path
from typing import Any

SKILLS_ROOT = Path(__file__).parent.parent / "hermes-desktop" / "skills"
INSTALL_SCRIPT = Path(__file__).parent.parent / "hermes-desktop" / "install.sh"

SKILL_IDS = ("account-action-brief", "meeting-prep", "community-pulse", "workshop-60min")

REQUIRED_SKILL_FILES: dict[str, tuple[str, ...]] = {
    "account-action-brief": (
        "SKILL.md",
        "references/output-schema.md",
        "references/connector-map.md",
        "references/review-gates.md",
        "references/youcom-api-chain.md",
        "references/calendar-trigger.md",
    ),
    "meeting-prep": (
        "SKILL.md",
        "references/account-action-brief-delegate.md",
        "references/calendar-connectors.md",
        "references/delivery-options.md",
    ),
    "community-pulse": ("SKILL.md",),
    "workshop-60min": (
        "SKILL.md",
        "references/install.md",
        "references/post-event.md",
    ),
}

PACK_ROOT = Path(__file__).parent.parent / "hermes-desktop"
SETUP_DOC = Path(__file__).parent.parent / "HERMES-DESKTOP-SETUP.md"

SKILL_SUMMARIES: dict[str, str] = {
    "account-action-brief": "Source-backed account brief via You.com Search, Contents, Research",
    "meeting-prep": "Calendar-triggered briefs delivered before customer meetings",
    "community-pulse": "Weekly sourced digest for workshop alumni (facilitators)",
    "workshop-60min": "60-min workshop guide and post-event pointers inside Hermes",
}


def _skills_dest() -> str:
    home = Path.home()
    return str(home / ".hermes" / "skills")


def _meeting_prep_test_command(session: dict[str, Any]) -> str:
    company = session.get("company", "AMD")
    return (
        "/meeting-prep\n\n"
        "lookahead_hours: 24\n"
        "delivery: hermes_thread\n"
        "meeting_filter: customer-facing\n\n"
        f"# Or single meeting:\n"
        f"Prep brief for my {company} call tomorrow"
    )


def _personalized_example(session: dict[str, Any]) -> str:
    company = session.get("company", "AMD")
    website = session.get("website", "")
    workflow_goal = session.get("workflow_goal", "").strip()
    lines = [
        "/account-action-brief",
        "",
        f"company: {company}",
        f"website: {website or 'optional'}",
    ]
    if workflow_goal:
        lines.append(f"goal: {workflow_goal}")
    lines.append("output_audience: internal")
    return "\n".join(lines)


def _session_context_ref(session: dict[str, Any]) -> str:
    company = session.get("company", "AMD")
    website = session.get("website", "")
    connectors = session.get("connector_map", {})
    lines = [
        f"# Workshop Session — {company}",
        "",
        f"**Website:** {website or 'not set'}",
        f"**Primary user:** {session.get('primary_user', '')}",
        "",
        "## Connector map (from workshop session)",
        "",
        f"**Read-only:** {connectors.get('read_tools', '')}",
        f"**Draft-only:** {connectors.get('draft_tools', '')}",
        f"**Blocked:** {connectors.get('blocked', '')}",
        "",
        "## Test command",
        "",
        "```text",
        _personalized_example(session),
        "```",
    ]
    return "\n".join(lines)


def get_hermes_desktop_payload(session: dict[str, Any]) -> dict[str, Any]:
    pack_root = Path(__file__).parent.parent / "hermes-desktop"
    install_rel = "workshop-app/hermes-desktop/install.sh"
    skills = []
    for skill_id in SKILL_IDS:
        skill_dir = SKILLS_ROOT / skill_id
        skill_md = skill_dir / "SKILL.md"
        refs = []
        ref_dir = skill_dir / "references"
        if ref_dir.is_dir():
            refs = sorted(p.name for p in ref_dir.iterdir() if p.is_file())
        skills.append(
            {
                "id": skill_id,
                "name": f"/{skill_id}",
                "summary": SKILL_SUMMARIES.get(skill_id, ""),
                "path": str(skill_dir.relative_to(pack_root.parent)),
                "has_skill_md": skill_md.is_file(),
                "references": refs,
            }
        )

    return {
        "title": "Hermes Desktop Skill Pack",
        "subtitle": "Install ready-made skills into Hermes Agent (desktop or CLI)",
        "skills_dest": _skills_dest(),
        "install_script": install_rel,
        "install_commands": {
            "script": f"cd workshop-app/hermes-desktop && chmod +x install.sh && ./install.sh",
            "cli": "\n".join(
                f'hermes skills install "{SKILLS_ROOT / sid / "SKILL.md"}"'
                for sid in SKILL_IDS
            ),
            "manual": f"cp -r workshop-app/hermes-desktop/skills/* {_skills_dest()}/",
        },
        "skills": skills,
        "mcp_server": "https://api.you.com/mcp",
        "mcp_tools": ["you-search", "you-contents", "you-research"],
        "test_command": _personalized_example(session),
        "meeting_prep_test_command": _meeting_prep_test_command(session),
        "setup_checklist": [
            "Install Hermes Agent desktop app (or CLI) and sign in",
            "Run install.sh or download the personalized skill pack zip (4 skills)",
            "Restart Hermes if skills do not appear immediately",
            "Add You.com MCP server: https://api.you.com/mcp",
            "Enable you-search, you-contents, you-research",
            f"Test /account-action-brief with your workshop company",
            "Week 2+: wire calendar read-only → test /meeting-prep",
        ],
        "desktop_vs_studio": {
            "desktop": "Install skill pack → wire MCP → run /account-action-brief (faster, recommended)",
            "studio": "Create skill manually → paste packaging prompt from Agent Build Lab",
        },
        "download_url": "/api/hermes-desktop/download",
        "docs": "HERMES-DESKTOP-SETUP.md",
    }


def build_hermes_desktop_setup_markdown(session: dict[str, Any]) -> str:
    payload = get_hermes_desktop_payload(session)
    company = session.get("company", "AMD")
    lines = [
        "# Hermes Desktop Setup — Workshop Skill Pack",
        "",
        f"**Workshop company:** {company}",
        "",
        "Four installable skills for Hermes Agent:",
        "",
    ]
    for skill in payload["skills"]:
        lines.append(f"- `{skill['name']}` — {skill['summary']}")
    lines.append("")
    lines.append("## Quick install")
    lines.append("")
    lines.append("```bash")
    lines.append(payload["install_commands"]["script"])
    lines.append("```")
    lines.append("")
    lines.append(f"Skills install to: `{payload['skills_dest']}`")
    lines.append("")
    lines.append("## Wire You.com MCP")
    lines.append("")
    lines.append(f"Server: `{payload['mcp_server']}`")
    lines.append("")
    lines.append("Enable:")
    for tool in payload["mcp_tools"]:
        lines.append(f"- {tool}")
    lines.append("")
    lines.append("## Test run")
    lines.append("")
    lines.append("```text")
    lines.append(payload["test_command"])
    lines.append("```")
    lines.append("")
    lines.append("## Setup checklist")
    lines.append("")
    for item in payload["setup_checklist"]:
        lines.append(f"- [ ] {item}")
    lines.append("")
    return "\n".join(lines)


def build_skill_pack_zip(session: dict[str, Any]) -> bytes:
    """Zip skill pack; adds personalized session reference for account-action-brief."""
    buf = io.BytesIO()
    session_ref = _session_context_ref(session)
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        if INSTALL_SCRIPT.is_file():
            zf.write(INSTALL_SCRIPT, "install.sh")
        for skill_id in SKILL_IDS:
            skill_dir = SKILLS_ROOT / skill_id
            if not skill_dir.is_dir():
                continue
            for path in skill_dir.rglob("*"):
                if path.is_file():
                    arcname = f"skills/{skill_id}/{path.relative_to(skill_dir)}"
                    zf.write(path, arcname)
            if skill_id == "account-action-brief":
                zf.writestr(
                    f"skills/{skill_id}/references/workshop-session.md",
                    session_ref,
                )
        zf.writestr("README.txt", _zip_readme(session))
    return buf.getvalue()


def _zip_readme(session: dict[str, Any]) -> str:
    company = session.get("company", "AMD")
    dest = _skills_dest()
    return (
        "Hermes Workshop Skill Pack\n"
        "==========================\n\n"
        f"Personalized for workshop company: {company}\n\n"
        "Install:\n"
        "  chmod +x install.sh && ./install.sh\n\n"
        f"Or copy skills/* to {dest}/\n\n"
        "Then wire You.com MCP: https://api.you.com/mcp\n"
        "Test: /account-action-brief\n"
    )


def validate_skill_pack(session: dict[str, Any] | None = None) -> dict[str, Any]:
    """Preflight validation for Hermes desktop skill pack files and zip export."""
    session = session or {"company": "AMD", "website": "", "connector_map": {}}
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict[str, Any]] = []

    def record(name: str, ok: bool, detail: str = "") -> None:
        checks.append({"name": name, "ok": ok, "detail": detail})
        if not ok:
            errors.append(f"{name}: {detail}" if detail else name)

    record("HERMES-DESKTOP-SETUP.md", SETUP_DOC.is_file())
    record("install.sh", INSTALL_SCRIPT.is_file())
    if INSTALL_SCRIPT.is_file() and not os.access(INSTALL_SCRIPT, os.X_OK):
        warnings.append("install.sh is not executable — run: chmod +x hermes-desktop/install.sh")
        record("install.sh executable", False, "chmod +x required")
    else:
        record("install.sh executable", INSTALL_SCRIPT.is_file() and os.access(INSTALL_SCRIPT, os.X_OK))

    if INSTALL_SCRIPT.is_file():
        script = INSTALL_SCRIPT.read_text(encoding="utf-8")
        for skill_id in SKILL_IDS:
            record(
                f"install.sh references {skill_id}",
                skill_id in script,
                "missing from install loop" if skill_id not in script else "",
            )

    for skill_id in SKILL_IDS:
        skill_dir = SKILLS_ROOT / skill_id
        record(f"skill directory {skill_id}", skill_dir.is_dir())
        for rel_path in REQUIRED_SKILL_FILES.get(skill_id, ("SKILL.md",)):
            full = skill_dir / rel_path
            record(f"{skill_id}/{rel_path}", full.is_file(), "file missing" if not full.is_file() else "")
            if full.is_file() and rel_path == "SKILL.md":
                text = full.read_text(encoding="utf-8")
                record(
                    f"{skill_id}/SKILL.md frontmatter",
                    text.startswith("---") and "name:" in text and "description:" in text,
                    "YAML frontmatter with name and description required",
                )

    try:
        zip_bytes = build_skill_pack_zip(session)
        record("skill pack zip builds", len(zip_bytes) > 1000, f"{len(zip_bytes)} bytes")
        with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
            names = set(zf.namelist())
            for skill_id in SKILL_IDS:
                entry = f"skills/{skill_id}/SKILL.md"
                record(f"zip contains {entry}", entry in names, "missing from archive")
            record("zip contains install.sh", "install.sh" in names)
            record(
                "zip contains workshop-session.md",
                "skills/account-action-brief/references/workshop-session.md" in names,
            )
    except Exception as exc:
        record("skill pack zip builds", False, str(exc))

    ok = len(errors) == 0
    return {
        "ok": ok,
        "errors": errors,
        "warnings": warnings,
        "checks": checks,
        "skill_count": len(SKILL_IDS),
        "skills_root": str(SKILLS_ROOT),
        "install_script": str(INSTALL_SCRIPT),
    }
