# Hermes Workflow Studio Execution Playbook

## Goal

Run a public Hermes-led workshop series that shows how to build, connect, govern, package, and pilot a reusable AI workflow.

The flagship workflow is `/account-action-brief`: a governed account workflow that uses You.com for live web intelligence, Hermes for orchestration and reusable workflow packaging, NemoClaw for risk and approved-language review, and GTM systems for context and handoff.

## What Success Looks Like

By the end of the workshop, attendees should understand that Hermes is not just a place to run prompts. It is the layer that turns a useful AI task into a governed, reusable, tool-connected workflow.

Success outcomes:
- Attendees can explain the Hermes workflow lifecycle: run, integrate, govern, package, and pilot.
- Attendees leave with a workflow card they can adapt.
- High-intent attendees identify one workflow to pilot.
- Follow-up conversations focus on API/MCP access, connector setup, and pilot planning.

## Recommended Format

Preferred format:
Four-part public workshop series.

Fallback format:
Two-session version.

Two-session version:
- Session 1: Build and connect the workflow.
- Session 2: Govern, package, and pilot the workflow.

## Required Assets

Content assets:
- Event page and registration copy
- Slide deck
- Workflow card template
- Connector map template
- Governance checklist
- NemoClaw review checklist
- Two-week pilot plan template
- Follow-up email template
- Audience workflow-building tutorial
- You.com API demo video runbook

Demo assets:
- Demo account: ServiceNow
- Public-source account brief prompt
- You.com Search, Contents, and Research examples
- You.com API demo commands for Web Search, Contents, Research, and optional Finance Research
- Saved JSON responses for API demo fallback
- Sample CRM context
- Sample approved messaging doc
- Sample Slack review request
- Sample CRM update draft
- Sample outreach draft

## Roles

Host:
Sets context, introduces the series, manages questions, and closes with the CTA.

Hermes lead:
Shows workflow creation, tool orchestration, governance setup, and packaging.

You.com lead:
Explains Search, Contents, Research, MCP, citations, freshness, and source inspection.

NemoClaw lead:
Explains review rules, approved language, risky claims, and human-review gates.

Facilitator:
Collects attendee questions, watches timing, captures pilot interest, and routes follow-ups.

## Pre-Workshop Steps

### 1. Finalize the public promise

Use this promise:
Build a reusable Hermes workflow that uses You.com for live web intelligence, connects to your GTM stack, routes risky claims through NemoClaw, and ends with a two-week production pilot plan.

### 2. Create registration flow

Registration questions:
- Which workflow do you want to make reusable?
- Which systems do you use today?
- Is the workflow internal-only or external-facing?
- Who owns approval or governance?
- What would make a two-week pilot successful?

### 3. Prepare the demo path

Use one flagship workflow:
`/account-action-brief`

Demo flow:
- Start with ServiceNow as the account.
- Use You.com to gather current public context.
- Add sample CRM and internal context.
- Produce an internal account brief and external-ready outreach draft.
- Run NemoClaw review.
- Create Slack review request and CRM update draft.
- Package the workflow into a Hermes skill or playbook.

### 4. Prepare templates

Templates to include:
- Workflow card
- Connector map
- Governance checklist
- Review states
- Quality scorecard
- Two-week pilot plan

### 5. Prepare follow-up motion

Segment attendees after the event:
- Wants account intelligence workflow
- Wants trusted answer product
- Wants support copilot
- Wants competitive intelligence
- Wants renewal or expansion prep
- Wants partner brief workflow

## Live Workshop Agenda

### Opening

Set the frame:
Most AI demos stop at an answer. Real teams need workflows that can be reused, governed, reviewed, and piloted.

Introduce the layers:
- You.com: live web intelligence
- Hermes: reusable workflow orchestration
- NemoClaw: review and governance
- GTM tools: context and handoff

### Part 1: Build the first Hermes workflow

Show:
- Workflow command
- Inputs
- Output schema
- Source requirements
- First account brief
- API path: Web Search discovers candidate sources, Contents reads selected URLs, Research synthesizes the strategic answer, and optional Finance Research adds public-company financial context

Artifact:
Workflow card.

### API demo insert: Show You.com APIs in action

Run this as a five- to seven-minute demo before or during Part 1.

Show:
- Web Search API returning structured web and news results.
- Domain control with `include_domains`, `exclude_domains`, or `boost_domains`.
- Contents API retrieving clean Markdown and metadata from selected URLs.
- Research API producing a citation-backed synthesis.
- Structured Research output that maps into a workflow card.
- Optional Finance Research API for public-company financial context.
- Hermes receiving the API evidence and turning it into `/account-action-brief`.

Artifact:
API demo video runbook.

### Part 2: Connect the GTM stack

Show:
- CRM context
- Docs and approved messaging
- Meeting or support signals
- Slack/Teams review handoff
- Outreach draft

Artifact:
Connector map.

### Part 3: Govern the workflow

Show:
- Allowed tools
- Restricted data
- Review rules
- NemoClaw checks
- Approval states

Artifact:
Governance checklist.

### Part 4: Package and pilot

Show:
- Reusable Hermes skill or playbook
- Pilot owner
- Success metrics
- Two-week rollout
- Adjacent use cases

Artifact:
Pilot launch kit.

## Follow-Up Steps

Within 24 hours:
- Send recording, slides, and templates.
- Ask attendees to name one pilot workflow.
- Offer workflow design review.

Within 3 business days:
- Qualify high-intent attendees.
- Identify systems to connect.
- Confirm owner, scope, and review requirements.
- Propose a two-week pilot.

Within 2 weeks:
- Help the team run the pilot.
- Review metrics and failure cases.
- Decide whether to expand, revise, or stop.

## Conversion Metrics

Registration metrics:
- Number of registrants
- Percentage with a named workflow
- Percentage using CRM, docs, support, analytics, or outreach tools

Workshop metrics:
- Attendance rate
- Template downloads
- Questions about API, MCP, governance, or pilots
- Number of pilot workflows named

Follow-up metrics:
- Workflow reviews booked
- Pilot owners identified
- Pilot plans created
- API/MCP conversations started
- Qualified opportunities sourced

## Risks And Mitigations

Risk:
The session feels like a generic integration showcase.

Mitigation:
Lead with the Hermes lifecycle and use one flagship workflow.

Risk:
The demo overpromises automation.

Mitigation:
Keep writebacks and outbound actions draft-only until human approval.

Risk:
NemoClaw capabilities are not fully validated.

Mitigation:
Frame NemoClaw as a review and governance layer until exact product claims are confirmed.

Risk:
Attendees do not know what to do next.

Mitigation:
End with the two-week pilot plan and a workflow design review CTA.

## Final CTA

Bring one repeated workflow your team already runs manually. We will help you map the sources, tools, review rules, and two-week pilot plan needed to make it a reusable Hermes workflow.
