---
type: reference
description: Distilled Astro docs for components, layouts, assets, scripts, islands, and TypeScript
last_updated: 2026-05-21
tags: [reference, astro, components, assets, islands, typescript]
source: Official Astro docs raw MDX snapshot
source_file: wiki/assets/astro-docs/manifest.json
related:
  - reference/astro-docs-index
  - projects/bizwholistic
  - implementation/impl-bizwholistic-astro
---

# Astro Components, Assets, and Interactivity

← [[MOC/MOC-Reference]] · [[reference/astro-docs-index]] · [[implementation/impl-bizwholistic-astro]]

## Source Coverage

| Official doc | Published URL | Raw MDX |
|--------------|---------------|---------|
| Components | [docs](https://docs.astro.build/en/basics/astro-components/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/basics/astro-components.mdx) |
| Layouts | [docs](https://docs.astro.build/en/basics/layouts/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/basics/layouts.mdx) |
| Scripts and event handling | [docs](https://docs.astro.build/en/guides/client-side-scripts/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/client-side-scripts.mdx) |
| Islands architecture | [docs](https://docs.astro.build/en/concepts/islands/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/concepts/islands.mdx) |
| Images | [docs](https://docs.astro.build/en/guides/images/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/images.mdx) |
| TypeScript | [docs](https://docs.astro.build/en/guides/typescript/) | [raw MDX](https://raw.githubusercontent.com/withastro/docs/main/src/content/docs/en/guides/typescript.mdx) |

## What the Official Docs Cover

- Components: Component Structure; The Component Script; The Component Template; Component-based design; Component Props; Slots; Named Slots; Fallback Content for Slots
- Layouts: Sample Layout; Using TypeScript with layouts; Markdown Layouts; Markdown Layout Props; Importing Layouts Manually (MDX); Nesting Layouts
- Scripts and event handling: Client-Side Scripts; Script processing; Unprocessed scripts; Include JavaScript files on your page; Common script patterns; Handle `onclick` and other events; Web components with custom elements; Pass frontmatter variables to scripts
- Islands architecture: A brief history; What is an island?; Island components; Client Islands; Server islands
- Images: Where to store images; `src/` vs `public/`; Remote images; Images in `.astro` files; Images in Markdown files; Images in MDX files; Images in UI framework components; Astro components for images
- TypeScript: Setup; TSConfig templates; TypeScript editor plugin; UI Frameworks; Type Imports; Import Aliases; Extending global types; `window` and `globalThis`

## Local Distillation

- Astro components split server-side frontmatter from rendered markup. Bizwholistic reusable UI lives in `Bizwholistic/src/components/` and layout ownership lives in `Bizwholistic/src/layouts/Base.astro`.
- Prefer static HTML/CSS first. Add client JavaScript only where a static pattern cannot satisfy the interaction.
- Islands are the hydration boundary for framework components; Bizwholistic should not introduce an island or framework dependency for a minor brochure-site interaction without a clear reason.
- Images/assets that need processing or imports belong under `src/`. Files that should pass through unchanged belong under `public/`.
- Current Bizwholistic SVG artwork is under `src/assets/`; changes to SVG-heavy hero sections need visual verification on mobile and desktop.
- TypeScript-sensitive component props should be checked in `.astro` frontmatter rather than inferred from templates.

## Bizwholistic Checklist

- [ ] Keep shared page chrome in `src/layouts/Base.astro`.
- [ ] Keep reusable display blocks in `src/components/`.
- [ ] Do not add a client runtime unless the interaction requires browser state.
- [ ] Verify asset paths in a fresh build, especially imported SVGs.
- [ ] Browser-check mobile and desktop when image/SVG geometry changes.
