# 60-Minute Workshop — Google Slides Deck

Companion slides for the live workshop app (`http://localhost:8080`).

**Latest deck:** `60-min-workshop-slides.pptx` — regenerated from `build_60min_slides.py`  
**Synced with:** MCP explainer, Hermes skills + connectors, playground walk, live Hermes setup

---

## Import into Google Slides

1. Open [Google Slides](https://slides.google.com)
2. **File → Import slides** → upload `workshop-app/60-min-workshop-slides.pptx`

### Regenerate

```bash
cd workshop-app
python build_60min_slides.py
```

Output: **21 slides**

**Companion docs (not on slides — facilitator use):**
- `PLAYGROUND-API-WALKTHROUGH.md` — full queries, parameters, curl, goal-specific examples
- `SLIDE-PRESENTER-SCRIPT.md` / `./walk_slides.py` — detailed say/do per slide

---

## Slide list (21)

1. Title
2. Two platforms
3. Agenda
4. API map
5. Web Search API
6. Contents API
7. Research API
8. **MCP — what it is + You.com MCP server**
9. **How You.com MCP works** — step-by-step flow in `/account-action-brief`
10. Finance Research (optional)
11. Platform playground walkthrough
12. **Hermes skills & connectors** — skills vs permissions
13. Govern — review gates
14. Define inputs in Hermes
15. Hermes install (`install.sh`)
16. Wire MCP (copy-paste)
17. Define inputs + test command
18. Minimum success checklist
19. Discord
20. Close script
21. Resources

---

## When to show the new slides

| Slide | When | Say |
|-------|------|-----|
| **8–9 MCP** | After Research API, before playground | "You just ran these APIs manually — MCP is how Hermes runs the same chain as tools." |
| **12 Skills & connectors** | After playground, before Hermes install | "You're installing a skill today. Connectors control what it can touch." |
| **13 Govern** | App govern step (18–23 min) | Review gates in the app; reference slide 12 for connector map |

---

## Copy-paste blocks

**Install:**
```bash
cd workshop-app/hermes-desktop && chmod +x install.sh && ./install.sh
```

**MCP (slide 16):**
```
https://api.you.com/mcp
you-search, you-contents, you-research
```

**Test (slide 17):**
```
/account-action-brief
company: AMD
website: https://www.amd.com
goal: [Renewal | Outbound | Competitive | Partner]
output_audience: internal
```

**Discord:** https://discord.gg/2C4WgryxSD
