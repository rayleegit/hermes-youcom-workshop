# Workshop Content Starter

## Workshop 1: Hermes + You.com Account-Brief Workflow

### Narrative

Audience: public workshop for product, GTM, solutions, developer-relations, legal/compliance, and AI platform teams.

Placeholder timing: [DATE TBD], [TIME TBD] PT.

The core message: useful enterprise AI workflows need three things at once: real-time external context, reusable workflow design, and clear governance. You.com provides web intelligence through Search, Contents, Research, and MCP access. Hermes turns the repeated work into a governed workflow that teams can reuse. NemoClaw can add a legal, compliance, policy, approved-language, or capability-governance review layer for outputs that may be used externally or in high-stakes decisions.

### 60-minute run of show

0:00-0:05 - Set the goal
- Outcome: a reusable `/account-brief` workflow blueprint.
- Audience promise: non-technical users can run it; admins can govern it; teams can pilot it.

0:05-0:15 - Run the workflow
- Pick one account, prospect, partner, or company.
- Ask Hermes for a source-grounded account brief.
- Use You.com to gather current web context.
- Inspect source quality before trusting the answer.

0:15-0:25 - Teach the non-technical pattern
- Ask for the brief.
- Inspect the sources.
- Refine the output.
- Reuse the workflow.

0:25-0:38 - Admin setup decisions
- Eligible users and groups.
- Allowed You.com tools.
- Whether NemoClaw review is required for external-use briefs, regulated-industry accounts, competitive claims, sensitive outreach language, or tool actions that need tighter governance.
- Credential location and rotation owner.
- Data that must not leave the environment.
- Human review requirements.
- Logging and audit expectations.

0:38-0:48 - Make it reusable
- Turn the proven prompt into a Hermes skill or playbook.
- Define inputs, defaults, allowed source types, output schema, and review checklist.
- Add an optional NemoClaw review step that flags unsupported claims, sensitive wording, external-use risk, tool-permission concerns, and required human review.
- Keep the workflow simple enough for repeated use.

0:48-0:58 - Productionize the pilot
- Fill out the workflow card.
- Pick a two-week pilot cohort.
- Define success metrics and owner.

0:58-1:00 - Close
- Assign follow-up owner.
- Collect pilot participants.

### Demo prompt

Create a source-grounded account brief for `ServiceNow`.

Use current public web sources. Prioritize the company's official site, recent news, product pages, executive announcements, filings if relevant, and credible industry coverage.

Return:
- Company snapshot
- Business model
- Recent strategic updates
- Relevant buying triggers
- Risks or open questions
- Suggested outreach angle
- NemoClaw review status if the brief will be used externally
- Source list with URLs

If the sources do not support a claim, say so.
If NemoClaw flags a claim, outreach angle, or requested tool action as risky, rewrite it with approved safer language or mark it for human review.

### NemoClaw integration module

Use this as a 5-minute optional add-on after the first account brief demo.

Goal:
Show how a governed workflow can separate internal research from external-ready messaging.

High-value review checks:
- Unsupported or weakly supported claims
- Competitive or comparative language
- Regulated-industry, privacy, security, or compliance-sensitive claims
- Customer-specific claims that should not leave internal systems
- Outreach language that needs approved wording
- Cases that require human legal, compliance, policy, or capability-governance review

Demo output:
- Safe for internal use: yes/no
- Safe for external use: yes/no
- Required edits
- Approved replacement language
- Tool or action restrictions
- Human review required: yes/no

### Workflow card template

Workflow name: `/account-brief`

Owner:

Primary user:

Trigger:

Inputs:
- Company name
- Account URL
- Region or market
- Customer/prospect/partner status
- Optional CRM notes

Allowed tools:
- You.com Search
- You.com Contents
- You.com Research
- NemoClaw review or approved-language lookup
- Other approved MCP tools

Off-limits data:

Output format:
- Executive summary
- Account facts
- Recent events
- Buyer context
- Recommended next action
- Source list

Review rules:
- Human review required before external use.
- Claims must be source-supported.
- NemoClaw review required for regulated industries, competitive claims, privacy/security statements, contract/procurement claims, externally sent outreach, or high-risk agent actions.
- Sensitive CRM or customer data must not be included unless approved.

