import networkx as nx
from itertools import combinations
from functools import reduce

def td(g):
    nodes=list(g); n=len(nodes)
    masks=[sum(1<<i for i,v in enumerate(nodes) if g.has_edge(u,v)) for u in nodes]
    for k in range(2,n+1):
        for I in combinations(masks,k):
            if reduce(int.__or__,I,0)==(1<<n)-1: return k

def hh(g):
    a=sorted(dict(g.degree()).values(),reverse=True); k=0
    while 0 not in a:
        d=a.pop(0); a=sorted([v-(i<d) for i,v in enumerate(a)],reverse=True); k+=1
    return k

counts={208:0,235:0,290:0,305:0}
for g in nx.graph_atlas_g():
    n=len(g)
    if n<2 or not nx.is_connected(g): continue
    t=td(g); m=n*(n-1)//2-g.number_of_edges()
    if 2*m+3<=6*len(nx.max_weight_matching(g,maxcardinality=True)):
        states={(1<<i,i) for i in g}
        for _ in range(n-1):
            states={(S|1<<j,j) for S,i in states for j in g[i] if not S>>j&1}
        assert states
        counts[208]+=1
    ecc=nx.eccentricity(g); B={i for i in g if ecc[i]==max(ecc.values())}
    e=max(nx.multi_source_dijkstra_path_length(g,B).values())
    assert 3*t>=2*e+3*nx.is_bipartite(g); counts[235]+=1
    if n>2:
        assert t<=hh(g)*max(dict(g.degree()).values()); counts[290]+=1
        h=nx.complement(g)
        if h.number_of_edges():
            M=max(len(set(h[u])|set(h[v])) for u,v in h.edges)
            assert t<=(2*M+2)//3; counts[305]+=1
assert counts=={208:235,235:995,290:994,305:989}
print(counts)
