"""Test the constructive domatic bound for split graphs; Python standard library."""
from itertools import product
from random import Random


def check(columns, m):
    n = len(columns)
    if n == 0:
        return 1
    C = sorted(range(n), key=lambda u: -len(columns[u]))
    rows = [{u for u in C if x in columns[u]} for x in range(m)]
    delta = min([n - 1 + len(a) for a in columns] + [len(row) for row in rows])
    # This r ensures the absence of an induced S_{r,r} with clique centers.
    # In a split graph the middle edge of an induced P4 lies in the clique.
    r = 1 + max((min(len(columns[u]-columns[v]), len(columns[v]-columns[u]))
                 for u in C for v in C), default=0)
    k = max(1, (delta + 1)//r)
    if k == 1:
        return k
    if m == 0:
        assert k == n
        return k
    if r == 1:
        T = C[:delta]
        assert all(set(T) <= row for row in rows)
        colors = {u:j for j,u in enumerate(T)}
        colors.update({u:delta for u in C[delta:]})
        independent_colors = [delta]*m
    else:
        T = C[:k]
        U = C[k:]
        requests = [(x,j) for x,row in enumerate(rows) for j,u in enumerate(T) if u not in row]
        assert all(len(rows[x].intersection(U)) >= delta-k+1 for x,j in requests)
        assert all(sum(v in rows[x] for x,j in requests) <= k*(r-1) for v in U)
        owner = {}
        def augment(req, seen):
            x,j = req
            for v in U:
                if v in seen or v not in rows[x]:
                    continue
                seen.add(v)
                if v not in owner or augment(owner[v], seen):
                    owner[v] = req
                    return True
            return False
        for req in requests:
            assert augment(req,set()), (columns, r, k, req)
        colors = {u:j for j,u in enumerate(T)}
        colors.update({v:j for v,(x,j) in owner.items()})
        colors.update({v:colors.get(v,0) for v in C})
        independent_colors = [0]*m
    wanted = set(range(k))
    for u in C:
        assert {colors[v] for v in C} | {independent_colors[x] for x in columns[u]} == wanted
    for x,row in enumerate(rows):
        assert {colors[u] for u in row} | {independent_colors[x]} == wanted
    return k

if __name__ == '__main__':
    total = nontrivial = 0
    for n in range(1,6):
        for m in range(0,5):
            if n*m > 16:
                continue
            for bits in product((0,1),repeat=n*m):
                cols=[{x for x in range(m) if bits[u*m+x]} for u in range(n)]
                k=check(cols,m); total+=1; nontrivial+=k>=2
    rng=Random(20261127)
    for _ in range(2000):
        n=rng.randint(5,60); m=rng.randint(1,40)
        cols=[]
        for u in range(n):
            a=set(range(rng.randint(m//2,m)))
            for x in rng.sample(sorted(a), min(len(a),rng.randrange(3))):
                a.remove(x)
            cols.append(a)
        k=check(cols,m); total+=1; nontrivial+=k>=2
    print(f'PASS: {total} split-graph incidence matrices; {nontrivial} with k >= 2.')
