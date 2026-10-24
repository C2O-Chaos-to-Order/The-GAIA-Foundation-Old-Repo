# SIM-CV-SOC-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Does a location shift (mu +-0.5) move the bound at sigma 3?

## Phase operationalization tested
SOC Convergence = collective estimation (P69).

## Sources this run draws on
P69 (Almaatouq, Rahimian, Burton & Alhajri 2022, 'The distribution of initial estimates moderates the effect of social influence on the wisdom of the crowd', Sci Rep 12:16546, PMC9530231, CC BY; read in full in CV0, SI not read): a_n(omega) = omega a_1 + (1 - omega) mean; Omega_n; Fig. 2 (n 50, theta 2, omega 1/3, log-normal): centralization helps under overestimation or large dispersion, hurts under low-dispersion underestimation.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | log-normal CDF at the truth with mu = 0 is exactly 1/2 |
| H1 | hypothesis | P69's bound never exceeds Monte Carlo Omega_n (3 SE) in any case |
| H2 | hypothesis | at sigma 3 a location shift of +-0.5 changes the bound by less than 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iter-1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds/options in CVD (stats_audit, instrument_core, levelling_voter bias_mode=selection) were smoke-tested once at trivial size (seed 99, temporary directory, nothing kept) with printed values suppressed; existing kinds were not smoke-tested. CVC results were known when these hypotheses were written (replications say so).

## Parameters
```json
{
 "sim_id": "SIM-CV-SOC-D",
 "iteration": 3,
 "kind": "crowd_bound",
 "seed": 33303,
 "theta": 2.0,
 "omega": 0.3333333333333333,
 "reps": 2000,
 "contexts": [
  [
   0.5,
   3.0
  ],
  [
   -0.5,
   3.0
  ]
 ],
 "n_values": [
  100,
  1000
 ],
 "hyps": [
  [
   "P69's bound never exceeds Monte Carlo Omega_n (3 SE) in any case",
   "all(v['bound_le_mc_plus_3se'] for v in o['by_case'].values())"
  ],
  [
   "at sigma 3 a location shift of +-0.5 changes the bound by less than 0.1",
   "all(abs(o['by_case'][f'mu0.5_s3.0_n{n}']['bound'] - o['by_case'][f'mu-0.5_s3.0_n{n}']['bound']) < 0.1 for n in [100, 1000])"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
