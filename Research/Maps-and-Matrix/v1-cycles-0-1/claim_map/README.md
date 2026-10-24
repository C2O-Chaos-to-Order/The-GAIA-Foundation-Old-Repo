# Claim map (v1, Cycles 0–1)

`claim_map.csv` has one row per claim per cycle: 100 rows for Cycle 0 and 142 for Cycle 1. Cycle-0 claim IDs (`C0v2-…`) are carried into Cycle 1 under the same ID, and new Cycle-1 claims use `C1-…`. No claim was dropped.

| Column | Meaning |
|---|---|
| cycle, claim_id, report | where the claim lives (`Research/Cycles/<cycle>/Report-*/claims/claims.csv`) |
| label, label_code | framework label (E / P / PS / H) |
| conclusion_status, claim_class | as recorded in the ledger |
| source_ids | as cited. `literature_sources` and `simulation_checks` split this field; `full_text_sources` gives the literature sources whose register access mode is full text |
| prev_label, prev_status | the same claim's label and status in the previous cycle (empty when new) |
| change_vs_prev_cycle | deterministic class, computed by `gaia_tools.maps.classify_claim_change` (rules in order: new / dropped / label down → weakened / label up → strengthened / note 'Upgraded…' → strengthened (full-text source) / 'counter-evidence' → weakened (label unchanged) / status changed / identical → unchanged / 'Carried forward…' → carried forward / otherwise updated) |
| change_note | the cycle's own `c1_change` text, verbatim |

Label totals: Cycle 0 65 E / 14 P / 19 PS / 2 H; Cycle 1 91 E / 28 P / 21 PS / 2 H.
