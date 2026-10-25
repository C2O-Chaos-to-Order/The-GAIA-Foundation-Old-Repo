# PC-1 x3: passes

| Pass | What was done | Result |
|---|---|---|
| 1 | **Anchor re-read.** For each of the 66 distinct anchors cited in the Baseline, the passage it points to was read (about 420 characters after the anchor, inspected outside the repository and not filed). Every domain–anchor pair was judged `direct`, `partial` or `none`, with a note, in `../judgments/anchor_review_x3.csv`. | 94 Baseline pairs judged: 56 direct, 37 partial, 1 `none` (033's numerical-matrix anchor, a Baseline error, now removed). 15 anchors added: 13 direct, 2 partial (UR ETH-5 for 021 and 027). One review note is wrong: 018's file-level change-log anchor is noted as "replaced", but it is still cited next to the new incident-section anchor. The note is corrected in x6. The judgment inputs of this run are left as they ran. |
| 2 | **Deeper audit mapping.** Each of the 45 audit v2 items now has exactly one primary domain. The remedy home of each of the 16 non-PASS items was judged on its own, without copying the primary domain's home, and the implementation locus was recorded (`../judgments/audit_map_x3.csv`). | For 5 of the 16, the fix belongs in a different file than the primary domain's home. |
| 3 | **Authority register.** Every source a domain cites, other than its home, was classified (`../judgments/authority_x3.csv`). | 87 rows. |
| 4 | **Wave proposals.** For each of the five mismatches, options and an agent preference were recorded (`../judgments/wave_proposals_x3.csv`). | 5 rows. For 038 the agent records no preference. |

Iterations 1–3 used the home rules `as_judged`, `always_new` and `no_planned`.
