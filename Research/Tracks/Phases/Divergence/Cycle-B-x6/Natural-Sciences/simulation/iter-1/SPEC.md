# SIM-DV-NAT-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Linkage follow-up: does divergence at neutral loci decay with recombination distance from a divergently selected locus (an 'island' shape), as P01 reports divergence decaying within 1-2 cM of colour-pattern loci?

## Phase operationalization tested
NAT Divergence = locus-specific differentiation that extends to linked neutral sites and decays with recombination distance (P01, as a toy).

## Sources this run draws on
P01 (Nadeau et al. 2012; re-read in full in DVB): differentiation decays within 1-2 cM of the colour-pattern loci; 'peaks of divergence should be interpreted with caution'. The two-locus Wright-Fisher model is textbook population genetics, not a source claim.

## Refinement from previous iteration
New run family (DVA had unlinked loci only; linkage was the listed follow-up).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral mean frequency 0.5 within 4 SE |
| H1 | hypothesis | Fst(c=0) - Fst(c=0.5) > 4 SE |
| H2 | hypothesis | Fst non-increasing in c (tol 0.02) |
| H3 | hypothesis | Fst(c=0.01) below midpoint |
| R1 | reporting | Fst by c |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Haploid two-deme toy, one selected locus, each neutral locus linked to it independently (no multi-locus hitchhiking), random initial frequencies (no secondary contact). Map distance c is a per-generation recombination probability, not cM in Heliconius. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-B",
 "iteration": 1,
 "kind": "wf_linked",
 "seed": 16101,
 "m": 0.01,
 "s": 0.1,
 "N": 200,
 "reps": 60,
 "generations": 400,
 "per_c": 8,
 "c_values": [
  0.0,
  0.001,
  0.01,
  0.05,
  0.5
 ],
 "c_mid": 0.01,
 "tol_se": 4,
 "mono_tol": 0.02
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
