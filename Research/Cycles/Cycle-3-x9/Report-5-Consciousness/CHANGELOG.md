# Report-5-Consciousness — Cycle 3 change log

## Claims added or annotated (what and why)
- C0v2-R5-02 (E): Petersen & Posner 2012 now read in full text (X03): the three-network framework is confirmed. Source X03 and its phrase added.
- C0v2-R5-06 (E): Casali et al. 2013 now read in full text (X05; C3-R5-04).
- C0v2-R5-07 (H): Full text now read (X02): the 'just below criticality' wording is confirmed in the full text; label unchanged (Hypothetical). Source X02 and its phrase added.
- C2-R5-05 (E): Reinterpreted in Cycle 3 (label and status unchanged): with a perturbation scaled to network size the peak is robust (C3-R5-05), so the Cycle-2 non-robustness was a design artefact.
- C3-R5-01 (P): New in Cycle 3.
- C3-R5-02 (P): New in Cycle 3.
- C3-R5-03 (E): New in Cycle 3.
- C3-R5-04 (E): New in Cycle 3.
- C3-R5-05 (E): New in Cycle 3.
- C3-R5-06 (E): New in Cycle 3.
- C3-R5-07 (P): New in Cycle 3.
- C3-R5-08 (P): New in Cycle 3.
- C3-R5-09 (E): New in Cycle 3.

## Simulation iterations (what changed and why)
- iter-1: Code check against Cycle 2.
- iter-2: Redo the failed Cycle-2 robustness test (C2-R5-05) with the perturbation scaled to one module.
- iter-3: Do larger networks keep the peak?
- iter-4: Sensitivity to perturbation strength.
- iter-5: Sensitivity to the response binarisation threshold.
- iter-6: Criticality link (X12): does the PCI-like peak sit where a criticality proxy peaks?
- iter-7: Can spontaneous dynamics predict perturbational complexity (X12's claim, in toy form)?
- iter-8: Anaesthesia-like coupling reduction: do spontaneous and perturbational complexity dissociate?
- iter-9: Consolidation: replicate iteration 2 with new seeds.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
