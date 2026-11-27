"""Targeted failed-tour stress test for the Eulerian three-color construction.
Requires NetworkX and eulerian_universal_verify.py in the same directory.
"""
import random
from itertools import combinations
from collections import Counter
import networkx as nx
from eulerian_universal_verify import construct, check, visits, residues


def generate(m,h,triple,rng):
    if h==2:
        s=rng.randrange(m-1); singles=[s,s+1]
    else:singles=rng.sample(range(m),h)
    avail=set(range(m))-set(singles); groups=[[s] for s in singles]
    if triple:
        ts=[(a,b,c) for a in avail for b in avail for c in avail
            if a%3==0 and b%3==1 and c%3==2 and a+3<=b and b+3<=c and m-c+a>=3]
        if not ts:return None
        t=rng.choice(ts);groups.append(t);avail.difference_update(t)
    H=nx.Graph();H.add_nodes_from(avail)
    for a,b in combinations(sorted(avail),2):
        if min(b-a,m-b+a)>=3 and (a%3,b%3) in [(0,1),(1,2),(2,0),(0,2)]:
            H.add_edge(a,b,weight=rng.random())
    M=nx.max_weight_matching(H,maxcardinality=True)
    if len(M)*2!=len(avail):return None
    groups.extend(M);W=[None]*m
    for j,ps in enumerate(groups):
        for p in ps:W[p]=j
    E=list(zip(W[-1:]+W[:-1],W))
    if any(a==b for a,b in E) or len({frozenset(e) for e in E})!=m:return None
    R=residues(visits(E),m)
    S=[i for i in range(m) if 2 in R[i] or 0 in R[i-1]]
    assert all(i%3==0 for i in S)
    return E


def main():
    rng=random.Random(291127);counts=Counter();kinds=Counter(); repairs=Counter()
    for h in (0,1,2):
        for t in (0,1):
            for k in range(4,13):
                m=3*k+2
                if (m-h-3*t)%2:continue
                good=0
                for _ in range(500):
                    E=generate(m,h,t,rng)
                    if E is None:continue
                    F,c,kind,moves=construct(E);check(F,c)
                    counts[h,t]+=1;kinds[kind]+=1;repairs[h,t]+=bool(moves)
                    good+=1
                    if good==10:break
    print('Targeted graphs:',dict(counts));print('Methods:',dict(kinds));print('Tour repairs:',dict(repairs));print('Total:',sum(counts.values()))
if __name__=='__main__':main()