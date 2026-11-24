import itertools as it
import networkx as nx
from math import prod

count=0
for g in nx.graph_atlas_g():
    if len(g)<2 or not nx.is_connected(g): continue
    V=set(g); n=len(g)
    subsets=[set(s) for k in range(1,n+1) for s in it.combinations(g,k)]
    def N(s): return set().union(*(set(g[v]) for v in s))
    t=next(len(s) for s in subsets if N(s)==V)
    L=max(2,n-next(len(s) for s in subsets if N(s)|s==V and nx.is_connected(g.subgraph(s))))
    deg=dict(g.degree()); ecc=nx.eccentricity(g)
    for X in ({v for v in g if deg[v]==max(deg.values())},
              {v for v in g if ecc[v]==max(ecc.values())},
              {v for v in g if deg[v]==2}):
        assert t*L>=2*len(N(X)-X)
    if L>=3:
        for X in subsets: assert t*L>=2*len(N(X)-X)
    count+=1
assert count==995
print("Atlas:",count)
for d in range(14,32,2):
    for m in range(3,6):
        g=nx.path_graph(d+1)
        g.add_edges_from((0,d+1+i) for i in range(m))
        g.add_edges_from((d,d+1+m+i) for i in range(m))
        h=nx.power(g,2); deg=dict(h.degree())
        M=[v for v in h if deg[v]==max(deg.values())]
        assert M==[1,d-1]
        assert nx.diameter(g)+1==d+3
        assert 3*nx.shortest_path_length(h,*M)>d+3
        def dp(v,p):
            ch=[dp(w,v) for w in g[v] if w!=p]
            incl=(1+sum(z[0][0] for z in ch),prod(z[0][1] for z in ch))
            excl=(sum(max(z[0][0],z[1][0]) for z in ch),
                  prod(sum(x[1] for x in z if x[0]==max(y[0] for y in z)) for z in ch))
            return excl,incl
        z=dp(0,None); a=max(x[0] for x in z)
        assert a==2*m+d//2
        assert sum(x[1] for x in z if x[0]==a)==1
print("Counterexample family: 27 instances passed")
