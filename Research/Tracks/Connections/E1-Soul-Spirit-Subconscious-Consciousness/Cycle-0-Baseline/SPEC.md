# Connection Baseline: specification

This specification, `config.json`, the tool `../tools/conn.py` and the judgment files `../judgments/*_c0.csv` were committed and pushed **before** the Baseline run. The method is in `../PLAN.md`.

## Sources read in full for the Baseline
- SSSC track: `FRAMEWORK.md`, `README.md`, `Cycle-D-x12/SUMMARY.md`, the four `Cycle-D-x12/<topic>/REPORT.md` (all 139 claims with their sources and limits), and `Cycle-D-x12/Links/link_register.csv` (TL-01 to TL-35).
- `Research/Tracks/Phases/SYNTHESIS.md`.
- `Research/README.md` §6–§9 and `Research/WORK_QUEUE.md` §E, §G and §L (owner wording).

Their SHA-256 hashes are in each EXECUTION_RECORD (`inputs.read_in_full`). The claim ledgers are used by the tool for IDs, labels, sources and cross-references; their extra columns are read in full in x3. The phase ledgers are used here only to resolve IDs and the Being placement. No new external source is added in this cycle.

## Pass 1 (agent judgment)
- `factors_c0.csv`: 11 factors (method, subject matter, tradition, ethics), one row per factor and topic. Each row names basis claims from **that topic's own** ledger.
- `claims_c0.csv`: 18 claims, CN0-01 to CN0-18, kinds shared, difference, unity, census, owner and framing. Census claims state a value the tool must reproduce. Owner claims quote the Work Queue verbatim.
- `links_c0.csv`: 17 topic-to-topic links, CL-01 to CL-17, in the `Research/README.md` §9.2 vocabulary plus `shared method` and `shared factor`. CL-02 carries the existing TL-08.

## Pass 2 (tool)
One iteration, rule `as_judged` (every judged factor row counts). Later cycles add `strict` (a factor row counts only with an Established or Plausible basis claim) and `established_only`.

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C0-1 | Sources read in full exist | missing_inputs | = 0 |
| C0-2 | Every basis ID resolves | dangling_basis | = 0 |
| C0-3 | Every source ID is in an existing register | unresolved_sources | = 0 |
| C0-4 | Every listed source is cited by a basis item | sources_not_in_basis | = 0 |
| C0-5 | No label above its weakest ranked basis | label_rule_violations | = 0 |
| C0-6 | Owner claims marked, labelled H or PS, quoted verbatim | owner_rule_violations | = 0 |
| C0-7 | Census claims match computed values | census_claim_mismatches | = 0 |
| C0-8 | Judgment rows well-formed | problems | = 0 |
| C0-9 | Work Queue §L: no topic-to-topic link in the SSSC register | topic_topic_links_in_track | = 0 |
| C0-10 | No duplicate source registration in the SSSC register | register_duplicate_groups | = 0 |
| C0-11 | Every pair shares a cited evidence source (G03 excluded) | pairs_without_shared_evidence_source | = 0 |
| C0-12 | Every pair has a cross-citation in the existing ledgers | pairs_without_cross_citation | = 0 |
| C0-13 | At least one judged factor in all four topics | unity_factors | ≥ 1 |
| C0-14 | Every pair has a Connection link | pairs_without_connection_link | = 0 |
| C0-15 | No 80-character overlap with the Totality Suite | boundary_overlaps | = 0 |

C0-9 to C0-12 test **existing records** and earlier claims. A failure there is a finding, not a method failure. C0-13 and C0-14 summarise this report's own judgments; they show the judgments are complete, not that the topics are united.

**Disclosure of dry-run knowledge.** While the tool was being developed it was dry-run on these inputs:
- Before writing the plan, reading the link register showed TL-08 (SUBC→CONS), so C0-9 was expected to FAIL (value 1). The threshold stays at the Work Queue's implied 0.
- Reading the reports suggested duplicate registrations. The dry run found four groups (K04 = K43, K12 = K58, K20 = K52, K26 = K64), not the three first noticed, and CN0-02 was corrected to 4 before this push. C0-10 is expected to FAIL.
- The dry run showed that the original form of C0-11 (any shared cited source) passes only because every topic cites the owner's framework G03, and that with G03 excluded only SUBC–CONS shares sources (S16, S31, S32). The metric was changed to exclude the framing source **after** seeing this, because a framework citation is not shared evidence. Both values are kept in the record (`pairs_without_shared_source`, `pairs_without_shared_evidence_source`). C0-11 is expected to FAIL.
- The dry run showed three cross-citations (TD-CONS-20 → TC-SUBC-20, TD-CONS-29 → TC-SOUL-21, TD-SPIRIT-31 → TC-SOUL-01) and three pairs with none. C0-12 is expected to FAIL.
No threshold was changed after the dry run.

## Maps & Matrix
v39 (`v39-cycles-0-4-mr-track-abcd-phases-x12-conn0`) is built by `tools/conn.py maps` from the unchanged `gaia_tools.phases maps` base, plus the overlay: `matrix/connection_claim_placement.csv`, `matrix/connection_factor_x_topic.csv`, `matrix/connection_pairs_6.csv`, one added column in `matrix/intersections_625.csv`, CL-* edges between the existing topic nodes in `graph/link_graph.json`, `changes/connection_changes.csv` and `validation/connection_Baseline.json`. v1–v38 are not modified.

## Gate
- PASS needs C0-1 to C0-8, C0-13 to C0-15, identical reruns (worktree and fresh clone), manifests, validator and tests.
- C0-9 to C0-12 are reported as they fall.
- The Connection's content stays **Proposed**, gate INDETERMINATE pending independent review.
