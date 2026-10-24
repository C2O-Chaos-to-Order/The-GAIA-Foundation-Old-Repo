# SIM-R7-C2 — simulation library and iterations

Script: `sim_r7.py` (imports `../../tools/runner.py`, byte-identical to Cycle 1). Iterations are chained: iteration k reads `iter-(k-1)/outputs/results.json` where its params set `prev`.

Reproduce: `cd Report-7-Unified/simulation && for k in 1 2 3 4 5 6; do python sim_r7.py iter-$k; done` (Python 3 with numpy, scipy). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment. Or from `Research/tools`: `python -m gaia_tools.rerun .. C2`.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
