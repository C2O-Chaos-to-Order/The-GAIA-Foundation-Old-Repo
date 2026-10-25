# SIM-AS-SOC-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P87's growth statements: does 'about 1.5 percentage points per decade' follow from Table 1, did growth slow after 1974, and are both unidiff parameters more than 3 SE from zero?

## Phase operationalization tested
SOC Ascendence = growth of upward and total mobility (P87).

## Sources this run draws on
P87 (Paterson et al. 2025, social mobility in Scotland 1901-2001, Br J Sociol, PMC11890437, CC BY; read in full in AS0): Table 1 mobile/up/down; Table 2 origin and destination distributions (weighted in 1901 and 2001; sample sizes unweighted) and dissimilarity indices 0.12/0.16/0.23; Tables 3-4 outflow/inflow 1901 with sample sizes; Table 5 deviances 30,992/6865/1302 and printed reductions 78.8/95.8; text 'reduced by 79%', '17%', '46%', 'Fully 57%'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | chi-square survival at 3.8415 (1 df) = 0.05 |
| H1 | hypothesis | P87's 'about 1.5 percentage points per decade' follows from Table 1 (52 to 67 over 100 years) within 0.05 |
| H2 | hypothesis | growth was slower after 1974 than before (per-decade rates from Table 1), as P87's 'possibly slowing to 1 point per decade' says |
| H3 | hypothesis | both unidiff parameters are more than 3 standard errors from zero |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Arithmetic on printed rounded numbers; 1901 to 1974 taken as 7.3 decades and 1974 to 2001 as 2.7. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-A",
 "iteration": 2,
 "kind": "arith_audit",
 "seed": 35302,
 "items": [
  {
   "name": "growth_1901_2001_per_decade",
   "expr": "(67-52)/10",
   "printed": 1.5
  },
  {
   "name": "growth_1901_1974_per_decade",
   "expr": "(64-52)/7.3"
  },
  {
   "name": "growth_1974_2001_per_decade",
   "expr": "(67-64)/2.7",
   "printed": 1.0
  },
  {
   "name": "unidiff_1974_z",
   "expr": "0.24/0.073"
  },
  {
   "name": "unidiff_2001_z",
   "expr": "0.48/0.086"
  },
  {
   "name": "unidiff_diff_z_indep",
   "expr": "(0.48-0.24)/sqrt(0.073**2+0.086**2)"
  },
  {
   "name": "T6_inheritance_odds_agri_self",
   "expr": "exp(2.79)"
  },
  {
   "name": "T6_inheritance_odds_semi",
   "expr": "exp(0.32)"
  },
  {
   "name": "constant_fluidity_dev_p",
   "expr": "chi2_sf(241, 32)"
  },
  {
   "name": "unidiff_dev_p",
   "expr": "chi2_sf(183, 30)"
  }
 ],
 "hyps": [
  [
   "P87's 'about 1.5 percentage points per decade' follows from Table 1 (52 to 67 over 100 years) within 0.05",
   "abs(o['items']['growth_1901_2001_per_decade']['diff']) <= 0.05"
  ],
  [
   "growth was slower after 1974 than before (per-decade rates from Table 1), as P87's 'possibly slowing to 1 point per decade' says",
   "o['items']['growth_1974_2001_per_decade']['value'] < o['items']['growth_1901_1974_per_decade']['value']"
  ],
  [
   "both unidiff parameters are more than 3 standard errors from zero",
   "o['items']['unidiff_1974_z']['value'] > 3 and o['items']['unidiff_2001_z']['value'] > 3"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
