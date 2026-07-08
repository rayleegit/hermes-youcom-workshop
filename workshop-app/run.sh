#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install -q -r requirements.txt

if [ -f .env ]; then
  set -a
  source .env
  set +a
elif [ ! -f .env ] && [ -z "${YDC_API_KEY:-}" ]; then
  echo ""
  echo "No .env file found. Running in DEMO MODE with sample data."
  echo "To use live APIs: cp .env.example .env && add your YDC_API_KEY"
  echo ""
  export DEMO_MODE=true
fi

echo "Starting workshop app at http://localhost:8080"
echo "Press Ctrl+C to stop"
exec uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
