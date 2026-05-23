---
type: operation
description: Standing rule for every Website Development design-editing session
status: active
last_updated: 2026-05-21
tags: [operation, rule, design-editing, web-design]
verifier: bash .claude/scripts/verify_wiki.sh
related: [logs/work-record-2026-05-21-astro-portfolio-preview-motion, MOC/MOC-Operations, projects/astro-portfolio]
---

# Design Editing Rule

← [[MOC/MOC-Operations]]

This is the standing rule for every design-editing session in this workspace. It must be curated after each substantial design pass, especially when Luca says a design works, does not work, feels janky, feels empty, looks too AI-generated, lacks pictures, or needs more business-specific detail.

## Rule

Before editing visual design, do four things:

1. Read [[index]] and the relevant project/implementation page.
2. Read the most recent relevant design-session log.
3. Create or update a work record with outcome, evidence, verifier, and handoff path.
4. Define what rendered evidence will prove the design improved: screenshot/contact sheet, browser geometry, section count, asset load, local-link check, and/or a project-specific structural verifier.

After editing visual design, do five things:

1. Run the structural verifier for the target pages.
2. Run rendered desktop/mobile QA, not just code inspection.
3. Record what worked and what failed in the work record or this rule.
4. Ask Luca a focused why-question when his feedback reveals a new taste rule that is not yet captured here.
5. Run `bash .claude/scripts/verify_wiki.sh` if any wiki or rule file changed.

## Current Design Lessons

- Real-world visual evidence beats abstract decorative cards. When a page feels empty, add relevant photos, maps, dossiers, product scenes, ledgers, calendars, route diagrams, or other proof objects.
- For website-development portfolio showcases, rendered screenshots of the actual pages are the proof object. Abstract browser mockups or CSS pseudo-thumbnails can still read as empty; generate local screenshots from the real static pages and commit them as preview assets.
- Home-page preview cards should not show abstract empty rectangles for website work. Use real screenshot thumbnails by default, then add calm motion: slow floating in the resting state and rotation/cycling on hover or keyboard focus.
- Avoid hover-state jumps in portfolio motion: do not swap to a different `animation-name` on hover if the resting state has carefully positioned elements. Install the rotating animation at rest, pause it at matching keyframe offsets, keep calm float motion running, and let hover/focus change only `animation-play-state`.
- Reuse approved screenshot motion systems across related entry points. If the home preview uses a real website screenshot collage, the Projects bridge for the same showcase should use the same evidence-rich visual language rather than separate abstract panels.
- Screenshot carousel motion should be one-in/one-out, not a fan stack. Non-active cards should be fully transparent/off-canvas; at rest and during hover, QA should prove no more than one card is visibly present above the chosen opacity threshold.
- Portfolio project cards that represent videos should behave like premium local video previews, not static posters or visible YouTube widgets. Use muted clipped MP4 files with explicit source start/end metadata, a poster fallback, cover-cropped framing, and a fade-reset loop; no visible play button, red dot, or timestamp badge unless Luca asks for controls. Keep route payloads separate: homepage previews can be 720p/480p and visibility-gated; full project-detail videos can use 1080p only on `projects.html`. Do not preload/prefetch heavy showcase or project assets across routes. See [[logs/work-record-2026-05-21-astro-portfolio-project-video-loops]].
- Generic gradients and glossy cards often read as AI-generated. Use domain-specific composition instead: a legal desk for translation, a garden/menu/map for a cafe, a route board for commute analytics, a grant table/report spread for a foundation.
- Structural verifier PASS is necessary but not enough. Luca may reject a page that is technically valid but visually thin, too playful, too abstract, low contrast, or missing believable business texture.
- Preserve approved pages or approved directions. Do not average them into a new style just because another page is being fixed.
- Use shared briefs for design specialists, then reconcile. Divergent opinions are useful; the final implementation must choose, not blend everything indiscriminately.
- For portfolio/showcase work, a sparse gallery shell works only if the showcased pieces have strong visuals and the interaction is discoverable. Add subtle controls, readable labels, and a simpler mobile stack.
- KSW-style inspiration means: one dominant project, muted neighboring cards, oversized clean typography, minimal chrome, category pills, and gallery pacing. It does not mean copying the exact site or hiding navigation so much that users cannot browse.

## Questions To Ask Luca When Feedback Arrives

Use these only when the answer is not obvious from the rendered page:

- What made this feel empty: missing images, weak hierarchy, too little copy, or lack of business-specific proof?
- Which part feels AI-generated: color, copy, card layout, fake metrics, or generic iconography?
- What should be preserved from the current direction before I rebuild anything?
- Should the page feel more editorial, more operational, more premium, more local, or more technical?
- Which one page in the current batch is the reference standard for the others?

## Closeout Checklist

- [ ] Work record updated with final evidence.
- [ ] This page updated if a new durable lesson was learned.
- [ ] Browser QA or screenshot evidence captured for changed pages.
- [ ] `bash .claude/scripts/verify_wiki.sh` returns `VERDICT: PASS -- safe to proceed.`

→ All operations: [[MOC/MOC-Operations]]
