# Cycle 4 (x12) — change log (from Cycle 3)

## Evidence
- 6 new sources registered (Y01–Y06; 5 full text, Y05 abstract only). Two more read and not usable (Y07, Y08; logged only). 19 logged queries.
- 23 new claims (C4-R1-01 … C4-R7-03). **No carried claim changed label or status (SIM-R7-C4 iteration 9: 0/216)** — the third cycle in a row with no change (0/142, 0/177). 13 carried claims annotated (`c4_change`).
- Link register: 28 links (L28 new, Plausible, within Report 2); strict rule downgraded nothing; `c4_strict_rule` column added. Report 2 still has no Established link to another report.

## Simulations
- Twelve chained iterations per report (84 runs), runner byte-identical to Cycles 1–3. Validation 19/19 pass; hypotheses 46/73 supported, 27 not supported (reported as findings); 14 reporting checks.

## Tools and maps
- `Research/tools` 0.4.0, data model 1.3.0 (Y source IDs; `../../tools/CHANGELOG.md`); Maps & Matrix v4 (`../../Maps-and-Matrix/v4-cycles-0-4/`).

## Development disclosures (honesty)
- **R2 substitute:** the carried item 'faithful Mackintosh (1975) rule' is BLOCKED by access (no open-access specification; Y05 abstract only; Y07, Y08 read without a specification). SIM-R2-C4 is a smaller substitute (PH-vs-KF design robustness), not the carried test. The PH 'rho' option is our addition.
- **R3:** no independent human coder is possible for this agent; SIM-R3-C4 tests stability of the single coding, not reliability.
- **R4 iteration 6 design error:** the selection-bias scenario set the confounder's effects to zero, so selection created no bias to detect (median ORs ~1.01); its 'not supported' is a design error, not a finding about Y04. Kept as run; not re-specified; not cited by any claim.
- **R1 iteration-10 SPEC wording error:** the SPEC says '192-setting grid'; the grid is 4×4×3×3 = 144. Results correct; SPEC not edited after the run.
- **R5:** a handoff note recorded R5 as 9/11 hypotheses supported; the execution records give 8/10 (iteration 10's check is a validation check). The records are authoritative.
- **R6:** W03 still closed; our cost form is ours; agreement would have been calibration.
- **R7:** Report 7's own claims (C4-R7-*) are excluded from its inputs, so no re-run was needed after writing them.
- **Research passes:** many of the 84 passes added nothing new (Report 1, 3 and 6 literature passes in particular); each NOTES file says so. Passes were not padded.
- **Simulation development:** scripts were written and the official iterations executed once in this tree (SPEC and params written before execution); one R3 attempt failed before execution because a data-copy path was wrong (no results produced; SPECs regenerated identically).
- Not done (carried beyond Cycle 4): independent human coders (R3, lens placement); faithful Mackintosh (R2, blocked); W03 equations (R6, blocked); Body×Justice cell; an Established link for Report 2; independent review.
