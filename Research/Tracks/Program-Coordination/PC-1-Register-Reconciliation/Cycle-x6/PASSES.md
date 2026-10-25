# PC-1 x6: passes

| Pass | What was done | Result |
|---|---|---|
| 1 | **UR b16 crosswalk.** Each of the 26 UR §5 criteria (EPI-1 to OPS-5) was read, and the TOT domain whose purpose names its subject was chosen as primary (`../judgments/ur_criteria_x6.csv`). The tool does not suggest these choices; it only checks their consistency. | All 26 are mapped, to 17 distinct domains. |
| 2 | **ToG §19 planned files.** Each of the 10 planned files was assigned to the domains it serves, with a relation (`../judgments/tog19_x6.csv`). | All 10 are assigned. |
| 3 | **Product Register rules.** 8 rules (6 product kinds, 2 overlays) were written and joined to the 64 products (`../judgments/product_rules_x6.csv`). | All 64 products are governed. |
| 4 | **Corrections.** The 018 review note was fixed. 003 now cites RL-3 (partial), and a matching authority row was added. | x3 inputs are unchanged; the x6 inputs are new files. |

The tool parses the dependencies in the register (286 named edges) and counts how many fall out of order under the roadmap schedule and under the proposed one. Iteration 1 sets 038 to Wave 3 and iteration 2 to Wave 4.
