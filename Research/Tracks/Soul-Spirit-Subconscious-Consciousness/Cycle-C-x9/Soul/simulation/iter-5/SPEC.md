# SIM-SOUL-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K46 classified NDEs by a self-report scale cut-off. With a reliable but imperfect scale, how many classified cases are true non-cases?

## Sources this run draws on
K46 (NDE-C scale; 23 of 63 classified as NDE). Reliability .8 ILLUSTRATIVE (not reported in what was read).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | PPV = bivariate normal |
| H1 | hypothesis | >= 20% false cases |
| R1 | reporting | agreement |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Continuous latent trait; symmetric cut-offs. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 5,
 "kind": "cutoff_misclass",
 "seed": 615,
 "N": 1000000,
 "rel": 0.8,
 "prev": 0.37
}
```

## Command
`python sim_soul.py iter-5` (run from `Soul/simulation/`)
