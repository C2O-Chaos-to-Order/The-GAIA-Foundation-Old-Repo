# Ascendence in the Applied Sciences — Cycle-0-Baseline (AS0)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: ascent rate and mountain sickness (P88); faster ascent, more severe AMS; the 'odds' wording of the 2.069 counterfactual is a risk ratio.

## Claims (ledger: `claims/claims.csv`)
- **AS0-APP-02** [E] P88's odds ratios, counts and test statistics reproduce (exp(1.14) = 3.127, exp(-1.82) = 0.162; 78 = 48 + 28 + 2; chi-square p 0.038, 0.0155, 8e-5; SpO2 t p 0.2245). Model-4 point estimates with natural logs give P(moderate or severe) 0.873 for one day and 0.417 for three days, a risk ratio of 2.095 against the printed 2.069 (log10 gives 1.78), so 2.069 is a risk (probability) ratio; the corresponding odds ratio is 9.6, so the Fig. 2 wording 'odds ... increase twofold (2.069)' is not supported. *Operationalization:* APP Ascendence = auditing an ascent-rate study. *Sources:* SIM-AS-APP-0/iter-1#V1;SIM-AS-APP-0/iter-1#H1;SIM-AS-APP-0/iter-1#H2;SIM-AS-APP-0/iter-1#H3;SIM-AS-APP-0/iter-1#H4;SIM-AS-APP-0/iter-1#H5. *Limits:* Point estimates rather than P88's posterior; the natural-log reading of '(Log)' is the agent's assumption.
- **AS0-APP-01** [P] Among 105 travellers treated for high-altitude illness at Mustang district hospital (Nepal), 74% had acute mountain sickness (61% mild, 36% moderate, 3% severe); in a Bayesian ordered logistic model of severity (None, Mild, Moderate or Severe), faster ascent rate (km/day) was associated with greater severity (coefficient 1.14, odds ratio 3.13) and smoking with less (odds ratio 0.16). P88's counterfactual says a 1-day Pokhara-Muktinath trip (2978 m gain) doubles the risk of moderate or severe AMS compared with 3 days. *Operationalization:* APP Ascendence = ascent to altitude and ascent rate. *Sources:* P88. *Limits:* Hospital register sample (P88 notes selection by Thorong La and airlift of severe cases); one site; credible intervals reported as 99% for headline effects. P88 calls the 2.069 counterfactual 'odds' in Fig. 2 and 'risk' in the abstract; see AS0-APP-02.

## Simulations (SIM-AS-APP-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 4/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `5d3347b9` | P88's ordered-logit results: do exp(B) give the printed odds ratios, do percentages give whole counts, do the printed test statistics give the stated p-values, and does model 4 reproduce the 2.069 counterfactual for a 1-day vs 3-day Pokhara-Muktinath ascent, and as which quantity (risk ratio or odds ratio)? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; H5 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Ascent rate and AMS severity sourced (AS0-APP-01); audit: statistics reproduce; the 2.069 counterfactual is a risk ratio, not odds (AS0-APP-02).

## Unresolved
- P88's posterior draws are not available; the 2.069 vs 2.095 gap is attributed to posterior averaging (not verified).
- Experimental (randomised) ascent-rate evidence not yet read.
