# SIM-AS-HUM-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P89's minority-variant argument as a toy: under majority-amplifying copying (c 1.5; a stand-in for Trudgill's majority rule) in a community of 200 speakers, is a variant at 15% (P89's Irish share of Liverpool in 1871) or 30% lost in at least 99% / 95% of runs?

## Phase operationalization tested
HUM Ascendence = rising intonation as a minority variant selected in new-dialect formation (P89).

## Sources this run draws on
P89 (Nance et al. 2022, rising intonation in Liverpool English, Lang Speech, PMC9669732, CC BY-NC; read in full in AS0): 17 Liverpool and 15 Manchester speakers; L* L-H% = Knowles' 'rise', L* H-H% = 'rise-plateau'; Tables 1-2 LRT chi-squares; rise-plateau-slump counts by gender; F0 excursion 18 Hz, chi2(1) 2.82, p 0.09; Lawton's 1349% population increase 1773-1871.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral drift over 3 generations keeps the mean share within 4 SE |
| H1 | hypothesis | majority-amplifying copying (c 1.5): a variant starting at 15% (P89: Irish share of Liverpool 1871) is lost in at least 99% of runs |
| H2 | hypothesis | c 1.5: a 30% variant is also lost in at least 95% of runs |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's toy (levelling_voter from CVD); N, c and the 15% start are the agent's choices. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-HUM-A",
 "iteration": 1,
 "kind": "levelling_voter",
 "seed": 35501,
 "N": 200,
 "gens_max": 2000,
 "reps": 4000,
 "c": 1.5,
 "b": 0.0,
 "x0_values": [
  0.15,
  0.3,
  0.5
 ],
 "hyps": [
  [
   "majority-amplifying copying (c 1.5): a variant starting at 15% (P89: Irish share of Liverpool 1871) is lost in at least 99% of runs",
   "o['by_x0']['0.15']['p_lost'] >= 0.99"
  ],
  [
   "c 1.5: a 30% variant is also lost in at least 95% of runs",
   "o['by_x0']['0.3']['p_lost'] >= 0.95"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
