---
type: business
description: Static demo page library for Micro and Basic website packages
last_updated: 2026-05-21
tags: [business, package-demos, frontend, templates, static-pages]
source_file: graphify-out/converted/Luca Kosowski Website fees_cd1a932d.md
related_files:
  - package-demo-pages/index.html
  - package-demo-pages/README.md
  - package-demo-pages/verify_demo_pages.py
  - package-demo-pages/verify_demo_uniqueness.py
  - package-demo-pages/verify_demo_polish.py
  - .harness/kanban/package-demo-uniqueness/apply_unique_rewrites.py
  - .harness/kanban/package-demo-uniqueness/run_m2_concept_agents.py
  - .harness/kanban/package-demo-uniqueness/run_gpt55_final_agents.py
  - .claude/agents/frontend-template-strategist.md
  - .claude/agents/frontend-visual-systems-designer.md
  - .claude/agents/static-page-implementer.md
  - .claude/agents/package-scope-copy-guardian.md
  - .claude/agents/static-page-responsive-qa.md
related:
  - business/business-service-offers
  - business/website-spec-micro
  - business/website-spec-basic
  - reference/external-website-template-library-2026-05-20
  - logs/work-record-2026-05-20-package-demo-pages
---

# Website Package Demo Pages

← [[MOC/MOC-Business]] · [[business/business-service-offers]]  
Work records: [[logs/work-record-2026-05-20-package-demo-pages]], [[logs/session-handoff-2026-05-20-package-demo-polish]], [[logs/session-handoff-2026-05-20-basic-photo-rebuild]]

This page records the static demo-page library for Luca's Micro and Basic website packages. The pages are fictional package examples, not live client sites. They show how `Micro Website - Emergency / testimonial` and `Simple Website` fee-sheet scope becomes concrete static HTML/CSS.

## Source Inputs

- Fee extraction: `graphify-out/converted/Luca Kosowski Website fees_cd1a932d.md`.
- Micro package spec: [[business/website-spec-micro]].
- Basic/Simple package spec: [[business/website-spec-basic]].
- External section/template patterns: [[reference/external-website-template-library-2026-05-20]].
- Local reference projects: [[projects/bizwholistic]] and [[projects/portfolio-main]].

## Specialized Frontend Agent Files

| Agent file | Purpose |
|------------|---------|
| `.claude/agents/frontend-template-strategist.md` | Maps a brief to the correct package tier, template family, section order, contact method, and exclusions. |
| `.claude/agents/frontend-visual-systems-designer.md` | Defines package-feasible visual systems from Bizwholistic, Portfolio-main, and external template patterns. |
| `.claude/agents/static-page-implementer.md` | Builds scoped plain HTML/CSS pages with semantic markup and direct-contact links. |
| `.claude/agents/package-scope-copy-guardian.md` | Reviews copy against fee-sheet constraints so pages do not overpromise. |
| `.claude/agents/static-page-responsive-qa.md` | Verifies static pages for structure, responsive risks, accessibility basics, and package-scope compliance. |

## Corrective Design Workflow

Initial corrective pass: Luca accepted `package-demo-pages/micro/riverside-bike-rescue/index.html` as the first usable reference and rejected the other nine pages as too similar. Later visual QA changed the current state: `package-demo-pages/micro/city-lab-pop-up/` is the preserved approved Micro reference, `package-demo-pages/basic/mosaic-content-studio/` is protected as the approved Basic creative reference, and Riverside was later rebuilt/photo-rescued with real bicycle repair imagery. The corrective passes used:

- Kanban board: `.harness/kanban/package-demo-uniqueness/`.
- Scratch worktrees: `.harness/worktrees/package-demo-uniqueness/wt-*`.
- MiniMax M2.7 concept reports: `9` files in `.harness/kanban/package-demo-uniqueness/agent-reports/*-m2-concept.md`.
- GPT-5.5 final/taste reports: `9` files in `.harness/kanban/package-demo-uniqueness/agent-reports/*-gpt55-final.md`.
- Apply script: `.harness/kanban/package-demo-uniqueness/apply_unique_rewrites.py`.

## Demo Page Index

Root index:

- `package-demo-pages/index.html`

### Micro pages

