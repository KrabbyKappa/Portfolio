---
type: reference
description: Graph linking rules for the Website Development wiki
last_updated: 2026-05-20
tags: [graph, governance, links]
source: wiki
---

# Graph Guidelines

← [[MOC/MOC-Graph]]

## Link Purposes

Every link must serve at least one purpose:

- taxonomy: page belongs to a hub
- evidence: a claim points to a source or verifier
- implementation: project links to code map
- operation: workflow links to the check that proves it
- decision: page links to the decision shaping it

## Orphan Rule

Every non-template content page must have at least one inbound link from [[index]] or a relevant MOC. If no destination exists yet, record the gap in [[missing-pages]].

## Link Form

Use full-path wikilinks from `wiki/` root:

```markdown
[[projects/bizwholistic]]
[[operations/operations-site-verification]]
```

→ All governance: [[MOC/MOC-Graph]]
