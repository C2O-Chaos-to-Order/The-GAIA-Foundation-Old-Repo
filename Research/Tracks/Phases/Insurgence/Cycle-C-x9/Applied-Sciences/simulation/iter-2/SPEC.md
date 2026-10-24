# SIM-IN-APP-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Warning signs before N-tipping (P41: CSD indicators fail; noise level is what changes): rolling standard deviation, lag-1 autocorrelation, drift slope and noise level up to the switch.

## Phase operationalization tested
APP Insurgence = a technical system tipping into failure: by noise (N-tipping) or by a parameter crossing a fold (B-tipping) (P41).

## Sources this run draws on
P41 (Hessler & Kamps 2025, Nat Commun 16:6246, CC BY 4.0; read in full in INC): Eq. 2 N-tipping dataset (h = nu x - x^3, noise ramp, N-tipping at t = 1386.8 in one realisation), Eq. 3 fold drift h = r + x - x^3; 1996 Western Interconnection blackout: noise level rose about 2 min before the 15:42:03 line trip; CSD indicators fail for N-tipping. The least-squares estimator is the agent's, not P41's Bayesian BLE.

## Refinement from previous iteration
Iteration 2 of the x9 family for APP; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | windows available |
| H1 | hypothesis | SD rises |
| H2 | hypothesis | AR1 flat |
| H3 | hypothesis | estimator accurate |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
40 realisations; windows 2,000 points shifted by 100 (P41). Foreknowledge: a 4-run smoke gave AR1 trend 0.37. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-C",
 "iteration": 2,
 "kind": "ntipping",
 "seed": 22402,
 "mode": "indicators",
 "reps": 40
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
