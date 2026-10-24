# SIM-R5-C1 — simulation library and iterations

Script: `sim_r5.py` (imports `../../tools/runner.py`). Iterations are chained: iteration k reads `iter-(k-1)/outputs/results.json` where its params set `prev`.

Reproduce: `cd Report-5-Consciousness/simulation && python sim_r5.py iter-1 && python sim_r5.py iter-2 && python sim_r5.py iter-3` (Python 3 with numpy, scipy, pandas). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
