---
type: project
description: Astro rebuild of Luca's personal portfolio site
last_updated: 2026-05-21
tags: [project, portfolio, astro, static-site]
project_path: Astro Portfolio
status: active
related:
  - implementation/impl-astro-portfolio
  - projects/portfolio-main
  - logs/work-record-2026-05-21-astro-portfolio-preview-motion
  - logs/work-record-2026-05-21-astro-portfolio-project-video-loops
  - logs/work-record-2026-05-21-astro-portfolio-code-reduction-audit
  - logs/work-record-2026-05-21-portfolio-package-demo-showcase
  - logs/work-record-2026-05-21-astro-portfolio-showcase-full-demo-card-clicks
  - logs/work-record-2026-05-21-astro-portfolio-project-video-youtube-links
  - logs/work-record-2026-05-23-git-force-push-wipe-incident
---

# Astro Portfolio

← [[MOC/MOC-Projects]] · [[projects/portfolio-main]]

`Astro Portfolio/` is the Astro rebuild of Luca's personal portfolio. It is now located directly under the Website Development workspace root and is the canonical folder for the Astro version.

## Key Paths

| Path | Role |
|------|------|
| `Astro Portfolio/package.json` | Astro package scripts and dependencies |
| `Astro Portfolio/astro.config.mjs` | Static output, canonical site URL, and build config |
| `Astro Portfolio/src/pages/` | Astro route source |
| `Astro Portfolio/src/layouts/` | Shared portfolio and showcase layouts |
| `Astro Portfolio/src/components/` | Reusable components |
| `Astro Portfolio/src/data/` | Content/data modules |
| `Astro Portfolio/public/` | Stable passthrough assets, PDFs, CNAME, CSS, screenshots, demo assets |
| `Astro Portfolio/dist/` | Fresh static build output after `npm run build` |
| `Astro Portfolio/verify_astro_portfolio_site.py` | Built-site structural verifier |
| `Astro Portfolio/verify_astro_portfolio_visual_qa.py` | Rendered browser QA verifier |

## Route Contract

| Public route | Astro source |
|--------------|--------------|
| `/` | `src/pages/index.astro` |
| `/projects.html` | `src/pages/projects.astro` |
| `/articles.html` | `src/pages/articles.astro` |
| `/references.html` | `src/pages/references.astro` |
| `/website-development/` | `src/pages/website-development/index.astro` |
| `/website-development/demos/**/` | `src/pages/website-development/demos/**/index.astro` |

## Current Design State

The project video cards are local MP4 previews rather than YouTube widgets: the homepage uses lightweight 720p clips and `projects.html` uses 1080p project-detail clips, all visibility-gated and route-isolated for GitHub Pages/free hosting. The home page no longer uses the hero focus-strip pills. The home Website Development preview and the Projects bridge now use a left/center/right screenshot orbit with a six-site teaser set: Bizwholistic, Mosaic Content Studio, Verde Lunch Club, Harbor Legal Translation, City Lab Pop-Up, and Mila Yoga Reset. The full `/website-development/` route includes the same five fictional package demos plus the Bizwholistic case-study card.

The `/website-development/` showcase page is now a warm light-themed, no-floating-background surface. It opens with the centered marketing headline `Your ideal website, shaped around your ambition.` above a wider horizontal Bizwholistic live case-study glass card, then five selected package demos: Mosaic Content Studio, Verde Lunch Club, Harbor Legal Translation, City Lab Pop-Up, and Mila Yoga Reset. The page has no technical hero lead, category pill rail, proof-contract rows, Bizwholistic disclaimer/kind lines, demo intro paragraph, footer disclaimer, separate purple double-circle decoration, visible SVG number labels, or ambient SVG/physics layer.

The selected cards use more transparent real-glass surfaces with 34px backdrop blur. The rounded card label tabs and nav tabs now use a sticker-like thick liquid-glass treatment inspired by `liquidGL`: explicit `data-thick-glass-tab` markers, near-clear centers, raised 3D transform context, crisp masked bevel/specular rims, tight contact shadows, deeper underside slabs, and subtle colored `--tab-refract` caustic glows below the glass. The top header intentionally uses a different quieter light-glass shell with a separate rounded nav capsule, rather than the same dark pill treatment as the tabs.

The Mosaic card embeds a same-origin live iframe preview of the actual Astro demo, scaled down inside the card so the animated page is visible without loading external services. The live iframe is sandboxed with `allow-same-origin`, pointer-events are disabled, and a static fallback image remains present for structural proof. The selected demo cards now use a single full-card overlay anchor (`.demo-card__full-link`) so clicking the preview, text, tab labels, or lower action area opens the full Astro demo without nested CTA anchors.

## Verification

```bash
cd "Astro Portfolio"
npm run build
python3 verify_astro_portfolio_site.py
python3 verify_astro_portfolio_showcase_card_links.py --base-url http://127.0.0.1:8796
python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796
```

→ Implementation: [[implementation/impl-astro-portfolio]]

The screenshot preview motion now follows Luca's newer ethereal-window direction: home and Projects both show a clipped left/center/right screenshot orbit using real website preview images, with CSS-only motion and a reduced-motion static triad fallback.
