#!/usr/bin/env python3
"""Verify visual-polish requirements for Luca's package demo rescue pass."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def css_block(css: str, selector: str) -> str:
    pattern = re.compile(re.escape(selector) + r"\s*\{(?P<body>.*?)\}", re.S)
    match = pattern.search(css)
    return match.group("body") if match else ""


def has_all(text: str, tokens: list[str]) -> bool:
    lower = text.lower()
    return all(token.lower() in lower for token in tokens)


def main() -> int:
    failures: list[str] = []

    target_css = [
        "basic/atlas-family-foundation/styles.css",
        "basic/clearpath-commute-analytics/styles.css",
        "basic/harbor-legal-translation/styles.css",
        "micro/city-lab-pop-up/styles.css",
        "micro/lumo-desk-lamp-teaser/styles.css",
        "micro/mila-yoga-testimonial/styles.css",
        "micro/northstar-notary-proof/styles.css",
        "micro/riverside-bike-rescue/styles.css",
    ]
    for rel in target_css:
        css = read(rel)
        if ":focus-visible" not in css:
            failures.append(f"{rel}: missing explicit focus-visible state")

    clear_html = read("basic/clearpath-commute-analytics/index.html")
    clear_css = read("basic/clearpath-commute-analytics/styles.css")
    if not has_all(clear_css, ["#4ee8ff", "--cyan", "--bg: #06111f", ".zone"]):
        failures.append("clearpath: missing dark cyan dashboard system tokens")
    if ".node.hot" not in clear_css and ".hub.hot" not in clear_css:
        failures.append("clearpath: missing dark cyan dashboard system tokens")
    if not has_all(clear_html, ["87%", "12m", "4", "zone", "Sample model"]):
        failures.append("clearpath: dashboard artifact still lacks compact model metrics/zones")

    atlas_html = read("basic/atlas-family-foundation/index.html")
    atlas_css = read("basic/atlas-family-foundation/styles.css")
    if "data-label=\"Recipient\"" not in atlas_html or "content: attr(data-label)" not in atlas_css:
        failures.append("atlas: mobile grant ledger labels missing")
    if "foundation-slip" not in atlas_html:
        failures.append("atlas: foundation summary slip missing")

    harbor_html = read("basic/harbor-legal-translation/index.html")
    harbor_css = read("basic/harbor-legal-translation/styles.css")
    if not has_all(harbor_html, ["dossier-shell", "legal-photo", "harbor-legal-handoff.jpg", "Certified translations for legal records"]):
        failures.append("harbor: title/picture hero composition missing")
    if "cert-panel" in harbor_html or "HLT-2026-04" in harbor_html:
        failures.append("harbor: old separate certificate panel returned to the hero")
    if not has_all(harbor_css, ["margin-top: clamp(24px", "grid-template-columns: minmax(0, .98fr) minmax(350px, 500px)", "border-left: 7px solid"]):
        failures.append("harbor: top-harmony dossier shell styling missing")
    if "--red: #8b2c2c" not in harbor_css and "--burgundy: #8b2c2c" not in harbor_css:
        failures.append("harbor: red accent is still too loud")

    city_css = read("micro/city-lab-pop-up/styles.css")
    city_h1 = css_block(city_css, "h1")
    if "line-height: 1.3" not in city_h1 or "text-transform: none" not in city_h1:
        failures.append("city-lab: hero headline readability patch missing")

    lumo_css = read("micro/lumo-desk-lamp-teaser/styles.css")
    lumo_html = read("micro/lumo-desk-lamp-teaser/index.html")
    if "polygon(28% 0, 72% 0" not in lumo_css and "polygon(30% 0, 70% 0" not in lumo_css:
        failures.append("lumo: glow cone was not widened")
    if "Request launch notes" not in lumo_html:
        failures.append("lumo: premium launch CTA missing")

    mila_html = read("micro/mila-yoga-testimonial/index.html")
    mila_css = read("micro/mila-yoga-testimonial/styles.css")
    if "student-note" not in mila_html or "figcaption" not in mila_html:
        failures.append("mila: testimonial cards are not grounded as notes")
    if ".student-note" not in mila_css:
        failures.append("mila: testimonial note styling missing")

    north_html = read("micro/northstar-notary-proof/index.html")
    north_css = read("micro/northstar-notary-proof/styles.css")
    if "notary public" not in north_html.lower():
        failures.append("northstar: official notary seal language missing")
    if "border: 7px double" in north_css or "rotate(-9deg)" in north_css or "rotate(10deg)" in north_css:
        failures.append("northstar: playful seal styling still present")

    riverside_css = read("micro/riverside-bike-rescue/styles.css")
    if "border: 18px solid" in riverside_css:
        failures.append("riverside: clunky decorative wheel still present")

    if failures:
        print(f"Checked polish targets: 8")
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"VERDICT: FAIL — {len(failures)} visual polish issue(s)")
        return 1

    print("Checked polish targets: 8")
    print("VERDICT: PASS — requested visual polish markers are present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
