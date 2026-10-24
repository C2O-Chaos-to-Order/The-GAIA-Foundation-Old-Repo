# SIM-IN-FOR-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
The critical window (P36): with c = 1 + lambda n^(-1/3), lambda = 0, is the largest component ~ n^(2/3) over n = 10^3 to 10^6?

## Phase operationalization tested
FOR Insurgence = the critical window of the giant-component transition.

## Sources this run draws on
P36 (Goldschmidt, Warwick lecture 3, 27 April 2009, slides PDF; read in full in INB): in the critical window p = 1/n + lambda n^(-4/3) the largest components are of size Theta(n^(2/3)). P27 for the transition.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | fraction falls with n |
| H1 | hypothesis | slope within 0.1 of 2/3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
10 graphs per n; n up to 10^6. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-B",
 "iteration": 1,
 "kind": "er_critical",
 "seed": 21201,
 "c": 1.0,
 "lam": 0.0,
 "n_values": [
  1000,
  10000,
  100000,
  1000000
 ],
 "reps": 10,
 "h1": 0.1
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
