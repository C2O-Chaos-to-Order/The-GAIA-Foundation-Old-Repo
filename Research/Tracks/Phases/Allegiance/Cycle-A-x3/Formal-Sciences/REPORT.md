# Allegiance in the Formal Sciences — Cycle-A-x3 (ALA)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: the 1/3 rule holds within 1% at N = 1000 and weak selection; AL0's miss came from selection strength, and a 4% finite-N gap remains at N = 100.

## Claims (ledger: `claims/claims.csv`)
- **ALA-FOR-01** [E] P47 states five mechanisms under which natural selection can favour cooperation, each a benefit-to-cost threshold: kin selection r > c/b, direct reciprocity w > c/b, indirect reciprocity q > c/b, network reciprocity b/c > k, group selection b/c > 1 + n/m; for reciprocity, Table 1 adds stricter thresholds for risk-dominance and advantageousness, and the latter links to the '1/3 rule', which P47 says holds in the limit of weak selection. *Operationalization:* FOR Allegiance = cooperation stabilised by a mechanism. *Sources:* P47. *Limits:* Author manuscript of a short review; each rule is derived in a simplified model, and P47's 1/3 rule is stated only for weak selection.
- **ALA-FOR-02** [P] Numerically solving P47's Table 1 matrices (w = q = r = 0.5, k = 4, n = 10, m = 20) reproduced every printed threshold exactly (ESS/RD/AD b/c = 2, 3, 4 for reciprocity). In a Moran process (N = 100, selection 0.005) the fixation probability of tit-for-tat in always-defect was below 1/N at b/c = 3.5 (0.00947) and above at 4.5 (0.01019), as the 1/3 rule predicts, but the crossing was at b/c 4.23, not within 5% of 4: the finite-N prediction is not supported at N = 100 (expected from the smoke test). *Operationalization:* FOR Allegiance = cooperation thresholds. *Sources:* SIM-AL-FOR-0/iter-1#V1;SIM-AL-FOR-0/iter-1#V2;SIM-AL-FOR-0/iter-1#H1;SIM-AL-FOR-0/iter-1#H2. *Limits:* The 1/3 rule is a large-N weak-selection limit; finite-N correction not sourced. Stochastic check at N = 20 matched the exact formula (0.0531 vs 0.0515).
- **ALA-FOR-03** [P] With N = 1000 and weak selection (s = 0.00005) the fixation probability of tit-for-tat crosses 1/N at b/c = 4.02 for w = 0.5 (P47's AD threshold 4) and at 1.753 for w = 0.8 (threshold 1.75), within 1% in both; P47's printed thresholds were again reproduced exactly for all five mechanisms at the new parameters. *Operationalization:* FOR Allegiance = 1/3 rule at large N and weak selection. *Sources:* SIM-AL-FOR-A/iter-1#V1;SIM-AL-FOR-A/iter-1#V2;SIM-AL-FOR-A/iter-1#H1;SIM-AL-FOR-A/iter-1#H2;SIM-AL-FOR-A/iter-2#V1;SIM-AL-FOR-A/iter-2#V2;SIM-AL-FOR-A/iter-2#H1;SIM-AL-FOR-A/iter-2#H2. *Limits:* Expected from the agent's weak-selection formula (not from a source read in this track).
- **ALA-FOR-04** [P] At N = 100 with weak selection (N s = 0.005) the crossing was b/c = 4.159, within 5% of 4 (AL0 with N s = 0.5 gave 4.23, outside): AL0's miss came mostly from selection strength, and the remaining 4% gap matches the finite-N weak-selection value (4N - 5)/(N - 5) = 4.158. *Operationalization:* FOR Allegiance = finite-N 1/3 rule. *Sources:* SIM-AL-FOR-A/iter-3#V1;SIM-AL-FOR-A/iter-3#V2;SIM-AL-FOR-A/iter-3#H1;SIM-AL-FOR-A/iter-3#H2. *Limits:* The finite-N formula is the agent's, not sourced.

## Simulations (SIM-AL-FOR-A; 3 iteration(s), spec-first; validation 6/6, hypotheses supported 6/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `88e25836` | 1/3 rule at larger N and weaker selection (N = 1000, s = 0.00005, w = 0.5): does the crossing of rho = 1/N move to within 5% of P47's AD threshold 4? | V1 Pass; V2 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `7f590518` | Same at w = 0.8 (AD threshold 1.75), N = 1000, s = 0.00005: do the numerical thresholds still equal P47's printed rules and does the crossing fall within 5% of 1.75? | V1 Pass; V2 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `eb3ca00a` | Disentangling N from selection strength: N = 100 as in AL0 but weak selection s = 0.00005 (N s = 0.005): is the crossing now within 5% of 4? | V1 Pass; V2 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: ALA-FOR-03: at N = 1000 and weak selection the crossing is within 1% of P47's thresholds (w = 0.5 and 0.8); no new search (disclosed).
- Pass 2: ALA-FOR-04: at N = 100 with weak selection the crossing (4.159) is within 5%; AL0's miss was mostly selection strength.
- Pass 3: Added nothing: no source on the finite-N correction or on non-reciprocity mechanisms was searched or read.

## Unresolved
- Finite-N weak-selection formula still unsourced.
- Non-reciprocity mechanisms (kin, network, group) only checked as printed thresholds.
