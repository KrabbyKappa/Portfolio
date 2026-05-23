---
type: project
description: Astro multilingual marketing site for Bizwholistic
last_updated: 2026-05-20
tags: [project, astro, bizwholistic]
project_path: Bizwholistic
status: active
related:
  - implementation/impl-bizwholistic-astro
  - seo/seo-bizwholistic-crawlability
  - reference/bizwholistic-design-papers-index
  - reference/astro-docs-index
---

# Bizwholistic

← [[MOC/MOC-Projects]]

Bizwholistic is the Astro static site in `Bizwholistic/`. The source of truth is the source tree and config, not the built `dist/` folder unless a fresh build was run.

## Key Paths

| Path | Role |
|------|------|
| `Bizwholistic/src/pages/` | Routes and localized pages |
| `Bizwholistic/src/components/` | Shared Astro components |
| `Bizwholistic/src/data/intentPages.ts` | Intent-page data |
| `Bizwholistic/public/robots.txt` | Crawler policy |
| `Bizwholistic/public/llms.txt` | AI-search summary |
| `Bizwholistic/public/llms-full.txt` | Extended machine-readable summary |
| `Bizwholistic/astro.config.mjs` | Site, i18n, sitemap, and build config |

## Design Reference Bundle

The copied design papers and editable option files are indexed at [[reference/bizwholistic-design-papers-index]]. They live under `wiki/assets/design-papers/bizwholistic-hk/` and are reference assets, not the implementation source of truth.

## Astro Docs Reference

The official Astro docs distilled for this workspace start at [[reference/astro-docs-index]]. Use that page before changing routing, i18n, sitemap, asset handling, or deployment behavior.

## Verification

Use [[operations/operations-site-verification]] after edits. For source changes, run `npm run build` inside `Bizwholistic/`.

→ All projects: [[MOC/MOC-Projects]]
