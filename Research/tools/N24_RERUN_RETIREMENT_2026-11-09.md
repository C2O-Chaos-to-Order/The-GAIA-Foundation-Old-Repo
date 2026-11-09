# N24 re-run retirement — 2026-11-09

**Decision:** Kyle Steen (owner), card t44s607, answered 2026-11-09 14:13 CT: RETIRE the GAIA no-op re-run code instead of keeping the repair.

**Verification level:** internal recheck only; **not independent verification**.

## Prior record (kept)

On 2026-11-08 this branch (`fix/w1-n24-rerun-freshness`) applied a freshness repair: `gaia_tools.rerun`, `tracks.rerun`, and `phases.rerun` deleted the copied `EXECUTION_RECORD.json` (and, for `rerun`, listed outputs) before executing, so a script replaced by `pass` could no longer compare a cached record with itself and report `ALL IDENTICAL` with exit 0. That repair and its tests (`tests/test_w1_n24_rerun_freshness.py` as of commit 2b263e61) remain in git history. The CHANGELOG entry "Unreleased — Wave 1 remediation N24 (2026-11-08)" is kept below the retirement entry and marked superseded.

The original audit finding (N24, 2026-11-07, High) was that a no-op script produced a false "ALL IDENTICAL" pass because the checker compared the copied stored record with itself.

## What was retired

Less destructive than deletion: the modules remain importable and the CLI entry points remain so that `--help` still works. The callable paths now refuse immediately with an error whose text includes `retired`:

- `gaia_tools.rerun.run_cycle` / `python -m gaia_tools.rerun`
- `gaia_tools.tracks.rerun` / `python -m gaia_tools.tracks rerun`
- `gaia_tools.phases.rerun` / `python -m gaia_tools.phases rerun`

They do not copy trees, do not execute simulation scripts, and do not compare hashes. Other commands (`validate`, `claimsource`, `maps`) are unchanged.

`.github/` was not touched (`verify.yml` is `workflow_dispatch` only).
