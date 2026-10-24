# Cycle 3 (x9) — change log (from Cycle 2)

## Evidence
- 21 new sources registered (X02, X03, X05, X08, X09, X11–X26), all full text (Europe PMC XML, PMC OAI-PMH, or an open submitted-version PDF for X05). Three are full texts of sources previously read only as abstracts (X02 for U21, X03 for U20, X05 for T10). Five retrievals failed and are logged, not registered (see `Provenance/README.md`).
- 49 logged queries (22 OpenAlex open-access lookups).
- 39 new claims (C3-R1-01 … C3-R7-04). **No carried claim changed label or status (SIM-R7-C3 iteration 9: 0/177)** — diminishing returns on revising earlier conclusions. 15 carried claims were annotated (`c3_change`); two gained a full-text source and phrase (C0v2-R5-02, C0v2-R5-07); C2-R5-05 was reinterpreted as a design artefact (label unchanged).
- **Replications labelled as such:** C3-R4-03's common-outcome E-value (~1.97) repeats C1-R4-07; C3-R4-05's synthetic-cohort check repeats C0v2-R4-13. Only the exact-PH conversion, tipping points, many-weak-confounder, healthy-attender and mediator-vs-confounder results are new in Report 4.
- Link register: 27 links (new L25 P, L26 H, L27 PS); strict rule downgraded nothing; the essential-claim rule would restore none of L04/L08/L16; `c3_strict_rule` and `c3_essential_rule` columns added.

## Simulations
- Nine chained iterations per report (63 runs), runner byte-identical to Cycles 1–2. Validation 16/17 pass (**1 Fail: SIM-R4-C3 it1 V1**, a rounding check, disclosed and not re-specified); hypotheses 35/58 supported, 23 not supported (reported as findings); 6 reporting checks.

## Tools and maps
- `Research/tools` 0.3.0, data model 1.2.0 (`../../tools/CHANGELOG.md`); Maps & Matrix v3 (`../../Maps-and-Matrix/v3-cycles-0-3/`).

## Development disclosures (honesty)
- **R4 run 1 superseded:** a coding error swapped the confounder prevalences in iterations 3 and 9, which made both checks 'not supported'. Run 1 is preserved in `Report-4-Spirit/simulation/superseded-run-1/` (with its script and README); run 2 is current. During the fix an edit swallowed a code line and run 2 first stopped with a NameError; repaired and run 2 executed in full (README there).
- **R4 V1 Fail kept:** 2.167 vs S12's printed 2.16 (pre-registered to 2 decimals). Not re-specified. C3-R4-03 no longer cites this check (an Established claim may not cite a failed check; `gaia_tools` K-sim flagged it).
- **Ledger corrections found by tools before verification:** C3-R1-06 now says 'not supported' for the coarse-grid check it cites (K-sim); C3-R2-05 wording corrected ('parametric pre-exposure design', not 'compound-with-context'); C3-R4-03/05 and the C0v2-R4-09 note re-worded to say they repeat earlier cycles.
- **R3 coder C:** same research agent, different method (mechanical lexicon on keyword windows); not independent inter-rater reliability. Only lexicon-hit tables are stored, not source text (copyright and size).
- **R7:** all nine iterations were re-run (a) after the C3-R7 claims were added to the ledger (the audits must see the final ledger) and (b) after the lens rule and the Maps-v2 matrix were copied into `Report-7-Unified/simulation/data/` so that `gaia_tools.rerun` (which copies only `Cycles/`) can re-execute iterations 6–7; the first tool rerun had failed on those two for that reason. `draw_lens_sample.py` was amended to exclude C3-R7-* claims from its sampling frame, which keeps the hand-coded 40-claim sample identical (the frame was the 212-claim ledger when it was drawn). Pre-registered checks were not changed.
- **R1:** iteration 8's savings result is trivially satisfied; the ratio metric is quantised by whole days.
- **R2:** the Mackintosh rule was simplified to the point of producing no LI — an implementation limit, reported as such.
- **R6:** W03's equations unavailable; constrained adaptation compared against W01's published row only.
- **Research passes:** passes 6–9 were often empty for literature (stated per pass); several Cycle-3 passes added nothing new, and are recorded as such.
- Not done (carried to Cycle 4): independent human coder (R3) and independent lens coder (R7); continuous re-induction metric (R1); faithful Mackintosh (R2); negative-control designs (R4); better criticality proxy (R5); W03 equations (R6); Body×Justice cell.
