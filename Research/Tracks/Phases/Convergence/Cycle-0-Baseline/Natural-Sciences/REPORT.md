# Convergence in the Natural Sciences — Cycle-0-Baseline (CV0)

Phase report: Convergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: convergence as synchronisation (P68); the cheater bound 1/(1 - cos alpha) and the 50-50 equilibrium reproduce exactly in a 200-oscillator run.

## Claims (ledger: `claims/claims.csv`)
- **CV0-NAT-01** [E] P68 models collective synchrony with a Sakaguchi-Kuramoto model in which each individual's phase lag is its strategy; in a population of cooperators (lag 0) and cheaters (lag alpha) the two-cluster state with phase gap alpha is stable when the cheater fraction n_ch < 1/(1 - cos alpha), numerical critical fractions follow this curve, and under P68's payoffs persistent populations settle at 50-50 because the minority loses its advantage as it grows. *Operationalization:* NAT Convergence = synchronisation (oscillators converging on a common rhythm). *Sources:* P68. *Limits:* Identical natural frequencies; one coupling strength. Slips: Eq. 9 has a stray bracket and drops K from the second term; 'strays too far form'; the Fig. 2 caption says the system is incoherent 'when alpha_ch >= pi/2', which on the bound applies only above the critical fraction.
- **CV0-NAT-02** [P] With 200 oscillators started near the two-cluster state, the state persisted at every tested cheater fraction for alpha pi/3 (bound 2) and, for alpha 2pi/3 and 5pi/6, persisted exactly when n_ch was below 1/(1 - cos alpha) (0.667, 0.536) and fell to near-incoherence above it (R 0.058 at alpha 2pi/3, n_ch 0.7; R 0.0002 at 5pi/6, n_ch 0.6); at alpha 2pi/3 with n_ch 0.3 the two clusters stayed locked with R 0.61. P68's replicator dynamic at alpha pi/2 went from 0.2 to 0.500. Classical Kuramoto (lags 0) reached R 1.000. *Operationalization:* NAT Convergence = synchronisation. *Sources:* SIM-CV-NAT-0/iter-1#V1;SIM-CV-NAT-0/iter-1#H1;SIM-CV-NAT-0/iter-1#H2;SIM-CV-NAT-0/iter-1#H3. *Limits:* Tests only P68's analysis, not animal data; the two-cluster criterion is the agent's.

## Simulations (SIM-CV-NAT-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 3/3)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `4e80362b` | P68's two-group Sakaguchi-Kuramoto model: does the cooperator/cheater two-cluster state persist exactly when n_ch < 1/(1 - cos alpha) (N = 200 oscillators, alpha pi/3, 2pi/3, 5pi/6; n_ch 0.3-0.9), and does P68's replicator dynamic at alpha pi/2 settle at the 50-50 population? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Synchrony with phase-lag strategies and the cheater bound sourced (CV0-NAT-01); bound and 50-50 equilibrium reproduced with 200 oscillators (CV0-NAT-02).

## Unresolved
- Convergent evolution (competing reading) not yet read; PMC13438476 found for later cycles.
- Non-identical frequencies and P68's mutation runs (N 1000, sigma 0.05) not reproduced.
