# SIM-DV-NAT-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Slow ramp with stronger noise (sigma 0.2): does the loop narrow or vanish?

## Phase operationalization tested
NAT Divergence = a state jumping to a different branch at a fold (catastrophe) and not returning when the parameter is reversed (hysteresis; P22).

## Sources this run draws on
P22 (Sayama, 'Bifurcations in 1-D Continuous-Time Models', LibreTexts, CC BY-NC-SA 3.0; read in full in DVC): Eq. 8.14 dx/dt = r + x - x^3, hysteresis with thresholds stated as 'r ≈ 0.4' and 'r ≈ -0.4'; exact saddle-node value 2/(3 sqrt 3) = 0.3849 is a direct computation.

## Refinement from previous iteration
Only sigma and seed change from iteration 4.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | analytic root count 3 inside |r| < 0.3849, 1 outside |
| V2 | validation | every replicate jumps up and down |
| H1 | hypothesis | mean up-jump within 0.02 of 0.3849 |
| H2 | hypothesis | hysteresis width > 0.5 |
| R1 | reporting | jump points |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One-variable normal form; a ramp of finite speed delays jumps (slow-passage effect), so the 'threshold' measured depends on ramp rate and noise. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-C",
 "iteration": 5,
 "kind": "hysteresis_sweep",
 "seed": 17105,
 "dt": 0.01,
 "rate": 0.001,
 "sigma": 0.2,
 "reps": 40,
 "h1": 0.02,
 "h2": 0.5
}
```

## Command
`python sim_nat.py iter-5` (run from `Natural-Sciences/simulation/`)
