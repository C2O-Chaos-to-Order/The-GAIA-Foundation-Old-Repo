# SIM-IN-NAT-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Is the critical nucleus a point of no return (P37: below n* clusters dissolve, above they grow)? Share of walks started at n* = 27 (A = 4.5, B = 1) that reach 54 before dissolving.

## Phase operationalization tested
NAT Insurgence = the critical nucleus as tipping point.

## Sources this run draws on
P37 (Tokmakoff, Concepts in Biophysical Chemistry, LibreTexts section 19.2, CC BY-NC-SA 4.0; read in full in INB): dG_n = gamma alpha n^(2/3) - d_eps V0 n, n*, G*. Kinetics (attachment rate 1, detailed-balance detachment) and the birth-death MFPT formula are the agent's (standard, not from P37).

## Refinement from previous iteration
Iteration 3 of the x6 family for NAT; follows iteration 2 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | probability |
| H1 | hypothesis | within 0.15 of 1/2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge: a smoke run at n* = 8 gave 0.33 (not supported at that size); the size was raised to 27 for this run, the threshold kept. 1,000 walks. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-B",
 "iteration": 3,
 "kind": "nucleation",
 "seed": 21103,
 "mode": "commit",
 "A": 4.5,
 "B": 1.0,
 "N_end": 54,
 "reps": 1000,
 "h1": 0.15
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
