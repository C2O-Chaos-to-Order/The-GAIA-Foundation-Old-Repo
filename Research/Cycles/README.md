# Research Cycles

Each cycle is a complete, separately versioned pass over all seven foundational reports, followed by a Verification. Cycles never overwrite one another; each lives in its own folder (and is intended to be pushed on its own branch for review).

| Folder | Cycle | Specification | Status |
|---|---|---|---|
| `Cycle-0-Baseline/` | 0 | 1 research pass + 1 simulation run per report; Verification | Staged; gate **Indeterminate** |
| `Cycle-1-x3/` | 1 | 3 distinct research passes + 3 distinct simulation runs per report; Verification | Not started |
| `Cycle-2-x6/` | 2 | ×6 | Not started |
| `Cycle-3-x9/` | 3 | ×9 | Not started |
| `Cycle-4-x12/` | 4 | ×12 | Not started |

Standard layout inside every cycle:
```
Cycle-N-.../
  README.md
  Report-1-Body/ … Report-7-Unified/
     REPORT.md          report (Plan §8 structure)
     claims/claims.csv  claim-to-source ledger
     sources/sources.csv sources used by this report
     simulation/        SPEC.md (written before execution), params.json, script, outputs/, EXECUTION_RECORD.json
  Verification/        VERIFICATION.md + raw check outputs
  Provenance/          SOURCE_REGISTER.csv, repository inventory, MANIFEST.sha256
  tools/               shared helper code
```
The Master Report (Unconditional Love and Conditional Love) lives outside the cycles at `Research/Master-Report-Unconditional-and-Conditional-Love/`.
