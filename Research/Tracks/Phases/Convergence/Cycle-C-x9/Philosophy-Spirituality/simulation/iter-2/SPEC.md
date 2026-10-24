# SIM-CV-PHI-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Global diffusion (contact with anyone): no gradient and above-chance similarity, i.e. indistinguishable from a core by these statistics?

## Phase operationalization tested
PHI Convergence = convergence of religious traditions on a common core (P81).

## Sources this run draws on
P81 (Wikipedia contributors, 'Perennial philosophy', English Wikipedia, revision oldid 1376373344 of 23 September 2026, CC BY-SA 4.0; read in full in CVC): perennialism holds that the world's religious traditions share a single metaphysical truth or origin (Steuco: 'one principle of all things, of which there has always been one and the same knowledge among all peoples'); Huxley vs the Traditionalist School; the common-core view of mystical experience (Stace, Smith, Forman); criticism: ahistorical, overemphasises similarities, unfalsifiable (Craig Martin's 'no true Scotsman').

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | core-model mean similarity within 0.01 of p^2 + (1 - p^2)/2 |
| H1 | hypothesis | global diffusion (contact with anyone): no distance gradient either (|corr| < 0.05) - the gradient test cannot separate it from a common core |
| H2 | hypothesis | global diffusion produces above-chance similarity (> 0.55), like a core |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-C",
 "iteration": 2,
 "kind": "common_core",
 "seed": 32602,
 "T": 12,
 "F": 40,
 "reps": 200,
 "p_core": 0.5,
 "rounds": 2000,
 "long": 1.0,
 "hyps": [
  [
   "global diffusion (contact with anyone): no distance gradient either (|corr| < 0.05) - the gradient test cannot separate it from a common core",
   "abs(o['models']['diffusion']['corr_sim_dist']) < 0.05"
  ],
  [
   "global diffusion produces above-chance similarity (> 0.55), like a core",
   "o['models']['diffusion']['mean_sim'] > 0.55"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
