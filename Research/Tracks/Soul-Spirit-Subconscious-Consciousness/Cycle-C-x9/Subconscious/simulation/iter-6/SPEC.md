# SIM-SUBC-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Toy illustration of K36's HYPOTHESIS that the felt authorship of action is a conditioned misattribution: can a causally idle 'intention' signal that merely precedes action come to predict it strongly?

## Sources this run draws on
K36 (Kansala et al. 2026, Hypothesis and Theory): free will as a conditioned illusion from the temporal contiguity of premotor and motor activations.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | uninformative intention -> chance |
| H1 | hypothesis | learned prediction >= .80 |
| R1 | reporting | trajectory |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Delta-rule learner; one cause; no dopamine or timing model. Illustrates the logic only; it is not evidence that the hypothesis is true. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-C",
 "iteration": 6,
 "kind": "superstitious_conditioning",
 "seed": 516,
 "trials": 2000,
 "noise": 0.5,
 "noise_null": 100.0,
 "lr": 0.05
}
```

## Command
`python sim_subc.py iter-6` (run from `Subconscious/simulation/`)
