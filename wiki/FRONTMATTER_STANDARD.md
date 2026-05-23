---
type: reference
description: Canonical frontmatter examples for Website Development wiki pages
last_updated: 2026-05-20
tags: [frontmatter, schema, governance]
source: wiki
---

# Frontmatter Standard

← [[index]]

## Project

```yaml
---
type: project
description: One-line project summary
last_updated: YYYY-MM-DD
tags: [project]
project_path: Path/From/Workspace
status: active
related:
  - implementation/example-page
---
```

## Implementation

```yaml
---
type: implementation
description: One-line implementation summary
last_updated: YYYY-MM-DD
tags: [implementation]
primary_file: Path/To/File
related_files:
  - Path/To/Other/File
---
```

## Operation

```yaml
---
type: operation
description: One-line runbook summary
last_updated: YYYY-MM-DD
tags: [operation]
verifier: command to run
---
```

## Decision

```yaml
---
type: decision
description: One-line decision summary
last_updated: YYYY-MM-DD
tags: [decision]
id: DEC-001
status: accepted
---
```

Use [[SCHEMA]] as the authority when adding or changing fields.

→ All governance: [[MOC/MOC-Graph]]
