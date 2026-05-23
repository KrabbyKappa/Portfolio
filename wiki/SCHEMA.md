---
type: reference
description: Schema and ontology for the Website Development wiki
last_updated: 2026-05-20
tags: [schema, governance, wiki]
source: wiki
---

# Website Development Wiki Schema

← [[index]]

## Page Types

| type | Purpose | Required fields |
|------|---------|-----------------|
| `index` | Main entry point or high-level hub | `type`, `description`, `last_updated`, `tags` |
| `moc` | Map of Content for a domain | `type`, `description`, `last_updated`, `tags`, `children` |
| `project` | Website or client project | `type`, `description`, `last_updated`, `tags`, `project_path`, `status` |
| `implementation` | Code architecture or module notes | `type`, `description`, `last_updated`, `tags`, `primary_file` |
| `operation` | Runbook or workflow | `type`, `description`, `last_updated`, `tags` |
| `seo` | Crawlability, search, schema, or AI-search analysis | `type`, `description`, `last_updated`, `tags`, `project` |
| `business` | Business offer, pricing, positioning, or client material | `type`, `description`, `last_updated`, `tags`, `source_file` |
| `decision` | Architecture or operating decision | `type`, `description`, `last_updated`, `tags`, `id`, `status` |
| `log` | Chronological changelog or session handoff | `type`, `description`, `last_updated`, `tags`, `date` |
| `reference` | Schema, standard, or source note | `type`, `description`, `last_updated`, `tags`, `source` |
| `template` | Copy stub excluded from normal graph checks | `type`, `description`, `last_updated`, `tags` |

## Universal Rules

- Every page starts with YAML frontmatter.
- Every page has `type`, `description`, `last_updated`, and `tags`.
- Use full-path wikilinks from the `wiki/` root, for example `[[projects/bizwholistic]]`.
- Every non-hub content page links back to a relevant MOC.
- Every content claim that names a file path should use a real path in this workspace.

## Evidence Fields

| Field | Meaning |
|-------|---------|
| `project_path` | Root folder for a project, relative to `/Users/lucak/Website Development` |
| `primary_file` | Main implementation file or config path |
| `related_files` | Supporting source files |
| `source_file` | Business, reference, or external-source artifact |
| `verifier` | Command that proves the page's operational claim |
| `project` | Wikilink to the project page a record belongs to |

## Website Truth Hierarchy

1. Source files in `Bizwholistic/src/`, `Bizwholistic/public/`, and `Portfolio-main/`.
2. Configuration files such as `Bizwholistic/astro.config.mjs` and `Bizwholistic/package.json`.
3. Fresh build output in `Bizwholistic/dist/`.
4. Deployed live site, when a task explicitly asks for live-state verification.
5. Wiki text.

If the wiki disagrees with a higher-authority source, the wiki is wrong.

## Related Standards

- [[FRONTMATTER_STANDARD]]
- [[MOC/MOC-Graph]]

→ All governance: [[MOC/MOC-Graph]]
