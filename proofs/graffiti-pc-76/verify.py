from itertools import combinations
from fractions import Fraction

n=20
edges={e for i in range(5) for e in combinations(range(4*i,4*i+4),2)}
edges.update((i,4*(i+1)) for i in range(4))
adj=[0]*n
for u,v in edges:
    adj[u]|=1<<v;adj[v]|=1<<u

def connected(mask):
    reached=mask&-mask
    while True:
        old=reached
        for v in range(n):
            if (reached>>v)&1:reached|=adj[v]&mask
        if old==reached:return reached==mask

def tree(S):
    mask=sum(1<<v for v in S)
    return sum((adj[v]&mask).bit_count() for v in S)==2*(len(S)-1) and connected(mask)

assert connected((1<<n)-1)
tri=[0]*n
for u,v,w in combinations(range(n),3):
    if {(u,v),(u,w),(v,w)}<=edges:
        for a in (u,v,w):tri[a]+=1
assert tri==[3]*20
assert tree((0,1,4,5,8,9))
count=0
for S in combinations(range(n),7):
    assert not tree(S), S
    count+=1
avg=Fraction(2*len(edges),n); floor=avg.numerator//avg.denominator
assert 6*floor<tri.count(max(tri))
print(f'n={n}, m={len(edges)}, average degree={avg}, triangle counts={set(tri)}, maximum induced tree=6, checked {count} seven-vertex subsets; conjecture false')