| Demo | Business type | Style direction | Path |
|------|---------------|-----------------|------|
| Riverside Bike Rescue | Mobile bicycle repair | Photo-rescued mobile mechanic dispatch card with real bicycle repair/workshop imagery | `package-demo-pages/micro/riverside-bike-rescue/index.html` |
| Northstar Notary Desk | Temporary notary proof page | `notary-ledger-grid`: seal-stack document desk and ledger grid | `package-demo-pages/micro/northstar-notary-proof/index.html` |
| Mila Yoga Reset | Solo wellness testimonial page | `wellness-breath-orbit`: soft circular ritual/wellness page | `package-demo-pages/micro/mila-yoga-testimonial/index.html` |
| Lumo Desk Lamp | Single-product teaser | `product-night-stage`: dark cinematic product stage | `package-demo-pages/micro/lumo-desk-lamp-teaser/index.html` |
| City Lab Pop-Up | Short-term workshop/event page | `event-poster-system`: fluorescent Swiss poster/ticket system | `package-demo-pages/micro/city-lab-pop-up/index.html` |

### Basic pages

| Demo | Business type | Style direction | Path |
|------|---------------|-----------------|------|
| Harbor Legal Translation | Legal translation consultant | `translation-dossier-editorial`: certified legal case-file layout | `package-demo-pages/basic/harbor-legal-translation/index.html` |
| Verde Lunch Club | Local lunch/catering brand | `food-menu-market`: warm chalkboard/menu counter system | `package-demo-pages/basic/verde-lunch-club/index.html` |
| Mosaic Content Studio | Small creative/content agency | `creative-sticker-chaos`: sticker/cut-paper creative studio collage | `package-demo-pages/basic/mosaic-content-studio/index.html` |
| ClearPath Commute Analytics | B2B commute analytics product | `saas-dashboard-blueprint`: dark transit dashboard console | `package-demo-pages/basic/clearpath-commute-analytics/index.html` |
| Atlas Family Foundation | Small nonprofit/foundation presence | `foundation-impact-brochure`: warm grant-ledger brochure | `package-demo-pages/basic/atlas-family-foundation/index.html` |

## Verification

Structural verifier:

```bash
python3 package-demo-pages/verify_demo_pages.py
```

Observed output:

```text
Checked demo pages: 10 (micro=5, basic=5)
Checked root: /Users/lucak/Website Development/package-demo-pages
VERDICT: PASS — package demo pages are structurally scoped and static-safe
```

Uniqueness verifier:

```bash
python3 package-demo-pages/verify_demo_uniqueness.py
```

Observed output:

```text
Checked uniqueness targets: 9
VERDICT: PASS — all target demo pages have unique design signatures, archetypes, and CSS modules
```

Polish verifier:

```bash
python3 package-demo-pages/verify_demo_polish.py
```

Observed output:

```text
Checked polish targets: 8
VERDICT: PASS — requested visual polish markers are present
```

Browser render checks covered corrected target pages at mobile and desktop widths. The relevant assertion is at least one H1 per page, rendered CSS, no horizontal overflow, no too-wide elements, tap-safe/direct-contact links, and a design signature on each corrected page. Section counts intentionally vary by demo: current pages range from 6 to 11 `<section>` elements, while the uniqueness verifier requires at least six sections on target pages.

Contact-sheet visual QA reported that the corrected thumbnails look graphically distinct, with no obvious visual blockers. Later photo-led QA rebuilt the non-City-Lab Micro pages and the four non-Mosaic Basic pages with real photo/map assets; current structural, uniqueness, and polish verifiers pass together.

## Scope Guardrails

- All names, quotes, contacts, and business details are fictional placeholders.
- Micro pages: one page, direct links only, no forms, no analytics scripts, no CMS, no login, no payment flow.
- Basic pages: one static public page, direct contact links, basic metadata and `llms.txt`, no backend by default. Verde additionally includes an optional Google Maps iframe as a third-party embed; this is still static/no-backend scope, not a custom app or form workflow.
- External template library patterns were reused as section logic and visual references only; no external source code, brand assets, logos, or client copy were copied.

→ Back to offers: [[business/business-service-offers]] · [[MOC/MOC-Business]]
