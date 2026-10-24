# SIM-R2-C0 — Two bounded learning/memory models (specification, written before execution)

**Status:** Specified before execution. Class: Mathematical/computational. Part (b) uses published empirical data (S04 Table 3).

## (a) Rescorla–Wagner blocking
**Question:** Does the Rescorla–Wagner (RW) update ΔV_i = αβ(λ − ΣV) reproduce Kamin blocking as described in S06?
**Design:** Blocking group: 20 A+ trials then 20 AX+ trials. Control group: 20 B+ trials (B unrelated) then 20 AX+ trials. α=0.3, β=1, λ=1. Deterministic.
**Expected:** E1: V_X(blocking) < 0.1·V_X(control). E2: ΣV on AX trials converges to λ (|ΣV−1|<0.01) in both groups.

## (b) Forgetting-curve function comparison
**Question:** Which of three standard functional forms best fits the savings data for Ebbinghaus (1885) and Dros (Murre & Dros 2015 replication), as tabulated in S04 Table 3?
**Data:** intervals 20 min, 1 h, 9 h, 1 d, 2 d, 6 d, 31 d (converted to hours); savings Ebbinghaus = 0.582, 0.442, 0.358, 0.337, 0.278, 0.254, 0.211; Dros = 0.472, 0.373, 0.276, 0.317, 0.230, 0.168, 0.041.
**Models:** exponential b = a·e^(−kt); power b = a·t^(−c); logarithmic b = a − c·ln t. Least squares (scipy curve_fit); compare SSE and AIC (n=7, 2 parameters each).
**Expected (stated before running):** E3: for Ebbinghaus, power or log beats exponential on AIC (consistent with S04's report that simple exponential decay fits poorly). E4: report Dros result without expectation (its 31-day point is noted by S04 as anomalously low).
**Failure criteria:** non-convergence of any fit, or E1–E3 not met → Fail recorded.

**Not shown:** that RW is the correct theory of learning (it has known failures — see report), or that any forgetting function is a law of memory.

## Correction recorded after execution
The E3 rationale "(consistent with S04's report that simple exponential decay fits poorly)" was written from memory before checking. A text search of the S04 snapshot did not locate such a statement; S04 compares several functions (power, power with 1-day boost, summed exponential, Memory Chain Model) by SSD/R²/AIC. The rationale is withdrawn. E3 itself (an expectation, not a citation) was executed unchanged.

## Baseline v2 note (2026-10-24)
Re-run fresh for Baseline v2 with unchanged model, parameters and seeds; no deviation. Outputs reproduce v1 (see Verification/VERIFICATION.md). The v1 deviations recorded above still apply.
