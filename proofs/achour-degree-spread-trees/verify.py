from itertools import combinations

def invariants(n,edges):
    a=[0]*n
    for u,v in edges:a[u]|=1<<v;a[v]|=1<<u
    full=(1<<n)-1
    def independent(b):
        return all(not (a[u]&b) for u in range(n) if b>>u&1)
    i=n
    for k in range(1,n+1):
        if any(independent(b:=sum(1<<u for u in S)) and all(b&(a[u]|(1<<u)) for u in range(n)) for S in combinations(range(n),k)):
            i=k;break
    for k in range(n//2+1):
        for M in combinations(edges,k):
            b=0
            for u,v in M:
                t=(1<<u)|(1<<v)
                if b&t:break
                b|=t
            else:
                if independent(full^b):return i,k,max(x.bit_count() for x in a)-min(x.bit_count() for x in a)
    raise AssertionError

def corona_path(m):
    return 2*m,[(j,j+1) for j in range(m-1)]+[(j,j+m) for j in range(m)]

if __name__=='__main__':
    for m in range(2,9):
        n,E=corona_path(m); r=invariants(n,E)
        assert r==(m,(m+1)//2,1 if m==2 else 2),r
        print(f'n={n}, i={r[0]}, s={r[1]}, degree spread={r[2]}')
    E=[(1,0),(1,2),(1,5),(0,6),(2,3),(2,4),(6,7),(6,10),(7,8),(7,9)]
    assert invariants(11,E)==(5,2,2)
    print('11-vertex witness verified')
    import sys
    if '--atlas' in sys.argv:
        import networkx as nx
        for n in range(2,12):
            total=bad=0
            for G in nx.nonisomorphic_trees(n):
                i,s,d=invariants(n,list(G.edges()));total+=1;bad+=i-s>d
            assert bad==(1 if n==11 else 0)
            print(n,total,bad)
