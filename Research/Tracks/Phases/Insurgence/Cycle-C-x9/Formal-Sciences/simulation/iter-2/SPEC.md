# SIM-IN-FOR-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Critical window at lambda = +2 (P36: Theta(n^(2/3)) for any fixed lambda).

## Phase operationalization tested
FOR Insurgence = critical window, slightly supercritical.

## Sources this run draws on
P36 (Goldschmidt, Warwick lecture 3, 27 April 2009, slides PDF; read in full in INB): in the critical window p = 1/n + lambda n^(-4/3) the largest components are of size Theta(n^(2/3)). P27 for the transition.

## Refinement from previous iteration
Iteration 2 of the x9 family for FOR; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | fraction falls with n |
| H1 | hypothesis | slope within 0.1 of 2/3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-C",
 "iteration": 2,
 "kind": "er_critical",
 "seed": 22202,
 "c": 1.0,
 "lam": 2.0,
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
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
