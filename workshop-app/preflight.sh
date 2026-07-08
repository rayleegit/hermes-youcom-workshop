#!/usr/bin/env bash
# Pre-workshop verification — run before teaching
set -euo pipefail
cd "$(dirname "$0")"

PASS=0
FAIL=0

check() {
  local name="$1"
  shift
  if "$@" >/dev/null 2>&1; then
    echo "  ✓ $name"
    PASS=$((PASS + 1))
  else
    echo "  ✗ $name"
    FAIL=$((FAIL + 1))
  fi
}

echo "Account Action Brief Workshop — Preflight Check"
echo "================================================"
echo ""

# Python environment
echo "Environment"
if [ ! -d ".venv" ]; then
  echo "  → Creating virtual environment..."
  python3 -m venv .venv
fi
source .venv/bin/activate
pip install -q -r requirements.txt

check "Python venv active" test -d .venv
check "Dependencies installed" python -c "import fastapi, requests, uvicorn"
echo ""

# Module integrity
echo "Modules"
check "18 workshop steps" python -c "from app.steps import WORKSHOP_STEPS; assert len(WORKSHOP_STEPS)==18"
check "Platform highlights" python -c "from app.platform_highlights import WORKSHOP_STORY, YOU_COM_STRENGTHS, HERMES_STRENGTHS"
check "Teaching materials" python -c "from app.materials import OUTPUT_SCHEMA, OPENING_SCRIPT, CLOSING_SCRIPT"
check "Demo fixtures" test -f app/fixtures/search.json
check "Demo fixtures (contents)" test -f app/fixtures/research.json
check "Brief builder" python -c "from app.brief import build_brief, build_workflow_card, build_hermes_prompt"
echo ""

# API smoke test (offline)
echo "API logic (offline)"
check "Demo mode search" python -c "
import os; os.environ['DEMO_MODE']='true'
from app.youcom import search, extract_urls
r = search('AMD')
assert extract_urls(r)
"
check "Demo mode research" python -c "
import os; os.environ['DEMO_MODE']='true'
from app.youcom import research
r = research('AMD')
assert r.get('output')
"
check "Brief generation" python -c "
import os; os.environ['DEMO_MODE']='true'
from app.youcom import search, research
from app.brief import build_brief, build_workflow_card
s = {'company':'AMD','job':'test','search_results':search('AMD'),'research_results':research('AMD'),'demo_mode':True}
assert 'Account Action Brief' in build_brief(s)
assert 'Workflow Card' in build_workflow_card(s)
"
echo ""

# Static assets
echo "Static assets"
check "index.html" test -f static/index.html
check "app.js" test -f static/app.js
check "style.css" test -f static/style.css
echo ""

# Hermes desktop skill pack
echo "Hermes desktop skill pack"
[ -f hermes-desktop/install.sh ] && chmod +x hermes-desktop/install.sh 2>/dev/null || true
check "HERMES-DESKTOP-SETUP.md" test -f HERMES-DESKTOP-SETUP.md
check "install.sh" test -f hermes-desktop/install.sh
check "install.sh executable" test -x hermes-desktop/install.sh
check "account-action-brief SKILL.md" test -f hermes-desktop/skills/account-action-brief/SKILL.md
check "community-pulse SKILL.md" test -f hermes-desktop/skills/community-pulse/SKILL.md
check "workshop-60min SKILL.md" test -f hermes-desktop/skills/workshop-60min/SKILL.md
check "account-action-brief references" test -f hermes-desktop/skills/account-action-brief/references/connector-map.md
check "meeting-prep SKILL.md" test -f hermes-desktop/skills/meeting-prep/SKILL.md
check "skill pack validation" python -c "
from app.hermes_desktop import validate_skill_pack
r = validate_skill_pack()
assert r['ok'], r['errors']
assert r['skill_count'] == 4
"
check "skill pack zip export" python -c "
from app.hermes_desktop import build_skill_pack_zip
z = build_skill_pack_zip({'company': 'AMD', 'website': '', 'connector_map': {}})
assert len(z) > 1000
"
echo ""

# Teaching materials
echo "Teaching materials"
check "Facilitator run-of-show" test -f FACILITATOR.md
check "Attendee handout" test -f materials/attendee-handout.md
check "50-min facilitator guide" test -f FACILITATOR-50MIN.md
check "Express track (8 steps, 60 min)" python -c "from app.steps import get_express_steps, EXPRESS_50; assert len(get_express_steps())==8; assert EXPRESS_50['total_minutes']==60"
check "Root TEACH.md" test -f ../TEACH.md
echo ""

# Optional live check
echo "Optional"
if [ -n "${YDC_API_KEY:-}" ] || [ -f .env ] && grep -q "YDC_API_KEY=." .env 2>/dev/null; then
  echo "  ✓ YDC_API_KEY configured (live mode available)"
  PASS=$((PASS + 1))
else
  echo "  ○ YDC_API_KEY not set (demo mode only — OK for teaching)"
fi
echo ""

echo "================================================"
if [ "$FAIL" -eq 0 ]; then
  echo "READY TO TEACH ($PASS checks passed)"
  echo ""
  echo "Next: ./run.sh  →  open http://localhost:8080"
  echo "Script: FACILITATOR.md (full) or FACILITATOR-60MIN.md (60-min)"
  echo "Hermes desktop: ./hermes-desktop/install.sh  →  see HERMES-DESKTOP-SETUP.md"
  exit 0
else
  echo "NOT READY ($FAIL checks failed, $PASS passed)"
  exit 1
fi
