# Ascendence in the Formal Sciences — Cycle-A-x3 (ASA)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: discrete ascent has a step-size limit (dt < 1 natural, 2/lambda_max plain); global convergence from 200 starts.

## Claims (ledger: `claims/claims.csv`)
- **ASA-FOR-01** [E] P86 shows that natural gradient descent x' = -M(x)^-1 grad f converges globally and exponentially when f is strongly geodesically convex in a metric M, equivalently when the flow is contracting in M, which covers non-convex functions; the natural gradient is 'the direction of steepest ascent on the manifold'. For the Rosenbrock function with M = [[400x1^2 + 1, -200x1], [-200x1, 100]] the flow is h = -2[x1 - 1, x1^2 - 2x1 + x2] and contracts at rate 2 (M A + A^T M + Mdot = -4M). *Operationalization:* FOR Ascendence = steepest ascent / descent toward an optimum. *Sources:* P86. *Limits:* Contraction metrics must be found case by case; Example 5's metric is typeset in a layout that is garbled in the extracted text.
- **ASA-FOR-02** [E] At 2000 random points in [-3, 3]^2, P86's printed Rosenbrock field equals -M^-1 grad f and M A + A^T M + Mdot = -4M exactly (maximum relative error 0); in P86's coordinates z the flow decays as e^-2t (|z(1)|/|z(0)| = 0.13533528 = e^-2); Example 5's metric as the agent read it gives a largest generalized eigenvalue of exactly -4 (rate 2). From (-1.5, 2) natural gradient flow reached within 1e-4 of (1, 1) at t 5.49, plain gradient flow at t 23.47. *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-0/iter-1#V1;SIM-AS-FOR-0/iter-1#H1;SIM-AS-FOR-0/iter-1#H2;SIM-AS-FOR-0/iter-1#H3;SIM-AS-FOR-0/iter-1#H4. *Limits:* Checks P86's examples, not its theorems in general; one start point for the flow comparison; Example 5's reading is the agent's.
- **ASA-FOR-03** [E] Ascent in discrete steps has a speed limit. Euler steps of P86's natural-gradient field on Rosenbrock converged from all three starts for dt 0.5 (in 2 steps) and 0.9 (63-72 steps), stalled at dt 1.0 and diverged for dt 1.1 and 1.5, the same dt < 1 limit as the linear z-map 1 - 2dt. Plain gradient steps converged for eta 0.0005 and 0.001 (29,000-70,000 steps) and failed for eta 0.002 and 0.005, consistent with the limit 2/lambda_max = 0.002 at the minimum. *Operationalization:* FOR Ascendence = steepest ascent / descent in discrete steps. *Sources:* SIM-AS-FOR-A/iter-1#V1;SIM-AS-FOR-A/iter-1#H1;SIM-AS-FOR-A/iter-1#H2;SIM-AS-FOR-A/iter-1#H3;SIM-AS-FOR-A/iter-2#V1;SIM-AS-FOR-A/iter-2#H1;SIM-AS-FOR-A/iter-2#H2;SIM-AS-FOR-A/iter-2#H3. *Limits:* Three start points; the 2/lambda_max limit is standard theory added by the agent, not P86.
- **ASA-FOR-04** [E] From 200 random starts in [-3, 3]^2, natural gradient flow reached within 1e-4 of (1, 1) every time (median t 5.30) and faster than plain gradient flow every time (median 22.1), as P86's global contraction implies. The pre-registered check that times never exceed ln(|z0|/tol)/2 by more than 0.05 was not supported (maximum excess 0.39); this is the agent's design error, since the stopping rule measures |x - x*| while the prediction is for |z|. *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-A/iter-3#V1;SIM-AS-FOR-A/iter-3#H1;SIM-AS-FOR-A/iter-3#H2;SIM-AS-FOR-A/iter-3#H3. *Limits:* H3 compares unlike norms (disclosed in the SPEC).

## Simulations (SIM-AS-FOR-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 8/9)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `b759b19d` | Discrete steps on P86's Example 3: do Euler steps of the natural-gradient field converge from three starts for dt 0.5 and 0.9 and fail for dt 1.1 and 1.5 (in z-coordinates the linear map 1 - 2dt converges iff dt < 1)? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 2 | `b8f7137d` | Plain gradient steps on Rosenbrock: do steps of 0.0005 and 0.001 converge from three starts within 100,000 steps and does 0.005 (above 2/lambda_max at the minimum, 0.002) fail? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 3 | `48ce2b99` | Global convergence claim of P86 for Example 3: from 200 random starts in [-3, 3]^2 does natural gradient flow always reach (1, 1), faster than plain gradient flow, in the time predicted by zdot = -2z? | V1 Pass; H1 Supported; H2 Supported; H3 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: ASA-FOR-03: discrete natural-gradient steps converge only for dt < 1; plain steps only below 2/lambda_max.
- Pass 2: ASA-FOR-03 (plain steps, iteration 2).
- Pass 3: ASA-FOR-04: global convergence from 200 random starts; one design error disclosed.

## Unresolved
- Stochastic gradient ascent (noisy steps) not covered.
- Example 5's metric reading depends on a garbled layout.
