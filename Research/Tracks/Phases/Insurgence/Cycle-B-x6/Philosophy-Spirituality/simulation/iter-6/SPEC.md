# SIM-IN-PHI-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of IN0-PHI-02 (CRP, alpha 5) on a new seed.

## Phase operationalization tested
PHI Insurgence = continuing novelty (replication; interpretive).

## Sources this run draws on
P08 (read in full in DVB); CRP is the agent's stand-in.

## Refinement from previous iteration
Iteration 6 of the x6 family for PHI; follows iteration 5 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | within 4 SE |
| H1 | hypothesis | more forms at 100,000 |
| H2 | hypothesis | rate < 0.01 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-B",
 "iteration": 6,
 "kind": "novelty_stream",
 "seed": 21606,
 "alpha": 5.0,
 "n_values": [
  1000,
  10000,
  100000
 ],
 "reps": 200,
 "tol_se": 4,
 "h2": 0.01
}
```

## Command
`python sim_phi.py iter-6` (run from `Philosophy-Spirituality/simulation/`)
