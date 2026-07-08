"""FastAPI backend for the Account Action Brief workshop app."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from app.hermes_desktop import (
    build_hermes_desktop_setup_markdown,
    build_skill_pack_zip,
    get_hermes_desktop_payload,
    validate_skill_pack,
)
from app.automation_explainer import get_automation_payload
from app.post_event import get_post_event_payload
from app.community import build_community_playbook_markdown, get_community_payload
from app.agent_build import build_agent_kit_markdown, get_agent_build_payload
from app.brief import build_brief, build_hermes_live_run, build_hermes_prompt, build_workflow_card
from app.deep_dives import get_deep_dives_payload
from app.materials import (
    CLOSING_SCRIPT,
    OPENING_SCRIPT,
    OUTPUT_SCHEMA,
    PILOT_PLAN_TEMPLATE,
    SAMPLE_CRM_UPDATE,
    SAMPLE_INTERNAL_CONTEXT,
    SAMPLE_OUTREACH_DRAFT,
    SAMPLE_SLACK_REVIEW,
)
from app.platform_highlights import (
    API_DECISION_MATRIX,
    HERMES_LIFECYCLE,
    HERMES_STRENGTHS,
    PHASE_PLATFORM_FOCUS,
    QUALITY_SCORECARD,
    REVIEW_STATES,
    WORKSHOP_STORY,
    YOU_COM_PRODUCTS,
    YOU_COM_STRENGTHS,
)
from app.steps import EXPRESS_50, WORKSHOP_STEPS, get_express_steps, get_step
from app.youcom import (
    YouComError,
    contents,
    extract_urls,
    finance_research,
    is_demo_mode,
    research,
    search,
    summarize_search,
)

load_dotenv()

STATIC_DIR = Path(__file__).parent.parent / "static"

app = FastAPI(
    title="Account Action Brief Workshop",
    description="Teach the Hermes + You.com /account-action-brief workflow",
    version="1.0.0",
)

# In-memory session store (one session per facilitator machine is fine for workshops)
_session: dict[str, Any] = {
    "company": "AMD",
    "website": "https://www.amd.com",
    "job": (
        "When I am preparing for a customer meeting, I need a current account brief, "
        "so I can enter the call with relevant business context and suggested next actions."
    ),
    "workflow_goal": (
        "Prepare for an upcoming customer meeting — understand recent strategic signals "
        "and decide what actions the account team should consider."
    ),
    "primary_user": "Account owner or customer-facing team",
    "workflow_owner": "",
    "internal_context": "",
    "connector_map": {
        "read_tools": "You.com Search, Contents, Research, CRM (read-only), internal docs",
        "draft_tools": "Email draft, Slack review request, CRM update draft",
        "blocked": "Sensitive customer data, unapproved legal/compliance language, PII",
    },
    "selected_urls": [],
    "search_results": None,
    "contents_results": None,
    "research_results": None,
    "structured_research": None,
    "finance_research": None,
    "source_scores": {},
    "review_status": "Draft",
    "pilot_plan": dict(PILOT_PLAN_TEMPLATE),
    "demo_mode": is_demo_mode(),
}


class SessionUpdate(BaseModel):
    company: str | None = None
    website: str | None = None
    job: str | None = None
    workflow_goal: str | None = None
    primary_user: str | None = None
    workflow_owner: str | None = None
    internal_context: str | None = None
    read_tools: str | None = None
    draft_tools: str | None = None
    blocked_tools: str | None = None
    selected_urls: list[str] | None = None
    source_scores: dict[str, int] | None = None
    review_status: str | None = None
    pilot_plan: dict[str, str] | None = None


class SearchRequest(BaseModel):
    include_domains: list[str] = Field(default_factory=list)


class ContentsRequest(BaseModel):
    urls: list[str] = Field(default_factory=list)


class ResearchRequest(BaseModel):
    effort: str = "standard"
    boost_domains: list[str] = Field(default_factory=list)


class FullChainRequest(BaseModel):
    include_structured: bool = True
    include_finance: bool = True


@app.get("/api/platform-highlights")
def platform_highlights() -> dict[str, Any]:
    return {
        "story": WORKSHOP_STORY,
        "youcom_strengths": YOU_COM_STRENGTHS,
        "hermes_strengths": HERMES_STRENGTHS,
        "api_decision_matrix": API_DECISION_MATRIX,
        "hermes_lifecycle": HERMES_LIFECYCLE,
        "phase_focus": PHASE_PLATFORM_FOCUS,
        "review_states": REVIEW_STATES,
        "quality_scorecard": QUALITY_SCORECARD,
        "youcom_products": YOU_COM_PRODUCTS,
    }


@app.get("/api/health")
def health() -> dict[str, Any]:
    skill_pack = validate_skill_pack(_session)
    return {
        "status": "ok" if skill_pack["ok"] else "degraded",
        "demo_mode": is_demo_mode(),
        "api_key_set": bool(os.environ.get("YDC_API_KEY")),
        "hermes_desktop_skill_pack": skill_pack,
    }


@app.get("/api/hermes-desktop/preflight")
def hermes_desktop_preflight() -> dict[str, Any]:
    result = validate_skill_pack(_session)
    if not result["ok"]:
        raise HTTPException(status_code=503, detail=result["errors"])
    return result


@app.get("/api/steps")
def list_steps(express: bool = False) -> list[dict[str, Any]]:
    if express:
        return get_express_steps()
    return WORKSHOP_STEPS


@app.get("/api/express-track")
def express_track_info() -> dict[str, Any]:
    return {
        "total_minutes": EXPRESS_50["total_minutes"],
        "label": EXPRESS_50["label"],
        "cuts": EXPRESS_50["cuts"],
        "step_count": len(EXPRESS_50["track"]),
        "post_event_doc": EXPRESS_50.get("post_event_doc", ""),
    }


@app.get("/api/steps/full")
def list_steps_full() -> list[dict[str, Any]]:
    return WORKSHOP_STEPS


@app.get("/api/steps/{step_id}")
def step_detail(step_id: str) -> dict[str, Any]:
    step = get_step(step_id)
    if not step:
        raise HTTPException(status_code=404, detail="Step not found")
    return step


@app.get("/api/session")
def get_session() -> dict[str, Any]:
    return {**_session, "demo_mode": is_demo_mode()}


@app.patch("/api/session")
def update_session(body: SessionUpdate) -> dict[str, Any]:
    for field in ("company", "website", "job", "workflow_goal", "primary_user", "workflow_owner", "internal_context", "selected_urls", "source_scores", "review_status"):
        value = getattr(body, field, None)
        if value is not None:
            _session[field] = value
    if body.pilot_plan is not None:
        _session["pilot_plan"].update(body.pilot_plan)
    if body.read_tools is not None:
        _session["connector_map"]["read_tools"] = body.read_tools
    if body.draft_tools is not None:
        _session["connector_map"]["draft_tools"] = body.draft_tools
    if body.blocked_tools is not None:
        _session["connector_map"]["blocked"] = body.blocked_tools
    _session["demo_mode"] = is_demo_mode()
    return _session


@app.post("/api/run/search")
def run_search(body: SearchRequest | None = None) -> dict[str, Any]:
    body = body or SearchRequest()
    company = _session["company"]
    goal = _session.get("workflow_goal")
    try:
        result = search(company, goal=goal, include_domains=body.include_domains or None)
        _session["search_results"] = result
        urls = extract_urls(result)
        _session["selected_urls"] = urls
        return {
            "results": result,
            "summary": summarize_search(result),
            "suggested_urls": urls,
            "demo_mode": result.get("_demo_mode", False),
        }
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/api/run/contents")
def run_contents(body: ContentsRequest | None = None) -> dict[str, Any]:
    body = body or ContentsRequest()
    urls = body.urls or _session.get("selected_urls") or []
    if not urls:
        raise HTTPException(status_code=400, detail="No URLs selected. Run Search first.")
    try:
        result = contents(urls[:3])
        _session["contents_results"] = result
        return {"results": result, "demo_mode": result.get("_demo_mode", False)}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/api/run/research")
def run_research(body: ResearchRequest | None = None) -> dict[str, Any]:
    body = body or ResearchRequest()
    company = _session["company"]
    goal = _session.get("workflow_goal")
    domain = _session.get("website", "").replace("https://", "").replace("http://", "").split("/")[0]
    boost = body.boost_domains or ([domain] if domain else [])
    try:
        result = research(company, goal=goal, effort=body.effort, boost_domains=boost or None)
        _session["research_results"] = result
        return {"results": result, "demo_mode": result.get("_demo_mode", False)}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/api/run/research-structured")
def run_research_structured() -> dict[str, Any]:
    company = _session["company"]
    goal = _session.get("workflow_goal")
    try:
        result = research(company, goal=goal, structured=True)
        _session["structured_research"] = result
        return {"results": result, "demo_mode": result.get("_demo_mode", False)}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@app.post("/api/run/finance-research")
def run_finance_research() -> dict[str, Any]:
    company = _session["company"]
    goal = _session.get("workflow_goal")
    try:
        result = finance_research(company, goal=goal)
        _session["finance_research"] = result
        return {"results": result, "demo_mode": result.get("_demo_mode", False)}
    except YouComError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
def post_event_learning() -> dict[str, Any]:
    return get_post_event_payload()


@app.get("/api/automation")
def automation_explainer() -> dict[str, Any]:
    return get_automation_payload()


@app.get("/api/community")
def community_info() -> dict[str, Any]:
    return get_community_payload()


@app.get("/api/hermes-desktop")
def hermes_desktop_info() -> dict[str, Any]:
    return get_hermes_desktop_payload(_session)


@app.get("/api/hermes-desktop/download")
def hermes_desktop_download() -> Response:
    company = _session.get("company", "workshop")
    slug = company.lower().replace(" ", "-")
    return Response(
        content=build_skill_pack_zip(_session),
        media_type="application/zip",
        headers={
            "Content-Disposition": f'attachment; filename="{slug}-hermes-skill-pack.zip"'
        },
    )


@app.get("/api/agent-build")
def get_agent_build() -> dict[str, Any]:
    _session["demo_mode"] = is_demo_mode()
    return get_agent_build_payload(_session)


@app.get("/api/deep-dives")
def deep_dives() -> dict[str, Any]:
    return get_deep_dives_payload()


@app.get("/api/materials")
def get_materials() -> dict[str, Any]:
    return {
        "output_schema": OUTPUT_SCHEMA,
        "sample_internal_context": SAMPLE_INTERNAL_CONTEXT,
        "sample_slack_review": SAMPLE_SLACK_REVIEW,
        "sample_crm_update": SAMPLE_CRM_UPDATE,
        "sample_outreach_draft": SAMPLE_OUTREACH_DRAFT,
        "opening_script": OPENING_SCRIPT,
        "closing_script": CLOSING_SCRIPT,
        "pilot_plan_template": PILOT_PLAN_TEMPLATE,
    }


@app.post("/api/run/full-chain")
def run_full_chain(body: FullChainRequest | None = None) -> dict[str, Any]:
    """Run all You.com APIs in sequence: Search → Contents → Research → Structured → Finance."""
    body = body or FullChainRequest()
    company = _session["company"]
    goal = _session.get("workflow_goal")
    steps_run: list[str] = []
    skipped: list[str] = []
    notes: list[str] = []
    try:
        search_result = search(company, goal=goal)
        _session["search_results"] = search_result
        urls = extract_urls(search_result)
        _session["selected_urls"] = urls
        steps_run.append("search")

        contents_result: dict[str, Any] | None = None
        if urls:
            try:
                contents_result = contents(urls[:3])
                _session["contents_results"] = contents_result
                steps_run.append("contents")
            except Exception as exc:
                skipped.append(f"contents — {exc}")

        domain = _session.get("website", "").replace("https://", "").replace("http://", "").split("/")[0]
        boost = [domain] if domain else []

        research_result: dict[str, Any] | None = None
        research_preview = ""
        try:
            research_result = research(company, goal=goal, boost_domains=boost or None)
            _session["research_results"] = research_result
            steps_run.append("research")
            research_preview = _preview_output(research_result)
        except Exception as exc:
            skipped.append(f"research — {exc}")
            research_preview = f"(skipped — {exc})"

        structured_preview = ""
        if body.include_structured:
            try:
                structured_result = research(company, goal=goal, structured=True)
                _session["structured_research"] = structured_result
                steps_run.append("research_structured")
                structured_preview = _preview_output(structured_result)
            except Exception as exc:
                skipped.append(f"research_structured — {exc}")
                structured_preview = f"(skipped — {exc})"
        else:
            structured_preview = (
                "Skipped in 60-min chain (saves ~1–2 min). "
                "Use ?full=1 or run Structured Research separately."
            )
            notes.append("structured_research omitted for 60-min timing")

        finance_preview = ""
        if body.include_finance:
            try:
                finance_result = finance_research(company, goal=goal, effort="deep")
                _session["finance_research"] = finance_result
                steps_run.append("finance_research")
                finance_preview = _preview_output(finance_result)
            except Exception as exc:
                skipped.append(f"finance_research — {exc}")
                finance_preview = f"(skipped — {exc})"
        else:
            finance_preview = (
                "Skipped in 60-min chain — Finance Research often takes 2–5 minutes. "
                "Click **Run Finance Research (Optional)** below and wait."
            )
            notes.append("finance_research omitted for 60-min timing")

        return {
            "status": "ok",
            "steps_run": steps_run,
            "skipped": skipped,
            "notes": notes,
            "products_covered": [p["name"] for p in YOU_COM_PRODUCTS if p["id"] != "mcp"],
            "search_summary": summarize_search(search_result),
            "research_preview": research_preview,
            "structured_preview": structured_preview,
            "finance_preview": finance_preview,
            "contents_count": len(contents_result.get("results", [])) if contents_result else 0,
            "demo_mode": search_result.get("_demo_mode", False),
        }
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


def _preview_output(api_result: dict[str, Any], limit: int = 400) -> str:
    output = api_result.get("output", {})
    if not isinstance(output, dict):
        return str(output)[:limit]
    content = output.get("content", "")
    if isinstance(content, str):
        return content[:limit]
    if isinstance(content, (dict, list)):
        return json.dumps(content, indent=2)[:limit]
    return str(content)[:limit]


@app.get("/api/export-all")
def export_all() -> dict[str, str]:
    _session["demo_mode"] = is_demo_mode()
    pilot = _session.get("pilot_plan", {})
    pilot_md = "\n".join(
        f"- **{k.replace('_', ' ').title()}:** {v}" for k, v in pilot.items() if v
    )
    return {
        "brief": build_brief(_session),
        "workflow_card": build_workflow_card(_session),
        "hermes_prompt": build_hermes_prompt(_session),
        "agent_kit": build_agent_kit_markdown(_session),
        "hermes_desktop_setup": build_hermes_desktop_setup_markdown(_session),
        "community_playbook": build_community_playbook_markdown(),
        "pilot_plan": (
            "# Team Rollout Plan (Champions — Optional)\n\n"
            "> **Not required for most attendees.** Default path: join community → finish agent → "
            "run 3 briefs (Week 1). Use this template when pitching a small team pilot to your manager.\n\n"
            + pilot_md
        ),
        "review_status": _session.get("review_status", "Draft"),
    }


@app.get("/api/brief")
def get_brief() -> dict[str, str]:
    _session["demo_mode"] = is_demo_mode()
    return {"markdown": build_brief(_session)}


@app.get("/api/workflow-card")
def get_workflow_card() -> dict[str, str]:
    _session["demo_mode"] = is_demo_mode()
    return {"markdown": build_workflow_card(_session)}


@app.get("/api/hermes-live-run")
def get_hermes_live_run() -> dict[str, str]:
    return build_hermes_live_run(_session)


@app.get("/api/hermes-prompt")
def get_hermes_prompt() -> dict[str, str]:
    return {"prompt": build_hermes_prompt(_session)}


@app.post("/api/session/reset")
def reset_session() -> dict[str, Any]:
    global _session
    _session = {
        "company": "AMD",
        "website": "https://www.amd.com",
        "job": (
            "When I am preparing for a customer meeting, I need a current account brief, "
            "so I can enter the call with relevant business context and suggested next actions."
        ),
        "workflow_goal": (
            "Prepare for an upcoming customer meeting — understand recent strategic signals "
            "and decide what actions the account team should consider."
        ),
        "primary_user": "Account owner or customer-facing team",
        "workflow_owner": "",
        "internal_context": "",
        "connector_map": {
            "read_tools": "You.com Search, Contents, Research, CRM (read-only), internal docs",
            "draft_tools": "Email draft, Slack review request, CRM update draft",
            "blocked": "Sensitive customer data, unapproved legal/compliance language, PII",
        },
        "selected_urls": [],
        "search_results": None,
        "contents_results": None,
        "research_results": None,
        "structured_research": None,
        "finance_research": None,
        "source_scores": {},
        "review_status": "Draft",
        "pilot_plan": dict(PILOT_PLAN_TEMPLATE),
        "demo_mode": is_demo_mode(),
    }
    return _session


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")
