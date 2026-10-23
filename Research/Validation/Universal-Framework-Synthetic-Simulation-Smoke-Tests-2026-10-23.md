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


## Independent rerun record — 2026-10-23 (supplemental)

**Purpose:** independently re-execute the five bounded synthetic smoke-test functions during the repository reconciliation pass, and distinguish that result from the twelve full Report 7 study designs.

**Source inspected:** `Research/Validation/universal_framework_synthetic_smoke_tests.py`, Git blob `82ab6c29abcddd02540df42107bd691d0b71f708`. The function logic was re-executed in an isolated Python analysis environment from the fetched source content; the exact repository file was not downloaded as a local file byte-for-byte, so this is a logic-level rerun rather than a verified checksum of a local executable copy.

**Runtime:** Python 3.13.5; NumPy 2.3.5; SciPy 1.17.0.

| Test | Rerun outcome | Interpretation |
|---|---|---|
| Lorenz initial-condition sensitivity | 12/12 solver runs reported success; all state values finite | Execution sanity only; no Lyapunov exponent or general chaos claim established |
| Homeostatic feedback controller | Mean absolute deviation across 12 seeds = 0.20120802797751702 | The toy controller remains bounded for the tested settings; no physiological inference |
| Reinforcement-learning foraging proxy | Mean final-window reward: penalty 0.00 = 0.7588066666666667; penalty 0.15 = 0.7448475000000002 | Difference is specific to the defined synthetic reward and update rules; no human learning inference |
| Planetary radiative-balance toy | Effective-radiating temperature range = 249.90499601146894–263.2201280492291 K across albedo 0.35–0.20 | Direction matches the model equation; not a climate projection and excludes greenhouse/transport/feedback processes |
| Synthetic spectrum pipeline | Mean absolute peak error = 0.0005485026041666582 Hz; maximum = 0.0011132812499999867 Hz across 12 seeded signals | FFT pipeline recovers the dominant frequency of these generated signals; no real geomagnetic-data claim |

**Disposition:** the bounded smoke-test logic reproduced the recorded headline outcomes. This improves confidence in the limited computational record, but it does not establish that the repository's exact file bytes were run in place, that an independent third party reproduced the tests, or that the twelve full Report 7 simulations have been executed. The RL comparison is exploratory and should not be interpreted as a causal result beyond this synthetic setup. No new empirical data were used.
