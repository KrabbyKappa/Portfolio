---
type: operation
description: Required work-start documentation protocol for agents
last_updated: 2026-05-20
tags: [operation, agent-workflow, wiki]
verifier: bash .claude/scripts/verify_wiki.sh
---

# Agent Work-Start Documentation

← [[MOC/MOC-Operations]]

Before meaningful work, create or update a wiki record that states:

| Field | Meaning |
|-------|---------|
| Outcome wanted | What should be true when the task is complete |
| Current evidence | Files, pages, or commands already checked |
| Intended verifier | Command or inspection that will prove the work |
| Handoff path | Where future agents should resume |

## When Required

- Site source changes
- SEO or crawlability audits
- Business-offer edits
- Hermes or agent configuration changes
- Wiki content or schema changes

## When Not Required

- One-line shell checks
- Simple file lookup
- Pure conversation with no operational conclusion

## Closeout

Run `bash .claude/scripts/verify_wiki.sh` after touching wiki or agent files.

→ All operations: [[MOC/MOC-Operations]]
