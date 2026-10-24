# Report-4-Spirit — Cycle 2 change log

## Claims added or annotated (what and why)
- C0v2-R4-01 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R4-03 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R4-04 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R4-05 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R4-07 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R4-15 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C1-R4-07 (E): Complemented in Cycle 2 by mediation simulations (C2-R4-04 to C2-R4-06).
- C1-R4-08 (E): Complemented in Cycle 2 by mediation simulations (C2-R4-04 to C2-R4-06).
- C1-R4-09 (E): Complemented in Cycle 2 by mediation simulations (C2-R4-04 to C2-R4-06).
- C2-R4-01 (E): New in Cycle 2.
- C2-R4-02 (E): New in Cycle 2.
- C2-R4-03 (E): New in Cycle 2.
- C2-R4-04 (E): New in Cycle 2.
- C2-R4-05 (E): New in Cycle 2.
- C2-R4-06 (E): New in Cycle 2.

## Simulation iterations (what changed and why)
- iter-1: Carried agenda (C1 R4: mediation designs). Baseline: under the no-unmeasured-confounding assumption S12 states, the product-of-coefficients method recovers the indirect effect and proportion mediated (PM).
- iter-2: Violate the mediator-outcome no-confounding assumption with an unmeasured U and measure the bias in PM.
- iter-3: W09: with causally ordered mediators there are many decompositions. Does summing separately estimated single-mediator PMs (as a reader might do with S12 Table 4) overstate the joint PM?
- iter-4: Scale dependence: S12 computed PM on the risk-difference scale. How far does a PM from the odds-ratio difference method depart when the outcome is common vs rare?
- iter-5: Inference: at a realistic sample size, does the usual (Sobel) 95% CI keep its coverage, and how much does moderate unmeasured M-Y confounding destroy it?
- iter-6: Consolidation: replicate iterations 2 and 3 with a new seed.

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
