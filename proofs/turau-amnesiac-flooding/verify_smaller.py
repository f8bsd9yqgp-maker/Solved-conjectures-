from collections import deque, defaultdict
from itertools import combinations

def graph(k):
    n=7*k
    E=set()
    for i in range(k):
        j=7*i
        E.update((j+a,j+b) for a,b in [(0,1),(1,2),(2,3),(3,4),(1,5),(2,5),(2,6),(3,6)])
        if i:E.add((j-3,j))
    A=[set() for _ in range(n)]
    for u,v in E:A[u].add(v);A[v].add(u)
    return A,E,{7*i+2 for i in range(k)}

def flood(A,S):
    M={(u,v) for u in S for v in A[u]}; sizes=[]; seen=set(S)
    while M:
        sizes.append(len(M))
        R=defaultdict(set)
        for u,v in M:R[v].add(u)
        seen.update(R)
        M={(v,w) for v,N in R.items() for w in A[v]-N}
        assert len(sizes)<=2*len(A)+1
    assert len(seen)==len(A)
    return sizes

def eccentricities(A):
    result=[]
    for u in range(len(A)):
        d={u:0};q=deque([u])
        while q:
            v=q.popleft()
            for w in A[v]-d.keys():d[w]=d[v]+1;q.append(w)
        assert len(d)==len(A)
        result.append(max(d.values()))
    return result

if __name__=='__main__':
    for k in range(1,51):
        A,E,S=graph(k);e=eccentricities(A)
        assert len(E)==9*k-1 and len(A)==7*k
        assert min(e)==5*k//2 and max(e)==5*k-1
        assert flood(A,S)==[4*k,6*k,8*k-2]
        assert sum(flood(A,S))==2*len(E)
        if k>=4:assert 3*k<min(e)+k-1
    A,E,S=graph(4)
    counts=defaultdict(int)
    for T in combinations(range(len(A)),4):counts[len(flood(A,T))]+=1
    assert min(counts)==3
    print('Checked k=1..50; 28-vertex witness:',flood(A,S),'radius',min(eccentricities(A)))
    print('Exhaustive four-source choices:',sum(counts.values()),'minimum rounds:',min(counts),'distribution:',dict(sorted(counts.items())))
