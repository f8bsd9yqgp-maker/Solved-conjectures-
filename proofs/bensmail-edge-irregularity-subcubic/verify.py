from itertools import combinations
from fractions import Fraction
E={(0,5),(0,6),(1,2),(1,5),(1,6),(2,3),(3,4),(5,6)}
ROOT=4

def degrees(edges):
    d={}
    for u,v in edges:
        d[u]=d.get(u,0)+1;d[v]=d.get(v,0)+1
    return d

def bad(edges):
    d=degrees(edges)
    return [(u,v) for u,v in edges if d[u]==d[v]]

checks=0
for k in range(3):
    for D in combinations(sorted(E),k):
        K=E-set(D); assert any(ROOT not in e for e in bad(K)), D
        checks+=1
assert checks==37
D={(0,5),(1,5),(2,3)}
assert all(ROOT in e for e in bad(E-D))
assert degrees(E-D)[3]==1

def graph(k):
    assert k>=2
    C={(i,i+1) for i in range(k-1)}
    leaves=[];nextv=k
    for i in range(k):
        for _ in range(2 if i in (0,k-1) else 1):
            C.add((i,nextv));leaves.append(nextv);nextv+=1
    G=set(C);blocks=[]
    for root in leaves:
        for _ in range(2):
            f={4:root}
            for x in range(7):
                if x!=4:f[x]=nextv;nextv+=1
            B={tuple(sorted((f[a],f[b]))) for a,b in E}
            assert not G&B;G|=B;blocks.append(B)
    assert len(G)==18*k+33
    assert max(degrees(G).values())==3 and len(degrees(G))==14*k+26
    return G,C,blocks

for k in range(2,201):
    G,C,B=graph(k)
    path={(i,i+1) for i in range(k-1)}
    assert all(sum(bool(set(e)&set(f)) for f in path)<=3 for e in C)
    assert len(B)==2*(k+2)
    lower=3*len(B)+(k-1+2)//3
    assert Fraction(lower)-Fraction(len(G),3)==1+(k-1+2)//3
print('37 rooted deletion cases verified; graph counts, degree bound, disjointness and path-conflict incidence verified for k=2..200.')
