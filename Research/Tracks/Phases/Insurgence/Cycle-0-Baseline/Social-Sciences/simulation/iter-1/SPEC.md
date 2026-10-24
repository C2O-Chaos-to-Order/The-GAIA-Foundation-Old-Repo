# SIM-IN-SOC-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Check P25's printed design counts (17,280 runs; 480 per (p, r) cell; 2,160 per n) and its statement that the fitted probability of killing a policeman k(0.9, 0.3, n) peaks for n in [1.0, 1.1] and then 'decreases markedly', using P25's Table 2 coefficients for all four link functions.

## Phase operationalization tested
SOC Insurgence = an organised uprising that starts when rebel numbers pass a threshold n relative to government forces (P25, agent-based model of revolutions).

## Sources this run draws on
P25 (Moro 2016, PLoS ONE 11:e0154175, CC BY; read in full in IN0): Methods, Table 2, Fig 5 text.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | counts reproduce |
| H1 | hypothesis | all links peak in [1.0, 1.1] |
| H2 | hypothesis | k falls by > 0.05 from the peak to n = 1.4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Uses the printed (rounded) coefficients; checks P25's fitted model, not its NetLogo simulations; 'markedly' read as a drop > 0.05 in probability (agent's threshold). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-0",
 "iteration": 1,
 "kind": "moro_arith",
 "seed": 19301,
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
 "p": 0.9,
 "r": 0.3,
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
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
