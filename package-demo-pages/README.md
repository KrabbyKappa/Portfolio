# Website Package Demo Pages

Fictional static demo pages generated from the Micro and Basic package specs plus the external template library. City Lab is preserved as the approved Micro visual reference, Mosaic remains the protected Basic creative reference, and the other pages were rebuilt or photo-rescued after Luca correction as distinct graphical prototypes.

## Pages

- `micro/riverside-bike-rescue/index.html` — Micro — Riverside Bike Rescue — Mobile bicycle repair — style `photo-rescued mobile mechanic dispatch card with real repair/workshop imagery`
- `micro/northstar-notary-proof/index.html` — Micro — Northstar Notary Desk — Temporary notary proof page — style `notary-ledger-grid / seal-stack document desk`
- `micro/mila-yoga-testimonial/index.html` — Micro — Mila Yoga Reset — Solo wellness testimonial page — style `wellness-breath-orbit / soft circular ritual page`
- `micro/lumo-desk-lamp-teaser/index.html` — Micro — Lumo Desk Lamp — Single-product teaser — style `product-night-stage / dark cinematic lamp launch`
- `micro/city-lab-pop-up/index.html` — Micro — City Lab Pop-Up — Short-term workshop/event page — style `event-poster-system / fluorescent Swiss poster`
- `basic/harbor-legal-translation/index.html` — Basic — Harbor Legal Translation — Legal translation consultant — style `translation-dossier-editorial / certified case file`
- `basic/verde-lunch-club/index.html` — Basic — Verde Lunch Club — Local lunch and catering brand — style `food-menu-market / chalkboard counter menu`
- `basic/mosaic-content-studio/index.html` — Basic — Mosaic Content Studio — Small creative/content agency — style `creative-sticker-chaos / cut-paper studio collage`
- `basic/clearpath-commute-analytics/index.html` — Basic — ClearPath Commute Analytics — B2B commute analytics product — style `saas-dashboard-blueprint / transit console`
- `basic/atlas-family-foundation/index.html` — Basic — Atlas Family Foundation — Small nonprofit/foundation presence — style `foundation-impact-brochure / grant ledger brochure`

## Corrective workflow

- Kanban board: `.harness/kanban/package-demo-uniqueness/`.
- Scratch worktrees: `.harness/worktrees/package-demo-uniqueness/wt-*`.
- MiniMax M2.7 concept reports: `.harness/kanban/package-demo-uniqueness/agent-reports/*-m2-concept.md`.
- GPT-5.5 final/taste reports: `.harness/kanban/package-demo-uniqueness/agent-reports/*-gpt55-final.md`.
- Apply script: `.harness/kanban/package-demo-uniqueness/apply_unique_rewrites.py`.
- Structural verifier: `python3 package-demo-pages/verify_demo_pages.py`.
- Uniqueness verifier: `python3 package-demo-pages/verify_demo_uniqueness.py`.
- Polish verifier: `python3 package-demo-pages/verify_demo_polish.py`.

## Scope guardrails

- All names, quotes, contacts, and business details are fictional placeholders.
- Micro examples: one page, direct contact links, no forms, no analytics, no CMS.
- Basic examples: one static page, direct contact links, basic metadata, no backend by default.
- These are design/package examples, not live client sites.
