---
type: implementation
description: Implementation map for the Astro Portfolio static site rebuild
last_updated: 2026-05-21
tags: [implementation, portfolio, astro, static-site]
primary_file: Astro Portfolio/src/pages/index.astro
related_files:
  - Astro Portfolio/astro.config.mjs
  - Astro Portfolio/package.json
  - Astro Portfolio/src/layouts/BaseLayout.astro
  - Astro Portfolio/src/layouts/ShowcaseLayout.astro
  - Astro Portfolio/src/components
  - Astro Portfolio/src/data/site.ts
  - Astro Portfolio/src/pages/projects.astro
  - Astro Portfolio/src/pages/articles.astro
  - Astro Portfolio/src/pages/references.astro
  - Astro Portfolio/public/styles.css
  - Astro Portfolio/verify_astro_portfolio_site.py
  - Astro Portfolio/verify_astro_portfolio_visual_qa.py
  - Astro Portfolio/verify_astro_portfolio_showcase_card_links.py
  - Astro Portfolio/verify_astro_portfolio_video_loops.py
  - Astro Portfolio/verify_astro_portfolio_performance_budget.py
related:
  - projects/astro-portfolio
  - implementation/impl-portfolio-static-site
  - operations/operations-design-editing-rule
  - logs/work-record-2026-05-21-astro-portfolio-code-reduction-audit
---

# Astro Portfolio Implementation

← [[MOC/MOC-Implementation]] · [[projects/astro-portfolio]]

The Astro Portfolio rebuild keeps the visual system and public URLs from `Portfolio-main/` while converting page ownership to Astro.

## Architecture

| Layer | Path | Notes |
|-------|------|-------|
| Config | `Astro Portfolio/astro.config.mjs` | Static output, `site: https://lucakosowski.com`, no base path, `build.format: preserve` so root portfolio routes build as `.html` files while nested showcase routes keep directory indexes. |
| Shared layout | `Astro Portfolio/src/layouts/BaseLayout.astro` | Portfolio metadata, fonts, header/footer, global CSS link, GoatCounter. |
| Showcase layout | `Astro Portfolio/src/layouts/ShowcaseLayout.astro` | Standalone `/website-development/` chrome and showcase CSS. |
| Page routes | `Astro Portfolio/src/pages/` | Keeps `/projects.html`, `/articles.html`, `/references.html`. |
| Content data | `Astro Portfolio/src/data/` | Shared content arrays and demo metadata where used. |
| Stable assets | `Astro Portfolio/public/` | PDFs, images, CSS, CNAME, screenshot previews, selected demo assets, and the Bizwholistic case-study screenshot. |

## Home Preview Interaction

The home `Website Development Showcase` preview must not use abstract rectangles. It uses real screenshots under `Astro Portfolio/public/website-development/assets/site-previews/`.

- Default state: `.showcase-shot` cards have `showcaseRotate` installed but paused at matching keyframe offsets, while `showcaseFloat` keeps slow vertical motion running.
- Hover/focus state: `.preview-card--showcase:hover .showcase-shot` and `.showcase-bridge:hover .showcase-shot` change only `animation-play-state` to `running, running`, avoiding sudden jumps caused by animation-name swaps.
- The home preview and Projects page `showcase-bridge__visual` use a six-image teaser orbit: Bizwholistic, Mosaic Content Studio, Verde Lunch Club, Harbor Legal Translation, City Lab Pop-Up, and Mila Yoga Reset; they do not use abstract panel placeholders. The full `/website-development/` selected-demo grid uses the same fictional demo set plus the Bizwholistic case-study card.
- Structural verifier checks that the hero focus strip is absent, no `showcase-thumb span` placeholders return, the Projects bridge has no `.panel` placeholders, screenshot references exist, and the motion CSS tokens exist.
- Rendered QA checks the real images load and that default/hover animation states are present on both the home preview and Projects bridge.

- Showcase preview orbit rule: when Luca explicitly requests an ethereal preview window, the home preview and Projects bridge use a CSS-only left/center/right screenshot orbit (`showcaseOrbit`) rather than the earlier one-in/one-out carousel. The preview window background is now a black vacuum/depth gradient (`showcaseVacuumDepth`), not a space/star/mist field. Rendered QA samples default and hover motion, requires visible cards in a bounded 2-4 range, confirms left/right cards appear, checks reduced-motion static behavior separately, and controls the orbit timeline around each 4-second stagger boundary. The orbit must pre-enter the next right-side card before the current right-side card replaces the middle card, so the left/right websites remain visible and no right-card spawn is perceptible.

- Education visual rule: the homepage education entries use three local 320x320 transparent logo-symbol assets under `public/media/education-logos/`; only compact marks are shown in badges, not full university wordmarks.


## Project Video Preview Policy

Project video previews are local clipped MP4 assets instead of YouTube iframes. The homepage uses lightweight 720p clips because those cards are small and part of initial portfolio browsing; `projects.html` uses 1080p clips for larger project-detail media. Both routes use `preload="metadata"`, no `autoplay` attribute, `muted`, `playsinline`, `IntersectionObserver` visibility-gated playback, and `prefers-reduced-motion` handling. The verifier rejects cross-route leakage: the homepage must not include the 1080p project-detail assets, and the standalone `/website-development/` surface must not load project-preview videos.

