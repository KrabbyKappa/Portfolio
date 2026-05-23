---
type: log
description: Astro Portfolio source simplification and code-reduction audit
last_updated: 2026-05-21
tags: [log, portfolio, astro, refactor, audit]
date: 2026-05-21
status: complete
related:
  - projects/astro-portfolio
  - implementation/impl-astro-portfolio
  - operations/operations-design-editing-rule
---

# Astro Portfolio Code Reduction Audit

← [[projects/astro-portfolio]] · [[implementation/impl-astro-portfolio]]

## Outcome wanted

Find how much source code can be removed or consolidated while preserving the current Astro Portfolio look, feel, route behavior, video-preview behavior, showcase behavior, and verifier contract.

Ladder target:
- 10% source reduction: required if safe.
- 20% source reduction: ideal.
- 50% source reduction: exceptional, only if it preserves behavior through generated/data-driven components rather than visual loss.

## Evidence gathered

- Boot docs read: `CLAUDE.md`, `AGENTS.md`, `wiki/index.md`.
- Project docs read: [[projects/astro-portfolio]] and [[implementation/impl-astro-portfolio]].
- Graph query run: `graphify query "Astro Portfolio code reduction duplicate CSS components verifiers"`.
- Three read-only reduction audits run: one GPT-class architecture pass and two MiniMax passes.
- Fresh build run from `Astro Portfolio/`: Astro CLI reported `astro v5.18.1`; `npm run build` built 15 pages.
- Baseline verifiers run after the audit:
  - `python3 verify_astro_portfolio_site.py` → `VERDICT: PASS`
  - `python3 verify_astro_portfolio_video_loops.py` → `VERDICT: PASS`
  - `python3 verify_astro_portfolio_performance_budget.py` → `VERDICT: PASS`
  - `python3 verify_astro_portfolio_visual_qa.py --base-url http://127.0.0.1:8796` → `VERDICT: PASS`

## Baseline counts

Scope used for the active website source baseline excludes `node_modules/`, `dist/`, binary assets, generated preview artifacts, and `package-lock.json`.

| Scope | Files | Lines | Nonblank lines | Bytes |
|-------|------:|------:|---------------:|------:|
| Active Astro Portfolio source | 51 | 7,290 | 6,851 | 332,543 |
| Active source + local verifiers | 55 | 8,517 | 7,962 | 399,288 |

Category breakdown inside the active source baseline:

| Category | Files | Lines |
|----------|------:|------:|
| `src/` Astro/TS source | 20 | 2,745 |
| Portfolio global CSS | 1 | 1,024 |
| Showcase global CSS | 1 | 505 |
| Demo public CSS/SVG/HTML | 26 | 2,985 |
| Config | 3 | 31 |

Legacy/non-active duplicate text also exists in the workspace:

| Folder | Files | Lines | Notes |
|--------|------:|------:|-------|
| `Portfolio-main/` | 5 | 1,630 | Old flat static portfolio, not the active Astro build. |
| `package-demo-pages/` | 87 | 10,354 | Separate demo/oracle project; many pages duplicate Astro Portfolio demo route bodies exactly. |

## Verified reduction candidates

| Candidate | Estimated net reduction | Risk | Notes |
|-----------|------------------------:|------|-------|
| Remove unused `src/components/StaticBody.astro` and unused `src/data/demos.ts`; inline the single `site.goatCounter` value and remove unused fields from `src/data/site.ts` | 20-30 lines | Very low | `StaticBody` has no references. `demoSlugs` appears only in its own file. Only `site.goatCounter` is used exactly. |
| Move identical root header/footer into `BaseLayout.astro` | about 60 lines | Low | The four root pages have exactly identical 18-line headers and 3-line footers. |
| Move mobile-menu script into `BaseLayout.astro` | about 55-65 lines | Low | The same mobile nav logic appears on all four root pages. |
| Extract shared video-loop script into one inline Astro component used by home/projects | about 55-65 lines | Low-medium | The video behavior block is duplicated almost exactly on home/projects. Keep it inline in built HTML so existing verifiers still find `IntersectionObserver`, `rootMargin: '160px 0px'`, and reduced-motion behavior. |
| Extract duplicated five-image showcase thumbnail stack into a component | about 10-20 lines | Low | Preserve class names: `showcase-thumb`, `showcase-thumb--bridge`, `showcase-shot`, and numbered shot modifiers. |
| Extract common demo document shell into a demo layout | about 100-130 lines | Low-medium | Ten demo route files have about 177 repeated head/body/footer shell lines. Preserve per-demo body attributes, titles, descriptions, local `styles.css`, and favicon links. |
| Data-drive portfolio repeated cards/sections | 120-180 lines | Medium | Requires strict generated HTML/content comparison for anchors, order, copy, and video route split. |
| Consolidate verifier constants/common helpers | 80-150 lines if verifier code counts | Low to site, medium to QA harness | Does not change website output; must preserve the four PASS scripts and all route/video budget checks. |

## Negative findings

- Exact duplicate text groups inside the active Astro Portfolio source: 0.
- Static class-selector dead CSS found by generated-HTML scan: 0 obvious selectors. Do not assume `public/styles.css` or demo CSS can be safely pruned without browser proof.
- Cross-demo CSS consolidation is risky: the demo stylesheets carry intentionally different visual signatures. Reset-only extraction may be possible but should not be counted as a large safe win.
- CSS minification would reduce line count but is not a real simplification and hurts maintainability; do not count it.

## Ladder verdict

| Ladder | Verdict | What it would mean |
|--------|---------|--------------------|
| 10% active-source reduction | Plausible but not automatic | Needs the low-risk shared-layout/script/component pass plus some data-driven refactor or verifier consolidation. The no-visual-change safe floor is closer to 4-7% before touching content data or verifier structure. |
| 20% active-source reduction | Possible only with a deeper architecture pass | Likely needs data-driven demo/source generation, shared verifier helpers, and careful demo layout work. Requires before/after HTML and browser QA for all routes. |
| 50% active-source reduction | Not safe | The active site is demo-heavy. Removing half the active source would almost certainly delete demo visual signatures, route content, or verification coverage. |
| 20-50% workspace text reduction | Technically possible but a product/archive decision | `package-demo-pages/` and `Portfolio-main/` are not required by the active Astro build, but they are reference/oracle/history surfaces. Archive/delete only after an explicit decision that those references are no longer needed. |

## Recommended implementation order

1. Build a dedicated branch/worktree or use exact-path staging because the main workspace currently has unrelated dirty package-demo/showcase edits.
2. First pass: remove dead files and centralize root header/footer/mobile nav/video loop/showcase thumbnail components.
3. Verify with the full active gate: build, structural, video-loop, performance-budget, rendered QA.
4. Second pass: demo document layout extraction, with all ten demo routes visually checked on desktop and mobile.
5. Third pass only if still needed: data-driven cards/sections and verifier helper consolidation.

## Do not touch without explicit approval

- Local project-preview MP4/poster assets and route-split behavior.
- The 15 built routes and their public URLs.
- The one-in/one-out screenshot carousel class/token contract.
- The Mosaic live same-origin iframe preview behavior.
- `Portfolio-main/` and `package-demo-pages/` deletion/archive decisions.

## Closeout verifier

After writing this work record, run:

```bash
bash .claude/scripts/verify_wiki.sh
```
