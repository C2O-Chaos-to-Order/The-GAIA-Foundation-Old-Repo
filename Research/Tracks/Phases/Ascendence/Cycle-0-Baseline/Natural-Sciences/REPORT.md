# Ascendence in the Natural Sciences — Cycle-0-Baseline (AS0)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: ascent as adaptive walks up fitness landscapes (P85); rugged landscapes make high peaks harder to reach, and peak height and basin size correlate positively.

## Claims (ledger: `claims/claims.csv`)
- **AS0-NAT-01** [P] P85 estimates the probability that adaptive walks (each step to a random fitter neighbour, ending at a peak) reach the highest 1, 5, 14 or 25% of peaks: it varies widely among six empirical landscapes, is generally comparable to or smaller than in Rough Mount Fuji landscapes of similar ruggedness, and falls with ruggedness (RMF P14% from 96.3% at sigma 0.5 to 26.4% at sigma 10; NK from 100% at K 0 to 24.8% at K 8; House of Cards about 25%); peak height and basin size correlate positively in every landscape (R_ph-bs 0.69-0.97) but this does not guarantee a large probability of reaching a high peak. *Operationalization:* NAT Ascendence = adaptive walks climbing a fitness landscape. *Sources:* P85. *Limits:* Empirical landscapes are a few protein/RNA systems; P85 notes P14% cannot be fairly compared with very few peaks (NK K 0-1). P85 also reports that a 1/28 chance calculation in the study it re-examines (Papkou et al.) was incorrect.
- **AS0-NAT-02** [P] On 6-site four-state landscapes (one walk from every genotype, 10 landscapes per type) the chance of reaching the top 14% of peaks fell with RMF ruggedness (0.84 at sigma 0.5, 0.32 at sigma 2, 0.21 at sigma 10), was 0.21 for House of Cards (P85: about 25%), exceeded 0.14 for every landscape type, and peak height correlated positively with basin size in every landscape (minimum r 0.43; mean 0.93 at sigma 0.5 falling to 0.49-0.50 for sigma 10 and HoC). NK K 4 gave 0.243 vs 0.252 at K 1, so the pre-registered 'lower at K 4' held only narrowly; in the seed-99 smoke test it went the other way (0.240 vs 0.202), and with about 10 peaks at K 1 'top 14%' is the global peak alone, so this comparison is not robust. *Operationalization:* NAT Ascendence = adaptive walks to high peaks. *Sources:* SIM-AS-NAT-0/iter-1#V1;SIM-AS-NAT-0/iter-1#H1;SIM-AS-NAT-0/iter-1#H2;SIM-AS-NAT-0/iter-1#H3;SIM-AS-NAT-0/iter-1#H4;SIM-AS-NAT-0/iter-1#H5. *Limits:* Much smaller landscapes than P85's 9 sites; model landscapes only; the NK K comparison is fragile and seed-dependent (disclosed).

## Simulations (SIM-AS-NAT-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 5/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `0446721e` | P85's adaptive walks on small landscapes (6 four-state sites, 4096 genotypes; 10 landscapes per type): does the chance of reaching the top 14% of peaks fall as RMF ruggedness sigma rises, sit near 25% for HoC, fall with NK K, exceed 14% everywhere, and do peak height and basin size correlate positively? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; H5 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Probability of reaching high peaks by adaptive walks and its dependence on ruggedness sourced (AS0-NAT-01); ruggedness trend, HoC level and positive peak-basin correlation reproduced on small landscapes; NK K comparison fragile (AS0-NAT-02).

## Unresolved
- P85's empirical landscapes and 9-site size not reproduced; supplementary figures not read.
- Competing reading (anagenesis / increase in complexity) not yet sourced.
