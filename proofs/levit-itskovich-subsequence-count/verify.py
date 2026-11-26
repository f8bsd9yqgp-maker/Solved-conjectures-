from itertools import permutations
from random import Random
import networkx as nx


def check_graph(G):
    n=len(G)
    if not n:return None
    def maximum_sets(H):
        sets=list(nx.find_cliques(H)); size=max(map(len,sets))
        return size,[set(S) for S in sets if len(S)==size]
    a,ind=maximum_sets(nx.complement(G)); b,clq=maximum_sets(G)
    k=n-a-b+1; product=len(ind)*len(clq)
    assert k>=0 and product<=n*4**k
    disjoint=any(not S&T for S in ind for T in clq)
    if disjoint:
        assert k>=1 and product<=(1+2*(a+b))*4**(k-1)
    else:
        assert product<=n*2**k
    return disjoint


def count_monotone(seq, increasing=True):
    lengths=[1]*len(seq); counts=[1]*len(seq)
    for i,x in enumerate(seq):
        for j in range(i):
            if (seq[j]<x)==increasing:
                m=lengths[j]+1
                if m>lengths[i]: lengths[i]=m;counts[i]=counts[j]
                elif m==lengths[i]:counts[i]+=counts[j]
    m=max(lengths)
    return m,sum(c for l,c in zip(lengths,counts) if l==m)


def main():
    c=[0,0]
    for G in nx.graph_atlas_g():
        result=check_graph(G)
        if result is not None:c[int(result)]+=1
    print(f'Graph atlas: {sum(c)} nonempty graphs; {c[0]} all-intersecting, {c[1]} disjoint-pair cases: PASS')
    rng=Random(900);c=[0,0]
    for _ in range(1000):
        G=nx.gnp_random_graph(rng.randrange(2,25),rng.random(),seed=rng.randrange(2**32))
        c[int(check_graph(G))]+=1
    print(f'Seeded random graphs: {sum(c)} graphs; {c[0]} all-intersecting, {c[1]} disjoint-pair cases: PASS')
    total=0
    for n in range(1,9):
        for p in permutations(range(n)):
            l,i=count_monotone(p);d,j=count_monotone(p,False)
            assert i*j<=n*4**(n-l-d+1)
            total+=1
    print(f'All permutations through length 8: {total} cases: PASS')

if __name__=='__main__':main()
