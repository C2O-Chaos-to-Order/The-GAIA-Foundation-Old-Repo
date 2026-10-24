"""SIM-<PH>-SOC: Social-Sciences simulations (Phases track). Usage: python sim_soc.py iter-<k>."""
import os, sys, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import track_runner as R
chk = R.chk

def _clusters(x, gap, min_share):
    xs = np.sort(x); cut = np.where(np.diff(xs) > gap)[0]; groups = np.split(xs, cut + 1)
    return [g for g in groups if len(g) >= min_share * len(x)]

def deffuant(P, rng):
    """Deffuant-Weisbuch bounded-confidence model: random pairs interact if |xi - xj| < eps and move mu toward each other;
    optional Gaussian noise (sd 'noise') per interaction (cf. P03's noisy assimilative influence). Counts major opinion clusters."""
    out = {}
    for eps in P["eps_values"]:
        ks, drift = [], []
        for rep in range(P["reps"]):
            x = rng.uniform(0, 1, P["agents"]); m0 = x.mean()
            for _ in range(P["steps"]):
                i, j = rng.integers(0, P["agents"], 2)
                if i != j and abs(x[i] - x[j]) < eps:
                    d = P["mu"] * (x[j] - x[i]); x[i] += d; x[j] -= d
                    if P["noise"] > 0: x[i] = np.clip(x[i] + rng.normal(0, P["noise"]), 0, 1); x[j] = np.clip(x[j] + rng.normal(0, P["noise"]), 0, 1)
            drift.append(abs(x.mean() - m0)); ks.append(len(_clusters(x, P["gap"], P["min_share"])))
        out[str(eps)] = dict(clusters=ks, mean_clusters=float(np.mean(ks)), max_mean_drift=float(max(drift)))
    lo, hi = str(P["eps_values"][0]), str(P["eps_values"][-1])
    c = [chk("V1", "noise = 0: pairwise updates conserve the mean opinion (|drift| < 1e-9)", max(v["max_mean_drift"] for v in out.values()),
             (max(v["max_mean_drift"] for v in out.values()) < 1e-9) if P["noise"] == 0 else True),
         chk("H1", f"eps = {hi}: every replicate ends in one major cluster (consensus)", out[hi]["clusters"], all(k == 1 for k in out[hi]["clusters"]), "hypothesis"),
         chk("H2", f"eps = {lo}: mean number of major clusters in [{P['h2'][0]}, {P['h2'][1]}] (fragmentation; ~floor(1/(2 eps)))", out[lo]["mean_clusters"],
             P["h2"][0] <= out[lo]["mean_clusters"] <= P["h2"][1], "hypothesis"),
         chk("R1", "clusters per replicate by eps", {k: v["clusters"] for k, v in out.items()}, True, "reporting")]
    return out, c