## Showcase Page Selection

The `/website-development/` route presents:
- one real case-study card: Bizwholistic, using `public/website-development/assets/site-previews/bizwholistic.jpg` and linking to `https://bizwholistic.com/`;
- five selected fictional package demo cards: Mosaic Content Studio, Verde Lunch Club, Harbor Legal Translation, City Lab Pop-Up, and Mila Yoga Reset.

The current hero is deliberately marketing-first, not implementation-first: `Your ideal website, shaped around your ambition.` is centered horizontally above a wider Bizwholistic card, avoiding the earlier cramped left-title composition. The visible hero eyebrow, hero lead, proof-contract row set, Bizwholistic kind/disclaimer lines, demos intro paragraph, footer disclaimer, separate purple double-circle decoration, visible SVG number labels, and ambient SVG/physics layer were removed after Luca rejected the technical copy density and background motion. The Bizwholistic and selected demo cards are more transparent real-glass panels (`backdrop-filter: blur(34px) saturate(1.55)` / `-webkit-backdrop-filter`) over a warm light page background. The rounded card label tabs and nav tabs keep Apple-style translucent saturation blur (`saturate(180%) blur(...)`), specular inset highlights, restrained shadows, and subtle per-tab `--tab-refract` caustic glows beneath the glass so the light background reads as refracted by each tab color. The header intentionally uses a different quieter light-glass shell with a separate rounded nav capsule instead of matching the tab shape exactly. `html` and `body` use the light theme and `overscroll-behavior: none` so forced scroll bounds stay visually coherent.

The fictional demos remain Astro-owned routes under `src/pages/website-development/demos/**/index.astro`. The live case study is a screenshot/link only, so the portfolio does not duplicate the Bizwholistic site or invent outcome metrics. Selected demo cards on `/website-development/` use one absolute overlay anchor (`.demo-card__full-link`) per card; the visible `Open full Astro demo` treatment is a non-anchor `.demo-action-label`, so the full card is clickable without nested anchors. The persistent verifier is `verify_astro_portfolio_showcase_card_links.py`, which checks structural markup and rendered desktop/mobile clicks from multiple non-CTA points on each selected card.

## Mosaic Interactive Route

The Mosaic Content Studio route (`src/pages/website-development/demos/basic/mosaic-content-studio/index.astro`) mirrors the canonical package-demo source and uses only static-safe HTML/CSS interaction. Required markers are enforced in `verify_astro_portfolio_site.py`: `data-interaction-style="css-only-floating-collage"`, `.marquee-tape`, focusable case cards, `<details>` process panels, radio inputs, `data-interactive="radio-brief-mixer"`, keyframes for `tapeMove` and `stickerDrift`, `content-visibility:auto`, `contain-intrinsic-size:360px`, `will-change:transform`, and the reduced-motion guard. The verifier also rejects the removed/heavy background elements (`.float-field`, `.float-chip`, `.float-dot`, `dotOrbit`, `floatLoose`, `bubbleBob`, `spotlightWander`, and `mix-blend-mode`), requires the marquee tape CSS block to have no `rotate()`, and requires metric bubbles to use flex centering inside a 1:1 bubble.

The `/website-development/` Mosaic showcase card uses `data-live-preview-card="mosaic-content-studio"` and a same-origin `iframe.live-demo-frame` pointed at `demos/basic/mosaic-content-studio/`. The shell remains card-sized while the iframe has a larger internal viewport (`width:192%`, `height:192%`, `transform:scale(0.52)`) so more of the actual animated website is visible in the card. Rendered QA inspects the child frame, confirms the marquee/sticker animations are running, and enforces the lightweight route budget (`0` scripts/images/iframes on the Mosaic demo and at most `3` continuously running infinite animations).

## Migration Rule

This is a true Astro rebuild. Do not serve the old root HTML files from `public/`. Portfolio pages must be generated from `.astro` route files. Static assets and per-demo CSS/image files may be passed through `public/` when stable URLs are required.

## Verification Gates

1. `npm run build` from `Astro Portfolio/`.
2. `python3 verify_astro_portfolio_site.py` from the Astro folder.
3. `python3 verify_astro_portfolio_video_loops.py`.
4. `python3 verify_astro_portfolio_performance_budget.py`.
5. `python3 verify_astro_portfolio_showcase_card_links.py --base-url http://127.0.0.1:8796`.
6. `python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796` against the local preview server.
7. Workspace wiki verifier and Graphify refresh after source/wiki changes.

→ Source baseline: [[implementation/impl-portfolio-static-site]]


## Website Development No-Floating Background Contract

The `/website-development/` route deliberately has no ambient floating SVG/physics layer now. Structural, performance, and rendered QA reject `data-ambient-geometry`, `.ambient-geometry`, `.geo-node`, `data-magnet`, `__ambientPhysics`, `ambientCanvasWrap`, and `geoFloat` remnants. The visual contract is instead a warm light gradient background, lightweight grid texture, glass cards, a distinct light header shell, rounded glass tabs, and subtle per-tab `--tab-refract` caustic glows under the nav/card label chips.
