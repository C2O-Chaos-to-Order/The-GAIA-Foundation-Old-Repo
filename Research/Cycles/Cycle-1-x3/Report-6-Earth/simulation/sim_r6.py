"""SIM-R6 (Cycle 1+): Daisyworld regulation robustness and a toy adaptation test; geomagnetic spectrum (IGRF-14) and free-decay times.
Daisyworld is a parable model (Watson & Lovelock 1983, S24). Adaptation is our own toy design and is not a reproduction of any published study."""
import sys, os, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")); import runner as R
SB = 5.670374419e-8
def daisy(d, Ls, life=True, adapt=0.0):
    ab = aw = d["seed_area"] if life else 0.0; Tob = Tow = d["T_opt"]; rows = []
    for L in Ls:
        for _ in range(d["steps"]):
            ag = d["P"]-ab-aw; A = ag*d["Ag"]+ab*d["Ab"]+aw*d["Aw"]+(1-d["P"])*d["Ag"]
            Te = (d["S"]*L*(1-A)/SB)**0.25-273; Tb = d["q"]*(A-d["Ab"])+Te; Tw = d["q"]*(A-d["Aw"])+Te
            bb = max(0.0, 1-0.003265*(Tob-Tb)**2); bw = max(0.0, 1-0.003265*(Tow-Tw)**2)
            ab += d["dt"]*ab*(ag*bb-d["gamma"]); aw += d["dt"]*aw*(ag*bw-d["gamma"])
            if life: ab = max(ab, d["seed_area"]); aw = max(aw, d["seed_area"])
            if adapt:
                Tob += d["dt"]*adapt*(Tb-Tob); Tow += d["dt"]*adapt*(Tw-Tow)
                if d.get("topt_max_shift") is not None:
                    m = d["topt_max_shift"]; Tob = min(max(Tob, d["T_opt"]-m), d["T_opt"]+m); Tow = min(max(Tow, d["T_opt"]-m), d["T_opt"]+m)
        ag = d["P"]-ab-aw; A = ag*d["Ag"]+ab*d["Ab"]+aw*d["Aw"]+(1-d["P"])*d["Ag"]; Te = (d["S"]*L*(1-A)/SB)**0.25-273
        rows.append((float(L), float(Te), float(ab), float(aw), float(Tob), float(Tow)))
    return rows
def band(rows, centre, half):
    ok = [abs(r[1]-centre) <= half for r in rows]; best = cur = 0; step = rows[1][0]-rows[0][0]
    for o in ok: cur = cur+1 if o else 0; best = max(best, cur)
    return round(max(best-1, 0)*step, 4)
