# SIM-AL-HUM-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Three languages (statuses 0.6, 0.25, 0.15; shares the same) with P30's exponent 1.31: does only the dominant survive, and does the non-officialised heritage language vanish first?

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
| H1 | hypothesis | dominant share > 0.99 at the end |
| H2 | hypothesis | non-officialised language extinct before the officialised one |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; statuses are the agent's. Smoke test (seed 99, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); thresholds were not changed after it.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-C",
 "iteration": 1,
 "kind": "three_language",
 "seed": 27501,
 "s": [
  0.6,
  0.25,
  0.15
 ],
 "x0": [
  0.6,
  0.25,
  0.15
 ],
 "a": 1.31,
 "c": 1.0,
 "dt": 0.01,
 "T": 200,
 "hyps": [
  [
   "dominant share > 0.99 at the end",
   "o['x_end'][0] > 0.99"
  ],
  [
   "non-officialised language extinct before the officialised one",
   "o['t_extinct'][2] is not None and (o['t_extinct'][1] is None or o['t_extinct'][2] < o['t_extinct'][1])"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
