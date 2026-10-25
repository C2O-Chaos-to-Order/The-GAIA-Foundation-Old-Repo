# SIM-CV-SOC-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Thin spread (sigma 0.25): is the bound trivial (< 0.01) for n >= 100?

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
| H1 | hypothesis | P69's lower bound never exceeds the Monte Carlo Omega_n (by more than 3 SE) in any case |
| H2 | hypothesis | thin spread (sigma 0.25): the bound is trivial (< 0.01) for n >= 100 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iter-1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kinds in CVC (kuramoto_lyap, kuramoto_fss, crowd_bound, trap_simpson, levelling_voter, common_core) were smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before the SPECs; printed values were suppressed except one kuramoto_lyap smoke (N = 3 and 4, K = 1, 3 settings, T 400) whose maxima (both slightly negative) were seen (disclosed). Thresholds were not informed by smoke values. Existing kinds were not smoke-tested.

## Parameters
```json
{
 "sim_id": "SIM-CV-SOC-C",
 "iteration": 4,
 "kind": "crowd_bound",
 "seed": 32304,
 "theta": 2.0,
 "omega": 0.3333333333333333,
 "reps": 20000,
 "contexts": [
  [
   0.0,
   0.25
  ]
 ],
 "n_values": [
  10,
  100,
  1000
 ],
 "hyps": [
  [
   "P69's lower bound never exceeds the Monte Carlo Omega_n (by more than 3 SE) in any case",
   "all(v['bound_le_mc_plus_3se'] for v in o['by_case'].values())"
  ],
  [
   "thin spread (sigma 0.25): the bound is trivial (< 0.01) for n >= 100",
   "all(o['by_case'][f'mu0.0_s0.25_n{n}']['bound'] < 0.01 for n in [100, 1000])"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-4` (run from `Social-Sciences/simulation/`)
