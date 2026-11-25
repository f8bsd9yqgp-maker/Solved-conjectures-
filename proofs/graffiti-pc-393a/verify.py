import itertools as it
import networkx as nx

def subsets(V):
    return (set(s) for k in range(len(V)+1) for s in it.combinations(V,k))

counts={k:0 for k in ['393a','393b','393c','412a','412b','412e','450']}
bip=0
for g in nx.graph_atlas_g():
    n=len(g)
    if n<3 or not nx.is_connected(g):continue
    V=set(g); deg=dict(g.degree()); P={v for v in V if deg[v]==1}
    N=lambda s:set().union(*(set(g[v]) for v in s))
    S=N(P); X=N(S); A2={v for v in V if deg[v]==2}; B={v for v in V if deg[v]<=2}
    pn=lambda s:sum(len(set(g[v])&s)==1 for v in V)
    sets=list(subsets(V))
    inds=[s for s in sets if not g.subgraph(s).number_of_edges()]
    score=max((len(s)-len(N(s)),len(s)) for s in inds)
    H=set().union(*(s for s in inds if (len(s)-len(N(s)),len(s))==score))
    c=max(map(len,nx.connected_components(g.subgraph(S))),default=0)
    assert len(H)>=c
    counts['412a']+=1;counts['412b']+=1
    if nx.is_bipartite(g):
        alpha=lambda X:max(len(s) for s in inds if s<=X)
        assert len(H)>=c+alpha(V-X),(g.edges(),'412a')
        assert len(H)>=c+alpha(A2),(g.edges(),'412b')
        assert len(H)>=1+max(dict(g.subgraph(X).degree()).values(),default=0),(g.edges(),'412e')
        bip+=1;counts['412e']+=1
    D2=min(len(s) for s in sets if all(len(set(g[v])&s)>=2 for v in V-s))
    assert D2<=n-len(X)+len(nx.max_weight_matching(g.subgraph(X),maxcardinality=True))+len(P),(g.edges(),'393a')
    counts['393a']+=1
    assert D2<=n-len(X)+g.subgraph(S).number_of_edges()+pn(S),(g.edges(),'393b')
    assert D2<=n-len(X)+len(S)+pn(P|S),(g.edges(),'393c')
    counts['393b']+=1;counts['393c']+=1
    if n>3:
        a2=max(len(s) for s in sets if max(dict(g.subgraph(s).degree()).values(),default=0)<=1)
        assert a2<=pn(A2)+n-len(S)+pn(B),(g.edges(),'450')
        counts['450']+=1
assert counts=={'393a':994,'393b':994,'393c':994,'412a':994,'412b':994,'412e':70,'450':992}
assert bip==70
print(counts,'bipartite',bip)
