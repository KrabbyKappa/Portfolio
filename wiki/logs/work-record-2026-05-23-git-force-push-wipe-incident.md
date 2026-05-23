---
type: work-record
description: "INTERNAL INCIDENT: force-push to origin/main wiped full Astro Portfolio source; recovered via reflog"
last_updated: 2026-05-23
tags: [work-record, incident, git, recovery, force-push]
related:
  - projects/astro-portfolio
  - implementation/impl-astro-portfolio
---

# Work Record: Git Force-Push Wipe Incident — 2026-05-23

## What Happened

**Root cause:** Someone force-pushed to `origin/main` on GitHub, replacing the full Astro Portfolio source tree with only the built static output (`docs/`). The remote `259ee03 Add files via upload` contained only the `docs/` folder — no `src/`, no `public/`, no `package.json`, no `Astro Portfolio/` source files.

**Trigger:** Running `git reset --hard origin/main` to resolve a "remote diverged" push rejection. This synced local to the stripped-down remote, wiping everything that wasn't in `docs/`.

**Files lost (temporarily):** All of `Astro Portfolio/` except the built output in `docs/`. Specifically: `src/`, `public/`, `package.json`, `astro.config.mjs`, all verifier scripts, `node_modules/`, `dist/`.

**Recovery:** The commit `77ef612` (wording refresh) still existed in local reflog even though no branch pointed to it after the reset. Used `git checkout 77ef612` to enter detached HEAD state and confirm all files were intact. Then `git checkout main` to return to the branch with full source restored.

## Prevention Rules

1. **Never `git reset --hard` to a remote branch without inspecting it first.** Always run `git log origin/main --oneline -5` and `git diff --stat main..origin/main` before resetting.
2. **Inspect what `origin/main` actually contains before any force-reset.** If it only has `docs/` and no `src/`, it's a stripped-down version — do NOT reset to it.
3. **If remote diverged, prefer `git pull` or merge, not reset.** Only reset as a last resort and only after confirming remote content is what you expect.
4. **The `.gitignore` rewrite that whitelisted `docs/` content is correct** — but it made `docs/` the only thing on the remote. This was the state that caused the wipe.

## Recovery Commands (exact sequence used)

```bash
# Step 1 — See what origin/main actually is before touching anything
git fetch origin
git log origin/main --oneline -5
# If the top commit only touches docs/ and has no Astro Portfolio/src, STOP — do not reset

# Step 2 — If you must reset and remote IS what you want
git reset --hard origin/main

# Step 3 — If you accidentally wiped the source (like this incident)
git reflog
# Find the last known good commit hash (e.g. 77ef612)
git checkout <good-hash>
# Verify all files are back (src/, public/, package.json, etc.)
ls "Astro Portfolio/"
# Then return to a branch
git checkout main
```

## After Recovery — Full Push Sequence

```bash
cd /Users/lucak/Website\ Development

# Confirm correct state
git log --oneline -3
# Should show: wording refresh, Set outDir, ...

# Ensure Astro Portfolio source is complete
cd "Astro Portfolio"
npm install
npm run build
# Confirm build has your wording
grep "Click here" docs/index.html

# Stage everything
git add -A
git commit -m "wording refresh, restore after force-push incident"

# Push — if remote diverges again, pull first instead of resetting
git pull origin main --no-rebase
git push origin main
```

## Key Files Restored

- `Astro Portfolio/src/` — all page and component source
- `Astro Portfolio/public/` — static assets, CNAME, CSS
- `Astro Portfolio/package.json` — Astro 5.x dependency
- `Astro Portfolio/astro.config.mjs` — static output, docs/ outDir
- `Astro Portfolio/node_modules/` — dependencies
- All `verify_astro_portfolio_*.py` verifier scripts

## Git State After Recovery

```
77ef612 wording refresh        ← detached HEAD used to restore
7ea7f2e Set outDir to docs
864a91f Add mobile hamburger
```

`origin/main` is still the bad stripped-down commit. Pushing `main` will override it.

---
← [[projects/astro-portfolio]] · [[MOC/MOC-Projects]]