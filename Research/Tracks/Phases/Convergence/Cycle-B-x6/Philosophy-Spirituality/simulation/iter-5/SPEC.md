# SIM-CV-PHI-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Three-fold larger initial biases (+-9%): spread < 1% of initial at round 100?

## Phase operationalization tested
PHI Convergence = convergence of inquiry.

## Sources this run draws on
P75 (Peirce, C. S. 1878, 'Illustrations of the Logic of Science II: How to Make Our Ideas Clear', Popular Science Monthly 12:286-302; public domain; Wikisource transcription, CC BY-SA; read in full in CVA): investigators of the velocity of light by different methods 'may at first obtain different results, but, as each perfects his method and his processes, the results will move steadily together toward a destined centre'; 'The opinion which is fated to be ultimately agreed to by all who investigate, is what we mean by the truth'; buried secrets.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | noise-free spread at round 0 equals max(b) - min(b) |
| H1 | hypothesis | the investigators' spread at round 100 is below 1% of the round-0 spread |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; relative criterion, so expected to add little. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-B",
 "iteration": 5,
 "kind": "peirce_methods",
 "seed": 31605,
 "truth": 299792.458,
 "biases": [
  -0.09,
  -0.06,
  -0.03,
  0.015,
  0.03,
  0.045,
  0.06,
  0.07500000000000001,
  0.09
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
 "hyps": [
  [
   "the investigators' spread at round 100 is below 1% of the round-0 spread",
   "o['rounds']['100']['spread_rel'] < 0.01*o['rounds']['0']['spread_rel']"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-5` (run from `Philosophy-Spirituality/simulation/`)
