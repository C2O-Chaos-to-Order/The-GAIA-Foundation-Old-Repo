# SIM-CV-PHI-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Common core vs local diffusion (12 traditions on a ring, 40 features): does a common core leave no similarity-distance gradient while local contact leaves one?

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
| H1 | hypothesis | common core: similarity shows no gradient with contact distance (|corr| < 0.05) |
| H2 | hypothesis | local diffusion: similarity falls with contact distance (corr < -0.2) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy of P81's inference (agent's); fidelity 0.5, 2000 copying events. Neither P81 nor its critics propose this model. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-C",
 "iteration": 1,
 "kind": "common_core",
 "seed": 32601,
 "T": 12,
 "F": 40,
 "reps": 200,
 "p_core": 0.5,
 "rounds": 2000,
 "long": 0.0,
 "hyps": [
  [
   "common core: similarity shows no gradient with contact distance (|corr| < 0.05)",
   "abs(o['models']['core']['corr_sim_dist']) < 0.05"
  ],
  [
   "local diffusion: similarity falls with contact distance (corr < -0.2)",
   "o['models']['diffusion']['corr_sim_dist'] < -0.2"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
