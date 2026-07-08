# Adjacent Use Case Hints

Use these as teaser paths, not full demos. The flagship demo should remain the Account-to-Approved-Outreach workflow.

## 1. Trusted Answer Product

Audience:
Product, engineering, support, developer-relations, and AI governance teams.

Hook:
Fast answers are easy to demo. Trusted answers need sources, freshness, uncertainty language, escalation, and review.

Integration hint:
- You.com answers the public or current-events portion.
- Internal docs provide approved product truth.
- Support tools show what users actually ask.
- Analytics tools show whether the question matters at scale.
- NemoClaw decides when the answer needs approved wording or review.

Takeaway:
Trusted Answer Product Kit.

## 2. Support Answer Copilot

Audience:
Support, success, product operations, and documentation teams.

Hook:
Reduce repetitive support work without letting the assistant invent product behavior.

Integration hint:
- You.com handles current external context and public docs.
- Zendesk or Intercom supplies similar tickets and customer language.
- Google Drive, Notion, or Confluence supplies approved internal docs.
- Linear, Jira, or GitHub creates follow-up tasks for answer gaps.
- NemoClaw flags sensitive customer, policy, or compliance language.

Takeaway:
Support answer workflow with escalation and documentation-gap tracking.

## 3. Competitive Intelligence Brief

Audience:
Product marketing, sales enablement, strategy, and partnerships.

Hook:
Turn current web signals into a source-backed competitive brief that sales can use safely.

Integration hint:
- You.com Search finds recent competitor launches, pricing pages, customer stories, and news.
- You.com Contents reads top competitor pages.
- Internal docs provide approved competitive positioning.
- Slack or Teams routes high-impact claims to product marketing.
- NemoClaw reviews comparative claims before external use.

Takeaway:
Competitive brief template with claim support and approved talk tracks.

## 4. Market or Account Research Desk

Audience:
Strategy, partnerships, business development, and market research teams.

Hook:
Move from ad hoc research requests to reusable research workflows with consistent source quality.

Integration hint:
- You.com Research creates the first synthesized brief.
- Drive or Notion stores canonical research outputs.
- BigQuery or Snowflake adds internal account or segment data.
- Slack or Teams collects stakeholder feedback.
- NemoClaw flags claims that need softer language or review.

Takeaway:
Reusable market-research workflow with source and review standards.

## 5. Renewal or Expansion Prep

Audience:
Customer success, account management, RevOps, and product teams.

Hook:
Combine public account changes, product usage, support themes, and approved messaging before a renewal or expansion conversation.

Integration hint:
- CRM provides renewal date, owner, contacts, and account health.
- You.com finds current company changes and executive priorities.
- Product analytics shows usage and adoption signals.
- Support tools surface open issues and common pain points.
- NemoClaw checks external-facing recommendations.

Takeaway:
Renewal-prep brief with account context, risks, and next best action.

## 6. Partner Brief and Co-Sell Prep

Audience:
Partnerships, alliances, ecosystem, and channel teams.

Hook:
Create partner briefs that combine public context, joint-value messaging, approved proof points, and review-ready outreach.

Integration hint:
- You.com gathers current partner news, ecosystem announcements, and product pages.
- CRM or partner systems provide relationship status and owner.
- Internal docs provide approved co-sell language.
- Slack routes the brief to partner and legal stakeholders.
- NemoClaw reviews claims about the partner or joint offer.

Takeaway:
Partner brief workflow with co-sell angle and governance checks.

## 7. Calendar-Triggered Meeting Prep

Audience:
Account executives, CSMs, SDRs, and anyone with a full customer calendar.

Hook:
You built `/account-action-brief` — the next step is getting the brief **before the meeting** without manual triggers.

Integration hint:
- Calendar read-only (Google Calendar, Outlook) detects upcoming customer meetings.
- Extract company from meeting title, attendees, or CRM link.
- Hermes runs the same You.com evidence chain automatically (24h or 2h before).
- Deliver Draft brief to **you** via Slack DM, email-to-self, or prep doc — never auto-send to attendees.
- Human reviews before the call; connector map blocks calendar write and external email.

Takeaway:
`workshop-app/CALENDAR-MEETING-PREP.md` + `/meeting-prep` skill in desktop pack. Week 2+ community challenge.

## How To Present These Hints

After the flagship demo, use one slide:

Same pattern, different workflow:
- Live external context from You.com
- Internal context from the systems of record
- Reusable orchestration in Hermes
- Review and approved language through NemoClaw
- Human-approved handoff into the tools teams already use

Then show the six use cases as short cards. Do not demo them live unless the flagship workflow finishes early.
