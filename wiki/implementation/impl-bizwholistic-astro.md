---
type: implementation
description: Implementation map for the Bizwholistic Astro site
last_updated: 2026-05-20
tags: [implementation, astro, bizwholistic]
primary_file: Bizwholistic/astro.config.mjs
related_files:
  - Bizwholistic/package.json
  - Bizwholistic/src/pages/en/index.astro
  - Bizwholistic/src/pages/pl/index.astro
  - Bizwholistic/src/data/intentPages.ts
  - Bizwholistic/public/robots.txt
  - Bizwholistic/public/llms.txt
related:
  - reference/astro-docs-index
---

# Bizwholistic Astro Implementation

← [[MOC/MOC-Implementation]]

The Astro implementation is a static multilingual site. `astro.config.mjs` sets the production site URL, static output, trailing slashes, i18n routing, and sitemap integration.

## Source Areas

| Area | Path |
|------|------|
| Page routes | `Bizwholistic/src/pages/` |
| Shared layout | `Bizwholistic/src/layouts/Base.astro` |
| Components | `Bizwholistic/src/components/` |
| Intent pages | `Bizwholistic/src/data/intentPages.ts` |
| Public crawler assets | `Bizwholistic/public/` |

## Official Astro Docs Layer

Use [[reference/astro-docs-index]] as the local entry point for official Astro documentation. The distilled pages cover [[reference/astro-docs-project-structure-routing]], [[reference/astro-docs-components-assets-interactivity]], [[reference/astro-docs-config-data-build-deploy]], and [[reference/astro-version-watch]].

## Verifier

Use `npm run build` from `Bizwholistic/` and then `bash .claude/scripts/verify_wiki.sh` from the workspace root.

→ All implementation: [[MOC/MOC-Implementation]]
