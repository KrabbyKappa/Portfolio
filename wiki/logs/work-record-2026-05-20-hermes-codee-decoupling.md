---
type: log
description: Work record for removing active CODEE assumptions from Website Development Hermes setup
last_updated: 2026-05-20
tags: [log, hermes, workspace]
date: 2026-05-20
---

# Work Record: Hermes CODEE Decoupling

← [[MOC/MOC-Operations]]

## Outcome

Hermes must treat `/Users/lucak/Website Development` as a standalone workspace. CODEE can be referenced only when a task explicitly asks for it; it must not appear as a normal active mount or active rule source for website work.

## Current Evidence

- Active Hermes config already points `terminal.cwd` at `/Users/lucak/Website Development`.
- Active Hermes config still exposed `/Users/lucak/CODEE` and `/host/codee` as workspace mounts.
- The package-demo uniqueness board still pointed agents at `/Users/lucak/CODEE/.claude/rules/*`.
- Subagent logs showed folder-specific path mistakes around the spaced `Website Development` path, making any extra workspace hint more costly.

## Intended Verifier

```bash
bash .claude/scripts/verify_site_assets.sh
bash .claude/scripts/verify_wiki.sh
bash .claude/scripts/refresh_graphify_workspace.sh
```

## Handoff Path

- Runtime config: `/Users/lucak/.hermes/config.yaml`
- Workspace instructions: `HERMES.md`
- Workspace operation page: [[operations/operations-hermes-website-development]]
- Active guard: `.claude/scripts/verify_site_assets.sh`

→ All operations: [[MOC/MOC-Operations]]
