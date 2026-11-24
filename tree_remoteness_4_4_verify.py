"""Exact verifier for arXiv:2611.27685v1, Conjecture 4.4 counterexample."""
from collections import Counter, deque
from itertools import product

D = [408,213,175,67,65,65,65,8]+[1]*15
S = sum(D)
C0 = sum(l*(l+1)//2 for l in D)
def B(l): return l*(S-l)

# Independently construct the subdivided graph and calculate distances.
g = [[],[],[]]
def path(u,l,v=None):
    for i in range(l):
        w = v if i==l-1 and v is not None else len(g)
        if w == len(g): g.append([])
        g[u].append(w); g[w].append(u); u=w
path(0,408,1); path(1,213,2)
for u,ls in enumerate(([65]*3,[175,67,8],[1]*15)):
    for l in ls: path(u,l)
def transmission(v):
    d=[-1]*len(g); d[v]=0; queue=deque([v])
    while queue:
        u=queue.popleft()
        for w in g[u]:
            if d[w]<0: d[w]=d[u]+1; queue.append(w)
    assert min(d)>=0
    return sum(d)
assert len(g)==1082 and sum(len(a)>=3 for a in g)==3
candidate=max(map(transmission,range(len(g))))
assert candidate==394650

# Exhaust all possible 2-branch trees by internal length and pendant multiset partition.
best={}
for a in sorted(set(D)):
    remaining=D.copy(); remaining.remove(a)
    counts=Counter(remaining)
    best[a]=float("inf")
    for ns in product(*(range(c+1) for c in counts.values())):
        if not 2<=sum(ns)<=len(remaining)-2: continue
        q=sum(l*n for l,n in zip(counts,ns))
        p=max(l for l,n in zip(counts,ns) if n)
        r=max(l for l,n in zip(counts,ns) if n<counts[l])
        val=max(B(p)+a*(S-a-q),B(r)+a*q)
        best[a]=min(best[a],val)
star=C0+B(max(D))
two=C0+min(best.values())
assert (S,C0,star,two,candidate)==(1081,130391,404975,394835,394650)
assert min(star,two)>candidate
print("Adjusted minima by internal length:",best)
print("Maximum transmissions: candidate",candidate,"star",star,"best two-branch",two)
print("Verified strict gap:",two-candidate,"/",S)
