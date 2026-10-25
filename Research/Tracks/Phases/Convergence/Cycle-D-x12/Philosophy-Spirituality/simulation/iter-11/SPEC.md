# SIM-CV-PHI-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Half long-range contact.

## Phase operationalization tested
PHI Convergence = convergence of traditions on a common core of mystical experience (P81, P83, P84).

## Sources this run draws on
P81 (Wikipedia contributors, 'Perennial philosophy', English Wikipedia, revision oldid 1376373344 of 23 September 2026, CC BY-SA 4.0; read in full in CVC): perennialism holds that the world's religious traditions share a single metaphysical truth or origin (Steuco: 'one principle of all things, of which there has always been one and the same knowledge among all peoples'); Huxley vs the Traditionalist School; the common-core view of mystical experience (Stace, Smith, Forman); criticism: ahistorical, overemphasises similarities, unfalsifiable (Craig Martin's 'no true Scotsman').

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | core-model mean similarity within 0.01 of p^2 + (1 - p^2)/2 |
| H1 | hypothesis | half long-range contact: diffusion gradient weaker than -0.5 (corr > -0.5) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-D",
 "iteration": 11,
 "kind": "common_core",
 "seed": 33611,
 "T": 12,
 "F": 40,
 "reps": 200,
 "p_core": 0.8,
 "rounds": 2000,
 "long": 0.5,
 "hyps": [
  [
   "half long-range contact: diffusion gradient weaker than -0.5 (corr > -0.5)",
   "o['models']['diffusion']['corr_sim_dist'] > -0.5"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-11` (run from `Philosophy-Spirituality/simulation/`)
