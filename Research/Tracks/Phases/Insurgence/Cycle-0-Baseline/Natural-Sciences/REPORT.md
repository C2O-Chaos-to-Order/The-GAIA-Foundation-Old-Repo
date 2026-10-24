# Insurgence in the Natural Sciences — Cycle-0-Baseline (IN0)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: insurgence as a new state rising when a threshold is crossed (transcritical bifurcation, P22); onset is slow near the threshold.

## Claims (ledger: `claims/claims.csv`)
- **IN0-NAT-01** [E] In a transcritical bifurcation one equilibrium passes through another and they exchange stability: for dx/dt = r x - x^2 the equilibria are 0 and r, and at r = 0 they collide and swap stabilities, so for r > 0 the zero state becomes unstable and a new nonzero state takes over. *Operationalization:* NAT Insurgence = a new state rising when a threshold is crossed (exchange of stability). *Sources:* P22. *Limits:* One-variable normal form; reading it as 'insurgence' is this track's operationalization, not P22's term.
- **IN0-NAT-02** [P] From a seed of 0.001 the state rose to r for r = 0.05, 0.2 and 1 and decayed for r = -0.1; the time to reach r/2 matched the logistic value ln((r - x0)/x0)/r (77.84, 26.47, 6.91 time units) and was 11 times longer at r = 0.05 than at r = 1: near the threshold a new state rises slowly. *Operationalization:* NAT Insurgence = onset from a seed; slow onset near threshold. *Sources:* SIM-IN-NAT-0/iter-1#V1;SIM-IN-NAT-0/iter-1#H1;SIM-IN-NAT-0/iter-1#H2. *Limits:* Deterministic, no noise; RK4 step 0.01.

## Simulations (SIM-IN-NAT-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 2/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `c4793477` | Onset of a new state at a transcritical bifurcation (P22 Eq. 8.8, dx/dt = r x - x^2): from a seed x0 = 0.001 the state rises to r only for r > 0; is the rise time the logistic value, and does onset slow near the threshold? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Insurgence operationalized for NAT as the rise of a new state at a transcritical bifurcation (IN0-NAT-01) using a source already read in full; no new search (disclosed).

## Unresolved
- Physical insurgence beyond normal forms (nucleation, ignition, convection onset) unsourced.
- No noise in the onset run.
