# Insurgence in the Natural Sciences — Cycle-B-x6 (INB)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: insurgence as nucleation (P37): a critical nucleus of near-even odds, waits growing like exp(barrier); noise-advance and bottleneck results replicate.

## Claims (ledger: `claims/claims.csv`)
- **INB-NAT-01** [E] In a transcritical bifurcation one equilibrium passes through another and they exchange stability: for dx/dt = r x - x^2 the equilibria are 0 and r, and at r = 0 they collide and swap stabilities, so for r > 0 the zero state becomes unstable and a new nonzero state takes over. *Operationalization:* NAT Insurgence = a new state rising when a threshold is crossed (exchange of stability). *Sources:* P22. *Limits:* One-variable normal form; reading it as 'insurgence' is this track's operationalization, not P22's term.
- **INB-NAT-05** [E] In classical nucleation theory the free energy of a cluster of n molecules has a surface cost growing like n^(2/3) and a cohesive gain growing like n; their competition gives a maximum at the critical nucleation cluster size n*, the nucleation barrier: smaller clusters dissociate, larger ones grow into the new phase. *Operationalization:* NAT Insurgence = a new phase appearing once a critical nucleus forms. *Sources:* P37. *Limits:* P37 is a short textbook summary; its printed derivative has a sign slip (+ instead of - before the cohesive term) and mixes gamma and gamma_0, while the stated n* and G* follow from the correct sign (agent's check).
- **INB-NAT-02** [P] From a seed of 0.001 the state rose to r for r = 0.05, 0.2 and 1 and decayed for r = -0.1; the time to reach r/2 matched the logistic value ln((r - x0)/x0)/r (77.84, 26.47, 6.91 time units) and was 11 times longer at r = 0.05 than at r = 1: near the threshold a new state rises slowly. *Operationalization:* NAT Insurgence = onset from a seed; slow onset near threshold. *Sources:* SIM-IN-NAT-0/iter-1#V1;SIM-IN-NAT-0/iter-1#H1;SIM-IN-NAT-0/iter-1#H2. *Limits:* Deterministic, no noise; RK4 step 0.01.
- **INB-NAT-03** [P] Just past a saddle-node bifurcation (dx/dt = r + x^2, P22's saddle-node type) the passage from x = -10 to +10 took 313.96, 99.15, 31.22 and 9.74 time units for r = 0.0001, 0.001, 0.01, 0.1, matching 2 arctan(L/sqrt r)/sqrt r within 0.5%; the log-log slope was -0.503, the r^(-1/2) bottleneck law: the closer to threshold, the longer the new state lingers before breaking out. *Operationalization:* NAT Insurgence = break-out through a bottleneck just past threshold. *Sources:* SIM-IN-NAT-A/iter-1#V1;SIM-IN-NAT-A/iter-1#H1. *Limits:* Normal form only; the closed-form time is the agent's integral, not P22's.
- **INB-NAT-04** [P] With noise sigma = 0.005 (larger than the seed 0.001) the transcritical onset at r = 0.05 came at 21.4 time units on average (SE 1.2) instead of the deterministic 77.8, with a coefficient of variation of 0.82; with sigma = 0.0005 the advance was not supported (76.8, SE 1.6), but onset timing still varied (CV 0.30). Noise makes the moment of onset unpredictable; it brings onset forward only when it is large relative to the seed. *Operationalization:* NAT Insurgence = onset timing under noise. *Sources:* SIM-IN-NAT-A/iter-2#V1;SIM-IN-NAT-A/iter-2#H1;SIM-IN-NAT-A/iter-2#H2;SIM-IN-NAT-A/iter-3#V1;SIM-IN-NAT-A/iter-3#H1;SIM-IN-NAT-A/iter-3#H2. *Limits:* Reflecting boundary at x = 0 pushes small x upward, so part of the strong-noise advance is a boundary effect (disclosed in the SPEC).
- **INB-NAT-06** [P] In a cluster-size random walk built on P37's free energy (A = 3, B = 1: n* = 8, G* = 4 kT) the mean time to grow from 1 to 16 molecules was 217.6 (SE 9.8) against the exact 204.9; across barriers of 1.8 to 6.3 kT the waiting time rose from 10 to 2,157, and ln(time) grew with slope 1.17 in G*: waiting for a nucleus grows roughly exponentially with the barrier. *Operationalization:* NAT Insurgence = rare onset over a barrier. *Sources:* SIM-IN-NAT-B/iter-1#V1;SIM-IN-NAT-B/iter-1#H1;SIM-IN-NAT-B/iter-2#V1;SIM-IN-NAT-B/iter-2#H1. *Limits:* Detailed-balance kinetics and the birth-death formula are the agent's, not P37's; slope above 1 reflects small-cluster prefactors.
- **INB-NAT-07** [P] A cluster started exactly at the critical size n* = 27 grew to 54 molecules in 42% of 1,000 walks (SE 1.5%), within 0.15 of one half; at n* = 8 (smoke run) the share was 0.33. The critical nucleus is close to a point of even odds, not a guaranteed take-off. *Operationalization:* NAT Insurgence = critical nucleus as tipping point. *Sources:* SIM-IN-NAT-B/iter-3#V1;SIM-IN-NAT-B/iter-3#H1. *Limits:* Discrete small clusters; commitment depends on the end point chosen.
- **INB-NAT-08** [P] Onset advance grows with noise: mean onset 51.9 (sigma 0.002) and 20.0 (sigma 0.005, replicating INA's 21.4) against the deterministic 77.8, with CV 0.58 and 0.76. The bottleneck law replicated with L = 20 down to r = 1e-5 (993.4 vs 993.4; slope -0.500). *Operationalization:* NAT Insurgence = onset under noise; bottleneck (replications). *Sources:* SIM-IN-NAT-B/iter-4#V1;SIM-IN-NAT-B/iter-4#H1;SIM-IN-NAT-B/iter-4#H2;SIM-IN-NAT-B/iter-5#V1;SIM-IN-NAT-B/iter-5#H1;SIM-IN-NAT-B/iter-5#H2;SIM-IN-NAT-B/iter-6#V1;SIM-IN-NAT-B/iter-6#H1. *Limits:* Reflecting boundary as in INA.

## Simulations (SIM-IN-NAT-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 8/8)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `568854ab` | Classical nucleation as a cluster-size walk (P37): with A = 3, B = 1 (n* = 8, G* = 4 kT) does the simulated mean time to grow from 1 to 16 molecules match the exact birth-death value? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `14c3a69b` | Barrier height and waiting time (P37): for B = 0.8, 1.0, 1.2, 1.5 (G* = 6.25 to 1.78 kT) is ln MFPT linear in G* with slope near 1? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `79aeb749` | Is the critical nucleus a point of no return (P37: below n* clusters dissolve, above they grow)? Share of walks started at n* = 27 (A = 4.5, B = 1) that reach 54 before dissolving. | V1 Pass; H1 Supported; R1 Reported |
| 4 | `799dd16d` | Intermediate noise (NAT x6): sigma = 0.002 between INA's 0.005 and 0.0005: does onset still advance beyond 4 SE? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 5 | `1df4cb13` | Replication of INA iter-2 (sigma 0.005) on a new seed. | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 6 | `8daf80d2` | Replication of INA-NAT-03 with L = 20 and r down to 1e-5. | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: INB-NAT-05: classical nucleation (critical nucleus, barrier) sourced, filling the INA physical-onset gap.
- Pass 2: INB-NAT-06: nucleation waiting time grows roughly as exp(G*).
- Pass 3: INB-NAT-07: the critical nucleus is near even odds (42% at n* = 27).
- Pass 4: INB-NAT-08 (part): intermediate noise gives an intermediate advance.
- Pass 5: Added nothing: replication of INA-NAT-04 on a new seed (folded into INB-NAT-08).
- Pass 6: Added nothing: bottleneck replication only (folded into INB-NAT-08).

## Unresolved
- Nucleation kinetics are the agent's (P37 gives only thermodynamics); P34 review not read.
- Ignition, convection onset unsourced.
