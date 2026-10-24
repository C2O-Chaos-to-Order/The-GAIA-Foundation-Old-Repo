# SIM-DV-APP-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replicate DV0's single clonal-branching run: is the 1/f signature (R^2 >= 0.98) typical across replicates, or was DV0's 0.958 typical?

## Phase operationalization tested
APP Divergence = neutral branching clonal evolution (P05's neutral-evolution reading).

## Sources this run draws on
DV0 sources P05, P04 (read at cited passages in DV0; not re-read in full in this cycle). The model is unchanged from DV0's clonal_branching.

## Refinement from previous iteration
DV0 ran one replicate (H1 Not supported, R^2 0.958); this iteration runs five with new seeds.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | N reached, bookkeeping exact |
| H1 | hypothesis | median R^2 >= 0.98 |
| R1 | reporting | R^2 per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Cell fractions, no sequencing noise; five replicates only.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-A",
 "iteration": 1,
 "kind": "clonal_branching_reps",
 "seed": 15401,
 "N": 5000,
 "birth": 1.0,
 "death": 0.3,
 "u": 2.0,
 "fmin": 0.1,
 "fmax": 0.4,
 "reps": 5,
 "h1": 0.98
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
