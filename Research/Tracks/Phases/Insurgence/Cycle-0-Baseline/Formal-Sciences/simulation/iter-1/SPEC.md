# SIM-IN-FOR-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Emergence of the giant component in sparse Erdos-Renyi graphs (P27): reproduce P27's subcritical experiment (n 5000, c 0.8, 1000 samples, printed mean 5.45 vs theory 5.00) and the largest-component fraction against s = 1 - exp(-cs) across c = 0.5-1.5.

## Phase operationalization tested
FOR Insurgence = a phase transition: a component holding a positive fraction of nodes appears suddenly as mean degree crosses 1 (P27).

## Sources this run draws on
P27 (Chodrow, Math 168 lecture notes ch. 2 'Random Graphs: Erdős–Rényi', read in full in IN0); Eq. 2.2 and the printed experiment.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | subcritical mean within 4 SE of 1/(1-c) |
| H1 | hypothesis | P27's 5.45 within 4 SE |
| H2 | hypothesis | within 0.02 of s for c >= 1.2 |
| H3 | hypothesis | <= 0.02 at c <= 0.9, >= 0.5 at c = 1.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Finite n (50,000) blurs the transition near c = 1; component of node 0 used for the subcritical sample. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-0",
 "iteration": 1,
 "kind": "er_giant",
 "seed": 19201,
 "n_sub": 5000,
 "c_sub": 0.8,
 "reps_sub": 1000,
 "printed": 5.45,
 "c_values": [
  0.5,
  0.7,
  0.9,
  1.0,
  1.1,
  1.2,
  1.3,
  1.5
 ],
 "n": 50000,
 "reps": 10,
 "h2": 0.02,
 "h2_from": 1.2,
 "below": 0.9,
 "above": 1.5,
 "h3_lo": 0.02,
 "h3_hi": 0.5,
 "tol_se": 4
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
