# SIM-CV-FOR-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P73 says regularity is sufficient, not necessary: does P73's non-regular B still converge to a unique limit from two starts, does the Wielandt matrix attain (n - 1)^2 + 1 for n = 7-9, and do 2000 random primitive 0/1 patterns per size (n = 3-7) stay within (and for n >= 5 below) the bound?

## Phase operationalization tested
FOR Convergence = convergence of Markov chains; the primitivity bound.

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | P73's B is not regular, yet both starts converge to the same limit (1, 0) (regularity sufficient, not necessary) |
| H2 | hypothesis | the Wielandt matrix attains (n - 1)^2 + 1 for n = 7, 8, 9 |
| H3 | hypothesis | no random primitive pattern (n = 3-7, 2000 each) exceeds the bound |
| H4 | hypothesis | for n >= 5 no random pattern reaches the bound (it is attained only by special matrices) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Random patterns have density 0.3 (agent's choice); the Wielandt matrix is standard theory, not in P73. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-A",
 "iteration": 2,
 "kind": "markov_converge",
 "seed": 30202,
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
 "V0_alt": [
  0.9,
  0.1
 ],
 "report_n": [
  1,
  50
 ],
 "n_max": 200,
 "check_regular": {
  "B": [
   [
    1,
    0
   ],
   [
    0.3,
    0.7
   ]
  ]
 },
 "wielandt_n": [
  7,
  8,
  9
 ],
 "random_primitive": {
  "n": [
   3,
   4,
   5,
   6,
   7
  ],
  "count": 2000,
  "density": 0.3
 },
 "hyps": [
  [
   "P73's B is not regular, yet both starts converge to the same limit (1, 0) (regularity sufficient, not necessary)",
   "o['regular']['B']['exponent'] is None and o['alt']['max_diff'] < 1e-9 and abs(o['E'][0]-1) < 1e-9"
  ],
  [
   "the Wielandt matrix attains (n - 1)^2 + 1 for n = 7, 8, 9",
   "all(v['exponent'] == v['bound'] for v in o['wielandt'].values())"
  ],
  [
   "no random primitive pattern (n = 3-7, 2000 each) exceeds the bound",
   "all(v['max_exponent'] <= v['bound'] for v in o['random_primitive'].values())"
  ],
  [
   "for n >= 5 no random pattern reaches the bound (it is attained only by special matrices)",
   "all(v['max_exponent'] < v['bound'] for k, v in o['random_primitive'].items() if int(k) >= 5)"
  ]
 ]
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
