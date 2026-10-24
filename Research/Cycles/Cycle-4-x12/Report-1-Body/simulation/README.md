# SIM-R1-C4 — simulation library and iterations

Script: `sim_r1.py` (imports `../../tools/runner.py`, byte-identical to Cycles 1–3). Iterations are chained where params set `prev`.

Reproduce: `cd Report-1-Body/simulation && for k in $(seq 1 12); do python sim_r1.py iter-$k; done` (Python 3 with numpy, scipy). `results.json` is deterministic (seeded); `EXECUTION_RECORD.json` also holds timestamps and environment. Or from `Research/tools`: `python -m gaia_tools.rerun .. C4`.

Disclosure: the iteration-10 SPEC says '192-setting grid' but the grid is 4×4×3×3 = 144 (a wording error in the SPEC; the results are correct and the SPEC was not edited after the run).

These are toy or bookkeeping models; see each `SPEC.md` for limits.
