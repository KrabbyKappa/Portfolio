---
type: operation
description: Hermes setup for the Website Development workspace
last_updated: 2026-05-20
tags: [operation, hermes, agent]
verifier: bash .claude/scripts/verify_wiki.sh
---

# Hermes Website Development Setup

← [[MOC/MOC-Operations]]

Hermes should work from:

`/Users/lucak/Website Development`

## Required Config Facts

| Config item | Expected value |
|-------------|----------------|
| `terminal.cwd` | `/Users/lucak/Website Development` |
| `terminal.backend` | `local` |
| Writable workspace mount | Not required while `terminal.backend` is `local`; if switched to Docker, use `/Users/lucak/Website Development:/host/website-development:rw` |
| Other project workspace mounts | Not present in this Website Development profile |
| Local boot file | `CLAUDE.md` |
| Hermes note | `HERMES.md` |
| Wiki entry | `wiki/index.md` |

## Operating Rule

Hermes should read `CLAUDE.md` and then [[index]] before editing. For wiki changes, it must run `bash .claude/scripts/verify_wiki.sh`.

## 2026-05-20 Delegation Repair

| Field | Current record |
|-------|----------------|
| Outcome wanted | Hermes subagents in this workspace must route through the configured role table: GPT-5.5 xhigh for default/specialist GPT roles, and MiniMax M2.7 only for explicit MiniMax peer roles. |
| Current evidence | `terminal.cwd` is already `/Users/lucak/Website Development`, but native `delegate_task` only read top-level `delegation.model/provider/reasoning_effort`; it ignored `delegation.role_routes`, so children still launched as `MiniMax-M2.7` even when the prompt described a GPT-5.5 pass. |
| Intended verifier | `/Users/lucak/.hermes/hermes-agent/venv/bin/python -m pytest -o addopts='' -p no:cacheprovider tests/tools/test_delegate.py -q` from `/Users/lucak/.hermes/hermes-agent`, plus `bash .claude/scripts/verify_wiki.sh` here. |
| Handoff path | Runtime patch lives in `/Users/lucak/.hermes/hermes-agent/tools/delegate_tool.py` and `/Users/lucak/.hermes/hermes-agent/run_agent.py`; active config remains `/Users/lucak/.hermes/config.yaml`. |

Verified closeout: the delegate tool tests passed with `138 passed`, the workspace wiki verifier passed, and `bash .claude/scripts/refresh_graphify_workspace.sh` rebuilt `graphify-out/graph.json` with 2583 nodes and 2646 edges.

## 2026-05-20 Provider Timeout Repair

| Field | Current record |
|-------|----------------|
| Outcome wanted | GPT-5.5 and MiniMax delegation from this workspace should survive large website/wiki/design contexts without false 300-second stale-call failures, while preserving the configured GPT-5.5 default and explicit MiniMax peer routes. |
| Current evidence | `graphify query "Hermes GPT-5.5 MiniMax provider timeout folder config"` routes this issue to `CLAUDE.md` and the Hermes setup pages. Active config has `terminal.cwd: /Users/lucak/Website Development`, `display.streaming: true`, and `providers: {}`. Logs show `openai-codex/gpt-5.5` requests killed by `Non-streaming API call stale for 300s` at `~77,840` and `~141,990` tokens; some killed requests later completed, proving the 300-second stale detector was too aggressive. Logs also show MiniMax routed as `minimax/MiniMax-M2.7`, with intermittent empty/invalid content retries and one folder-specific unquoted-path failure on the space in `Website Development`. |
| Intended verifier | Check provider timeout resolution with `/Users/lucak/.hermes/hermes-agent/venv/bin/python`, run Hermes timeout/delegate tests from `/Users/lucak/.hermes/hermes-agent`, then run `bash .claude/scripts/verify_wiki.sh` and `bash .claude/scripts/refresh_graphify_workspace.sh` here. |
| Handoff path | Runtime config fix lives in `/Users/lucak/.hermes/config.yaml` and mirror `/Users/lucak/agent-maintenance/config.yaml`; workspace evidence lives in this page and `HERMES.md`. |

