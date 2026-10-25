# Maps & Matrix — v33 (covers Cycles 0-4, Master Report, SSC Track Cycles A-D, and the Phases track up to Ascendence Cycle-D-x12)

**Date:** 2026-10-25 · **Tooling:** gaia_tools 0.6.0, data model 1.5.0 (`python -m gaia_tools.phases maps`, which runs `maps_all` unchanged and adds the phase overlay). Earlier versions (v1–v32) are kept unchanged.

## What changed in the matrix
- 449 phase-track claims (all phase cycles so far) are placed on the Phase axis by their own report's phase: Divergence 132; Insurgence 89; Allegiance 88; Convergence 80; Ascendence 60 (organisational placement by report scope; it does not show that a claim instantiates a phase). Earlier README versions said all phase claims were placed on the then-current phase; the placement data were correct, only that sentence was wrong (fix-forward from v26; earlier versions unchanged).
- New projections: `matrix/phase_x_field_30.csv` (5 phases × 6 fields) and `matrix/phase_x_lens_25.csv` (5 phases × 5 lenses). `intersections_625.csv` gains a column `phase_claims_in_being_phase_lens_projection`.
- 447 of 449 phase claims sit **outside the Being axis** (no claim is explicitly about Body, Mind, Soul, Spirit or Consciousness), so the Being × Lens projection is unchanged from v32 and every 625-cell phase count is 0. This is a finding about the grid: field-of-knowledge claims and the Being axis are largely orthogonal.
- Phase × Field movement:
  - Ascendence × Natural-Sciences: populated → populated (11 claims)
  - Ascendence × Formal-Sciences: populated → populated (10 claims)
  - Ascendence × Social-Sciences: populated → populated (10 claims)
  - Ascendence × Applied-Sciences: populated → populated (11 claims)
  - Ascendence × Humanities: populated → populated (9 claims)
  - Ascendence × Philosophy-Spirituality: UNDER-RESEARCHED (no E/P claim) → UNDER-RESEARCHED (no E/P claim) (9 claims)
- Phase × Lens (Ascendence): Truth 15; Integrity 12; Love 6; Justice 0; Wisdom 3 (keyword lens rule v1.0.1, provisional; a navigation aid, not a classification).
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
python -m gaia_tools.phases maps .. ../Maps-and-Matrix/v33-cycles-0-4-mr-track-abcd-phase-dv0abcd-in0abcd-al0abcd-cv0abcd-as0abcd --version-label "..."
```
(The README, `validation/` and `data-model/` folders are written by the build script `build15/docs.py`, not by `phases maps`.)
