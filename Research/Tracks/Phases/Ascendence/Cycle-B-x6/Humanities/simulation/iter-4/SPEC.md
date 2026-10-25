# SIM-AS-HUM-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Neutral copying plus selection b 0.1 from 15%: fixation > 50%?

## Phase operationalization tested
HUM Ascendence = rising intonation (uptalk; P89, P92) and the spread of a minority rising variant.

## Sources this run draws on
P89 (Nance et al. 2022, rising intonation in Liverpool English, Lang Speech, PMC9669732, CC BY-NC; read in full in AS0): 17 Liverpool and 15 Manchester speakers; L* L-H% = Knowles' 'rise', L* H-H% = 'rise-plateau'; Tables 1-2 LRT chi-squares; rise-plateau-slump counts by gender; F0 excursion 18 Hz, chi2(1) 2.82, p 0.09; Lawton's 1349% population increase 1773-1871.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral drift over 3 generations keeps the mean share within 4 SE |
| H1 | hypothesis | neutral copying plus selection b 0.1: a 15% variant fixes in more than 50% of runs |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-HUM-B",
 "iteration": 4,
 "kind": "levelling_voter",
 "seed": 36504,
 "gens_max": 2000,
 "reps": 4000,
 "N": 200,
 "c": 1.0,
 "b": 0.1,
 "bias_mode": "selection",
 "x0_values": [
  0.15
 ],
 "hyps": [
  [
   "neutral copying plus selection b 0.1: a 15% variant fixes in more than 50% of runs",
   "o['by_x0']['0.15']['p_fix'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-4` (run from `Humanities/simulation/`)
