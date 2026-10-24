# SIM-AL-FOR-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Other payoffs (b 0, c 1, d 2) and N 20, 200, 2000: same three questions.

## Phase operationalization tested
FOR Allegiance = how large a basin a conforming convention needs to take over (P58).

## Sources this run draws on
P58 (Ohtsuki, Bordalo & Nowak 2007, 'The one-third law of evolutionary dynamics', J Theor Biol; Harvard DASH, read in full in ALB): Moran fixation probability with f = 1 - w + w F, Eq. 4 finite-N weak-selection condition (N - 2)a + (2N - 1)b > (N + 1)c + (2N - 4)d, Discussion: the required basin of attraction grows from 2/3 (Nw << 1) toward 1 (large Nw).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | Nw < 0.1: exact critical x* within 0.01 of P58 Eq. 4 |
| H2 | hypothesis | N 2000, w 1e-5: x* within 0.01 of 1/3 |
| H3 | hypothesis | N 2000: x* falls as w grows |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-FOR-C",
 "iteration": 2,
 "kind": "moran_game",
 "seed": 27202,
 "b": 0.0,
 "c": 1.0,
 "d": 2.0,
 "N_values": [
  20,
  200,
  2000
 ],
 "w_values": [
  1e-05,
  0.01,
  0.1
 ],
 "hyps": [
  [
   "Nw < 0.1: exact critical x* within 0.01 of P58 Eq. 4",
   "all(abs(v['x_crit'] - v['x_eq4']) < 0.01 for v in o.values() if v['Nw'] < 0.1)"
  ],
  [
   "N 2000, w 1e-5: x* within 0.01 of 1/3",
   "abs(o['N2000_w1e-05']['x_crit'] - 1/3) < 0.01"
  ],
  [
   "N 2000: x* falls as w grows",
   "o['N2000_w1e-05']['x_crit'] > o['N2000_w0.01']['x_crit'] > o['N2000_w0.1']['x_crit']"
  ]
 ]
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
