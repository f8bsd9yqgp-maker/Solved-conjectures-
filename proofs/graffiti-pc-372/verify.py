import itertools as it
import networkx as nx
count=0
for g in nx.graph_atlas_g():
    if len(g)<3 or not nx.is_connected(g): continue
    V=set(g); n=len(V); deg=dict(g.degree()); M={v for v in V if deg[v]==max(deg.values())}; A={v for v in V if deg[v]==min(deg.values())}; P={v for v in V if deg[v]==1}
    N=lambda s:set().union(*(set(g[v]) for v in s))
    inds=[set(s) for k in range(n+1) for s in it.combinations(V,k) if g.subgraph(s).number_of_edges()==0]
    crit=max((len(s)-len(N(s)),len(s)) for s in inds)
    H=set().union(*(s for s in inds if (len(s)-len(N(s)),len(s))==crit))
    even={v:sum(d%2==0 for d in nx.single_source_shortest_path_length(g,v).values()) for v in V}
    for ext in (min,max):
        De={v for v in V if even[v]==ext(even.values())}
        assert len(H)<=n-len(A)+n-len(M)+g.subgraph(De).number_of_edges()
    if n>3:
        i=min(len(s) for s in inds if s|N(s)==V)
        S=N(P); d=max(nx.core_number(nx.complement(g)).values()); dm=min(dict(g.subgraph(M).degree()).values())
        assert i<=n-len(S)+min(2*x-n for x in even.values())*nx.is_bipartite(g)
        assert i<=len(M)+2*(d//2)
        assert i<=d+dm
    count+=1
assert count==994
print(count, 'connected graphs; 992 of order >=4')
npass=p2=0
for n in range(3,13):
    for g in nx.nonisomorphic_trees(n):
        V=set(g); E=list(g.edges()); S={next(iter(g[v])) for v in g if g.degree(v)==1}; N=lambda s:set().union(*(set(g[v]) for v in s))
        t=len(S)+next(k for k in range(n-len(S)+1) if any(N(S|set(s))==V for s in it.combinations(V-S,k)))
        p=next(k+1 for k in range(len(E)+1) if any(max(dict(h.degree()).values(),default=0)<=2 for rem in it.combinations(E,k) for h in [nx.Graph(g.edge_subgraph(set(E)-set(rem)))]))
        if p>1:
            mu=len(nx.max_weight_matching(g,maxcardinality=True))
            assert t*(p-1)>=mu
            npass+=1; p2+=p==2
assert (npass,p2)==(975,84)
print(npass,p2)
