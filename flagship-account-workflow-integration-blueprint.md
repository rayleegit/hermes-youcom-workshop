# Flagship Integration Blueprint

## Use Case

Name: Account-to-Approved-Outreach Workflow

Workflow command: `/account-action-brief`

Core promise:
Turn one target account into a source-backed brief, approved outreach angle, CRM-ready update, Slack review request, and two-week pilot workflow.

Why this should be the flagship:
- It has a direct revenue story.
- It is easy for public attendees to understand.
- It shows You.com as the live web intelligence layer.
- It demonstrates why one-off AI answers are not enough.
- It creates a natural sales conversion path: attendees can pilot the workflow with their own CRM, docs, and review rules.

Public demo account:
ServiceNow.

Primary attendee:
GTM, RevOps, sales engineering, partnerships, customer success, AI platform, legal/compliance, and developer-relations teams.

## Integration Story

The workshop should not look like a tool zoo. Present the integrations as one workflow with four layers:

1. Live external context:
You.com searches, reads, and synthesizes current web context.

2. Internal operating context:
CRM, docs, meeting notes, support data, and product signals add what the public web does not know.

3. Governance and review:
NemoClaw checks claims, approved language, sensitive topics, and high-risk actions.

4. Action handoff:
Slack or Teams requests review, CRM stores the brief, and outreach tools hold the human-approved draft.

## Detailed Workflow

### 1. Trigger

Pick one trigger for the live demo:
- New target account added to CRM.
- Account owner asks for a meeting prep brief.
- Open opportunity moves to discovery or evaluation.
- Strategic account has new public AI, product, funding, regulatory, or executive news.

Recommended demo trigger:
Account owner asks: `Create an account-action brief for ServiceNow for a first executive meeting.`

### 2. CRM intake

Example tools:
Salesforce, HubSpot.

Inputs:
- Account name
- Website
- Industry
- Region
- Account owner
- Opportunity stage
- Existing product interest
- Last activity date
- Known contacts
- Open next step

Output into workflow:
- Account identity
- Sales context
- Known internal assumptions
- Fields eligible for writeback

Governance:
- Read account and opportunity context.
- Do not write back automatically during the demo.
- Prepare a draft CRM update for human approval.

### 3. You.com external intelligence

Example tools:
You.com Search, Contents, Research, MCP.

Search questions:
- What has ServiceNow announced recently about AI, agents, workflows, partnerships, or enterprise automation?
- What are the most relevant product and strategic themes from official sources?
- What recent news or investor context changes the account angle?
- Which sources are fresh enough to use in an account brief?

Use Search for:
- Recent news
- Official pages
- Executive announcements
- Partner announcements
- Investor and public-company context

Use Contents for:
- Reading top source pages in detail.
- Extracting clean source context from official URLs.
- Pulling exact supporting context for claims.

Use Research for:
- Synthesizing broader strategic context.
- Comparing multiple sources.
- Producing a deeper brief when Search snippets are not enough.

Output:
- Source list
- Freshness notes
- Supported claims
- Open questions
- Suggested buying triggers

### 4. Internal docs and approved knowledge

Example tools:
Google Drive, Notion, Confluence.

Inputs:
- Approved product messaging
- Sales playbooks
- Case studies
- Security and compliance language
- Partner positioning
- Competitive guidance
- Customer proof points approved for external use

Output:
- Approved language options
- Relevant proof points
- Disallowed claims
- Playbook-matched talk track

Governance:
- Use only approved docs for external language.
- Mark unapproved internal notes as internal-only.

### 5. Meeting intelligence

Example tools:
Gong, Fireflies, Granola, Otter.

Inputs:
- Recent call summaries
- Objections
- Buying committee notes
- Stakeholder priorities
- Mentioned competitors
- Next steps from prior meetings

Output:
- Account-specific priorities
- Current objections
- Stakeholder map
- Follow-up commitments

Governance:
- Use call notes internally.
- Do not quote customers externally unless explicitly approved.

### 6. Support and product signals

Example tools:
Zendesk, Intercom, BigQuery, Snowflake, Amplitude, PostHog.

Inputs:
- Recent support themes
- Open issues
- Feature usage signals
- Product adoption indicators
- Segment or firmographic signals

Output:
- Customer pain themes
- Adoption context
- Expansion or risk signals
- Product-led talk track

Governance:
- Keep sensitive usage or support details internal.
- Use aggregate trends for external messaging when allowed.

### 7. Hermes synthesis

Hermes produces two outputs.

