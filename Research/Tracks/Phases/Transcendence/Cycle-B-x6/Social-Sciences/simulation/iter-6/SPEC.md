# SIM-TR-SOC-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Power at P99's group sizes for the Stimulation effect: as P99's significance pattern implies?

## Phase operationalization tested
SOC Transcendence = self-transcendence values and prosocial orientation (P99).

## Sources this run draws on
P99 (Nezlek 2024, values and social value orientation, PLoS One, PMC11602047, CC BY; read in full in TR0): 1655 participants; SVO prosocial 1151, individualist 381, competitor 123; Portrait Values Questionnaire (self-transcendence = universalism + benevolence); Table 2 means; Table 3 group means, F(2, n - 3), eta^2, planned comparisons; participant flows in Method and Results.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Monte Carlo rejection rate within 4 SE of the noncentral-F value |
| H1 | hypothesis | Stimulation (eta^2 0.00186): power at alpha .05 < 0.50 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Unit SD, Table 3 mean pattern, 4000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-B",
 "iteration": 6,
 "kind": "anova_power_mc",
 "seed": 41306,
 "ns": [
  1151,
  381,
  123
 ],
 "eta2": 0.00186,
 "pattern": [
  -0.243,
  -0.171,
  -0.134
 ],
 "alpha": 0.05,
 "reps": 4000,
 "hyps": [
  [
   "Stimulation (eta^2 0.00186): power at alpha .05 < 0.50",
   "o['power_mc'] < 0.50"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
