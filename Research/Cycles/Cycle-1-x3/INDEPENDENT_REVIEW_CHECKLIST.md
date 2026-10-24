# Independent review checklist (Cycle 1)

For a reviewer who did not produce this work. Tick each item; record disagreements in a review file rather than editing the ledgers.

## Sources and claims
- [ ] Pick at least 10 Established claims at random (`Report-*/claims/claims.csv`); open the source URL and confirm the wording is supported by the cited locator, not only the verification phrase.
- [ ] Confirm every Established literature claim has a full-text source (`Provenance/SOURCE_REGISTER.csv`, access_mode) — K4 checks this mechanically.
- [ ] Check the 3 downgrades and 8 upgrades in `CHANGELOG.md` are justified.
- [ ] Check that abstract-only new sources (V08, V16, V22, V30, V37, V38, V39) support only Plausible claims.
- [ ] Look for missing counter-evidence in each report's 'Competing views' section.

## Labels
- [ ] Each Philosophical/Spiritual claim is phrased as interpretation, not as fact.
- [ ] GAIA framing never substitutes for evidence (Report 7, C0v2-R7-01; C1-R7-01).
- [ ] Review the three Established links with contested basis claims (L04, L08, L16) — retain or downgrade?

## Simulations
- [ ] Re-run all 21 iterations (`README.md`) and compare `outputs/results.json` hashes with `EXECUTION_RECORD.json`.
- [ ] Read each `SPEC.md`: were checks plausible pre-registrations? Note any you would have set differently.
- [ ] Confirm 'not supported' outcomes are reported as findings in the reports.
- [ ] Assess the R7 K3/K5 changes disclosed in `CHANGELOG.md`.

## Process
- [ ] Search-strategy gap: queries were not logged in Cycle 1 — judge whether key literature is missing.
- [ ] Ethics: no human-subject data used; check reports for harmful framings (esp. Report 4 health claims).

Until this checklist is completed by someone independent, the gate stays **Indeterminate**.
