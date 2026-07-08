# Walkthrough Decks — Account Action Brief Workshop

## Primary deck (60-min live — use this)

**Local PPTX:** `workshop-app/60-min-workshop-slides.pptx`  
**Import guide:** `workshop-app/60-MIN-GOOGLE-SLIDES.md`

17 slides aligned to the **60-minute app track** (http://localhost:8080 default):

- Two platforms story, agenda, live vs post-event
- Manual demo vs automated agent
- Full Demo Chain, govern, workflow card, agent build
- Hermes desktop skill pack (4 skills)
- You.com Discord close + facilitator cheatsheet

Regenerate: `cd workshop-app && python build_60min_slides.py`

**The app is the live walkthrough.** Slides frame timing; the app runs APIs and agent build.

---

## Alternate deck (legacy — 28 slides)

Google Slides (older Hermes Workflow Studio tour):
https://docs.google.com/presentation/d/1HTaIN4Nt4difkLAdHUbCGjXoAwUlO5wORlufJo_Otno/edit?usp=drivesdk

**Status:** Legacy reference. Does not include:
- 60-minute condensed track
- Hermes desktop skill pack (4 skills)
- You.com Discord community close
- `/meeting-prep` calendar pattern
- Automation explainer (manual app vs Hermes agent)
- Champions-only rollout (vs required pilot form)

Use for deep-dive context or adjacent workflow hints — not as the primary 60-min walkthrough.

---

## Walkthrough structure (current 60-min)

1. Frame: You.com = evidence, Hermes = governed workflow (not a chatbot demo).
2. **Manual:** Full Demo Chain in the app — attendees see each API.
3. **Automated:** Install Hermes skill pack → `/account-action-brief` runs the same chain via MCP.
4. Govern: connector map + review gates → every output starts as Draft.
5. Package: workflow card + 4 installable skills.
6. Close: You.com Discord intro + Week 1 challenge (3 briefs).
7. **Week 2+:** `/meeting-prep` for calendar-triggered briefs (post-workshop).

---

## QA / teaching notes

- Default app URL: http://localhost:8080 (not `?express=1`)
- Preflight: `./preflight.sh` validates skill pack + app
- Facilitator script: `FACILITATOR-60MIN.md`
- Full written depth: `audience-workflow-building-tutorial.md` (17 steps — synced with 60-min + post-event)
