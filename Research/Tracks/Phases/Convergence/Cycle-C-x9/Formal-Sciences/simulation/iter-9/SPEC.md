# SIM-CV-FOR-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of CVB iter-1 (52 cards): t_mix(1/4) = 8, d(7) = 0.334?

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
| H1 | hypothesis | replication of CVB iter-1 (deterministic): t_mix(1/4) = 8 and d(7) = 0.334 (within 5e-4) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; pure replication. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-C",
 "iteration": 9,
 "kind": "mixing_time",
 "seed": 32209,
 "riffle": {
  "n_cards": [
   52
  ],
  "k_max": 12
 },
 "eps_values": [
  0.25,
  0.5,
  0.1
 ],
 "hyps": [
  [
   "replication of CVB iter-1 (deterministic): t_mix(1/4) = 8 and d(7) = 0.334 (within 5e-4)",
   "o['riffle']['52']['tmix']['0.25'] == 8 and abs(o['riffle']['52']['d']['7'] - 0.334) < 5e-4"
  ]
 ]
}
```

## Command
`python sim_for.py iter-9` (run from `Formal-Sciences/simulation/`)
