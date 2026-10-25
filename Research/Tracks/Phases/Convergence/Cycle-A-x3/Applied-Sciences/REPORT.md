# Convergence in the Applied Sciences — Cycle-A-x3 (CVA)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P70's evaluation counts for f2-f4 do not reproduce; Algorithm 1 as printed is reliable but far costlier than Table 2.

## Claims (ledger: `claims/claims.csv`)
- **CVA-APP-02** [E] Recomputing P70's Table 1 for exp(-x^2) on [0, 1] (n = subintervals) gave the expected orders (2.00, 4.00, 4.00) but different errors: trapezoid 9.59e-4 vs printed 2.13e-3 at n = 8, Simpson 1.99e-6 vs 1.47e-5, 2-point Gauss about 8e-8 vs 8.92e-6 (the record rounds to 8 decimals); the trapezoid needs 2479 evaluations, not 256, for 1e-8; the asymptotic eta is 0.400 (supported); Table 2's own counts give 25-36% savings over adaptive Simpson for f1-f4 and 32% more evaluations for f5, not 40-62% (not supported), and 18-29% over Gauss-Kronrod (f3 18%, outside the claimed 20-35%). Algorithm 1 as printed used 305 evaluations for f1 at 1e-8 (P70: 36). *Operationalization:* APP Convergence = convergence order and cost. *Sources:* SIM-CV-APP-0/iter-1#V1;SIM-CV-APP-0/iter-1#H1;SIM-CV-APP-0/iter-1#H2;SIM-CV-APP-0/iter-1#H3;SIM-CV-APP-0/iter-1#H4;SIM-CV-APP-0/iter-1#H5;SIM-CV-APP-0/iter-1#H6. *Limits:* P70 does not define n; other readings were not exhaustively tried, though no single reading fixes all three rules. 4 of 6 hypotheses not supported, 1 supported (eta), as anticipated from hand estimates (disclosed).
- **CVA-APP-03** [E] P70's Table 2 counts were not supported for f2-f4: composite trapezoid needs 11,665, 15,703 and 8,631 nodes for 1e-8 (printed 2048, 4096, 1024), Simpson 363, 165 and 155 (printed 512, 1024, 256), and Algorithm 1 as printed needs 4,455, 5,695 and 1,965 evaluations (printed hybrid 247, 523, 128), though it does reach 1e-8 (for f4 also 1e-6 and 1e-10). Only the accuracy hypotheses were supported (4 of 13). *Operationalization:* APP Convergence = cost of reaching a tolerance. *Sources:* SIM-CV-APP-A/iter-1#V1;SIM-CV-APP-A/iter-1#H1;SIM-CV-APP-A/iter-1#H2;SIM-CV-APP-A/iter-1#H3;SIM-CV-APP-A/iter-1#H4;SIM-CV-APP-A/iter-2#V1;SIM-CV-APP-A/iter-2#H1;SIM-CV-APP-A/iter-2#H2;SIM-CV-APP-A/iter-2#H3;SIM-CV-APP-A/iter-2#H4;SIM-CV-APP-A/iter-3#V1;SIM-CV-APP-A/iter-3#H1;SIM-CV-APP-A/iter-3#H2;SIM-CV-APP-A/iter-3#H3;SIM-CV-APP-A/iter-3#H4;SIM-CV-APP-A/iter-3#H5. *Limits:* 'Evaluations' for composite rules read as nodes; P70's MATLAB code was not run, so a different implementation could explain the gap; the acceptance rule sigma eps h / L is applied as printed.
- **CVA-APP-01** [P] P70 proposes an adaptive quadrature that accepts the 2-point Gauss value on an interval when it agrees with Simpson's rule within a cost-aware tolerance (Algorithm 1), states an efficiency bound eta <= 2/5 (Lemma 2.6), and claims 40-62% fewer function evaluations than adaptive Simpson; its Table 2 lists evaluations to reach 1e-8 for five test functions, its Section 4.3 claims 20-35% savings over Gauss-Kronrod for f2-f5. *Operationalization:* APP Convergence = numerical convergence order. *Sources:* P70. *Limits:* Internal conflicts: Lemma 2.6's proof arithmetic gives 2, not 2/5; Appendix Theorem A.4 gives a limit of 1 for a differently defined index; Theorem 2.7 states h_max but its proof ends with h_min; f4 = x sin(10x) is called a 'boundary singularity' though smooth; Tables 1-2 report 'mean +/- std over 100 runs' for deterministic rules.

## Simulations (SIM-CV-APP-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 4/13)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `60a099b6` | P70 Table 2 for f2 (sin(20 x^2)): do composite trapezoid and Simpson need P70's printed evaluations (within 10%) to reach 1e-8, and does Algorithm 1 as printed need P70's hybrid count (within 25%) with error below 1e-8? | V1 Pass; H1 Not supported; H2 Not supported; H3 Not supported; H4 Supported; R1 Reported |
| 2 | `cb0f777b` | P70 Table 2 for f3 (1/(0.01 + (x - 0.5)^2)): do composite trapezoid and Simpson need P70's printed evaluations (within 10%) to reach 1e-8, and does Algorithm 1 as printed need P70's hybrid count (within 25%) with error below 1e-8? | V1 Pass; H1 Not supported; H2 Not supported; H3 Not supported; H4 Supported; R1 Reported |
| 3 | `1e82916a` | P70 Table 2 for f4 (x sin(10 x)): do composite trapezoid and Simpson need P70's printed evaluations (within 10%) to reach 1e-8, and does Algorithm 1 as printed need P70's hybrid count (within 25%) with error below 1e-8? Is its error below eps at eps 1e-6, 1e-8 and 1e-10? | V1 Pass; H1 Not supported; H2 Not supported; H3 Not supported; H4 Supported; H5 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: CVA-APP-03 (f2): P70's evaluation counts not reproduced; no new search (disclosed).
- Pass 2: CVA-APP-03 (f3): same pattern for the sharp peak.
- Pass 3: CVA-APP-03 (f4): same pattern; Algorithm 1 reliable at three tolerances.

## Unresolved
- The reading of 'n' and of 'evaluations' in P70 remains unresolved; P70's MATLAB code not run.
- No independent quadrature benchmark sourced.
