# ToG1 x3 iteration1: executed report

One initial execution and one same-author isolated-copy reproduction. Not independent review. See SPEC.md,EXECUTION_RECORD.json,outputs/results.json and Verification/REPRODUCTION.json. Specifications unchanged from their pre-execution digests. Iteration1 reconstructs the conversational baseline rule and adds synthetic evidence screening.

## Recorded result

```json
{
  "vector_count": 177147,
  "outcomes": {
    "PASS": 1,
    "FAIL": 175099,
    "INDETERMINATE": 2047
  },
  "oracle_mismatches": 0,
  "unsafe_passes": 0,
  "defect_fixtures": 55,
  "defect_outcomes": {
    "INDETERMINATE": 44,
    "FAIL": 11
  },
  "novelty": "Reconstructed rule plus a metadata screen; no original Baseline bytes available",
  "checks": {
    "E1": "PASS",
    "E2": "PASS",
    "E3": "PASS",
    "E4": "PASS",
    "E5": "PASS",
    "E6": "PASS",
    "E7": "PASS"
  },
  "scope": "Synthetic consistency testing only; no independent review or real-world authorization"
}
```

## Interpretation and limits

All results are about stipulated finite models,not actual human rights protection,independent reviewer qualifications or lawful authority. Outputs reproduced byte-for-byte by the same author. Separate execution-record timestamps and predecessor-record digests differ as expected. The source metadata screen accepts fabricated but well-formed fields;known forgery must be represented in the input. All-defect detection is limited to55specified synthetic fixtures.
