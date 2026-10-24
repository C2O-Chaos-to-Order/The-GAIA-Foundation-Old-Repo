# Ascendence in the Formal Sciences — Cycle-0-Baseline (AS0)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: steepest ascent/descent and contraction (P86); the Rosenbrock example's contraction at rate 2 holds exactly.

## Claims (ledger: `claims/claims.csv`)
- **AS0-FOR-01** [E] P86 shows that natural gradient descent x' = -M(x)^-1 grad f converges globally and exponentially when f is strongly geodesically convex in a metric M, equivalently when the flow is contracting in M, which covers non-convex functions; the natural gradient is 'the direction of steepest ascent on the manifold'. For the Rosenbrock function with M = [[400x1^2 + 1, -200x1], [-200x1, 100]] the flow is h = -2[x1 - 1, x1^2 - 2x1 + x2] and contracts at rate 2 (M A + A^T M + Mdot = -4M). *Operationalization:* FOR Ascendence = steepest ascent / descent toward an optimum. *Sources:* P86. *Limits:* Contraction metrics must be found case by case; Example 5's metric is typeset in a layout that is garbled in the extracted text.
- **AS0-FOR-02** [E] At 2000 random points in [-3, 3]^2, P86's printed Rosenbrock field equals -M^-1 grad f and M A + A^T M + Mdot = -4M exactly (maximum relative error 0); in P86's coordinates z the flow decays as e^-2t (|z(1)|/|z(0)| = 0.13533528 = e^-2); Example 5's metric as the agent read it gives a largest generalized eigenvalue of exactly -4 (rate 2). From (-1.5, 2) natural gradient flow reached within 1e-4 of (1, 1) at t 5.49, plain gradient flow at t 23.47. *Operationalization:* FOR Ascendence = steepest ascent / descent. *Sources:* SIM-AS-FOR-0/iter-1#V1;SIM-AS-FOR-0/iter-1#H1;SIM-AS-FOR-0/iter-1#H2;SIM-AS-FOR-0/iter-1#H3;SIM-AS-FOR-0/iter-1#H4. *Limits:* Checks P86's examples, not its theorems in general; one start point for the flow comparison; Example 5's reading is the agent's.

## Simulations (SIM-AS-FOR-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 4/4)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `4a92cb17` | P86's contraction analysis: do Example 3's printed natural-gradient field and contraction identity (rate 2) hold numerically at 2000 random points, does Example 5's metric (as read from the garbled extracted text) give rate 2, and does natural gradient flow reach the Rosenbrock minimum sooner than plain gradient flow? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Contraction analysis of natural gradient ('steepest ascent on the manifold') sourced (AS0-FOR-01); Example 3 identities and Example 5 rate verified numerically; natural gradient faster than plain flow on Rosenbrock (AS0-FOR-02).

## Unresolved
- Discrete-step gradient ascent (step-size limits) not covered; only continuous flows checked.
- Example 5's metric reading depends on a garbled layout.
