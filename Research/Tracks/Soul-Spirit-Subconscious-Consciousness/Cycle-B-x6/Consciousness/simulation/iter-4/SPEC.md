# SIM-CONS-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Consciousness x Love (K28): a single brief mindfulness meditation showed no overall effect on compassion but a significant serial indirect path. Is that pattern what a small, fully mediated effect predicts at n = 80?

## Sources this run draws on
K28 (Gorska & Holas 2025, Sci Rep): n = 80 randomised, no significant overall group effect, serial partial mediation. Path values ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | a1 = 0 indirect <= .05 |
| H1 | hypothesis | total power < .5 |
| H2 | hypothesis | indirect joint-sig > .5 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Linear-normal paths; joint-significance test rather than bootstrap. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-B",
 "iteration": 4,
 "kind": "compassion_mediation",
 "seed": 414,
 "n": 80,
 "a1": 0.8,
 "d": 0.5,
 "b": 0.5,
 "c_direct": 0.0,
 "reps": 3000
}
```

## Command
`python sim_cons.py iter-4` (run from `Consciousness/simulation/`)
