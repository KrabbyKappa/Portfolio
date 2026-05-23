#!/usr/bin/env python3
"""Verify OpenAI Codex PDF ingestion assets and wiki wiring."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
PDF = WIKI / "assets/reference/openai-how-openai-uses-codex.pdf"
TEXT = WIKI / "assets/reference/openai-how-openai-uses-codex.txt"
META = WIKI / "assets/reference/openai-how-openai-uses-codex-meta.json"
PAGE = WIKI / "reference/openai-how-openai-uses-codex.md"
MOC_REFERENCE = WIKI / "MOC/MOC-Reference.md"
MOC_OPERATIONS = WIKI / "MOC/MOC-Operations.md"
LOG = WIKI / "log.md"
WORK_RECORD = WIKI / "logs/work-record-2026-05-21-openai-codex-pdf-ingestion.md"
SOURCE_URL = "https://cdn.openai.com/pdf/6a2631dc-783e-479b-b1a4-af0cfbd38630/how-openai-uses-codex.pdf"
EXPECTED_SHA256 = "95b5272e2635211bd621ee605a7f6846d030f6d5cab791206c9ba73b86b7da62"
EXPECTED_BYTES = 8040907
EXPECTED_PAGES = 13

REQUIRED_TEXT_SNIPPETS = [
    "How OpenAI uses Codex",
    "Code understanding",
    "Refactoring and migrations",
    "Performance optimization",
    "Improving test coverage",
    "Increasing development velocity",
    "Staying in flow",
    "Exploration and ideation",
    "Start with Ask Mode",
    "Use AGENTS.md",
]

REQUIRED_PAGE_SNIPPETS = [
    SOURCE_URL,
    "Local extraction",
    "Reported Use Cases",
    "Best Practices to Port Into This Workspace",
    "Guardrails",
    "[[MOC/MOC-Reference]]",
    "[[MOC/MOC-Operations]]",
]

issues: list[str] = []

for path in [PDF, TEXT, META, PAGE, MOC_REFERENCE, MOC_OPERATIONS, LOG, WORK_RECORD]:
    if not path.exists():
        issues.append(f"missing file: {path.relative_to(ROOT)}")

if PDF.exists():
    data = PDF.read_bytes()
    if len(data) != EXPECTED_BYTES:
        issues.append(f"pdf bytes mismatch: {len(data)} != {EXPECTED_BYTES}")
    sha = hashlib.sha256(data).hexdigest()
    if sha != EXPECTED_SHA256:
        issues.append(f"pdf sha256 mismatch: {sha} != {EXPECTED_SHA256}")

if META.exists():
    meta = json.loads(META.read_text(encoding="utf-8"))
    if meta.get("source_url") != SOURCE_URL:
        issues.append("meta source_url mismatch")
    if meta.get("bytes") != EXPECTED_BYTES:
        issues.append(f"meta bytes mismatch: {meta.get('bytes')} != {EXPECTED_BYTES}")
    if meta.get("sha256") != EXPECTED_SHA256:
        issues.append("meta sha256 mismatch")
    if meta.get("pages") != EXPECTED_PAGES:
        issues.append(f"meta page mismatch: {meta.get('pages')} != {EXPECTED_PAGES}")
    if meta.get("text_chars", 0) < 10000:
        issues.append(f"extracted text too short: {meta.get('text_chars')}")

if TEXT.exists():
    text = TEXT.read_text(encoding="utf-8")
    for snippet in REQUIRED_TEXT_SNIPPETS:
        if snippet not in text:
            issues.append(f"text missing snippet: {snippet}")

if PAGE.exists():
    page = PAGE.read_text(encoding="utf-8")
    for snippet in REQUIRED_PAGE_SNIPPETS:
        if snippet not in page:
            issues.append(f"page missing snippet: {snippet}")

for path, needle in [
    (MOC_REFERENCE, "[[reference/openai-how-openai-uses-codex]]"),
    (MOC_OPERATIONS, "[[logs/work-record-2026-05-21-openai-codex-pdf-ingestion]]"),
    (LOG, "[[reference/openai-how-openai-uses-codex]]"),
    (WORK_RECORD, "[[reference/openai-how-openai-uses-codex]]"),
]:
    if path.exists() and needle not in path.read_text(encoding="utf-8"):
        issues.append(f"{path.relative_to(ROOT)} missing {needle}")

if issues:
    print("VERDICT: FAIL -- OpenAI Codex PDF ingestion is incomplete")
    for issue in issues:
        print(f"- {issue}")
    sys.exit(1)

print("VERDICT: PASS -- OpenAI Codex PDF ingestion is complete")
print(f"pdf_bytes={EXPECTED_BYTES}")
print(f"pdf_pages={EXPECTED_PAGES}")
print(f"sha256={EXPECTED_SHA256}")
