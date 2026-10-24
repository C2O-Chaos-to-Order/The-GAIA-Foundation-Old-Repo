# Research Cycles

Each cycle is a complete, separately versioned pass over all seven foundational reports, followed by a Verification. Cycles never overwrite one another; each lives in its own folder (and is intended to be pushed on its own branch for review).

| Folder | Cycle | Specification | Status |
|---|---|---|---|
| `Cycle-0-Baseline/` | 0 | 1 research pass + 1 simulation run per report; Verification — **Baseline v2 (framework-aligned)**, scope per `Cycle-0-Baseline/FRAMEWORK.md` | Branch `research/cycle-0-baseline`; gate **Indeterminate** |
| `Cycle-1-x3/` | 1 | 3 distinct research passes + 3 chained simulate+report iterations per report; Verification | Branch `research/cycle-1-x3` (PR to `main`); gate **Indeterminate** |
| `Cycle-2-x6/` | 2 | ×6 | Not started |
| `Cycle-3-x9/` | 3 | ×9 | Not started |
| `Cycle-4-x12/` | 4 | ×12 | Not started |

Standard layout inside every cycle:
```
Cycle-N-.../
  README.md
  FRAMEWORK.md         governing scope (Seven-Report Framework; GAIA Is the Motherthread) + label mapping
  Report-1-Body/ … Report-7-Unified/
     REPORT.md          report (Plan §8 structure + framework scope coverage and labels)
     claims/claims.csv  claim-to-source ledger
     sources/sources.csv sources used by this report
     simulation/        SPEC.md (written before execution), params.json, script, outputs/, EXECUTION_RECORD.json
                        (from Cycle 1: script + iter-1..N/ each with SPEC.md, params.json, outputs/, EXECUTION_RECORD.json)
     research/pass-1..N/NOTES.md   (from Cycle 1) one folder per research pass
     CHANGELOG.md       (from Cycle 1) what changed and why
  Verification/        VERIFICATION.md + raw check outputs
  Provenance/          SOURCE_REGISTER.csv, repository inventory, MANIFEST.sha256
  tools/               shared helper code
```
The Master Report (Unconditional Love and Conditional Love) lives outside the cycles at `Research/Master-Report-Unconditional-and-Conditional-Love/`.

## Version history of this index
| Version | Date | Change |
|---|---|---|
| 1 | 2026-10-24 | Created with Cycle 0 Baseline v2 (blob d915d51 on main) |
| 2 | 2026-10-24 | Cycle 1 (x3) row updated; layout extended for passes and iterations |
