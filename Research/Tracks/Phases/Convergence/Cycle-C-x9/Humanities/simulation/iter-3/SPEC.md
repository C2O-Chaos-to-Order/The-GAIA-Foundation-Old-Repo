# SIM-CV-HUM-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Larger community (N 10000): majority fixation >= 0.99 and mean time <= 8 generations?

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
| H1 | hypothesis | larger community (N 10000): majority variants fix with probability >= 0.99 |
| H2 | hypothesis | larger community (N 10000): mean levelling time from 70% at most 8 generations |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-C",
 "iteration": 3,
 "kind": "levelling_voter",
 "seed": 32503,
 "N": 10000,
 "gens_max": 500,
 "reps": 1000,
 "x0_values": [
  0.55,
  0.7
 ],
 "c": 2.0,
 "hyps": [
  [
   "larger community (N 10000): majority variants fix with probability >= 0.99",
   "all(v['p_fix'] >= 0.99 for v in o['by_x0'].values())"
  ],
  [
   "larger community (N 10000): mean levelling time from 70% at most 8 generations",
   "o['by_x0']['0.7']['mean_gens'] <= 8"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
