# SIM-DV-APP-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P17's error scaling: forward Euler global RMS error on exponential decay is O(h) (slope one on log-log).

## Phase operationalization tested
APP Divergence = discretisation error growth (the computed solution departing from the analytic one) and its scaling.

## Sources this run draws on
P17 (read in full): RMS error e ~ O(h), fig. 2.4 slope one.

## Refinement from previous iteration
New run family.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | iteration = closed form (rtol 1e-10) |
| H1 | hypothesis | slope within 0.1 of 1 |
| R1 | reporting | errors, slope |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One linear ODE; a = -0.5 is the agent's choice (P17 shows several alpha). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-B",
 "iteration": 5,
 "kind": "euler_order",
 "seed": 16405,
 "a": -0.5,
 "y0": 1.0,
 "T": 10,
 "h_values": [
  0.1,
  0.05,
  0.02,
  0.01,
  0.005
 ],
 "h1": 0.1
}
```

## Command
`python sim_app.py iter-5` (run from `Applied-Sciences/simulation/`)
