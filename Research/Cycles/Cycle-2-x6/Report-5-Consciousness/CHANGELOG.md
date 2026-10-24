# Report-5-Consciousness — Cycle 2 change log

## Claims added or annotated (what and why)
- C0v2-R5-01 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R5-03 (P): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R5-08 (E): Counterevidence/limits field filled in Cycle 2 (was empty).
- C0v2-R5-12 (PS): Counterevidence/limits field filled in Cycle 2 (was empty).
- C2-R5-01 (P): New in Cycle 2.
- C2-R5-02 (P): New in Cycle 2.
- C2-R5-03 (E): New in Cycle 2.
- C2-R5-04 (E): New in Cycle 2.
- C2-R5-05 (E): New in Cycle 2.
- C2-R5-06 (P): New in Cycle 2.

## Simulation iterations (what changed and why)
- iter-1: Validate the Lempel-Ziv (LZ76, Kaspar-Schuster) implementation used for both spontaneous and perturbational complexity.
- iter-2: Spontaneous complexity vs coupling: is it simply maximal for independent (uncoupled) units? (The known confound that motivates perturbational measures.)
- iter-3: Perturbational (PCI-like) complexity vs coupling: does it peak at intermediate coupling (integrated AND differentiated responses)?
- iter-4: Dissociation: an uncoupled, very noisy network vs the network at the PCI-like peak found in iteration 3.
- iter-5: 'Anaesthesia-like' manipulation (loosely after W13): reduce between-module coupling at fixed within-module coupling; does PCI-like fall?
- iter-6: Consolidation: does the iteration-3 inverted-U replicate across network sizes and seeds?

## Development disclosure
Simulation code was smoke-tested before the official runs; official iterations were run in this tree and re-executed byte-identically by `Research/tools` (`gaia_tools.rerun`). Pre-registered checks were not changed after seeing results; any re-runs are listed in `../CHANGELOG.md`.
