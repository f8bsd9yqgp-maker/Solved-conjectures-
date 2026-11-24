import networkx as nx

count=0
for g in nx.graph_atlas_g():
    if len(g)<3 or not nx.is_connected(g):
        continue
    r=min(g,key=lambda v:sum(nx.single_source_shortest_path_length(g,v).values()))
    S=sum(nx.single_source_shortest_path_length(g,r).values())
    t=nx.bfs_tree(g,r)
    I={v for v in t if t.out_degree(v)}
    assert S>=3*(len(I)-1)
    D=I if len(I)>1 else I|{next(iter(t.successors(r)))}
    assert all(any(w in D for w in g[v]) for v in g)
    assert len(D)<=1+(S+2)//3
    count+=1
assert count==994
print("Passed",count,"connected atlas graphs.")
