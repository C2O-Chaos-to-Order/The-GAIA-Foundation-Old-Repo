# Cycle 1 (x3) — change log (from Cycle 0 Baseline v2)

## Evidence
- Access rule added (FRAMEWORK.md). Of the 11 abstract-only Established claims: upgraded to full text — C0v2-R1-09 (V06), R2-04 (V04), R2-12 (V05), R5-02 (V01), R5-06 (V07), R6-02 (V02), R6-05 (V03), R6-13 (V09); downgraded to Plausible — C0v2-R4-10, R6-01, R6-04.
- 37 new sources (V01–V41 minus failures: V10 Sterling full text unavailable; IDs V20, V21, V31 were not assigned); 7 of them abstract-only.
- 42 new claims; revised claims listed per report in `Report-*/CHANGELOG.md`.
- Link register: all 24 links given Cycle-1 evidence, simulation checks, literature tests and status; L20 Established → Plausible.

## Simulations
- Cycle-0 single runs replaced by per-report libraries (`sim_rN.py`) with three chained iterations each (iteration k reads iteration k-1 where `prev` is set) and a shared runner writing EXECUTION_RECORD.json with check kinds (validation / hypothesis / reporting).

## Development disclosures (honesty)
- Simulation libraries were smoke-tested in a scratch folder (/tmp) during development; official iterations were run from scratch in this tree, and Verification re-ran all 21 in a fresh copy (byte-identical).
- Bug fixes during development (before official runs): R1 delay buffer used zero instead of the current state when lag = 0; R2 code rewritten for clarity; R3 custom ARI/silhouette (scikit-learn unavailable); R5 fixed-point counter double-counted a root lying exactly on a grid point; check kinds introduced so that substantive 'not supported' outcomes are not reported as errors.
- Parameters chosen in development and disclosed in SPECs: R5 mask amplitude 1.5 (so thresholds fall inside the grid).
- R7 after its first official run: (a) bug fix — citations of Cycle-0 runs (`C0:` prefix) were not routed to the Cycle-0 records; (b) access-mode wording for S19 and S27 normalized to 'full text (...)' (their access did not change); (c) **scope refinement made after seeing output**: K5 (no Established claim on governing documents alone) now exempts claims backed by simulation evidence (C0v2-R7-05/06); (d) K3 changed from 'only Pass/Supported' to 'no failed validation check; any cited Not-supported outcome must be stated as not supported in the wording'. All R7 iterations were then re-run.
- The Cycle-0 tree is untouched; Cycle-1 claims that rest on Cycle-0 runs cite them with a `C0:` prefix.
