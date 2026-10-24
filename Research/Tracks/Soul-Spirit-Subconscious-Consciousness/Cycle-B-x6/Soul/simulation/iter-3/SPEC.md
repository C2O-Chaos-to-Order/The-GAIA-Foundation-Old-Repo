# SIM-SOUL-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K15 found implicit mind-body dualism even in participants who explicitly rejected dualism. If the implicit score only reflected the same latent belief as the explicit answer, could explicit rejecters show a positive implicit dualism score?

## Sources this run draws on
K15 (Berent & Sansiveri 2025, Open Mind): brief implicit association task, five experiments; dualism evident even among explicit rejecters.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | analytic mean |
| H1 | hypothesis | a = 0: rejecters significantly positive in >= 50% |
| R1 | reporting | by a |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Single latent belief; linear implicit score; illustrative parameters. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-B",
 "iteration": 3,
 "kind": "implicit_explicit",
 "seed": 213,
 "p_endorse": 0.4,
 "g": 0.5,
 "noise": 1.0,
 "n": 120,
 "a_grid": [
  0.0,
  0.1,
  0.3
 ],
 "reps": 3000
}
```

## Command
`python sim_soul.py iter-3` (run from `Soul/simulation/`)