def main():
    P, prev, H = R.start(sys.argv[1]); t0 = R.now(); X = P["experiments"]; res = {}; chk = []
    base = P["daisy"]; Ls = np.round(np.arange(*base["L"]), 4)
    if "daisy_sensitivity" in X:
        s = X["daisy_sensitivity"]; rows = []
        dead = daisy(base, Ls, life=False)
        Te_an = [(base["S"]*L*(1-base["Ag"])/SB)**0.25-273 for L in Ls]
        chk.append(R.chk("D0", "lifeless planet matches analytic radiative balance (max |dT| < 1e-9 C)", float(np.max(np.abs(np.array([r[1] for r in dead])-Te_an))), np.max(np.abs(np.array([r[1] for r in dead])-Te_an)) < 1e-9))
        wd = band(dead, base["T_opt"], base["band_half"])
        for g in s["gamma"]:
            for q in s["q"]:
                for ab_, aw_ in s["albedo_pairs"]:
                    d = dict(base, gamma=g, q=q, Ab=ab_, Aw=aw_); w = band(daisy(d, Ls), base["T_opt"], base["band_half"])
                    rows.append(dict(gamma=g, q=q, Ab=ab_, Aw=aw_, width_life=w, width_lifeless=wd, ratio=w/wd if wd else None))
        frac = float(np.mean([r["ratio"] is not None and r["ratio"] >= s["ratio_threshold"] for r in rows]))
        res["daisy_sensitivity"] = dict(rows=rows, width_lifeless=wd, frac_configs_regulating=frac)
        chk.append(R.chk("D1", f"regulation (band width >= {s['ratio_threshold']}x lifeless) holds in >= 80% of parameter configurations", frac, frac >= 0.8, kind="hypothesis"))
        chk.append(R.chk("D2", "report the configurations where regulation fails", [r for r in rows if not (r["ratio"] and r["ratio"] >= s["ratio_threshold"])], True, kind="reporting"))
    if "adaptation" in X:
        a = X["adaptation"]; out = []
        w0 = band(daisy(base, Ls), base["T_opt"], base["band_half"])
        for rate in a["rates"]:
          for shift in a.get("max_shift", [None]):
            rows = daisy(dict(base, topt_max_shift=shift), Ls, adapt=rate)
            out.append(dict(rate=rate, max_shift=shift, width_life=band(rows, base["T_opt"], base["band_half"]), final_Topt_black=rows[-1][4], final_Topt_white=rows[-1][5],
                            Te_at_L=[(r[0], round(r[1], 3)) for r in rows[::max(1, len(rows)//12)]]))
        res["adaptation"] = dict(no_adaptation_width=w0, rows=out)
        chk.append(R.chk("A0", "adaptation rate 0 reproduces the non-adapting run exactly", [out[0]["width_life"], w0], a["rates"][0] == 0 and out[0]["width_life"] == w0))
        unb = [o["width_life"] for o in out if o["rate"] > 0 and o["max_shift"] is None]
        chk.append(R.chk("A1", "toy: regulation band survives UNBOUNDED adaptation of daisy optimum temperature (min width >= 0.8x non-adapting)", [min(unb), w0], min(unb) >= 0.8*w0, kind="hypothesis"))
        for sh in [x for x in a.get("max_shift", []) if x is not None]:
            bd = [o["width_life"] for o in out if o["rate"] > 0 and o["max_shift"] == sh]
            chk.append(R.chk(f"A_bounded_{sh}", f"toy: regulation band survives adaptation bounded to +/-{sh} C (min width >= 0.8x non-adapting)", [min(bd), w0], min(bd) >= 0.8*w0, kind="hypothesis"))
        chk.append(R.chk("A2", "report optimum-temperature drift per rate and bound", [(o["rate"], o["max_shift"], round(o["final_Topt_black"], 2), round(o["final_Topt_white"], 2), o["width_life"]) for o in out], True, kind="reporting"))
    if "geomag" in X:
        g = X["geomag"]; lines = [l.split() for l in open(os.path.join(H, "..", g["igrf_file"])) if not l.startswith("#")]
        years = [float(y) for y in lines[1][3:-1]]; co = {(r[0], int(r[1]), int(r[2])): [float(v) for v in r[3:-1]] for r in lines[2:]}
        nmax = g["nmax"]; spec = {}; slopes = {}
        for i, y in enumerate(years):
            if y not in g["epochs"]: continue
            Rn = [(n+1)*sum(co[("g", n, m)][i]**2+(co[("h", n, m)][i]**2 if m > 0 else 0) for m in range(n+1)) for n in range(1, nmax+1)]
            Rc = [Rn[n-1]*(g["RE_m"]/g["Rc_m"])**(2*n+4) for n in range(1, nmax+1)]
            ns = np.arange(2, nmax+1); s_s = np.polyfit(ns, np.log10(Rn[1:]), 1)[0]; s_c = np.polyfit(ns, np.log10(Rc[1:]), 1)[0]
            spec[str(y)] = dict(R_surface_nT2=Rn, R_cmb_nT2=Rc); slopes[str(y)] = dict(surface=float(s_s), cmb=float(s_c))
            B0 = np.sqrt(co[("g", 1, 0)][i]**2+co[("g", 1, 1)][i]**2+co[("h", 1, 1)][i]**2)
            if str(y) == str(float(g["epochs"][-1])):
                chk.append(R.chk("G0", "R_1 = 2*(g10^2+g11^2+h11^2) (Lowes-Mauersberger definition)", [Rn[0], 2*B0**2], abs(Rn[0]-2*B0**2) < 1e-6*Rn[0]))
        res["geomag"] = dict(spectra=spec, slopes_log10_per_degree_n2_to_nmax=slopes)
        chk.append(R.chk("G1", "surface spectrum is steep (slope < -0.3 per degree) and the CMB spectrum is near-flat (|slope| < 0.15) in every epoch", slopes,
                         all(v["surface"] < -0.3 and abs(v["cmb"]) < 0.15 for v in slopes.values()), kind="hypothesis"))
        tau = {str(s): g["mu0"]*s*g["Rc_m"]**2/np.pi**2/3.15576e7 for s in g["sigma_S_per_m"]}
        res["free_decay_tau_yr"] = tau; res["paleo_over_max_tau"] = g["paleo_min_yr"]/max(tau.values())
        if "wf" in g:
            w = g["wf"]; res["wiedemann_franz"] = {f"k{k}_T{T}": k/(w["L0"]*T) for k in w["k_W_per_mK"] for T in w["T_K"]}
            res["wf_tau_yr"] = {kk: g["mu0"]*v*g["Rc_m"]**2/np.pi**2/3.15576e7 for kk, v in res["wiedemann_franz"].items()}
        alltau = list(tau.values())+list(res.get("wf_tau_yr", {}).values())
        chk.append(R.chk("G2", "free decay time < 1e6 yr across the whole conductivity range (so a 3.3 Gyr-old field needs regeneration)", max(alltau), max(alltau) < 1e6, kind="hypothesis"))
    R.finish(H, P, res, chk, t0)
if __name__ == "__main__": main()
