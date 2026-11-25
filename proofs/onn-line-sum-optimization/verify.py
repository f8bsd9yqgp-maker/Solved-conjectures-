from itertools import product, combinations_with_replacement

def construct(a,B):
    m=len(a)//3; R=3*m; L=B+2; C=(m-1)*L+B
    assert len(a)==R and sum(a)==m*B and all(B<4*x and 2*x<B for x in a)
    d=sorted([z for j in range(m) for z in (j*L+B,j*L,j*L)],reverse=True)
    c=[sum(x>=k for x in d) for k in range(1,C+1)]
    ts=[t for j in range(1,m) for t in (j*L-1,j*L)]
    def h(x):return sum(max(0,x-t) for t in ts)
    H=h(C); T=R*H-sum(map(h,d)); P=T+1
    f=[[H-h(x) if x in {j*L+v for j in range(m)} else P for x in range(C+1)] for v in a]
    g=[[0 if x==v else P for x in range(R+1)] for v in c]
    return m,R,L,C,d,c,ts,T,f,g

def graphical(r,c):
    r=sorted(r,reverse=True)
    return sum(r)==sum(c) and all(sum(r[:k])<=sum(min(k,z) for z in c) for k in range(1,len(r)+1))

def test(a,B):
    m,R,L,C,d,c,ts,T,f,g=construct(a,B)
    assert all(x>=0 for row in f+g for x in row)
    assert sum(d)==sum(c)
    yes=False; accept=0
    for labels in product(range(m),repeat=R):
        partition=all(sum(z==j for z in labels)==3 and sum(x for x,z in zip(a,labels) if z==j)==B for j in range(m))
        r=[j*L+x for j,x in zip(labels,a)]
        accepted=sum(f[i][x] for i,x in enumerate(r))<=T and graphical(r,c)
        assert accepted==partition,(a,B,labels,r,accepted,partition)
        yes|=partition;accept+=accepted
    return yes,accept,m**R

if __name__=='__main__':
    n=y=no=assignments=0
    for B in range(8,31):
        for a in combinations_with_replacement(range(B//4+1,(B+1)//2),6):
            if sum(a)!=2*B:continue
            v,k,q=test(a,B);n+=1;y+=v;no+=not v;assignments+=q
    for a,B in [([5,5,8,6,6,6,5,6,7],18),([6]*9,18),([4]*6+[8]*3,16),([5]*6+[8]*3,18),([5,5,5,5,7,7,7,7,6],18)]:
        if not all(B<4*x and 2*x<B for x in a) or sum(a)!=3*B:continue
        v,k,q=test(a,B);n+=1;y+=v;no+=not v;assignments+=q
    print(f'Checked {n} 3-PARTITION instances ({y} yes, {no} no), {assignments} assignments, using direct Gale-Ryser prefix inequalities; all equivalences passed.')
