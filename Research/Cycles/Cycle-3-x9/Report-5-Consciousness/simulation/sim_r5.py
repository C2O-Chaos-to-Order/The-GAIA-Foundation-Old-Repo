"""SIM-R5-C3: perturbation scaled with network size, and a criticality link (carried item 'R5 perturbation scaled with network size';
new literature X12: criticality in spontaneous EEG predicts PCI). Toy modular Kuramoto network; lz76, lz_norm, coupling, simulate,
spont_lz, pci_like and run_point are copied unchanged from SIM-R5-C2. A 'PCI-like' number in a toy says nothing about consciousness;
the point is whether the measure behaves sensibly once the perturbation is scaled with size."""
import sys, os, json, numpy as np
from scipy.stats import spearmanr
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "tools")); import runner as R
C2IT6 = os.path.join(HERE, "..", "..", "..", "Cycle-2-x6", "Report-5-Consciousness", "simulation", "iter-6", "outputs", "results.json")
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
def scaled(p, N, modules, frac=None):
    q = dict(p); f = p["kick_frac"] if frac is None else frac; q["kick_units"] = list(range(max(1, int(round(f*N)))))
    return q
def sweep(N, modules, Ks, out_ratio, p, seed):
    Pc = [run_point(N, modules, K, K*out_ratio, p, seed)["pci_like"] for K in Ks]; i = int(np.argmax(Pc))
    return dict(N=N, seed=seed, pci=Pc, peak_K=Ks[i], interior=0 < i < len(Pc)-1, ratio=Pc[i]/max(Pc[0], Pc[-1], 1e-9))
