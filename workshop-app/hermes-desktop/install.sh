#!/usr/bin/env bash
# Install workshop skills into Hermes Agent (~/.hermes/skills/)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="${HERMES_SKILLS_DIR:-$HOME/.hermes/skills}"

mkdir -p "$DEST"

for skill in account-action-brief community-pulse workshop-60min meeting-prep; do
  src="$SCRIPT_DIR/skills/$skill"
  if [[ ! -d "$src" ]]; then
    echo "Missing skill directory: $src" >&2
    exit 1
  fi
  rm -rf "$DEST/$skill"
  cp -r "$src" "$DEST/$skill"
  echo "Installed: $DEST/$skill"
done

echo ""
echo "Done. Restart Hermes if skills do not appear."
echo "Wire You.com MCP: https://api.you.com/mcp"
echo "Test: /account-action-brief  or  /meeting-prep"
