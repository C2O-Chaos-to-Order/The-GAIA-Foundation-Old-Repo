# Maps & Matrix — v38 (covers Cycles 0-4, Master Report, SSC Track Cycles A-D, and the Phases track up to Transcendence Cycle-D-x12)

**Date:** 2026-10-25 · **Tooling:** gaia_tools 0.6.0, data model 1.5.0 (`python -m gaia_tools.phases maps`, which runs `maps_all` unchanged and adds the phase overlay). Earlier versions (v1–v37) are kept unchanged.

## What changed in the matrix
- 512 phase-track claims (all phase cycles so far) are placed on the Phase axis by their own report's phase: Divergence 132; Insurgence 89; Allegiance 88; Convergence 80; Ascendence 60; Transcendence 63 (organisational placement by report scope; it does not show that a claim instantiates a phase). Earlier README versions said all phase claims were placed on the then-current phase; the placement data were correct, only that sentence was wrong (fix-forward from v26; earlier versions unchanged).
- New projections: `matrix/phase_x_field_30.csv` (5 canonical phases × 6 fields) and `matrix/phase_x_lens_25.csv` (5 phases × 5 lenses). `intersections_625.csv` gains a column `phase_claims_in_being_phase_lens_projection`. **Transcendence (sixth phase, owner update 2026-10-25)** is recorded only in phases-track overlay files `matrix/phase_track_transcendence_x_field_6.csv`, `matrix/phase_track_transcendence_x_lens_5.csv` and `matrix/phase_track_transcendence_cells_125.csv` (the 125 cells a 750-cell matrix would add). The canonical `intersections_625.csv` and `maps.AXES` are **not** re-dimensioned: 625 -> 750 is a pending owner-approved update.
- 510 of 512 phase claims sit **outside the Being axis** (no claim is explicitly about Body, Mind, Soul, Spirit or Consciousness), so the Being × Lens projection is unchanged from v37 and every 625-cell phase count is 0. This is a finding about the grid: field-of-knowledge claims and the Being axis are largely orthogonal.
- Phase × Field movement:

- Phase × Lens (Transcendence):  (keyword lens rule v1.0.1, provisional; a navigation aid, not a classification).
- Graph: field and phase nodes added with PL-* links; claim map and Being × Lens files from `maps_all` are regenerated identically from the same inputs.

## Files
`claim_map/`, `matrix/` (incl. the two new projections), `graph/`, `changes/` (phase claim rows appended), `simulations/simulations_index.json` (all runs incl. phase runs), `data-model/`, `validation/` (phase cycle verification files).

## Honest limits
- Alchemy remains undefined. Phase placement is by report scope only.
- Lens placement uses the provisional keyword rule; e.g. Love and Justice may be empty for a phase because of wording, not substance.
- Links are typed and labelled by the agent that wrote the claims; gate INDETERMINATE (independent review pending).

## Reproduce
```
cd Research/tools && pip install -r requirements.txt
python -m gaia_tools.phases maps .. ../Maps-and-Matrix/v38-cycles-0-4-mr-track-abcd-phase-dv0abcd-in0abcd-al0abcd-cv0abcd-as0abcd-tr0abcd --version-label "..."
```
(The README, `validation/` and `data-model/` folders are written by the build script `build15/docs.py`, not by `phases maps`.)
