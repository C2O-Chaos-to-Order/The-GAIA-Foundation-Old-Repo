# SIM-CONS-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K32: clinical dream recall (3%-8%) is far below experimental recall (often 40%-80%); immediate interviews give about 10% versus about 6% when delayed. Can interview timing explain the gap?

## Sources this run draws on
K32: immediate interviews 9.7% and 10.4% vs 5.9% when delayed >= 24 h; clinical typically 3%-8%; experimental often 40%-80%. Midpoints used.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = arithmetic |
| H1 | hypothesis | timing explains < 20% of the gap |
| R1 | reporting | retention |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Cross-study figures combined; assumes a uniform timing effect.

## Parameters
```json
{
 "sim_id": "SIM-CONS-C",
 "iteration": 3,
 "kind": "recall_gap",
 "seed": 813,
 "recall_immediate": 0.1,
 "recall_delayed": 0.059,
 "clinical_typical": 0.055,
 "experimental_typical": 0.6
}
```

## Command
`python sim_cons.py iter-3` (run from `Consciousness/simulation/`)
