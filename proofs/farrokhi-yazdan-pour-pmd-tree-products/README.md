# Counterexample to Farrokhi–Yazdan Pour Conjecture 2.5

25 November 2026. AI-assisted exact finite counterexample. Source: Mohammad Farrokhi Derakhshandeh Ghouchan and Ali Akbar Yazdan Pour, Positive matching decompositions of the cartesian product of graphs, arXiv:2502.02826v1, p. 5, Conjecture 2.5 (https://arxiv.org/abs/2502.02826). Independent review and discovery priority remain unverified.

The conjecture predicts pmd(G)=Delta(G)+m-1_{m>0} for a Cartesian product of trees with m<=3 factors isomorphic to K2. Take G=K1,3 square K2 square K2, equivalently K1,3 square C4. It has 16 vertices, 28 edges, maximum degree 5, and m=2. The conjecture predicts 6. The certificate below proves pmd(G)=5.

Label vertices 4a+b for a,b in {0,1,2,3}, with a=0 the center of the star. The cycle coordinate b is modulo four. Each row of M is a matching in the graph remaining after deleting preceding rows. The corresponding row of W assigns integer weights to vertices 0 through 15 such that an edge in that remaining graph has positive endpoint-weight sum exactly when it belongs to that matching. Thus these five rows constitute a positive matching decomposition. Since each matching can cover at most one edge incident to any vertex, pmd(G)>=Delta(G)=5. Equality follows, contradicting the conjecture.

## Exact certificate and dependency-free verifier (Python 3)

```python
M=[
 [(0,4),(1,9),(2,6),(3,11),(12,13)],
 [(0,8),(1,5),(2,10),(3,7),(12,15),(13,14)],
 [(0,12),(1,2),(3,15),(4,5),(8,9)],
 [(0,1),(2,3),(4,7),(5,6),(8,11),(9,10),(14,15)],
 [(0,3),(1,13),(2,14),(6,7),(10,11)]
]
W=[
 [-1,-2,0,-1,2,-3,1,-3,-4,3,-4,2,0,1,-2,-1],
 [-3,-2,-1,0,-4,3,-4,1,4,-5,2,-5,2,1,0,-1],
 [-3,2,-1,0,0,1,-2,-1,0,1,-2,-1,4,-3,-2,1],
 [-1,2,1,0,1,2,-1,0,1,2,-1,0,0,-3,-2,3],
 [1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0]
]
E={tuple(sorted((4*a+b,4*a+(b+1)%4)))
   for a in range(4) for b in range(4)}
E|={(b,4*a+b) for a in range(1,4) for b in range(4)}
assert len(E)==28
assert max(sum(v in e for e in E) for v in range(16))==5
for m,w in zip(M,W):
    assert len(set(v for e in m for v in e))==2*len(m)
    m=set(m)
    assert m<=E
    assert {e for e in E if w[e[0]]+w[e[1]]>0}==m
    E-=m
assert not E
assert len(M)==5
print("Exact counterexample verified: pmd=5, conjectured 6")
```

Discovery method: search over positive matchings using the pendant-edge peeling characterization in Theorem 1.1 of the source, with residual maximum-degree pruning; independent linear feasibility checks supplied the integer weights above, which were then checked exactly. The final proof needs neither search nor floating-point arithmetic.

A targeted literature search found no prior exact resolution of Conjecture 2.5; other conjectures of the same paper already have reported counterexamples. No assertion of absolute priority is made.
