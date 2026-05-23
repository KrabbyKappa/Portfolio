---
type: log
description: Work record for Astro Portfolio local project video preview loops
last_updated: 2026-05-21
tags: [log, portfolio, astro, design-editing, video-preview, verification]
date: 2026-05-21
related:
  - projects/astro-portfolio
  - implementation/impl-astro-portfolio
  - operations/operations-design-editing-rule
---

# Work Record: Astro Portfolio Project Video Loops

← [[projects/astro-portfolio]] · [[operations/operations-design-editing-rule]]

## Outcome wanted

Luca wants the Astro Portfolio home-page Projects preview cards to show looping video previews rather than only static YouTube thumbnails:

- Italian National Day 2025 should show the `hz1xPkvdhcI` YouTube video as a calm muted loop using the opening 15 seconds, with a fade-out/fade-in reset.
- Perché ci siamo noi should show the `yUjjPUTrvt0` YouTube video looped from 1:50 to 2:13, also as a muted preview loop.

The preview cards must still route to the full project sections on `projects.html`.

## Current evidence

- Target project folder: `/Users/lucak/Website Development/Astro Portfolio`.
- Source route: `Astro Portfolio/src/pages/index.astro`, section `#projects`.
- Shared CSS: `Astro Portfolio/public/styles.css`.
- Full project-detail videos on `Astro Portfolio/src/pages/projects.astro` are local, muted, visibility-gated MP4 loops rather than external YouTube iframes.
- Existing rendered QA already checks the homepage and Projects page at mobile and desktop viewports.

## Intended verifier

1. `npm run build` from `Astro Portfolio/`.
2. `python3 verify_astro_portfolio_site.py` from `Astro Portfolio/`.
3. `python3 verify_astro_portfolio_video_loops.py` from `Astro Portfolio/`.
4. `python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796` against the local preview server.
5. Browser DOM/visual check on `http://127.0.0.1:8796/#projects`.
6. `bash .claude/scripts/verify_wiki.sh`.
7. `bash .claude/scripts/refresh_graphify_workspace.sh`.

## Implementation decision

For premium speed on the free GitHub Pages portfolio, local clipped MP4s are preferred over preloading YouTube iframes. YouTube embeds would add third-party JS, connection waterfalls, widget chrome risk, and less control over fade/reset timing. Local clips add repository/bandwidth weight, so the implementation splits by route and quality:

- `index.html` homepage cards use lightweight 720p files only:
  - `media/project-previews/italian-national-day-2025-preview-720.mp4`
  - `media/project-previews/perche-ci-siamo-noi-110-133-preview-720.mp4`
- `projects.html` project-detail cards use 1080p files because they are larger on the page and only load on that route:
  - `media/project-previews/italian-national-day-2025-loop-1080.mp4`
  - `media/project-previews/italian-national-day-2024-loop-1080.mp4`
  - `media/project-previews/perche-ci-siamo-noi-110-133-loop-1080.mp4`
- All preview loops use `preload="metadata"`, no `autoplay` attribute, `muted`, `playsinline`, `IntersectionObserver` visibility-gated playback, and a reduced-motion guard.
- `website-development/` is treated as a separate site surface; it should not load project-preview videos or the portfolio stylesheet. The homepage may show small screenshot thumbnails for the showcase bridge, but it must not preload demo pages or demo CSS.

GitHub Pages free-hosting constraints recorded during this pass: published Pages sites may be no larger than 1 GB, and Pages has a soft bandwidth limit of 100 GB/month. The local verifier keeps the built site well below those limits.

## Status

Implemented 2026-05-21. Pending final verifier pass and local commit.
