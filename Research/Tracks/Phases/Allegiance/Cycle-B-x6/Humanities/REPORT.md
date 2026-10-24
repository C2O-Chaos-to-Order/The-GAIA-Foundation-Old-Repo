# Allegiance in the Humanities — Cycle-B-x6 (ALB)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: mostly variants; equilibria depend only on rate ratios, and survival near a = 1 is tiny.

## Claims (ledger: `claims/claims.csv`)
- **ALB-HUM-01** [P] P50 fits language-competition models with prestige and bilingualism to public population data for six bilingual cases (e.g. Gaelic-English 1891-1971, Welsh-English 1901-2001); Bayes factors favour the model with bilingualism, which decelerates the shift from minority to majority language, and in the four unequal-prestige cases the majority language has higher prestige (e.g. Spanish-English in the USA, s2 = 1.2553 > s1 = 0.0691). *Operationalization:* HUM Allegiance = language loyalty under prestige pressure. *Sources:* P50. *Limits:* Six cases; model rates are estimates; P50 has small slips (cites figure 1a for results in figure 2; 'minority Catalonia').
- **ALB-HUM-02** [P] Plugging P50's reported rates into its constant-rate Eq. 4.4 gives positive minority equilibria in all four unequal-prestige cases (Canada 0.186, USA 0.081, Wales 0.018, Scotland 0.061), and the prestige-weighted flow runs minority-to-majority in each (USA 0.134 vs 0.012, although r12 < r21); by contrast, in P30's exponent form the weaker group survives only for a < 1 (0.31 at a = 0.5, 0 at a = 1 and 1.31). *Operationalization:* HUM Allegiance = persistence of a minority language. *Sources:* SIM-AL-HUM-0/iter-1#V1;SIM-AL-HUM-0/iter-1#H1;SIM-AL-HUM-0/iter-1#H2;SIM-AL-HUM-0/iter-1#H3. *Limits:* Agent's simplification: rates estimated in P50's bilingual model are used in a model without bilinguals; not a re-fit.
- **ALB-HUM-03** [P] Counterfactual: giving both languages the same prestige (the mean of P50's two values) raises the minority equilibrium in every case (Canada 0.19 to 0.41, Wales 0.02 to 0.22, Scotland 0.06 to 0.07) and in the USA reverses the flow (majority-to-minority 0.114 vs 0.071; Spanish equilibrium 0.62), so the minority-to-majority prediction is not supported in every case: in P50's rates the USA shift is driven by prestige, not by the transition rates. *Operationalization:* HUM Allegiance = language loyalty without a prestige gap. *Sources:* SIM-AL-HUM-A/iter-1#V1;SIM-AL-HUM-A/iter-1#H1;SIM-AL-HUM-A/iter-1#H2;SIM-AL-HUM-A/iter-1#H3. *Limits:* Counterfactual in the agent's simplified model without bilinguals; not a forecast.
- **ALB-HUM-04** [P] In P30's form at status 0.3 the weaker group kept 0.24 at a = 0.25 but only 0.033 at a = 0.75 and vanished at a = 1.5 and 2: the AL0 rule 'coexistence for a < 1' is not supported at the 0.05 level near a = 1, because the surviving share shrinks continuously as a approaches 1. *Operationalization:* HUM Allegiance = minority persistence in the exponent form. *Sources:* SIM-AL-HUM-A/iter-2#V1;SIM-AL-HUM-A/iter-2#H1;SIM-AL-HUM-A/iter-2#H2;SIM-AL-HUM-A/iter-2#H3. *Limits:* Deterministic; the 0.05 coexistence threshold is the agent's.
- **ALB-HUM-05** [P] Replication with step 0.001: the Eq. 4.4 equilibria (0.186, 0.081, 0.018, 0.061) and the exponent-form results are unchanged. *Operationalization:* HUM Allegiance = persistence of a minority language (replication). *Sources:* SIM-AL-HUM-A/iter-3#V1;SIM-AL-HUM-A/iter-3#H1;SIM-AL-HUM-A/iter-3#H2;SIM-AL-HUM-A/iter-3#H3. *Limits:* Numerical replication only.
- **ALB-HUM-06** [P] In P50's model the minority's equilibrium depends only on the ratio of rates: halving all rates leaves it unchanged; doubling the majority's prestige lowers it to 0.10, 0.04, 0.009, 0.03 (Wales below 0.01: not supported as surviving); raising the minority's prestige to the majority's raises it to 0.41, 0.62, 0.22, 0.07, and in the USA the flow then reverses (not supported in every case). *Operationalization:* HUM Allegiance = language loyalty and prestige. *Sources:* SIM-AL-HUM-B/iter-1#V1;SIM-AL-HUM-B/iter-1#H1;SIM-AL-HUM-B/iter-1#H2;SIM-AL-HUM-B/iter-1#H3;SIM-AL-HUM-B/iter-2#V1;SIM-AL-HUM-B/iter-2#H1;SIM-AL-HUM-B/iter-2#H2;SIM-AL-HUM-B/iter-2#H3;SIM-AL-HUM-B/iter-6#V1;SIM-AL-HUM-B/iter-6#H1;SIM-AL-HUM-B/iter-6#H2;SIM-AL-HUM-B/iter-6#H3. *Limits:* Counterfactuals in the agent's model without bilinguals.
- **ALB-HUM-07** [P] In P30's exponent form near a = 1 the weaker group keeps 0.017 at a = 0.9 and 0.0003 at a = 0.95 and vanishes above 1, so coexistence above 0.05 for a < 1 is not supported near the threshold; at status 0.45 it keeps 0.40 at a = 0.5; a coarse step (0.05) reproduces the equilibria. *Operationalization:* HUM Allegiance = minority persistence near the conformity threshold. *Sources:* SIM-AL-HUM-B/iter-3#V1;SIM-AL-HUM-B/iter-3#H1;SIM-AL-HUM-B/iter-3#H2;SIM-AL-HUM-B/iter-3#H3;SIM-AL-HUM-B/iter-4#V1;SIM-AL-HUM-B/iter-4#H1;SIM-AL-HUM-B/iter-4#H2;SIM-AL-HUM-B/iter-4#H3;SIM-AL-HUM-B/iter-5#V1;SIM-AL-HUM-B/iter-5#H1;SIM-AL-HUM-B/iter-5#H2;SIM-AL-HUM-B/iter-5#H3. *Limits:* Deterministic toy; threshold 0.05 the agent's.

## Simulations (SIM-AL-HUM-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 15/18)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `f9f3fb59` | Doubling the majority's prestige: how much lower are the minority equilibria? | V1 Pass; H1 Not supported; H2 Supported; H3 Supported; R1 Reported |
| 2 | `10a2b746` | Halving all transition rates: are the equilibria unchanged (only the ratio matters)? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 3 | `ce026429` | P30 form near symmetric status (u_x 0.45). | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 4 | `067933ee` | Coarse step (dt 0.05): does Euler integration still reach the equilibria within 1e-3? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 5 | `142dc301` | P30 form with exponents just around 1 (0.9, 0.95, 1.05, 1.1). | V1 Pass; H1 Supported; H2 Supported; H3 Not supported; R1 Reported |
| 6 | `dbeb5d3b` | Equalizing the minority's prestige to the majority's (s1 = s2 = majority value). | V1 Pass; H1 Supported; H2 Not supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: ALB-HUM-06: doubling the majority's prestige drives Wales below 0.01; no new HUM source read (disclosed).
- Pass 2: Added nothing: halving all rates leaves the equilibria unchanged, as the model implies.
- Pass 3: Added nothing: status 0.45 shifts the exponent-form share as expected (0.40 at a = 0.5).
- Pass 4: Added nothing: coarse Euler step reproduces the equilibria.
- Pass 5: ALB-HUM-07: the surviving share is 0.017 at a = 0.9 and 0.0003 at a = 0.95.
- Pass 6: ALB-HUM-06: equal prestige raises minority equilibria to 0.07-0.62 and reverses the USA flow.

## Unresolved
- No literary or historical source on allegiance; P50's SI not read.
