"""Exhaustive exact checks for WOWII 342,343,344,348,361 on nonisomorphic trees of orders 3–12."""
import networkx as nx
from itertools import combinations
count=0
mins={k:10000 for k in (342,343,344,348,361)}
for n in range(3,13):
    for g in nx.nonisomorphic_trees(n):
        masks=[sum(1<<u for u in g[v]) for v in range(n)]
        full=(1<<n)-1
        def covers(comb):
            c=0
            for v in comb: c|=masks[v]
            return c==full
        t=next(k for k in range(2,n+1) if any(covers(comb) for comb in combinations(range(n),k)))
        deg=dict(g.degree())
        L={v for v in g if deg[v]==1}
        S={next(iter(g[v])) for v in L}
        D2={v for v in g if deg[v]==2}
        i=sum(g.subgraph(S).degree(v)==0 for v in S)
        a=su=0
        for d in sorted(deg.values()):
            if su+d>n-1: break
            su+=d; a+=1
        cs=nx.number_connected_components(g.subgraph(S|L))
        cd=nx.number_connected_components(g.subgraph(D2))
        q=len(set().union(*(set(g[v]) for v in D2))-D2)
        slacks={342:a+(i+1)//2-t,344:a-1+cs-t,348:3*t-2*q,361:t-i-len(nx.center(g))}
        if cd: slacks[343]=a+(cd+1)//2-t
        for k,v in slacks.items():
            assert v>=0,(k,n,list(g.edges()),v)
            mins[k]=min(mins[k],v)
        count+=1
assert count==985
assert mins=={342:0,343:0,344:0,348:2,361:0}
print(count,mins)
