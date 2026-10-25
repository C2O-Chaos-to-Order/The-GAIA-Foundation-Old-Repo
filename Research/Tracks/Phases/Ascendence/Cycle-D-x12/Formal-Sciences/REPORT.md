# Ascendence in the Formal Sciences — Cycle-D-x12 (ASD)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x12: plain-step basin shrinks with step size (25 to 0 of 25); natural-gradient limit dt < 1 holds everywhere.

## Claims (ledger: `claims/claims.csv`)
- **ASD-FOR-01** [E] P86 shows that natural gradient descent x' = -M(x)^-1 grad f converges globally and exponentially when f is strongly geodesically convex in a metric M, equivalently when the flow is contracting in M, which covers non-convex functions; the natural gradient is 'the direction of steepest ascent on the manifold'. For the Rosenbrock function with M = [[400x1^2 + 1, -200x1], [-200x1, 100]] the flow is h = -2[x1 - 1, x1^2 - 2x1 + x2] and contracts at rate 2 (M A + A^T M + Mdot = -4M). *Operationalization:* FOR Ascendence = steepest ascent / descent toward an optimum. *Sources:* P86. *Limits:* Contraction metrics must be found case by case; Example 5's metric is typeset in a layout that is garbled in the extracted text.
- **ASD-FOR-02** [E] At 2000 random points in [-3, 3]^2, P86's printed Rosenbrock field equals -M^-1 grad f and M A + A^T M + Mdot = -4M exactly (maximum relative error 0); in P86's coordinates z the flow decays as e^-2t (|z(1)|/|z(0)| = 0.13533528 = e^-2); Example 5's metric as the agent read it gives a largest generalized eigenvalue of exactly -4 (rate 2). From (-1.5, 2) natural gradient flow reached within 1e-4 of (1, 1) at t 5.49, plain gradient flow at t 23.47. *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-0/iter-1#V1;SIM-AS-FOR-0/iter-1#H1;SIM-AS-FOR-0/iter-1#H2;SIM-AS-FOR-0/iter-1#H3;SIM-AS-FOR-0/iter-1#H4. *Limits:* Checks P86's examples, not its theorems in general; one start point for the flow comparison; Example 5's reading is the agent's.
- **ASD-FOR-03** [E] Ascent in discrete steps has a speed limit. Euler steps of P86's natural-gradient field on Rosenbrock converged from all three starts for dt 0.5 (in 2 steps) and 0.9 (63-72 steps), stalled at dt 1.0 and diverged for dt 1.1 and 1.5, the same dt < 1 limit as the linear z-map 1 - 2dt. Plain gradient steps converged for eta 0.0005 and 0.001 (29,000-70,000 steps) and failed for eta 0.002 and 0.005, consistent with the limit 2/lambda_max = 0.002 at the minimum. *Operationalization:* FOR Ascendence = steepest ascent / descent in discrete steps. *Sources:* SIM-AS-FOR-A/iter-1#V1;SIM-AS-FOR-A/iter-1#H1;SIM-AS-FOR-A/iter-1#H2;SIM-AS-FOR-A/iter-1#H3;SIM-AS-FOR-A/iter-2#V1;SIM-AS-FOR-A/iter-2#H1;SIM-AS-FOR-A/iter-2#H2;SIM-AS-FOR-A/iter-2#H3. *Limits:* Three start points; the 2/lambda_max limit is standard theory added by the agent, not P86.
- **ASD-FOR-04** [E] From 200 random starts in [-3, 3]^2, natural gradient flow reached within 1e-4 of (1, 1) every time (median t 5.30) and faster than plain gradient flow every time (median 22.1), as P86's global contraction implies. The pre-registered check that times never exceed ln(|z0|/tol)/2 by more than 0.05 was not supported (maximum excess 0.39); this is the agent's design error, since the stopping rule measures |x - x*| while the prediction is for |z|. *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-A/iter-3#V1;SIM-AS-FOR-A/iter-3#H1;SIM-AS-FOR-A/iter-3#H2;SIM-AS-FOR-A/iter-3#H3. *Limits:* H3 compares unlike norms (disclosed in the SPEC).
- **ASD-FOR-05** [E] The natural-gradient step limit is sharp and global: Euler steps converged from all starts at dt 0.95 (132-152 steps) and 0.99 (684-786 steps), and from far starts ((10, -10), (-5, 25), (3, 9)) in 2 steps at dt 0.5 and 74-83 steps at dt 0.9, as the linear z-map 1 - 2dt predicts. *Operationalization:* FOR Ascendence = steepest ascent in discrete steps. *Sources:* SIM-AS-FOR-B/iter-1#V1;SIM-AS-FOR-B/iter-1#H1;SIM-AS-FOR-B/iter-5#V1;SIM-AS-FOR-B/iter-5#H1. *Limits:* Six start points in total.
- **ASD-FOR-06** [E] Plain gradient steps have no global step limit at 2/lambda_max: from (2, -1) they diverged even at eta 0.0015 and 0.0019, below the limit at the minimum (0.001997), so the pre-registered check that both converge from all starts was not supported; from the other two starts they converged (17,000-23,000 steps), and eta 0.0021 converged from no start. In continuous time natural gradient flow converged from all 100 starts in [-6, 6]^2 and all 200 in [-1, 1]^2, always faster than plain flow (median t 5.9 vs 22.2; 5.0 vs 22.1). P86's Example 3 identity held exactly on [-10, 10]^2, and the agent's reading of Example 5's metric gives contraction rate 2 on the whole box (largest generalized eigenvalue -4). *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-B/iter-2#V1;SIM-AS-FOR-B/iter-2#H1;SIM-AS-FOR-B/iter-2#H2;SIM-AS-FOR-B/iter-3#V1;SIM-AS-FOR-B/iter-3#H1;SIM-AS-FOR-B/iter-3#H2;SIM-AS-FOR-B/iter-4#V1;SIM-AS-FOR-B/iter-4#H1;SIM-AS-FOR-B/iter-4#H2;SIM-AS-FOR-B/iter-6#V1;SIM-AS-FOR-B/iter-6#H1;SIM-AS-FOR-B/iter-6#H2. *Limits:* 2/lambda_max is standard theory added by the agent; Example 5's metric reading is the agent's.
- **ASD-FOR-07** [E] Plain gradient steps have a start-dependent basin: on a 5 x 5 grid over [-1.95, 2.05]^2, eta 0.0015 converged from 19 of 25 starts (diverging from the six corner and edge starts at x -1.95 or 2.05 with y <= 0.05), eta 0.001 from 23 (diverging from (-1.95, -1.95) and (2.05, -1.95); pre-registered 'every start' not supported), and eta 0.0005 from all 25. *Operationalization:* FOR Ascendence = steepest descent in discrete steps. *Sources:* SIM-AS-FOR-C/iter-1#V1;SIM-AS-FOR-C/iter-1#H1;SIM-AS-FOR-C/iter-2#V1;SIM-AS-FOR-C/iter-2#H1;SIM-AS-FOR-C/iter-3#V1;SIM-AS-FOR-C/iter-3#H1. *Limits:* One test function (Rosenbrock, P86's example); grid of 25.
- **ASD-FOR-08** [E] Natural-gradient ascent is start-independent: Euler steps converged from every grid start at dt 0.99 and from none at dt 1.01, and from far starts at dt 0.999; the continuous flow converged from all 100 starts in [-10, 10]^2 (median t 6.3 vs 24.2 for plain flow) and was faster from every start in [-0.1, 0.1]^2; P86's Example 3 identity and the agent's Example 5 rate held on [-20, 20]^2. *Operationalization:* FOR Ascendence = natural-gradient ascent. *Sources:* SIM-AS-FOR-C/iter-4#V1;SIM-AS-FOR-C/iter-4#H1;SIM-AS-FOR-C/iter-5#V1;SIM-AS-FOR-C/iter-5#H1;SIM-AS-FOR-C/iter-6#V1;SIM-AS-FOR-C/iter-6#H1;SIM-AS-FOR-C/iter-7#V1;SIM-AS-FOR-C/iter-7#H1;SIM-AS-FOR-C/iter-8#V1;SIM-AS-FOR-C/iter-8#H1;SIM-AS-FOR-C/iter-9#V1;SIM-AS-FOR-C/iter-9#H1. *Limits:* Example 5's metric reading is the agent's.
- **ASD-FOR-09** [E] The basin of plain gradient steps shrinks as the step grows toward the limit: of 25 grid starts, 25 converge at eta 0.0001 and 0.0005, 23 at 0.001, 21 at 0.0012, 19 at 0.0015 (ASC), 17 at 0.0018, 16 at 0.0019 and none at 0.0025. *Operationalization:* FOR Ascendence = steepest descent in discrete steps. *Sources:* SIM-AS-FOR-D/iter-1#V1;SIM-AS-FOR-D/iter-1#H1;SIM-AS-FOR-D/iter-2#V1;SIM-AS-FOR-D/iter-2#H1;SIM-AS-FOR-D/iter-3#V1;SIM-AS-FOR-D/iter-3#H1;SIM-AS-FOR-D/iter-4#V1;SIM-AS-FOR-D/iter-4#H1;SIM-AS-FOR-D/iter-12#V1;SIM-AS-FOR-D/iter-12#H1. *Limits:* One test function; 25-point grid.
- **ASD-FOR-10** [E] The natural-gradient limit is exactly dt < 1 everywhere: every grid start converges at dt 0.5 and none at dt 1.0 or 1.5; very far starts ((50, -50), (-30, 100), (0, 40)) converge at dt 0.95; the continuous flow converged from all 300 starts in [-3, 3]^2 and all 50 in [-15, 15]^2, always faster than plain flow (median t 6.5 vs 24.1 on [-15, 15]^2); the Example 3 identity and Example 5 rate held on [-50, 50]^2. *Operationalization:* FOR Ascendence = natural-gradient ascent. *Sources:* SIM-AS-FOR-D/iter-5#V1;SIM-AS-FOR-D/iter-5#H1;SIM-AS-FOR-D/iter-6#V1;SIM-AS-FOR-D/iter-6#H1;SIM-AS-FOR-D/iter-7#V1;SIM-AS-FOR-D/iter-7#H1;SIM-AS-FOR-D/iter-8#V1;SIM-AS-FOR-D/iter-8#H1;SIM-AS-FOR-D/iter-9#V1;SIM-AS-FOR-D/iter-9#H1;SIM-AS-FOR-D/iter-10#V1;SIM-AS-FOR-D/iter-10#H1;SIM-AS-FOR-D/iter-11#V1;SIM-AS-FOR-D/iter-11#H1. *Limits:* Example 5's metric reading is the agent's.

