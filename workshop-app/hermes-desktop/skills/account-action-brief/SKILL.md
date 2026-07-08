---
name: account-action-brief
description: Source-backed account brief via You.com Search, Contents, Research
version: 1.0.0
metadata:
  hermes:
    tags: [youcom, sales, account-research, workshop]
    category: youcom-workshop
    requires_toolsets: [web]
---

# Account Action Brief

## When to Use

Use when preparing for a customer meeting, account review, QBR, outbound sequence, or partner call — and you need a **current, source-backed** brief with suggested next actions.

Trigger examples:
- `/account-action-brief company: AMD`
- "Create an account action brief for Acme Corp before tomorrow's call"
- Calendar: upcoming customer meeting in 24h → auto-prep brief (see `references/calendar-trigger.md`)

## Required Inputs

- **company_name** (required)
- **company_url** (optional)
- **workflow_goal** (optional — brief focus; tailors Search and Research queries)
- **internal_context** (optional, sanitized — never cite as public evidence)
- **output_audience** (optional: `internal` or `external draft`)

## Procedure

1. Confirm company name, optional website, and **brief goal** (what this brief should help the user decide or prepare for).
2. Call **You.com Search** for recent strategic signals (news, product, partnerships) **relevant to the goal**.
3. Select 1–3 high-value URLs; call **You.com Contents** for page-level markdown.
4. Call **You.com Research** when synthesis is needed — frame the question around the stated goal.
5. Optionally call **Finance Research** for public-company financial context.
6. Produce output in the six-section schema — load `references/output-schema.md` if needed.
7. Separate sourced facts from recommendations; label internal-only context.
8. End with **review status: Draft** and recommended next action.

## Output Format

Return these sections in order:

1. Snapshot
2. Current Signals
3. Why This Account Might Care
4. Suggested Actions
5. Claims And Sources (claim → URL → freshness)
6. Review Notes

For schema detail: `skill_view("account-action-brief", "references/output-schema.md")`

## Governance

Load connector and review rules when setting tool permissions:
- `references/connector-map.md`
- `references/review-gates.md`

**Read-only:** You.com APIs, CRM read, internal docs  
**Draft-only:** email, Slack review, CRM update draft  
**Blocked:** auto-send, auto-CRM-update, sensitive data, unapproved legal language

## Pitfalls

- Do not invent facts or URLs — every claim needs a source or "assumption" label.
- Do not treat old sources as current — check freshness metadata.
- Do not mix private internal context into external-facing language.
- Do not auto-send messages or write to CRM unless explicitly approved.

## Verification

- [ ] All six sections present
- [ ] Claims & Sources lists real URLs
- [ ] Review status = Draft
- [ ] No auto-send or CRM write occurred
