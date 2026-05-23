---
type: operation
description: Graphify setup and query workflow for the Website Development workspace
last_updated: 2026-05-21
tags: [operation, graphify, knowledge-graph, hermes]
verifier: graphify --help
---

# Graphify Operations

← [[MOC/MOC-KnowledgeGraph]]

Graphify is available locally in these forms:

| Item | Path or command |
|------|-----------------|
| Source checkout | `Graphify/` |
| Installed CLI | `graphify` (`graphifyy v0.8.13` via `uv tool list`) |
| Hermes query-first rules | `AGENTS.md` |
| Ignore rules | `.graphifyignore` |
| Current graph | `graphify-out/graph.json` |
| Visual folder map | `graphify-out/GRAPH_TREE.html` |
| Integration verifier | `.claude/scripts/verify_graphify_workspace.py` |

## Install State

The CLI was installed from the local checkout with PDF and Office support:

```bash
uv tool install './Graphify[office,pdf]'
```

The Hermes integration was registered with:

```bash
graphify hermes install
```

Verified local behavior on 2026-05-20: `graphify hermes install` reports that `AGENTS.md` is the always-on mechanism for Hermes in this workspace. No separate `~/.hermes/skills/graphify` directory is expected for this installed CLI version.

## Query Workflow

When `graphify-out/graph.json` exists, prefer scoped graph queries before broad reads:

```bash
graphify query "how is Bizwholistic routing localized pages?"
graphify explain "Bizwholistic"
graphify path "robots.txt" "llms.txt"
```

After source changes, refresh the AST graph with the local wrapper (it removes stale `graph.json` before rebuilding so repeated refreshes do not accumulate duplicate links):

```bash
bash .claude/scripts/refresh_graphify_workspace.sh
```

Low-level command used by the wrapper:

```bash
graphify update . --no-cluster --force
```

The initial local graph was created with `graphify update . --no-cluster`, producing 450 nodes in `graphify-out/graph.json`. Current refreshes are run through `bash .claude/scripts/refresh_graphify_workspace.sh`; the wrapper requires a valid non-empty graph, no duplicate links, manifest coverage across the intended workspace areas, and a passing scoped query traversal.

Generate the visual folder map after a refresh:

```bash
graphify tree --graph graphify-out/graph.json --output graphify-out/GRAPH_TREE.html --root /Users/lucak/Website\ Development --label "Website Development"
```

Run the integration verifier after refreshes:

```bash
python3 .claude/scripts/verify_graphify_workspace.py
```

The verifier checks that the graph covers the intended workspace areas, that ignored dependency/vendor/generated prefixes stay excluded, that the visual tree and report artifacts exist, and that a scoped graph query returns traversal evidence.

## Ignore Policy

`.graphifyignore` excludes `.DS_Store`, `.git/`, `node_modules/`, `dist/`, `.astro/`, `graphify-out/manifest.json`, `graphify-out/cost.json`, `graphify-out/cache/`, `external-references/website-template-full-source/`, `Graphify/`, and `*.zip`. The goal is to map this website workspace, not third-party tool source, generated output/cache files, large archives, or downloaded third-party reference code.

→ All operations: [[MOC/MOC-Operations]]
