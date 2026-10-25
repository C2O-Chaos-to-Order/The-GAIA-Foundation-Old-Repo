# Transcendence in the Applied Sciences — Cycle-0-Baseline (TR0)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: Spanish Self-Transcendence Scale (P100); validity statistics mostly reproduce; three chance-agreement values and a df do not.

## Claims (ledger: `claims/claims.csv`)
- **TR0-APP-02** [E] P100's I-CVIs equal the share of agreeing experts (18/19, 17/19, 16/19, 15/18), its modified kappas follow from its printed I-CVI and Pc, S-CVI is 0.922, and RMSEA (0.053, 0.050, 0.053, 0.078) and chi-square p (0.024, 0.039, 0.023, < 0.001) reproduce for the four factor models. Two pre-registered checks were not supported: the chance agreement Pc = C(N, A) 0.5^N gives 0.00033, 0.0018 and 0.0031 for 17/19, 16/19 and 15/18, not the printed 0.0013, 0.0665 and 0.1120 (the kappas inherit them, though all stay above 0.81); and Bartlett's df for 15 items is 105, not 1,050. *Operationalization:* APP Transcendence = auditing a scale validation. *Sources:* SIM-TR-APP-0/iter-1#V1;SIM-TR-APP-0/iter-1#H1;SIM-TR-APP-0/iter-1#H2;SIM-TR-APP-0/iter-1#H3;SIM-TR-APP-0/iter-1#H4;SIM-TR-APP-0/iter-1#H5;SIM-TR-APP-0/iter-1#H6. *Limits:* Audits printed rounded numbers; Pc formula as P100 cites it (Polit et al.).
- **TR0-APP-01** [P] P100 adapts Reed's Self-Transcendence Scale to Spanish: 19 experts gave a global content validity coefficient S-CVI of 0.92; in 116 adults internal consistency was alpha 0.772 (test) and 0.833 (retest); scores correlated with psychological well-being (r 0.636) and spiritual well-being (0.687); the abstract reports three factors explaining 42.3% of the variance and the four- and three-factor models fit acceptably (RMSEA 0.053 and 0.049). *Operationalization:* APP Transcendence = self-transcendence measured in nursing research. *Sources:* P100. *Limits:* Small online sample; intraclass ICC 0.278 (p 0.097) is low. Slips: Bartlett 'df = 1,050' (105 for 15 items); three factors 42.3% vs four factors 41.4% elsewhere; one-factor SRMR printed 0.837; the 'no children' row total is 16 (11 + 50 = 61); Pc values for three items do not follow the stated formula (TR0-APP-02).

## Simulations (SIM-TR-APP-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 4/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `3282a679` | P100's content-validity and factor-analysis statistics: do I-CVIs, chance agreement Pc, modified kappa and S-CVI follow from the expert counts, do RMSEA and chi-square p follow from chi-square, df and N, and is Bartlett's df right for 15 items? | V1 Pass; H1 Supported; H2 Not supported; H3 Supported; H4 Supported; H5 Supported; H6 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Spanish Self-Transcendence Scale validation sourced (TR0-APP-01); audit: I-CVI, kappa, RMSEA reproduce; three Pc values and Bartlett's df do not (TR0-APP-02).

## Unresolved
- Source of P100's Pc values (0.0013, 0.0665, 0.1120) unexplained.
- Clinical (nursing) outcome studies of self-transcendence not yet read.
