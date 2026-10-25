# Transcendence in the Social Sciences — Cycle-A-x3 (TRA)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P99's power statements reproduce; small effects have power near 0.5; Benevolence orders the groups differently.

## Claims (ledger: `claims/claims.csv`)
- **TRA-SOC-02** [E] Most of P99's printed numbers reproduce: 1151 + 381 + 123 = 1655 (69.5, 23.0, 7.4%), every main-effect and planned-comparison eta^2 from F and df (largest gap 0.0005), every printed p within 0.002. Two pre-registered checks were not supported: the Results participant flow (1906 - 223 - 23) gives 1660, not the analysed 1655 (the Method flow 1903 - 226 - 22 gives 1655); and the n-weighted Table 3 means reproduce Table 2 for ten values but give -0.524 for Power where Table 2 prints .469. Also: competitors are 7.4% (text elsewhere 7.3%); critical r .048 and .063 (printed .049, .064). *Operationalization:* SOC Transcendence = auditing a values study. *Sources:* SIM-TR-SOC-0/iter-1#V1;SIM-TR-SOC-0/iter-1#H1;SIM-TR-SOC-0/iter-1#H2;SIM-TR-SOC-0/iter-1#H3;SIM-TR-SOC-0/iter-1#H4;SIM-TR-SOC-0/iter-1#H5;SIM-TR-SOC-0/iter-1#H6. *Limits:* Audits printed rounded numbers; error df n - 3 from each row's n is the agent's assumption.
- **TRA-SOC-03** [E] At P99's unequal group sizes (1151, 381, 123) a one-way ANOVA detects a Universalism-sized effect (eta^2 .037) essentially always (power 1.00) but a Security-sized effect (eta^2 .003) only about half the time (Monte Carlo 0.510, noncentral F 0.501), so P99's non-significant small effects are not evidence of no difference. *Operationalization:* SOC Transcendence = power of the values comparisons. *Sources:* SIM-TR-SOC-A/iter-1#V1;SIM-TR-SOC-A/iter-1#H1;SIM-TR-SOC-A/iter-2#V1;SIM-TR-SOC-A/iter-2#H1. *Limits:* Normal data with unit SD and Table 3's mean pattern assumed.
- **TRA-SOC-04** [E] P99's five G*Power statements reproduce (0.962, 0.963, 0.998, 0.921, 0.486 vs .96, .96, .99, .92, .49). Universalism means are ordered prosocial > individualist > competitor, but one pre-registered check was not supported: for the first Benevolence measure competitors (.667) score above individualists (.558), so self-transcendence values do not rank the three SVO groups the same way, consistent with P99's caution against a combined Self-transcendence score. *Operationalization:* SOC Transcendence = auditing power and orderings. *Sources:* SIM-TR-SOC-A/iter-3#V1;SIM-TR-SOC-A/iter-3#H1;SIM-TR-SOC-A/iter-3#H2;SIM-TR-SOC-A/iter-3#H3. *Limits:* Ordering of printed means only; no test of the individualist-competitor difference is recomputed.
- **TRA-SOC-01** [P] P99 finds that prosocial participants (social value orientation, 1151 of 1655) endorse self-transcendence values, Universalism and Benevolence, more strongly than individualists and competitors, and Power values less strongly (largest effects Universalism eta^2 .037 and Power .040). P99 cautions that combining Universalism and Benevolence into a higher-order Self-transcendence score can obscure differences between them. *Operationalization:* SOC Transcendence = self-transcendence values and prosocial orientation. *Sources:* P99. *Limits:* Student sample; small effects. Slips: the Results text says pro-socials endorsed Conformity 'less strongly' although Table 3's means (-.513 vs -.692 and -.675) and the planned comparison show the opposite; Table 2 prints Power's mean as .469 (Universalism's value); see TR0-SOC-02.

## Simulations (SIM-TR-SOC-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 4/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `b1c014a2` | Monte Carlo power at P99's group sizes for a Security-sized effect (eta^2 .003): below .80? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `4130508e` | Monte Carlo power for a Universalism-sized effect (eta^2 .037): above .99? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `d7c69481` | P99's G*Power statements (.96, .96, .99, .92, .49): do they reproduce, and are the Universalism and Benevolence group means ordered prosocial > individualist > competitor? | V1 Pass; H1 Supported; H2 Supported; H3 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: TRA-SOC-03: power about 0.5 for a Security-sized effect.
- Pass 2: TRA-SOC-03 (Universalism-sized effect, iteration 2): power 1.00.
- Pass 3: TRA-SOC-04: G*Power values reproduce; Benevolence does not order the SVO groups as Universalism does.

## Unresolved
- Whether Table 2's Power .469 is a typo cannot be confirmed without data.
- Individualist-competitor differences not recomputed (SDs not printed).
