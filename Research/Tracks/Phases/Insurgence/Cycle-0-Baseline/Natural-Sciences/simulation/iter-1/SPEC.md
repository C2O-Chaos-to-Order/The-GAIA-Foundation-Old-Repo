# SIM-IN-NAT-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Onset of a new state at a transcritical bifurcation (P22 Eq. 8.8, dx/dt = r x - x^2): from a seed x0 = 0.001 the state rises to r only for r > 0; is the rise time the logistic value, and does onset slow near the threshold?

## Phase operationalization tested
NAT Insurgence = the rise of a new state from a small seed once a parameter crosses a threshold (exchange of stability; P22).

## Sources this run draws on
P22 (Sayama, LibreTexts section 8.2, CC BY-NC-SA 3.0; read in full in DVC): transcritical bifurcation, 'one equilibrium point passes through another, exchanging their stabilities'. Logistic solution is a direct computation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | final = max(r, 0) |
| H1 | hypothesis | rise time within 1% of logistic |
| H2 | hypothesis | t_half(0.05)/t_half(1) > 10 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic RK4, dt 0.01, 400 time units. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-NAT-0",
 "iteration": 1,
 "kind": "transcritical_onset",
 "seed": 19101,
 "r_values": [
  -0.1,
  0.05,
  0.2,
  1.0
 ],
 "x0": 0.001,
 "dt": 0.01,
 "steps": 40000,
 "tol": 1e-06,
 "h1": 0.01,
 "h2": 10
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
