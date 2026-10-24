# SIM-IN-FOR-D - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Larger arrays (n = 400): does the 50% crossing fall between 0.58 and 0.60 (the literature value 0.5927 is the agent's knowledge; seen only in search snippets, not read)?

## Phase operationalization tested
FOR Insurgence = a connected path appearing abruptly across a medium as the density of open sites passes a critical value (percolation, P44/P45).

## Sources this run draws on
P44/P45 (Downey, Think Complexity sections 7.3 Percolation and 7.4 Phase change, Engineering LibreTexts, CC BY-NC-SA 3.0; both read in full in IND): percolation CA, percolating cluster; 'When p=0.55 , the probability of a percolating cluster is near 0. At p=0.60 , it is about 70%, and at p=0.65 it is near 1'; random-walk estimate of the critical value about 0.59, not depending on n.

## Refinement from previous iteration
Iteration 4 of the x12 family for FOR; follows iteration 3 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | monotone |
| H1 | hypothesis | crossing in (0.58, 0.60) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
200 arrays per q. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-D",
 "iteration": 4,
 "kind": "percolation",
 "seed": 23204,
 "mode": "prob",
 "n": 400,
 "reps": 200,
 "q_values": [
  0.58,
  0.59,
  0.6
 ],
 "h1_text": "probability below 0.5 at 0.58 and above 0.5 at 0.60",
 "h1_expr": "o[0] < 0.5 < o[2]"
}
```

## Command
`python sim_for.py iter-4` (run from `Formal-Sciences/simulation/`)
