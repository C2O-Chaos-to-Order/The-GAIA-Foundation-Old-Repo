# SIM-CV-FOR-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P73's regular Markov chains: do the printed iterates and equilibrium of the BestTV/CableCast example reproduce, does the error shrink as |lambda2|^n, are A regular and B not, does the Wielandt matrix attain P73's bound (n - 1)^2 + 1, does a periodic chain have a solution of ET = E without converging, and does DeGroot averaging reach an E-weighted consensus?

## Phase operationalization tested
FOR Convergence = convergence of a Markov chain to its equilibrium (and, transposed, DeGroot consensus) (P73).

## Sources this run draws on
P73 (Sekhon & Bloom, '10.3: Regular Markov Chains', Applied Finite Mathematics, Mathematics LibreTexts, CC BY 4.0; read in full in CV0): regular chains, the bound m <= (n - 1)^2 + 1, BestTV/CableCast example V1-V3 and E = (3/7, 4/7), matrices A and B, Method 2 (ET = E) usable for non-regular chains.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ET = E within 1e-12; E and the rows of T sum to 1 |
| H1 | hypothesis | V1, V2, V3 equal P73's printed (.36,.64), (.408,.592), (.4224,.5776) within 1e-9 |
| H2 | hypothesis | E = (3/7, 4/7) within 1e-9 and the error after 20 steps is below 1e-9 (|lambda2| = 0.3) |
| H3 | hypothesis | A is regular (A^2 = [[.40,.60],[.24,.76]]), B is not |
| H4 | hypothesis | the Wielandt matrix attains the bound (n - 1)^2 + 1 exactly for n = 3..6 |
| H5 | hypothesis | periodic chain: ET = E is solvable (E = (.5,.5)) but V_n does not converge |
| H6 | hypothesis | DeGroot averaging reaches consensus equal to the E-weighted mean (4/7) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. The Wielandt matrix, the periodic chain and the DeGroot reading (x_{t+1} = T x_t) are standard theory added by the agent, not in P73. Foreknowledge: hand arithmetic of V1-V3 before running.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so every outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-0",
 "iteration": 1,
 "kind": "markov_converge",
 "seed": 29201,
 "T": [
  [
   0.6,
   0.4
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
  2,
  3,
  20,
  21
 ],
 "check_regular": {
  "A": [
   [
    0,
    1
   ],
   [
    0.4,
    0.6
   ]
  ],
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
  3,
  4,
  5,
  6
 ],
 "periodic": [
  [
   0,
   1
  ],
  [
   1,
   0
  ]
 ],
 "degroot_x0": [
  0.0,
  1.0
 ],
 "hyps": [
  [
   "V1, V2, V3 equal P73's printed (.36,.64), (.408,.592), (.4224,.5776) within 1e-9",
   "all(abs(a-b)<1e-9 for n,p in [('1',[.36,.64]),('2',[.408,.592]),('3',[.4224,.5776])] for a,b in zip(o['V'][n],p))"
  ],
  [
   "E = (3/7, 4/7) within 1e-9 and the error after 20 steps is below 1e-9 (|lambda2| = 0.3)",
   "abs(o['E'][0]-3/7)<1e-9 and o['err_n20']<1e-9 and abs(o['lambda2']-0.3)<1e-9"
  ],
  [
   "A is regular (A^2 = [[.40,.60],[.24,.76]]), B is not",
   "o['regular']['A']['exponent']==2 and o['regular']['B']['exponent'] is None and abs(o['powers2']['A'][1][0]-.24)<1e-12"
  ],
  [
   "the Wielandt matrix attains the bound (n - 1)^2 + 1 exactly for n = 3..6",
   "all(v['exponent']==v['bound'] for v in o['wielandt'].values())"
  ],
  [
   "periodic chain: ET = E is solvable (E = (.5,.5)) but V_n does not converge",
   "abs(o['periodic']['E'][0]-.5)<1e-9 and not o['periodic']['converges']"
  ],
  [
   "DeGroot averaging reaches consensus equal to the E-weighted mean (4/7)",
   "o['degroot']['spread']<1e-9 and abs(o['degroot']['x_end'][0]-4/7)<1e-9"
  ]
 ]
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
