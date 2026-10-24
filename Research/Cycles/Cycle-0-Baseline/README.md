# Cycle 0 — Baseline

**Version label:** Baseline (Cycle 0) · **Date:** 2026-10-23 · **Prepared by:** Grok Bot for Kyle Alexander Steen · **Gate:** INDETERMINATE (not independently reviewed).

Scope: one bounded research pass and one simulation execution for each of the seven reports defined in `Research/RESEARCH_PLAN_EXTENSION.md` §2, then an internal Verification.

| Report | Folder | Simulation | Checks |
|---|---|---|---|
| 1 Body | `Report-1-Body/` | SIM-R1-C0 negative-feedback homeostasis toy | 5/5 pass (E1 substituted check documented) |
| 2 Mind | `Report-2-Mind/` | SIM-R2-C0 Rescorla–Wagner blocking + forgetting-curve fits | 4/4 pass |
| 3 Soul | `Report-3-Soul/` | SIM-R3-C0 interpretive-coding overlap analysis | 2/2 pass; result Indeterminate (coding-sensitive) |
| 4 Spirit | `Report-4-Spirit/` | SIM-R4-C0 E-value + confounding Monte Carlo | 2/3 — **E2 Fail** (spec error, preserved) |
| 5 Consciousness | `Report-5-Consciousness/` | SIM-R5-C0 toy recurrent ignition | 3/3 pass |
| 6 Earth | `Report-6-Earth/` | SIM-R6-C0 Daisyworld + IGRF dipole + free decay | 4/4 pass |
| 7 Unified | `Report-7-Unified/` | SIM-R7-C0 625-index, matrix arithmetic, ledger consistency | 7/8 — **E7 Fail** (reviewed in Verification) |

- Verification: `Verification/VERIFICATION.md`
- Sources: `Provenance/SOURCE_REGISTER.csv` (30 sources; third-party page snapshots are kept off-repo, identified by SHA-256)
- Integrity: `Provenance/MANIFEST.sha256` (verify with `sha256sum -c Provenance/MANIFEST.sha256` from this folder)
- Reproduce: `python <Report>/simulation/<script>.py` (Python 3.13, NumPy 2.5, SciPy 1.18, pandas 3.1)

Repository context at the time of work: `main` @ 7875b4e held only README.md, Research/README.md and Research/RESEARCH_PLAN_EXTENSION.md. Files the top-level README refers to (Global Research Completion Gate, Albedo checkpoint, Research/Validation/, Report-18 branch) are **not present** on any branch (see `Provenance/tree_main_7875b4e.txt`, `Provenance/tree_prior_11a2107.txt`).
