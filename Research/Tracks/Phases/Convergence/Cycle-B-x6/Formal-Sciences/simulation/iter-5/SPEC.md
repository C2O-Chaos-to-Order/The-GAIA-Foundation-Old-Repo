# SIM-CV-FOR-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P73's chains, larger sizes: does the Wielandt matrix attain (n - 1)^2 + 1 for n = 10, 11, and do 1000 random primitive patterns per size (n = 8-10) stay below it?

## Phase operationalization tested
FOR Convergence = convergence of Markov chains; primitivity bound.

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | the Wielandt matrix attains (n - 1)^2 + 1 for n = 10, 11 |
| H2 | hypothesis | no random primitive pattern (n = 8-10, 1000 each) reaches the bound |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Density 0.3 (agent's). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-B",
 "iteration": 5,
 "kind": "markov_converge",
 "seed": 31205,
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
  10,
  11
 ],
 "random_primitive": {
  "n": [
   8,
   9,
   10
  ],
  "count": 1000,
  "density": 0.3
 },
 "hyps": [
  [
   "the Wielandt matrix attains (n - 1)^2 + 1 for n = 10, 11",
   "all(v['exponent'] == v['bound'] for v in o['wielandt'].values())"
  ],
  [
   "no random primitive pattern (n = 8-10, 1000 each) reaches the bound",
   "all(v['max_exponent'] < v['bound'] for v in o['random_primitive'].values())"
  ]
 ]
}
```

## Command
`python sim_for.py iter-5` (run from `Formal-Sciences/simulation/`)
