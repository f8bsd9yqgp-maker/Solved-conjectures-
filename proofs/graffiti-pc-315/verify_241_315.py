"""Exhaustive sanity checks for WOW II 241 and 315; requires NetworkX."""
import itertools
import networkx as nx

def total_sets(g):
    nodes = tuple(g)
    masks = [sum(1 << i for i,v in enumerate(nodes) if g.has_edge(u,v)) for u in nodes]
    full = (1 << len(nodes)) - 1
    def dominates(s):
        covered = 0
        for i,m in enumerate(masks):
            if s >> i & 1:
                covered |= m
        return covered == full
    return dominates, full

trees = 0
for n in range(2,13):
    for g in nx.nonisomorphic_trees(n):
        S = {v for v in g if g.degree(v) == 2}
        N = S | {u for v in S for u in g[v]}
        c = nx.number_connected_components(g.subgraph(N))
        dom,full = total_sets(g)
        gamma = min(s.bit_count() for s in range(full+1) if dom(s))
        assert gamma >= max(2,c+1)
        trees += 1
assert trees == 986
print("241:",trees,"trees")

count = eligible = 0
for g in nx.graph_atlas_g():
    if len(g) < 2 or not nx.is_connected(g):
        continue
    count += 1
    P = {v for v in g if g.degree(v) == 1}
    alpha = max(len(s) for k in range(len(g)+1) for s in itertools.combinations(g,k)
                if not g.subgraph(s).number_of_edges())
    if alpha != len(P):
        continue
    eligible += 1
    dom,full = total_sets(g)
    sizes = {s.bit_count() for s in range(full+1) if dom(s)
             and all(not dom(s^(1<<i)) for i in range(len(g)) if s>>i&1)}
    assert len(sizes) == 1
assert (count,eligible) == (995,16)
print("315:",count,"graphs screened,",eligible,"eligible passed")
