"""Exact finite checks for WOWII 365, 376, 377, 380, 381; NetworkX."""
import itertools as it
import networkx as nx
count=0
defined380=0
for n in range(3,13):
    for g in nx.nonisomorphic_trees(n):
        deg=dict(g.degree()); V=set(g)
        S={next(iter(g[v])) for v in V if deg[v]==1}
        M={v for v in V if deg[v]==max(deg.values())}
        I={v for v in M if not set(g[v])&M}
        J={v for v in S if not set(g[v])&S}
        A={v for v in V if deg[v]==2}
        N=lambda s:set().union(*(set(g[v]) for v in s))
        masks=[sum(1<<u for u in g[v]) for v in range(n)]
        full=(1<<n)-1
        forced=sorted(S); rest=sorted(V-S); cover=0
        for v in forced: cover|=masks[v]
        def ok(s):
            c=cover
            for v in s: c|=masks[v]
            return c==full
        t=len(S)+next(k for k in range(len(rest)+1)
                      if any(ok(s) for s in it.combinations(rest,k)))
        assert 3*(t-len(J))>=g.subgraph(A).number_of_edges()+1
        sums={v:sum(nx.single_source_shortest_path_length(g,v).values()) for v in V}
        cent={v for v in V if sums[v]==min(sums.values())}
        med=sorted(deg.values())[n//2]
        assert t>=len(I)+len(cent)
        assert t>=len(I)+med
        C=nx.center(g)
        ecc=max(min(nx.shortest_path_length(g,v,c) for c in C) for v in V)
        if ecc>1:
            assert t*(ecc-1)>=sum(d%2==0 for d in deg.values())
            defined380+=1
        assert t*(max(deg[v] for v in S)-1)>=sum(not set(g[v])&N(S) for v in N(S))
        count+=1
assert (count,defined380)==(985,950)
print(count,defined380)
