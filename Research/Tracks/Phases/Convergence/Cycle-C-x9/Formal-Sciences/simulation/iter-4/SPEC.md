# SIM-CV-FOR-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Odd lazy cycles (9, 17, 33): does t_mix(1/4) grow like n^2, and is the relaxation time within a factor 2 of t_mix?

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
| H1 | hypothesis | odd lazy cycles: t_mix(1/4) ratio per near-doubling (9 -> 17 -> 33) in [3, 5] |
| H2 | hypothesis | relaxation time t_rel = 1/(1 - lambda2) within a factor 2 of t_mix(1/4) for each cycle |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Exact matrix powers. Relaxation time is not in P78 (agent's addition). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-C",
 "iteration": 4,
 "kind": "mixing_time",
 "seed": 32204,
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
   "odd lazy cycles: t_mix(1/4) ratio per near-doubling (9 -> 17 -> 33) in [3, 5]",
   "all(3 <= o['chains'][b]['tmix']['0.25']/o['chains'][a]['tmix']['0.25'] <= 5 for a, b in [('cycle9', 'cycle17'), ('cycle17', 'cycle33')])"
  ],
  [
   "relaxation time t_rel = 1/(1 - lambda2) within a factor 2 of t_mix(1/4) for each cycle",
   "all(0.5 <= v['tmix']['0.25']/v['t_rel'] <= 2 for v in o['chains'].values())"
  ]
 ]
}
```

## Command
`python sim_for.py iter-4` (run from `Formal-Sciences/simulation/`)
