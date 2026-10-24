# SIM-CV-FOR-D - iteration 11 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of CVC's odd cycles.

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
| H1 | hypothesis | replication of CVC odd cycles: t_mix(1/4) = 8, 28, 103 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pure replication. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-D",
 "iteration": 11,
 "kind": "mixing_time",
 "seed": 33211,
 "chains": {
  "cycle9": {
   "lazy_cycle": 9
  },
  "cycle17": {
   "lazy_cycle": 17
  },
  "cycle33": {
   "lazy_cycle": 33
  }
 },
 "eps_values": [
  0.25
 ],
 "t_max": 40000,
 "hyps": [
  [
   "replication of CVC odd cycles: t_mix(1/4) = 8, 28, 103",
   "[o['chains'][k]['tmix']['0.25'] for k in ['cycle9', 'cycle17', 'cycle33']] == [8, 28, 103]"
  ]
 ]
}
```

## Command
`python sim_for.py iter-11` (run from `Formal-Sciences/simulation/`)
