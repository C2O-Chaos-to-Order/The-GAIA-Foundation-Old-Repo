# SIM-CV-HUM-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Corrected prestige design (bias as selection, b 0.05) with conformity: is a 30% standard variant still lost, and does a 45% one win?

## Phase operationalization tested
HUM Convergence = convergence of dialects by levelling (P82).

## Sources this run draws on
P82 (Wikipedia contributors, 'Dialect levelling', English Wikipedia, revision oldid 1381046553 of 19 October 2026, CC BY-SA 4.0; read in full in CVC): levelling = reduction of differences between dialects through contact; Hinskens: 14 of 21 features lost distinctions, wider-distributed features less likely to level, levelling not necessarily toward the standard; New Zealand English formed 1840-1880, Australians 7% of immigrants before 1881, Trudgill's deterministic 'majority forms win'; Taiwan Mandarin tonal levelling in about 30 years.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral copying is a martingale (3 generations, 4 SE) |
| H1 | hypothesis | corrected prestige design (selection b 0.05) with conformity c 2: a 30% standard variant is still lost with probability >= 0.9 (Hinskens: levelling need not go toward the standard) |
| H2 | hypothesis | a 45% standard variant wins more often than not |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Corrects CVC iter-5's design error (constant bias made loss impossible). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-D",
 "iteration": 1,
 "kind": "levelling_voter",
 "seed": 33501,
 "N": 1000,
 "gens_max": 500,
 "reps": 2000,
 "x0_values": [
  0.3,
  0.45
 ],
 "c": 2.0,
 "b": 0.05,
 "bias_mode": "selection",
 "hyps": [
  [
   "corrected prestige design (selection b 0.05) with conformity c 2: a 30% standard variant is still lost with probability >= 0.9 (Hinskens: levelling need not go toward the standard)",
   "o['by_x0']['0.3']['p_lost'] >= 0.9"
  ],
  [
   "a 45% standard variant wins more often than not",
   "o['by_x0']['0.45']['p_fix'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
