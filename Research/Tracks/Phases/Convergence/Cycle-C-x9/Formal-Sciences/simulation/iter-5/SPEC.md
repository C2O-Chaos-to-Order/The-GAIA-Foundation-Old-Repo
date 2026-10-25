# SIM-CV-FOR-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Wielandt bound for n = 12, 13 and random primitive patterns (n = 11, 12): replication-extension of CVB iter-5.

## Phase operationalization tested
FOR Convergence = convergence to stationarity (P78). Primitivity exponent (P73 context).

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | the Wielandt matrix attains (n - 1)^2 + 1 for n = 12, 13 |
| H2 | hypothesis | no random primitive pattern (n = 11, 12; 500 each) reaches the bound |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic Wielandt; random patterns seeded. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-C",
 "iteration": 5,
 "kind": "markov_converge",
 "seed": 32205,
 "T": [
  [
   1,
   0
  ],
  [
   0.3,
   0.7
  ]
 ],
 "V0": [
  0.2,
  0.8
 ],
 "report_n": [
  1,
  50
 ],
 "n_max": 200,
 "wielandt_n": [
  12,
  13
 ],
 "random_primitive": {
  "n": [
   11,
   12
  ],
  "count": 500,
  "density": 0.3
 },
 "hyps": [
  [
   "the Wielandt matrix attains (n - 1)^2 + 1 for n = 12, 13",
   "all(v['exponent'] == v['bound'] for v in o['wielandt'].values())"
  ],
  [
   "no random primitive pattern (n = 11, 12; 500 each) reaches the bound",
   "all(v['max_exponent'] < v['bound'] for v in o['random_primitive'].values())"
  ]
 ]
}
```

## Command
`python sim_for.py iter-5` (run from `Formal-Sciences/simulation/`)