def peak_ok(o): return o["interior"] and o["ratio"] >= 1.5
def susceptibility(N, modules, K, out_ratio, p, seed):
    rng = np.random.default_rng(seed); C = coupling(N, modules, K, K*out_ratio); omega = rng.normal(p["omega_mean"], p["omega_sd"], N)
    th = rng.uniform(0, 2*np.pi, N); nz = np.sqrt(p["dt"])*p["noise"]*rng.standard_normal((p["burn"]+p["T"], N)); r = []
    for t in range(p["burn"]+p["T"]):
        th = th + p["dt"]*(omega + (C*np.sin(th[None, :]-th[:, None])).sum(1)) + nz[t]
        if t >= p["burn"]: r.append(abs(np.exp(1j*th).mean()))
    r = np.array(r); return float(N*r.var()), float(r.mean())
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; p = P["net"]; res = {}; chk = []
    if "reproduce" in X:
        c2 = json.load(open(C2IT6)); e = X["reproduce"]; q = dict(p, kick_units=list(range(10)))
        o = sweep(40, 4, e["K"], 0.2, q, 1); ref = [r for r in c2["robustness"] if r["N"] == 40 and r["seed"] == 1][0]
        chk.append(R.chk("V1", "copied code with the Cycle-2 fixed 10-unit kick reproduces Cycle-2 iteration 6 at N=40, seed 1 (peak K and ratio, |diff| < 1e-9)", [o["peak_K"], o["ratio"], ref["peak_K"], ref["ratio"]], o["peak_K"] == ref["peak_K"] and abs(o["ratio"]-ref["ratio"]) < 1e-9))
        z = run_point(24, 4, 2.0, 0.4, dict(p, kick_units=[], kick_size=0.0), 1)["pci_like"]
        chk.append(R.chk("V2", "no perturbation gives PCI-like = 0", z, z == 0.0))
    if "scaled" in X:
        e = X["scaled"]; out = [sweep(N, 4, e["K"], 0.2, scaled(p, N, 4), sd) for N in e["N"] for sd in e["seeds"]]
        res["scaled"] = out; f = float(np.mean([peak_ok(o) for o in out]))
        chk.append(R.chk("H2", "with the kick scaled to one module (N/4 units), the PCI-like peak at intermediate coupling (interior, >= 1.5x both ends) holds in >= 80% of (size, seed) settings, including N=64 where Cycle 2 failed", [f, [(o["N"], o["seed"], o["peak_K"], round(o["ratio"], 3)) for o in out]], f >= 0.8, kind="hypothesis"))
    if "larger" in X:
        e = X["larger"]; out = [sweep(N, 4, e["K"], 0.2, scaled(p, N, 4), 1) for N in e["N"]]; res["larger"] = out
        chk.append(R.chk("H3", "the peak persists at N = 96 and 128 with the scaled kick", [(o["N"], o["peak_K"], o["ratio"]) for o in out], all(peak_ok(o) for o in out), kind="hypothesis"))
    if "kick_size" in X:
        e = X["kick_size"]; out = [dict(kick_size=k, **sweep(e["N"], 4, e["K"], 0.2, scaled(dict(p, kick_size=k), e["N"], 4), 1)) for k in e["sizes"]]; res["kick_size"] = out
        idx = [e["K"].index(o["peak_K"]) for o in out]
        chk.append(R.chk("H4", "peak location is stable (within one grid step) across kick sizes 0.25-2", [(o["kick_size"], o["peak_K"], round(o["ratio"], 3)) for o in out], max(idx)-min(idx) <= 1 and all(peak_ok(o) for o in out), kind="hypothesis"))
    if "threshold" in X:
        e = X["threshold"]; out = [dict(thresh=t, **sweep(e["N"], 4, e["K"], 0.2, scaled(dict(p, thresh=t), e["N"], 4), 1)) for t in e["thresh"]]; res["threshold"] = out
        n = sum(peak_ok(o) for o in out)
        chk.append(R.chk("H5", "intermediate-coupling peak holds for >= 3 of 4 binarisation thresholds", [(o["thresh"], o["peak_K"], round(o["ratio"], 3)) for o in out], n >= 3, kind="hypothesis"))
    if "criticality" in X:
        e = X["criticality"]; sus = [susceptibility(e["N"], 4, K, 0.2, p, 1) for K in e["K"]]; o = sweep(e["N"], 4, e["K"], 0.2, scaled(p, e["N"], 4), 1)
        ks = e["K"][int(np.argmax([s[0] for s in sus]))]; res["criticality"] = dict(K=e["K"], susceptibility=[s[0] for s in sus], mean_r=[s[1] for s in sus], pci=o["pci"], K_sus=ks, K_pci=o["peak_K"])
        chk.append(R.chk("H6", "the coupling that maximises synchrony susceptibility (a criticality proxy) is within one grid step of the PCI-like peak", [ks, o["peak_K"]], abs(e["K"].index(ks)-e["K"].index(o["peak_K"])) <= 1, kind="hypothesis"))
    if "predict" in X:
        e = X["predict"]; xs, ys = [], []
        for N in e["N"]:
            for sd in e["seeds"]:
                for K in e["K"]:
                    xs.append(susceptibility(N, 4, K, 0.2, p, sd)[0]/N); ys.append(run_point(N, 4, K, K*0.2, scaled(p, N, 4), sd)["pci_like"])
        rho = float(spearmanr(xs, ys)[0]); res["predict"] = dict(rho=rho, n=len(xs))
        chk.append(R.chk("H7", "across sizes, seeds and couplings, spontaneous susceptibility predicts PCI-like (Spearman >= 0.6), the toy analogue of X12", rho, rho >= 0.6, kind="hypothesis"))
    if "dissociation" in X:
        e = X["dissociation"]; base = sweep(e["N"], 4, e["K"], 0.2, scaled(p, e["N"], 4), 1); Kp = base["peak_K"]
        hi = run_point(e["N"], 4, Kp, Kp*0.2, scaled(p, e["N"], 4), 1); lo = run_point(e["N"], 4, Kp*e["factor"], Kp*e["factor"]*0.2, scaled(p, e["N"], 4), 1)
        res["dissociation"] = dict(K_peak=Kp, at_peak=hi, reduced=lo); drop = 1-lo["pci_like"]/hi["pci_like"] if hi["pci_like"] else None
        chk.append(R.chk("H8", "halving all coupling from the peak lowers PCI-like by >= 30% while spontaneous LZ rises (dissociation, cf. C2-R5-04)", [drop, hi["spont_lz"], lo["spont_lz"]], drop is not None and drop >= 0.3 and lo["spont_lz"] > hi["spont_lz"], kind="hypothesis"))
    if "replicate" in X:
        e = X["replicate"]; out = [sweep(N, 4, e["K"], 0.2, scaled(p, N, 4), sd) for N in e["N"] for sd in e["seeds"]]; res["replicate"] = out
        n = sum(peak_ok(o) for o in out)
        chk.append(R.chk("H9", "iteration-2 result replicates with new seeds (peak in >= 8 of 9 settings)", [n, [(o["N"], o["seed"], o["peak_K"]) for o in out]], n >= 8, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
