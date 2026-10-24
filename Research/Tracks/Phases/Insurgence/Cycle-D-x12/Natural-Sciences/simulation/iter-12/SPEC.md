# SIM-IN-NAT-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INB-NAT iter-1 (nucleation MFPT) on a new seed.

## Phase operationalization tested
NAT Insurgence = a new phase appearing once a cluster passes the critical nucleus (P37).

## Sources this run draws on
P37 (Tokmakoff, Concepts in Biophysical Chemistry, LibreTexts section 19.2, CC BY-NC-SA 4.0; read in full in INB): dG_n = gamma alpha n^(2/3) - d_eps V0 n, n*, G*. Kinetics (attachment rate 1, detailed-balance detachment) and the birth-death MFPT formula are the agent's (standard, not from P37).

## Refinement from previous iteration
Iteration 12 of the x12 family for NAT; follows iteration 11 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | grid max within 1 of n* |
| H1 | hypothesis | MFPT within 4 SE of exact |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-D",
 "iteration": 12,
 "kind": "nucleation",
 "seed": 23112,
 "mode": "mfpt",
 "A": 3.0,
 "B": 1.0,
 "N_end": 16,
 "reps": 400,
 "tol_se": 4
}
```

## Command
`python sim_nat.py iter-12` (run from `Natural-Sciences/simulation/`)
