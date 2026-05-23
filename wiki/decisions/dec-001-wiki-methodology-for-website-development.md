---
type: decision
description: Adopt a local wiki operating methodology for website development work
last_updated: 2026-05-20
tags: [decision, wiki, methodology]
id: DEC-001
status: accepted
---

# DEC-001: Local Wiki Methodology For Website Development

← [[MOC/MOC-Decisions]]

## Decision

Use a local wiki method for this website-development workspace: a read-first index, MOC routing, schema-governed pages, dedicated wiki agents, and a verifier that must pass before completion claims.

## Reason

Website work crosses source code, business positioning, SEO assets, and deployment artifacts. A routing wiki reduces repeated discovery and keeps future agents aligned with evidence.

## Consequences

- Agents start from [[index]].
- Non-trivial work gets a durable wiki record.
- Structural health is verified by `bash .claude/scripts/verify_wiki.sh`.
- Search and business claims must be backed by files or live checks.

→ All decisions: [[MOC/MOC-Decisions]]
