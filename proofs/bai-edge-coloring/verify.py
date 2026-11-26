#!/usr/bin/env python3
"""Exact finite checks for the analytical proof; requires networkx."""
from collections import defaultdict
from itertools import combinations
from math import prod
import networkx as nx

def falling(k,r):
    return prod(range(k-r+1,k+1)) if 0 <= r <= k else 0

def partitions(edges):
    m=len(edges)
    def rec(p,blocks):
        if len(p)==m:
            yield tuple(p),len(blocks); return
        uv=set(edges[len(p)])
        for i,b in enumerate(blocks):
            if not uv & b:
                yield from rec(p+[i],blocks[:i]+[b|uv]+blocks[i+1:])
        yield from rec(p+[len(blocks)],blocks+[uv])
    return list(rec([],[]))

def pattern(p,S):
    seen={}
    return tuple(seen.setdefault(p[i],len(seen)) for i in S)

def extend_counts(parts,S,k):
    ans=defaultdict(int)
    for p,q in parts:
        if q>k: continue
        a=pattern(p,S); r=len(set(a))
        ans[a]+=falling(k-r,q-r)
    return ans

def kempe_checks(G,k):
    import random
    rng=random.Random(20261126)
    E=list(G.edges()); m=len(E); adj=[set() for _ in E]
    for i,j in combinations(range(m),2):
        if set(E[i])&set(E[j]): adj[i].add(j);adj[j].add(i)
    checked=0
    for _ in range(8):
        order=list(range(m));rng.shuffle(order); col={}
        for i in order:
            avail=list(set(range(k))-{col[j] for j in adj[i] if j in col})
            if not avail: break
            col[i]=rng.choice(avail)
        if len(col)!=m: continue
        for e in rng.sample(range(m),min(m,12)):
            a=col[e];others=list(set(range(m))-{e});rng.shuffle(others)
            t=rng.randrange(min(m-1,k//8)+1);F=set(others[:t]);good=1
            for b in range(k):
                if b==a: continue
                C={e}; stack=[e]
                while stack:
                    i=stack.pop()
                    for j in adj[i]-C:
                        if col[j] in (a,b): C.add(j);stack.append(j)
                if C&F: continue
                good+=1
                new={i:(b if col[i]==a else a) if i in C else col[i] for i in col}
                assert all(new[i]!=new[j] for i in range(m) for j in adj[i])
                assert all(new[i]==col[i] for i in F) and new[e]==b
            assert 2*good>=2*k-m-6*t
            checked+=1
    return checked

def ring(k,t):
    G=nx.Graph()
    for i in range(t):
        G.add_edges_from(((i,0,a),(i,1,b)) for a in range(k) for b in range(k) if (a,b)!=(0,0))
        G.add_edge((i,0,0),((i+1)%t,1,0))
    color={frozenset((u,v)): ((v[2]-u[2])%k if u[1]==0 else (u[2]-v[2])%k) if u[0]==v[0] else 0 for u,v in G.edges()}
    assert len(G)==2*k*t and G.number_of_edges()==k*k*t
    assert nx.is_connected(G) and all(G.degree(u)==k for u in G)
    assert all(len({color[frozenset((u,v))] for v in G[u]})==k for u in G)
    for i in range(t):
        assert sum(u[0]==i and v[0]!=i or v[0]==i and u[0]!=i for u,v in G.edges())==2
    return G

def main():
    graphs=counts=prefix=0
    for G in nx.graph_atlas_g():
        m=G.number_of_edges()
        if not 1<=m<=7: continue
        parts=partitions(list(G.edges()));graphs+=1
        for k in range((6*m+6)//7,m+2):
            total=sum(falling(k,q) for p,q in parts)
            if not total: continue
            assert total*10**m>=k**m
            for s in range(1,m+1):
                for S in combinations(range(m),s):
                    prev=extend_counts(parts,S[:-1],k)
                    for pat,ext in extend_counts(parts,S,k).items():
                        assert total*10**(10*s)>=k**s*ext
                        counts+=1
                        assert 2*prev[pat[:-1]] >= (2*k-m-6*(s-1))*ext
                        prefix+=1
    switches=0
    for m in (20,40,80,160):
        for G in (nx.star_graph(m),nx.path_graph(m+1),nx.gnm_random_graph(m+1,m,seed=m)):
            k=max(max(dict(G.degree()).values()),(6*m+6)//7)
            switches+=kempe_checks(G,k)
    rings=0
    for k in (2,3,5,10,100):
        for t in (2,3,7):
            ring(k,t);rings+=1
    print(f'Atlas graphs: {graphs}; exact extension-count checks: {counts}; exact prefix checks: {prefix}')
    print(f'Randomized proper-coloring switch checks: {switches}; explicit regular ring constructions: {rings}')
    print('All assertions passed. Finite checks supplement, not replace, the proof.')

if __name__=='__main__':
    main()
