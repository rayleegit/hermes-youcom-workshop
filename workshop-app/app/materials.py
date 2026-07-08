"""Workshop teaching materials: templates, samples, and output schema."""

from __future__ import annotations

OUTPUT_SCHEMA = """# Account Action Brief — Output Schema

Every run of `/account-action-brief` returns these six sections in order.

## 1. Snapshot
- Company, website, industry, size/scale, business model
- Source confidence rating

## 2. Current Signals
- Recent company news and announcements
- Product or strategy updates
- Executive or leadership changes
- Funding, financial, or market signals
- Partnership or ecosystem signals

## 3. Why This Account Might Care
- Likely priorities and pain points
- Possible buying triggers
- Relevant transformation themes

## 4. Suggested Actions
- Recommended next step
- Suggested internal owner
- Suggested outreach angle
- Open questions to resolve

## 5. Claims And Sources
- Claim → Source URL → Date/freshness → Confidence

## 6. Review Notes
- Claims needing human review
- Missing sources, assumptions
- Do not use externally until reviewed
"""

SAMPLE_INTERNAL_CONTEXT = """Internal context (sanitized):
- Account segment: Enterprise
- Relationship stage: Active customer, 3-year contract
- Current opportunity: Platform expansion into HR workflows
- Known initiatives: AI agent pilot in IT department
- Known objections: Security review required for AI features
- Existing products used: ITSM, HR Service Delivery
- Recent meeting notes: Customer asked about AI governance controls for agent deployment
- Approved positioning: "Workflow automation with governance controls"
- Do not use externally: Specific contract values, internal security audit findings
"""

SAMPLE_SLACK_REVIEW = """Subject: Review request — Account action brief for [COMPANY]

Hi team — I ran `/account-action-brief` for [COMPANY] ahead of our [MEETING TYPE] on [DATE].

**Review status:** Draft (needs your eyes before internal use)

Please check:
1. Are factual claims source-backed? (see Claims & Sources section)
2. Any claims that should NOT be used externally?
3. Is the suggested next action reasonable for our account stage?

**Brief attached / linked:** [LINK OR PASTE]

Target: Approved for internal use by [DATE]
Reviewer: @[OWNER]
"""

SAMPLE_CRM_UPDATE = """CRM update draft (do not auto-save — human approval required):

Account: [COMPANY]
Last brief run: [DATE]
Workflow: /account-action-brief

**Key signals:**
- [Signal 1 from brief]
- [Signal 2 from brief]

**Suggested next step:** [From Suggested Actions section]
**Owner:** [From workflow inputs]
**Review status:** Draft

**Sources:** [Top 2-3 URLs from Claims & Sources]
"""

SAMPLE_OUTREACH_DRAFT = """Outreach draft (BLOCKED until Approved for external use):

Subject: [COMPANY] + [RELEVANT THEME from brief]

Hi [NAME],

I noticed [SOURCED SIGNAL — must have URL backing from brief].

[Brief value prop tied to approved positioning — no internal-only details]

Would it make sense to explore [SUGGESTED ACTION]?

Best,
[YOUR NAME]

---
Sources used: [URL 1], [URL 2]
Review status required: Approved for external use
"""

PILOT_PLAN_TEMPLATE = {
    "workflow_owner": "",
    "pilot_users": "5",
    "pilot_accounts": "20",
    "week0_tasks": "Confirm owner, review rules, allowed tools, feedback form",
    "week1_goal": "10 briefs with required human review",
    "week2_goal": "20 briefs with quality scorecard",
    "success_metrics": "Time saved, % claims with strong sources, % briefs used in real workflows",
    "expand_criteria": "Average quality scores 2+ and no recurring unsupported-claim issues",
}

OPENING_SCRIPT = """Welcome to the Account Action Brief Workshop.

Today we're building one workflow — /account-action-brief — that shows how two platforms work together:

You.com provides live, source-grounded web intelligence.
Hermes turns that intelligence into a governed, reusable workflow.

We'll walk the You.com APIs together in the platform playground at you.com/platform —
Search discovers sources, Contents reads them, Research synthesizes with citations.

Then everyone installs Hermes desktop live, defines company and brief goal in the test command,
wires You.com MCP, and runs /account-action-brief.

By the end you'll have a working agent and an invite to the You.com Discord community.
"""

CLOSING_SCRIPT = """Let's close:

You.com answered: what is true and current? — with cited, structured evidence in the playground.
Hermes answered: how does my team use this safely and repeatedly? — with governance and a skill you installed today.

Your next step: join the You.com Discord, introduce yourself, and say you came from this workshop.

See you in the server.
"""
