# SIM-AS-HUM-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Can selection for a minority variant (b 0.3, as for functional load; P89 citing Hickey) overcome majority-amplifying copying (c 1.5) from 15% and 30%?

## Phase operationalization tested
HUM Ascendence = selection of a minority variant (P89).

## Sources this run draws on
P89 (Nance et al. 2022, rising intonation in Liverpool English, Lang Speech, PMC9669732, CC BY-NC; read in full in AS0): 17 Liverpool and 15 Manchester speakers; L* L-H% = Knowles' 'rise', L* H-H% = 'rise-plateau'; Tables 1-2 LRT chi-squares; rise-plateau-slump counts by gender; F0 excursion 18 Hz, chi2(1) 2.82, p 0.09; Lawton's 1349% population increase 1773-1871.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral drift over 3 generations keeps the mean share within 4 SE |
| H1 | hypothesis | with selection b 0.3 for the variant (e.g. functional load; P89 citing Hickey), a 15% variant fixes in more than half of runs despite c 1.5 |
| H2 | hypothesis | selection b 0.3: a 30% variant fixes in more than 90% of runs |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's toy; selection form q' = q + b q (1 - q). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-HUM-A",
 "iteration": 2,
 "kind": "levelling_voter",
 "seed": 35502,
 "N": 200,
 "gens_max": 2000,
 "reps": 4000,
 "c": 1.5,
 "b": 0.3,
 "bias_mode": "selection",
 "x0_values": [
  0.15,
  0.3
 ],
 "hyps": [
  [
   "with selection b 0.3 for the variant (e.g. functional load; P89 citing Hickey), a 15% variant fixes in more than half of runs despite c 1.5",
   "o['by_x0']['0.15']['p_fix'] > 0.5"
  ],
  [
   "selection b 0.3: a 30% variant fixes in more than 90% of runs",
   "o['by_x0']['0.3']['p_fix'] > 0.9"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