Success metrics:
- Time saved per brief
- Source coverage
- User satisfaction
- Number of reused briefs
- Number of briefs requiring correction
- Number of NemoClaw flags resolved before external use

Two-week pilot:
- Week 1: 5 users, 10 briefs, daily issue log.
- Week 2: 10 users, 25 briefs, quality scorecard and admin review.

## Workshop 2: You.com Answers API Trusted Answer Experience

### Narrative

Audience: public workshop for product managers, developers, designers, developer-relations, solution engineers, and trust/governance partners.

Placeholder timing: [DATE TBD], [TIME TBD] PT.

The core message: an answer product is not only an endpoint. It is a user experience with trust decisions. The product must decide what to cite, when to disclose uncertainty, when to ask a follow-up, and when to escalate from a fast answer to deeper research. NemoClaw can strengthen this pattern by classifying legal, compliance, policy, or capability-governance risk and by deciding when fast answers need approved language or human review.

### 60-minute run of show

0:00-0:05 - Set the goal
- Outcome: product pattern for a trusted answer experience.
- Note: Answers API is treated as upcoming; collect launch feedback explicitly.

0:05-0:15 - Clarify the API landscape
- Search API: structured web and news results.
- Contents API: clean content from known URLs.
- Research API: synthesized answers with sources and configurable research effort.
- Answers API: proposed fast answer layer that needs clear positioning.

0:15-0:30 - Build the answer experience
- User asks a question.
- System returns concise answer.
- Sources are visible and scannable.
- User can ask follow-up questions.
- Product offers a go-deeper path when the question needs more research.

0:30-0:42 - Design for trust
- Citations should support the factual claims they appear near.
- Freshness should be visible when recency matters.
- Uncertainty language should be direct and specific.
- NemoClaw can classify high-stakes questions, flag risky answer language, limit unsafe tool paths, and require escalation for sensitive domains.
- Failure states should say what is missing and what the user can do next.

0:42-0:52 - Evaluate quality
- Use the scorecard below.
- Compare raw search results, fast answers, and deeper research outputs.

0:52-1:00 - Capture launch feedback
- Response format
- Docs and examples
- SDK needs
- Pricing questions
- Demo queries
- Product positioning

### Answer experience pattern

Question:

Fast answer:

Why this answer:

Sources:
- Source title
- Publisher/domain
- Date or freshness signal
- URL
- Key supporting passage summary

Follow-up questions:
- What would you like to compare?
- Do you want the latest news only?
- Should I go deeper and produce a research brief?

Go-deeper path:
- Escalate to Research API when the question is broad, high-stakes, contradictory, or requires synthesis across many sources.
- Escalate to NemoClaw or human review when the answer involves legal, compliance, privacy, contract, regulated-industry, externally actionable claims, or high-risk tool use.

### NemoClaw trust module

Use this as a 5-minute optional add-on after the answer experience pattern.

Goal:
Show that trusted answers need both source grounding and risk-aware product behavior.

Recommended classification:
- Low risk: answer directly with citations.
- Medium risk: answer with uncertainty language, source details, and follow-up questions.
- High risk: escalate to deeper research, approved language, or human review.
- Blocked: refuse to answer as final guidance and explain what review is needed.

Example risk pass output:
- Risk category
- Citation sufficiency
- Freshness requirement
- Approved-language requirement
- Whether a fast answer is acceptable
- Whether to escalate to deeper research
- Whether legal, compliance, or policy review is required

### Demo questions

Use these public-safe demo questions unless a better launch query is available:
- What has ServiceNow recently announced about AI agents?
- What sources support that answer, and how fresh are they?
- What is the difference between raw search results, a fast answer, and a deeper research brief for this question?
- Which claims in the answer would need stronger citation support before being used externally?
- When should this answer escalate to NemoClaw review or deeper You.com Research?

### Quality scorecard

Use a 1-5 score for each criterion.

Correctness:

Citation support:

Risk classification:

Approved-language handling:

Latency:

Freshness:

Formatting:

Uncertainty handling:

Failure handling:

Overall launch readiness:

### Launch feedback questions

- What should the default response object include?
- Should citations be inline, grouped below, or both?
- What examples should appear first in the docs?
- What SDK patterns would reduce time to first useful demo?
- What pricing questions will developers ask immediately?
- Which demo queries best show the difference between search results, fast answers, and deeper research?
- What should the product page say in one sentence?
