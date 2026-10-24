#!/usr/bin/env bash
# Verify every MANIFEST.sha256 in the repository (research tooling only; read-only).
# Convention: a manifest stored in a folder named "Provenance" lists paths relative to
# that folder's parent (the cycle root); every other manifest lists paths relative to
# its own folder. Exit status is non-zero if any manifest fails or none is found.
set -uo pipefail
root="${1:-.}"
cd "$root" || exit 2
fail=0; n=0
while IFS= read -r -d '' m; do
  n=$((n+1))
  dir=$(dirname "$m")
  base=$dir
  [ "$(basename "$dir")" = "Provenance" ] && base=$(dirname "$dir")
  rel=$(realpath --relative-to="$base" "$m")
  if (cd "$base" && sha256sum --check --quiet --strict "$rel"); then
    echo "PASS $m ($(grep -c . "$m") entries)"
  else
    echo "FAIL $m"; fail=1
  fi
done < <(find . -name MANIFEST.sha256 -not -path './.git/*' -print0 | sort -z)
if [ "$n" -eq 0 ]; then echo "FAIL no manifests found"; exit 1; fi
echo "manifests checked: $n; result: $([ $fail -eq 0 ] && echo PASS || echo FAIL)"
exit $fail
