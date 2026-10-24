# SIM-AL-FOR-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Nw sweep at N 100 (w 0.001, 0.003, 0.01, 0.03): is x* monotone decreasing in Nw?

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
| H1 | hypothesis | x* strictly decreasing in w |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-FOR-C",
 "iteration": 5,
 "kind": "moran_game",
 "seed": 27205,
 "b": 1.0,
 "c": 2.0,
 "d": 3.0,
 "N_values": [
  100
 ],
 "w_values": [
  0.001,
  0.003,
  0.01,
  0.03
 ],
 "hyps": [
  [
   "x* strictly decreasing in w",
   "o['N100_w0.001']['x_crit'] > o['N100_w0.003']['x_crit'] > o['N100_w0.01']['x_crit'] > o['N100_w0.03']['x_crit']"
  ]
 ]
}
```

## Command
`python sim_for.py iter-5` (run from `Formal-Sciences/simulation/`)
