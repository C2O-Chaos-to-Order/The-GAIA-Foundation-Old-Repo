# Insurgence in the Humanities — Cycle-A-x3 (INA)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P28 adds corpus evidence of latency then S-growth and a near-critical model; simulations reproduce the threshold and the delta^(-1/2) law, and show latency absorbing the distance to threshold.

## Claims (ledger: `claims/claims.csv`)
- **INA-HUM-01** [E] In P21's analysis of US Billboard Hot 100 songs 1960-2010, a style enriched for rap-related tags was very rare before the mid-1980s and then rapidly expanded to become the single largest style; P21 links this rise to the 1991 stylistic revolution. *Operationalization:* HUM Insurgence = a rare style rising rapidly to dominance. *Sources:* P21. *Limits:* Styles are clusters inferred from audio features and listener tags; chart songs only.
- **INA-HUM-02** [P] In a Wright-Fisher toy (1,000 songs, advantage 5%), a new style entering as a single copy took over in only 9.9% of 4,000 runs (Kimura 9.5%); the successful takeovers were S-shaped, with 10%-90% times of 90.9 generations against the logistic 90.1. Rare insurgent styles usually vanish, and the ones that win rise fast. *Operationalization:* HUM Insurgence = establishment and logistic takeover of a rare style. *Sources:* SIM-IN-HUM-0/iter-1#V1;SIM-IN-HUM-0/iter-1#H1;SIM-IN-HUM-0/iter-1#H2. *Limits:* Agent's toy; P21 gives frequencies, not a mechanism.
- **INA-HUM-03** [P] In the French Frantext corpus (1321 to the present) P28 studied 408 forms that underwent semantic expansion; 295 (over 70%) show at least one sigmoidal rise in frequency (p < 0.05 against random growth), and in 69% of sigmoidal growths the rise is preceded by a latency phase of near-constant low frequency lasting up to several centuries. *Operationalization:* HUM Insurgence = a new meaning taking over after a latency. *Sources:* P28. *Limits:* Single corpus and language; forms chosen by the authors (functional meanings); latency may be underestimated when the form is too rare to appear.
- **INA-HUM-04** [P] P28 models semantic expansion as a random walk of exemplar frequencies with a control parameter (the strength of the link from a related context) that tunes the system near a saddle-node bifurcation; latency is a first-passage time out of a trapping region of near-zero drift and the S-growth the fast convergence after it, and both durations are predicted to follow inverse-Gaussian-like distributions, as found in the corpus. *Operationalization:* HUM Insurgence = near-critical latency then S-growth. *Sources:* P28. *Limits:* P28 notes the inverse Gaussian fit is not perfect (KL divergence 0.10); model is mean-field, sociolinguistic factors backgrounded.
- **INA-HUM-05** [P] In P28's deterministic limit (beta = 0.808) the threshold was gamma_c = 0.378; below it the new form stuck at a low frequency (0.037 at delta = -0.05, 0.060 at -0.01) and above it took over, the transmission time falling from 100.2 at delta = 0.001 to 10.7 at 0.1 with log-log slope -0.486, the saddle-node bottleneck law also found in NAT (INA-NAT-03). *Operationalization:* HUM Insurgence = threshold for semantic invasion. *Sources:* SIM-IN-HUM-A/iter-1#V1;SIM-IN-HUM-A/iter-1#H1. *Limits:* gamma_c found numerically; P(x) built from P28's Eqs. 3.1-3.2.
- **INA-HUM-06** [P] In P28's random walk (M = 500) every one of 400 runs completed the change at the threshold (delta = 0), with mean latency 38.2 against mean growth 6.0 time units (latency CV 0.74). Just below threshold (delta = -0.02) the expectation that only some runs escape was not supported: all 400 escaped, but mean latency rose to 181 while growth stayed near 7.5. Noise removes the sharp threshold (as P28 states) and the distance to threshold sets mainly the length of the latency. *Operationalization:* HUM Insurgence = latency then S-growth. *Sources:* SIM-IN-HUM-A/iter-2#V1;SIM-IN-HUM-A/iter-2#H1;SIM-IN-HUM-A/iter-2#H2;SIM-IN-HUM-A/iter-3#V1;SIM-IN-HUM-A/iter-3#H1;SIM-IN-HUM-A/iter-3#H2. *Limits:* M = 500 (P28 used 5000), so noise is stronger than in P28; latency window x_c +/- 0.1 is the agent's.

## Simulations (SIM-IN-HUM-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 4/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `b43f28cf` | P28's model of semantic expansion, deterministic limit (HUM pass 2): with beta = 0.808, is there a threshold gamma_c below which the new form is stuck, and does the transmission time diverge like delta^(-1/2) just above it? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `46ca6b0c` | P28's random walk at the threshold (HUM pass 3): with delta = 0 (P28's choice) and M = 500 exemplars, 400 runs: does every run complete the change (finite stochastic transmission time, P28 Fig. 6b), and is the latency longer than the growth? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `067e87f2` | Just below the threshold (HUM pass 3): delta = -0.02; does noise still let some runs escape (P28: no clear-cut transition in the stochastic model), but not all within 2,000 time units? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: INA-HUM-03 (latency then S-growth in about 400 French semantic expansions) and INA-HUM-04 (P28's near-critical random-walk model).
- Pass 2: INA-HUM-05: P28's deterministic threshold gamma_c = 0.378 and the delta^(-1/2) transmission time.
- Pass 3: INA-HUM-06: in the stochastic walk all runs complete even below threshold (H1 of iter-3 not supported); latency, not growth, absorbs the distance to threshold.

## Unresolved
- P29 (Ghanbarnejad et al., S-curve vs exponential) could not be fetched.
- Single-language corpus (P28); supplementary material not read; M = 500 vs P28's 5000.
