# Report-6-Earth — Cycle 2 change log

## Claims added or annotated (what and why)
- C0v2-R6-06 (E): Counterevidence/limits field filled in Cycle 2 (was empty). Limits field filled; adaptive-Daisyworld literature added (C2-R6-01 to C2-R6-03).
- C0v2-R6-09 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R6-10 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R6-11 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R6-12 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R6-13 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R6-19 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C1-R6-08 (E): Now matched to the published literature (C2-R6-01; W01 full text) and replicated on a finer rate grid (C2-R6-04).
- C2-R6-01 (E): New in Cycle 2.
- C2-R6-02 (P): New in Cycle 2.
- C2-R6-03 (E): New in Cycle 2.
- C2-R6-04 (E): New in Cycle 2.
- C2-R6-05 (E): New in Cycle 2.
- C2-R6-06 (E): New in Cycle 2.

## Simulation iterations (what changed and why)
- iter-1: Replicate the Cycle-1 toy exactly, then test the Robertson & Robinson 1998 (W02) design claim over a finer grid of adaptation rates: unconstrained adaptation of optimum temperature erodes regulation.
- iter-2: Test the Lenton & Lovelock 2000 (W03) / 2001 (W01 sec. 6.3) design claim: bounds on adaptation plus growth limitation near the bounds recover regulation.
- iter-3: Test the W03 verbal argument that adaptation fast relative to environmental change removes the need for (and the fact of) regulation, by varying forcing speed (steps per luminosity increment) against adaptation rate.
- iter-4: A second, band-independent regulation metric: damping ratio = mean |dTe/dL| lifeless / with life inside the habitable band.
- iter-5: Test W01's statement (citing Stocker 1995, not read) that mutation of the trait extends regulation: k albedo types with neighbour mutation.
- iter-6: Consolidation: do the iteration 1-2 conclusions (unbounded erodes, constrained recovers) hold across death rate gamma and heat-transfer q?

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
