---
type: index
description: Main entry point for the Website Development business wiki; read this first every session
last_updated: 2026-05-21
tags: [index, home, entry-point, website-development]
---

# Website Development Wiki

> READ THIS FIRST every session. This index routes agents to the right page in one hop and keeps website work grounded in measured files, not chat memory.

> WORK-START DOCUMENTATION RULE: after reading this index and before implementation, create or update the relevant wiki work record. The work record must state the outcome, current evidence, intended verifier, and handoff path. See [[operations/operations-agent-work-start-documentation]].

> HERMES RULE: this workspace is `/Users/lucak/Website Development`. Hermes should run with that path as `terminal.cwd` and with a writable mount for this folder. See [[operations/operations-hermes-website-development]].

## Start Here

| What you need | Go to |
|---------------|-------|
| Start any non-trivial agent work | [[operations/operations-agent-work-start-documentation]] |
| Confirm Hermes can work here | [[operations/operations-hermes-website-development]] |
| Use or refresh the knowledge graph | [[operations/operations-graphify]] |
| Understand projects in this workspace | [[MOC/MOC-Projects]] |
| Work on Bizwholistic | [[projects/bizwholistic]] |
| Work on Luca portfolio | [[projects/portfolio-main]] |
| Check SEO and AI-search assets | [[MOC/MOC-SEO]] |
| Run local wiki and site checks | [[operations/operations-site-verification]] |
| Understand implementation paths | [[MOC/MOC-Implementation]] |
| Review business offer material | [[MOC/MOC-Business]] |
| Understand why this wiki exists | [[decisions/dec-001-wiki-methodology-for-website-development]] |

## Agent Task Routing

| Your task | Start here | Then check |
|-----------|------------|------------|
| Add or edit a site page | [[MOC/MOC-Projects]] | [[MOC/MOC-Implementation]] |
| Audit SEO, crawlability, or AI-search readiness | [[seo/seo-bizwholistic-crawlability]] | [[operations/operations-site-verification]] |
| Change Bizwholistic Astro code | [[implementation/impl-bizwholistic-astro]] | [[projects/bizwholistic]] |
| Change portfolio static files | [[implementation/impl-portfolio-static-site]] | [[projects/portfolio-main]] |
| Create a decision record | [[MOC/MOC-Decisions]] | [[_templates/tpl-decision]] |
| Fix broken wiki links or orphans | [[MOC/MOC-Graph]] | [[operations/operations-site-verification]] |
| Ask a codebase-wide question | [[operations/operations-graphify]] | `graphify query "<question>"` |
| Verify the wiki system | [[operations/operations-site-verification]] | `bash .claude/scripts/verify_wiki.sh` |
| Use ingested Astro docs | [[reference/astro-docs-index]] | [[implementation/impl-bizwholistic-astro]] |
| Use design/reference research | [[MOC/MOC-Reference]] | [[MOC/MOC-Business]] |

## Maps of Content

| MOC | Contents |
|-----|----------|
| [[MOC/MOC-Projects]] | Website projects and their source paths |
| [[MOC/MOC-Implementation]] | Code architecture and file ownership |
| [[MOC/MOC-Operations]] | Work-start protocol, Hermes setup, verification |
| [[MOC/MOC-SEO]] | Crawlability, machine-readable assets, search visibility |
| [[MOC/MOC-Decisions]] | Decisions and methodology records |
| [[MOC/MOC-Graph]] | Wiki graph rules and structural health |
| [[MOC/MOC-KnowledgeGraph]] | Graphify setup and graph-query workflow |
| [[MOC/MOC-Business]] | Offer, pricing, package specs, and package demo docs |
| [[MOC/MOC-Reference]] | Astro docs, design papers, template research, and external references |

## Current Workspace Snapshot

| Area | Current source of truth |
|------|-------------------------|
| Bizwholistic site | `Bizwholistic/src/`, `Bizwholistic/public/`, `Bizwholistic/astro.config.mjs` |
| Bizwholistic build output | `Bizwholistic/dist/` after `npm run build` |
| Portfolio site | `Portfolio-main/*.html`, `Portfolio-main/styles.css`, `Portfolio-main/profile.jpg` |
| Business offer | `Luca Kosowski Website fees.docx` |
| Knowledge graph tool | `Graphify/`, `AGENTS.md`, `.graphifyignore` |
| Wiki health | `.claude/scripts/verify_wiki.sh` |
| Agent instructions | `CLAUDE.md`, `HERMES.md`, `.claude/agents/` |
| Astro docs reference | `wiki/assets/astro-docs/manifest.json`, [[reference/astro-docs-index]] |

## Governance

- [[SCHEMA]] defines page types, frontmatter, and required evidence fields.
- [[FRONTMATTER_STANDARD]] gives copy-ready frontmatter patterns.
- [[MOC/MOC-Graph]] defines graph topology and orphan rules.
- [[missing-pages]] tracks known gaps instead of hiding them.
- [[log]] records notable wiki changes.

## Session Records

- [[logs/work-record-2026-05-21-astro-docs-design-papers]] records the Astro docs ingestion and Bizwholistic design-paper import.
- [[logs/session-handoff-2026-05-20-wiki-bootstrap]] records the initial local wiki bootstrap for this workspace.
- [[logs/session-handoff-2026-05-20-package-demo-polish]] records the package demo page visual polish/rebuild pass.
- [[logs/session-handoff-2026-05-20-basic-photo-rebuild]] records the photo-led Basic package correction pass.
