# SIM-R7-C4 — simulation library and iterations

Script: `sim_r7.py` (imports `../../tools/runner.py`, byte-identical to Cycles 1–3). Iterations are chained where params set `prev`.

Reproduce: `cd Report-7-Unified/simulation && for k in $(seq 1 12); do python sim_r7.py iter-$k; done` (Python 3 with numpy, scipy). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment. Or from `Research/tools`: `python -m gaia_tools.rerun .. C4`.

Report 7's own Cycle-4 claims (C4-R7-*) are excluded from the simulation's inputs (they are written from its results), so reruns are identical without the Cycle-3 practice of re-running after adding them.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
