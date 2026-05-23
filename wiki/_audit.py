#!/usr/bin/env python3
"""Structural audit for the Website Development wiki."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
FENCE_RE = re.compile(r"^\s*(```|~~~)")
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")
FM_BOUNDARY_RE = re.compile(r"^---\s*$", re.M)

UNIVERSAL = {"type", "description", "last_updated", "tags"}
REQUIRED_BY_TYPE = {
    "index": set(),
    "moc": {"children"},
    "project": {"project_path", "status"},
    "implementation": {"primary_file"},
    "operation": set(),
    "seo": {"project"},
    "business": {"source_file"},
    "decision": {"id", "status"},
    "log": {"date"},
    "reference": {"source"},
    "template": set(),
}
PATH_KEYS = {"project_path", "primary_file", "related_files", "source_file"}
LINK_KEYS = {"children", "related", "project"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

issues: list[str] = []


def add(section: str, msg: str) -> None:
    issues.append(f"[{section}] {msg}")


def strip_code(content: str) -> str:
    out: list[str] = []
    in_fence = False
    for line in content.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence:
            out.append("")
            continue
        out.append(re.sub(r"`[^`\n]+`", "", line))
    return "\n".join(out)


def parse_frontmatter(content: str) -> dict[str, object]:
    if not content.startswith("---"):
        return {}
    match = FM_BOUNDARY_RE.search(content, 3)
    if not match:
        return {}
    out: dict[str, object] = {}
    current_key: str | None = None
    for raw in content[3:match.start()].splitlines():
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", raw)
        if key_match:
            current_key = key_match.group(1)
            value = key_match.group(2).strip()
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1].strip()
                out[current_key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
            elif value:
                out[current_key] = value.strip("'\"")
            else:
                out[current_key] = []
            continue
        list_match = re.match(r"^\s*-\s*(.+?)\s*$", raw)
        if current_key and list_match:
            value = list_match.group(1).strip().strip("'\"")
            existing = out.setdefault(current_key, [])
            if isinstance(existing, list):
                existing.append(value)
    return out


def as_values(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(v).strip().strip("'\"") for v in value if str(v).strip()]
    if isinstance(value, str) and value:
        return [value.strip().strip("'\"")]
    return []


def all_pages() -> dict[Path, str]:
    return {p: p.read_text(encoding="utf-8") for p in WIKI.rglob("*.md")}


def check_schema(pages: dict[Path, str]) -> None:
    for page, text in pages.items():
        rel = page.relative_to(WIKI)
        if "_templates" in rel.parts:
            continue
        fm = parse_frontmatter(text)
        if not fm:
            add("schema", f"{rel}: missing frontmatter")
            continue
        missing = sorted(UNIVERSAL - set(fm))
        page_type = str(fm.get("type", ""))
        if page_type not in REQUIRED_BY_TYPE:
            add("schema", f"{rel}: unknown type={page_type!r}")
        else:
            missing.extend(sorted(REQUIRED_BY_TYPE[page_type] - set(fm)))
        if missing:
            add("schema", f"{rel}: missing fields {missing}")
        if "description" in fm and not str(fm["description"]).strip():
            add("schema", f"{rel}: empty description")
        if "last_updated" in fm and not DATE_RE.match(str(fm["last_updated"])):
            add("schema", f"{rel}: last_updated must be YYYY-MM-DD")
        if "tags" in fm and not as_values(fm["tags"]):
            add("schema", f"{rel}: tags must be a non-empty list")


def resolve_wiki_target(target: str, stems: dict[str, list[Path]]) -> list[Path]:
    target = target.split("#", 1)[0].strip().removesuffix(".md")
    if not target:
        return []
    direct = WIKI / f"{target}.md"
    index = WIKI / target / "index.md"
    found = []
    if direct.exists():
        found.append(direct)
    if index.exists():
        found.append(index)
    found.extend(stems.get(target, []))
    found.extend(stems.get(target.split("/")[-1], []))
    return list(dict.fromkeys(found))


def check_orphans(pages: dict[Path, str]) -> None:
    stems: dict[str, list[Path]] = defaultdict(list)
    for page in pages:
        rel = page.relative_to(WIKI)
        stems[page.stem].append(page)
        stems[str(rel.with_suffix(""))].append(page)

    inbound: Counter[Path] = Counter()
    for page, text in pages.items():
        cleaned = strip_code(text)
        for link in WIKILINK_RE.findall(cleaned):
            for target in resolve_wiki_target(link, stems):
                if target != page:
                    inbound[target] += 1
        fm = parse_frontmatter(text)
        for key in LINK_KEYS:
            for value in as_values(fm.get(key)):
                value = value.replace("[[", "").replace("]]", "")
                for target in resolve_wiki_target(value, stems):
                    if target != page:
                        inbound[target] += 1

    for page, text in pages.items():
        rel = page.relative_to(WIKI)
        if rel == Path("index.md") or "_templates" in rel.parts:
            continue
        fm = parse_frontmatter(text)
        if fm.get("type") == "template":
            continue
        if inbound[page] == 0:
            add("orphan", f"{rel}: no inbound links")


def check_file_refs(pages: dict[Path, str]) -> None:
    for page, text in pages.items():
        rel = page.relative_to(WIKI)
        if "_templates" in rel.parts:
            continue
        fm = parse_frontmatter(text)
        for key in PATH_KEYS:
            for value in as_values(fm.get(key)):
                value = value.strip()
                if not value or value.startswith("http"):
                    continue
                candidate = Path(value)
                if not candidate.is_absolute():
                    candidate = ROOT / candidate
                if not candidate.exists():
                    add("file-ref", f"{rel}: {key} references missing path: {value}")


def check_frontmatter_links(pages: dict[Path, str]) -> None:
    stems: dict[str, list[Path]] = defaultdict(list)
    for page in pages:
        rel = page.relative_to(WIKI)
        stems[page.stem].append(page)
        stems[str(rel.with_suffix(""))].append(page)

    for page, text in pages.items():
        rel = page.relative_to(WIKI)
        if "_templates" in rel.parts:
            continue
        fm = parse_frontmatter(text)
        for key in LINK_KEYS:
            for value in as_values(fm.get(key)):
                target = value.replace("[[", "").replace("]]", "")
                if not resolve_wiki_target(target, stems):
                    add("frontmatter-link", f"{rel}: {key} references missing page: {value}")


def check_duplicate_filenames(pages: dict[Path, str]) -> None:
    allowed = {"index.md", "README.md"}
    by_name: dict[str, list[str]] = defaultdict(list)
    for page in pages:
        rel = page.relative_to(WIKI)
        if "_templates" in rel.parts:
            continue
        by_name[page.name].append(str(rel))
    for name, files in by_name.items():
        if len(files) > 1 and name not in allowed:
            add("dup-filename", f"{name} appears in {len(files)} folders: {files}")


def main() -> int:
    pages = all_pages()
    check_schema(pages)
    check_duplicate_filenames(pages)
    check_file_refs(pages)
    check_frontmatter_links(pages)
    check_orphans(pages)

    by_section = Counter(issue.split("]")[0][1:] for issue in issues)
    print(f"Total issues: {len(issues)}")
    print("By section:")
    for section, count in by_section.most_common():
        print(f"  {section}: {count}")
    print()
    for issue in issues:
        print(issue)
    return len(issues)


if __name__ == "__main__":
    raise SystemExit(main())
