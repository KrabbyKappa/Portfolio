---
type: business
description: Project-manager explanation of the Website Development wiki ingestion and accuracy pass
last_updated: 2026-05-21
tags: [business, project-management, wiki, ingestion, accuracy]
source_file: wiki/logs/work-record-2026-05-21-project-manager-wiki-ingestion.md
related:
  - business/website-package-demo-pages
  - reference/astro-docs-index
  - reference/bizwholistic-design-papers-index
  - logs/work-record-2026-05-21-astro-docs-design-papers
  - logs/work-record-2026-05-20-wiki-perfection-audit
---

# Project Manager Brief: Wiki Ingestion and Accuracy Pass

← [[MOC/MOC-Business]] · [[MOC/MOC-Reference]] · [[MOC/MOC-Operations]]

## Executive Summary

The Website Development wiki now works as a project-management control surface for Luca's website business, not just as loose notes. It connects business/pricing material, package demo evidence, source-backed Astro reference material, Bizwholistic design-paper assets, and verification commands in one navigable system.

The practical result: a project manager can answer three questions quickly:

1. What has been ingested into the knowledge base?
2. Which pages or files are the source of truth?
3. Which verifier proves the current wiki state is internally consistent?

## What Was Ingested

| Area | Ingested material | Evidence path |
|------|-------------------|---------------|
| Astro framework docs | 19 selected official docs, with 19 raw MDX fetches recorded in the manifest | `wiki/assets/astro-docs/manifest.json`, [[reference/astro-docs-index]] |
| Bizwholistic design papers | 23 local design-option assets: 10 DOCX files, 12 PDF files, 1 PNG contact sheet; 4,712,609 total bytes | `wiki/assets/design-papers/bizwholistic-hk/`, [[reference/bizwholistic-design-papers-index]] |
| Business/package docs | Business offers, package specs, and demo-page status routed through a dedicated business map | [[MOC/MOC-Business]], [[business/business-service-offers]], [[business/website-package-demo-pages]] |
| Reference docs | Astro docs, design papers, external template research, and source-code analysis routed through a dedicated reference map | [[MOC/MOC-Reference]] |
| Package demo status | 10 static demo pages documented: 5 Micro and 5 Basic | [[business/website-package-demo-pages]], `package-demo-pages/` |

## What Was Corrected

The accuracy pass tightened the wiki so a future project manager does not inherit stale or misleading assumptions.

- Added [[MOC/MOC-Business]] for offer, pricing, package-spec, and demo-page routing.
- Added [[MOC/MOC-Reference]] for external references, Astro docs, design papers, and research assets.
- Corrected the Astro docs route to [[reference/astro-docs-index]].
- Recorded that Riverside was later photo-rescued, City Lab is the preserved approved Micro reference, and Mosaic is the protected Basic creative reference.
- Recorded that `verify_demo_polish.py` is now part of the current package-demo verification set.
- Replaced the inaccurate uniform section-count claim with the current fact: demo pages vary from 6 to 11 sections, while the verifier requires at least six.
- Added the Verde Google Maps iframe note so static scope is accurately described as no backend or app logic, while allowing the third-party map embed.
- Corrected Basic photo-rebuild records from active/backlog to complete where PASS evidence already existed.
- Corrected the current City Lab CSS checksum and preserved historical context.

## Why It Matters to a Project Manager

This changes the operating model from "remember what happened" to "follow the routed evidence."

- The wiki index points work to the right MOC instead of relying on chat memory.
- Business decisions are linked to offer documents, package specs, and demo examples.
- Technical implementation decisions can start from distilled Astro docs instead of searching upstream docs from scratch.
- Design options for Bizwholistic are preserved locally and indexed, so future design work can cite actual files.
- Verification commands are named and repeatable, so claims like "the wiki is clean" or "the ingestion is consistent" can be checked, not trusted.

## Current Verifier Set

Run these from `/Users/lucak/Website Development` when touching the wiki or the ingested reference layer:

```bash
bash .claude/scripts/verify_wiki.sh
python3 .claude/scripts/verify_astro_docs_ingestion.py
python3 .claude/scripts/tests/test_wiki_system.py
python3 .claude/scripts/verify_graphify_workspace.py
python3 package-demo-pages/verify_demo_pages.py
python3 package-demo-pages/verify_demo_uniqueness.py
python3 package-demo-pages/verify_demo_polish.py
```

## Current Verified Baseline

Fresh checks before this brief was written showed:

```text
VERDICT: PASS -- safe to proceed.
VERDICT: PASS -- Astro docs and Bizwholistic design-paper ingestion are internally consistent
```

Primary file evidence also showed:

- `wiki/assets/astro-docs/manifest.json`: `selected_count=19`, `raw_mdx_ok=19`, `docs_len=19`, `fetched_at_utc=2026-05-20T17:03:27Z`.
- `wiki/assets/design-papers/bizwholistic-hk/`: `23` files, `4,712,609` bytes.
- `package-demo-pages/`: `10` demo index pages: `5` Micro and `5` Basic.

## Manager Handoff

Start here for each future work type:

- Business offer, pricing, package specs, demo examples: [[MOC/MOC-Business]].
- Astro framework docs, design papers, external website references: [[MOC/MOC-Reference]].
- Verification commands and work-start process: [[MOC/MOC-Operations]].
- Detailed ingestion record: [[logs/work-record-2026-05-21-astro-docs-design-papers]].
- Detailed accuracy closeout: [[logs/work-record-2026-05-20-wiki-perfection-audit]].
- This project-manager summary: [[business/project-manager-wiki-ingestion-brief-2026-05-21]].
