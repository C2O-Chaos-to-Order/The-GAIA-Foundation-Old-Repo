# SIM-AS-APP-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P91's P1 values compare the same subjects at two altitudes: do they equal an unpaired chi-square (suggesting a test that ignores pairing)?

## Phase operationalization tested
APP Ascendence = ascent rate / protocol and AMS (P88, P91).

## Sources this run draws on
P91 (Zhao, Zhao, Ma, Liu, Chen & Sha 2024, 'Dynamics in the prevalence and clinical manifestations of acute mountain sickness of different ascent protocols during high altitudes exposure', Front Public Health 12:1472935, PMC11617577, CC BY; read in full in ASA): 770 young lowland men, fast (air, n 424) vs slow (bus over 2 days, n 346) ascent to 3650 m, then 4400 m (717 reached); Tables 1-2 counts and p-values; adjusted OR fast vs slow 1.52 at 3650 m and 0.67 at 4400 m; propensity-matched 272 + 272 (Table 5).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P91's within-cohort P1 values (same subjects at two altitudes) equal an unpaired 2x2 chi-square within 0.005 (0.594, 1.000) |
| H2 | hypothesis | slow cohort 72 vs 121: unpaired p below 0.001 as printed |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Paired data cannot be re-tested without the paired table (not printed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-APP-B",
 "iteration": 1,
 "kind": "arith_audit",
 "seed": 36401,
 "items": [
  {
   "name": "P1_fast_old_unpaired",
   "expr": "chi2_2x2(103, 169, 97, 175)",
   "printed": 0.594
  },
  {
   "name": "P1_fast_new_unpaired",
   "expr": "chi2_2x2(88, 184, 88, 184)",
   "printed": 1.0
  },
  {
   "name": "P2_slow_old_unpaired",
   "expr": "chi2_2x2(72, 200, 121, 151)",
   "printed": 0.001
  }
 ],
 "hyps": [
  [
   "P91's within-cohort P1 values (same subjects at two altitudes) equal an unpaired 2x2 chi-square within 0.005 (0.594, 1.000)",
   "abs(o['items']['P1_fast_old_unpaired']['diff']) <= 0.005 and abs(o['items']['P1_fast_new_unpaired']['diff']) <= 0.005"
  ],
  [
   "slow cohort 72 vs 121: unpaired p below 0.001 as printed",
   "o['items']['P2_slow_old_unpaired']['value'] < 0.001"
  ]
 ]
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
