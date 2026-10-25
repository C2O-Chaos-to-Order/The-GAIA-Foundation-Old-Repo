# SIM-CV-FOR-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P78's growth 1.5 log2 n: for 52, 104, 208 and 416 cards, is t_mix(1/4) within 20% of 1.5 log2 n, adding at most 2 shuffles per doubling?

## Phase operationalization tested
FOR Convergence = mixing time growth.

## Sources this run draws on
P78 (Wikipedia contributors, 'Markov chain mixing time', English Wikipedia, revision 1323553013 of 22 November 2025, CC BY-SA 4.0; read in full in CVB): t_mix(eps) = min{t : max_x max_A |Pr(X_t in A | X_0 = x) - pi(A)| <= eps}; changing eps < 1/2 changes t_mix by a constant factor, eps = 1/4 by convention; 'This is the sense in which Dave Bayer and Persi Diaconis (1992) proved that the number of riffle shuffles needed to mix an ordinary 52 card deck is 7'; growth 1.5 log2 n.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | a chain whose rows equal pi has d(1) = 0 |
| H1 | hypothesis | P78's growth 1.5 log2 n: t_mix(1/4) within 20% of 1.5 log2 n for n = 52, 104, 208, 416 |
| H2 | hypothesis | each doubling of n adds at most 2 shuffles |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic exact arithmetic up to k = 20. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-B",
 "iteration": 2,
 "kind": "mixing_time",
 "seed": 31202,
 "riffle": {
  "n_cards": [
   52,
   104,
   208,
   416
  ],
  "k_max": 20
 },
 "eps_values": [
  0.25
 ],
 "hyps": [
  [
   "P78's growth 1.5 log2 n: t_mix(1/4) within 20% of 1.5 log2 n for n = 52, 104, 208, 416",
   "all(abs(v['tmix']['0.25']/v['one_point_five_log2n']-1) < 0.2 for v in o['riffle'].values())"
  ],
  [
   "each doubling of n adds at most 2 shuffles",
   "all(o['riffle'][str(2*n)]['tmix']['0.25']-o['riffle'][str(n)]['tmix']['0.25'] <= 2 for n in [52, 104, 208])"
  ]
 ]
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
