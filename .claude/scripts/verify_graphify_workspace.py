#!/usr/bin/env python3
"""Verify that Graphify maps the intended Website Development workspace."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH_DIR = ROOT / "graphify-out"
GRAPH = GRAPH_DIR / "graph.json"
MANIFEST = GRAPH_DIR / "manifest.json"
TREE = GRAPH_DIR / "GRAPH_TREE.html"
REPORT = GRAPH_DIR / "GRAPH_REPORT.md"


def rel(path: str) -> str:
    p = Path(path)
    try:
        return str(p.relative_to(ROOT))
    except ValueError:
        return path


def main() -> int:
    errors: list[str] = []

    required_files = [
        "AGENTS.md",
        "CLAUDE.md",
        ".graphifyignore",
        "wiki/index.md",
        "wiki/operations/operations-graphify.md",
        "graphify-out/graph.json",
        "graphify-out/manifest.json",
        "graphify-out/GRAPH_TREE.html",
        "graphify-out/GRAPH_REPORT.md",
    ]
    for item in required_files:
        if not (ROOT / item).exists():
            errors.append(f"missing required file: {item}")

    if GRAPH.exists():
        graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    else:
        graph = {}
    if MANIFEST.exists():
        manifest_raw = json.loads(MANIFEST.read_text(encoding="utf-8"))
    else:
        manifest_raw = {}

    nodes = graph.get("nodes", [])
    links = graph.get("links", graph.get("edges", graph.get("hyperedges", [])))
    manifest = {rel(path) for path in manifest_raw}

    if len(nodes) < 500:
        errors.append(f"graph too small: nodes={len(nodes)} < 500")
    if len(links) < 600:
        errors.append(f"graph too sparse: links={len(links)} < 600")
    seen_links: set[str] = set()
    duplicate_links = 0
    for link in links:
        key = json.dumps(link, sort_keys=True, separators=(",", ":"))
        if key in seen_links:
            duplicate_links += 1
        else:
            seen_links.add(key)
    if duplicate_links:
        errors.append(f"duplicate links present: {duplicate_links}")
    if len(manifest) < 100:
        errors.append(f"manifest too small: sources={len(manifest)} < 100")

    required_manifest = [
        "AGENTS.md",
        "CLAUDE.md",
        "Bizwholistic/astro.config.mjs",
        "Bizwholistic/src/layouts/Base.astro",
        "Bizwholistic/src/i18n/ui.ts",
        "Bizwholistic/src/data/intentPages.ts",
        "Bizwholistic/src/pages/en/index.astro",
        "Bizwholistic/src/pages/pl/index.astro",
        "Bizwholistic/public/llms.txt",
        "Bizwholistic/public/robots.txt",
        "Portfolio-main/index.html",
        "wiki/index.md",
        "wiki/operations/operations-graphify.md",
        ".claude/scripts/verify_wiki.sh",
    ]
    for item in required_manifest:
        if item not in manifest:
            errors.append(f"manifest missing expected source: {item}")

    prefix_minimums = {
        "Bizwholistic/src/": 40,
        "Bizwholistic/public/": 10,
        "Portfolio-main/": 4,
        "wiki/": 30,
        ".claude/": 7,
        "graphify-out/converted/": 1,
    }
    prefix_counts = {
        prefix: sum(1 for item in manifest if item.startswith(prefix))
        for prefix in prefix_minimums
    }
    for prefix, minimum in prefix_minimums.items():
        if prefix_counts[prefix] < minimum:
            errors.append(
                f"manifest undercovers {prefix}: {prefix_counts[prefix]} < {minimum}"
            )

    if not any(
        item.startswith("graphify-out/converted/") and "Website fees" in item
        for item in manifest
    ):
        errors.append("business offer conversion missing from graphify-out/converted/")

    ignored_prefixes = [
        "Graphify/",
        "node_modules/",
        "Bizwholistic/node_modules/",
        "Bizwholistic/dist/",
        "Bizwholistic/.astro/",
        "graphify-out/cache/",
    ]
    for prefix in ignored_prefixes:
        offenders = sorted(item for item in manifest if item.startswith(prefix))
        if offenders:
            errors.append(f"ignored prefix present in manifest: {prefix} ({len(offenders)})")

    ignore_text = (ROOT / ".graphifyignore").read_text(encoding="utf-8") if (ROOT / ".graphifyignore").exists() else ""
    for token in ["Graphify/", "node_modules/", "dist/", ".astro/", "graphify-out/cache/"]:
        if token not in ignore_text:
            errors.append(f".graphifyignore missing token: {token}")

    if TREE.exists() and TREE.stat().st_size < 1000:
        errors.append(f"GRAPH_TREE.html is unexpectedly small: {TREE.stat().st_size} bytes")
    if REPORT.exists() and REPORT.stat().st_size < 1000:
        errors.append(f"GRAPH_REPORT.md is unexpectedly small: {REPORT.stat().st_size} bytes")

    query = subprocess.run(
        [
            "graphify",
            "query",
            "Graphify workflow AGENTS CLAUDE Bizwholistic Portfolio wiki business offer",
            "--budget",
            "1200",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    if query.returncode != 0:
        errors.append(f"graphify query failed: {query.stdout.strip()}")
    elif "NODE" not in query.stdout or "EDGE" not in query.stdout:
        errors.append("graphify query returned no NODE/EDGE traversal evidence")

    print(f"graphify_nodes={len(nodes)}")
    print(f"graphify_links={len(links)}")
    print(f"graphify_duplicate_links={duplicate_links}")
    print(f"manifest_sources={len(manifest)}")
    for prefix in sorted(prefix_counts):
        print(f"manifest_{prefix}={prefix_counts[prefix]}")
    print(f"query_exit={query.returncode}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print("VERDICT: FAIL — graphify workspace integration is incomplete")
        return 1

    print("VERDICT: PASS — graphify workspace integration covers the intended workspace")
    return 0


if __name__ == "__main__":
    sys.exit(main())
