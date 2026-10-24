# SIM-CV-SOC-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Mean-unbiased (mu -0.5, sigma 1) by group size: is Omega < 0.5 for n = 5-200?

## Phase operationalization tested
SOC Convergence = collective estimation.

## Sources this run draws on
P69 (Almaatouq, Rahimian, Burton & Alhajri 2022, 'The distribution of initial estimates moderates the effect of social influence on the wisdom of the crowd', Sci Rep 12:16546, PMC9530231, CC BY; read in full in CV0, SI not read): a_n(omega) = omega a_1 + (1 - omega) mean; Omega_n; Fig. 2 (n 50, theta 2, omega 1/3, log-normal): centralization helps under overestimation or large dispersion, hurts under low-dispersion underestimation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | omega = 0 gives Omega exactly 0 |
| H1 | hypothesis | mean-unbiased (mu -0.5, sigma 1): Omega < 0.5 for n = 5, 10, 50, 200 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Monte Carlo. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-SOC-B",
 "iteration": 4,
 "kind": "crowd_centralization",
 "seed": 31304,
 "n": 50,
 "omega": 0.3333333333333333,
 "theta": 2.0,
 "reps": 20000,
 "contexts": [
  [
   -0.5,
   1.0
  ]
 ],
 "n_values": [
  5,
  10,
  50,
  200
 ],
 "hyps": [
  [
   "mean-unbiased (mu -0.5, sigma 1): Omega < 0.5 for n = 5, 10, 50, 200",
   "all(v < 0.5 for v in o['by_n'].values())"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-4` (run from `Social-Sciences/simulation/`)
