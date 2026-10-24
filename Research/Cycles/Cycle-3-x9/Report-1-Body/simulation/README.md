# SIM-R1-C3 — simulation library and iterations

Script: `sim_r1.py` (imports `../../tools/runner.py`, byte-identical to Cycles 1–2). Iterations are chained: iteration k reads `iter-(k-1)/outputs/results.json` where its params set `prev`.

Reproduce: `cd Report-1-Body/simulation && for k in 1 2 3 4 5 6 7 8 9; do python sim_r1.py iter-$k; done` (Python 3 with numpy, scipy). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment. Or from `Research/tools`: `python -m gaia_tools.rerun .. C3`.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
