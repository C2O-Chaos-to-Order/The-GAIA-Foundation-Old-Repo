# Cycle 0 — Baseline v2 (Cycle 0, framework-aligned)

**Version label:** Baseline v2 (Cycle 0, framework-aligned) · **Date:** 2026-10-24 · **Prepared by:** Grok Bot for Kyle Alexander Steen · **Gate:** INDETERMINATE (not independently reviewed).

**Governing scope:** `FRAMEWORK.md`, a copy of the owner's Seven-Report Foundational Framework with the organizing principle **GAIA Is the Motherthread** (labelled Philosophical/Spiritual) and a label-mapping appendix. **Integrity rules:** Research/README.md and Research/RESEARCH_PLAN_EXTENSION.md. Every conclusion carries one framework label: Established, Plausible, Philosophical/Spiritual or Hypothetical.

| Report | Folder | Claims (E / P / PS / H) | Simulation | Checks |
|---|---|---|---|---|
| 1 Body | `Report-1-Body/` | 16 (13 / 2 / 1 / 0)* | SIM-R1-C0 feedback + feedforward homeostasis toy | 7/7 pass |
| 2 Mind | `Report-2-Mind/` | 13 (7 / 3 / 3 / 0)* | SIM-R2-C0 Rescorla–Wagner blocking + forgetting-curve fits | 4/4 pass |
| 3 Soul | `Report-3-Soul/` | 18 (13 / 0 / 5 / 0)* | SIM-R3-C0 14-tradition × 12-attribute overlap analysis | 3/3 pass; result coding-sensitive (Indeterminate) |
| 4 Spirit | `Report-4-Spirit/` | 15 (9 / 2 / 3 / 1)* | SIM-R4-C0 E-value + **corrected** confounding Monte Carlo | 5/5 pass (v1 E2 Fail archived) |
| 5 Consciousness | `Report-5-Consciousness/` | 12 (6 / 3 / 2 / 1)* | SIM-R5-C0 toy recurrent ignition | 3/3 pass |
| 6 Earth (A life, B core) | `Report-6-Earth/` | 19 (12 / 4 / 3 / 0)* | SIM-R6-C0 Daisyworld + IGRF dipole + free decay | 4/4 pass |
| 7 Unified (GAIA motherthread) | `Report-7-Unified/` | 7 (5 / 0 / 2 / 0)* + 24-link register | SIM-R7-C0 ledgers, link register, 625-index, matrix arithmetic | 10/10 pass |

\*Counts from `claims/claims.csv` (E = Established, P = Plausible, PS = Philosophical/Spiritual, H = Hypothetical). Totals: 100 claims (65 / 14 / 19 / 2); 75 external sources plus 3 governing documents.

- One-page summary: `SUMMARY.md` · Verification: `Verification/VERIFICATION.md`
- Sources: `Provenance/SOURCE_REGISTER.csv` (third-party snapshots kept off-repo, identified by SHA-256)
- Integrity: `Provenance/MANIFEST.sha256` (run `sha256sum -c Provenance/MANIFEST.sha256` from this folder)
- Reproduce: `python <Report>/simulation/<script>.py` (Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1, pandas 3.1.0)

Repository context: `main` @ 7875b4e holds only README.md, Research/README.md and Research/RESEARCH_PLAN_EXTENSION.md. Files the top-level README mentions (Global Research Completion Gate, Albedo checkpoint, Research/Validation/, Report-18 branch) are **not present** on any branch (see `Provenance/tree_main_7875b4e.txt`, `Provenance/tree_prior_11a2107.txt`).

## Change history (v1 → v2)
- **2026-10-24 — Baseline v2 (Cycle 0, framework-aligned).** Redone at the owner's request against the Seven-Report Foundational Framework, because v1 leaned on the repository's older files rather than the framework.
  - **Scope:** every framework scope item for every report is now covered and mapped in each REPORT.md, closing all gaps listed in v1 Verification (R1 nervous system, perception, environment; R2 thought, reasoning, emotion, perception, identity, learning, mind–body; R3 ten traditions plus identity, character, purpose, independence; R4 vitality, transcendence, connection, inspiration plus well-being evidence; R5 attention, self-awareness, perception, altered states, origin/nature; R6 biodiversity, interdependence, philosophy of the whole, heat transfer, planetary dynamics, heart symbol; R7 all seven link types with tests and rejection criteria).
  - **Labels:** the four framework labels on every claim and link, mapped to repository statuses (FRAMEWORK.md appendix).
  - **GAIA Is the Motherthread:** added to FRAMEWORK.md as the organizing principle (owner instruction, 2026-10-24). Report 7 is organized around it, with every link traced back to it. It is labelled Philosophical/Spiritual and kept separate from the Gaia-hypothesis and Earth-system science.
  - **Sources:** 30 → 78 register entries. Added the 17 usable pre-fetched Cycle-1 sources (T01–T08 with T07e, T10–T17; T09 dropped for lack of an abstract, T18 not needed) and 30 new sources (U-series, U01–U50).
  - **Simulations** were all re-run fresh. R1 adds feedforward checks E6–E7. R3 is re-coded to 14×12 with Monte Carlo robustness. **R4's confounding model is corrected:** v1 E2 failed because of a specification error; the v1 run is kept unaltered in `Report-4-Spirit/simulation/archive_v1/`. R7 adds label-mapping checks, a per-check SIM-citation rule (refined E7), a link-register check (E9) and a no-metaphor-as-evidence check (E10). R2, R5 and R6 numbers are unchanged; R6 CSVs now use LF line endings.
  - **Verification:** 55/55 Established literature claims re-verified against live re-fetches (92/92 passages found), up from 8/42 in v1.
  - Every v1 path is kept: v1 files are superseded in place (same paths, v2 content), and the v1 text remains in this branch's git history. Claim IDs changed from `C0-Rn-xx` to `C0v2-Rn-xx`; each REPORT.md change history maps the old IDs to the new ones.
- **2026-10-23 — Baseline (Cycle 0) v1.** First pass (42 claims, 30 sources, gate Indeterminate; SIM-R4 E2 and SIM-R7 E7 failed and were recorded).
