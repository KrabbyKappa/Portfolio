#!/usr/bin/env python3
"""Verify generated Website Development package demo pages.

Scope: static HTML/CSS examples in package-demo-pages/.
The script intentionally avoids network access and reports a single final PASS/FAIL line.
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED_MICRO = {
    "riverside-bike-rescue",
    "northstar-notary-proof",
    "mila-yoga-testimonial",
    "lumo-desk-lamp-teaser",
    "city-lab-pop-up",
}
EXPECTED_BASIC = {
    "harbor-legal-translation",
    "verde-lunch-club",
    "mosaic-content-studio",
    "clearpath-commute-analytics",
    "atlas-family-foundation",
}
DIRECT_SCHEMES = ("mailto:", "tel:", "https://wa.me/", "#")
FORBIDDEN_HTML = ("<form", "<script", "gtag(", "googletagmanager", "dataLayer", "analytics.js", "plausible.io", "umami")

class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.tags: list[str] = []
        self.h1_count = 0
        self.title_text = ""
        self.in_title = False
        self.meta_names: set[str] = set()
        self.hrefs: list[str] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k.lower(): (v or "") for k, v in attrs}
        self.tags.append(tag.lower())
        if tag.lower() == "h1":
            self.h1_count += 1
        if tag.lower() == "title":
            self.in_title = True
        if tag.lower() == "meta":
            name = attrs_dict.get("name", "").lower()
            prop = attrs_dict.get("property", "").lower()
            if name:
                self.meta_names.add(name)
            if prop:
                self.meta_names.add(prop)
        if tag.lower() == "a":
            self.hrefs.append(attrs_dict.get("href", ""))
        if attrs_dict.get("id"):
            self.ids.add(attrs_dict["id"])

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_text += data.strip()


def check_page(path: Path, tier: str, issues: list[str]) -> None:
    html = path.read_text(encoding="utf-8")
    lower = html.lower()
    parser = PageParser()
    parser.feed(html)

    rel = path.relative_to(ROOT)
    required_tags = {"header", "main", "section", "footer", "nav"}
    missing_tags = required_tags - set(parser.tags)
    if missing_tags:
        issues.append(f"{rel}: missing semantic tags {sorted(missing_tags)}")
    if parser.h1_count != 1:
        issues.append(f"{rel}: expected exactly 1 h1, found {parser.h1_count}")
    if not parser.title_text:
        issues.append(f"{rel}: missing title text")
    for meta in ("viewport", "description"):
        if meta not in parser.meta_names:
            issues.append(f"{rel}: missing meta {meta}")
    for token in FORBIDDEN_HTML:
        if token in lower:
            issues.append(f"{rel}: forbidden token present: {token}")
    if "fictional demo" not in lower:
        issues.append(f"{rel}: missing fictional-demo disclosure")
    if "no form" not in lower and tier == "micro":
        issues.append(f"{rel}: micro page missing explicit no-form guardrail")
    if tier == "basic" and "add-ons" not in lower:
        issues.append(f"{rel}: basic page missing add-on/scope language")
    bad_hrefs = []
    for href in parser.hrefs:
        if href.startswith("#") and href[1:] and href[1:] not in parser.ids and href != "#top":
            bad_hrefs.append(href)
        if href and not href.startswith(DIRECT_SCHEMES):
            bad_hrefs.append(href)
    if bad_hrefs:
        issues.append(f"{rel}: unexpected hrefs {bad_hrefs}")

    css_path = path.with_name("styles.css")
    css = css_path.read_text(encoding="utf-8") if css_path.exists() else ""
    if not css_path.exists():
        issues.append(f"{rel}: missing styles.css")
    if "@media (max-width" not in css:
        issues.append(f"{rel}: CSS missing responsive media query")
    if "prefers-reduced-motion" not in css:
        issues.append(f"{rel}: CSS missing reduced-motion guard")
    if "box-sizing: border-box" not in css:
        issues.append(f"{rel}: CSS missing border-box reset")
    if "100vw" in css:
        issues.append(f"{rel}: CSS uses 100vw, horizontal-scroll risk")
    if css.count("{") != css.count("}"):
        issues.append(f"{rel}: CSS brace count mismatch")

    for required in ("robots.txt", "favicon.svg"):
        if not path.with_name(required).exists():
            issues.append(f"{rel}: missing {required}")
    if tier == "micro" and path.with_name("llms.txt").exists():
        issues.append(f"{rel}: micro page should not include llms.txt")
    if tier == "basic" and not path.with_name("llms.txt").exists():
        issues.append(f"{rel}: basic page missing llms.txt")


def main() -> int:
    issues: list[str] = []
    if not (ROOT / "index.html").exists():
        issues.append("root index.html missing")
    if not (ROOT / "README.md").exists():
        issues.append("README.md missing")

    micro_dirs = {p.name for p in (ROOT / "micro").glob("*") if p.is_dir()} if (ROOT / "micro").exists() else set()
    basic_dirs = {p.name for p in (ROOT / "basic").glob("*") if p.is_dir()} if (ROOT / "basic").exists() else set()
    if micro_dirs != EXPECTED_MICRO:
        issues.append(f"micro directory mismatch: expected {sorted(EXPECTED_MICRO)}, found {sorted(micro_dirs)}")
    if basic_dirs != EXPECTED_BASIC:
        issues.append(f"basic directory mismatch: expected {sorted(EXPECTED_BASIC)}, found {sorted(basic_dirs)}")

    for slug in sorted(EXPECTED_MICRO):
        page = ROOT / "micro" / slug / "index.html"
        if not page.exists():
            issues.append(f"missing micro page {page.relative_to(ROOT)}")
        else:
            check_page(page, "micro", issues)
    for slug in sorted(EXPECTED_BASIC):
        page = ROOT / "basic" / slug / "index.html"
        if not page.exists():
            issues.append(f"missing basic page {page.relative_to(ROOT)}")
        else:
            check_page(page, "basic", issues)

    total_pages = len(list((ROOT / "micro").glob("*/index.html"))) + len(list((ROOT / "basic").glob("*/index.html")))
    print(f"Checked demo pages: {total_pages} (micro={len(micro_dirs)}, basic={len(basic_dirs)})")
    print(f"Checked root: {ROOT}")
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        print(f"VERDICT: FAIL — {len(issues)} issue(s)")
        return 1
    print("VERDICT: PASS — package demo pages are structurally scoped and static-safe")
    return 0

if __name__ == "__main__":
    sys.exit(main())
