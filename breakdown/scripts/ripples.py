import math, json, sys
def profile(R, lam, A0, A1, h0=0.0025, taper=0.08, ppw=6, phase=0.0):
    n = int(R/lam*ppw)
    top=[]
    for i in range(n, -1, -1):
        r = R*i/n
        t = r/R
        A = A0 + (A1-A0)*t
        h = h0
        if r > R-taper:
            k = (R-r)/taper
            A *= k; h = 0.0005 + (h0-0.0005)*k
        top.append([round(r,4), round(h + A*math.sin(2*math.pi*r/lam + phase),5)])
    return [[0,0],[R,0]] + top[0:] [:-1] + [[0, top[-1][1]]]
out = {
 "A": profile(1.0, 0.045, 0.0018, 0.0006),
 "B": profile(1.1, 0.06, 0.0015, 0.0005, phase=1.3),
 "C": profile(0.9, 0.035, 0.0012, 0.0005, phase=2.1),
}
for k,v in out.items():
    part=[{"name":"ondas","shape":"lathe","material":"groundPoolWater","color":"#05080a","profile":v,"position":[0,0,0]}]
    open(f'/tmp/claude-0/-home-user-claude/9733e48e-7a84-5400-b19d-228c1dc52b81/scratchpad/rip_{k}.json','w').write(json.dumps(part))
    print(k, len(v), min(p[1] for p in v[2:]), max(p[1] for p in v))
