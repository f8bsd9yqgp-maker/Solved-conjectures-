from itertools import combinations

def graph(m, clique):
    n=2*m+3
    adj=[set() for _ in range(n)]
    def edge(u,v):
        adj[u].add(v); adj[v].add(u)
    edge(0,1); edge(1,2)
    for i in range(m):
        x,y=3+i,3+m+i
        edge(0,x); edge(x,y); edge(y,2)
    if clique:
        for x,y in combinations(range(3,3+m),2):
            edge(x,y)
    return adj

def verify(m,clique):
    a=graph(m,clique); n=len(a); V=set(range(n))
    assert set.union(*(a[i] for i in (0,1,2)))==V
    assert all(a[u]|a[v]!=V for u in V for v in a[u])
    M=max(len(a[u]|a[v]) for u in V for v in a[u])
    assert M==m+3
    if clique:
        assert all(len(a[u])<n-1 and {u}|a[u]|set.union(*(a[v] for v in a[u]))==V for u in V)
        k=n
    else:
        A={u for u in V if len(a[u])==min(map(len,a))}
        k=len(set.union(*(a[u] for u in A)))
        assert k==2*m+2
    assert 2*k>3*M
    return n,3,k,M

for clique,lo in [(True,4),(False,6)]:
    for m in range(lo,101):
        verify(m,clique)
    print(255 if clique else 256,verify(lo,clique),'checked',101-lo,'parameters')
