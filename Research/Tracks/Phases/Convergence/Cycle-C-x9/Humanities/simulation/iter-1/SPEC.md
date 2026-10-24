# SIM-CV-HUM-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Dialect-levelling toy, neutral copying (N 200): does a variant fix with probability equal to its initial share, so a majority is not deterministic?

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
| H1 | hypothesis | neutral copying: P(variant fixes) within 4 SE of its initial share for every x0 |
| H2 | hypothesis | neutral copying is not majority-deterministic: a 70% variant fixes with probability < 0.9 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy (agent's); Wright-Fisher copying is the agent's choice, not P82's. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-C",
 "iteration": 1,
 "kind": "levelling_voter",
 "seed": 32501,
 "N": 200,
 "gens_max": 4000,
 "reps": 4000,
 "x0_values": [
  0.07,
  0.3,
  0.5,
  0.7
 ],
 "c": 1.0,
 "hyps": [
  [
   "neutral copying: P(variant fixes) within 4 SE of its initial share for every x0",
   "all(abs(v['p_fix'] - float(k)) < 4 * (float(k) * (1 - float(k)) / 4000) ** 0.5 for k, v in o['by_x0'].items())"
  ],
  [
   "neutral copying is not majority-deterministic: a 70% variant fixes with probability < 0.9",
   "o['by_x0']['0.7']['p_fix'] < 0.9"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
