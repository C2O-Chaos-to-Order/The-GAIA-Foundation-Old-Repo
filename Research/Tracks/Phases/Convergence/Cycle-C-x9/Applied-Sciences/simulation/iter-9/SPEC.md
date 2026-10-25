# SIM-CV-APP-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of P79's ln 3 example (deterministic).

## Phase operationalization tested
APP Convergence = convergence of quadrature rules (P79).

## Sources this run draws on
P79 (Wikipedia contributors, 'Trapezoidal rule', English Wikipedia, revision fetched 2026-10-24, CC BY-SA 4.0; read in full in CVB): composite rule error E = -(b - a)^3/(12 N^2) f''(xi); asymptotic E = -(b - a)^2/(12 N^2)[f'(b) - f'(a)] + O(N^-3); concave-up integrands are overestimated; worked examples ln 3 (N = 3: 356/315, error 0.031546, 2.87148%; N = 6: 2789/2520, 8.13e-3, 0.74036%; N = 116 for 1e-4) and int_0.1^1.3 5x e^-2x dx (0.84385 vs 0.89387, error 0.05002, 5.5959%).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | trapezoidal rule exact for 2x + 1 |
| H1 | hypothesis | replication (deterministic) of P79's T_3 = 356/315 and T_6 = 2789/2520 within 1e-9 |
| H2 | hypothesis | P79's N = 116 from the bound |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pure replication. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-APP-C",
 "iteration": 9,
 "kind": "trap_error",
 "seed": 32409,
 "case": "ln3",
 "f": "1/x",
 "d1": "-1/x**2",
 "d2": "2/x**3",
 "a": 1.0,
 "b": 3.0,
 "exact": "np.log(3)",
 "N_values": [
  3,
  6
 ],
 "tol": 0.0001,
 "N_cap": 100000,
 "hyps": [
  [
   "replication (deterministic) of P79's T_3 = 356/315 and T_6 = 2789/2520 within 1e-9",
   "abs(o['rows']['3']['T']-356/315) < 1e-9 and abs(o['rows']['6']['T']-2789/2520) < 1e-9"
  ],
  [
   "P79's N = 116 from the bound",
   "o['tol']['N_bound'] == 116"
  ]
 ]
}
```

## Command
`python sim_app.py iter-9` (run from `Applied-Sciences/simulation/`)
