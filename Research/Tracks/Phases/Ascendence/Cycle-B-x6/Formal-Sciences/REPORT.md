# Ascendence in the Formal Sciences — Cycle-B-x6 (ASB)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: natural-gradient step limit is global; plain steps can diverge below 2/lambda_max.

## Claims (ledger: `claims/claims.csv`)
- **ASB-FOR-01** [E] P86 shows that natural gradient descent x' = -M(x)^-1 grad f converges globally and exponentially when f is strongly geodesically convex in a metric M, equivalently when the flow is contracting in M, which covers non-convex functions; the natural gradient is 'the direction of steepest ascent on the manifold'. For the Rosenbrock function with M = [[400x1^2 + 1, -200x1], [-200x1, 100]] the flow is h = -2[x1 - 1, x1^2 - 2x1 + x2] and contracts at rate 2 (M A + A^T M + Mdot = -4M). *Operationalization:* FOR Ascendence = steepest ascent / descent toward an optimum. *Sources:* P86. *Limits:* Contraction metrics must be found case by case; Example 5's metric is typeset in a layout that is garbled in the extracted text.
- **ASB-FOR-02** [E] At 2000 random points in [-3, 3]^2, P86's printed Rosenbrock field equals -M^-1 grad f and M A + A^T M + Mdot = -4M exactly (maximum relative error 0); in P86's coordinates z the flow decays as e^-2t (|z(1)|/|z(0)| = 0.13533528 = e^-2); Example 5's metric as the agent read it gives a largest generalized eigenvalue of exactly -4 (rate 2). From (-1.5, 2) natural gradient flow reached within 1e-4 of (1, 1) at t 5.49, plain gradient flow at t 23.47. *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-0/iter-1#V1;SIM-AS-FOR-0/iter-1#H1;SIM-AS-FOR-0/iter-1#H2;SIM-AS-FOR-0/iter-1#H3;SIM-AS-FOR-0/iter-1#H4. *Limits:* Checks P86's examples, not its theorems in general; one start point for the flow comparison; Example 5's reading is the agent's.
- **ASB-FOR-03** [E] Ascent in discrete steps has a speed limit. Euler steps of P86's natural-gradient field on Rosenbrock converged from all three starts for dt 0.5 (in 2 steps) and 0.9 (63-72 steps), stalled at dt 1.0 and diverged for dt 1.1 and 1.5, the same dt < 1 limit as the linear z-map 1 - 2dt. Plain gradient steps converged for eta 0.0005 and 0.001 (29,000-70,000 steps) and failed for eta 0.002 and 0.005, consistent with the limit 2/lambda_max = 0.002 at the minimum. *Operationalization:* FOR Ascendence = steepest ascent / descent in discrete steps. *Sources:* SIM-AS-FOR-A/iter-1#V1;SIM-AS-FOR-A/iter-1#H1;SIM-AS-FOR-A/iter-1#H2;SIM-AS-FOR-A/iter-1#H3;SIM-AS-FOR-A/iter-2#V1;SIM-AS-FOR-A/iter-2#H1;SIM-AS-FOR-A/iter-2#H2;SIM-AS-FOR-A/iter-2#H3. *Limits:* Three start points; the 2/lambda_max limit is standard theory added by the agent, not P86.
- **ASB-FOR-04** [E] From 200 random starts in [-3, 3]^2, natural gradient flow reached within 1e-4 of (1, 1) every time (median t 5.30) and faster than plain gradient flow every time (median 22.1), as P86's global contraction implies. The pre-registered check that times never exceed ln(|z0|/tol)/2 by more than 0.05 was not supported (maximum excess 0.39); this is the agent's design error, since the stopping rule measures |x - x*| while the prediction is for |z|. *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-A/iter-3#V1;SIM-AS-FOR-A/iter-3#H1;SIM-AS-FOR-A/iter-3#H2;SIM-AS-FOR-A/iter-3#H3. *Limits:* H3 compares unlike norms (disclosed in the SPEC).
- **ASB-FOR-05** [E] The natural-gradient step limit is sharp and global: Euler steps converged from all starts at dt 0.95 (132-152 steps) and 0.99 (684-786 steps), and from far starts ((10, -10), (-5, 25), (3, 9)) in 2 steps at dt 0.5 and 74-83 steps at dt 0.9, as the linear z-map 1 - 2dt predicts. *Operationalization:* FOR Ascendence = steepest ascent in discrete steps. *Sources:* SIM-AS-FOR-B/iter-1#V1;SIM-AS-FOR-B/iter-1#H1;SIM-AS-FOR-B/iter-5#V1;SIM-AS-FOR-B/iter-5#H1. *Limits:* Six start points in total.
- **ASB-FOR-06** [E] Plain gradient steps have no global step limit at 2/lambda_max: from (2, -1) they diverged even at eta 0.0015 and 0.0019, below the limit at the minimum (0.001997), so the pre-registered check that both converge from all starts was not supported; from the other two starts they converged (17,000-23,000 steps), and eta 0.0021 converged from no start. In continuous time natural gradient flow converged from all 100 starts in [-6, 6]^2 and all 200 in [-1, 1]^2, always faster than plain flow (median t 5.9 vs 22.2; 5.0 vs 22.1). P86's Example 3 identity held exactly on [-10, 10]^2, and the agent's reading of Example 5's metric gives contraction rate 2 on the whole box (largest generalized eigenvalue -4). *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-B/iter-2#V1;SIM-AS-FOR-B/iter-2#H1;SIM-AS-FOR-B/iter-2#H2;SIM-AS-FOR-B/iter-3#V1;SIM-AS-FOR-B/iter-3#H1;SIM-AS-FOR-B/iter-3#H2;SIM-AS-FOR-B/iter-4#V1;SIM-AS-FOR-B/iter-4#H1;SIM-AS-FOR-B/iter-4#H2;SIM-AS-FOR-B/iter-6#V1;SIM-AS-FOR-B/iter-6#H1;SIM-AS-FOR-B/iter-6#H2. *Limits:* 2/lambda_max is standard theory added by the agent; Example 5's metric reading is the agent's.

## Simulations (SIM-AS-FOR-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 9/10)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `1b5a0f5f` | Euler natural-gradient steps just below the limit (dt 0.95, 0.99): convergence from three starts? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `4030528f` | Plain gradient steps near 2/lambda_max (0.001997): do eta 0.0015 and 0.0019 converge and 0.0021 fail from three starts? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |
| 3 | `319ef667` | Global convergence on a larger box [-6, 6]^2 (100 starts): always, and always faster than plain flow? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 4 | `6ac152fe` | P86 Example 3 identity and the agent's reading of Example 5's metric on [-10, 10]^2 (5000 points) | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 5 | `b29c2819` | Euler natural-gradient steps from far starts ((10, -10), (-5, 25), (3, 9)) at dt 0.5 and 0.9 | V1 Pass; H1 Supported; R1 Reported |
| 6 | `83317338` | Near starts ([-1, 1]^2, 200): both flows converge; is natural gradient more than twice as fast (median)? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: ASB-FOR-05: convergence at dt 0.95 and 0.99.
- Pass 2: ASB-FOR-06: plain steps diverge from (2, -1) below 2/lambda_max.
- Pass 3: ASB-FOR-06: global convergence on [-6, 6]^2.
- Pass 4: ASB-FOR-06: Example 3 identity and Example 5 rate on [-10, 10]^2.
- Pass 5: ASB-FOR-05: far starts converge.
- Pass 6: ASB-FOR-06: near starts; natural gradient over 4x faster.

## Unresolved
- Stochastic gradient ascent not covered.
- The global basin of plain gradient steps is not mapped.
