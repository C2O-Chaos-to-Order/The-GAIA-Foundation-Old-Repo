# SIM-CV-PHI-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Two methods at opposite extremes that never improve: is the spread kept >= 0.055 and do their errors cancel in the mean (within 1e-3)?

## Phase operationalization tested
PHI Convergence = a failure mode with symmetric stuck methods.

## Sources this run draws on
P75 (Peirce, C. S. 1878, 'Illustrations of the Logic of Science II: How to Make Our Ideas Clear', Popular Science Monthly 12:286-302; public domain; Wikisource transcription, CC BY-SA; read in full in CVA): investigators of the velocity of light by different methods 'may at first obtain different results, but, as each perfects his method and his processes, the results will move steadily together toward a destined centre'; 'The opinion which is fated to be ultimately agreed to by all who investigate, is what we mean by the truth'; buried secrets.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | noise-free spread at round 0 equals max(b) - min(b) |
| H1 | hypothesis | two never-improving methods (bias -0.03 and 0.03) keep the spread >= 0.055 |
| H2 | hypothesis | their errors cancel: mean within 1e-3 of the truth |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; noise of stuck methods also does not shrink. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-B",
 "iteration": 3,
 "kind": "peirce_methods",
 "seed": 31603,
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
 "rho": [
  1.0,
  0.9,
  0.9,
  0.9,
  0.9,
  0.9,
  0.9,
  0.9,
  1.0
 ],
 "hyps": [
  [
   "two never-improving methods (bias -0.03 and 0.03) keep the spread >= 0.055",
   "o['rounds']['100']['spread_rel'] >= 0.055"
  ],
  [
   "their errors cancel: mean within 1e-3 of the truth",
   "o['rounds']['100']['mean_err_rel'] < 1e-3"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
