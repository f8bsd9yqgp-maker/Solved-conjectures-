from itertools import combinations, product

def graphs(n):
    es=list(combinations(range(n),2))
    for m in range(1<<len(es)):
        yield n, [e for j,e in enumerate(es) if m>>j&1]

def adj(n,E):
    A=[0]*n
    for u,v in E:A[u]|=1<<v; A[v]|=1<<u
    return A

def invariants(n,E):
    A=adj(n,E); best=odd=0
    def visit(S,R):
        nonlocal best,odd
        k=S.bit_count();best=max(best,k)
        if k>odd and all((z:=(a&S).bit_count())==0 or z%2 for a in A):odd=k
        while R:
            b=R&-R;R^=b;v=b.bit_length()-1
            visit(S|b,R&~A[v])
    visit(0,(1<<n)-1)
    return best,odd

def good(n,E):
    F=[]
    for v in range(n): F.extend([(4*v,4*v+2),(4*v+1,4*v+2),(4*v+2,4*v+3)])
    for u,v in E:F.extend((4*u+i,4*v+j) for i,j in product(range(2),repeat=2))
    return 4*n,F

def bad(n,E):
    return 2*n,[(2*u+i,2*v+j) for u,v in E for i,j in product(range(2),repeat=2)]

def reduction(A,B):
    na,EA=A;nb,EB=B
    L=2*((nb+1)//2)
    a,Fa=bad(na,EA);a+=L
    b,Fb=good(nb,EB);b+=L+1-nb
    return a+b,Fa+[(u+a,v+a) for u,v in Fb]+[(u,v) for u in range(a) for v in range(a,a+b)]

if __name__=='__main__':
    G=[g for n in range(1,5) for g in graphs(n)]
    vals=[invariants(*g)[0] for g in G]
    for g,a in zip(G,vals):assert invariants(*good(*g))==(g[0]+2*a,)*2
    count=yes=0
    for i,A in enumerate(G):
        for j,B in enumerate(G):
            if A[0]==B[0]==4:continue
            x,y=invariants(*reduction(A,B))
            assert (x==y)==(vals[i]<=vals[j]),(A,B,x,y)
            count+=1;yes+=x==y
    print(f'checked {len(G)} gadget instances and {count} ordered comparisons ({yes} yes, {count-yes} no)')

def packing(n,E):
    A=adj(n,E); B=A.copy()
    for v in range(n):
        for u in range(n):
            if A[v]>>u&1:B[v]|=A[u]
        B[v]&=~(1<<v)
    F=[(u,v) for u in range(n) for v in range(u+1,n) if B[u]>>v&1]
    return invariants(n,F)[0]

def line_corona(n,E):
    F=E+[(v,v+n) for v in range(n)]
    return len(F),[(i,j) for i,j in combinations(range(len(F)),2) if set(F[i])&set(F[j])]

def midpoint_join(A,B):
    a,EA=A;b,EB=B
    mid=[(u,a+v) for u in range(a) for v in range(b)]
    m=a+b
    return m+len(mid),EA+[(u+a,v+a) for u,v in EB]+[(v,m+i) for i,p in enumerate(mid) for v in p]+list(combinations(range(m,m+len(mid)),2))

def reduction2(A,B):
    na,EA=A;nb,EB=B;L=2*((nb+1)//2)
    a,Fa=bad(na,EA);a+=L+1
    a,Fa=line_corona(a,Fa)
    b,Fb=good(nb,EB);b+=L+1-nb
    Fb=Fb+[(v,b) for v in range(b)];b+=1
    return midpoint_join((a,Fa),(b,Fb))

if __name__=='__main__':
    count2=yes2=0
    for A,B in product(G[:3],repeat=2):
        a,b=invariants(*A)[0],invariants(*B)[0]
        n,E=reduction2(A,B)
        p=packing(n,E);o=invariants(n,E)[1]
        assert p==2*a+2*((B[0]+1)//2)+1
        assert o==max(p,2*b+2*((B[0]+1)//2)+1)
        assert (p==o)==(a>=b)
        count2+=1;yes2+=p==o
    print(f'second equality checked {count2} ordered comparisons ({yes2} yes, {count2-yes2} no)')
