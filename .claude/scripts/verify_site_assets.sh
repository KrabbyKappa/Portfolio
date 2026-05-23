#!/usr/bin/env bash
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

failures=0

check_path() {
  if [ ! -e "$ROOT/$1" ]; then
    echo "FAIL: missing $1"
    failures=$((failures + 1))
  fi
}

check_contains() {
  file="$1"
  pattern="$2"
  if ! grep -q "$pattern" "$ROOT/$file"; then
    echo "FAIL: $file does not contain $pattern"
    failures=$((failures + 1))
  fi
}

check_path "Bizwholistic/package.json"
check_path "Bizwholistic/astro.config.mjs"
check_path "Bizwholistic/public/robots.txt"
check_path "Bizwholistic/public/llms.txt"
check_path "Bizwholistic/public/llms-full.txt"
check_path "Portfolio-main/index.html"
check_path "Portfolio-main/styles.css"
check_path "Graphify/README.md"
check_path "Graphify/pyproject.toml"
check_path "graphify-out/graph.json"
check_path "AGENTS.md"
check_path ".graphifyignore"
check_path "CLAUDE.md"
check_path "HERMES.md"

if command -v graphify >/dev/null 2>&1; then
  graphify --help >/tmp/.website_graphify_help.out 2>&1
  if [ $? -ne 0 ]; then
    echo "FAIL: graphify --help failed"
    failures=$((failures + 1))
  fi
else
  echo "FAIL: graphify command not found"
  failures=$((failures + 1))
fi

check_contains "AGENTS.md" "graphify"
check_contains ".graphifyignore" "Graphify/"
check_contains ".graphifyignore" "node_modules/"
check_contains ".graphifyignore" "dist/"
check_contains "CLAUDE.md" "Graphify"
check_contains "HERMES.md" "graphify"
check_contains "graphify-out/graph.json" "\"nodes\""

python3 -c "import json, pathlib; data=json.loads(pathlib.Path('$ROOT/graphify-out/graph.json').read_text()); assert isinstance(data.get('nodes'), list) and data['nodes']" >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "FAIL: graphify-out/graph.json is not valid JSON with a non-empty nodes array"
  failures=$((failures + 1))
fi

if [ -f "/Users/lucak/.hermes/config.yaml" ]; then
  if ! grep -q "cwd: /Users/lucak/Website Development" "/Users/lucak/.hermes/config.yaml"; then
    echo "FAIL: Hermes global config does not point terminal.cwd at Website Development"
    failures=$((failures + 1))
  fi
  if ! grep -q "/Users/lucak/Website Development:/host/website-development:rw" "/Users/lucak/.hermes/config.yaml"; then
    echo "FAIL: Hermes global config is missing the website-development writable mount"
    failures=$((failures + 1))
  fi
  if grep -q "/Users/lucak/CODEE" "/Users/lucak/.hermes/config.yaml" || grep -q "/host/codee" "/Users/lucak/.hermes/config.yaml" || grep -q "codee_broker_secret" "/Users/lucak/.hermes/config.yaml"; then
    echo "FAIL: Hermes global config still exposes CODEE as an active workspace mount"
    failures=$((failures + 1))
  fi
else
  echo "FAIL: /Users/lucak/.hermes/config.yaml missing"
  failures=$((failures + 1))
fi

if [ -f "$ROOT/.harness/kanban/package-demo-uniqueness/README.md" ]; then
  if grep -q "/Users/lucak/CODEE" "$ROOT/.harness/kanban/package-demo-uniqueness/README.md"; then
    echo "FAIL: package-demo-uniqueness board still points agents at CODEE rules"
    failures=$((failures + 1))
  fi
fi

if [ "$failures" -ne 0 ]; then
  echo "FAIL: $failures website asset issue(s)"
  exit 1
fi

echo "PASS: website assets and Graphify setup are present"
exit 0
