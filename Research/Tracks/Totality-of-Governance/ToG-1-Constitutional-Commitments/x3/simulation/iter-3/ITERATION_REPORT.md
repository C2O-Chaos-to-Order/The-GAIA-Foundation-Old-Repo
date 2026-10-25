# ToG1 x3 iteration3: executed report

One initial execution and one same-author isolated-copy reproduction. Not independent review. See SPEC.md,EXECUTION_RECORD.json,outputs/results.json and Verification/REPRODUCTION.json. Specifications unchanged from their pre-execution digests. Iteration3 reads actual iter2 ready-state output and tests lifecycle event chains.

## Recorded result

```json
{
  "trace_count": 2401,
  "event_steps": 9604,
  "post_event_outcomes": {
    "PASS": 1764,
    "INDETERMINATE": 2676,
    "FAIL": 5164
  },
  "final_outcomes": {
    "INDETERMINATE": 527,
    "FAIL": 1776,
    "PASS": 98
  },
  "oracle_mismatches": 0,
  "unsafe_passes": 0,
  "post_revocation_or_incident_passes": 0,
  "novelty": "Extends static iter2 readiness to bounded time/version/event traces",
  "checks": {
    "L1": "PASS",
    "L2": "PASS",
    "L3": "PASS",
    "L4": "PASS",
    "L5": "PASS",
    "L6": "PASS",
    "L7": "PASS",
    "L8": "PASS",
    "L9": "PASS",
    "L10": "PASS"
  },
  "scope": "Synthetic consistency testing only; no independent review or real-world authorization"
}
```

## Interpretation and limits

All results are about stipulated finite models,not actual human rights protection,independent reviewer qualifications or lawful authority. Outputs reproduced byte-for-byte by the same author. Separate execution-record timestamps and predecessor-record digests differ as expected. The2401traces have horizon4 only. The mutation counterexamples encode fixed predicted outputs of two unsafe strategies,not general source-code mutation coverage;do not interpret them as an exhaustive mutation test.
