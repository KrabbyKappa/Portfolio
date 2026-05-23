---
name: website-deployment-guide
description: Step-by-step guide for deploying the Astro Portfolio to GitHub Pages — source restoration, build, commit, and push pipeline.
version: 1.0.0
last_updated: 2026-05-23
type: guide
tags: [website, astro, github-pages, deploy]
related: [projects/astro-portfolio.md]
---

# Website Deployment Guide — Astro Portfolio

## What gets deployed

The deployed site at **https://lucakosowski.com/** is a static Astro build served via GitHub Pages from the `main` branch of `https://github.com/KrabbyKappa/Portfolio.git`.

GitHub Pages is configured to serve from the `/docs` folder on `main`.

## Source vs. build output

| Layer | Location | Role |
|-------|----------|------|
| **Source** | `Astro Portfolio/src/pages/` | `.astro` files — edit these |
| **Build config** | `Astro Portfolio/astro.config.mjs` | Sets `outDir: './docs'` |
| **Build output** | `Astro Portfolio/docs/` | Static HTML — what GitHub Pages serves |
| **CNAME** | `Astro Portfolio/docs/CNAME` | `lucakosowski.com` — must be in docs/ after build |

## Deploy step by step

### Step 1 — Confirm source files exist

Before editing or building, verify the `.astro` source files are present:

```bash
ls "Astro Portfolio/src/pages/"
# Expected: articles.astro  index.astro  projects.astro  references.astro  website-development/
```

If the `src/pages/` directory is empty or missing `.astro` files, the source was likely wiped (see [[#Source recovery from wiki-temp branch]]).

### Step 2 — Make your edits

Edit the relevant `.astro` file in `Astro Portfolio/src/pages/`. For wording changes to the index page, edit:

```
Astro Portfolio/src/pages/index.astro
```

### Step 3 — Build

```bash
cd "Astro Portfolio"
npm install      # only if node_modules is missing
npm run build
```

Output lands in `Astro Portfolio/docs/`. The build:
- Compiles all `.astro` files to static HTML
- Copies `public/` assets
- Writes `CNAME` to docs/ (carried from `public/CNAME` or direct copy)

**Verify the build produced `docs/index.html`:**
```bash
ls "Astro Portfolio/docs/index.html" && echo "BUILD OK"
```

### Step 4 — Commit

```bash
cd /Users/lucak/Website\ Development
git add -A
git commit -m "your commit message here"
```

The `git add -A` stages both source changes and the rebuilt `docs/` output.

### Step 5 — Push

```bash
git push origin main
```

GitHub Pages automatically rebuilds from the updated `/docs` folder. It typically takes 30–60 seconds.

### Step 6 — Verify

```bash
curl -s -o /dev/null -w "%{http_code}" https://lucakosowski.com/
# 200 = live, 404 = not updated yet, 000 = DNS/propagation issue
```

## Source recovery from wiki-temp branch

**What happened (2026-05-23):** A `git reset --hard origin/main` wiped the `Astro Portfolio/src/pages/` source files while preserving the `dist/` and `docs/` build output. The `.astro` source files were restored from the `wiki-temp` branch.

### The recovery commands

```bash
cd /Users/lucak/Website\ Development

# Verify wiki-temp branch exists and has the source
git branch -a | grep wiki-temp

# Restore all .astro source files from wiki-temp
git checkout wiki-temp -- "Astro Portfolio/src/pages/index.astro" \
                          "Astro Portfolio/src/pages/articles.astro" \
                          "Astro Portfolio/src/pages/projects.astro" \
                          "Astro Portfolio/src/pages/references.astro"

# Verify
ls "Astro Portfolio/src/pages/"

# Rebuild from restored source
cd "Astro Portfolio"
npm install && npm run build

# Commit and push
cd ..
git add -A
git commit -m "restore Astro source from wiki-temp"
git push origin main
```

### Why wiki-temp?

The `wiki-temp` branch (`eb447bd`, "wording refresh, full Astro Portfolio source") was created to hold the complete Astro Portfolio source. It is NOT the same as `main` — `main` had been reset to only contain the built `docs/` output without the `.astro` source files.

**Always keep the source files on `main` going forward.** The `.gitignore` at repo root intentionally ignores `node_modules/`, `dist/`, `.astro/`, and `.agent-artifacts/` but keeps the source (`src/`) and built output (`docs/`) tracked.

## Preventing source loss

The repo root `.gitignore` correctly ignores build artifacts. The danger is `git reset --hard` to a commit that only has the build output. Mitigation:

1. **Never `git reset --hard` to an old commit without checking what it contains:**
   ```bash
   git log --oneline -5
   git show --stat <commit>  # check for src/ content before resetting
   ```

2. **The `wiki-temp` branch always holds the full source.** Treat it as a backup.

3. **After any `git reset --hard` or force-push, immediately verify source files exist:**
   ```bash
   ls "Astro Portfolio/src/pages/index.astro"
   ```

## Current state (2026-05-23)

| Item | Value |
|------|-------|
| Remote | `https://github.com/KrabbyKappa/Portfolio.git` |
| Branch | `main` |
| Last deploy commit | `7df2b3c` |
| Last push | Sat May 23 16:38 UTC |
| Live site | https://lucakosowski.com/ → **HTTP 200** |
| CNAME | `lucakosowski.com` in `docs/CNAME` |
| Source | `Astro Portfolio/src/pages/` — .astro files present |
| Build output | `Astro Portfolio/docs/` |

## Astro config reference

```js
// Astro Portfolio/astro.config.mjs
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lucakosowski.com',
  outDir: './docs',      // GitHub Pages serves /docs
  output: 'static',
  compressHTML: false,
  build: {
    format: 'preserve',
  },
});
```

## package.json scripts

```json
{
  "scripts": {
    "dev": "astro dev",
    "start": "astro dev",
    "build": "astro build",
    "preview": "astro preview",
    "astro": "astro"
  }
}
```

## GitHub Pages configuration

- **Repository:** `KrabbyKappa/Portfolio`
- **Branch:** `main`
- **Folder:** `/docs`
- **Custom domain:** `lucakosowski.com`
- **CNAME file:** `docs/CNAME` must contain `lucakosowski.com`

The CNAME file is generated by Astro from `public/CNAME` during build.