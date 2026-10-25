# SIM-CV-FOR-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Lazy 4-cycle: lambda2 and t_mix.

## Phase operationalization tested
FOR Convergence = convergence to stationarity (P78).

## Sources this run draws on
P78 (Wikipedia contributors, 'Markov chain mixing time', English Wikipedia, revision 1323553013 of 22 November 2025, CC BY-SA 4.0; read in full in CVB): t_mix(eps) = min{t : max_x max_A |Pr(X_t in A | X_0 = x) - pi(A)| <= eps}; changing eps < 1/2 changes t_mix by a constant factor, eps = 1/4 by convention; 'This is the sense in which Dave Bayer and Persi Diaconis (1992) proved that the number of riffle shuffles needed to mix an ordinary 52 card deck is 7'; growth 1.5 log2 n.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | a chain whose rows equal pi has d(1) = 0 |
| H1 | hypothesis | the lazy 4-cycle: lambda2 = 1/sqrt(2) within 1e-9 and t_mix(1/4) <= 5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; agent arithmetic. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-D",
 "iteration": 6,
 "kind": "mixing_time",
 "seed": 33206,
 "chains": {
  "lazyrot4": [
   [
    0.5,
    0.5,
    0,
    0
   ],
   [
    0,
    0.5,
    0.5,
    0
   ],
   [
    0,
    0,
    0.5,
    0.5
   ],
   [
    0.5,
    0,
    0,
    0.5
   ]
  ]
 },
 "eps_values": [
  0.25
 ],
 "t_max": 200,
 "hyps": [
  [
   "the lazy 4-cycle: lambda2 = 1/sqrt(2) within 1e-9 and t_mix(1/4) <= 5",
   "abs(o['chains']['lazyrot4']['lambda2'] - 0.5**0.5) < 1e-9 and o['chains']['lazyrot4']['tmix']['0.25'] <= 5"
  ]
 ]
}
```

## Command
`python sim_for.py iter-6` (run from `Formal-Sciences/simulation/`)
