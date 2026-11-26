from itertools import combinations
from random import Random
import networkx as nx


def flip(G, blocks):
    H = G.copy()
    for C in blocks:
        for u, v in combinations(C, 2):
            if H.has_edge(u, v): H.remove_edge(u, v)
            else: H.add_edge(u, v)
    return H


def covers(G, S, C):
    return all(any(G.has_edge(v, w) for w in S) for v in C)


def local_witness(G, H, C):
    C = set(C)
    if len(C) == 1:
        u = next(iter(C))
        return {next(iter(G[u]))}, {next(iter(H[u]))}
    for X, Y, reverse in [(G, H, False), (H, G, True)]:
        isolated = next((u for u in C if not (set(X[u]) & C)), None)
        if isolated is not None:
            S = {next(iter(X[u])) for u in C}
            T = {isolated, next(iter(C - {isolated}))}
            return (T, S) if reverse else (S, T)
    u = min(C)
    v = min(set(G[u]) & C)
    w = min(set(H[u]) & C)
    S, T = {u, v}, {u, w}
    A = {z for z in C if not (set(G[z]) & S)}
    B = {z for z in C if not (set(H[z]) & T)}
    assert not (A & B) and len(A)+len(B) <= len(C)-2
    S |= {next(iter(G[z])) for z in A}
    T |= {next(iter(H[z])) for z in B}
    return S, T


def total_domination(G):
    for k in range(1, len(G)+1):
        for S in combinations(G.nodes, k):
            if covers(G, S, G): return k
    raise AssertionError('isolated vertex')


def verify(G, blocks, exact=False):
    H = flip(G, blocks)
    if any(d == 0 for _, d in G.degree()) or any(d == 0 for _, d in H.degree()):
        return False
    S, T = set(), set()
    for C in blocks:
        A, B = local_witness(G, H, C)
        assert covers(G, A, C) and covers(H, B, C)
        assert len(A)+len(B) <= len(C)+2-(len(C)==1)
        S |= A; T |= B
    bound = len(G)+2*len(blocks)-sum(len(C)==1 for C in blocks)
    assert covers(G, S, G) and covers(H, T, H)
    assert len(S)+len(T) <= bound
    if exact:
        assert total_domination(G)+total_domination(H) <= bound
    return True


def degree_blocks(G):
    return [tuple(v for v, d in G.degree() if d == k) for k in sorted(set(dict(G.degree()).values()))]


def main():
    atlas = [G for G in nx.graph_atlas_g() if len(G)>0]
    count = sum(verify(G, degree_blocks(G), exact=True) for G in atlas)
    print(f'Graph atlas: {len(atlas)} nonempty graphs through order 7; {count} eligible degree-partition checks passed (exact minima).')
    rng = Random(1797)
    arbitrary = 0
    for _ in range(3000):
        n = rng.randrange(3, 31)
        G = nx.gnp_random_graph(n, rng.uniform(.12,.88), seed=rng.randrange(2**32))
        k = rng.randrange(1,n+1)
        bins = [[] for _ in range(k)]
        for v in G: bins[rng.randrange(k)].append(v)
        arbitrary += verify(G, [C for C in bins if C])
    print(f'Arbitrary partitions: {arbitrary} eligible checks out of 3000 seeded trials passed (constructive witnesses).')


if __name__ == '__main__': main()
