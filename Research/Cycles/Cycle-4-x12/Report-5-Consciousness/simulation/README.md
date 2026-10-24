# SIM-R5-C4 — simulation library and iterations

Script: `sim_r5.py` (imports `../../tools/runner.py`, byte-identical to Cycles 1–3). Iterations are chained where params set `prev`.

Reproduce: `cd Report-5-Consciousness/simulation && for k in $(seq 1 12); do python sim_r5.py iter-$k; done` (Python 3 with numpy, scipy). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment. Or from `Research/tools`: `python -m gaia_tools.rerun .. C4`.

Generic branching process, not a brain model.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
