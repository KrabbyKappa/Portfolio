---
type: log
description: Work record for Luca-requested Astro Portfolio home-page preview interaction correction
last_updated: 2026-05-21
tags: [log, portfolio, astro, design-editing, verification]
date: 2026-05-21
related:
  - projects/portfolio-main
  - operations/operations-design-editing-rule
---

# Work Record: Astro Portfolio Preview Motion Correction

← [[log]]

## Outcome wanted

Luca wants the Astro Portfolio home page to stop showing the hero focus-strip pill buttons and to replace the Website Development Showcase preview's empty abstract rectangles with real website screenshots.

The showcase preview should behave as follows:

- Default state: real website screenshots float very slowly up/down, so the preview feels alive without looking jittery.
- Hover/focus state: the preview rotates/cycles through real website screenshots inside the same card.
- The card still links users toward `projects.html#other-projects`.

## Current evidence

- Target project folder: `/Users/lucak/Website Development/Astro Portfolio`.
- Source route: `Astro Portfolio/src/pages/index.astro`.
- Shared portfolio CSS: `Astro Portfolio/public/styles.css`.
- Existing real screenshots live under `Astro Portfolio/public/website-development/assets/site-previews/`.
- Existing structural verifier: `Astro Portfolio/verify_astro_portfolio_site.py`.
- Existing rendered QA verifier: `Astro Portfolio/verify_astro_portfolio_visual_qa.py`.

## Intended verifier

1. `npm run build`
2. `python3 verify_astro_portfolio_site.py`
3. `python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796`
4. Browser/DOM check for screenshot slides, hover animation style, removed hero focus strip, and image loading.
5. `bash .claude/scripts/verify_wiki.sh`
6. `bash .claude/scripts/refresh_graphify_workspace.sh`

## Design-learning note

Luca's correction reinforces a standing rule: portfolio/showcase preview slots should use the real rendered website screenshots as proof objects. Abstract rectangles read as empty placeholders, even when they are visually styled.


## Implementation notes

- Removed the home hero `.hero-focus-strip` pill row from `Astro Portfolio/src/pages/index.astro`.
- Replaced the `showcase-thumb` empty spans with five real screenshot images from `website-development/assets/site-previews/`.
- Added slow default `showcaseFloat` motion and hover/focus `showcaseRotate` cycling in `Astro Portfolio/public/styles.css`.
- Hardened `verify_astro_portfolio_site.py` and `verify_astro_portfolio_visual_qa.py` so the removed strip, no placeholder spans, real screenshot count, default float, and hover rotation become regression gates.
- Updated hero/meta language toward the user-provided LinkedIn/Bizwholistic role and existing verified portfolio roles. Direct LinkedIn page access was auth-walled / returned LinkedIn error 999 through the reader proxy, so no unverified LinkedIn-only facts were invented.

## Final evidence

- `npm run build`: PASS, 15 pages built.
- `python3 verify_astro_portfolio_site.py`: `VERDICT: PASS — Astro Portfolio build has route, content, asset, screenshot, link, heading, CSS, and Astro-source parity`.
- `python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796`: `VERDICT: PASS — Astro Portfolio rendered QA covered 7 pages x 2 viewports with h1=1, overflowX=0, no console errors, and loaded images`.
- Rendered QA home metrics: mobile and desktop both had `heroFocusStripCount=0`, `showcaseThumbImages=5`, `showcaseThumbSpanPlaceholders=0`, `showcaseDefaultFloating=True`, `showcaseHoverRotating=True`, `unloadedImages=0`, and `overflowX=0`.
- Browser DOM check confirmed five loaded screenshot images at 1440×980 natural dimensions and zero hero focus strips.
- Browser visual inspection of the Projects section confirmed the Website Development Showcase card uses real website screenshot thumbnails rather than empty abstract rectangles.

## Status

Completed 2026-05-21 pending final git commit.


## Follow-up correction: hover continuity and Projects bridge reuse

Luca confirmed the resting animation was good but the hover state jumped. The fix was to stop swapping `animation-name` on hover. The rotate animation is now installed all the time and paused at matching keyframe offsets, while the floating animation keeps running. Hover/focus now changes only `animation-play-state` from `paused, running` to `running, running`, which preserves the current transform at hover start.

The same real-screenshot animation was also reused inside `projects.html#other-projects`, replacing the three abstract `.panel` spans in `showcase-bridge__visual`.

Verification evidence:

- `npm run build`: PASS, 15 pages built.
- `python3 verify_astro_portfolio_site.py`: PASS.
- `python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796`: PASS across 9 pages x 2 viewports.
- Playwright motion check: home and projects both reported `same_animation_name_on_hover=True` and `paused_to_running=True`; first-shot transform was unchanged immediately after hover, proving no name-swap jump.
- Browser DOM check on `projects.html#other-projects`: `bridgeImgs=5`, `panels=0`, animation names `showcaseRotate, showcaseFloat`, and default states `paused, running`.
- Browser visual inspection confirmed the Other Projects bridge now shows the real screenshot collage style instead of abstract placeholder panels.


## Follow-up correction: one-in / one-out carousel motion

Luca flagged that the screenshot cards could still overlap: the intended behavior is not a fan where one card remains in the background while another moves. The corrected motion uses one visible card at a time. Non-active cards are transparent and off-canvas; hover/focus starts the paused rotate animation while preserving the calm floating layer.

Implementation details:

- `@keyframes showcaseRotate` now gives each card one active visible window and sends it off-canvas left before the next card becomes visible.
- Five `.showcase-shot` cards remain staggered by 20% of the 12s cycle.
- The rendered QA script now samples hover motion and fails if the home preview or Projects bridge has more than one visible screenshot card above the opacity threshold.

Verification evidence:

- `npm run build`: PASS, 15 pages built.
- `python3 verify_astro_portfolio_site.py`: PASS.
- `python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796`: PASS across 9 pages x 2 viewports.
- Browser/Playwright one-in-one-out check: home `max_visible=1`, projects `max_visible=1`; both had rotate layer running on hover.
- Browser visual inspection of `projects.html#other-projects`: real screenshot card visible at rest, `panelPlaceholders=0`, and no stacked background card visible.
