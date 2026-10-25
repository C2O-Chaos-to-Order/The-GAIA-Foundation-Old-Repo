# Transcendence in the Social Sciences — Cycle-0-Baseline (TR0)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: self-transcendence values and prosocial orientation (P99); effects reproduce; two printed numbers do not.

## Claims (ledger: `claims/claims.csv`)
- **TR0-SOC-02** [E] Most of P99's printed numbers reproduce: 1151 + 381 + 123 = 1655 (69.5, 23.0, 7.4%), every main-effect and planned-comparison eta^2 from F and df (largest gap 0.0005), every printed p within 0.002. Two pre-registered checks were not supported: the Results participant flow (1906 - 223 - 23) gives 1660, not the analysed 1655 (the Method flow 1903 - 226 - 22 gives 1655); and the n-weighted Table 3 means reproduce Table 2 for ten values but give -0.524 for Power where Table 2 prints .469. Also: competitors are 7.4% (text elsewhere 7.3%); critical r .048 and .063 (printed .049, .064). *Operationalization:* SOC Transcendence = auditing a values study. *Sources:* SIM-TR-SOC-0/iter-1#V1;SIM-TR-SOC-0/iter-1#H1;SIM-TR-SOC-0/iter-1#H2;SIM-TR-SOC-0/iter-1#H3;SIM-TR-SOC-0/iter-1#H4;SIM-TR-SOC-0/iter-1#H5;SIM-TR-SOC-0/iter-1#H6. *Limits:* Audits printed rounded numbers; error df n - 3 from each row's n is the agent's assumption.
- **TR0-SOC-01** [P] P99 finds that prosocial participants (social value orientation, 1151 of 1655) endorse self-transcendence values, Universalism and Benevolence, more strongly than individualists and competitors, and Power values less strongly (largest effects Universalism eta^2 .037 and Power .040). P99 cautions that combining Universalism and Benevolence into a higher-order Self-transcendence score can obscure differences between them. *Operationalization:* SOC Transcendence = self-transcendence values and prosocial orientation. *Sources:* P99. *Limits:* Student sample; small effects. Slips: the Results text says pro-socials endorsed Conformity 'less strongly' although Table 3's means (-.513 vs -.692 and -.675) and the planned comparison show the opposite; Table 2 prints Power's mean as .469 (Universalism's value); see TR0-SOC-02.

## Simulations (SIM-TR-SOC-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 4/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `d038baab` | P99's printed statistics: do the SVO counts and percentages add up, do both participant flows reach 1655, do eta^2 and p follow from the printed F and df, and do Table 3's group means weight back to Table 2's means? | V1 Pass; H1 Supported; H2 Not supported; H3 Supported; H4 Supported; H5 Supported; H6 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Self-transcendence values and prosocial orientation sourced, with a Conformity wording slip (TR0-SOC-01); audit: eta^2 and p reproduce; Results participant flow (1660) and Table 2's Power mean do not (TR0-SOC-02).

## Unresolved
- Whether Table 2's Power .469 is a typo (weighted mean -0.524) cannot be confirmed without data.
- Higher-order Self-transcendence score not analysed separately by P99.
