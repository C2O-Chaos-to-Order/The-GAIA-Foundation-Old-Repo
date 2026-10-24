# SIM-SPIRIT-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. Lower reliabilities (.6-.7), as for short or translated scales.

## Sources this run draws on
K43, K45 (as iteration 3).

## Refinement from previous iteration
Iteration 3 used .7/.9.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = analytic |
| H1 | hypothesis | loss >= .05 |
| R1 | reporting | disattenuated |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 3.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-C",
 "iteration": 7,
 "kind": "attenuation",
 "seed": 717,
 "N": 200000,
 "cases": {
  "low_rel": [
   0.3,
   0.6,
   0.7
  ],
  "high_rel": [
   0.3,
   0.9,
   0.9
  ]
 },
 "test_case": "low_rel",
 "observed": {
  "K45_spirituality_mindfulness": [
   0.198,
   0.6,
   0.7
  ]
 }
}
```

## Command
`python sim_spirit.py iter-7` (run from `Spirit/simulation/`)
