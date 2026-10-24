# Allegiance in the Natural Sciences — Cycle-0-Baseline (AL0)

Phase report: Allegiance (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: allegiance as cooperative binding (P46): bonds that make further bonds likelier give a curved Hill plot with maximal cooperativity at half-saturation; an Adair toy reproduces it.

## Claims (ledger: `claims/claims.csv`)
- **AL0-NAT-01** [E] Cooperative binding is described by the Hill equation Y = L^n/(Kd + L^n), with Kd = P50^n, and the Hill coefficient n is the slope of the Hill plot log(Y/(1-Y)) vs log L; for haemoglobin a fit gives n = 2.8, but the real Hill plot is curvilinear: its ends approach slope 1 and its slope is highest in the middle, so cooperativity is maximal near half-saturation. *Operationalization:* NAT Allegiance = cooperative binding (each bond makes the next more likely). *Sources:* P46. *Limits:* Textbook page; the Hill equation is an approximation (P46 notes it is not a mechanism). P46 contains a slip ('log 1 = log 100 = 0') and typos; reading binding as 'allegiance' is this track's operationalization.
- **AL0-NAT-02** [P] A four-site Adair model with stepwise constants rising 100-fold (0.02, 0.05, 0.2, 2.0) reproduced P46's qualitative Hill plot: end slopes 1.0001, maximal slope 3.63 at log L = 0.883, 0.03 log units from half-saturation (0.853); independent sites gave slope 1.000 throughout, and the Hill equation gave Y = 0.5 at P50 with Kd = P50^n. *Operationalization:* NAT Allegiance = cooperative binding. *Sources:* SIM-AL-NAT-0/iter-1#V1;SIM-AL-NAT-0/iter-1#H1;SIM-AL-NAT-0/iter-1#H2;SIM-AL-NAT-0/iter-1#H3. *Limits:* Constants are the agent's choice, not haemoglobin data; Adair's polynomial is standard theory not stated in P46.

## Simulations (SIM-AL-NAT-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 3/3)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `d6903587` | Cooperative binding (P46): does a 4-site binding model with affinity rising as sites fill give a curved Hill plot whose ends approach slope 1 and whose slope is greatest (between 1 and 4) near half-saturation, while independent sites give slope 1 throughout? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Cooperative binding and the curvilinear Hill plot sourced (AL0-NAT-01); Adair-model check of P46's qualitative claims (AL0-NAT-02).

## Unresolved
- Mechanistic models of cooperativity (MWC, KNF) not sourced; Adair constants are illustrative.
- Other physical 'allegiance' senses (bonding, synchronisation) not covered.
