# Report-3-Soul — Cycle 2 change log

## Claims added or annotated (what and why)
- C0v2-R3-01 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-03 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-07 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-09 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-10 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-13 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-14 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-15 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-16 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R3-18 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C1-R3-03 (E): Further pressure in Cycle 2: the typology tolerates only ~4 random cell flips (C2-R3-03).
- C1-R3-04 (E): Further pressure in Cycle 2 (C2-R3-03).
- C1-R3-05 (PS): Remains Indeterminate; Cycle-2 re-coding (C2-R3-01) and tolerance analysis (C2-R3-03) add pressure.
- C2-R3-01 (E): New in Cycle 2.
- C2-R3-02 (E): New in Cycle 2.
- C2-R3-03 (E): New in Cycle 2.
- C2-R3-04 (P): New in Cycle 2.
- C2-R3-05 (E): New in Cycle 2.

## Simulation iterations (what changed and why)
- iter-1: Carried agenda (C1 R3: inter-rater coding). Agreement between the C1 coding (A) and a codebook re-coding (B) of a seeded random sample of 48 of the 180 cells (4 per attribute).
- iter-2: Uncertainty of the agreement estimate: bootstrap CI and Krippendorff's alpha (W08).
- iter-3: Is disagreement concentrated where the cited source is silent (coder B 'uncertain')?
- iter-4: Direction of disagreement: does one coding systematically assign 1 more often (bias), and how does prevalence affect kappa?
- iter-5: Consequence for the Cycle-1 typology: substitute coder B's values on the 48 cells and compare the jaccard/average/k=4 partition with the C1 base (ARI); null = same number of random flips.
- iter-6: Tolerance: how many random cell flips can the typology absorb before its median ARI drops below 0.8, compared with the disagreement rate extrapolated to all 180 cells?

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
