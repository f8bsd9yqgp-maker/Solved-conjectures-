from functools import lru_cache
from itertools import combinations

def bits(s):
    while s:
        b=s&-s;s^=b;yield b

def graph(n,m):
    h=n+m; N=2*h
    A=[sum(1<<(l*h+j) for j in (range(n,h) if i<n else range(n))) | 1<<((1-l)*h+i) for l in range(2) for i in range(h)]
    return h,N,A

def relaxed_lower(n,m):
    # Exact shortest-path DP in a relaxation of play against the proof's oracle.
    # All paid moves, all ordinary forces, and any force restricted to a
    # white component lacking an untouched rung are allowed, even if an
    # actual oracle offer would not be legal. No other oracle move can force.
    h,N,A=graph(n,m); F=(1<<N)-1; half=(1<<h)-1
    def force(W,U):
        out=0
        for b in bits(F^W):
            nb=A[b.bit_length()-1]&U
            if nb and not nb&(nb-1):out|=nb
        return out
    @lru_cache(None)
    def f(W):
        if not W:return 0
        untouched=W&(W>>h)&half; untouched|=untouched<<h
        rest=W; comps=[]
        while rest:
            c=rest&-rest;old=0
            while c!=old:
                old=c
                for b in bits(c):c|=A[b.bit_length()-1]&W
            comps.append(c);rest^=c
        ff=force(W,W)
        for c in comps:
            if not c&untouched:ff|=force(W,c)
        # Check the response when every offered component has an untouched rung.
        for c,d in combinations([c for c in comps if c&untouched],2):
            assert not force(W,c|d)
        best=min(1+f(W^b) for b in bits(W))
        for b in bits(ff):best=min(best,f(W^b))
        return best
    v=f(F);assert v==h,(n,m,v)
    return v,f.cache_info().currsize

def gram_check(n,m):
    if n>m:n,m=m,n
    h,N,A=graph(n,m)
    U=([[3,4],[4,-3]] if m==2 else [[m*(i==j)-2 for j in range(m)] for i in range(m)])[:n]
    E=[[int(i==j) for j in range(m)] for i in range(m)]
    V=[u+[-v for v in u] for u in U]+[e+[0]*m for e in E]+[[0]*m+u for u in U]+[e+e for e in E]
    for i,j in combinations(range(N),2):
        assert bool(sum(a*b for a,b in zip(V[i],V[j])))==bool(A[i]>>j&1)
    # The B-layer vectors span the entire 2m-dimensional ambient space.
    assert V[n:h]==[e+[0]*m for e in E]
    assert V[h+n:]==[e+e for e in E]
    return N-2*m

if __name__=='__main__':
    total=0
    for n,m in [(2,2),(2,3),(2,4),(3,3),(2,5),(3,4),(2,6),(3,5),(4,4)]:
        z,states=relaxed_lower(n,m); total+=states
        assert gram_check(n,m)==2*min(n,m)
        print(n,m,'Z0',2*min(n,m),'Z1',z,'states',states,flush=True)
    print('Total white configurations checked:',total)
