"""Reproducible synthetic smoke tests for the GAIA Universal Framework.
These are toy-model diagnostics only, not empirical validation of consciousness,
metaphysics, geophysics, or the biological mechanisms discussed in the reports.
Requires Python 3.11+, NumPy, and SciPy.
"""
import json
import numpy as np
from scipy.integrate import solve_ivp

def lorenz(t, s, sigma=10.0, rho=28.0, beta=8.0/3.0):
    x, y, z = s
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

def run_lorenz():
    base = np.array([1.0, 1.0, 1.0])
    rows = []
    for i in range(12):
        eps = 10 ** (-8 + i * 0.5)
        initial = base.copy()
        initial[0] += eps
        sol = solve_ivp(lorenz, (0, 30), initial, rtol=1e-9,
                        atol=1e-11, max_step=0.02)
        rows.append({"run": i + 1, "initial_perturbation": float(eps),
                     "n_points": len(sol.t),
                     "final_state": [float(v) for v in sol.y[:, -1]],
                     "finite": bool(np.isfinite(sol.y).all())})
    return {"all_finite": all(r["finite"] for r in rows), "runs": rows}

def run_homeostasis():
    rows = []
    for seed in range(12):
        rng = np.random.default_rng(seed)
        x, total_abs = 0.0, 0.0
        for _ in range(1000):
            disturbance = rng.normal(0, 0.25)
            action = np.clip(-0.8 * x, -0.5, 0.5)
            x = 0.95 * x + disturbance + action
            total_abs += abs(x)
        rows.append({"seed": seed, "mean_abs_deviation": total_abs / 1000,
                     "final_deviation": float(x)})
    return {"mean_abs_deviation_across_seeds":
            float(np.mean([r["mean_abs_deviation"] for r in rows])),
            "runs": rows}

def run_rl_proxy():
    rows = []
    for seed in range(12):
        for penalty in (0.0, 0.15):
            rng = np.random.default_rng(seed)
            q = np.zeros((5, 2))
            rewards = []
            for _ in range(600):
                s = int(rng.integers(0, 5))
                for _ in range(12):
                    a = int(rng.integers(0, 2)) if rng.random() < 0.1 else int(np.argmax(q[s]))
                    reward = (1.0 if (a == 1 and s >= 2) else 0.0)
                    reward -= (0.12 if a == 1 else 0.0)
                    reward -= penalty * max(0, 2 - s)
                    ns = int(np.clip(s + (1 if a == 1 else -1) + rng.integers(-1, 2), 0, 4))
                    q[s, a] += 0.08 * (reward + 0.9 * np.max(q[ns]) - q[s, a])
                    s = ns
                    rewards.append(reward)
            rows.append({"seed": seed, "interoceptive_penalty": penalty,
                         "mean_reward_last_1000_steps": float(np.mean(rewards[-1000:]))})
    means = {str(p): float(np.mean([r["mean_reward_last_1000_steps"]
                                    for r in rows if r["interoceptive_penalty"] == p]))
             for p in (0.0, 0.15)}
    return {"group_means": means, "runs": rows}

def run_radiative_toy():
    sigma_sb = 5.670374419e-8
    solar_constant = 1361.0
    rows = []
    for i, albedo in enumerate(np.linspace(0.20, 0.35, 12), 1):
        absorbed = (solar_constant / 4.0) * (1.0 - albedo)
        temp = (absorbed / sigma_sb) ** 0.25
        rows.append({"run": i, "albedo": float(albedo),
                     "absorbed_solar_W_m2": float(absorbed),
                     "effective_radiating_temperature_K": float(temp)})
    return {"temperature_range_K":
            [min(r["effective_radiating_temperature_K"] for r in rows),
             max(r["effective_radiating_temperature_K"] for r in rows)],
            "runs": rows}

def run_synthetic_spectrum():
    rows = []
    for seed in range(12):
        rng = np.random.default_rng(seed)
        n, fs = 4096, 10.0
        t = np.arange(n) / fs
        known = 0.30 + seed * 0.02
        signal = np.sin(2 * np.pi * known * t) + 0.35 * rng.normal(size=n)
        freqs = np.fft.rfftfreq(n, 1 / fs)
        power = np.abs(np.fft.rfft(signal * np.hanning(n))) ** 2
        estimated = float(freqs[np.argmax(power[1:]) + 1])
        rows.append({"seed": seed, "known_frequency_hz": known,
                     "estimated_peak_hz": estimated,
                     "absolute_error_hz": abs(estimated - known)})
    return {"mean_peak_error_hz": float(np.mean([r["absolute_error_hz"] for r in rows])),
            "max_peak_error_hz": float(max(r["absolute_error_hz"] for r in rows)),
            "runs": rows}

if __name__ == "__main__":
    print(json.dumps({
        "lorenz_initial_condition_sensitivity": run_lorenz(),
        "homeostatic_controller": run_homeostasis(),
        "reinforcement_learning_foraging_proxy": run_rl_proxy(),
        "radiative_energy_balance_toy": run_radiative_toy(),
        "synthetic_spectrum_pipeline": run_synthetic_spectrum(),
    }, indent=2))
