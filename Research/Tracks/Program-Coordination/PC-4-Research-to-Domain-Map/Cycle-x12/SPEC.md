# PC-4 Cycle x12: Specification

Written and pushed **before** any x12 change and before the x12 run. Stacked on `research/pc4-x9` @ ade15958. Pre-registered checks: `config.json`. This is the last cycle. Expectation stated in advance: the map has largely converged, so most passes should confirm earlier results rather than change them.

## Passes (12)
1. **Fold the x9 scan proposals** into the cluster file: NEW-3 God and Lucifer (home KL-07), and G-07 joining b7.1.
2. **Source check, governance reports.** Read the ToG draft sections each ToG report covers and the Universal Regulation header (A-04), and confirm or change their homes.
3. **Gap check comparison.** Compare the map with `Research/GAP_CHECK_2026-10-24_TOTALITY.md` §1 (existing material per domain).
4. **Re-examine the 24 no-primary domains.** Should any report be re-homed to one of them?
5. **Cross-cutting domains.** Name the domains that apply to every report whatever its home (claims, records, public claims, portfolio), so they are not mistaken for gaps.
6. **One home per report.** Replication check that every report has exactly one primary (or NONE with a reason).
7. **Reverse map.** For each domain, the reports its domain report must read first (primary and secondary), from `coverage_domains.csv`.
8. **Owner decision list.** Every open decision PC-4 raises, in one place.
9. **Stability across matcher variants** (the 12 iterations).
10. **Drift since x9** (`primaries_changed_since_previous`).
11. **Adoption-boundary audit.** Mechanical: no file in the PC-4 folder shares a 120-character window with any suite file (checked against the external suite by the tool).
12. **Consolidation.** Write the final `MAP.md` at the track root from the x12 outputs, and update the track README.

## Iterations (12)
`charter`, `title_purpose` and `title` at k = 1, 3 and 5 with stemming (1–9), plus each variant at k = 3 without stemming (10–12). 500 permutations each.

## Pre-registered checks
| ID | Hypothesis | Metric | Test | Iterations |
|---|---|---|---|---|
| X12-1 | Inventory complete | inventory_gap | = 0 | all |
| X12-2 | Integrity | problems | = 0 | all |
| X12-3 | No queue-named domain missing | queue_named_missing | = 0 | all |
| X12-4 | Every cluster proposal passes | clusters_failed | = 0 | all |
| X12-5 | 12 cluster proposals (9 b7 + NEW-1–3) | n_clusters | = 12 | all |
| X12-6 | At most 3 primaries changed since x9 | primaries_changed_since_previous | ≤ 3 | all |
| X12-7 | No 120-character overlap with any suite file | boundary_overlaps | = 0 | all |
| X12-8 | Matcher beats chance at k = 3 | perm_p | ≤ 0.01 | 2, 5, 8, 10, 11, 12 |
| X12-9 | Reports with no domain ≤ 1 | reports_no_domain | ≤ 1 | all |
| X12-10 | ≤ 10 unclustered similar pairs after folding | similar_pairs_unclustered | ≤ 10 | all |
