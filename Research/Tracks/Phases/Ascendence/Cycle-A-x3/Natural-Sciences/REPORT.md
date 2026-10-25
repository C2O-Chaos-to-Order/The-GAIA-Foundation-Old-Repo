# Ascendence in the Natural Sciences — Cycle-A-x3 (ASA)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P85's RMF values reproduce at its size; NK P14% is not monotone in K at 6 sites; HoC is size-independent but about 0.2.

## Claims (ledger: `claims/claims.csv`)
- **ASA-NAT-01** [P] P85 estimates the probability that adaptive walks (each step to a random fitter neighbour, ending at a peak) reach the highest 1, 5, 14 or 25% of peaks: it varies widely among six empirical landscapes, is generally comparable to or smaller than in Rough Mount Fuji landscapes of similar ruggedness, and falls with ruggedness (RMF P14% from 96.3% at sigma 0.5 to 26.4% at sigma 10; NK from 100% at K 0 to 24.8% at K 8; House of Cards about 25%); peak height and basin size correlate positively in every landscape (R_ph-bs 0.69-0.97) but this does not guarantee a large probability of reaching a high peak. *Operationalization:* NAT Ascendence = adaptive walks climbing a fitness landscape. *Sources:* P85. *Limits:* Empirical landscapes are a few protein/RNA systems; P85 notes P14% cannot be fairly compared with very few peaks (NK K 0-1). P85 also reports that a 1/28 chance calculation in the study it re-examines (Papkou et al.) was incorrect.
- **ASA-NAT-02** [P] On 6-site four-state landscapes (one walk from every genotype, 10 landscapes per type) the chance of reaching the top 14% of peaks fell with RMF ruggedness (0.84 at sigma 0.5, 0.32 at sigma 2, 0.21 at sigma 10), was 0.21 for House of Cards (P85: about 25%), exceeded 0.14 for every landscape type, and peak height correlated positively with basin size in every landscape (minimum r 0.43; mean 0.93 at sigma 0.5 falling to 0.49-0.50 for sigma 10 and HoC). NK K 4 gave 0.243 vs 0.252 at K 1, so the pre-registered 'lower at K 4' held only narrowly; in the seed-99 smoke test it went the other way (0.240 vs 0.202), and with about 10 peaks at K 1 'top 14%' is the global peak alone, so this comparison is not robust. *Operationalization:* NAT Ascendence = adaptive walks to high peaks. *Sources:* SIM-AS-NAT-0/iter-1#V1;SIM-AS-NAT-0/iter-1#H1;SIM-AS-NAT-0/iter-1#H2;SIM-AS-NAT-0/iter-1#H3;SIM-AS-NAT-0/iter-1#H4;SIM-AS-NAT-0/iter-1#H5. *Limits:* Much smaller landscapes than P85's 9 sites; model landscapes only; the NK K comparison is fragile and seed-dependent (disclosed).
- **ASA-NAT-03** [P] At P85's own size (9 four-state sites, 262,144 genotypes) the agent's walks reproduce P85's RMF values: P14% 0.963 at sigma 0.5 (P85: 96.3%) and 0.221 at sigma 10 (P85: 26.4%, within the pre-registered 0.10); House of Cards gave 0.216, inside the 0.15-0.35 band but below P85's 'about 25%'. *Operationalization:* NAT Ascendence = adaptive walks to high peaks. *Sources:* SIM-AS-NAT-A/iter-1#V1;SIM-AS-NAT-A/iter-1#H1;SIM-AS-NAT-A/iter-1#H2;SIM-AS-NAT-A/iter-1#H3. *Limits:* Two landscapes per type; model landscapes only; P85's supplementary figures not read.
- **ASA-NAT-04** [P] With 30 NK landscapes per K (6 four-state sites), P14% was 1 at K 0 (one peak), then 0.249, 0.269, 0.277, 0.253 and 0.203 for K 1-5: lower at K 5 than K 2 as pre-registered, but the fall over K 2-5 was not supported as monotone (K 3 above K 2). The AS0 'lower at K 4 than K 1' result (AS0-NAT-02) is thus not a stable trend at this size: P14% peaks at intermediate K before falling, and the global-peak probability falls steadily (0.24 to 0.008). *Operationalization:* NAT Ascendence = adaptive walks on NK landscapes. *Sources:* SIM-AS-NAT-A/iter-2#V1;SIM-AS-NAT-A/iter-2#H1;SIM-AS-NAT-A/iter-2#H2;SIM-AS-NAT-A/iter-2#H3. *Limits:* 6 sites, not P85's 9; P85 warns that K 0-1 are not fairly comparable.
- **ASA-NAT-05** [P] On House of Cards landscapes of 5, 6, 7 and 8 four-state sites, P14% was 0.195, 0.198, 0.218 and 0.214: within 0.15-0.35 at every size and varying by only 0.023, consistent with P85's statement that the number of sites has minimal impact, though about 0.2 rather than P85's 'about 25%'. *Operationalization:* NAT Ascendence = adaptive walks on maximally rugged landscapes. *Sources:* SIM-AS-NAT-A/iter-3#V1;SIM-AS-NAT-A/iter-3#H1;SIM-AS-NAT-A/iter-3#H2. *Limits:* Sizes 5-8 only (P85: 5-10); five landscapes per size.

## Simulations (SIM-AS-NAT-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 7/8)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `dc5ad3a3` | P85 at its own size: with 9 four-state sites (262,144 genotypes; 2 landscapes per type, one walk from every genotype), is P14% within 0.10 of P85's printed 96.3% (RMF sigma 0.5) and 26.4% (sigma 10), and between 0.15 and 0.35 for HoC? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 2 | `7da35a5f` | The fragile AS0 NK comparison with 30 landscapes per K (6 sites): does P14% fall from K 2 to K 5, monotonically, and is K 0 single-peaked? | V1 Pass; H1 Supported; H2 Not supported; H3 Supported; R1 Reported |
| 3 | `385bb374` | P85's statement that HoC P14% is 'always around 25%' whatever the number of sites: is mean P14% between 0.15 and 0.35 at 5, 6, 7 and 8 four-state sites, with a range below 0.08? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: Search logged; hits were taxon-specific anagenesis case studies, not read. ASA-NAT-03: P85's RMF values reproduced at P85's size.
- Pass 2: ASA-NAT-04: NK P14% not monotone in K at 6 sites; AS0's K comparison not a stable trend.
- Pass 3: ASA-NAT-05: HoC P14% about 0.2 at 5-8 sites, size-independent.

## Unresolved
- P85's empirical landscapes not reproduced; HoC level about 0.2 vs P85's 25% unexplained.
- Competing reading (anagenesis / complexity) still unsourced.
