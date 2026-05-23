#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WebsiteWikiSystemTest(unittest.TestCase):
    def test_core_wiki_files_exist(self) -> None:
        required = [
            "CLAUDE.md",
            "HERMES.md",
            "AGENTS.md",
            ".graphifyignore",
            "Graphify/README.md",
            "graphify-out/graph.json",
            "graphify-out/GRAPH_TREE.html",
            "wiki/index.md",
            "wiki/SCHEMA.md",
            "wiki/FRONTMATTER_STANDARD.md",
            "wiki/MOC/MOC-Projects.md",
            "wiki/MOC/MOC-Operations.md",
            "wiki/MOC/MOC-Implementation.md",
            "wiki/MOC/MOC-SEO.md",
            "wiki/MOC/MOC-Decisions.md",
            "wiki/MOC/MOC-KnowledgeGraph.md",
            "wiki/operations/operations-graphify.md",
            "wiki/_find_broken.py",
            "wiki/_audit.py",
            ".claude/scripts/verify_site_assets.sh",
            ".claude/scripts/refresh_graphify_workspace.sh",
            ".claude/scripts/verify_graphify_workspace.py",
            ".claude/scripts/verify_wiki.sh",
            ".claude/agents/wiki-scribe.md",
            ".claude/agents/wiki-truth-auditor.md",
            ".claude/agents/wiki-connectivity-curator.md",
            ".claude/rules/wiki-session-update.md",
        ]
        missing = [path for path in required if not (ROOT / path).exists()]
        self.assertEqual([], missing)

    def test_index_is_the_agent_routing_surface(self) -> None:
        text = (ROOT / "wiki/index.md").read_text()
        self.assertIn("Website Development Wiki", text)
        self.assertIn("READ THIS FIRST", text)
        self.assertIn("Start Here", text)
        self.assertIn("Agent Task Routing", text)
        self.assertIn("[[MOC/MOC-Projects]]", text)
        self.assertIn("[[operations/operations-hermes-website-development]]", text)
        self.assertIn("[[operations/operations-graphify]]", text)

    def test_project_instructions_point_agents_to_the_wiki_gate(self) -> None:
        text = (ROOT / "CLAUDE.md").read_text()
        self.assertIn("/Users/lucak/Website Development", text)
        self.assertIn("wiki/index.md", text)
        self.assertIn("bash .claude/scripts/verify_wiki.sh", text)
        self.assertIn("Bizwholistic", text)
        self.assertIn("Portfolio-main", text)
        self.assertIn("Graphify", text)

    def test_graphify_is_locally_available_and_routed(self) -> None:
        agents = (ROOT / "AGENTS.md").read_text()
        graphify_ignore = (ROOT / ".graphifyignore").read_text()
        runbook = (ROOT / "wiki/operations/operations-graphify.md").read_text()
        self.assertIn("graphify", agents)
        self.assertIn("Graphify/", graphify_ignore)
        self.assertIn("node_modules/", graphify_ignore)
        self.assertIn("dist/", graphify_ignore)
        self.assertIn("graphify query", runbook)
        graph = (ROOT / "graphify-out/graph.json").read_text()
        self.assertIn('"nodes"', graph)
        result = subprocess.run(
            ["graphify", "--help"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=10,
        )
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("Usage: graphify", result.stdout)

    def test_graph_json_is_valid_and_nonempty(self) -> None:
        data = json.loads((ROOT / "graphify-out/graph.json").read_text())
        self.assertIsInstance(data.get("nodes"), list)
        self.assertGreater(len(data["nodes"]), 0)

    def test_broken_link_checker_flags_missing_wikilink_with_spaces(self) -> None:
        checker = load_module(ROOT / "wiki/_find_broken.py", "website_find_broken")
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp)
            (wiki / "index.md").write_text(
                "---\ntype: index\ndescription: tmp\nlast_updated: 2026-05-20\ntags: [tmp]\n---\n\n[[Missing Page]]\n",
                encoding="utf-8",
            )
            self.assertEqual([("index.md", "Missing Page")], checker.find_broken(wiki))

    def test_audit_flags_missing_frontmatter_routes(self) -> None:
        audit = load_module(ROOT / "wiki/_audit.py", "website_audit")
        old_wiki = audit.WIKI
        old_issues = audit.issues
        try:
            with tempfile.TemporaryDirectory() as tmp:
                audit.WIKI = Path(tmp) / "wiki"
                audit.WIKI.mkdir()
                audit.issues = []
                (audit.WIKI / "index.md").write_text(
                    "---\ntype: index\ndescription: tmp\nlast_updated: 2026-05-20\ntags: [tmp]\n---\n\n# Tmp\n",
                    encoding="utf-8",
                )
                (audit.WIKI / "MOC.md").write_text(
                    "---\ntype: moc\ndescription: tmp\nlast_updated: 2026-05-20\ntags: [tmp]\nchildren:\n  - missing/page\n---\n\n# MOC\n",
                    encoding="utf-8",
                )
                audit.check_frontmatter_links(audit.all_pages())
                self.assertIn(
                    "[frontmatter-link] MOC.md: children references missing page: missing/page",
                    audit.issues,
                )
        finally:
            audit.WIKI = old_wiki
            audit.issues = old_issues

    def test_wiki_verifier_passes(self) -> None:
        result = subprocess.run(
            ["bash", ".claude/scripts/verify_wiki.sh"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=30,
        )
        self.assertEqual(0, result.returncode, result.stdout)
        self.assertIn("VERDICT: PASS", result.stdout)


if __name__ == "__main__":
    unittest.main()
