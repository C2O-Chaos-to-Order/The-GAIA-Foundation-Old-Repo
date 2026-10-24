# SIM-R4-C3 — superseded run 1 (kept unchanged for the record)

Run 1 of all nine iterations (folders `iter-1` … `iter-9` here, produced by `sim_r4_run1.py`) is preserved exactly as executed.
It was superseded for one reason, found when reading the outputs:

- **Coding error in iterations 3 and 9 (H3, H9).** The synthetic cohort was called with the confounder prevalences swapped
  (confounder present in *all attenders* instead of in *all never-attenders*), so the simulated association pointed the wrong way:
  observed RR 1.316 instead of about 0.758. Its size was exactly the reciprocal of the target (1/1.316 = 0.760), which already
  showed the bound itself was right. H3 and H9 were therefore reported "Not supported" because of our bug, not because of a finding.

Fix in run 2 (`../sim_r4.py`, lines marked `run 2 fix`): the two arguments were swapped back. The `params.json` and `SPEC.md` of
every iteration are unchanged (same pre-registered checks), and all nine iterations were re-run in order.

Not changed, and still reported as a failure in run 2: **V1** (iteration 1). Its pre-registered expectation said our formula would
reproduce S12's E-values "to 2 decimals". The point estimate does (2.35), but E(0.71) = 2.167, which rounds to 2.17, while S12 prints
2.16. That is consistent with S12 truncating, or with an unrounded CI limit slightly above 0.71; we did not change the expectation after
seeing the result.

Execution note: the first attempt at run 2 stopped in iteration 9 with a NameError (our edit had turned part of a line into a comment).
The line was repaired and run 2 was executed again in full (iterations 1–9, in order); the outputs of iterations 1–8 are deterministic, so
only their timestamps differ from the interrupted attempt, which left no other record.
