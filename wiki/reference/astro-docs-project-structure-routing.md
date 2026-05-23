---
type: reference
description: Distilled Astro docs for setup, project structure, pages, routing, and i18n
last_updated: 2026-05-21
tags: [reference, astro, routing, i18n, project-structure]
source: Official Astro docs raw MDX snapshot
source_file: wiki/assets/astro-docs/manifest.json
related:
  - reference/astro-docs-index
  - projects/bizwholistic
  - implementation/impl-bizwholistic-astro
---

# Astro Project Structure, Pages, Routing, and i18n

← [[MOC/MOC-Reference]] · [[reference/astro-docs-index]] · [[projects/bizwholistic]]

## Source Coverage

| Official doc | Published URL | Raw MDX |
|--------------|---------------|---------|
| Astro Docs | [docs](https://docs.astro.build/en/getting-started/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/getting-started.mdx) |
| Install Astro | [docs](https://docs.astro.build/en/install-and-setup/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/install-and-setup.mdx) |
| Project structure | [docs](https://docs.astro.build/en/basics/project-structure/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/basics/project-structure.mdx) |
| Pages | [docs](https://docs.astro.build/en/basics/astro-pages/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/basics/astro-pages.mdx) |
| Routing | [docs](https://docs.astro.build/en/guides/routing/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/routing.mdx) |
| Add i18n features | [docs](https://docs.astro.build/en/recipes/i18n/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/recipes/i18n.mdx) |

## What the Official Docs Cover

- Astro Docs: no section headings in raw front page; use as entry point.
- Install Astro: Prerequisites; Browser compatibility; Install from the CLI wizard; CLI installation flags; Add integrations; Use a theme or starter template; Manual Setup
- Project structure: Directories and Files; Example Project Tree; `src/`; `src/pages`; `src/components`; `src/layouts`; `src/styles`; `public/`
- Pages: Supported page files; File-based routing; Link between pages; Astro Pages; Markdown/MDX Pages; HTML Pages; Custom 404 Error Page; Custom 500 Error Page
- Routing: Navigating between pages; Static routes; Dynamic routes; Static (SSG) Mode; On-demand dynamic routes; Redirects; Configured Redirects; Dynamic redirects
- Add i18n features: Recipe; Set up pages for each language; Use collections for translated content; Translate UI strings; Let users switch between languages; Hide default language in the URL; Translate Routes; Resources

## Local Distillation

- `src/pages/` defines routes. Bizwholistic uses localized route trees under `src/pages/en/` and `src/pages/pl/`, plus legacy redirect pages at the root.
- Static dynamic routes require explicit generated paths. Bizwholistic currently has `src/pages/en/[slug]/index.astro`; route additions should verify generated URLs after build.
- `astro.config.mjs` is the routing contract: local config uses `site: https://bizwholistic.com`, `output: static`, `trailingSlash: always`, `defaultLocale: en`, locales `en` and `pl`, and `prefixDefaultLocale: true`.
- Language switchers should point only to real alternate pages. If a translated page does not exist, do not emit a fake alternate route.
- Routing, redirects, and i18n changes should be checked against sitemap output and built `dist/` paths, not only source code.

## Bizwholistic Checklist

- [ ] Add routes under both `src/pages/en/` and `src/pages/pl/` when the page is truly bilingual.
- [ ] If using dynamic routes, verify `getStaticPaths()` or equivalent static enumeration covers every expected page.
- [ ] Keep trailing slash behavior consistent with `trailingSlash: always`.
- [ ] Verify language-switch links and hreflang only reference real built URLs.
- [ ] Run `npm run build` from `Bizwholistic/` after source changes.
