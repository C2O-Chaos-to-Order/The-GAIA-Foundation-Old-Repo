"""SIM-R5-C2: spontaneous vs perturbational Lempel-Ziv complexity in a modular Kuramoto network (toy).
Motivation: W13 (Schartner et al. 2015) - Lempel-Ziv complexity of spontaneous EEG decreases under propofol; Kuramoto simulations show
measures capture distinct 'flavours' of complexity. W11 (Sarasso et al. 2021) - complexity measures as markers of consciousness; the
perturbational approach (PCI) assesses the causal structure by perturbing and measuring the complexity of the response.
Our toy asks only how these MEASURES behave as network coupling changes; it says nothing about consciousness itself."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
def lz76(s):
    """Kaspar & Schuster (1987) LZ76 complexity counter for a binary sequence."""
    s = list(s); n = len(s)
    if n < 2: return n
    i, k, l, c, kmax = 0, 1, 1, 1, 1
    while True:
        if s[i+k-1] == s[l+k-1]:
            k += 1
            if l+k > n: c += 1; break
        else:
            kmax = max(k, kmax); i += 1
            if i == l:
                c += 1; l += kmax
                if l+1 > n: break
                i, k, kmax = 0, 1, 1
            else: k = 1
    return c
def lz_norm(bits):
    b = np.asarray(bits).astype(int).ravel(); n = len(b); p = b.mean()
    if p in (0, 1): return 0.0
    H = -(p*np.log2(p)+(1-p)*np.log2(1-p)); return lz76(b)*np.log2(n)/(n*H)
def coupling(N, modules, k_in, k_out):
    m = np.repeat(np.arange(modules), N//modules); C = np.where(m[:, None] == m[None, :], k_in, k_out); np.fill_diagonal(C, 0); return C/N
def simulate(C, omega, theta0, noise, dt, T, kick=None):
    th = theta0.copy(); X = np.empty((T, len(th)))
    for t in range(T):
        if kick is not None and t == kick[0]: th = th + kick[1]
        th = th + dt*(omega + (C*np.sin(th[None, :]-th[:, None])).sum(1)) + noise[t]
        X[t] = np.sin(th)
    return X
def spont_lz(X, every=1):
    X = X[::every]; B = X > np.median(X, 0); return lz_norm(B.T)  # channel-wise concatenation (Schartner-style), normalised by source entropy
def pci_like(C, omega, rng, p):
    """Perturb a set of units at the start of a window and compare with an unperturbed twin run driven by the SAME noise;
    binarise |difference| > thresh per unit and sample; PCI-like = source-entropy-normalised LZ of the response matrix."""
    N = C.shape[0]; th = rng.uniform(0, 2*np.pi, N); nz = np.sqrt(p["dt"])*p["noise"]*rng.standard_normal((p["burn"]+p["T"], N))
    for t in range(p["burn"]): th = th + p["dt"]*(omega + (C*np.sin(th[None, :]-th[:, None])).sum(1)) + nz[t]
    kick = np.zeros(N); kick[p["kick_units"]] = p["kick_size"]
    a = simulate(C, omega, th, nz[p["burn"]:], p["dt"], p["T"]); b = simulate(C, omega, th, nz[p["burn"]:], p["dt"], p["T"], kick=(0, kick))
    B = (np.abs(a-b) > p["thresh"])[::p["sample_every"]]; frac = B.mean()
    return (lz_norm(B.T) if 0 < frac < 1 else 0.0), float(frac)
def run_point(N, modules, k_in, k_out, p, seed):
    rng = np.random.default_rng(seed); C = coupling(N, modules, k_in, k_out); omega = rng.normal(p["omega_mean"], p["omega_sd"], N)
    th0 = rng.uniform(0, 2*np.pi, N); nz = np.sqrt(p["dt"])*p["noise"]*rng.standard_normal((p["burn"]+p["T"], N))
    X = simulate(C, omega, th0, nz, p["dt"], p["burn"]+p["T"])[p["burn"]:]
    s = spont_lz(X, p["sample_every"]); pc, frac = pci_like(C, omega, rng, p); return dict(spont_lz=s, pci_like=pc, response_fraction=frac)
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X_ = P["experiments"]; p = P["net"]; res = {}; chk = []
    if prev: res["carried_from_prev"] = {k: prev[k] for k in P.get("carry", []) if k in prev}
    from scipy.stats import spearmanr
    if "lz_validation" in X_:
        rng = np.random.default_rng(1); n = X_["lz_validation"]["n"]
        r = lz_norm(rng.integers(0, 2, n)); per = lz_norm(np.tile([0, 1, 1, 0], n//4)); c0 = lz76([0]*n)
        res["lz_validation"] = dict(random=r, periodic=per, constant_raw=c0, textbook_example=lz76([int(x) for x in "0001101001000101"]))
        chk.append(R.chk("Z1", "random binary sequence: normalised LZ in [0.9, 1.1]", r, 0.9 <= r <= 1.1))
        chk.append(R.chk("Z2", "period-4 sequence: normalised LZ < 0.05", per, per < 0.05))
        chk.append(R.chk("Z3", "Kaspar-Schuster textbook example 0001101001000101 has complexity 6 (0|001|10|100|1000|101)", res["lz_validation"]["textbook_example"], res["lz_validation"]["textbook_example"] == 6))
    if "coupling_sweep" in X_:
        e = X_["coupling_sweep"]; rows = []
        for K in e["K"]:
            rows.append(dict(K=K, **run_point(e["N"], e["modules"], K, K*e["out_ratio"], p, e["seed"])))
        res["coupling_sweep"] = rows; Ks = [r["K"] for r in rows]; S = [r["spont_lz"] for r in rows]; Pc = [r["pci_like"] for r in rows]
        rs = float(spearmanr(Ks, S).correlation); res["spont_spearman"] = rs
        if e.get("test_spont"):
            chk.append(R.chk("S1", "spontaneous LZ falls as coupling rises (Spearman <= -0.8): maximal for independent units", rs, rs <= -0.8, kind="hypothesis"))
        if e.get("test_pci"):
            i = int(np.argmax(Pc)); interior = 0 < i < len(Pc)-1; ratio = Pc[i]/max(Pc[0], Pc[-1], 1e-9)
            res["pci_peak_K"] = Ks[i]
            chk.append(R.chk("P1", "PCI-like complexity peaks at an intermediate coupling (interior maximum, >= 1.5x both ends)", [Ks[i], ratio], interior and ratio >= 1.5, kind="hypothesis"))
    if "noise_dissociation" in X_:
        e = X_["noise_dissociation"]; a = run_point(e["N"], e["modules"], 0.0, 0.0, dict(p, noise=e["noise"]), e["seed"])
        Kp = (prev or {}).get("pci_peak_K") or (prev or {}).get("carried_from_prev", {}).get("pci_peak_K") or e["K_fallback"]
        b = run_point(e["N"], e["modules"], Kp, Kp*e["out_ratio"], p, e["seed"]); res["noise_dissociation"] = dict(uncoupled_noisy=a, at_pci_peak=b, K_peak_used=Kp)
        chk.append(R.chk("N1", "dissociation: uncoupled noisy network has HIGHER spontaneous LZ but LOWER PCI-like than the network at the PCI peak", [a, b],
                         a["spont_lz"] > b["spont_lz"] and a["pci_like"] < b["pci_like"], kind="hypothesis"))
    if "disconnection" in X_:
        e = X_["disconnection"]; rows = []
        Kp = (prev or {}).get("carried_from_prev", {}).get("pci_peak_K") or (prev or {}).get("pci_peak_K") or e["K_fallback"]
        for r_ in e["out_ratio"]:
            rows.append(dict(out_ratio=r_, **run_point(e["N"], e["modules"], Kp, Kp*r_, p, e["seed"])))
        res["disconnection"] = dict(K_in=Kp, rows=rows); rr = float(spearmanr(e["out_ratio"], [r["pci_like"] for r in rows]).correlation)
        chk.append(R.chk("D1", "'anaesthesia-like' loss of between-module coupling lowers PCI-like (Spearman(out_ratio, PCI) >= 0.8)", rr, rr >= 0.8, kind="hypothesis"))
    if "robustness" in X_:
        e = X_["robustness"]; out = []
        for N in e["N"]:
            for sd in e["seeds"]:
                Pc = [run_point(N, e["modules"], K, K*e["out_ratio"], p, sd)["pci_like"] for K in e["K"]]; i = int(np.argmax(Pc))
                out.append(dict(N=N, seed=sd, peak_K=e["K"][i], interior=0 < i < len(Pc)-1, ratio=Pc[i]/max(Pc[0], Pc[-1], 1e-9)))
        res["robustness"] = out; f = float(np.mean([o["interior"] and o["ratio"] >= 1.5 for o in out]))
        chk.append(R.chk("R1", "P1 holds in >= 80% of (size, seed) configurations", f, f >= 0.8, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
