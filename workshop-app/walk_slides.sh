#!/usr/bin/env bash
# Interactive slide-by-slide presenter walkthrough.
set -euo pipefail
cd "$(dirname "$0")"
exec python3 walk_slides.py "$@"
