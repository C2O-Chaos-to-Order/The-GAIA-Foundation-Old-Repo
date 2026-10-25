# SIM-CV-FOR-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Gambler's-ruin chain (two absorbing ends) and DeGroot with two stubborn agents: does the limit depend on the start, and is there no consensus?

## Phase operationalization tested
FOR Convergence = convergence to stationarity (P78).

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | gambler's-ruin chain with two absorbing ends: the limit depends on the start (max difference > 0.1) |
| H2 | hypothesis | two stubborn agents at 0 and 1: no consensus (final spread > 0.5) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; replication-extension of CVB iter-6 on a 5-state chain. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-C",
 "iteration": 6,
 "kind": "markov_converge",
 "seed": 32206,
 "T": [
  [
   1,
   0,
   0,
   0,
   0
  ],
  [
   0.5,
   0,
   0.5,
   0,
   0
  ],
  [
   0,
   0.5,
   0,
   0.5,
   0
  ],
  [
   0,
   0,
   0.5,
   0,
   0.5
  ],
  [
   0,
   0,
   0,
   0,
   1
  ]
 ],
 "V0": [
  0.2,
  0.2,
  0.2,
  0.2,
  0.2
 ],
 "V0_alt": [
  0,
  1,
  0,
  0,
  0
 ],
 "report_n": [
  10,
  100
 ],
 "n_max": 400,
 "degroot_x0": [
  0.0,
  0.3,
  0.5,
  0.7,
  1.0
 ],
 "degroot_steps": 400,
 "hyps": [
  [
   "gambler's-ruin chain with two absorbing ends: the limit depends on the start (max difference > 0.1)",
   "o['alt']['max_diff'] > 0.1"
  ],
  [
   "two stubborn agents at 0 and 1: no consensus (final spread > 0.5)",
   "o['degroot']['spread'] > 0.5"
  ]
 ]
}
```

## Command
`python sim_for.py iter-6` (run from `Formal-Sciences/simulation/`)
