from collections import Counter
from fractions import Fraction

def check(d):
    q=1<<(d.bit_length()-1)
    label=list(range(q))+[0]*(d-q)
    N=1<<d
    synd=[0]*N
    for x in range(1,N):
        b=x&-x
        synd[x]=synd[x^b]^label[b.bit_length()-1]
    S=bytearray(x.bit_count()%2==1 and synd[x]!=0 for x in range(N))
    assert sum(S)==(N//2)-(N//(2*q))
    assert Fraction(sum(S),N)>=Fraction(1,2)-Fraction(1,d)
    counts=Counter()
    for x in range(N):
        k=sum(S[x^(1<<i)] for i in range(d))
        if S[x]: assert k==0
        else: assert k==0 or k%2==1
        if x.bit_count()%2==0:
            assert k==(q-1 if synd[x]==0 else d-1)
            counts[k]+=1
    print(d,sum(S),dict(counts))
    return N
if __name__=='__main__':
    print('Verified vertices:',sum(check(d) for d in range(2,19,2)))
