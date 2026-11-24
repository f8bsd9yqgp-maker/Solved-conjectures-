"""Verify the BFS-tree witness for WOW II 169 on the NetworkX atlas."""
import networkx as nx
count = 0
for g in nx.graph_atlas_g():
    if len(g) < 2 or not nx.is_connected(g):
        continue
    evens, leaves = [], []
    for v in g:
        ds = nx.single_source_shortest_path_length(g, v)
        evens.append(sum(d % 2 == 0 for d in ds.values()))
        t = nx.bfs_tree(g, v).to_undirected()
        leaves.append(sum(t.degree(u) == 1 for u in t))
    assert max(leaves) >= 1 + max(evens) - min(evens)
    count += 1
assert count == 995
print(f"Passed {count} graphs.")
