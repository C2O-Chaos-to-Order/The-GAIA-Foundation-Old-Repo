# Link register (Cycle 3)

- `link_register_input.csv` — the register before the Cycle-3 rule checks (24 Cycle-2 links with `c3_*` evidence columns, plus new L25–L27); read by SIM-R7-C3.
- `link_register.csv` — the final Cycle-3 register: the same rows plus `c3_strict_rule` (SIM-R7-C3 iteration 2: no Established link downgraded) and `c3_essential_rule` (iteration 3: the pre-registered essential-claim rule; it restores none of L04, L08, L16). Labels are those of the strict rule.
