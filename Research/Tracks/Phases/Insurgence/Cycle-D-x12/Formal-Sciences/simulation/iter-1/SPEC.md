# SIM-IN-FOR-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P45's percolation probabilities (n = 100): near 0 at q = 0.55, about 70% at 0.60, near 1 at 0.65?

## Phase operationalization tested
FOR Insurgence = a connected path appearing abruptly across a medium as the density of open sites passes a critical value (percolation, P44/P45).

## Sources this run draws on
P44/P45 (Downey, Think Complexity sections 7.3 Percolation and 7.4 Phase change, Engineering LibreTexts, CC BY-NC-SA 3.0; both read in full in IND): percolation CA, percolating cluster; 'When p=0.55 , the probability of a percolating cluster is near 0. At p=0.60 , it is about 70%, and at p=0.65 it is near 1'; random-walk estimate of the critical value about 0.59, not depending on n.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | monotone |
| H1 | hypothesis | P45's three values |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
1,000 arrays per q. Foreknowledge: a 100-array smoke gave 0.02, 0.66, 1.0. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-D",
 "iteration": 1,
 "kind": "percolation",
 "seed": 23201,
 "mode": "prob",
 "n": 100,
 "reps": 1000,
 "q_values": [
  0.55,
  0.6,
  0.65
 ],
 "h1_text": "below 0.1 at 0.55, within 0.15 of 0.70 at 0.60, above 0.9 at 0.65",
 "h1_expr": "o[0] < 0.1 and abs(o[1] - 0.7) <= 0.15 and o[2] > 0.9"
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
