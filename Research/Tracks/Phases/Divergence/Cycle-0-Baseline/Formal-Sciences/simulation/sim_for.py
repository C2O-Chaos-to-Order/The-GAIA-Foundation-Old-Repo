"""SIM-<PH>-FOR: Formal-Sciences simulations (Phases track). Usage: python sim_for.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def logistic_lyapunov(P, rng):
    """Logistic map x -> r x (1-x). Global Lyapunov exponent lambda = mean ln|r(1-2x)| along an orbit (after burn-in),
    and separation growth of two orbits started delta0 apart (sensitive dependence, P09 Chaos_lambda definition)."""
    lam = {}
    for r in P["r_values"]:
        x = rng.uniform(0.1, 0.9); s = 0.0
        for _ in range(P["burn"]): x = r * x * (1 - x)
        for _ in range(P["n"]):
            x = r * x * (1 - x); s += np.log(max(abs(r * (1 - 2 * x)), 1e-300))
        lam[str(r)] = s / P["n"]
    steps = []
    for k in range(P["pairs"]):
        x = rng.uniform(0.1, 0.9); y = x + P["delta0"]; t = 0
        while abs(x - y) < P["sep"] and t < 1000:
            x = 4 * x * (1 - x); y = 4 * y * (1 - y); t += 1
        steps.append(t)
    pred = np.log(P["sep"] / P["delta0"]) / np.log(2)
    res = dict(lyapunov=lam, steps_to_sep=dict(median=float(np.median(steps)), min=int(min(steps)), max=int(max(steps))), predicted_steps_ln2=float(pred))
    c = [chk("V1", "r = 4: lambda within 0.01 of ln 2 = 0.693147 (analytic)", lam["4.0"], abs(lam["4.0"] - np.log(2)) <= 0.01),
         chk("V2", "r = 3.2 (stable 2-cycle): lambda < 0 (analytic)", lam["3.2"], lam["3.2"] < 0),
         chk("H1", f"r = 4: median steps for a {P['delta0']:g} separation to exceed {P['sep']} within 25% of ln(sep/delta0)/ln 2", res["steps_to_sep"]["median"], abs(res["steps_to_sep"]["median"] / pred - 1) <= 0.25, "hypothesis"),
         chk("R1", "lambda by r", lam, True, "reporting")]
    return res, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
