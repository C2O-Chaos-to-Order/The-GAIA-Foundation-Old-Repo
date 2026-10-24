# SIM-IN-FOR-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Lineage survival very close to criticality: c = 1.02, 1.05 with K = 10,000.

## Phase operationalization tested
FOR Insurgence = lineage survival (branching approximation, P27).

## Sources this run draws on
P27 (read in full in IN0).

## Refinement from previous iteration
Iteration 7 of the x9 family for FOR; follows iteration 6 (see Purpose).

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
 "iteration": 7,
 "kind": "gw_survival",
 "seed": 22207,
 "c_values": [
  1.02,
  1.05
 ],
 "reps": 5000,
 "K": 10000,
 "tol_se": 4,
 "bias": 0.01
}
```

## Command
`python sim_for.py iter-7` (run from `Formal-Sciences/simulation/`)
