# PC-1 Baseline: passes

| Pass | What was done | Result |
|---|---|---|
| 1 | Agent judgment. Each of the 45 register domains was read against the governance files in this branch: Universal Regulation, Gate Authority, Risk Levels, Product Register, the UR audits and the Totality of Governance draft. For each domain the pass records a canonical home, stable ID, proposed document ID, owner, reviewer roles, UR domains, anchors, label and basis in `../judgments/domains_c0.csv`. The 45 audit v2 items were mapped to domains in `../judgments/audit_map_c0.csv`. The roadmap waves were read from the suite's wave lists by short phrase (in `../judgments/roadmap_c0.csv`). | 45 rows: 6 extend an existing file, 1 extends a file planned in ToG §19, 36 are new, and 2 are shared with the Encyclopedia. All 45 labels are Plausible: every row is a proposal for the owner, not a finding. |

Iteration 1 recomputed every check from the sources under the `as_judged` home rule.
