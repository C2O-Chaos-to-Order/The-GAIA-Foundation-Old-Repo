# SIM-IN-SOC-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Is P25's optimal threshold a property of its additive specification (SOC pass 3)? Repeat IN0's Table 2 check at another design cell (p = 0.3, r = 0.1, both on P25's grid): does every link still peak in n = [1.0, 1.1]?

## Phase operationalization tested
SOC Insurgence = the rebel-to-police ratio at which killing police is most likely (P25's fitted model).

## Sources this run draws on
P25 (read in full in IN0): Table 2 coefficients; p and r grids {0.1..0.9} and {0.1..0.4}.

## Refinement from previous iteration
Follows iter-1/2: returns to P25's fitted model to ask whether its optimal threshold depends on p and r.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | counts reproduce |
| H1 | hypothesis | all links peak in [1.0, 1.1] |
| H2 | hypothesis | fall > 0.05 from peak to 1.4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge (disclosed): because p and r enter the index additively and every link is monotone, the peak location cannot move and the linear-link drop stays 0.036, so H2 is expected not supported. The run documents this rather than testing it. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-A",
 "iteration": 3,
 "kind": "moro_arith",
 "seed": 20303,
 "grid_sizes": [
  8,
  9,
  4,
  60
 ],
 "printed": [
  17280,
  480,
  2160
 ],
 "p": 0.3,
 "r": 0.1,
 "n_lo": 0.7,
 "n_hi": 1.4,
 "band": [
  1.0,
  1.1
 ],
 "drop": 0.05,
 "coef": {
  "LPM": [
   0.432,
   -0.498,
   2.015,
   -0.079,
   0.381,
   -0.211
  ],
  "Logit": [
   -0.94,
   -4.969,
   20.12,
   -0.854,
   3.95,
   -2.181
  ],
  "Probit": [
   -0.047,
   -2.74,
   10.868,
   -1.917,
   3.87,
   -1.846
  ],
  "CLogLog": [
   -0.118,
   -2.438,
   9.154,
   -2.722,
   5.093,
   -2.44
  ]
 }
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
