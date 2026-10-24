# Insurgence in the Applied Sciences — Cycle-A-x3 (INA)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: near R0 = 1 rare large chains occur even below threshold; superspreading makes most introductions fail; immunity acts through R = R0 (1 - v) (P26's effective R).

## Claims (ledger: `claims/claims.csv`)
- **INA-APP-01** [E] R0, the expected number of secondary cases one case produces in a completely susceptible population, is usually read as a threshold (an outbreak continues if R0 > 1 and ends if R0 < 1), but it is not a biological constant, not a rate (it says nothing about how fast cases appear), not a measure of severity, and vaccination lowers the effective reproduction number R, not R0; reported values vary widely (measles 3.7-203.3 in one review) and some are obsolete. *Operationalization:* APP Insurgence = emergence of an outbreak when cases more than replace themselves. *Sources:* P26. *Limits:* Perspective article; the figures are P26's citations.
- **INA-APP-03** [E] P26 notes that removing susceptible people by vaccination does not technically reduce R0, because R0 assumes a completely susceptible population; for vaccination the appropriate metric is the effective reproduction number R, which does not assume complete susceptibility. *Operationalization:* APP Insurgence = outbreak potential in a partly immune population. *Sources:* P26. *Limits:* Definitional point; P26 gives no formula for R.
- **INA-APP-02** [P] In a branching model of one introduced case, no outbreak reached 1,000 cases at R0 = 0.8; at R0 = 1.5 and 3 major outbreaks occurred in 58.1% and 94.1% of 20,000 runs (theory 58.3%, 94.0%), so even above the threshold many introductions die out. Changing the generation time from 3 to 15 days left the outbreak probability unchanged and stretched the time to 1,000 cases five-fold (44 vs 219 days at R0 = 1.5), illustrating P26's point that R0 is not a rate. *Operationalization:* APP Insurgence = outbreak emergence above R0 = 1. *Sources:* SIM-IN-APP-0/iter-1#V1;SIM-IN-APP-0/iter-1#H1;SIM-IN-APP-0/iter-1#H2. *Limits:* Homogeneous Poisson offspring; fully susceptible population.
- **INA-APP-04** [P] Near the threshold the share of introductions reaching 1,000 cases was 9.36% at R0 = 1.05 (theory 9.37%) and 31.6% at 1.2 (31.4%); 'no major outbreak below 1' was not supported: at R0 = 0.95, 0.16% of chains (32 of 20,000) still reached 1,000 cases, after 64 generations on average. Just below the threshold, rare large chains occur. *Operationalization:* APP Insurgence = outbreak emergence near R0 = 1. *Sources:* SIM-IN-APP-A/iter-1#V1;SIM-IN-APP-A/iter-1#H1;SIM-IN-APP-A/iter-1#H2. *Limits:* 'Major' means reaching K = 1000; V1 passed at R0 = 0.95 only through the pre-set 0.002 allowance (disclosed).
- **INA-APP-05** [P] With superspreading (negative-binomial offspring, k = 0.1) the major-outbreak share fell to 7.0% at R0 = 1.5 (theory 6.8%; Poisson 58%) and 16.5% at R0 = 3 (16.2%; Poisson 94%): heterogeneity makes most introductions fail even at high R0, but those that take off are explosive. 'No major outbreak at R0 = 0.8' was not supported: one chain in 20,000 reached 1,000 cases. *Operationalization:* APP Insurgence = emergence with heterogeneous transmission. *Sources:* SIM-IN-APP-A/iter-2#V1;SIM-IN-APP-A/iter-2#H1;SIM-IN-APP-A/iter-2#H2. *Limits:* k = 0.1 illustrative; standard extinction equation, not from P26.
- **INA-APP-06** [P] With 60% random immunity, R0 = 2 gave R = 0.8 and no chain reached 1,000 cases in 20,000; R0 = 3 and 4 gave R = 1.2 and 1.6 and major-outbreak shares 30.9% and 64.4%, matching 1 - q at the reduced R (31.4%, 64.2%): what decides emergence is the effective number R (P26), not R0. *Operationalization:* APP Insurgence = emergence suppressed by immunity. *Sources:* SIM-IN-APP-A/iter-3#V1;SIM-IN-APP-A/iter-3#H1;SIM-IN-APP-A/iter-3#H2. *Limits:* Perfect random immunity, homogeneous mixing.

## Simulations (SIM-IN-APP-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 4/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `44ab6a5c` | Near the threshold (APP pass 2): R0 = 0.95, 1.05, 1.2 (P26's threshold reading); how close is the major-outbreak share (1,000 cases) to 1 - q when R0 is just above 1? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |
| 2 | `0591f241` | Superspreading (APP pass 2; P26 cautions that R0 hides heterogeneity): with negative-binomial offspring (dispersion k = 0.1) and the same R0 = 0.8, 1.5, 3, how much lower is the major-outbreak share than under Poisson (IN0-APP-02)? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |
| 3 | `ed140e7c` | Vaccination (APP pass 3): with a share v = 0.6 immune, offspring Poisson(R0 (1 - v)) for R0 = 2, 3, 4 (R = 0.8, 1.2, 1.6): is there no major outbreak at R = 0.8 and does the share follow 1 - q at the reduced R? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: INA-APP-03 (P26: vaccination changes R, not R0) and INA-APP-04 (near R0 = 1; rare large chains below threshold, H1 not supported).
- Pass 2: INA-APP-05: superspreading (k = 0.1) cuts the major-outbreak share from 58% to 7% at R0 = 1.5.
- Pass 3: INA-APP-06: with 60% immunity emergence follows R = R0 (1 - v).

## Unresolved
- What counts as 'major' (K = 1000) drives the below-threshold result.
- Superspreading dispersion k not sourced.
