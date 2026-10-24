# SIM-IN-APP-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Critical slowing down before B-tipping: does lag-1 autocorrelation (detrended) rise before the fold (median Kendall tau > 0.5)?

## Phase operationalization tested
APP Insurgence = a technical system tipping into failure: by noise (N-tipping) or by a parameter crossing a fold (B-tipping) (P41).

## Sources this run draws on
P41 (Hessler & Kamps 2025, Nat Commun 16:6246, CC BY 4.0; read in full in INC): Eq. 2 N-tipping dataset (h = nu x - x^3, noise ramp, N-tipping at t = 1386.8 in one realisation), Eq. 3 fold drift h = r + x - x^3; 1996 Western Interconnection blackout: noise level rose about 2 min before the 15:42:03 line trip; CSD indicators fail for N-tipping. The least-squares estimator is the agent's, not P41's Bayesian BLE.

## Refinement from previous iteration
Iteration 4 of the x9 family for APP; follows iteration 3 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | all tip |
| H1 | hypothesis | see text |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge: smoke gave 0.84. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-C",
 "iteration": 4,
 "kind": "ntipping",
 "seed": 22404,
 "mode": "fold",
 "r0": 1.0,
 "r1": -0.6,
 "rate": 0.0005,
 "sigma": 0.05,
 "reps": 40,
 "h1_text": "median Kendall tau of AR1 > 0.5",
 "h1_expr": "r['median_tau_ar1'] is not None and r['median_tau_ar1'] > 0.5"
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
