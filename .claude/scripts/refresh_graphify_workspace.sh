#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$ROOT"

mkdir -p /tmp/website-development-graphify
if [ -f graphify-out/graph.json ]; then
  cp graphify-out/graph.json /tmp/website-development-graphify/graph-before-refresh.json
  rm -f graphify-out/graph.json
fi

graphify update . --no-cluster --force
python3 - <<'PY'
import json
from pathlib import Path
path = Path('graphify-out/graph.json')
data = json.loads(path.read_text(encoding='utf-8'))
for key in ('links', 'edges', 'hyperedges'):
    if key not in data or not isinstance(data[key], list):
        continue
    seen = set()
    unique = []
    for item in data[key]:
        marker = json.dumps(item, sort_keys=True, separators=(',', ':'))
        if marker in seen:
            continue
        seen.add(marker)
        unique.append(item)
    data[key] = unique
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
PY
graphify tree --graph graphify-out/graph.json --output graphify-out/GRAPH_TREE.html --root "$ROOT" --label "Website Development"
python3 .claude/scripts/verify_graphify_workspace.py
