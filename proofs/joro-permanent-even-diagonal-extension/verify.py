from itertools import product

def permanent2(a):
    return a[0][0]*a[1][1]+a[0][1]*a[1][0]

def verify():
    count=0
    for a,c in product(range(1,24,2),repeat=2):
        if a*c%3: continue
        M=[[2*a,1],[1,2*c]]
        det=4*a*c-1
        assert det%24==11
        B=[[2*c*pow(det,-1,24)%24,-pow(det,-1,24)%24],[-pow(det,-1,24)%24,2*a*pow(det,-1,24)%24]]
        assert all(sum(M[i][k]*B[k][j] for k in range(2))%24==int(i==j) for i in range(2) for j in range(2))
        p,q=permanent2(M),permanent2(B)
        assert p%24==q%24==13
        assert q%8==5 and (2*p+q-3)%24==12
        count+=1
    print(f'{count} residue representatives checked: all exact congruences passed.')
if __name__=='__main__': verify()
