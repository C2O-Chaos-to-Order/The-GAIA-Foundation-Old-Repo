# Link graph (v1; state after Cycle 1)

GAIA (the motherthread; **Philosophical/Spiritual**, G03 `FRAMEWORK.md`) is at the centre. It has a dashed *motherthread* edge to each of the seven reports; these edges express the organizing framework, not findings. The 24 typed links L01–L24 come from `Research/Cycles/Cycle-1-x3/Report-7-Unified/maps/link_register.csv`. Each edge is labelled with its ID, its type and its framework label: E (green, thick), P (blue), PS (purple, dashed) or H (red, dotted). L24 ('unresolved question') points to *All reports*. Self-loops (L16, L19–L21) are links within one report.

```mermaid
flowchart LR
  GAIA(("GAIA<br/>motherthread [PS]"))
  R1["R1 Body"]
  R2["R2 Mind"]
  R3["R3 Soul"]
  R4["R4 Spirit"]
  R5["R5 Consciousness"]
  R6["R6 Earth"]
  R7["R7 Unified"]
  ALL[["All reports"]]
  GAIA -.->|"motherthread [PS]"| R1
  GAIA -.->|"motherthread [PS]"| R2
  GAIA -.->|"motherthread [PS]"| R3
  GAIA -.->|"motherthread [PS]"| R4
  GAIA -.->|"motherthread [PS]"| R5
  GAIA -.->|"motherthread [PS]"| R6
  GAIA -.->|"motherthread [PS]"| R7
  R1 -->|"L01 relationship [P]"| R6
  R1 -->|"L02 distinction [P]"| R6
  R1 -->|"L03 humans within Earth [E]"| R6
  R1 -->|"L04 dependency [E]"| R2
  R1 -->|"L05 feedback loop [P]"| R2
  R1 -->|"L06 competing interpretation [PS]"| R2
  R2 -->|"L07 relationship [P]"| R5
  R2 -->|"L08 distinction [E]"| R5
  R2 -->|"L09 competing interpretation [PS]"| R3
  R3 -->|"L10 relationship [E]"| R4
  R3 -->|"L11 distinction [PS]"| R4
  R3 -->|"L12 competing interpretation [PS]"| R5
  R3 -->|"L13 relationship [E]"| R6
  R4 -->|"L14 relationship [P]"| R1
  R4 -->|"L15 dependency [H]"| R1
  R4 -->|"L16 distinction [E]"| R4
  R5 -->|"L17 dependency [E]"| R1
  R5 -->|"L18 relationship [H]"| R4
  R6 -->|"L19 dependency [E]"| R6
  R6 -->|"L20 feedback loop [P]"| R6
  R6 -->|"L21 competing interpretation [P]"| R6
  R6 -->|"L22 humans within Earth [E]"| R7
  R6 -->|"L23 competing interpretation [PS]"| R3
  R7 -->|"L24 unresolved question [PS]"| ALL
  linkStyle 0 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 1 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 2 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 3 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 4 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 5 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 6 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 7 stroke:#1f5fbf,stroke-width:2px
  linkStyle 8 stroke:#1f5fbf,stroke-width:2px
  linkStyle 9 stroke:#1b7f3b,stroke-width:3px
  linkStyle 10 stroke:#1b7f3b,stroke-width:3px
  linkStyle 11 stroke:#1f5fbf,stroke-width:2px
  linkStyle 12 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 13 stroke:#1f5fbf,stroke-width:2px
  linkStyle 14 stroke:#1b7f3b,stroke-width:3px
  linkStyle 15 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 16 stroke:#1b7f3b,stroke-width:3px
  linkStyle 17 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 18 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 19 stroke:#1b7f3b,stroke-width:3px
  linkStyle 20 stroke:#1f5fbf,stroke-width:2px
  linkStyle 21 stroke:#c0392b,stroke-width:2px,stroke-dasharray:2 4
  linkStyle 22 stroke:#1b7f3b,stroke-width:3px
  linkStyle 23 stroke:#1b7f3b,stroke-width:3px
  linkStyle 24 stroke:#c0392b,stroke-width:2px,stroke-dasharray:2 4
  linkStyle 25 stroke:#1b7f3b,stroke-width:3px
  linkStyle 26 stroke:#1f5fbf,stroke-width:2px
  linkStyle 27 stroke:#1f5fbf,stroke-width:2px
  linkStyle 28 stroke:#1b7f3b,stroke-width:3px
  linkStyle 29 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
  linkStyle 30 stroke:#8a4fbf,stroke-width:2px,stroke-dasharray:6 4
```

Machine-readable form: `link_graph.json` (nodes, edges, type, label, label history across cycles, basis claim IDs, Cycle-1 status, rejection screen).

| Edge | From → To | Type | Label (C0 → C1) | Rejection screen (Cycle 1, SIM-R7-C1 it3) |
|---|---|---|---|---|
| M1 | GAIA → R1 | motherthread | PS | — |
| M2 | GAIA → R2 | motherthread | PS | — |
| M3 | GAIA → R3 | motherthread | PS | — |
| M4 | GAIA → R4 | motherthread | PS | — |
| M5 | GAIA → R5 | motherthread | PS | — |
| M6 | GAIA → R6 | motherthread | PS | — |
| M7 | GAIA → R7 | motherthread | PS | — |
| L01 | R1 → R6 | relationship | P → P | pressure: simulation test not supported |
| L02 | R1 → R6 | distinction | P → P | pressure: contested/indeterminate basis |
| L03 | R1 → R6 | humans within Earth | E → E | no rejection trigger observed |
| L04 | R1 → R2 | dependency | E → E | pressure: contested/indeterminate basis |
| L05 | R1 → R2 | feedback loop | P → P | pressure: simulation test not supported |
| L06 | R1 → R2 | competing interpretation | PS → PS | pressure: contested/indeterminate basis |
| L07 | R2 → R5 | relationship | P → P | pressure: contested/indeterminate basis |
| L08 | R2 → R5 | distinction | E → E | pressure: contested/indeterminate basis |
| L09 | R2 → R3 | competing interpretation | PS → PS | pressure: contested/indeterminate basis |
| L10 | R3 → R4 | relationship | E → E | no rejection trigger observed |
| L11 | R3 → R4 | distinction | PS → PS | pressure: contested/indeterminate basis |
| L12 | R3 → R5 | competing interpretation | PS → PS | pressure: contested/indeterminate basis |
| L13 | R3 → R6 | relationship | E → E | no rejection trigger observed |
| L14 | R4 → R1 | relationship | P → P | pressure: contested/indeterminate basis |
| L15 | R4 → R1 | dependency | H → H | no rejection trigger observed |
| L16 | R4 → R4 | distinction | E → E | pressure: contested/indeterminate basis |
| L17 | R5 → R1 | dependency | E → E | no rejection trigger observed |
| L18 | R5 → R4 | relationship | H → H | no rejection trigger observed |
| L19 | R6 → R6 | dependency | E → E | no rejection trigger observed |
| L20 | R6 → R6 | feedback loop | E → P | pressure: contested/indeterminate basis |
| L21 | R6 → R6 | competing interpretation | P → P | pressure: simulation test not supported |
| L22 | R6 → R7 | humans within Earth | E → E | no rejection trigger observed |
| L23 | R6 → R3 | competing interpretation | PS → PS | no rejection trigger observed |
| L24 | R7 → ALL | unresolved question | PS → PS | pressure: contested/indeterminate basis |

Counts after Cycle 1: 24 links = 9 E / 7 P / 6 PS / 2 H. 15 links are under pressure in the Cycle-1 rejection screen. The only label change is L20, E → P.
