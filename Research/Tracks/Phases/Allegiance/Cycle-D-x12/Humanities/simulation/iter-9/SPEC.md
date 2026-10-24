# SIM-AL-HUM-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Equal statuses and shares, a 1.31: does the symmetric state persist (all within 0.01 of 1/3)?

## Phase operationalization tested
HUM Allegiance = loyalty to a heritage language in P60's three-party game.

## Sources this run draws on
P60 (Song 2025, scoping review of Chinese heritage-language maintenance, Front Psychol, PMC12968234, CC BY; read in full in ALC): proposes 'a three-party game' of a dominant language, an officialised heritage language and a non-officialised heritage language, noting it 'requires primary empirical data'. P30 (read in full in INA): Abrams-Strogatz exponent form.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | all shares within 0.01 of 1/3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; statuses are the agent's.Unstable symmetric equilibrium; numerical persistence expected.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-D",
 "iteration": 9,
 "kind": "three_language",
 "seed": 28509,
 "s": [
  0.3333333333333333,
  0.3333333333333333,
  0.3333333333333333
 ],
 "x0": [
  0.3333333333333333,
  0.3333333333333333,
  0.3333333333333333
 ],
 "a": 1.31,
 "c": 1.0,
 "dt": 0.01,
 "T": 200,
 "hyps": [
  [
   "all shares within 0.01 of 1/3",
   "all(abs(v - 1/3) < 0.01 for v in o['x_end'])"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-9` (run from `Humanities/simulation/`)
