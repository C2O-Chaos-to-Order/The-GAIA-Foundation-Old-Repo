# SIM-MR-1 — Conditional vs unconditional cooperation strategies (iterated prisoner's dilemma) — SPEC

Written before execution (2026-10-24T05:03:11Z). Params: `params.json` (hashed in EXECUTION_RECORD.json). Code: `../sim_mr.py`.

## What this is — and is not
A model of **cooperation strategies** in a repeated two-player game (PLAN.md method step 3). It is **not** a model of love, of persons, or of any tradition's meaning of agapē/mettā/bhakti. Any mapping from "ALLC" to "unconditional love" or from "TFT/GTFT" to "conditional love" is an analogy, labelled **Hypothetical** in the report, and nothing in the outputs tests that analogy.

## Model
- Stage game: prisoner's dilemma with T=5, R=3, P=1, S=0 (modelling choice satisfying T>R>P>S and 2R>T+S; the ordinal structure is as described in Z11 §1).
- 200 rounds. Execution noise ε: each intended move is flipped with probability ε.
- Strategies (memory-0/1, terminology as in Z03): ALLC (always cooperate — unconditional cooperation), ALLD (always defect), TFT (cooperate first, then copy partner's last move — conditional, Z11 §14.1), GTFT (like TFT, but after a partner defection cooperates with probability q = 1/3 — conditional but forgiving).
- Expected payoffs computed **exactly** by propagating the 4-state Markov chain of joint moves for 200 rounds; cross-checked by Monte Carlo (seed in params).
- Replicator dynamics (Euler, dt 0.05, 2000 steps) on the 4×4 average-payoff matrix at ε = 0.05 from equal initial shares.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | ε=0: ALLD vs ALLC mean payoff per round = 5 (ALLD) and 0 (ALLC) |
| V2 | validation | ε=0: TFT vs TFT = 3 per round; TFT vs ALLD = (0 + 199·1)/200 = 0.995 for TFT |
| V3 | validation | Exact Markov payoffs and Monte Carlo agree within 0.05 per round for every pair at ε=0.05 |
| H1 | hypothesis | ε=0, round-robin including ALLD (self-play included): ALLC has the lowest mean score of the three cooperative strategies (ALLC < TFT and ALLC < GTFT) |
| H2 | hypothesis | ε=0.05: TFT-vs-TFT mutual-cooperation rate < 0.60 while GTFT-vs-GTFT ≥ 0.80 |
| H3 | hypothesis | Replicator (ε=0.05, ALLD present): final ALLC share < 0.01 and combined TFT+GTFT share > 0.5 |
| H4 | hypothesis | ε=0, population without ALLD (ALLC, TFT, GTFT only): all three earn identical mean scores (|diff| < 1e-9) |
| H5 | hypothesis | ε=0.05, population without ALLD: ALLC's mean score is ≥ TFT's mean score |
| R1 | reporting | full 4×4 payoff matrices at each noise level |
| R2 | reporting | replicator trajectory end-state shares |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = may go either way (Supported / Not supported — a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits (stated in advance)
Four hand-picked strategies; one payoff set; one forgiveness parameter; well-mixed infinite-population replicator; no learning, kinship, reputation, partner choice, or exit. Results describe this model only.
