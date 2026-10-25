# PC-4 Cycle x6: Specification

Written and pushed **before** any x6 change and before the x6 run. Stacked on `research/pc4-x3` @ 660e21b8. Pre-registered checks: `config.json`.

## Passes (6)
1. **Coverage-gap search in non-report work.** Map every update (§L), owner setting (§M a), gap (§M b), recommendation (§M c) and Afterwards item to domains (`../judgments/nonreport_x6.csv`). Report the domains with no work of any kind.
2. **b7 membership update for §N.** The b7 list predates §N (owner-approved 2026-10-25). Add §N items to the clusters they duplicate and re-test each single-home proposal. Propose new candidate clusters where §N creates a new overlap; these are labelled NEW-n and are proposals only.
3. **Dependency check.** For every domain that homes at least one report, list its register dependencies that have no report at all (`dependency_gaps`).
4. **ToG §6 alignment.** Map the 24 governance domains in the Totality of Governance draft §6 (in this repository) to the 45 TOT domains (`../judgments/tog24_x6.csv`). Report the TOT domains that no ToG domain reaches (`tog24_unreached`). This is the "24 ↔ 45" map that recommendation c4 asks PC-2 to hold; it is offered as input, not as PC-2.
5. **Sensitivity of the coverage lists** to the counting rule: primary only; primary or secondary; with candidates; with non-report work; excluding Hypothetical rows; open reports only.
6. **Label audit.** Re-read every Established reference and every Plausible basis; downgrade weak fits to Hypothetical with a reason.

## Rule refinement pre-registered here (from x3)
`named_examples`: PC-4, b8 and b9 name domains as examples or lists for *other* items. Their own-text domain names are excluded from `queue_named_missing`. This fixes the x3 X3-3 false positive. The x3 record keeps its FAIL.

## Iterations (6)
`charter` matcher: k = 1, 3 and 5, each with stemming on (iterations 1–3) and off (4–6).

## Pre-registered checks
| ID | Hypothesis | Metric | Test | Iterations |
|---|---|---|---|---|
| X6-1 | Inventory still complete | inventory_gap | = 0 | all |
| X6-2 | Every row passes integrity | problems | = 0 | all |
| X6-3 | No queue-named domain missing (with the example rule) | queue_named_missing | = 0 | all |
| X6-4 | 9 b7 proposals + 2 new candidate clusters pass | clusters_ok | = 11 | all |
| X6-5 | At most 1 domain has no work of any kind | domains_no_work_any | ≤ 1 | all |
| X6-6 | At least one dependency gap exists | dependency_gaps | ≥ 1 | all |
| X6-7 | At least 3 TOT domains are outside ToG §6 | tog24_unreached | ≥ 3 | all |
| X6-8 | Reports with no domain ≤ 1 | reports_no_domain | ≤ 1 | all |
| X6-9a/b/c | Matcher agreement ≥ 0.35 / 0.45 / 0.60 at k = 1 / 3 / 5 | topk_primary_rate | ≥ | 1,4 / 2,5 / 3,6 |

X6-5, X6-6 and X6-7 are predictions made before the passes. X6-4 fixes the number of new clusters at 2 in advance, so a third overlap found during pass 2 would fail it; it would be reported, not absorbed.
