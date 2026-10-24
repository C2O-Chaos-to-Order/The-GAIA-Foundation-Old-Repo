# SIM-AL-HUM-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Heritage majority (shares 0.3, 0.5, 0.2; statuses 0.6, 0.25, 0.15), a 1.31: does the heritage majority win on frequency?

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
| H1 | hypothesis | officialised heritage language wins (share > 0.99) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; statuses are the agent's.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-D",
 "iteration": 8,
 "kind": "three_language",
 "seed": 28508,
 "s": [
  0.6,
  0.25,
  0.15
 ],
 "x0": [
  0.3,
  0.5,
  0.2
 ],
 "a": 1.31,
 "c": 1.0,
 "dt": 0.01,
 "T": 400,
 "hyps": [
  [
   "officialised heritage language wins (share > 0.99)",
   "o['x_end'][1] > 0.99"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-8` (run from `Humanities/simulation/`)
