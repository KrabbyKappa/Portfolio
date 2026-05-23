---
type: operation
description: Local verification commands for wiki and website assets
last_updated: 2026-05-21
tags: [operation, verification, website]
verifier: bash .claude/scripts/verify_wiki.sh
---

# Site Verification

← [[MOC/MOC-Operations]]

## Wiki Gate

```bash
bash .claude/scripts/verify_wiki.sh
```

This runs:

| Check | Script |
|-------|--------|
| Broken wikilinks | `wiki/_find_broken.py` |
| Schema, frontmatter routes, file refs, orphans | `wiki/_audit.py` |
| Website asset readiness | `.claude/scripts/verify_site_assets.sh` |
| Python syntax for verifier helpers | `python3 -c "import ast, ..."` |

## Wiki Regression Test

```bash
python3 .claude/scripts/tests/test_wiki_system.py
```

This checks required files, Graphify availability, graph JSON validity, and targeted verifier behavior.

## Graphify Integration Gate

```bash
python3 .claude/scripts/verify_graphify_workspace.py
```

This checks graph JSON validity, manifest source coverage across the intended workspace areas, ignore-policy enforcement, visual map/report artifact readiness, and scoped query traversal.

## Astro Docs / Design-Paper Ingestion Gate

```bash
python3 .claude/scripts/verify_astro_docs_ingestion.py
```

This checks the local Astro docs manifest, distilled Astro wiki pages, Bizwholistic design-paper asset count/bytes, listed asset paths, local Astro package range, and the wiki verifier.

## Bizwholistic Build Gate

```bash
npm run build
```

Run from `Bizwholistic/` after source changes.

## What Counts As Evidence

- Command output and exit code.
- Specific file paths inspected.
- Freshly generated `Bizwholistic/dist/` files after a build.
- `graphify update .` or `graphify update . --no-cluster` after source/wiki code changes.
- Live website checks only when explicitly requested.

→ All operations: [[MOC/MOC-Operations]]
