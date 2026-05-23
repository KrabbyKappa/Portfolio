#!/usr/bin/env python3
"""Broken wikilink checker for the Website Development wiki."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


WIKI = Path(__file__).resolve().parent
EXCLUDE_PARTS = {"_templates", "__pycache__", ".obsidian"}
FENCE_RE = re.compile(r"^\s*(```|~~~)")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def strip_code(content: str) -> str:
    out: list[str] = []
    in_fence = False
    for line in content.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence or line.startswith("    ") or line.startswith("\t"):
            out.append("")
            continue
        out.append(re.sub(r"`[^`\n]+`", "", line))
    return "\n".join(out)


def pages(wiki_root: Path) -> list[Path]:
    return [
        p for p in wiki_root.rglob("*.md")
        if not any(part in EXCLUDE_PARTS for part in p.relative_to(wiki_root).parts)
    ]


def build_resolver(wiki_root: Path, wiki_pages: list[Path]):
    stems: dict[str, list[Path]] = {}
    for page in wiki_pages:
        rel = page.relative_to(wiki_root)
        keys = {page.stem, str(rel.with_suffix("")), str(rel)}
        for key in keys:
            stems.setdefault(key, []).append(page)

    def resolves(source: Path, target: str) -> bool:
        target = target.split("#", 1)[0].strip().removesuffix(".md")
        if not target or target.startswith("#"):
            return True
        candidates = [
            wiki_root / f"{target}.md",
            wiki_root / target / "index.md",
            source.parent / f"{target}.md",
            source.parent / target / "index.md",
        ]
        return any(c.exists() for c in candidates) or bool(stems.get(target) or stems.get(target.split("/")[-1]))

    return resolves


def find_broken(wiki_root: Path) -> list[tuple[str, str]]:
    wiki_pages = pages(wiki_root)
    resolves = build_resolver(wiki_root, wiki_pages)
    broken: list[tuple[str, str]] = []
    for page in wiki_pages:
        text = strip_code(page.read_text(encoding="utf-8"))
        for link in WIKILINK_RE.findall(text):
            link = link.strip().replace("\\", "")
            if not resolves(page, link):
                broken.append((str(page.relative_to(wiki_root)), link))
    return broken


def main() -> int:
    json_mode = "--json" in sys.argv
    broken = find_broken(WIKI)
    if json_mode:
        print(json.dumps({"broken": broken}, indent=2))
    else:
        print(f"Total broken links: {len(broken)}")
        for source, link in broken:
            print(f"  {source}: [[{link}]]")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
