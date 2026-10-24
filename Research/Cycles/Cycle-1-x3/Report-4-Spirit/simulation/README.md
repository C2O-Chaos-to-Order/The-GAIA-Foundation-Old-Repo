# SIM-R4-C1 — simulation library and iterations

Script: `sim_r4.py` (imports `../../tools/runner.py`). Iterations are chained: iteration k reads `iter-(k-1)/outputs/results.json` where its params set `prev`.

Reproduce: `cd Report-4-Spirit/simulation && python sim_r4.py iter-1 && python sim_r4.py iter-2 && python sim_r4.py iter-3` (Python 3 with numpy, scipy, pandas). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
