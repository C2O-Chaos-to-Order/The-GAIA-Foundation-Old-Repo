# SIM-R3-C4 — simulation library and iterations

Script: `sim_r3.py` (imports `../../tools/runner.py`, byte-identical to Cycles 1–3). Iterations are chained where params set `prev`.

Reproduce: `cd Report-3-Soul/simulation && for k in $(seq 1 12); do python sim_r3.py iter-$k; done` (Python 3 with numpy, scipy). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment. Or from `Research/tools`: `python -m gaia_tools.rerun .. C4`.

Stability is not reliability: all codings (A, B, coder C) are by the same research agent.

These are toy or bookkeeping models; see each `SPEC.md` for limits.
