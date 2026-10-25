# Convergence in the Applied Sciences — Cycle-0-Baseline (CV0)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: numerical convergence (P70); the orders are right, but P70's printed errors, trapezoid count and headline 40-62% saving do not reproduce from its own tables.

## Claims (ledger: `claims/claims.csv`)
- **CV0-APP-02** [E] Recomputing P70's Table 1 for exp(-x^2) on [0, 1] (n = subintervals) gave the expected orders (2.00, 4.00, 4.00) but different errors: trapezoid 9.59e-4 vs printed 2.13e-3 at n = 8, Simpson 1.99e-6 vs 1.47e-5, 2-point Gauss about 8e-8 vs 8.92e-6 (the record rounds to 8 decimals); the trapezoid needs 2479 evaluations, not 256, for 1e-8; the asymptotic eta is 0.400 (supported); Table 2's own counts give 25-36% savings over adaptive Simpson for f1-f4 and 32% more evaluations for f5, not 40-62% (not supported), and 18-29% over Gauss-Kronrod (f3 18%, outside the claimed 20-35%). Algorithm 1 as printed used 305 evaluations for f1 at 1e-8 (P70: 36). *Operationalization:* APP Convergence = convergence order and cost. *Sources:* SIM-CV-APP-0/iter-1#V1;SIM-CV-APP-0/iter-1#H1;SIM-CV-APP-0/iter-1#H2;SIM-CV-APP-0/iter-1#H3;SIM-CV-APP-0/iter-1#H4;SIM-CV-APP-0/iter-1#H5;SIM-CV-APP-0/iter-1#H6. *Limits:* P70 does not define n; other readings were not exhaustively tried, though no single reading fixes all three rules. 4 of 6 hypotheses not supported, 1 supported (eta), as anticipated from hand estimates (disclosed).
- **CV0-APP-01** [P] P70 proposes an adaptive quadrature that accepts the 2-point Gauss value on an interval when it agrees with Simpson's rule within a cost-aware tolerance (Algorithm 1), states an efficiency bound eta <= 2/5 (Lemma 2.6), and claims 40-62% fewer function evaluations than adaptive Simpson; its Table 2 lists evaluations to reach 1e-8 for five test functions, its Section 4.3 claims 20-35% savings over Gauss-Kronrod for f2-f5. *Operationalization:* APP Convergence = numerical convergence order. *Sources:* P70. *Limits:* Internal conflicts: Lemma 2.6's proof arithmetic gives 2, not 2/5; Appendix Theorem A.4 gives a limit of 1 for a differently defined index; Theorem 2.7 states h_max but its proof ends with h_min; f4 = x sin(10x) is called a 'boundary singularity' though smooth; Tables 1-2 report 'mean +/- std over 100 runs' for deterministic rules.

## Simulations (SIM-CV-APP-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 1/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `e34177c4` | P70's quadrature claims: do composite trapezoid, Simpson and 2-point Gauss errors for exp(-x^2) on [0, 1] at n = 8, 16, 32 subintervals match Table 1, does the trapezoid reach 1e-8 in 256 evaluations, is the asymptotic eta 2/5 (Lemma 2.6), and do Table 2's own counts give the 40-62% reduction over adaptive Simpson claimed in the abstract? | V1 Pass; H1 Not supported; H2 Not supported; H3 Not supported; H4 Not supported; H5 Supported; H6 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Adaptive hybrid quadrature and its convergence claims sourced (CV0-APP-01); Table 1 errors, the 256-evaluation trapezoid count and the 40-62% claim not reproduced; eta = 0.4 supported (CV0-APP-02).

## Unresolved
- The reading of 'n' in P70 Table 1 is unresolved; no reading reproduces all three rules.
- Algorithm 1's evaluation count (305) vs Table 2 (36) unexplained; P70's MATLAB code not run.
