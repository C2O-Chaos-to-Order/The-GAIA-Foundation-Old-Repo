# SIM-CV-FOR-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
DeGroot with two stubborn agents holding 0.9 and 0.3: is there no consensus, and does the chain's limit depend on the start?

## Phase operationalization tested
FOR Convergence = consensus and its failure.

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | two stubborn agents with different opinions: no consensus (final spread > 0.5) |
| H2 | hypothesis | the chain's limit depends on the start (max difference between starts > 0.1) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; network is the agent's. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-B",
 "iteration": 6,
 "kind": "markov_converge",
 "seed": 31206,
 "T": [
  [
   1,
   0,
   0,
   0
  ],
  [
   0.3,
   0.4,
   0.3,
   0
  ],
  [
   0,
   0.3,
   0.4,
   0.3
  ],
  [
   0,
   0,
   0,
   1
  ]
 ],
 "V0": [
  0.25,
  0.25,
  0.25,
  0.25
 ],
 "V0_alt": [
  0,
  0,
  0,
  1
 ],
 "report_n": [
  10,
  100
 ],
 "n_max": 400,
 "degroot_x0": [
  0.9,
  0.1,
  0.5,
  0.3
 ],
 "degroot_steps": 400,
 "hyps": [
  [
   "two stubborn agents with different opinions: no consensus (final spread > 0.5)",
   "o['degroot']['spread'] > 0.5"
  ],
  [
   "the chain's limit depends on the start (max difference between starts > 0.1)",
   "o['alt']['max_diff'] > 0.1"
  ]
 ]
}
```

## Command
`python sim_for.py iter-6` (run from `Formal-Sciences/simulation/`)
