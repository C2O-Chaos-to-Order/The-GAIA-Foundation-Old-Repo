# Maps & Matrix — v22 (covers Cycles 0-4, Master Report, SSC Track Cycles A-D, and the Phases track up to Allegiance Cycle-C-x9)

**Date:** 2026-10-24 · **Tooling:** gaia_tools 0.6.0, data model 1.5.0 (`python -m gaia_tools.phases maps`, which runs `maps_all` unchanged and adds the phase overlay). Earlier versions (v1–v21) are kept unchanged.

## What changed in the matrix
- 292 phase-track claims (all phase cycles so far) are placed on Phase = Allegiance (organisational placement by report scope; it does not show that a claim instantiates a phase).
- New projections: `matrix/phase_x_field_30.csv` (5 phases × 6 fields) and `matrix/phase_x_lens_25.csv` (5 phases × 5 lenses). `intersections_625.csv` gains a column `phase_claims_in_being_phase_lens_projection`.
- 292 of 292 phase claims sit **outside the Being axis** (no claim is explicitly about Body, Mind, Soul, Spirit or Consciousness), so the Being × Lens projection is unchanged from v21 and every 625-cell phase count is 0. This is a finding about the grid: field-of-knowledge claims and the Being axis are largely orthogonal.
- Phase × Field movement:
  - Allegiance × Natural-Sciences: populated → populated (15 claims)
  - Allegiance × Formal-Sciences: populated → populated (10 claims)
  - Allegiance × Social-Sciences: populated → populated (13 claims)
  - Allegiance × Applied-Sciences: populated → populated (12 claims)
  - Allegiance × Humanities: populated → populated (10 claims)
  - Allegiance × Philosophy-Spirituality: UNDER-RESEARCHED (no E/P claim) → UNDER-RESEARCHED (no E/P claim) (11 claims)
- Phase × Lens (Allegiance): Truth 22; Integrity 6; Love 12; Justice 0; Wisdom 0 (keyword lens rule v1.0.1, provisional; a navigation aid, not a classification).
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
python -m gaia_tools.phases maps .. ../Maps-and-Matrix/v22-cycles-0-4-mr-track-abcd-phase-dv0abcd-in0abcd-al0abc --version-label "..."
```
(The README, `validation/` and `data-model/` folders are written by the build script `build15/docs.py`, not by `phases maps`.)
