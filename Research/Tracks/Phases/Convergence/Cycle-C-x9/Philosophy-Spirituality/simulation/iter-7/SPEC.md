# SIM-CV-PHI-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Peirce toy (P75), rho 0.95 over 200 rounds: spread below 1% of initial?

## Phase operationalization tested
PHI Convergence = Peircean convergence of inquiry (P75).

## Sources this run draws on
P75 (Peirce, C. S. 1878, 'Illustrations of the Logic of Science II: How to Make Our Ideas Clear', Popular Science Monthly 12:286-302; public domain; Wikisource transcription, CC BY-SA; read in full in CVA): investigators of the velocity of light by different methods 'may at first obtain different results, but, as each perfects his method and his processes, the results will move steadily together toward a destined centre'; 'The opinion which is fated to be ultimately agreed to by all who investigate, is what we mean by the truth'; buried secrets.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | noise-free spread at round 0 equals max(b) - min(b) |
| H1 | hypothesis | rho 0.95: spread at round 200 below 1% of initial |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication-extension (expected to add little). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-PHI-C",
 "iteration": 7,
 "kind": "peirce_methods",
 "seed": 32607,
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
 "rho_all": 0.95,
 "noise": 0.01,
 "rounds": 200,
 "checkpoints": [
  0,
  100,
  200
 ],
 "hyps": [
  [
   "rho 0.95: spread at round 200 below 1% of initial",
   "o['rounds']['200']['spread_rel'] < 0.01*o['rounds']['0']['spread_rel']"
  ]
 ]
}
```

## Command
`python sim_phi.py iter-7` (run from `Philosophy-Spirituality/simulation/`)
