# Manifestation ×3 — Research Pass 3
## Reproducibility, Matrix Applicability, and Governance Boundaries

**Stable ID:** GAIA-RP-MANIFESTATION-X3-R3  
**Date:** 2026-10-28  
**Status:** Research pass completed; synthesis carried into the stage report  
**Scope:** Evidence preservation, uncertainty, matrix-cell applicability, status transitions, and the scope of the plan-authority decision for this stage.

### Research question
What records are needed to keep the stage reproducible and honest about uncertainty, and how should the two matrices and unresolved governance relationships be handled?

### Method
Review Research Plan v1.4 and Baseline ×1; compare them with the National Academies' definitions of reproducibility/replicability and uncertainty guidance, NIST's testing/measurement guidance, and preregistration practice guidance. Test matrix cardinality and status-transition rules using synthetic counterexamples.

### Sources
- **R3-S1 — GAIA Research Plan v1.4:** https://github.com/KyleAlexanderSteen/Research-for-The-GAIA-Foundation-Research/blob/main/The%20GAIA%20Research%20Plan/README.md ; commit 13e0330cb64eaff9e54d08b74a97fa3f05b1f02d.
- **R3-S2 — National Academies of Sciences, Engineering, and Medicine (2019), Reproducibility and Replicability in Science, Summary:** https://www.nationalacademies.org/read/25303/chapter/3 (accessed 2026-10-28).
- **R3-S3 — NIST (2023), AI Risk Management Framework 1.0:** https://doi.org/10.6028/NIST.AI.100-1 (accessed 2026-10-28).
- **R3-S4 — OSF Support, Welcome to Registrations & Preregistrations:** https://help.osf.io/article/330-welcome-to-registrations (accessed 2026-10-28).

The National Academies distinguishes computational reproducibility using the same data/code/methods/conditions from replicability across studies using new data and recommends acknowledging relevant uncertainty. OSF guidance recommends specifying hypotheses, methods, contingencies, and decision criteria before analysis. These practices do not turn one deterministic execution into independent replication.

### Findings
1. **Keep reproducibility, replicability, and independent review distinct.** Re-running a script on identical fixtures can check computational reproducibility, but not independent replication on new data.
2. **Criteria should precede interpretation.** The official simulation scripts and protocol are being registered before their official run records are produced. The repository commit order will make this order inspectable, but cannot prove when local drafting first began.
3. **Matrix counts are bookkeeping controls:** Zodiac × Alchemy = 12 × 5 = 60; Alchemy × Transformative Phase = 5 × 6 = 30. These related matrices are not automatically a validated 360-cell cube.
4. **Cell meanings are unresolved until operationalized:** Every applicable cell needs an operational question/hypothesis, evidence requirement, challenge/falsification condition, and uncertainty statement. N/A needs a rationale. Missing Zodiac identities or meanings must not be invented.
5. **Status discipline matters:** A PROPOSED dependency cannot be elevated to confirmed merely because track titles appear related; an UNKNOWN conflict cannot be closed without closure evidence. The v1.4 register defines stable IDs, affected stages/gates, and closure criteria.
6. **Stage-specific authority boundary:** The user's direct instruction to proceed from Baseline ×1 to Manifestation ×3 authorizes v1.4 for this current baseline-to-Manifestation sequence. It does not silently replace the older Foundation seven-report extension for other work. The older file remains preserved; any broader supersession/reconciliation remains a separate governance decision.

### Challenge / alternative explanation
The record-keeping overhead should be proportionate to consequence. Low-risk procedural controls may use compact IDs and evidence links; higher-consequence claims need stronger source snapshots, environments, uncertainty analysis, and independent review.

### Outcome
**Supported:** The plan's uncertainty and status distinctions are appropriate; the matrix dimensions can be checked without assuming semantic completeness.  
**Gap:** Zodiac and many conceptual cell definitions remain unoperationalized.  
**Recommendation:** Keep matrix work at candidate-cell level until definitions, evidence, and applicability are specified; preserve the narrow scope of the authority decision.
