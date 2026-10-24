# SIM-R1-C0 — Generic negative-feedback homeostasis model (specification, written before execution)

**Status:** Specified 2026-10-23 before execution. Model class: Mathematical/computational (toy). Not a model of any specific organ system.

## Question
In the generic sensor → comparator(set point) → controller → effector loop described by Modell et al. 2015 (S02), how do (a) no control, (b) proportional (P) control and (c) proportional-integral (PI) control respond to a sustained step disturbance, and what happens when feedback gain is degraded ("dysregulation")?

## Formal model
x = regulated variable (dimensionless, set point s = 0). Passive leak k_l.
dx/dt = -k_l·x + u(t) + d(t) + noise;  u = -k_p·e - k_i·∫e dt,  e = x - s;  effector output clipped to |u| ≤ u_max.
Disturbance d(t) = D for t ≥ t_d (step). Euler–Maruyama, dt = 0.01, T = 60.

## Inputs (params.json)
k_l=0.1, k_p=2.0, k_i=1.0, u_max=5, D=1.0, t_d=10, noise σ=0.02, seed=20261023. Degraded case: k_p, k_i scaled by 0.1.

## Expected outputs (pre-registered)
- E1: no control: steady-state x → D/k_l = 10 (analytic).
- E2: P-only: steady-state error → D/(k_l+k_p) ≈ 0.476 (analytic; noise-free run within 1%).
- E3: PI: steady-state error → 0 (|mean x over last 10 time units| < 0.02).
- E4: degraded PI shows larger peak deviation and slower recovery than intact PI.
- E5: saturation: with D=6 > u_max, PI cannot restore the set point (bounded capacity).

## Failure criteria
Any of E1–E5 not met → Fail recorded; results not rewritten.

## What this does NOT show
It does not establish any physiological parameter, organ mechanism, or health claim. It only checks that the textbook control-theoretic description behaves as the description says.

## Deviation recorded after first execution (not hidden)
E1 was pre-registered as "steady state → 10". With leak k_l = 0.1 (time constant 10) and only 50 time units after the step, the uncontrolled system has not reached steady state at T = 60. The check actually executed compares x(T) to the analytic transient value 10·(1 − e^(−5)) = 9.933 (1% tolerance). The pre-registered steady-state wording was therefore not testable as written; the substituted check is documented here and in EXECUTION_RECORD.json.
