#!/usr/bin/env python3
"""RED/GREEN verifier for package demo visual uniqueness.

This verifier encodes Luca's 2026-05-20 correction: Riverside can stay,
but the other four Micro pages and all five Basic pages must stop being
copies of one shared layout. Each target page must carry a unique design
signature, unique body archetype, and signature CSS modules that are not
shared with the other pages.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent

TARGETS = {
    "micro/northstar-notary-proof": {
        "signature": "notary-ledger-grid",
        "archetype": "micro-notary-ledger",
        "tokens": ["ledger-hero", "seal-stack", "clause-list"],
    },
    "micro/mila-yoga-testimonial": {
        "signature": "wellness-breath-orbit",
        "archetype": "micro-wellness-orbit",
        "tokens": ["breath-ring", "testimonial-ribbon", "ritual-cards"],
    },
    "micro/lumo-desk-lamp-teaser": {
        "signature": "product-night-stage",
        "archetype": "micro-product-stage",
        "tokens": ["lamp-stage", "beam-field", "spec-rail"],
    },
    "micro/city-lab-pop-up": {
        "signature": "event-poster-system",
        "archetype": "micro-event-poster",
        "tokens": ["poster-grid", "ticket-stub", "schedule-marquee"],
    },
    "basic/harbor-legal-translation": {
        "signature": "translation-dossier-editorial",
        "archetype": "basic-dossier-editorial",
        "tokens": ["dossier-shell", "language-matrix", "cert-panel"],
    },
    "basic/verde-lunch-club": {
        "signature": "food-menu-market",
        "archetype": "basic-market-menu",
        "tokens": ["menu-board", "ingredient-tape", "hours-card"],
    },
    "basic/mosaic-content-studio": {
        "signature": "creative-sticker-chaos",
        "archetype": "basic-sticker-studio",
        "tokens": ["sticker-cloud", "case-strip", "metric-bubbles"],
    },
    "basic/clearpath-commute-analytics": {
        "signature": "saas-dashboard-blueprint",
        "archetype": "basic-dashboard-blueprint",
        "tokens": ["dashboard-mock", "metric-grid", "workflow-rail"],
    },
    "basic/atlas-family-foundation": {
        "signature": "foundation-impact-brochure",
        "archetype": "basic-impact-brochure",
        "tokens": ["pillar-map", "grant-ledger", "transparency-band"],
    },
}

FORBIDDEN = ("<form", "<script", "googletagmanager", "gtag(", "plausible.io", "dataLayer")


def token_set(text: str) -> set[str]:
    return {t.lower() for t in re.findall(r"[a-zA-Z][a-zA-Z0-9_-]{2,}", text)}


def main() -> int:
    failures: list[str] = []
    seen_signatures: set[str] = set()
    seen_archetypes: set[str] = set()
    css_sets: dict[str, set[str]] = {}

    for rel, spec in TARGETS.items():
        page = ROOT / rel / "index.html"
        css = ROOT / rel / "styles.css"
        if not page.exists():
            failures.append(f"{rel}: missing index.html")
            continue
        if not css.exists():
            failures.append(f"{rel}: missing styles.css")
            continue
        html = page.read_text(encoding="utf-8")
        styles = css.read_text(encoding="utf-8")
        lower = (html + "\n" + styles).lower()

        if any(x.lower() in lower for x in FORBIDDEN):
            failures.append(f"{rel}: contains forbidden backend/tracking/form token")
        if html.lower().count("<h1") != 1:
            failures.append(f"{rel}: expected exactly one h1")
        if len(re.findall(r"<section\b", html, re.I)) < 6:
            failures.append(f"{rel}: expected at least six sections")
        if spec["signature"] in seen_signatures:
            failures.append(f"{rel}: duplicate signature {spec['signature']}")
        seen_signatures.add(spec["signature"])
        if spec["archetype"] in seen_archetypes:
            failures.append(f"{rel}: duplicate archetype {spec['archetype']}")
        seen_archetypes.add(spec["archetype"])

        sig_attr = f'data-design-signature="{spec["signature"]}"'
        arch_attr = f'data-design-archetype="{spec["archetype"]}"'
        if sig_attr not in html:
            failures.append(f"{rel}: missing {sig_attr}")
        if arch_attr not in html:
            failures.append(f"{rel}: missing {arch_attr}")
        if f"UNIQUE_STYLE: {spec['signature']}" not in styles:
            failures.append(f"{rel}: missing CSS UNIQUE_STYLE marker")
        for token in spec["tokens"]:
            if token not in lower:
                failures.append(f"{rel}: missing unique module token {token}")
        css_sets[rel] = token_set(styles)

    rels = list(css_sets)
    for i, a in enumerate(rels):
        for b in rels[i + 1:]:
            inter = css_sets[a] & css_sets[b]
            union = css_sets[a] | css_sets[b]
            score = len(inter) / max(1, len(union))
            if score > 0.56:
                failures.append(f"{a} vs {b}: CSS token similarity too high ({score:.2f})")

    if failures:
        print(f"Checked uniqueness targets: {len(TARGETS)}")
        for failure in failures[:80]:
            print(f"FAIL: {failure}")
        if len(failures) > 80:
            print(f"FAIL: ... {len(failures) - 80} additional failures omitted")
        print("VERDICT: FAIL — target demo pages are not uniquely redesigned")
        return 1

    print(f"Checked uniqueness targets: {len(TARGETS)}")
    print("VERDICT: PASS — all target demo pages have unique design signatures, archetypes, and CSS modules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
