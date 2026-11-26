from math import isqrt, log, pi
from array import array

def verify(limit=1_000_000):
    spf=array('I', range(limit+1))
    for p in range(2,isqrt(limit)+1):
        if spf[p]==p:
            for m in range(p*p,limit+1,p):
                if spf[m]==m: spf[m]=p
    primes=[p for p in range(2,limit+1) if spf[p]==p]
    endpoints={1000,10000,100000,len(primes)-1}
    total=individual=omega_total=0; violations=0; largest=None
    for n,(a,b) in enumerate(zip(primes,primes[1:]),1):
        seen=set()
        for m in range(a+1,b):
            z=m
            while z>1:
                p=spf[z]; individual+=p; seen.add(p)
                while z%p==0: z//=p
        s=sum(seen); w=len(seen); total+=s; omega_total+=w
        assert total<=individual
        # Exact sufficient violation certificate: ln(n)>=floor(log_3(n)).
        j=0; r=1
        while r*3<=n: j+=1; r*=3
        if w and j*s*s>4*n*n*w*w:
            violations+=1; largest=(n,a,b,s,w,j)
        if n in endpoints:
            expected=sum(p*(b//p-1) for p in primes if p<=b//2)
            assert individual==expected
            c=(pi*pi/6-1)/2
            print(f'N={n}, X={b}: gap_sum={total}, composite_sum={individual}, gap_ratio_to_asymptotic={total/(c*b*b/log(b)):.6f}, certified_violations={violations}')
    print('last exact upper-bound violation (n,p_n,p_next,S,W,j):',largest)
    print('All integer accounting identities passed.')

if __name__=='__main__': verify()
