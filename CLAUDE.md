# Website Development Agent Instructions

This folder is the working root for Luca's personal website development business:

`/Users/lucak/Website Development`

## Boot Rule

Read `wiki/index.md` first before any non-trivial work. The wiki is the routing surface for projects, operational checks, SEO, implementation notes, decisions, and handoff records.

## Work-Start Documentation

For meaningful work, create or update the relevant wiki work record before implementation. A useful work record states:

- outcome wanted
- current evidence
- intended verifier
- handoff path

Use `wiki/operations/operations-agent-work-start-documentation.md` for the protocol.

## Workspace Map

| Path | Purpose |
|------|---------|
| `Bizwholistic/` | Astro multilingual marketing site for `bizwholistic.com` |
| `Portfolio-main/` | Static personal portfolio site |
| `Graphify/` | Local checkout of `safishamsi/graphify` for knowledge-graph tooling |
| `Luca Kosowski Website fees.docx` | Business offer and fee reference document |
| `wiki/` | Operating wiki and project memory |
| `.claude/` | Local agent rules, agent briefs, and verification scripts |

## Truth Rules

- Website source files outrank wiki descriptions.
- Built output in `Bizwholistic/dist/` is verification evidence only after a fresh build or explicit inspection.
- For SEO and AI-search claims, inspect `robots.txt`, sitemap output, canonical/hreflang behavior, `llms.txt`, schema, redirects, and stale URLs before recommending changes.
- Do not invent metrics, dates, client facts, prices, or search visibility claims. If the evidence is missing, mark it as a gap.

## Verification

Run this after touching `wiki/*.md`, `.claude/agents/*.md`, `.claude/rules/*.md`, or wiki verifier scripts:

```bash
bash .claude/scripts/verify_wiki.sh
```

For Bizwholistic source changes, also run:

```bash
npm run build
```

from `Bizwholistic/`.

## Graphify

Graphify is installed locally from `Graphify/` as the `graphify` CLI. The Hermes integration is recorded in `AGENTS.md`.

Use graph queries before broad file reads when `graphify-out/graph.json` exists:

```bash
graphify query "<question>"
```

Refresh the graph with the local wrapper, not raw repeated `graphify update`, so stale output is removed before rebuilding:

```bash
bash .claude/scripts/refresh_graphify_workspace.sh
```

The root `.graphifyignore` excludes `Graphify/`, `node_modules/`, and `dist/` so the graph stays focused on the website business workspace.

## Hermes

Hermes must run with this workspace as its terminal cwd:

`/Users/lucak/Website Development`

If a Hermes session starts somewhere else, check `HERMES.md` and `wiki/operations/operations-hermes-website-development.md`.

Because the workspace path contains a space, terminal commands must either use relative paths from the workspace cwd or quote the absolute path, for example:

```bash
ls "package-demo-pages/basic"
ls "/Users/lucak/Website Development/package-demo-pages/basic"
```