Internal brief:
- Account snapshot
- Recent strategic updates
- Buying triggers
- Stakeholder context
- Product or workflow fit
- Risks and open questions
- Suggested next action
- Source list
- Internal-only notes

External-ready draft:
- Short outreach angle
- Three approved bullets
- Suggested meeting opener
- Questions to ask
- Claims with source support
- Claims requiring review

### 8. NemoClaw review

NemoClaw reviews before anything leaves the internal workflow.

Review checks:
- Unsupported claims
- Comparative or competitive claims
- Regulated-industry language
- Privacy, security, compliance, or procurement claims
- Customer-sensitive internal information
- Approved-language match
- Tool action risk
- Human-review requirement

Output:
- Safe for internal use: yes/no
- Safe for external use: yes/no
- Required edits
- Approved replacement language
- Tool/action restrictions
- Human review required: yes/no

### 9. Review handoff

Example tools:
Slack, Microsoft Teams.

Review message:

`ServiceNow account-action brief is ready for review.`

Include:
- Internal brief link or summary
- External-ready draft
- NemoClaw risk status
- Claims needing review
- Proposed CRM update
- Approve/edit/reject options

Governance:
- Reviewers approve before CRM writeback or outbound use.
- Keep a lightweight review log for the pilot.

### 10. Action systems

Example tools:
Salesforce, HubSpot, Outreach, Salesloft, Gmail, Linear, Jira, GitHub.

CRM draft update:
- Brief summary
- Buying trigger
- Suggested next action
- Owner
- Follow-up date
- Source-backed notes
- Review status

Outreach draft:
- Approved email or LinkedIn opener
- Source-supported reason for reaching out
- Human-editable next step

Project tracker task:
- Workflow gap
- Missing source
- Policy update needed
- Connector issue
- Follow-up owner

Governance:
- Draft actions first.
- Human approves external send and CRM writeback during the pilot.

## Output Schema

Use this as the demo output contract.

```yaml
workflow_name: account-action-brief
account:
  name:
  website:
  crm_owner:
  opportunity_stage:
external_context:
  company_snapshot:
  recent_updates:
  buying_triggers:
  sources:
internal_context:
  approved_messages:
  meeting_themes:
  support_or_product_signals:
recommended_action:
  internal_next_step:
  external_outreach_angle:
  suggested_questions:
governance:
  nemo_claw_internal_status:
  nemo_claw_external_status:
  unsupported_claims:
  required_edits:
  human_review_required:
handoff:
  slack_review_message:
  crm_update_draft:
  outreach_draft:
  follow_up_tasks:
```

## Demo Script

Opening:
Most teams do not need another chat answer. They need a workflow that starts with live web intelligence, adds internal context, checks risk, and hands off a next action.

Step 1:
Start from ServiceNow in CRM.

Step 2:
Run `/account-action-brief`.

Step 3:
Show You.com gathering current public context and sources.

Step 4:
Show internal docs, meeting notes, support, or product signals as optional enrichments.

Step 5:
Show Hermes producing internal and external outputs.

Step 6:
Show NemoClaw reviewing claims and approved language.

Step 7:
Show the Slack review request and draft CRM update.

Close:
The goal is not to automate judgment away. The goal is to make the work repeatable, sourced, reviewed, and ready for a two-week pilot.

## Two-Week Pilot

Week 0 setup:
- Pick 5 account owners.
- Pick 20 target accounts.
- Connect CRM read access.
- Identify approved messaging docs.
- Define NemoClaw review rules.
- Decide which actions are draft-only.

Week 1:
- Run 10 account-action briefs.
- Require human review before external use.
- Track time saved and correction rate.
- Log unsupported claims and missing sources.

Week 2:
- Run 25 account-action briefs.
- Add CRM draft writeback.
- Add Slack review workflow.
- Compare reviewed drafts against rep-created drafts.
- Decide whether to expand to another team.

Success metrics:
- Time saved per brief
- Percentage of claims with sources
- Number of NemoClaw flags resolved
- Review turnaround time
- CRM update acceptance rate
- Outreach draft usage rate
- Pilot users who want to keep using the workflow

## Conversion Hook

End the workshop with this ask:

Pick one account workflow you already run manually. We will help you map the tools, sources, review rules, and two-week pilot plan.

High-intent attendee signals:
- They can name the workflow.
- They can name the account owner or team.
- They have CRM plus docs or meeting data.
- They need source-backed current research.
- They need governance before external use.
- They have a two-week pilot window.
