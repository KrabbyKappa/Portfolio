---
type: implementation
description: Implementation map for the static portfolio site
last_updated: 2026-05-20
tags: [implementation, portfolio, static-site]
primary_file: Portfolio-main/index.html
related_files:
  - Portfolio-main/styles.css
  - Portfolio-main/projects.html
  - Portfolio-main/articles.html
  - Portfolio-main/references.html
---

# Portfolio Static Site Implementation

← [[MOC/MOC-Implementation]]

The portfolio site is plain HTML and CSS. There is no package manager or build pipeline in `Portfolio-main/`; direct file inspection is the source of truth.

## Source Areas

| Area | Path |
|------|------|
| Home page | `Portfolio-main/index.html` |
| Project list | `Portfolio-main/projects.html` |
| Articles | `Portfolio-main/articles.html` |
| References | `Portfolio-main/references.html` |
| Styling | `Portfolio-main/styles.css` |

→ All implementation: [[MOC/MOC-Implementation]]
