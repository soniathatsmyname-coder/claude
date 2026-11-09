import random, json, math
random.seed(7)
W,H=0.30,0.45
nx,ny=7,10
pts=[]
for i in range(nx):
    for j in range(ny):
        x=-W/2+(i+0.5)*W/nx+random.uniform(-0.35,0.35)*W/nx
        y=(j+0.5)*H/ny+random.uniform(-0.35,0.35)*H/ny
        pts.append((x,y))
def clip(poly,a,b,c):  # keep a*x+b*y<=c
    out=[]
    n=len(poly)
    for k in range(n):
        p=poly[k];q=poly[(k+1)%n]
        fp=a*p[0]+b*p[1]-c; fq=a*q[0]+b*q[1]-c
        if fp<=0: out.append(p)
        if fp*fq<0:
            t=fp/(fp-fq); out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
    return out
parts=[]
gap=0.004
for idx,(px,py) in enumerate(pts):
    poly=[(-W/2,0),(W/2,0),(W/2,H),(-W/2,H)]
    for (qx,qy) in pts:
        if (qx,qy)==(px,py): continue
        a,b=qx-px,qy-py; d=math.hypot(a,b)
        c=(qx*qx+qy*qy-px*px-py*py)/2 - gap*d
        poly=clip(poly,a,b,c)
        if not poly: break
    if len(poly)<3: continue
    parts.append({"name":f"celda {idx}","shape":"extrude","material":"paintMatteBlack","axis":"z","depth":0.004,
                  "outline":[[round(x,4),round(y,4)] for x,y in poly],"position":[0,0,0]})
# frame
parts.append({"name":"marco sup","shape":"box","material":"metalBlackSteel","size":[0.32,0.01,0.006],"position":[0,H+0.005,0]})
parts.append({"name":"marco inf","shape":"box","material":"metalBlackSteel","size":[0.32,0.01,0.006],"position":[0,-0.005,0]})
parts.append({"name":"marco lat","shape":"box","material":"metalBlackSteel","size":[0.01,0.47,0.006],"position":[0.155,H/2,0],"mirror":"x"})
print(json.dumps(parts))
print(len(parts),file=__import__('sys').stderr)
