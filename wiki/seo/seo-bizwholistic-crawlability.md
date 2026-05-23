---
type: seo
description: Bizwholistic crawlability and AI-search asset map
last_updated: 2026-05-20
tags: [seo, crawlability, ai-search, bizwholistic]
project: projects/bizwholistic
related_files:
  - Bizwholistic/public/robots.txt
  - Bizwholistic/public/llms.txt
  - Bizwholistic/public/llms-full.txt
  - Bizwholistic/astro.config.mjs
---

# Bizwholistic Crawlability

← [[MOC/MOC-SEO]]

The crawlability surface is source-controlled in `Bizwholistic/public/` and generated at build time through Astro sitemap integration.

## Machine-Readable Assets

| Asset | Source path |
|-------|-------------|
| Robots policy | `Bizwholistic/public/robots.txt` |
| AI-search summary | `Bizwholistic/public/llms.txt` |
| Extended AI-search summary | `Bizwholistic/public/llms-full.txt` |
| Sitemap config | `Bizwholistic/astro.config.mjs` |

## Verification

Use [[operations/operations-site-verification]]. If search visibility is the question, also inspect live crawlability and stale indexed URLs before making recommendations.

→ All SEO: [[MOC/MOC-SEO]]
