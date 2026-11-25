from fractions import Fraction
from collections import Counter

def check(d):
    q=1<<((2*d).bit_length()-1)
    labels=list(range(q))+[0]*(2*d-q)
    n=4**d
    # Each integer stores d base-four coordinate residues. Gray code is 00,01,11,10.
    def selected(x):
        parity=syndrome=0
        for j in range(d):
            r=(x>>(2*j))&3
            g=r^(r>>1)
            parity^=r&1
            if g&1: syndrome^=labels[2*j]
            if g&2: syndrome^=labels[2*j+1]
        return parity==1 and syndrome!=0
    S=bytearray(map(selected,range(n)))
    counts=Counter()
    for x in range(n):
        k=0
        for j in range(d):
            shift=2*j
            r=(x>>shift)&3
            base=x&~(3<<shift)
            k+=S[base|(((r+1)&3)<<shift)]
            k+=S[base|(((r-1)&3)<<shift)]
        assert (k==0 if S[x] else k==0 or k%2==1),(d,x,k)
        counts[k]+=1
    assert Fraction(sum(S),n)==Fraction(q-1,2*q)
    print(f'd={d}, period vertices={n}, selected={sum(S)}, density={Fraction(sum(S),n)}, neighbor counts={dict(sorted(counts.items()))}')
    return n
if __name__=='__main__':
    print('Total vertices verified:',sum(check(d) for d in range(1,9)))
