# Bounded-backdegree tournament recognition is fixed-parameter tractable

25 November 2026. AI-assisted alternative proof and generalization; independent review and priority for the generalization are pending.

Source question: Aboulker, Aubian and Lopes, Finding forest-orderings of tournaments is NP-complete, Problem 4.4, https://arxiv.org/abs/2402.10782 (published DOI https://doi.org/10.46298/dmtcs.14281). Important priority correction: the matching case was already answered by Bessy et al., Triangle packing in (sparse) tournaments: approximation and kernelization, Appendix C, Lemma C.47, https://arxiv.org/abs/1707.04220 (2017). Thus it must not be counted as a new conjecture resolution. The result below gives a different argument for arbitrary backdegree bound d. It does not settle the connected-path case.

## Theorem

Given an n-vertex tournament T and nonnegative integer d, whether a vertex ordering has a backward-edge graph of maximum degree at most d is decidable in O(n^2 (d+1) 2^(4d+1)) time with elementary adjacency-matrix operations. A witness order can be reconstructed via predecessors. This includes the matching case d=1.

Proof. Let s(v)=n-outdegree(v), with positions 1 through n. If v is placed at i, let a be the number of outgoing arcs to earlier vertices and b the number of incoming arcs from later vertices. The backward degree is a+b, and outdegree(v)=n-i+a-b. Consequently |i-s(v)|=|a-b|<=d.

Sort the s-values as s_1<=...<=s_n. A necessary condition for assigning all vertices to distinct allowed positions is |s_j-j|<=d for every j. Indeed, if s_j>j+d then the last n-j+1 vertices all require positions greater than j, of which there are only n-j. The opposite inequality follows by the symmetric counting argument. Reject if this test fails. In particular each sorted rank j satisfies |s_j-j|<=d.

For a prefix P of length t, all vertices with s(v)+d<=t must be present and all vertices with s(v)-d>t must be absent. Any ambiguous vertex satisfies t-d<s(v)<=t+d; its sorted rank j then satisfies t-2d<j<=t+2d. There are at most 4d such vertices, so at most 2^(4d) possible prefixes per layer.

Start with the empty prefix. For each reachable prefix P of size t, append any v outside P with |s(v)-(t+1)|<=d, discarding transitions that miss a vertex's deadline. The final backward degree of v depends only on P and v, not on the relative orders within P or its complement:
  B(v,P)=|{u in P: v->u}|+|{w outside P union {v}: w->v}|.
Accept the transition exactly when B(v,P)<=d. Every vertex's degree is tested once, when placed. Therefore the full prefix is reachable iff a valid ordering exists. Merging histories with the same prefix is sound because all future tests depend only on that prefix. There are at most 4d+1 vertices eligible to be placed at any next position by the sorted-rank bound, and each transition can be tested in O(n) time. This proves the stated complexity. With fixed d the cost is quadratic in n. No assertion is made that a maximum-degree-two backedge graph is connected or acyclic.

## Exhaustive verifier

Python 3, no dependencies. In this run all 1,099 labeled tournaments of orders 1 through 5 agreed with brute-force enumeration for d=0,1,2 (3,297 comparisons). The reference implementation scans all vertices for candidate selection; eligibility can be precomputed to attain the stated bound.

```python
import itertools as I

def dp(A,k):
    n=len(A)
    s=[n-sum(row) for row in A]
    if any(abs(x-i)>k for i,x in enumerate(sorted(s),1)):
        return False
    states={frozenset()}
    for i in range(1,n+1):
        nxt=set()
        for P in states:
            for v in range(n):
                if v in P or abs(s[v]-i)>k: continue
                R=P|{v}
                if any(s[u]+k<=i and u not in R for u in range(n)):
                    continue
                b=sum(A[v][u] for u in P)+sum(A[u][v] for u in range(n) if u not in R)
                if b<=k: nxt.add(R)
        states=nxt
        if not states: return False
    return bool(states)

def brute(A,k):
    n=len(A)
    for p in I.permutations(range(n)):
        deg=[0]*n
        for j in range(n):
            for i in range(j):
                if A[p[j]][p[i]]:
                    deg[p[j]]+=1
                    deg[p[i]]+=1
        if max(deg,default=0)<=k: return True
    return False

count=0
for n in range(1,6):
    pairs=list(I.combinations(range(n),2))
    for bits in I.product(range(2),repeat=len(pairs)):
        A=[[0]*n for _ in range(n)]
        for (u,v),b in zip(pairs,bits):
            A[u][v]=b
            A[v][u]=1-b
        for k in (0,1,2):
            assert dp(A,k)==brute(A,k)
        count+=1
assert count==1099
print(count, "tournaments verified for three degree bounds")
```
