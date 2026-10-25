# ToG1 x3 iteration2: executed report

One initial execution and one same-author isolated-copy reproduction. Not independent review. See SPEC.md,EXECUTION_RECORD.json,outputs/results.json and Verification/REPRODUCTION.json. Specifications unchanged from their pre-execution digests. Iteration2 reads actual iter1 output and tests six review/authority conditions.

## Recorded result

```json
{
  "vector_count": 729,
  "outcomes": {
    "PASS": 1,
    "FAIL": 665,
    "INDETERMINATE": 63
  },
  "oracle_mismatches": 0,
  "unsafe_passes": 0,
  "identity_only_mutant_false_passes": 242,
  "novelty": "Adds explicit synthetic review/authority conditions to actual iter1 screened fixture",
  "checks": {
    "R1": "PASS",
    "R2": "PASS",
    "R3": "PASS",
    "R4": "PASS",
    "R5": "PASS",
    "R6": "PASS",
    "R7": "PASS",
    "R8": "PASS"
  },
  "scope": "Synthetic consistency testing only; no independent review or real-world authorization"
}
```

## Interpretation and limits

All results are about stipulated finite models,not actual human rights protection,independent reviewer qualifications or lawful authority. Outputs reproduced byte-for-byte by the same author. Separate execution-record timestamps and predecessor-record digests differ as expected. The identity-only mutant is an intentionally unsafe policy;242falsePASS cases measure a difference between toy rules,not a real reviewer-error rate.
