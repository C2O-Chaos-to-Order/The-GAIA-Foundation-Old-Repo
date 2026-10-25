# SIM-TR-SOC-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P99 Stimulation-sized effect with quadrupled groups: power?

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
| H1 | hypothesis | Stimulation-sized effect with quadrupled groups: power above 0.80 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
4000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-TR-SOC-D",
 "iteration": 11,
 "kind": "anova_power_mc",
 "seed": 43311,
 "ns": [
  4604,
  1524,
  492
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
   "Stimulation-sized effect with quadrupled groups: power above 0.80",
   "o['power_mc'] > 0.80"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-11` (run from `Social-Sciences/simulation/`)
