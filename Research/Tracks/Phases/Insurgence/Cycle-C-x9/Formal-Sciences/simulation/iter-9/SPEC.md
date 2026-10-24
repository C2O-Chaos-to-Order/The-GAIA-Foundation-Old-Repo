# SIM-IN-FOR-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INA-FOR-04 (K = 1000) on a third seed.

## Phase operationalization tested
FOR Insurgence = lineage survival (replication).

## Sources this run draws on
P27.

## Refinement from previous iteration
Iteration 9 of the x9 family for FOR; follows iteration 8 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | probabilities |
| H1 | hypothesis | within 4 SE + 0.01 of s |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-C",
 "iteration": 9,
 "kind": "gw_survival",
 "seed": 22209,
 "c_values": [
  1.1,
  1.5,
  2.0,
  3.0
 ],
 "reps": 5000,
 "K": 1000,
 "tol_se": 4,
 "bias": 0.01
}
```

## Command
`python sim_for.py iter-9` (run from `Formal-Sciences/simulation/`)
