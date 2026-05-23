---
type: reference
description: Distilled Astro docs for content collections, sitemap, configuration, environment variables, backend boundaries, and deploy
last_updated: 2026-05-21
tags: [reference, astro, sitemap, deploy, config, environment]
source: Official Astro docs raw MDX snapshot
source_file: wiki/assets/astro-docs/manifest.json
related:
  - reference/astro-docs-index
  - projects/bizwholistic
  - implementation/impl-bizwholistic-astro
  - seo/seo-bizwholistic-crawlability
---

# Astro Config, Data, Build, and Deploy

← [[MOC/MOC-Reference]] · [[reference/astro-docs-index]] · [[MOC/MOC-SEO]]

## Source Coverage

| Official doc | Published URL | Raw MDX |
|--------------|---------------|---------|
| Content collections | [docs](https://docs.astro.build/en/guides/content-collections/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/content-collections.mdx) |
| '@astrojs/sitemap' | [docs](https://docs.astro.build/en/guides/integrations-guide/sitemap/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/integrations-guide/sitemap.mdx) |
| Deploy your Astro Site | [docs](https://docs.astro.build/en/guides/deploy/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/deploy/index.mdx) |
| Deploy your Astro Site to GitHub Pages | [docs](https://docs.astro.build/en/guides/deploy/github/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/deploy/github.mdx) |
| Configuration overview | [docs](https://docs.astro.build/en/guides/configuring-astro/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/configuring-astro.mdx) |
| Using environment variables | [docs](https://docs.astro.build/en/guides/environment-variables/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/environment-variables.mdx) |
| Use a backend service with Astro | [docs](https://docs.astro.build/en/guides/backend/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/backend/index.mdx) |

## What the Official Docs Cover

- Content collections: What are Content Collections?; Types of collections; When to create a collection; When not to create a collection; TypeScript configuration for collections; Defining build-time content collections; Build-time collection loaders; The `glob()` loader
- '@astrojs/sitemap': Why Astro Sitemap; Installation; Manual Install; Usage; Sitemap discovery; Configuration; `filter()`; `customPages`
- Deploy your Astro Site: Deployment Guides; Quick Deploy Options; Website UI; CLI Deployment; Building Your Site Locally; Adding an Adapter for on-demand rendering
- Deploy your Astro Site to GitHub Pages: How to deploy; Change your GitHub URL to a custom domain; Examples
- Configuration overview: The Astro config File; The TypeScript config File; Development Experience; Common new project tasks; Add your deployment domain; Add site metadata
- Using environment variables: Vite's built-in support; IntelliSense for TypeScript; Default environment variables; Setting environment variables; `.env` files; In the Astro config file; Using the CLI; Getting environment variables
- Use a backend service with Astro: Backend service guides; What is a backend service?; Why would I use a backend service?

## Local Distillation

- `astro.config.mjs` is the local source for site URL, static output, trailing slash behavior, i18n, sitemap integration, and build options.
- Bizwholistic uses `@astrojs/sitemap`; the config supplies i18n locale mappings, shared `lastmod`, and filters out apex-root and legacy redirect URLs.
- Content collections are a good fit only when content becomes data-driven and schema-validated. Do not add a collection for a one-off static page.
- Environment variables must be treated as build/deploy configuration, not committed content.
- Backend services are outside the current static-site boundary unless the project intentionally adopts runtime infrastructure.
- GitHub Pages docs are useful as static-output reference, but deployment behavior must be verified against the actual hosting target before treating redirects or fallback files as authoritative.

## Bizwholistic Checklist

- [ ] Run `npm run build` after source/config changes.
- [ ] Inspect generated sitemap if SEO, i18n, redirects, or canonical paths change.
- [ ] Keep redirect/fallback pages out of the sitemap unless they are intended canonical URLs.
- [ ] Treat backend integrations as a new architecture decision, not a default Astro feature.
- [ ] Keep deployment assumptions separate from local build evidence.
