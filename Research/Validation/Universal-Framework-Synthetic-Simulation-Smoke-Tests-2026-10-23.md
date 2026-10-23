# Universal Framework — Synthetic Simulation Smoke Tests

**Run date:** 2026-10-23  
**Status:** Executed locally; synthetic data only.  
**Scope:** Five small computational checks, with 12 cases each where applicable. These are not the twelve full Report 7 studies and are not empirical validation.

## Results

| Test | Cases | Result | Limitation |
|---|---:|---|---|
| Lorenz initial-condition sensitivity | 12 perturbation magnitudes | All trajectories returned finite numerical states; final states differed across perturbations | Numerical smoke test, not a new Lyapunov-exponent estimate |
| Homeostatic feedback controller | 12 seeds × 1,000 steps | Mean absolute deviation from target: 0.2012 model units | Toy control model, not physiological parameterization |
| Reinforcement-learning foraging proxy | 12 seeds per condition | Mean final-window reward: penalty 0.00 = 0.7588; penalty 0.15 = 0.7448 | Specific to the chosen synthetic reward/update rules; not evidence about human learning |
| Planetary radiative-balance toy | 12 albedo scenarios, 0.20–0.35 | Effective radiating temperature decreased from about 263.22 K to 249.90 K as albedo increased | Blackbody equilibrium only; omits greenhouse effect, clouds, transport, oceans, and feedbacks |
| Synthetic spectrum pipeline | 12 seeded noisy sinusoids, 0.30–0.52 Hz | Mean absolute peak-frequency error 0.000549 Hz; maximum 0.001113 Hz | Validates FFT on generated signals only, not real geomagnetic data |

## Reproducibility and limits

The runs used explicit seeds 0–11. The Lorenz integration used SciPy `solve_ivp` with relative tolerance (10^{-9}), absolute tolerance (10^{-11}), and maximum step 0.02. Other tests used NumPy-generated disturbances and synthetic signals. No observational data were downloaded.

**Passed:** execution, finite numerical outputs, bounded response in the tested feedback model, monotonic response of the radiative toy to the prescribed albedo, and recovery of dominant frequencies in synthetic stationary signals.

**Not established:** biological validity; any theory of subjective experience; metaphysical claims; real geomagnetic spectra; geodynamo or atmospheric-escape dynamics; climate projections; or independent reproduction.

These checks must not be counted as the twelve full simulation designs in the Report 7 addendum. Those studies require operational specifications, real data where appropriate, baselines, ablations, sensitivity analysis, output logs, and independent reproduction instructions. A synthetic signal is not a substitute for INTERMAGNET data, and a toy energy-balance equation is not a climate model.
