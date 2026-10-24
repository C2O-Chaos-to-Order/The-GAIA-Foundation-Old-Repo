# SIM-R5-C0 — Toy recurrent "ignition" model (specification, written before execution)

**Status:** Specified before execution. Class: Mathematical/computational **toy**. It models a dynamical signature (all-or-none sustained activity) that the Global Neuronal Workspace account associates with conscious *access* (S20). It says **nothing** about phenomenal experience (S16, S17), and Cogitate 2025 (S18) found a general lack of the predicted ignition at stimulus offset, so the signature itself is empirically contested.

## Model
Single rate population: τ dr/dt = −r + f(w·r + I(t) − θ) + η(t);  f(z) = 1/(1+e^(−z/κ)). τ=10 ms, θ=4, κ=0.5, dt=0.1 ms. Stimulus I = amplitude a for 50 ms then 0. Noise η ~ N(0, σ²), σ=0.3 (per √ms scaling), seed = 20261023. "Late activity" = mean r over 200–300 ms after stimulus offset.
Conditions: w = 8 (strong recurrence; bistable regime) vs w = 2 (weak recurrence). Amplitudes a ∈ linspace(0, 8, 41), 50 noisy trials each.

## Expected outputs (pre-registered)
- E1: w=8: late activity is bimodal across trials/amplitudes (fraction of trials with late r>0.5 jumps from <0.1 to >0.9 within a narrow amplitude band ≤ 2 units wide).
- E2: w=2: no trial sustains late r>0.5 (no self-sustained state).
- E3: w=8: the zero-stimulus condition does not spontaneously ignite in >10% of trials.
**Failure criteria:** E1–E3 not met → Fail recorded.
