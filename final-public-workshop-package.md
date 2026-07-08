# Public Workshop Package

## Assumptions

Audience: public.

Timing: [DATE TBD], [TIME TBD] PT.

**Core story:** You.com = live evidence. Hermes = governed workflow.

Governance: Hermes connector map + review gates (Draft → Approved). Every output starts as Draft; human review before external use.

Demo company for Workshop 1: AMD. Public, enterprise-oriented, enough current sources for a useful account-brief demo.

**Live format:** 60-minute express track (default). Full 90-minute deep dive optional (`?full=1`).

## Workshop 1

Title: Hermes + You.com: Ship a Governed Account-Brief Workflow

Public description:

Join a hands-on workshop on building a governed account-brief workflow that a non-technical user can run, an admin can govern, and a team can reuse in production.

We use You.com for current, source-grounded web intelligence and Hermes to turn repeated prep work into a reusable `/account-action-brief` workflow. You see each API manually in the workshop app; in Hermes the same chain runs automatically — you review the Draft.

Attendees leave with:

- A working Hermes skill (4-skill desktop pack or Studio path)
- A workflow card (owner, trigger, inputs, output format, allowed tools, review rules)
- You.com Discord community access + Week 1 challenge (3 briefs)
- Optional champion path: two-week pilot rollout template

Best-fit audience:

- GTM, sales, customer success, partnerships, and marketing teams
- Product and solutions teams building governed AI workflows
- AI platform, operations, and admin teams

What it covers (60 min live):

- Run a source-grounded account brief for AMD using You.com Search → Contents → Research
- Inspect sources before trusting the output
- Govern with connector map defaults and Draft review gates
- Install Hermes desktop skill pack (4 skills) and wire You.com MCP
- Join You.com Discord; Week 1: run 3 briefs

What it covers (after the event):

- Finish agent build (`AGENT-BUILD-GUIDE.md`)
- Full 17-step written tutorial (`audience-workflow-building-tutorial.md`)
- `/meeting-prep` for calendar-triggered briefs (Week 2+)
- Champions: two-week pilot plan (Step 16)

Demo flow:

- Manual: Full Demo Chain in workshop app — each You.com API visible
- Automated: `/account-action-brief` in Hermes — same chain via MCP
- Produce structured brief: snapshot, signals, why they care, actions, claims + sources, review notes
- Human review before external use; weak claims → Review Notes
- Package as workflow card + reusable Hermes skill

Review output (Hermes governance):

- Status: Draft / Approved / Needs revision / Blocked
- Unsupported or weak claims flagged
- Internal-only context labeled
- External-use requires human approval

## Workshop 2

Title: You.com Answers API: Build a Trusted Answer Experience

Public description:

This workshop focuses on the product pattern behind a trusted answer experience: how a user question becomes a fast, concise, source-backed answer with follow-up questions and a clear path to deeper research.

We position the upcoming Answers API relative to You.com's Search, Contents, and Research APIs, then use the session to collect launch feedback on response format, citations, docs, SDK expectations, pricing questions, demo queries, and product positioning.

Hermes review gates apply when answers may be used externally: Draft status, source inspection, escalation to deeper Research.

Best-fit audience:

- Product managers and designers building answer, search, support, research, or assistant experiences
- Developers and solutions teams evaluating You.com APIs
- Developer-relations and GTM teams shaping launch messaging
- Trust, safety, legal, compliance, and AI governance partners

What it covers:

- Clarify the difference between raw search results, fast answers, and deeper research
- Turn a user question into a concise answer with visible sources
- Design citations, freshness signals, uncertainty language, follow-up questions, and escalation paths
- Add review gates for sensitive or externally actionable answers
- Score answer quality across correctness, citation support, latency, freshness, formatting, uncertainty, failure handling, and risk classification

Demo questions:

- What has AMD recently announced about AI agents?
- What sources support that answer, and how fresh are they?
- What is the difference between raw search results, a fast answer, and a deeper research brief for this question?
- Which claims in the answer would need stronger citation support before being used externally?
- When should this answer escalate to deeper You.com Research or human review?

Review pass:

- Low risk: answer directly with citations
- Medium risk: answer with uncertainty language, source details, and follow-up questions
- High risk: escalate to deeper research or human review
- Blocked: do not present the answer as final guidance; explain what review is needed

## Promotion Copy

Short announcement:

We are hosting a public two-part You.com workshop series on building source-grounded, governed AI workflows.

Session 1 covers a reusable Hermes + You.com `/account-action-brief` workflow — manual API demo, automated agent, Discord community, and optional team pilot for champions.

Session 2 covers a trusted answer experience around You.com's upcoming Answers API, including citations, freshness, uncertainty, escalation, and review gates.

Timing: [DATE TBD], [TIME TBD] PT.

CTA: Register to join the public workshop.

## Luma CTA

Primary CTA: Register.

Secondary CTA: Bring a workflow or answer experience you want to make more trustworthy.

## Open Items Before Publishing

- Replace [DATE TBD] and [TIME TBD] PT.
- Add host and speaker names.
- Add final Luma URLs.

## Teaching Package (current)

| Resource | Purpose |
|----------|---------|
| `workshop-app/` + `./run.sh` | Live 60-min app (default) + `?full=1` deep dive |
| `workshop-app/FACILITATOR-60MIN.md` | Facilitator run-of-show |
| `workshop-app/60-min-workshop-slides.pptx` | Primary slide deck (16 slides) |
| `workshop-app/60-MIN-GOOGLE-SLIDES.md` | Import guide for Google Slides |
| `workshop-app/HERMES-DESKTOP-SETUP.md` | 4-skill pack install |
| `workshop-app/COMMUNITY-CONTINUATION.md` | You.com Discord + challenges |
| `workshop-app/CALENDAR-MEETING-PREP.md` | `/meeting-prep` Week 2+ pattern |
| `workshop-app/POST-EVENT-LEARNING.md` | After-event learning paths |
| `audience-workflow-building-tutorial.md` | Full 17-step written tutorial |
| `TEACH.md` | Facilitator readiness checklist |
| `alternate-no-nemoclaw-walkthrough-deck.md` | Deck index — 60-min PPTX primary, legacy 28-slide marked |

Audience tutorial Google Doc:
https://docs.google.com/document/d/1t_KiDWtM7v6A1LDEr2joZqkHwiKqtMW7GXDGE6WFDSk/edit?usp=drivesdk

Use `you-com-api-demo-video-runbook.md` for post-event API curl primer.

API demo video runbook Google Doc:
https://docs.google.com/document/d/17P8T-hZiOReVCFptaYdNGgMGSePsCsRIT0aN_AdH-BM/edit?usp=drivesdk

## Legacy / alternate materials

These retain NemoClaw positioning for historical reference — **not** the primary 60-min walkthrough:

- `hermes-led-multipart-workshop-series.md`
- `hermes-workflow-studio-event-description.md`
- `conversion-focused-workshop-version.md`
- `outputs/hermes-workflow-studio-workshop-deck.pptx` (28 slides)

**Primary walkthrough deck:** `workshop-app/60-min-workshop-slides.pptx`  
**Legacy deck:** https://docs.google.com/presentation/d/1HTaIN4Nt4difkLAdHUbCGjXoAwUlO5wORlufJo_Otno/edit?usp=drivesdk

See `alternate-no-nemoclaw-walkthrough-deck.md` for deck status and walkthrough structure.
