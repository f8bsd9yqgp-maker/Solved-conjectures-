"""Finite sanity check for the proof of WOW II 162 (NetworkX graph atlas)."""
import networkx as nx

count = 0
for g in nx.graph_atlas_g():
    if len(g) < 2 or not nx.is_connected(g):
        continue
    if min(dict(g.degree()).values()) != 1:
        continue
    simplicial = {v for v in g if all(g.has_edge(a, b)
                 for a in g[v] for b in g[v] if a != b)}
    if len(g) == 2:
        t = g
    else:
        root = next(v for v in g if v not in simplicial)
        t = nx.bfs_tree(g, root).to_undirected()
    assert nx.is_tree(t)
    assert set(t) == set(g)
    assert all(t.degree(v) == 1 for v in simplicial)
    count += 1
assert count == 412
print(f"Passed {count} graphs.")