def siem(P, rng):
    """Simplified re-implementation of the Social Influence and Event Model (SIEM) of P03: Hegselmann-Krause bounded confidence
    on opinions in [-1, 1]; each step every individual draws k random partners; individuals with certainty above their partners'
    mean drift by U[0, 0.1 eps] (random sign), others take the mean of themselves and partners within eps; certainty is pulled
    back toward its initial value by a random fraction and then given a symmetric drift of amplitude 'cdrift' (interpretation of
    P03's '[0 0.1]'); events start with probability Ef per step, last U[0, 2 Ed] steps, have strength U[Es-0.2, Es+0.2] and sign
    +/- at random, and pull individuals with |O - E| < eps and certainty <= strength toward the event by U[0,1] of the gap.
    Conflict = SD of opinions averaged over steps t0..T. Not P03's code; an independent approximation."""
    n = P["agents"]; out = {}
    for lab, Ef in (("no_events", 0.0), ("events", P["Ef"])):
        conf = []
        for rep in range(P["reps"]):
            lo = np.repeat(np.arange(7) * 0.1, n // 7 + 1)[:n]; C0 = lo + rng.uniform(0, 0.4, n); C = C0.copy()
            O = rng.uniform(-1, 1, n); ev_left = 0; E = 0.0; sds = []
            for t in range(P["T"]):
                nb = rng.integers(0, n, (n, P["k"])); On = O[nb]; Cn = C[nb].mean(1)
                within = np.abs(On - O[:, None]) < P["eps"]
                hk = (O + (On * within).sum(1)) / (1 + within.sum(1))
                drift = rng.uniform(0, 0.1 * P["eps"], n) * rng.choice([-1, 1], n)
                O = np.where(C > Cn, O + drift, hk)
                if ev_left <= 0 and Ef > 0 and rng.random() < Ef:
                    ev_left = rng.uniform(0, 2 * P["Ed"]); E = rng.uniform(P["Es"] - 0.2, P["Es"] + 0.2) * rng.choice([-1, 1])
                if ev_left > 0:
                    hit = (np.abs(O - E) < P["eps"]) & (C <= abs(E)); O = np.where(hit, O + rng.uniform(0, 1, n) * (E - O), O); ev_left -= 1
                O = np.clip(O, -1, 1)
                C = C + rng.uniform(0, 1, n) * (C0 - C); C = np.clip(C + rng.uniform(-P["cdrift"], P["cdrift"], n), 0, 1)
                if t >= P["t0"]: sds.append(O.std())
            conf.append(float(np.mean(sds)))
        out[lab] = dict(conflict=conf, mean=float(np.mean(conf)), se=float(np.std(conf, ddof=1) / np.sqrt(len(conf))))
    eq6 = lambda Es, EfEd: 0.75 * (1 - P["eps"]) * (0.44 + Es * EfEd ** 0.08) if EfEd > 0 else 0.75 * (1 - P["eps"]) * 0.44
    e0 = eq6(0, 0); e1 = eq6(P["Es"], P["Ef"] * P["Ed"]); a, b = out["no_events"]["mean"], out["events"]["mean"]
    lo = np.repeat(np.arange(7) * 0.1, n // 7 + 1)[:n] + rng.uniform(0, 0.4, n); k = P["tol_se"]; sec = lo.std(ddof=1) / np.sqrt(n)
    res = dict(out, eq6_no_events=e0, eq6_events=e1, certainty_mean=float(lo.mean()), certainty_sd=float(lo.std(ddof=1)))
    c = [chk("V1", f"initial certainty allocation (7 overlapping ranges of width 0.4) has mean within {k} standard errors of 0.50", [res["certainty_mean"], k * sec], abs(res["certainty_mean"] - 0.5) <= k * sec),
         chk("H1", f"no events: long-term conflict within {P['h_tol']} of P03 Eq. 6 = {e0:.3f}", a, abs(a - e0) <= P["h_tol"], "hypothesis"),
         chk("H2", f"events (Es {P['Es']}, Ef {P['Ef']}, Ed {P['Ed']}): long-term conflict within {P['h_tol']} of P03 Eq. 6 = {e1:.3f}", b, abs(b - e1) <= P["h_tol"], "hypothesis"),
         chk("H3", f"events raise conflict by more than {P['h3']} over the no-event condition (event-sustained polarisation)", b - a, b - a > P["h3"], "hypothesis"),
         chk("R1", "conflict per replicate, Eq. 6 values, certainty SD", dict(no_events=out["no_events"]["conflict"], events=out["events"]["conflict"], eq6=[e0, e1], certainty_sd=res["certainty_sd"]), True, "reporting")]
    return res, c

def value_divergence(P, rng):
    """Synthetic panel in the spirit of P11's measures (not WVS data): C countries in R regions, I items on a 0-1 scale, W waves.
    Region effects grow by 'region_drift' per wave and country idiosyncrasies shrink toward the region mean by 'pull' per wave.
    Computes P11's 'value variation' (SD of country means per item, averaged over items) globally and within regions, and
    'value distinctiveness' (mean |country mean - global median|)."""
    C, R, I, W = P["countries"], P["regions"], P["items"], P["waves"]; reg = np.arange(C) % R
    base = rng.uniform(0.3, 0.7, I); rdir = rng.normal(0, 1, (R, I)); idio = rng.normal(0, P["idio_sd"], (C, I)); rows = []
    for w in range(W):
        X = np.clip(base + P["region_drift"] * w * rdir[reg] + idio * (1 - P["pull"]) ** w + rng.normal(0, P["noise"], (C, I)), 0, 1)
        g = X.std(0, ddof=1).mean(); within = np.mean([X[reg == r].std(0, ddof=1).mean() for r in range(R)])
        dist = np.abs(X - np.median(X, 0)).mean(); rows.append(dict(wave=w + 1, global_variation=float(g), within_region_variation=float(within), distinctiveness=float(dist)))
    gv = [r["global_variation"] for r in rows]; wv = [r["within_region_variation"] for r in rows]
    t = np.arange(W); slope = lambda y: float(np.polyfit(t, y, 1)[0])
    # code check: two-point configuration with known SD
    x2 = np.array([0.4, 0.6]); sd2 = float(x2.std(ddof=1))
    c = [chk("V1", "SD routine: two countries at 0.4 and 0.6 give SD = 0.141421 (ddof 1)", sd2, abs(sd2 - 0.1414213562) < 1e-9),
         chk("H1", "global value variation rises across waves (positive slope) while within-region variation falls (negative slope): divergence globally, convergence regionally is jointly possible",
             [slope(gv), slope(wv)], slope(gv) > 0 and slope(wv) < 0, "hypothesis"),
         chk("R1", "measures by wave", rows, True, "reporting")]
    return dict(waves=rows, slope_global=slope(gv), slope_within=slope(wv)), c


KINDS = {k: v for k, v in dict(globals()).items() if callable(v) and not k.startswith('_') and k != 'chk' and getattr(v, '__module__', None) == '__main__'}

if __name__ == "__main__":
    P, H, t0 = R.start(sys.argv[1]); rng = np.random.default_rng(P["seed"])
    res, checks = KINDS[P["kind"]](P, rng); R.finish(H, P, res, checks, t0)
