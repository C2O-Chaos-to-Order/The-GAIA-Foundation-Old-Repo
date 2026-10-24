# SIM-IN-NAT-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Classical nucleation as a cluster-size walk (P37): with A = 3, B = 1 (n* = 8, G* = 4 kT) does the simulated mean time to grow from 1 to 16 molecules match the exact birth-death value?

## Phase operationalization tested
NAT Insurgence = a new phase appearing once a cluster passes the critical nucleus (P37).

## Sources this run draws on
P37 (Tokmakoff, Concepts in Biophysical Chemistry, LibreTexts section 19.2, CC BY-NC-SA 4.0; read in full in INB): dG_n = gamma alpha n^(2/3) - d_eps V0 n, n*, G*. Kinetics (attachment rate 1, detailed-balance detachment) and the birth-death MFPT formula are the agent's (standard, not from P37).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | grid max within 1 of n* |
| H1 | hypothesis | MFPT within 4 SE of exact |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Units of kT; tiny clusters, so n^(2/3) surface law is crude. 400 walks. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-B",
 "iteration": 1,
 "kind": "nucleation",
 "seed": 21101,
 "mode": "mfpt",
 "A": 3.0,
 "B": 1.0,
 "N_end": 16,
 "reps": 400,
 "tol_se": 4
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
