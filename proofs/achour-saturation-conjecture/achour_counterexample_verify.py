"""Exact verification of the port-gadget counterexamples to Achour's conjecture.
No external dependencies. Run: python achour_counterexample_verify.py
"""
from itertools import product
from functools import lru_cache


def gadget(D):
    assert D >= 3 and D % 2 == 1
    a,b,c,p=0,1,2,3
    r=(D-1)//2; q=(D+1)//2
    X0=list(range(4,4+2*r))
    X1=list(range(4+2*r,4+4*r))
    Y0=list(range(4+4*r,4+4*r+q))
    Y1=list(range(4+4*r+q,4+4*r+2*q))
    L={a:[p]+X0,b:X1[:r]+Y0,c:X1[r:]+Y1}
    edges={tuple(sorted((u,v))) for u in L for v in L[u]}
    for P,Q in [(X0,X1),(Y0,Y1)]:
        edges.update(tuple(sorted((u,v))) for u,v in product(P,Q))
    n=3*(D+1)
    assert sorted(v for ls in L.values() for v in ls)==list(range(3,n))
    return n,edges,L,p,(X0,X1,Y0,Y1)


def exact_gadget_by_center_choices(D,delete_port=False):
    n,E,L,p,parts=gadget(D)
    X0,X1,Y0,Y1=map(set,parts)
    owner={x:c for c,ls in L.items() for x in ls}
    best=n; tested=0
    for picks in product(*[[None]+[v for v in L[c] if not(delete_port and v==p)] for c in range(3)]):
        T={c for c,v in enumerate(picks) if v is not None}
        X={v for v in picks if v is not None}
        if not delete_port and p not in X and 0 not in T:continue
        cost=len(T); feasible=True
        for A,B in [(X0-X,X1-X),(Y0-X,Y1-X)]:
            # All maximal matchings of a biclique saturate its smaller part.
            # Mandatory vertices are those owned by unmatched centers.
            if sum(owner[v] not in T for v in A)>len(B) or sum(owner[v] not in T for v in B)>len(A):
                feasible=False;break
            cost+=min(len(A),len(B))
        if feasible:best=min(best,cost)
        tested+=1
    return best,tested


def assembled_graph(D,Q_edges,t):
    n,E,L,p,parts=gadget(D)
    all_E={(u+i*n,v+i*n) for i in range(t) for u,v in E}
    all_E.update(tuple(sorted((p+i*n,p+j*n))) for i,j in Q_edges)
    centers={i*n+c for i in range(t) for c in range(3)}
    return n*t,all_E,centers


def check_graph(n,E,S,D):
    A=[set() for _ in range(n)]
    for u,v in E:A[u].add(v);A[v].add(u)
    assert max(map(len,A))==D
    assert all(len(A[c])==D and not(A[c]&S) for c in S)
    assert all(len(A[v]&S)==1 for v in range(n) if v not in S)
    seen={0}; stack=[0]
    while stack:
        v=stack.pop()
        for w in A[v]-seen:seen.add(w);stack.append(w)
    assert len(seen)==n
    assert n==(D+1)*len(S)
    # Every dominating set has size >= ceil(n/(D+1)) = |S|.
    return len(S)


def witness(D,t,cross_matching):
    n,E,L,p,parts=gadget(D)
    X0,X1,Y0,Y1=parts
    covered_ports={i for e in cross_matching for i in e}
    M=[(i*n+p,j*n+p) for i,j in cross_matching]
    for i in range(t):
        M.extend((i*n+u,i*n+v) for u,v in list(zip(X0,X1))+list(zip(Y0,Y1)))
        if i not in covered_ports:M.append((i*n,p+i*n))
    return M


def check_matching(n,E,M):
    flat=[v for e in M for v in e]
    assert len(flat)==len(set(flat))
    assert all(tuple(sorted(e)) in E for e in M)
    covered=set(flat)
    assert all(u in covered or v in covered for u,v in E)


def exact_small_gadget_bruteforce(D):
    n,E,*_=gadget(D)
    A=[0]*n
    for u,v in E:A[u]|=1<<v;A[v]|=1<<u
    @lru_cache(None)
    def f(mask):
        rest=mask
        while rest:
            bit=rest&-rest;rest-=bit;u=bit.bit_length()-1
            ns=A[u]&mask
            if ns:
                v=(ns&-ns).bit_length()-1;break
        else:return 0
        ans=n
        for a in (u,v):
            ns=A[a]&mask
            while ns:
                b=ns&-ns;ns-=b
                ans=min(ans,1+f(mask&~((1<<a)|b)))
        return ans
    return f((1<<n)-1),f(((1<<n)-1)^(1<<3))


if __name__=='__main__':
    total=0
    for D in range(3,32,2):
        s,c1=exact_gadget_by_center_choices(D)
        sm,c2=exact_gadget_by_center_choices(D,True)
        total+=c1+c2
        assert s==(3*D+1)//2 and sm==(3*D-1)//2
    print(f'Exact gadget center-choice cases checked: {total}; all pass.')
    for D in (3,5):
        assert exact_small_gadget_bruteforce(D)==((3*D+1)//2,(3*D-1)//2)
    print('Independent exhaustive maximal-matching recursion agrees for D=3,5.')
    D=5;t=4;Q=[(0,1),(0,2),(0,3)]
    n,E,S=assembled_graph(D,Q,t)
    k=check_graph(n,E,S,D)
    # Cross links are a star: any matching can use at most one.
    sg,_=exact_gadget_by_center_choices(D)
    sd,_=exact_gadget_by_center_choices(D,True)
    lower=min(t*sg,(t-2)*sg+2*sd+1)
    M=witness(D,t,[(0,1)])
    check_matching(n,E,M)
    assert len(M)==lower==31 and (D*k+1)//2==30
    print(f'Counterexample: n={n}, m={len(E)}, Delta={D}, i={k}, exact s={lower}, conjectured bound={(D*k+1)//2}.')
    print('Explicit maximal matching:',sorted(tuple(sorted(e)) for e in M))