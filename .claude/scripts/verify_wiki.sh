#!/usr/bin/env bash
set -u

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

echo "=== website wiki lint gate ==="

python3 "$ROOT/wiki/_find_broken.py" > /tmp/.website_wiki_broken.out 2>&1
BROKEN=$?
python3 "$ROOT/wiki/_audit.py" > /tmp/.website_wiki_audit.out 2>&1
AUDIT=$?
bash "$ROOT/.claude/scripts/verify_site_assets.sh" > /tmp/.website_assets.out 2>&1
ASSETS=$?
python3 -c "import ast, pathlib, sys; [ast.parse(pathlib.Path(p).read_text(), filename=p) for p in sys.argv[1:]]" "$ROOT/wiki/_find_broken.py" "$ROOT/wiki/_audit.py" "$ROOT/.claude/scripts/verify_graphify_workspace.py" "$ROOT/.claude/scripts/tests/test_wiki_system.py" > /tmp/.website_wiki_syntax.out 2>&1
SYNTAX=$?

echo "_find_broken.py:        $([ "$BROKEN" -eq 0 ] && echo PASS || echo FAIL)  ($(head -1 /tmp/.website_wiki_broken.out))"
echo "_audit.py:              $([ "$AUDIT" -eq 0 ] && echo PASS || echo FAIL)  ($(head -1 /tmp/.website_wiki_audit.out))"
echo "verify_site_assets.sh:  $([ "$ASSETS" -eq 0 ] && echo PASS || echo FAIL)  ($(tail -1 /tmp/.website_assets.out))"
echo "python_syntax:          $([ "$SYNTAX" -eq 0 ] && echo PASS || echo FAIL)"

if [ "$BROKEN" -ne 0 ] || [ "$AUDIT" -ne 0 ] || [ "$ASSETS" -ne 0 ] || [ "$SYNTAX" -ne 0 ]; then
  echo
  echo "---- _find_broken.py output ----"
  cat /tmp/.website_wiki_broken.out
  echo
  echo "---- _audit.py output ----"
  cat /tmp/.website_wiki_audit.out
  echo
  echo "---- verify_site_assets.sh output ----"
  cat /tmp/.website_assets.out
  echo
  echo "---- python_syntax output ----"
  cat /tmp/.website_wiki_syntax.out
  echo
  echo "VERDICT: FAIL -- keep working."
  exit 1
fi

echo "VERDICT: PASS -- safe to proceed."
exit 0
