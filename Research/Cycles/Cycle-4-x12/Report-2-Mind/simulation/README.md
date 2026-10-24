# SIM-R2-C4 — simulation library and iterations

Script: `sim_r2.py` (imports `../../tools/runner.py`, byte-identical to Cycles 1–3). Iterations are chained where params set `prev`.

Reproduce: `cd Report-2-Mind/simulation && for k in $(seq 1 12); do python sim_r2.py iter-$k; done` (Python 3 with numpy, scipy). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment. Or from `Research/tools`: `python -m gaia_tools.rerun .. C4`.

SUBSTITUTE simulation (disclosed). The rho option (PH associability recovery during delay) is our addition, not from a source.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
