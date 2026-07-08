# Install Workshop Skills in Hermes Desktop

## Option A — Install script (recommended)

```bash
cd workshop-app/hermes-desktop
./install.sh
```

Skills install to `~/.hermes/skills/`.

## Option B — Hermes CLI

```bash
hermes skills install /path/to/workshop-app/hermes-desktop/skills/account-action-brief/SKILL.md
hermes skills install /path/to/workshop-app/hermes-desktop/skills/meeting-prep/SKILL.md
hermes skills install /path/to/workshop-app/hermes-desktop/skills/community-pulse/SKILL.md
hermes skills install /path/to/workshop-app/hermes-desktop/skills/workshop-60min/SKILL.md
```

## Option C — Manual copy

```bash
cp -r workshop-app/hermes-desktop/skills/* ~/.hermes/skills/
```

## Wire You.com MCP

1. Add MCP server: https://api.you.com/mcp
2. Enable: you-search, you-contents, you-research
3. Ensure `requires_toolsets: [web]` tools are available

## Test

```
/account-action-brief

company: AMD
website: https://www.amd.com
```