Verified closeout: timeout resolver reports `openai-codex` request/stale as `2400.0/1200.0` and `minimax` request/stale as `1800.0/900.0`; Hermes timeout/delegate tests passed with `150 passed`; live smoke calls returned `HERMES_GPT55_OK` and `HERMES_MINIMAX_OK`; `bash .claude/scripts/refresh_graphify_workspace.sh` passed with 2655 nodes and 2716 edges; `bash .claude/scripts/verify_wiki.sh` returned `VERDICT: PASS`.

## 2026-05-20 Path-Space and Fanout Repair

| Field | Current record |
|-------|----------------|
| Outcome wanted | The CLI agent must work reliably from `/Users/lucak/Website Development`, whose root path contains a space. |
| Current evidence | Direct reproduction showed unquoted `/Users/lucak/Website Development/HERMES.md` fails as `/Users/lucak/Website` + `Development/HERMES.md`, while the same unquoted pattern works under `/Users/lucak/CODEE/AGENTS.md`. Recent logs also showed commands failing with `ls: /Users/lucak/Website: No such file or directory`, plus provider empty/invalid-content retries under the previous 12-child/5-peer automatic fanout. |
| Fix | `AGENTS.md` now carries the path-space quoting rule in the auto-loaded project instructions. Active config now throttles delegation to `max_concurrent_children: 4` and disables automatic peer fanout (`minimax_fanout_per_gpt: 0`, `modular_fanout_required: false`, `fanout_policy.enabled: false`). Explicit `delegate_task(tasks=[...])` still works when parallelism is needed. |
| Backup | `/Users/lucak/.hermes/config.yaml.before-website-debug-20260520T104017Z` |
| Verifier | `bash .claude/scripts/verify_wiki.sh`, config sanity check, `hermes status --all`, and hidden-nonce delegated terminal smoke test from this folder. |

## 2026-05-20 CODEE Lock Check

| Field | Current record |
|-------|----------------|
| Outcome wanted | The CLI agent must not be locked to `/Users/lucak/CODEE` when launched from this workspace. |
| Current evidence | Static check: executable resolves to `/Users/lucak/.hermes/hermes-agent/venv/bin/hermes`, config resolves to `/Users/lucak/.hermes/config.yaml`, `terminal.backend=local`, `terminal.cwd=/Users/lucak/Website Development`, and no configured workspace mount points at `/Users/lucak/CODEE` or `/host/codee`. Runtime check: a fresh CLI session launched from this folder wrote `/tmp/website-runtime-lockcheck.json` with `cwd=/Users/lucak/Website Development`, `codee_current=false`, and `website_current=true`. Prompt check: the saved session prompt includes the website path and path-space guidance, while CODEE project markers (`CODEE — Kraken Futures Quant System`, `Kraken Futures`, `Current working directory: /Users/lucak/CODEE`) are absent. |
| Fix | Documentation only: this page and `HERMES.md` now record the active local backend accurately; no runtime config change was required. |
| Verifier | `STATIC_LOCKCHECK_VERDICT: PASS`, `RUNTIME_LOCKCHECK_VERDICT: PASS`, `PROMPT_LOCKCHECK_VERDICT: PASS`, then `bash .claude/scripts/verify_wiki.sh`. |

## Verified Local State

The active config at `/Users/lucak/.hermes/config.yaml` has been updated so Hermes starts in `/Users/lucak/Website Development`. The prior config was saved as `/Users/lucak/.hermes/config.yaml.website-development-before-20260520`.

The active Website Development profile is standalone: it points `terminal.cwd` at this folder, keeps this folder as the writable workspace mount, and does not expose any other project as a normal workspace mount. Cross-project reading should be requested explicitly per task instead of inferred from global mounts.

→ All operations: [[MOC/MOC-Operations]]
