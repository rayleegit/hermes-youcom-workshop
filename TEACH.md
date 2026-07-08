# Teach the Account Action Brief Workshop

**You are ready when `preflight.sh` passes.** Run it now:

```bash
cd workshop-app
./preflight.sh
```

---

## Readiness Checklist

### Must have (you're blocked without these)
- [ ] `./preflight.sh` exits 0 (includes 4-skill Hermes desktop pack)
- [ ] App loads at http://localhost:8080
- [ ] You've read `workshop-app/FACILITATOR-60MIN.md` (60-min live run-of-show)
- [ ] You can explain: "You.com = evidence, Hermes = workflow"
- [ ] You can explain: "App = manual API demo; Hermes agent = same chain automated on `/account-action-brief`"

### Should have (workshop works without, but better with)
- [ ] `YDC_API_KEY` set for live API demo (demo mode works otherwise)
- [ ] **Attendees have Hermes access** for hands-on agent build (Agent Build step)
- [ ] Projector / screen share tested
- [ ] Printed or shared `workshop-app/materials/attendee-handout.md`
- [ ] Slides: import `workshop-app/60-min-workshop-slides.pptx` (see `60-MIN-GOOGLE-SLIDES.md`)

### Nice to have
- [ ] `you-com-api-demo-video-runbook.md` as post-event primer
- [ ] `HERMES-DESKTOP-SETUP.md` shared for attendees using Hermes desktop
- [ ] `COMMUNITY-CONTINUATION.md` — You.com Discord join + intro template

---

## Start Teaching (3 commands)

```bash
cd workshop-app
./preflight.sh    # verify
./run.sh          # start app
```

Open **http://localhost:8080** (60-min track is default). Deep dive: `?full=1`.

| Duration | Guide |
|----------|--------|
| **60 min live** | `FACILITATOR-60MIN.md` + app default track |
| **90 min deep dive** | `FACILITATOR.md` + `?full=1` |
| **After the event** | `POST-EVENT-LEARNING.md` |

---

## 60-Minute Walkthrough (8 app steps)

| # | App step | Key action |
|---|----------|------------|
| 1 | Welcome | Platform Spotlight + post-event panel |
| 2 | Define | Company → Save; flash schema |
| 3 | API Map | Search → Contents → Research → MCP |
| 4 | Full Demo Chain | Run live; say "Hermes automates this same chain" |
| 5 | Govern | Connector defaults + Draft status |
| 6 | Workflow Card | Generate → Download |
| 7 | Agent Build | Install skill pack (4 skills) + wire MCP (steps 1–4 live) |
| 8 | Wrap-up | Join [You.com Discord](https://discord.gg/2C4WgryxSD), intro post, Week 1: 3 briefs |

**Say at Full Demo Chain:** "We run APIs manually here so you see each step. In Hermes, `/account-action-brief` runs this chain automatically — you review the Draft."

**Say at close:** "Join Discord, introduce yourself from this workshop, run three briefs. Week 2+: try `/meeting-prep` for calendar-triggered briefs."

---

## What You Teach

| Platform | What attendees learn |
|----------|---------------------|
| **You.com** | Search → Contents → Research chain, citations, MCP |
| **Hermes** | Skill pack install, automation loop, connector map, review gates |
| **Together** | Governed briefs — manual demo today, automated agent after |

---

## Files to Know

| File | Purpose |
|------|---------|
| `FACILITATOR-60MIN.md` | **Primary** 60-minute facilitator script |
| `60-min-workshop-slides.pptx` | Google Slides import (optional framing) |
| `60-MIN-GOOGLE-SLIDES.md` | Slide-to-app mapping |
| `HERMES-DESKTOP-SETUP.md` | 4 skills: account-action-brief, meeting-prep, community-pulse, workshop-60min |
| `COMMUNITY-CONTINUATION.md` | You.com Discord + intro template |
| `CALENDAR-MEETING-PREP.md` | Week 2+ `/meeting-prep` pattern |
| `POST-EVENT-LEARNING.md` | All deferred depth |
| `materials/attendee-handout.md` | Give to attendees |
| `audience-workflow-building-tutorial.md` | Full 17-step tutorial (take-home; deeper than 60-min) |

---

## 90-Second Dry Run (60-min track)

1. Open http://localhost:8080 → Welcome → Platform Spotlight
2. Define → change company → Save Inputs
3. Full Demo Chain → Run (expand "How Hermes automates this")
4. Agent Build → confirm skill pack panel + 4 skills listed
5. Wrap-up → Community panel → Discord link + intro template → Download All

If those five work, you're ready to teach.

---

## What's NOT in the 60-min room

Deferred to post-event (linked in app Post-Event panel):

- Individual API curl labs
- Source scoring exercise
- Agent build steps 5–6 (finish at home)
- Team rollout template (champions only, Week 2+)
- `/meeting-prep` calendar wiring (Week 2+)
- Full 18-step track (`?full=1`)
