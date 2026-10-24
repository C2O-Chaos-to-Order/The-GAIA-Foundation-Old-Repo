# SIM-SOUL-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K16 reports that 34% of 85 terminally ill patients had end-of-life experiences, but only 41% were followed until death. How much could incomplete follow-up understate prevalence by death?

## Sources this run draws on
K16 (da Silva et al. 2026, BMC Palliative Care): 85 patients, 34% ELEs, median 29.5 days first ELE to death, 41% followed to death. True prevalence (0.5) and survival (mean 30 days) are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | full follow-up recovers truth |
| H1 | hypothesis | observed < 0.8 x true |
| R1 | reporting | Wilson CI for 29/85 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Exponential survival and lead times; discharged patients observed for a uniform fraction of remaining time. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-B",
 "iteration": 4,
 "kind": "truncated_prevalence",
 "seed": 214,
 "N": 85,
 "p_true": 0.5,
 "median_lead_days": 29.5,
 "mean_survival_days": 30,
 "f_death": 0.41,
 "observed_k": 29,
 "reps": 4000
}
```

## Command
`python sim_soul.py iter-4` (run from `Soul/simulation/`)
