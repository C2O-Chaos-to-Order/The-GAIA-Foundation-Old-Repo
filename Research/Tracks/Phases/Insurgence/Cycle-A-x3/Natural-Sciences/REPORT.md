# Insurgence in the Natural Sciences — Cycle-A-x3 (INA)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: onset near threshold is slow because of a bottleneck (passage time ~ r^(-1/2)); noise makes the moment of onset unpredictable and, if large, earlier.

## Claims (ledger: `claims/claims.csv`)
- **INA-NAT-01** [E] In a transcritical bifurcation one equilibrium passes through another and they exchange stability: for dx/dt = r x - x^2 the equilibria are 0 and r, and at r = 0 they collide and swap stabilities, so for r > 0 the zero state becomes unstable and a new nonzero state takes over. *Operationalization:* NAT Insurgence = a new state rising when a threshold is crossed (exchange of stability). *Sources:* P22. *Limits:* One-variable normal form; reading it as 'insurgence' is this track's operationalization, not P22's term.
- **INA-NAT-02** [P] From a seed of 0.001 the state rose to r for r = 0.05, 0.2 and 1 and decayed for r = -0.1; the time to reach r/2 matched the logistic value ln((r - x0)/x0)/r (77.84, 26.47, 6.91 time units) and was 11 times longer at r = 0.05 than at r = 1: near the threshold a new state rises slowly. *Operationalization:* NAT Insurgence = onset from a seed; slow onset near threshold. *Sources:* SIM-IN-NAT-0/iter-1#V1;SIM-IN-NAT-0/iter-1#H1;SIM-IN-NAT-0/iter-1#H2. *Limits:* Deterministic, no noise; RK4 step 0.01.
- **INA-NAT-03** [P] Just past a saddle-node bifurcation (dx/dt = r + x^2, P22's saddle-node type) the passage from x = -10 to +10 took 313.96, 99.15, 31.22 and 9.74 time units for r = 0.0001, 0.001, 0.01, 0.1, matching 2 arctan(L/sqrt r)/sqrt r within 0.5%; the log-log slope was -0.503, the r^(-1/2) bottleneck law: the closer to threshold, the longer the new state lingers before breaking out. *Operationalization:* NAT Insurgence = break-out through a bottleneck just past threshold. *Sources:* SIM-IN-NAT-A/iter-1#V1;SIM-IN-NAT-A/iter-1#H1. *Limits:* Normal form only; the closed-form time is the agent's integral, not P22's.
- **INA-NAT-04** [P] With noise sigma = 0.005 (larger than the seed 0.001) the transcritical onset at r = 0.05 came at 21.4 time units on average (SE 1.2) instead of the deterministic 77.8, with a coefficient of variation of 0.82; with sigma = 0.0005 the advance was not supported (76.8, SE 1.6), but onset timing still varied (CV 0.30). Noise makes the moment of onset unpredictable; it brings onset forward only when it is large relative to the seed. *Operationalization:* NAT Insurgence = onset timing under noise. *Sources:* SIM-IN-NAT-A/iter-2#V1;SIM-IN-NAT-A/iter-2#H1;SIM-IN-NAT-A/iter-2#H2;SIM-IN-NAT-A/iter-3#V1;SIM-IN-NAT-A/iter-3#H1;SIM-IN-NAT-A/iter-3#H2. *Limits:* Reflecting boundary at x = 0 pushes small x upward, so part of the strong-noise advance is a boundary effect (disclosed in the SPEC).

## Simulations (SIM-IN-NAT-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 4/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `6c10ecb2` | Why onsets near a threshold are slow (NAT pass 2): in the saddle-node normal form dx/dt = r + x^2 just past the bifurcation, does the passage time from -10 to +10 match 2 arctan(L/sqrt r)/sqrt r and scale as r^(-1/2)? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `e588eee8` | Noise and onset (NAT pass 3): with additive noise sigma = 0.005, does a seed x0 = 0.001 at r = 0.05 (P22 Eq. 8.8) break out earlier than the deterministic 77.84 (IN0-NAT-02), and how variable is the onset time? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `b4bdece2` | Noise and onset, weak noise (NAT pass 3): same as iter-2 with sigma = 0.0005 (half the seed): does the advance shrink, and is onset still variable? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: INA-NAT-03: the saddle-node bottleneck (passage time ~ r^(-1/2)) explains why onsets near threshold are slow; no new search (disclosed).
- Pass 2: INA-NAT-04: noise makes onset timing unpredictable and advances onset only when large relative to the seed (iterations 2-3).
- Pass 3: Added nothing: no source on physical insurgence (nucleation, ignition, convection onset) was searched or read in this cycle; the weak-noise run only qualified INA-NAT-04.

## Unresolved
- Physical insurgence beyond normal forms (nucleation, ignition) still unsourced.
- Strong-noise advance partly a reflecting-boundary effect.