## Simulations (SIM-AS-FOR-D; 12 iteration(s), spec-first; validation 12/12, hypotheses supported 12/12)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `3b0a5830` | Plain steps eta 0.0012 on the grid | V1 Pass; H1 Supported; R1 Reported |
| 2 | `35e5ce1d` | Plain steps eta 0.0018 on the grid | V1 Pass; H1 Supported; R1 Reported |
| 3 | `a47d3715` | Plain steps eta 0.0019 on the grid | V1 Pass; H1 Supported; R1 Reported |
| 4 | `dbb76e11` | Plain steps eta 0.0025 on the grid | V1 Pass; H1 Supported; R1 Reported |
| 5 | `644934ce` | Euler natural dt 0.5 on the grid | V1 Pass; H1 Supported; R1 Reported |
| 6 | `f21399d6` | Euler natural dt 1.0 on the grid | V1 Pass; H1 Supported; R1 Reported |
| 7 | `3283adbc` | Euler natural dt 1.5 on the grid | V1 Pass; H1 Supported; R1 Reported |
| 8 | `29c153ba` | Natural flow from 300 starts in [-3, 3]^2 | V1 Pass; H1 Supported; R1 Reported |
| 9 | `1eb41f12` | Natural vs plain flow from 50 starts in [-15, 15]^2 | V1 Pass; H1 Supported; R1 Reported |
| 10 | `2591e4f9` | Example 3 identity and Example 5 rate on [-50, 50]^2 | V1 Pass; H1 Supported; R1 Reported |
| 11 | `856c7c84` | Euler natural dt 0.95 from very far starts | V1 Pass; H1 Supported; R1 Reported |
| 12 | `d6fe7855` | Plain steps eta 0.0001 on the grid | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (12; details `research/PASSES.md`)
- Pass 1: ASD-FOR-09 (iteration 1).
- Pass 2: ASD-FOR-09 (iteration 2).
- Pass 3: ASD-FOR-09 (iteration 3).
- Pass 4: ASD-FOR-09 (iteration 4).
- Pass 5: ASD-FOR-10 (iteration 5).
- Pass 6: ASD-FOR-10 (iteration 6).
- Pass 7: ASD-FOR-10 (iteration 7).
- Pass 8: ASD-FOR-10 (iteration 8).
- Pass 9: ASD-FOR-10 (iteration 9).
- Pass 10: ASD-FOR-10 (iteration 10).
- Pass 11: ASD-FOR-10 (iteration 11).
- Pass 12: ASD-FOR-09 (iteration 12).

## Unresolved
- Stochastic gradient ascent not covered.
- Plain-step basin mapped only on a 25-point grid, one function.
