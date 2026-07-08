"""Post-event learning paths — everything deferred from the 60-minute live workshop."""

from __future__ import annotations

from typing import Any

POST_EVENT_PATHS: list[dict[str, Any]] = [
    {
        "title": "Finish your agent",
        "time": "15–20 min async",
        "live_cut": "In-room: install desktop skill pack OR create skill + wire MCP (steps 1–4)",
        "resource": "workshop-app/HERMES-DESKTOP-SETUP.md + AGENT-BUILD-GUIDE.md",
        "app": "Agent Build Lab — steps 5–6 + verification checklist",
    },
    {
        "title": "API setup & curl deep dive",
        "time": "30–45 min",
        "live_cut": "Live: Full Demo Chain only — no individual curl",
        "resource": "you-com-api-demo-video-runbook.md",
        "app": "Learn More on API steps + API Implementation Path in tutorial",
    },
    {
        "title": "Connector map & review gates",
        "time": "20 min",
        "live_cut": "Live: defaults + 60-second review states",
        "resource": "audience-workflow-building-tutorial.md (Steps 10–11)",
        "app": "Learn More drill-downs on Govern steps",
    },
    {
        "title": "Source scoring & inspection",
        "time": "15 min",
        "live_cut": "Live: facilitator demos one source score",
        "resource": "audience-workflow-building-tutorial.md (Step 6)",
        "app": "Source Scoring panel (full track only)",
    },
    {
        "title": "Test three accounts + quality scorecard",
        "time": "30 min",
        "live_cut": "Live: mention only — do not run three accounts in room",
        "resource": "audience-workflow-building-tutorial.md (Steps 14–15)",
        "app": "Full track steps 15–16",
    },
    {
        "title": "Team rollout plan (champions only)",
        "time": "20 min async — after Week 1",
        "audience": "RevOps / GTM leads pitching a small team pilot",
        "live_cut": "Live: mention only — 'Download rollout template if you're taking this to your team'",
        "resource": "workshop-app/POST-EVENT-LEARNING.md + full track step 16",
        "app": "Team Rollout Plan step (?full=1) or Download All → pilot-plan.md",
    },
    {
        "title": "Stay in the You.com Discord",
        "time": "Ongoing",
        "audience": "All attendees",
        "live_cut": "Live: join Discord + intro post template on wrap-up step",
        "resource": "https://discord.gg/2C4WgryxSD + COMMUNITY-CONTINUATION.md",
        "app": "Community Continuation panel — copy intro, Week 1 challenge",
    },
    {
        "title": "Full 90-minute self-paced track",
        "time": "90 min",
        "live_cut": "All 18 steps with exercises — for facilitators and champions",
        "resource": "audience-workflow-building-tutorial.md",
        "app": "Open app with ?full=1",
    },
]


def get_post_event_payload() -> dict[str, Any]:
    return {
        "headline": "After the event — go deeper here",
        "summary": (
            "The 60-minute workshop covers the full story end-to-end. Depth, exercises, and "
            "finishing steps live in these resources — not in the room."
        ),
        "paths": POST_EVENT_PATHS,
        "downloads": [
            "Hermes Desktop Skill Pack (.zip)",
            "Agent Build Kit",
            "Workflow Card",
            "Community Playbook",
            "Account Action Brief",
            "Hermes Packaging Prompt",
            "Team Rollout Template (champions — optional)",
        ],
        "default_path": "Join You.com Discord → introduce yourself (from this workshop) → finish agent → 3 briefs (Week 1)",
        "champion_path": "After Week 1: calendar-triggered meeting prep (CALENDAR-MEETING-PREP.md) or team rollout template",
    }
