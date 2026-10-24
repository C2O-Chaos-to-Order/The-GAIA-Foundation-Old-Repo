# SIM-R6-C0 — Part A: Daisyworld; Part B: geomagnetic dipole trend + free-decay time (specification, written before execution)

**Status:** Specified before execution. Class: Mathematical/computational (A: published toy model; B: arithmetic on official model coefficients + order-of-magnitude physics).

## Part A — Daisyworld (Watson & Lovelock 1983, S21b)
**Question:** Does a re-implementation of the published Daisyworld equations, with the published Fig. 1 parameters, reproduce temperature regulation over a range of luminosity, and how does that compare with the lifeless planet?
**Equations (S21b eqs 1–5,7):** da_i/dt = a_i(xβ_i − γ); x = P − a_b − a_w; β_i = 1 − 0.003265(22.5 − T_i)²  (0 outside 5–40 °C); σ(T_e+273)⁴ = S·L(1−A); A = a_g·A_g + a_b·A_b + a_w·A_w; T_i = q′(A − A_i) + T_e.
**Parameters (S21b Fig. 1 caption):** γ = 0.3, P = 1, S = 917 W m⁻² (9.17×10⁵ erg cm⁻² s⁻¹), A_g = 0.5, A_b = 0.25, A_w = 0.75, q′ = 20.
**Implementation assumptions (ours, not from S21b):** minimum seed area 0.01 per species each step so populations can recolonise; Euler integration dt = 0.05 to quasi-steady state (2000 steps) at each L; L swept 0.5→1.7→0.5 in steps of 0.01.
**Expected:** E1: with daisies, T_e stays within 22.5 ± 10 °C over a contiguous L range at least 3× wider than the range over which the lifeless planet stays within the same band. E2: hysteresis — the L at which daisies first appear on the up-sweep differs from where they die out on the down-sweep (or the reverse), as S21b Fig. 1 notes.

## Part B — Geomagnetic dipole
**B1 Question:** What is the change in Earth's axial+equatorial dipole moment 1900–2025 according to IGRF-14 (S27)?
M = (4π R_E³/μ0)·sqrt(g10² + g11² + h11²), R_E = 6371.2 km.
**B2 Question:** Order of magnitude of free ohmic decay of a dipole field in a conducting sphere of core radius R_c = 3480 km (S25): τ = μ0 σ R_c²/π². σ is **assumed** in {0.5, 1.0, 1.5}×10⁶ S m⁻¹ (S29 reports conductivities 2–3× higher than older estimates but its abstract does not give the value used here; the range is our sensitivity assumption).
Compare τ with the ≥ 3.3–4.2 Gyr paleomagnetic record (S28).
**Expected:** E3: IGRF dipole moment decreases between 1900 and 2025 (sign only pre-registered). E4: τ ≤ 10⁶ yr for all σ, i.e. ≥ 3 orders of magnitude shorter than the paleomagnetic record — consistent with the field needing continual regeneration (a dynamo), not proving any particular dynamo mechanism.
**Failure criteria:** any E not met → Fail recorded.
**Not shown:** Earth is not Daisyworld; nothing here bears on Earth being conscious or having a "heart" except as metaphor.

## Baseline v2 note (2026-10-24)
Re-run fresh for v2 with unchanged model, parameters and seeds. One non-scientific change: output CSVs are now written with LF line endings (v1 wrote CRLF, which a later byte-exactness check of the GitHub push showed could be altered in transit). Numerical content is unchanged.
