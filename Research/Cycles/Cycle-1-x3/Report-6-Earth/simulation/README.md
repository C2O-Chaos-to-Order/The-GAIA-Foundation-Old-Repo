# SIM-R6-C1 — simulation library and iterations

Script: `sim_r6.py` (imports `../../tools/runner.py`). Iterations are chained: iteration k reads `iter-(k-1)/outputs/results.json` where its params set `prev`.

Reproduce: `cd Report-6-Earth/simulation && python sim_r6.py iter-1 && python sim_r6.py iter-2 && python sim_r6.py iter-3` (Python 3 with numpy, scipy, pandas). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
