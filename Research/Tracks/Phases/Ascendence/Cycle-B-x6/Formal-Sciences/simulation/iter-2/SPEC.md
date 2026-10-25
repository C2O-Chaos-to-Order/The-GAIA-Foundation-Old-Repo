# SIM-AS-FOR-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Plain gradient steps near 2/lambda_max (0.001997): do eta 0.0015 and 0.0019 converge and 0.0021 fail from three starts?

## Phase operationalization tested
FOR Ascendence = steepest ascent / descent (P86), continuous and discrete. Step-size limit is standard theory added by the agent.

## Sources this run draws on
P86 (Wensing & Slotine 2020, 'Beyond convexity - Contraction and global convergence of gradient descent', PLoS One, PMC7402485, CC BY; read in full in AS0): natural gradient as 'the direction of steepest ascent on the manifold'; Example 3 (Rosenbrock, metric M, h(x) = -2[x1 - 1, x1^2 - 2x1 + x2], contraction rate 2, coordinates z1 = 10x1^2 - 10x2, z2 = x1 - 1); Example 5 (f = x1^2 + x2^2 + x1^2 x2^2, metric printed in a garbled layout in the extracted text).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | the z-map (1 - 2 dt) shrinks |z| by 0.5 per step at dt 0.25 |
| H1 | hypothesis | plain steps converge from all starts at eta 0.0015 and 0.0019 (below 2/lambda_max = 0.001997) |
| H2 | hypothesis | eta 0.0021 converges from no start |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; 100,000-step cap. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-FOR-B",
 "iteration": 2,
 "kind": "grad_steps",
 "seed": 36202,
 "mode": "gd",
 "eta_values": [
  0.0015,
  0.0019,
  0.0021
 ],
 "starts": [
  [
   -1.5,
   2.0
  ],
  [
   2.0,
   -1.0
  ],
  [
   0.0,
   0.0
  ]
 ],
 "k_max": 100000,
 "tol": 1e-06,
 "hyps": [
  [
   "plain steps converge from all starts at eta 0.0015 and 0.0019 (below 2/lambda_max = 0.001997)",
   "all(v['conv'] for d in ['0.0015', '0.0019'] for v in o['results'][d].values())"
  ],
  [
   "eta 0.0021 converges from no start",
   "not any(v['conv'] for v in o['results']['0.0021'].values())"
  ]
 ]
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
