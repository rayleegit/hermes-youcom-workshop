"""You.com API client with demo-mode fallback for workshop teaching."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import requests

FIXTURES_DIR = Path(__file__).parent / "fixtures"

SEARCH_URL = "https://ydc-index.io/v1/search"
CONTENTS_URL = "https://ydc-index.io/v1/contents"
RESEARCH_URL = "https://api.you.com/v1/research"
FINANCE_RESEARCH_URL = "https://api.you.com/v1/finance_research"


class YouComError(Exception):
    pass


def _api_key() -> str | None:
    return os.environ.get("YDC_API_KEY") or None


def is_demo_mode() -> bool:
    if os.environ.get("DEMO_MODE", "").lower() in ("1", "true", "yes"):
        return True
    return not _api_key()


def _load_fixture(name: str) -> dict[str, Any]:
    path = FIXTURES_DIR / name
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def _normalize_contents(data: Any) -> dict[str, Any]:
    """Live Contents API returns a list; fixtures use {\"results\": [...]}."""
    if isinstance(data, list):
        return {"results": data}
    if isinstance(data, dict):
        if "results" in data or "pages" in data:
            if "results" not in data and "pages" in data:
                return {"results": data["pages"], **{k: v for k, v in data.items() if k != "pages"}}
            return data
    return {"results": []}


def _headers() -> dict[str, str]:
    key = _api_key()
    if not key:
        raise YouComError("YDC_API_KEY is not set")
    return {"X-API-Key": key, "Content-Type": "application/json"}


def _timeout_seconds(env_key: str, default: int) -> int:
    raw = os.environ.get(env_key, "")
    try:
        return int(raw) if raw else default
    except ValueError:
        return default


def _effective_goal(goal: str | None) -> str:
    if goal and goal.strip():
        return goal.strip()
    return (
        "prepare for a customer conversation with relevant business context "
        "and suggested next actions"
    )


def search(
    company: str,
    *,
    goal: str | None = None,
    count: int = 5,
    freshness: str = "year",
    include_domains: list[str] | None = None,
) -> dict[str, Any]:
    if is_demo_mode():
        data = _load_fixture("search.json")
        data["_demo_mode"] = True
        return data

    focus = _effective_goal(goal)
    query = f"{company} {focus}"
    params: dict[str, Any] = {
        "query": query,
        "count": count,
        "freshness": freshness,
    }
    if include_domains:
        params["include_domains"] = include_domains

    response = requests.get(
        SEARCH_URL,
        headers={"X-API-Key": _api_key() or ""},
        params=params,
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    data["_demo_mode"] = False
    return data


def contents(
    urls: list[str],
    *,
    crawl_timeout: int = 15,
    max_age: int = 86400,
) -> dict[str, Any]:
    if is_demo_mode():
        data = _load_fixture("contents.json")
        data["_demo_mode"] = True
        return data

    response = requests.post(
        CONTENTS_URL,
        headers=_headers(),
        json={
            "urls": urls,
            "formats": ["markdown", "metadata"],
            "crawl_timeout": crawl_timeout,
            "max_age": max_age,
        },
        timeout=60,
    )
    response.raise_for_status()
    data = _normalize_contents(response.json())
    data["_demo_mode"] = False
    return data


def research(
    company: str,
    *,
    goal: str | None = None,
    effort: str = "standard",
    boost_domains: list[str] | None = None,
    structured: bool = False,
) -> dict[str, Any]:
    if is_demo_mode():
        name = "research_structured.json" if structured else "research.json"
        data = _load_fixture(name)
        data["_demo_mode"] = True
        return data

    focus = _effective_goal(goal)
    question = (
        f"What are the most important recent strategic signals for {company} "
        f"given this goal: {focus}? "
        "What should an account team consider before acting?"
    )
    payload: dict[str, Any] = {
        "input": question,
        "research_effort": effort,
    }
    if boost_domains:
        payload["source_control"] = {
            "freshness": "year",
            "boost_domains": boost_domains,
        }

    if structured:
        payload["input"] = (
            f"Extract the top three recent {company} strategic signals "
            f"relevant to this goal: {focus}."
        )
        payload["output_schema"] = {
            "type": "object",
            "properties": {
                "signals": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "signal": {"type": "string"},
                            "why_it_matters": {"type": "string"},
                            "recommended_action": {"type": "string"},
                        },
                        "required": ["signal", "why_it_matters", "recommended_action"],
                        "additionalProperties": False,
                    },
                }
            },
            "required": ["signals"],
            "additionalProperties": False,
        }

    response = requests.post(
        RESEARCH_URL,
        headers=_headers(),
        json=payload,
        timeout=120,
    )
    response.raise_for_status()
    data = response.json()
    data["_demo_mode"] = False
    return data


def finance_research(company: str, *, goal: str | None = None, effort: str = "deep") -> dict[str, Any]:
    if is_demo_mode():
        data = _load_fixture("finance_research.json")
        data["_demo_mode"] = True
        return data

    # Finance Research accepts only deep | exhaustive (not standard — that is Research API).
    if effort not in ("deep", "exhaustive"):
        effort = "deep"

    focus = _effective_goal(goal)
    # Keep the question focused — long prompts slow Finance Research further.
    question = (
        f"What are the key recent financial signals for {company} "
        f"(earnings, revenue drivers, analyst outlook) for: {focus}?"
    )
    timeout = _timeout_seconds("FINANCE_RESEARCH_TIMEOUT", 300)
    payload = {"input": question, "research_effort": effort}
    last_timeout: requests.exceptions.Timeout | None = None

    for attempt in range(2):
        try:
            response = requests.post(
                FINANCE_RESEARCH_URL,
                headers=_headers(),
                json=payload,
                timeout=timeout,
            )
            if response.status_code == 422:
                detail = response.text[:200]
                raise YouComError(
                    "Finance Research rejected the request (422). "
                    "Use research_effort 'deep' or 'exhaustive' only. "
                    f"API said: {detail}"
                )
            response.raise_for_status()
            data = response.json()
            data["_demo_mode"] = False
            return data
        except requests.exceptions.Timeout as exc:
            last_timeout = exc
            if attempt == 0:
                continue
            raise YouComError(
                f"Finance Research timed out after {timeout}s (tried twice). "
                "This API often takes 2–5 minutes — use **Run Finance Research (Optional)** "
                "and wait, or set FINANCE_RESEARCH_TIMEOUT higher in .env."
            ) from exc

    if last_timeout:
        raise YouComError(
            f"Finance Research timed out after {timeout}s. "
            "Try again with **Run Finance Research (Optional)**."
        ) from last_timeout
    raise YouComError("Finance Research failed unexpectedly.")


def extract_urls(search_results: dict[str, Any], limit: int = 3) -> list[str]:
    urls: list[str] = []
    results = search_results.get("results", {})
    for bucket in ("web", "news"):
        for item in results.get(bucket, []):
            url = item.get("url")
            if url and url not in urls:
                urls.append(url)
            if len(urls) >= limit:
                return urls
    return urls


def summarize_search(search_results: dict[str, Any]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    results = search_results.get("results", {})
    for bucket in ("web", "news"):
        for item in results.get(bucket, []):
            items.append(
                {
                    "type": bucket,
                    "title": item.get("title", ""),
                    "url": item.get("url", ""),
                    "snippet": item.get("description") or item.get("snippets", [""])[0]
                    if isinstance(item.get("snippets"), list)
                    else item.get("description", ""),
                    "page_age": item.get("page_age", ""),
                }
            )
    return items
