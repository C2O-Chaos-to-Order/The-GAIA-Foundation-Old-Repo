# SIM-CV-PHI-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same toy with a bias of 1% shared by every method: do the investigators still converge (spread < 1% of initial) - but on a value 1% from the truth?

## Phase operationalization tested
PHI Convergence = agreement without truth (a shared systematic error).

## Sources this run draws on
P75 (Peirce, C. S. 1878, 'Illustrations of the Logic of Science II: How to Make Our Ideas Clear', Popular Science Monthly 12:286-302; public domain; Wikisource transcription, CC BY-SA; read in full in CVA): investigators of the velocity of light by different methods 'may at first obtain different results, but, as each perfects his method and his processes, the results will move steadily together toward a destined centre'; 'The opinion which is fated to be ultimately agreed to by all who investigate, is what we mean by the truth'; buried secrets. P72 (Capps, 'The Pragmatic Theory of Truth', Stanford Encyclopedia of Philosophy, first published 21 Mar 2019, substantive revision 22 May 2023; read in full in CV0): Peirce 1878 'The opinion which is fated to be ultimately agreed to by all who investigate'; Peirce 1901 'ideal limit towards which endless investigation would tend'; 'buried secrets' objection; Misak 'never in a position to judge'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | noise-free spread at round 0 equals max(b) - min(b) |
| H1 | hypothesis | with a bias shared by all methods the spread still falls below 1% of its initial value |
| H2 | hypothesis | the investigators agree on a value 0.01 from the truth (within 1e-4) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; shows that convergence of opinion is not by itself evidence of truth, which Peirce's 'destined centre' presupposes. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-A",
 "iteration": 3,
 "kind": "peirce_methods",
 "seed": 30603,
 "truth": 299792.458,
 "biases": [
  -0.03,
  -0.02,
  -0.01,
  0.005,
  0.01,
  0.015,
  0.02,
  0.025,
  0.03
 ],
 "rho_all": 0.9,
 "noise": 0.01,
 "rounds": 100,
 "checkpoints": [
  0,
  10,
  50,
  100
 ],
 "common_bias": 0.01,
 "hyps": [
  [
   "with a bias shared by all methods the spread still falls below 1% of its initial value",
   "o['rounds']['100']['spread_rel'] < 0.01*o['rounds']['0']['spread_rel']"
  ],
  [
   "the investigators agree on a value 0.01 from the truth (within 1e-4)",
   "abs(o['rounds']['100']['mean_err_rel']-0.01) < 1e-4"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
