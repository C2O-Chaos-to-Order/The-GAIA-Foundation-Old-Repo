# Cycle 2 (x6) — change log (from Cycle 1)

## Evidence
- 15 new sources (W01–W15): 13 full text (Europe PMC XML; W01 publisher OA PDF), 2 abstract-only (W02, W03; only Plausible claims rest on W02 alone). S12 (Cycle 0) re-read for mediation results.
- **Systematic searches are now logged** (`Provenance/SEARCH_LOG.jsonl`, 34 queries). Many broad queries were noisy; title-restricted retries are logged; screening covered top-ranked hits only.
- 35 new claims (28 E, 7 P). No carried claim changed label or status (SIM-R7-C2 T1: 0/142) — **diminishing returns** on revising earlier conclusions; Cycle 2's gains are new, sharper claims and filled limits.
- 37 empty limits fields (warning Q1) of carried claims filled (pass 6).
- Link register: strict Established-link rule applied — L04, L08, L16 Established → Plausible (procedural). 21 other links re-assessed with Cycle-2 evidence; labels unchanged.

## Simulations
- Six chained iterations per report (42 runs), runner byte-identical to Cycle 1. Validation 32/32 pass; hypotheses 32/49 supported, 17 not supported (reported as findings); 14 reporting checks.

## Tools and maps
- `Research/tools` 0.2.0, data model 1.1.0 (`../../tools/CHANGELOG.md`); Maps & Matrix v2 (`../../Maps-and-Matrix/v2-cycles-0-2/`).

## Development disclosures (honesty)
- **R7 re-runs:** iteration 2 was re-run after a bug fix in the reporting-only SP2 component calculation (connected components were mis-computed); iterations 4–6 were re-run after W15 and claim C2-R5-06 were added to the ledger (the audit must see the final ledger). Pre-registered checks were not changed.
- **R5 pilot:** a small pilot run was used to choose the coupling range; disclosed in every R5 SPEC.md.
- **R1:** H4b is supported only trivially (effector saturation); iteration 5 fell back to the unbounded learner because no safe bound existed (pre-specified fallback, disclosed in results).
- **R3:** both codings by the same research agent (re-coding reliability, not inter-rater reliability); codebook written before the second coding; blank form for an independent coder in `Report-3-Soul/research/pass-5/`.
- **Simulation code** was smoke-tested before official runs; R2's PH model was rewritten for clarity and R5 dead code removed before the official runs; a docstring of `tools/runner.py` was accidentally edited and reverted so that it stays byte-identical to Cycle 1.
- **Ledger corrections before verification:** a wrong counter-evidence note on C0v2-R4-10 was removed; a duplicate source entry ('Zapf') removed; C2-R4-06 wording corrected to match the executed checks; one verification phrase (C2-R2-01) escaped for regex use after the first live check failed on unescaped parentheses.
- Not done (carried to Cycle 3): independent human coder for R3; two-coder lens placement for the maps; definition of 'essential' basis claims.
