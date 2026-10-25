# SIM-CV-SOC-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P69's centralization model: with n 50, omega 1/3, theta 2 and log-normal estimates a = theta exp(mu + sigma Z), is Omega > 0.5 under overestimation (mu 0.5, sigma 1) and large dispersion (mu 0, sigma 1.5) and < 0.5 under low-dispersion underestimation (mu -0.3, sigma 0.3)?

## Phase operationalization tested
SOC Convergence = convergence of individual estimates into a collective estimate, centralised or decentralised (wisdom of crowds; P69).

## Sources this run draws on
P69 (Almaatouq, Rahimian, Burton & Alhajri 2022, 'The distribution of initial estimates moderates the effect of social influence on the wisdom of the crowd', Sci Rep 12:16546, PMC9530231, CC BY; read in full in CV0, SI not read): a_n(omega) = omega a_1 + (1 - omega) mean; Omega_n; Fig. 2 (n 50, theta 2, omega 1/3, log-normal): centralization helps under overestimation or large dispersion, hurts under low-dispersion underestimation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | omega = 0 gives Omega exactly 0 |
| H1 | hypothesis | overestimation (mu 0.5, sigma 1): Omega > 0.5 |
| H2 | hypothesis | large dispersion (mu 0, sigma 1.5): Omega > 0.5 |
| H3 | hypothesis | underestimation, low dispersion (mu -0.3, sigma 0.3): Omega < 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Monte Carlo, 20,000 crowds per context (SE <= 0.0035). The parametrisation a = theta exp(mu + sigma Z) is the agent's; P69's exact F is in its SI, which was not read.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-SOC-0",
 "iteration": 1,
 "kind": "crowd_centralization",
 "seed": 29301,
 "n": 50,
 "omega": 0.3333333333333333,
 "theta": 2.0,
 "reps": 20000,
 "contexts": [
  [
   0.5,
   1.0
  ],
  [
   0.0,
   1.5
  ],
  [
   -0.3,
   0.3
  ],
  [
   0.0,
   0.3
  ]
 ],
 "hyps": [
  [
   "overestimation (mu 0.5, sigma 1): Omega > 0.5",
   "o['Omega']['mu0.5_s1.0']>0.5"
  ],
  [
   "large dispersion (mu 0, sigma 1.5): Omega > 0.5",
   "o['Omega']['mu0.0_s1.5']>0.5"
  ],
  [
   "underestimation, low dispersion (mu -0.3, sigma 0.3): Omega < 0.5",
   "o['Omega']['mu-0.3_s0.3']<0.5"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
