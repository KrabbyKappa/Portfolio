#!/usr/bin/env python3
"""Verify the local Astro-docs and Bizwholistic design-paper wiki ingestion.

This verifier is intentionally offline: it checks the already-copied official-doc
manifest, the distilled wiki pages, and the local design-paper bundle. It does not
fetch the upstream Astro docs.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"

ASTRO_PAGES = [
    "reference/astro-docs-index.md",
    "reference/astro-docs-project-structure-routing.md",
    "reference/astro-docs-components-assets-interactivity.md",
    "reference/astro-docs-config-data-build-deploy.md",
    "reference/astro-version-watch.md",
]

DESIGN_FILES = [
    "BizWholistic_HK_10_Options_Preview.pdf",
    "BizWholistic_HK_Design_Diagnosis_and_Options_Report.pdf",
    "DOCX_options/BizWholistic_HK_01_approved_rhythm.docx",
    "DOCX_options/BizWholistic_HK_02_navy_sidebar_report.docx",
    "DOCX_options/BizWholistic_HK_03_minimal_memo.docx",
    "DOCX_options/BizWholistic_HK_04_balanced_card_grid.docx",
    "DOCX_options/BizWholistic_HK_05_thin_timeline.docx",
    "DOCX_options/BizWholistic_HK_06_compliance_matrix.docx",
    "DOCX_options/BizWholistic_HK_07_index_detail.docx",
    "DOCX_options/BizWholistic_HK_08_premium_purple_rail.docx",
    "DOCX_options/BizWholistic_HK_09_compact_bands.docx",
    "DOCX_options/BizWholistic_HK_10_board_brief.docx",
    "PDF_previews/BizWholistic_HK_01_approved_rhythm.pdf",
    "PDF_previews/BizWholistic_HK_02_navy_sidebar_report.pdf",
    "PDF_previews/BizWholistic_HK_03_minimal_memo.pdf",
    "PDF_previews/BizWholistic_HK_04_balanced_card_grid.pdf",
    "PDF_previews/BizWholistic_HK_05_thin_timeline.pdf",
    "PDF_previews/BizWholistic_HK_06_compliance_matrix.pdf",
    "PDF_previews/BizWholistic_HK_07_index_detail.pdf",
    "PDF_previews/BizWholistic_HK_08_premium_purple_rail.pdf",
    "PDF_previews/BizWholistic_HK_09_compact_bands.pdf",
    "PDF_previews/BizWholistic_HK_10_board_brief.pdf",
    "contact_sheet_all_options.png",
]


def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)
    print(f"FAIL: {msg}")


def main() -> int:
    failures: list[str] = []

    manifest_path = WIKI / "assets/astro-docs/manifest.json"
    if not manifest_path.exists():
        fail(f"missing Astro manifest: {manifest_path.relative_to(ROOT)}", failures)
        manifest = {}
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        docs = manifest.get("docs", [])
        if manifest.get("selected_count") != 19:
            fail(f"selected_count={manifest.get('selected_count')} expected 19", failures)
        if manifest.get("raw_mdx_ok") != 19:
            fail(f"raw_mdx_ok={manifest.get('raw_mdx_ok')} expected 19", failures)
        if len(docs) != 19:
            fail(f"manifest docs length={len(docs)} expected 19", failures)
        for i, doc in enumerate(docs, 1):
            for key in ("url", "raw_url", "title", "bytes"):
                if key not in doc:
                    fail(f"manifest doc {i} missing {key}", failures)

    for rel in ASTRO_PAGES:
        path = WIKI / rel
        if not path.exists():
            fail(f"missing Astro wiki page: wiki/{rel}", failures)
        elif "wiki/assets/astro-docs/manifest.json" not in path.read_text(encoding="utf-8"):
            fail(f"Astro page lacks manifest provenance: wiki/{rel}", failures)

    index = (WIKI / "reference/astro-docs-index.md").read_text(encoding="utf-8") if (WIKI / "reference/astro-docs-index.md").exists() else ""
    if "Selected docs | 19" not in index:
        fail("Astro index does not record Selected docs | 19", failures)
    if "Raw MDX fetches OK | 19" not in index:
        fail("Astro index does not record Raw MDX fetches OK | 19", failures)
    if "astro v5.18.1" not in index:
        fail("Astro index does not record verified installed version astro v5.18.1", failures)

    package_json = json.loads((ROOT / "Bizwholistic/package.json").read_text(encoding="utf-8"))
    astro_range = package_json.get("dependencies", {}).get("astro")
    if astro_range != "^5.0.0":
        fail(f"Bizwholistic astro package range={astro_range!r} expected '^5.0.0'", failures)

    design_dir = WIKI / "assets/design-papers/bizwholistic-hk"
    if not design_dir.exists():
        fail("missing Bizwholistic design-paper asset directory", failures)
    else:
        found = [p for p in design_dir.rglob("*") if p.is_file()]
        if len(found) != 23:
            fail(f"design-paper file count={len(found)} expected 23", failures)
        total_bytes = sum(p.stat().st_size for p in found)
        if total_bytes != 4_712_609:
            fail(f"design-paper total bytes={total_bytes} expected 4712609", failures)
        for rel in DESIGN_FILES:
            p = design_dir / rel
            if not p.exists() or p.stat().st_size <= 0:
                fail(f"missing/empty design-paper asset: {p.relative_to(ROOT)}", failures)

    design_index = WIKI / "reference/bizwholistic-design-papers-index.md"
    if not design_index.exists():
        fail("missing design-paper index page", failures)
    else:
        text = design_index.read_text(encoding="utf-8")
        for rel in DESIGN_FILES:
            if rel not in text:
                fail(f"design-paper index missing listed asset: {rel}", failures)

    bad_link_pattern = re.compile(r"\[\[project/astro-docs-index\]\]")
    for path in WIKI.rglob("*.md"):
        if bad_link_pattern.search(path.read_text(encoding="utf-8")):
            fail(f"bad singular project Astro link remains: {path.relative_to(ROOT)}", failures)

    # The wiki verifier must pass after these ingestion pages are present.
    verifier = subprocess.run(
        ["bash", ".claude/scripts/verify_wiki.sh"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if verifier.returncode != 0:
        print(verifier.stdout)
        fail("verify_wiki.sh failed", failures)

    if failures:
        print(f"VERDICT: FAIL -- {len(failures)} Astro/design ingestion issue(s)")
        return 1
    print("VERDICT: PASS -- Astro docs and Bizwholistic design-paper ingestion are internally consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
