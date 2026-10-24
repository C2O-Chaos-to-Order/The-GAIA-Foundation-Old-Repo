# SIM-SPIRIT-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Follow-up to SIM-SPIRIT-A iteration 3: does a Holm correction across four outcome families control error, and at what cost in power for one real effect?

## Sources this run draws on
K05 (four outcome families).

## Refinement from previous iteration
Cycle A measured the uncorrected family-wise rate.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Holm FWER <= .06 |
| H1 | hypothesis | power loss <= 10 points |
| R1 | reporting | power |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Equicorrelated normal outcomes. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-B",
 "iteration": 4,
 "kind": "holm_outcomes",
 "seed": 314,
 "k": 4,
 "r": 0.3,
 "n": 60,
 "d": 0.5,
 "reps": 4000
}
```

## Command
`python sim_spirit.py iter-4` (run from `Spirit/simulation/`)
