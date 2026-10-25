# SIM-AS-SOC-D - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Rank toy: does upgrading change the rank correlation?

## Phase operationalization tested
SOC Ascendence = upward and total intergenerational mobility (P87; P93 for women's educational mobility). ASD adds P96's US rank-based relative and absolute mobility.

## Sources this run draws on
P96 (Song, Massey, Rolf, Ferrie, Rothbaum & Xie 2020, 'Long-term decline in intergenerational mobility in the United States since the 1850s', PNAS 117:251-258, PMC6955340, CC BY-NC-ND; read in full in ASD, SI Appendix not read): father-son occupational rank-rank correlations rising from about 0.17 (1830 cohort) to 0.27 (1900) and 0.32 (1980); absolute upward mobility (>= 7.5 points on a 0-100 rank scale of 70 occupations) rising before 1900 and falling after 1940; the role of the farm-to-factory shift.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | independent latent statuses give |rank correlation| < 0.01 |
| H1 | hypothesis | upgrading by 0.3 SD changes the rank-rank correlation by less than 0.02 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-D",
 "iteration": 5,
 "kind": "rank_mobility",
 "seed": 38305,
 "n": 200000,
 "rho_values": [
  0.32
 ],
 "upgrade_values": [
  0.0,
  0.3
 ],
 "hyps": [
  [
   "upgrading by 0.3 SD changes the rank-rank correlation by less than 0.02",
   "abs(o['cells']['rho0.32_up0.3']['rank_corr'] - o['cells']['rho0.32_up0.0']['rank_corr']) < 0.02"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
