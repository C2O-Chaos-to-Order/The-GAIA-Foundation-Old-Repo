# SIM-CV-HUM-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Conformist copying (c 2, N 1000): Trudgill's majority determinism (>= 0.95 either way), the 7% variant, and levelling within 2 generations?

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
| H1 | hypothesis | conformist copying (c = 2): majority variants (x0 >= 0.55) fix with probability >= 0.95 and minority variants (x0 <= 0.45) are lost with probability >= 0.95 (Trudgill's majority determinism) |
| H2 | hypothesis | the 7% variant (cf. P82's Australians in pre-1881 New Zealand) never fixes |
| H3 | hypothesis | levelling from a 70% majority completes within 2 generations on average (cf. P82's New Zealand 1840-1880) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Agent arithmetic before the run: the deterministic map from 0.7 needs ~4-5 generations to reach fixation in N = 1000, so H3 was expected not supported. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-HUM-C",
 "iteration": 2,
 "kind": "levelling_voter",
 "seed": 32502,
 "N": 1000,
 "gens_max": 500,
 "reps": 2000,
 "x0_values": [
  0.07,
  0.3,
  0.45,
  0.55,
  0.7,
  0.93
 ],
 "c": 2.0,
 "hyps": [
  [
   "conformist copying (c = 2): majority variants (x0 >= 0.55) fix with probability >= 0.95 and minority variants (x0 <= 0.45) are lost with probability >= 0.95 (Trudgill's majority determinism)",
   "all((v['p_fix'] >= 0.95) if float(k) > 0.5 else (v['p_lost'] >= 0.95) for k, v in o['by_x0'].items())"
  ],
  [
   "the 7% variant (cf. P82's Australians in pre-1881 New Zealand) never fixes",
   "o['by_x0']['0.07']['p_fix'] == 0"
  ],
  [
   "levelling from a 70% majority completes within 2 generations on average (cf. P82's New Zealand 1840-1880)",
   "o['by_x0']['0.7']['mean_gens'] <= 2"
  ]
 ]
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
