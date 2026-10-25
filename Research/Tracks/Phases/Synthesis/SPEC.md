# SPEC — Six-phase SYNTHESIS (SIM-PH-SYN/iter-1)

Status: written 2026-10-25 before the aggregation script was run. Branch `research/phase-synthesis`, stacked on `research/phase-transcendence-x12` @ 3ae9bf57. Plan: `../PLAN.md` §7 as amended by §9 (six-phase synthesis after Transcendence x12).

## Purpose
Produce `../SYNTHESIS.md`, a cross-phase, cross-field synthesis of the six phase reports (Divergence, Insurgence, Allegiance, Convergence, Ascendence, Transcendence), using **only** what is already in the repository: the 30 cycle ledgers (`<Phase>/Cycle-*/<Field>/claims/claims.csv`), the 1,116 simulation `EXECUTION_RECORD.json` files, the research `PASSES.md` files, the source and link registers, and Maps v38 (`Research/Maps-and-Matrix/v38-...-tr0abcd/matrix/`). No new sources are read, no new simulations of the world are run and **no new claims** are made: every substantive statement in the synthesis cites an existing claim ID (with its ledger label), link ID (with its label), source ID or record. The synthesis is itself a synthesis document, not a ledger; it adds no rows to any claims.csv.

## Operation (deterministic; no randomness, no seeds)
`tools/synth.py aggregate` reads the inputs above and writes:
- `data/cycle_totals.csv` — per phase and cycle: claims by label, runs, validation pass/total, hypothesis Supported / Not supported / other, passes, passes recorded "Added nothing", passes whose "Read" line is "nothing new", sources first added in the cycle.
- `data/field_footprint.csv` — per phase and field in the x12 ledger: claims by label and by claim class, distinct sources cited, claims citing exactly one source, claims citing no P-source.
- `data/field_track.csv` — per field across the six x12 ledgers: distinct sources (union), claims, share of Simulation-class claims.
- `data/phase_links.csv` — every link of type "phase relation" (and PL-05, the GAIA motherthread link) with its label and the labels of the claims it cites (resolved in the cycle ledger named by each claim ID).
- `data/matrix_v38.json` — summary of Maps v38: phase x field and phase x lens counts, flagged cells, number of claims placed on the Phase axis and on the Being axis, and the Transcendence overlay status.
- `data/arithmetic.json` — README §10 arithmetic, recomputed.

`tools/synth.py render` fills the tables in `tools/SYNTHESIS.template.md` from `data/` and writes `../SYNTHESIS.md`. `tools/synth.py check` runs the citation checks below on the rendered file and writes `EXECUTION_RECORD.json`.

## Pre-registered checks
- **V1 (validation)** — for each phase, the x12 per-field label counts recomputed from the ledgers equal Maps v38 `phase_x_field_30.csv` (five phases) and `phase_track_transcendence_x_field_6.csv` (Transcendence): 36 of 36 rows equal.
- **V2 (validation)** — exactly 1,116 EXECUTION_RECORD.json files are found (6 phases x 186), each phase 186, and every record has `status` and `pre_registered_checks`.
- **V3 (validation)** — README §10 arithmetic: M = a b^T + 1 with a = (0,1,3,5,0), b = (3,6,9,12) reproduces the printed 5 x 4 table exactly; 5^4 = 625; 5 x 5 x 6 x 5 = 750; the later pattern A*B*C (element-wise) times D gives the zero vector.
- **C1 (citation)** — every claim ID written in `../SYNTHESIS.md` resolves to a row in the ledger of the cycle its prefix names, and each is followed by `[<label>]` equal to that row's `framework_label`.
- **C2 (citation)** — every link ID (`PL-nn`) written resolves in a Phases link register and is followed by `[<label>]` equal to its `framework_label`.
- **C3 (citation)** — every source ID (`Pnn`) written resolves in a Phases SOURCE_REGISTER.
- **C4 (no new claims)** — no claims.csv, link register or source register is changed on the branch (git diff against the base lists none).
- **R1 (reporting)** — counts of the synthesis's own citations (claims, links, sources).

Indeterminate is never Pass. A failed check is reported, not hidden; the text is corrected and the check re-run only for citation typos (C1-C3), and each such correction is listed in the record.

## Limitations (stated before the run)
- The synthesis can only be as strong as the ledgers; every phase gate is INDETERMINATE (independent review pending), so nothing here is reviewed.
- "Saturation" is read from recorded counts (new sources, empty passes, hypothesis support); the phases did not record empty passes in one consistent way, which the aggregation measures directly from PASSES.md.
- The owner's level-to-phase pattern is recorded as the owner's Hypothetical claim; it is not tested. Quantum's role in that pattern is not defined in the repository and is reported as unconfirmed.
- The matrix stays at 625 canonical cells; Transcendence is reported only from the phases-track overlay files (625 -> 750 pending owner approval).
- Maps: PLAN §6/§9 assign Maps versions to cycles only (v9-v38); the plan does not call for a Maps version for the synthesis, so none is made.
