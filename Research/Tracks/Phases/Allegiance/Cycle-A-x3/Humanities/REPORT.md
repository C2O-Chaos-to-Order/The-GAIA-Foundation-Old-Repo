# Allegiance in the Humanities — Cycle-A-x3 (ALA)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: without P50's prestige gap the USA flow would reverse; in P30's form survival fades continuously as conformity rises.

## Claims (ledger: `claims/claims.csv`)
- **ALA-HUM-01** [P] P50 fits language-competition models with prestige and bilingualism to public population data for six bilingual cases (e.g. Gaelic-English 1891-1971, Welsh-English 1901-2001); Bayes factors favour the model with bilingualism, which decelerates the shift from minority to majority language, and in the four unequal-prestige cases the majority language has higher prestige (e.g. Spanish-English in the USA, s2 = 1.2553 > s1 = 0.0691). *Operationalization:* HUM Allegiance = language loyalty under prestige pressure. *Sources:* P50. *Limits:* Six cases; model rates are estimates; P50 has small slips (cites figure 1a for results in figure 2; 'minority Catalonia').
- **ALA-HUM-02** [P] Plugging P50's reported rates into its constant-rate Eq. 4.4 gives positive minority equilibria in all four unequal-prestige cases (Canada 0.186, USA 0.081, Wales 0.018, Scotland 0.061), and the prestige-weighted flow runs minority-to-majority in each (USA 0.134 vs 0.012, although r12 < r21); by contrast, in P30's exponent form the weaker group survives only for a < 1 (0.31 at a = 0.5, 0 at a = 1 and 1.31). *Operationalization:* HUM Allegiance = persistence of a minority language. *Sources:* SIM-AL-HUM-0/iter-1#V1;SIM-AL-HUM-0/iter-1#H1;SIM-AL-HUM-0/iter-1#H2;SIM-AL-HUM-0/iter-1#H3. *Limits:* Agent's simplification: rates estimated in P50's bilingual model are used in a model without bilinguals; not a re-fit.
- **ALA-HUM-03** [P] Counterfactual: giving both languages the same prestige (the mean of P50's two values) raises the minority equilibrium in every case (Canada 0.19 to 0.41, Wales 0.02 to 0.22, Scotland 0.06 to 0.07) and in the USA reverses the flow (majority-to-minority 0.114 vs 0.071; Spanish equilibrium 0.62), so the minority-to-majority prediction is not supported in every case: in P50's rates the USA shift is driven by prestige, not by the transition rates. *Operationalization:* HUM Allegiance = language loyalty without a prestige gap. *Sources:* SIM-AL-HUM-A/iter-1#V1;SIM-AL-HUM-A/iter-1#H1;SIM-AL-HUM-A/iter-1#H2;SIM-AL-HUM-A/iter-1#H3. *Limits:* Counterfactual in the agent's simplified model without bilinguals; not a forecast.
- **ALA-HUM-04** [P] In P30's form at status 0.3 the weaker group kept 0.24 at a = 0.25 but only 0.033 at a = 0.75 and vanished at a = 1.5 and 2: the AL0 rule 'coexistence for a < 1' is not supported at the 0.05 level near a = 1, because the surviving share shrinks continuously as a approaches 1. *Operationalization:* HUM Allegiance = minority persistence in the exponent form. *Sources:* SIM-AL-HUM-A/iter-2#V1;SIM-AL-HUM-A/iter-2#H1;SIM-AL-HUM-A/iter-2#H2;SIM-AL-HUM-A/iter-2#H3. *Limits:* Deterministic; the 0.05 coexistence threshold is the agent's.
- **ALA-HUM-05** [P] Replication with step 0.001: the Eq. 4.4 equilibria (0.186, 0.081, 0.018, 0.061) and the exponent-form results are unchanged. *Operationalization:* HUM Allegiance = persistence of a minority language (replication). *Sources:* SIM-AL-HUM-A/iter-3#V1;SIM-AL-HUM-A/iter-3#H1;SIM-AL-HUM-A/iter-3#H2;SIM-AL-HUM-A/iter-3#H3. *Limits:* Numerical replication only.

## Simulations (SIM-AL-HUM-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 7/9)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `d4047dcf` | Counterfactual equal prestige: if each case's two prestige values were replaced by their mean (as P50 found for Montreal and Catalonia), does the flow still run minority-to-majority in every case? | V1 Pass; H1 Supported; H2 Not supported; H3 Supported; R1 Reported |
| 2 | `f36a7494` | P30 form at a lower status of the weaker group (u_x = 0.3) with exponents 0.25, 0.75, 1.5, 2: does coexistence for a < 1 and extinction for a >= 1 still hold (cases as AL0)? | V1 Pass; H1 Supported; H2 Supported; H3 Not supported; R1 Reported |
| 3 | `c05cecb2` | Numerical replication with step 0.001 and the AL0 cases: are the Eq. 4.4 equilibria unchanged? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: ALA-HUM-03: equal-prestige counterfactual reverses the USA flow; no new search (disclosed).
- Pass 2: ALA-HUM-04: in P30's form the surviving share shrinks continuously as a approaches 1.
- Pass 3: Added nothing new: numerical replication (ALA-HUM-05); no literary or historical source on allegiance was searched.

## Unresolved
- Rates from P50's bilingual model used without bilinguals; SI not read.
- No literary or historical source on allegiance.
