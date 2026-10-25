# N-A Level-Name Crosswalk — x12 report

**Status:** x12 complete. The crosswalk (`../CROSSWALK.md`) is **Proposed**. All 28 options are "open (Kyle)". GAIA-Documentation was only read, never written.

**Inputs:**
- `config.json`
- `../judgments/*_x12.csv`
- `../CROSSWALK.md` (hashed in every record)
- ledger `../ledger/ledger_x12.csv`

The tables are in `TABLES.md`. The run records are in `iter-1/` to `iter-3/`.

## Results
1. **The consolidation is complete.**
   - CROSSWALK.md covers all six conflicts and all 28 options (X12-29 and X12-30 PASS).
   - The GD and suite boundary scans are clean (X12-12 PASS).
2. **x9 corrections applied, and they reproduce:**
   - The conflict evidence now resolves (X12-23 PASS).
   - The ripple claim is corrected: any Work Queue edit, appended or not, changes the hashed blob.
   - The checker defect is fixed behind the `x12` key. The x9 record still reproduces with the defect on record.
3. **X12-28 FAIL (method).** CROSSWALK.md names two *check* IDs, "X9-27" and "X3-3". The row-ID pattern reads them as row IDs "X9" and "X3", which do not exist.
   - Every crosswalk row ID the document actually cites exists. The failure is a collision between check-ID and row-ID notation, which the check did not anticipate.
   - Following the standing rule, it stays failed. Neither the document nor the check was changed after the run.
   - The fix for any later use is to anchor row IDs as two digits (`X\d{2}`) or to write check IDs in code formatting.
4. **Diminishing returns (X12-31 PASS; a summary, as disclosed).**
   - No crosswalk row changed against x9.
   - Only five options changed: four consequences corrected (K1-C, K2-B, K2-C, K3-B) and one added (K3-G).
   - Only two conflicts changed (K5 and K6), both in their evidence citations.
5. **Findings that fail again, as expected:**
   - X12-24: the Work Queue's "24 tablet files" against 22 in the listing.
   - X12-25: the align-foundation options touch files that other records read.
   - X12-27: K6 has no unqualified surviving non-defer option.
   
   For K3, the new K3-G passes the adversarial rule, but it was added after X9-27 failed, so the pass is not independent evidence.
6. **GD-consistency findings carried from earlier cycles fail as before:** X12-8, -9, -11, -13, -14, -15, -19 and -20, plus X12-16 outside the gate.

## Gate
- **x12 gate: FAIL (method), because of X12-28.** All other method checks PASS: X12-1 to X12-7, X12-12, X12-17, X12-21, X12-22, X12-29 and X12-30.
- The verification gate (reruns, manifests, validator, tests) is in `VERIFICATION.md`.
- The substance of the crosswalk is not affected by the X12-28 failure. Its recorded cause is above.

## Diminishing returns, stated plainly
More cycles would not change the map. What remains open is Kyle's to decide:
- which sense of Meta the Foundation intends (K2)
- whether to cite GD phases as tracks, with sense qualifiers (K3)
- what the Tablets' sealing status, stage sequence and numbering are meant to be (K6, and N-B)

Each of these is an option in the register, with its review verdict and its ripple cost.
