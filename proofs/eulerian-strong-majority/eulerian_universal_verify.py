"""Constructive tests for the generalized Eulerian strong-majority proof.
Python 3 + NetworkX. Direct checks use original edge neighborhoods.
"""
from collections import defaultdict, Counter
from itertools import combinations
import random
import networkx as nx


def visits(E):
    m=len(E); P=defaultdict(list)
    assert len({frozenset(e) for e in E})==m
    for i,(u,v) in enumerate(E):
        assert u!=v and v==E[(i+1)%m][0]
        P[v].append(i)
    for ps in P.values():
        assert all(min(b-a,m-b+a)>=3 for a,b in combinations(ps,2))
    return P


def pairs(P):
    return [ab for ps in P.values() for ab in combinations(ps,2)]


def rotate(E,i): return E[i:]+E[:i]


def reverse(E,a,b):
    assert E[a][1]==E[b][1] and a<b
    return E[:a+1]+[(v,u) for u,v in reversed(E[a+1:b+1])]+E[b+1:]


def residues(P,m):
    R=[set() for _ in range(m)]
    for a,b in pairs(P):
        R[a].add((b-a)%3); R[b].add((m-b+a)%3)
    return R


def check(E,c):
    D=defaultdict(lambda:[0,0,0])
    for (u,v),x in zip(E,c): D[u][x]+=1; D[v][x]+=1
    for (u,v),x in zip(E,c):
        cap=(sum(D[u])+sum(D[v]))//2-1
        assert all(D[u][a]+D[v][a]-2*(x==a)<=cap for a in range(3)),(E,c,u,v)
    assert all(max(ds)<=sum(ds)//2 for ds in D.values() if sum(ds)>=4)


def colors(E,s):
    assert sum(s)%3==0 and len(E)==len(s)
    c=[0]
    for x in s[:-1]:c.append((c[-1]+x)%3)
    check(E,c)
    return c


def block(m,i,L):
    s=[1]*m
    for j in range(L):s[(i+j)%m]=-1
    return s


def find(E):
    m=len(E); P=visits(E); R=residues(P,m)
    h=[p[0] for p in P.values() if len(p)==1]
    if m%3==0:return E,[1]*m,'periodic'
    if m%3==1:
        if h:
            s=[1]*m;s[h[0]]=0
            return E,s,'one-zero'
        for i in range(m):
            if (1 in R[i] or 2 in R[i-1]) and (2 in R[(i+2)%m] or 0 in R[(i+1)%m]):
                return E,block(m,i,2),'two-step'
        return None
    for a,b in combinations(h,2):
        if min(abs(a-b),m-abs(a-b))>1:
            s=[1]*m;s[a]=s[b]=0
            return E,s,'two-zero'
    S=[i for i in range(m) if 2 in R[i] or 0 in R[i-1]]
    seen={}
    for j in S:
        if (j-1)%3 in seen:
            i=seen[(j-1)%3];return E,block(m,i,j-i),'two-defect'
        seen[j%3]=j
    for a in h:
        F=rotate(E,(a+1)%m); PP=visits(F)
        for ps in PP.values():
            for x,y in combinations(ps,2):
                if x%3==y%3==2:L=y
                elif x%3==y%3==1:L=x+1
                else:continue
                assert 2<=L<=m-3 and L%3==2
                s=[-1]*L+[1]*(m-1-L)+[0]
                return F,s,'one-zero-one-defect'
    return None


def nnon(E):
    assert len(E)%3==2
    return sum((b-a)%3!=1 for a,b in pairs(visits(E)))


def construct(E):
    E=list(E);m=len(E); moves=0
    ans=find(E)
    if ans is None and m%3==1:
        P=visits(E)
        d,a=min((d,a) for x,y in pairs(P) for d,a in ((y-x,x),(m-y+x,y)))
        E=reverse(rotate(E,a),0,d);moves+=1
        ans=find(E);assert ans is not None
    while ans is None:
        assert m%3==2
        N=nnon(E);better=None
        for a,b in pairs(visits(E)):
            F=reverse(E,a,b);ans=find(F)
            if ans is not None:break
            if better is None and nnon(F)>N:better=F
        moves+=1
        if ans is None:
            assert better is not None, ('no ascent or repair',E)
            E=better
            assert moves<=m*m
    F,s,kind=ans
    return F,colors(F,s),kind,moves


def random_mixed(n,rng):
    # Symmetric difference with random cycles preserves even degrees.
    # Start with a Hamilton cycle; reject disconnected final graphs.
    G=nx.cycle_graph(n)
    for _ in range(rng.randint(1,max(2,n//2))):
        cyc=rng.sample(range(n),rng.randint(3,n))
        for u,v in zip(cyc,cyc[1:]+cyc[:1]):
            if G.has_edge(u,v):G.remove_edge(u,v)
            else:G.add_edge(u,v)
    return G if nx.is_connected(G) else None


def high_mixed(n,rng):
    # Begin with 4-regular graphs, add edge-disjoint triangles or cycles.
    G=nx.random_regular_graph(4,n,seed=rng.randrange(2**32))
    for _ in range(n):
        cyc=rng.sample(range(n),rng.randint(3,min(n,6)))
        es=list(zip(cyc,cyc[1:]+cyc[:1]))
        if all(not G.has_edge(*e) for e in es):G.add_edges_from(es)
    return G if nx.is_connected(G) else None


def subdiv(G,h,rng,adjacent=False):
    G=G.copy();u,v=rng.choice(list(G.edges()));G.remove_edge(u,v)
    a=max(G)+1; G.add_edge(u,a)
    if h==1:G.add_edge(a,v)
    elif adjacent:G.add_edges_from([(a,a+1),(a+1,v)])
    else:raise ValueError
    return G


def main():
    rng=random.Random(20261127); count=Counter(); kinds=Counter(); moves=Counter()
    def test(G,category):
        if G is None:return
        assert nx.is_eulerian(G) and not G.is_multigraph()
        E=list(nx.eulerian_circuit(G));F,c,k,t=construct(E);check(F,c)
        count[category,len(E)%3]+=1;kinds[k]+=1;moves[category]+=bool(t)
    for G in nx.graph_atlas_g():
        if len(G)>1 and nx.is_connected(G) and nx.is_eulerian(G):test(G,'atlas')
    for n in range(5,41):
        for _ in range(25):
            G=high_mixed(n,rng);test(G,'minimum4')
            if G is not None:
                test(subdiv(G,1,rng),'one-degree2')
                test(subdiv(G,2,rng,True),'adjacent-degree2')
            test(random_mixed(n,rng),'random-even')
    print('Tests:',dict(sorted(count.items())))
    print('Coloring methods:',dict(kinds))
    print('Tour repairs:',dict(moves))
    print('Total:',sum(count.values()))

if __name__=='__main__':main()