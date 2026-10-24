# Insurgence in the Philosophy Spirituality — Cycle-A-x3 (INA)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: P30's group-competition model gives logistic spread of a preferred stance (a = 1), a critical mass when conformity is strong (a > 1), and a delay, not a block, from cliques; read interpretively as spreading rather than originating the new.

## Claims (ledger: `claims/claims.csv`)
- **INA-PHI-02** [P] In a Chinese-restaurant process with concentration 5, distinct forms kept appearing (26.8 after 1,000 draws, 37.7 after 10,000, 49.7 after 100,000; analytic 27.0, 38.5, 50.0) while the rate of new forms fell to 0.00005 per draw: novelty continues but slows logarithmically. *Operationalization:* PHI Insurgence = continuing emergence of new forms. *Sources:* SIM-IN-PHI-0/iter-1#V1;SIM-IN-PHI-0/iter-1#H1;SIM-IN-PHI-0/iter-1#H2. *Limits:* Formal stand-in only; it does not test Bergson's thesis.
- **INA-PHI-03** [P] P30 fits a two-group competition model (dx/dt = y P_yx - x P_xy, P_yx = c x^a u_x) to census data on religious non-affiliation in 85 regions; a broad error minimum near a = 1 gives logistic growth with rate c(2u_x - 1), and the fits indicate higher perceived utility for non-affiliation, from which P30's model predicts that religion will be driven toward extinction in those societies. *Operationalization:* PHI Insurgence = growth of a once-marginal stance by conversion. *Sources:* P30. *Limits:* The prediction is conditional on the model and on constant utilities (P30 notes abrupt utility changes are excluded); supplementary analyses not read; journal version not read.
- **INA-PHI-05** [P] With a = 1 and u = 0.65 a 1% minority reached 50% at t = 15.3 (logistic rate 0.3, RK4 within 1e-6). With a = 1.5 and u = 0.6 an unstable interior point appeared at x = 0.308: minorities starting at 5% and 20% died out despite their higher utility, while 40% and 60% took over. With strong conformity a preferred stance still needs a critical mass. *Operationalization:* PHI Insurgence = critical mass for a new stance. *Sources:* SIM-IN-PHI-A/iter-1#V1;SIM-IN-PHI-A/iter-1#H1;SIM-IN-PHI-A/iter-2#V1;SIM-IN-PHI-A/iter-2#H1;SIM-IN-PHI-A/iter-2#H2. *Limits:* a = 1.5 illustrative; P30's data favoured a near 1.
- **INA-PHI-06** [P] In a mean-field two-clique version of P30's experiment (minority clique of 10%, out-group weight p) the time to reach 50% grew from 11.0 at p = 1 to 39.0 at p = 0.001, linear in -ln p/(2u - 1) (r^2 = 0.995, slope 0.79), consistent with P30's reported delay d ~ -ln p/(2u - 1): cliques delay the spread of a stance but do not stop it. *Operationalization:* PHI Insurgence = spread out of a clique. *Sources:* SIM-IN-PHI-A/iter-3#V1;SIM-IN-PHI-A/iter-3#H1. *Limits:* Not P30's N = 500 stochastic network; slope not compared with P30 (P30 gives proportionality only).
- **INA-PHI-01** [PS] Bergson, as presented in P08, argues for an original common impulse, the vital impulse (élan vital), that explains the creation of all living species, together with a principle of divergence and differentiation; read in this track, the vital impulse is a philosophical account of insurgence as the upsurge of the new. *Operationalization:* PHI Insurgence = the upsurge of the new from a common impulse. *Sources:* P08. *Limits:* Metaphysical thesis; the 'insurgence' reading is the track's interpretation.
- **INA-PHI-04** [PS] Read philosophically, P30's model treats the rise or decline of a religious or irreligious stance as conversion driven by group size and perceived utility; it says nothing about the truth of either stance, and its 'extinction' result holds only for constant utilities. Set beside Bergson's vital impulse (P08), it is a mechanical account of how a new stance spreads, not of where the new comes from. *Operationalization:* PHI Insurgence = spreading versus originating the new. *Sources:* P30;P08. *Limits:* Interpretation by this track; neither source frames its claim as insurgence.

## Simulations (SIM-IN-PHI-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 4/4)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `c66d755d` | P30's group-competition model with a = 1 (PHI pass 2): with utility u = 0.65 for the unaffiliated (P30's collapse value) and x0 = 0.01, does the solution follow the logistic with rate c(2u - 1), and pass 0.5 by t = 20? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `4697f0eb` | P30's model with a = 1.5 (PHI pass 2): an interior unstable fixed point appears; does a minority with the higher utility (u = 0.6) decline if it starts below it and rise if above? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `f7d2ecc1` | P30's two-clique result (PHI pass 3): in a mean-field two-cluster version (sizes 0.1 and 0.9, out-group weight p), is the delay to x = 0.5 linear in -ln p/(2u - 1) as P30 reports? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: INA-PHI-03 (P30's model and its fit to 85 regions) and INA-PHI-04 (interpretive: spreading versus originating the new, PS).
- Pass 2: INA-PHI-05: logistic case reproduced; with a = 1.5 a preferred stance needs a critical mass.
- Pass 3: INA-PHI-06: cliques delay but do not stop the spread (delay linear in -ln p, as P30 reports).

## Unresolved
- P30 supplementary analyses (fixed-point proofs, error minimum, delay formula) not read.
- No theological source on revival or conversion read; P30's 'extinction' is model-conditional.
