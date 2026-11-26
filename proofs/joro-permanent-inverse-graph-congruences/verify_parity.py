import numpy as np
from itertools import combinations
from random import Random

r=Random(513259)
def inv(A):
    n=len(A); E=np.concatenate((A.copy(),np.eye(n,dtype=np.int64)),axis=1)
    for i in range(n):
        j=next((j for j in range(i,n) if E[j,i]%2),None)
        if j is None:return None
        E[[i,j]]=E[[j,i]]; E[i]=E[i]*int(E[i,i])%8
        for j in range(n):
            if j!=i:E[j]=(E[j]-E[j,i]*E[i])%8
    return E[:,n:]
def e2(x):
    return sum(int(x[i])*int(x[j]) for i,j in combinations(range(len(x)),2))

cnt=0
for n in range(2,13,2):
    for _ in range(200):
        A=np.zeros((n,n),dtype=np.int64)
        for i,j in combinations(range(n),2):A[i,j]=A[j,i]=r.randrange(2)
        B=inv(A)
        if B is None:continue
        rr=A.sum(1)%2; R=np.diag(rr); U=B@R@A; t=(B@rr-1)//2
        a=1+t-np.diag(U); K=A*(B%2); L=K@A
        z=(1+np.diag(U))%2; w=(U+L)%2
        Q=(n-int(rr.sum()))//2 + e2(t)+sum(int(a[i])*(int(U[:,i].sum())+int(rr[i])) for i in range(n))+sum(int(a[i]+w[i,j])*int(a[j]+w[j,i]) for i,j in combinations(range(n),2))
        Q2=(n-int(rr.sum()))//2+e2(z)+sum(int(w[i,j]*w[j,i]) for i,j in combinations(range(n),2))
        assert Q%2==Q2%2==0
        assert sum(int(K[i,j]) for i,j in combinations(range(n),2))%2==n//2%2
        cnt+=1
print('Parity identities verified on',cnt,'invertible graphs')
