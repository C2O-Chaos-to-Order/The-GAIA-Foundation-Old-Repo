# SIM-IN-FOR-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Size of the largest component at the critical point c = 1 (FOR pass 2): does it grow like n^(2/3) for n = 1,000, 10,000, 100,000?

## Phase operationalization tested
FOR Insurgence = the critical window of the giant-component transition.

## Sources this run draws on
P27 (read in full in IN0) gives the phase transition at c = 1 but not the n^(2/3) law; that law is a standard random-graph result stated here from the agent's knowledge (not from a source read in this track).

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
20 graphs per n; three n values; finite-size corrections not modelled. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-A",
 "iteration": 1,
 "kind": "er_critical",
 "seed": 20201,
 "c": 1.0,
 "n_values": [
  1000,
  10000,
  100000
 ],
 "reps": 20,
 "h1": 0.1
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
