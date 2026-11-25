from functools import lru_cache
from math import comb
from itertools import combinations

def choose(n,k): return comb(n,k) if 0<=k<=n else 0

@lru_cache(None)
def block(l,d,q):
    if d==0: return int(q==0 and l>=1)
    if q<0 or q>d or l<=d: return 0
    return sum((q+1)*block(l-b,d-1,q)+(l-b-q)*block(l-b,d-1,q-1) for b in range(1,l-d+1))

@lru_cache(None)
def suffix(left, asc, prev, used):
    if left==0: return 1
    ans=0
    for M in range(max(2,prev+1),asc+2):
        free=M-2-used
        for l in range(1,left+1):
            for d in range(min(free,l-1)+1):
                for q in range(d+1):
                    ans+=choose(free,d)*block(l,d,q)*suffix(left-l,asc+1+q,M,used+d+1)
    return ans

def count(n):
    if n==0:return 1
    return 2**(n-1)+sum(choose(p,2*r)*suffix(n-p,r,1,0) for p in range(2,n) for r in range(1,p//2+1))

def brute(N):
    def bad(a):
        x=a[-1]
        return any(a[i]<a[j]<a[k] and x in (a[i],a[j]) for i,j,k in combinations(range(len(a)-1),3))
    counts=[1,1]; words=[((0,),0)]
    for n in range(2,N+1):
        words=[(a+(v,),s+(a[-1]<v)) for a,s in words for v in range(s+2) if not bad(a+(v,))]
        counts.append(len(words))
    return counts

if __name__=='__main__':
    b=brute(10)
    assert [count(i) for i in range(11)]==b
    print('Brute-force verification passed:',b)
    print([(n,count(n)) for n in range(1,21)])
