import os, sys, json, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "tools")); import execrecord as ER
H=os.path.dirname(os.path.abspath(__file__)); P=json.load(open(f"{H}/params.json")); t0=ER.now(); os.makedirs(f"{H}/outputs",exist_ok=True)
d=P["daisy"]
def temps(ab,aw,L):
    ag=d["P"]-ab-aw; A=ag*d["Ag"]+ab*d["Ab"]+aw*d["Aw"]+(1-d["P"])*d["Ag"]
    Te=(d["S"]*L*(1-A)/d["sigma_SB"])**0.25-273; return Te, d["q"]*(A-d["Ab"])+Te, d["q"]*(A-d["Aw"])+Te
beta=lambda T:max(0.0,1-0.003265*(22.5-T)**2)
def sweep(Ls,life=True):
    ab=aw=d["seed_area"] if life else 0.0; rows=[]
    for L in Ls:
        for _ in range(d["steps"]):
            Te,Tb,Tw=temps(ab,aw,L); x=d["P"]-ab-aw
            ab+=d["dt"]*ab*(x*beta(Tb)-d["gamma"]); aw+=d["dt"]*aw*(x*beta(Tw)-d["gamma"])
            if life: ab=max(ab,d["seed_area"]); aw=max(aw,d["seed_area"])
        rows.append((round(L,3),*temps(ab,aw,L)[:1],ab,aw))
    return rows
L=np.round(np.arange(d["L"][0],d["L"][1]+1e-9,d["L"][2]),3)
up=sweep(L); down=sweep(L[::-1]); dead=sweep(L,False)
def band(rows):
    ok=[r[0] for r in rows if abs(r[1]-22.5)<=10]; 
    if not ok: return 0.0,None
    # longest contiguous run
    s=sorted(ok); best=(s[0],s[0]); cur=[s[0],s[0]]
    for v in s[1:]:
        if round(v-cur[1],3)<=0.0101: cur[1]=v
        else: cur=[v,v]
        if cur[1]-cur[0]>best[1]-best[0]: best=tuple(cur)
    return round(best[1]-best[0],3),best
wl,bl=band(up); wd,bd=band(dead)
alive=lambda rows:[r[0] for r in rows if r[2]>0.02 or r[3]>0.02]
au=alive(up); ad=alive(down)
import csv
for name,rows in (("daisy_up",up),("daisy_down",down),("lifeless",dead)):
    with open(f"{H}/outputs/{name}.csv","w",newline="") as fh: w=csv.writer(fh,lineterminator="\n"); w.writerow(["L","Te_C","a_black","a_white"]); w.writerows(rows)
# Part B
g=P["geomag"]; lines=[l.split() for l in open(f"{H}/{g['igrf_file']}") if not l.startswith("#")]
hdr=lines[1]; years=[float(y) for y in hdr[3:-1]]
co={(r[0],int(r[1]),int(r[2])):[float(v) for v in r[3:-1]] for r in lines[2:]}
M=[(4*np.pi*g["RE_m"]**3/g["mu0"])*np.sqrt(co[("g",1,0)][i]**2+co[("g",1,1)][i]**2+co[("h",1,1)][i]**2)*1e-9 for i in range(len(years))]
dip=dict(zip(years,M)); M0,M1=dip[1900.0],dip[max(years)]
tau={str(s):g["mu0"]*s*g["Rc_m"]**2/np.pi**2/3.15576e7 for s in g["sigma_S_per_m"]}
res=dict(daisy=dict(width_life=wl,band_life=bl,width_lifeless=wd,band_lifeless=bd,alive_up=[min(au),max(au)] if au else None,alive_down=[min(ad),max(ad)] if ad else None),
  geomag=dict(dipole_moment_Am2={str(k):v for k,v in dip.items()},change_pct_1900_to_last=100*(M1-M0)/M0,last_epoch=max(years),free_decay_tau_yr=tau,ratio_paleo_to_max_tau=g["paleo_min_yr"]/max(tau.values())))
json.dump(res,open(f"{H}/outputs/results.json","w"),indent=2)
chk=[dict(id="E1",expect="life band width >= 3x lifeless",observed=[wl,wd],result="Pass" if wl>=3*max(wd,1e-9) else "Fail"),
 dict(id="E2",expect="hysteresis: alive ranges differ up vs down",observed=[res['daisy']['alive_up'],res['daisy']['alive_down']],result="Pass" if res['daisy']['alive_up']!=res['daisy']['alive_down'] else "Fail"),
 dict(id="E3",expect="dipole moment decreases 1900->latest",observed=round(res['geomag']['change_pct_1900_to_last'],3),result="Pass" if M1<M0 else "Fail"),
 dict(id="E4",expect="tau <= 1e6 yr for all sigma",observed={k:round(v) for k,v in tau.items()},result="Pass" if max(tau.values())<=1e6 else "Fail")]
ER.write(H,"SIM-R6-C0",P,[f"{H}/outputs/{x}" for x in ("results.json","daisy_up.csv","daisy_down.csv","lifeless.csv")],chk,t0)
