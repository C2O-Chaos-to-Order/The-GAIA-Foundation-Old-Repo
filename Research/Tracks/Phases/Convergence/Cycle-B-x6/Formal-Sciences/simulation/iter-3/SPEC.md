# SIM-CV-FOR-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Mixing of the lazy random walk on n-cycles (n = 8-64): does t_mix(1/4) grow like n^2, and is P78's 'constant factor' between eps levels within ceil(log2(1/eps))?

## Phase operationalization tested
FOR Convergence = mixing time.

## Sources this run draws on
P78 (Wikipedia contributors, 'Markov chain mixing time', English Wikipedia, revision 1323553013 of 22 November 2025, CC BY-SA 4.0; read in full in CVB): t_mix(eps) = min{t : max_x max_A |Pr(X_t in A | X_0 = x) - pi(A)| <= eps}; changing eps < 1/2 changes t_mix by a constant factor, eps = 1/4 by convention; 'This is the sense in which Dave Bayer and Persi Diaconis (1992) proved that the number of riffle shuffles needed to mix an ordinary 52 card deck is 7'; growth 1.5 log2 n.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | a chain whose rows equal pi has d(1) = 0 |
| H1 | hypothesis | lazy cycle walk: t_mix(1/4) grows like n^2 (ratio per doubling in [3, 5]) |
| H2 | hypothesis | P78's 'constant factor': t_mix(eps) <= ceil(log2(1/eps)) t_mix(1/4) for every chain and eps |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic matrix powers. The ceil(log2(1/eps)) factor comes from submultiplicativity (standard theory, not in P78). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-CV-FOR-B",
 "iteration": 3,
 "kind": "mixing_time",
 "seed": 31203,
 "chains": {
  "cycle8": {
   "lazy_cycle": 8
  },
  "cycle16": {
   "lazy_cycle": 16
  },
  "cycle32": {
   "lazy_cycle": 32
  },
  "cycle64": {
   "lazy_cycle": 64
  }
 },
 "eps_values": [
  0.25,
  0.125,
  0.0625,
  0.01
 ],
 "t_max": 40000,
 "hyps": [
  [
   "lazy cycle walk: t_mix(1/4) grows like n^2 (ratio per doubling in [3, 5])",
   "all(3 <= o['chains'][f'cycle{2*n}']['tmix']['0.25']/o['chains'][f'cycle{n}']['tmix']['0.25'] <= 5 for n in [8, 16, 32])"
  ],
  [
   "P78's 'constant factor': t_mix(eps) <= ceil(log2(1/eps)) t_mix(1/4) for every chain and eps",
   "all(v['tmix'][e] <= -(-__import__('math').log2(1/float(e))//1) * v['tmix']['0.25'] for v in o['chains'].values() for e in v['tmix'])"
  ]
 ]
}
```

## Command
`python sim_for.py iter-3` (run from `Formal-Sciences/simulation/`)
