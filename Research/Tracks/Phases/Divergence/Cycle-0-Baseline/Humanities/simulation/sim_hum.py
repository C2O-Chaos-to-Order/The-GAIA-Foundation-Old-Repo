"""SIM-<PH>-HUM: Humanities simulations (Phases track). Usage: python sim_hum.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def lexical_divergence(P, rng):
    """Two daughter languages split T millennia ago; each of M meanings is replaced independently in each lineage at rate
    r*g per millennium, g ~ Gamma(shape a, mean 1) across meanings (a = 0 means homogeneous). Shared-cognate fraction C; the
    constant-rate (glottochronological) estimate T_hat = -ln C / (2 r). Formal check of a dating method, not a model of Andic (P06)."""
    out = {}
    for a in P["shapes"]:
        Ts, Cs = [], []
        for _ in range(P["reps"]):
            g = np.ones(P["M"]) if a == 0 else rng.gamma(a, 1 / a, P["M"])
            keep = (rng.random(P["M"]) < np.exp(-P["r"] * g * P["T"])) & (rng.random(P["M"]) < np.exp(-P["r"] * g * P["T"]))
            C = max(keep.mean(), 1 / P["M"]); Cs.append(C); Ts.append(-np.log(C) / (2 * P["r"]))
        exp_C = np.exp(-2 * P["r"] * P["T"]) if a == 0 else (1 + 2 * P["r"] * P["T"] / a) ** (-a)
        out[str(a)] = dict(mean_C=float(np.mean(Cs)), analytic_C=float(exp_C), mean_T_hat=float(np.mean(Ts)), bias=float(np.mean(Ts) / P["T"] - 1))
    h, het = out["0"], out[str(P["shapes"][-1])]
    c = [chk("V1", "homogeneous rates: mean T_hat within 5% of the true T", h["bias"], abs(h["bias"]) <= 0.05),
         chk("V2", "simulated mean shared-cognate fraction within 0.02 of the analytic value for every shape", max(abs(v["mean_C"] - v["analytic_C"]) for v in out.values()),
             max(abs(v["mean_C"] - v["analytic_C"]) for v in out.values()) <= 0.02),
         chk("H1", f"rate heterogeneity (shape {P['shapes'][-1]}) makes the constant-rate estimate underestimate T by >= 10%", het["bias"], het["bias"] <= -0.10, "hypothesis"),
         chk("R1", "results by shape", out, True, "reporting")]
    return out, c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
