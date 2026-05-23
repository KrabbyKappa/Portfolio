---
type: reference
description: Local Astro version and upstream-doc refresh watchpoints for Website Development
last_updated: 2026-05-21
tags: [reference, astro, version, verification]
source: Local Astro CLI and official Astro docs manifest
source_file: wiki/assets/astro-docs/manifest.json
related:
  - reference/astro-docs-index
  - implementation/impl-bizwholistic-astro
---

# Astro Version Watch

← [[MOC/MOC-Reference]] · [[reference/astro-docs-index]]

## Current Local Evidence

| Check | Value |
|-------|-------|
| `npm exec astro -- --version` from `Bizwholistic/` | `astro v5.18.1` |
| `Bizwholistic/package.json` package range | `astro: ^5.0.0` |
| Manifest fetched at UTC | `2026-05-20T17:03:27Z` |
| Selected official docs | 19 |
| Raw MDX verified | 19 |

## Rule

Before applying any version-sensitive Astro guidance, re-run the local version check and compare the target doc against the installed major version. Treat upstream migration guidance as advisory until local package and build evidence confirm it applies.

## Refresh Protocol

1. Re-fetch `https://docs.astro.build/sitemap-index.xml` and selected raw MDX paths.
2. Update `wiki/assets/astro-docs/manifest.json`.
3. Re-run `npm exec astro -- --version` from `Bizwholistic/`.
4. Update [[reference/astro-docs-index]] and topic pages only where the source facts changed.
5. Run:

```bash
python3 .claude/scripts/verify_astro_docs_ingestion.py
bash .claude/scripts/verify_wiki.sh
```
