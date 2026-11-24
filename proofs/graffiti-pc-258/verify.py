import networkx as nx
from itertools import combinations
def td(g):
    V=set(g)
    for k in range(2,len(g)+1):
        for S in combinations(g,k):
            if set().union(*(set(g[v]) for v in S))==V: return k
count=0
for g in nx.graph_atlas_g():
    n=len(g)
    if n<2 or not nx.is_connected(g): continue
    t=td(g)
    if n==2: L=2
    else:
        L=max(n-k for k in range(1,n-1) for s in combinations(g,k)
              if nx.is_connected(g.subgraph(s)) and set(s)|set().union(*(set(g[v]) for v in s))==set(g))
    E=max(sum(d%2==0 for d in ds.values()) for _,ds in nx.all_pairs_shortest_path_length(g))
    assert t*L>=2*E
    count+=1
assert count==995
print(count)
