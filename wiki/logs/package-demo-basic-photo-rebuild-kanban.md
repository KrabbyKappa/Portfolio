---
type: log
description: Kanban board for the Basic package photo-led correction pass
status: complete
date: 2026-05-20
last_updated: 2026-05-20
tags: [kanban, package-demo-pages, basic-tier, photo-led-rebuild]
related: [logs/session-handoff-2026-05-20-basic-photo-rebuild]
---

# Package Demo Basic Photo Rebuild Kanban

← [[logs/session-handoff-2026-05-20-basic-photo-rebuild]]

## Board rules

- One fresh agent per card where possible.
- Cards are small, page/section-specific, and independently reviewable.
- Mosaic is protected and must not be edited.
- External anchor hrefs are not allowed by the static verifier; use embeds, local assets, mailto/tel, or hash links only.
- All changed pages need desktop and mobile browser QA.

## Checklist

| ID | Status | Agent lane | Goal | Files | Verify |
|---|---|---|---|---|---|
| BPR-01 | complete | Harbor hero photo | Replace synthetic legal visual with real handshake/legal photography and warmer composition. | `package-demo-pages/basic/harbor-legal-translation/` | Harbor screenshot desktop/mobile |
| BPR-02 | complete | Harbor proof/copy | Add meaningful legal translation proof: certified copy flow, language matrix, delivery protocol, fewer pointless buttons. | `package-demo-pages/basic/harbor-legal-translation/index.html` | `verify_demo_polish.py` Harbor checks |
| BPR-03 | complete | Harbor CSS/background | Reduce plain white sterility with editorial paper, burgundy, document-shadow, and photo integration. | `package-demo-pages/basic/harbor-legal-translation/styles.css` | desktop/mobile overflow 0 |
| BPR-04 | complete | Verde hero | Build real garden/greenery photo hero with title overlay: seasonal lunches from a small green counter. | `package-demo-pages/basic/verde-lunch-club/` | Verde screenshot desktop/mobile |
| BPR-05 | complete | Verde menu/food | Add real food photos and a stronger menu section with lunch plates, drinks, and seasonal details. | `package-demo-pages/basic/verde-lunch-club/index.html` | section count + visual QA |
| BPR-06 | complete | Verde maps | Add a real Google Maps embed for a fake/demo location while preserving verifier-safe anchors. | `package-demo-pages/basic/verde-lunch-club/index.html` | static verifier PASS |
| BPR-07 | complete | ClearPath visual direction | Make ClearPath civic/transit, not crypto: lighter background, subway-web texture, clearer route colors. | `package-demo-pages/basic/clearpath-commute-analytics/styles.css` | ClearPath screenshot desktop/mobile |
| BPR-08 | complete | ClearPath graphs | Add more charts/graphs and route explanations: colors, corridor meaning, queue pressure, relief path. | `package-demo-pages/basic/clearpath-commute-analytics/index.html` | uniqueness + polish PASS |
| BPR-09 | complete | ClearPath imagery | Add real commute/city/transit photography without overwhelming the dashboard. | `package-demo-pages/basic/clearpath-commute-analytics/` | browser image load check |
| BPR-10 | complete | Atlas imagery | Add real community/foundation photography and preserve useful existing graphics. | `package-demo-pages/basic/atlas-family-foundation/` | Atlas screenshot desktop/mobile |
| BPR-11 | complete | Atlas background/proof | Improve background warmth and proof details: grantee story, public report, applicant timeline. | `package-demo-pages/basic/atlas-family-foundation/index.html` | polish PASS |
| BPR-12 | complete | CTA/buttons | Make buttons intentional and page-specific across all four pages. | four Basic page HTML/CSS files | browser focus/tap check |
| BPR-13 | complete | Asset provenance | Download/record Unsplash image assets and add text attribution/disclosure without external href breakage. | four Basic page dirs | local file existence check |
| BPR-14 | complete | Mobile QA | Audit 390px layouts for overflow, image cropping, readable maps, and CTA stacking. | four Basic pages | DOM geometry QA |
| BPR-15 | complete | Final verifier/audit | Run structural, uniqueness, polish, wiki, graph refresh, browser console, screenshots; update this board. | workspace root | all PASS lines captured |

## Final PASS evidence

- Structural package verifier: PASS.
- Uniqueness verifier: PASS.
- Polish verifier: PASS.
- Wiki verifier: PASS.
- Graphify refresh: PASS.
- Browser QA: PASS at 390px and 1440px for Harbor, Verde, ClearPath, and Atlas.
- Servers used for QA on ports 8792 and 8793 were stopped; final listener check returned no output.

