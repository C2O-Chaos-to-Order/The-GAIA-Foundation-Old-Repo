# SIM-CV-PHI-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same toy with one method that never improves: does the spread stay >= 0.027 and the mean >= 0.003 from the truth?

## Phase operationalization tested
PHI Convergence = convergence of inquiry; a failure mode.

## Sources this run draws on
P75 (Peirce, C. S. 1878, 'Illustrations of the Logic of Science II: How to Make Our Ideas Clear', Popular Science Monthly 12:286-302; public domain; Wikisource transcription, CC BY-SA; read in full in CVA): investigators of the velocity of light by different methods 'may at first obtain different results, but, as each perfects his method and his processes, the results will move steadily together toward a destined centre'; 'The opinion which is fated to be ultimately agreed to by all who investigate, is what we mean by the truth'; buried secrets.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | noise-free spread at round 0 equals max(b) - min(b) |
| H1 | hypothesis | one never-improving method (bias 0.03) keeps the spread at round 100 >= 0.027 |
| H2 | hypothesis | the mean stays at least 0.003 from the truth |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-A",
 "iteration": 2,
 "kind": "peirce_methods",
 "seed": 30602,
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
 "rho": [
  0.9,
  0.9,
  0.9,
  0.9,
  0.9,
  0.9,
  0.9,
  0.9,
  1.0
 ],
 "noise": 0.01,
 "rounds": 100,
 "checkpoints": [
  0,
  10,
  50,
  100
 ],
 "hyps": [
  [
   "one never-improving method (bias 0.03) keeps the spread at round 100 >= 0.027",
   "o['rounds']['100']['spread_rel'] >= 0.027"
  ],
  [
   "the mean stays at least 0.003 from the truth",
   "o['rounds']['100']['mean_err_rel'] >= 0.003"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
