---
type: work-record
description: Step-by-step guide for building and pushing the Astro Portfolio to GitHub Pages
last_updated: 2026-05-23
tags: [work-record, deployment, astro, github-pages, push]
related:
  - projects/astro-portfolio
  - implementation/impl-astro-portfolio
  - operations/operations-hermes-website-development
---

# Work Record: Astro Portfolio Push / GitHub Pages Deployment

## Context

Luca made wording adjustments to `src/pages/index.astro`. The changes are currently unstaged in the working tree.

**Current git state (2026-05-23):**
```
Unstaged modifications:
  M Astro Portfolio/.gitignore
  M astro.config.mjs
  M src/pages/index.astro

Unstaged deletions (verifier scripts staged for deletion):
  D Astro Portfolio/verify_astro_portfolio_*.py

Nothing staged or committed yet.
```

The Astro Portfolio project:
- Lives in `Astro Portfolio/` inside the main repo at `/Users/lucak/Website Development`
- Remote: `https://github.com/KrabbyKappa/Portfolio.git`
- Branch: `main`
- Build output goes to `Astro Portfolio/docs/` (configured via `outDir: './docs'` in `astro.config.mjs`)
- `docs/` contains `.nojekyll` and `CNAME` (lucakosowski.com) — ready for GitHub Pages

## Push / Deploy Step-by-Step

### Step 1 — Understand what gets pushed

The `.gitignore` in `Astro Portfolio/` has been rewritten to whitelist the built output. This means if you push the source + built output to GitHub, GitHub Pages can serve `docs/` directly as a static site at `lucakosowski.com`.

**What travels to GitHub:**
- Full Astro source in `Astro Portfolio/`
- Built static site in `Astro Portfolio/docs/`
- NOT: `node_modules/`, `dist/` (legacy), `.astro/` cache, `.DS_Store`

### Step 2 — Stage and commit Luca's wording changes

```bash
cd /Users/lucak/Website Development
git add src/pages/index.astro
git commit -m "portfolio: wording refresh on index page"
```

### Step 3 — Handle verifier deletion

The verifiers are staged for deletion (deleted from index). Commit that:

```bash
git add Astro\ Portfolio/verify_astro_portfolio_*.py
git commit -m "portfolio: remove archived verifier scripts"
```

Alternatively, restore them if you want to keep them:

```bash
git restore --staged Astro\ Portfolio/verify_astro_portfolio_*.py
git restore Astro\ Portfolio/verify_astro_portfolio_*.py
```

### Step 4 — Stage and commit config changes

```bash
git add Astro\ Portfolio/.gitignore astro.config.mjs
git commit -m "portfolio: update .gitignore and ensure docs/ outDir"
```

### Step 5 — Rebuild the Astro site

```bash
cd "/Users/lucak/Website Development/Astro Portfolio"
npm run build
```

This regenerates `docs/` with the updated index page content.

### Step 6 — Verify the built output

Check `docs/index.html` contains the new wording:

```bash
grep -c "Click here if you're in need of a new website" "Astro Portfolio/docs/index.html"
```

Should return `1` or more.

### Step 7 — Push to GitHub

```bash
git push origin main
```

This pushes source + `docs/` to the `main` branch on GitHub.

### Step 8 — Configure GitHub Pages (one-time)

If not already configured:
1. Go to `https://github.com/KrabbyKappa/Portfolio/settings/pages`
2. Under **Source**, select **Deploy from a branch**
3. Branch: `main`, folder: `/docs`
4. Save

GitHub will pick up `docs/CNAME` automatically and serve at `lucakosowski.com`.

### Step 9 — Wait ~2 minutes

GitHub Pages takes 1-5 minutes to deploy. Check at `https://github.com/KrabbyKappa/Portfolio/deployments`.

### Step 10 — Verify live

Visit `https://lucakosowski.com` and confirm:
- New wording visible on the homepage hero
- CNAME resolved correctly

## Alternative: Push only docs/ to gh-pages

If you prefer keeping source and deployed output on separate branches:

```bash
# Build
cd "/Users/lucak/Website Development/Astro Portfolio"
npm run build

# Switch to gh-pages, copy docs content, push
cd /Users/lucak/Website Development
git checkout -b gh-pages
git add Astro\ Portfolio/docs/ --force
git commit -m "deploy: $(date -u +%Y-%m-%d)"
git push origin gh-pages --force
```

Then configure GitHub Pages to serve from `gh-pages` branch root.

## Current Wording Changes (diff from HEAD)

File: `src/pages/index.astro`

```diff
- <p class="hero-subtitle">Digital marketing services · legal review · diplomatic coordination</p>
- <p class="hero-lead">Multilingual professional based in Kuala Lumpur, currently providing Digital and Marketing Services for Bizwholistic Ltd. while working across Italian legal review, trust and safety operations, diplomatic project coordination, stakeholder liaison, and public-facing digital content.</p>
+ <p class="hero-lead">Multilingual professional based in Kuala Lumpur, currently providing Digital and Marketing Services for Bizwholistic Ltd. Formerly, legal operations, diplomatic project coordination, stakeholder liaison, and public-facing digital content.</p>

- <li>Provide contract digital and marketing services for Bizwholistic Ltd.</li>
+ <li>Provide digital and marketing services for Bizwholistic Ltd.</li>

- <li>Trust & Safety</li>

- <h4 class="preview-title">Website Development Showcase</h4>
- <p class="preview-description">A standalone gallery of static website package demos and verified site-building context.</p>
- <span class="preview-link">View Website Showcase</span>
+ <h4 class="preview-title">Website Development Project</h4>
+ <p class="preview-description">A selection of websites</p>
+ <span class="preview-link">Click here if you're in need of a new website</span>
```

## Verification

After push and GitHub Pages deploy:
1. Visit `https://lucakosowski.com` — homepage should show new hero wording
2. Visit `https://lucakosowski.com/index.html` — same
3. Check `https://lucakosowski.com/website-development/` — should load without errors
4. Check browser console — no JS errors
5. Run `verify_wiki.sh` to confirm wiki is still clean

---
← [[projects/astro-portfolio]] · [[implementation/impl-astro-portfolio]]