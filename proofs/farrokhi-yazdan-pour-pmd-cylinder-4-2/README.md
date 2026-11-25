# Counterexample to Farrokhi–Yazdan Pour Conjecture 4.2

25 November 2026. AI-assisted candidate disproof. Source: Farrokhi Derakhshandeh Ghouchan and Yazdan Pour, Positive matching decompositions of the cartesian product of graphs, arXiv:2502.02826v1, Section 4, Conjecture 4.2 (https://arxiv.org/abs/2502.02826). Statement also transcribed at https://www.emergentmind.com/open-problems/pmd-path-cycle-grids-remaining-range.

For m,n>=3 the conjecture predicts pmd(P_m square C_n)=5 if n is even and n<4(m-1), or n is odd and n<2m. Set m=4,n=7, so n=7<8. The graph has 28 vertices, 49 edges and maximum degree 4. The four matchings and integer weights below give a positive matching decomposition, proving pmd<=4. At least four matchings are necessary because four edges meet at each interior vertex. Hence pmd=4, disproving the conjecture as stated.

Label vertices 7a+b, 0<=a<4 and 0<=b<7. Edges join adjacent path coordinates with equal cycle coordinate, or adjacent cyclic coordinates with equal path coordinate.

## Certificate and exact verifier

Python 3, standard library only. Each row of W assigns weights to vertices in numerical order. On the residual edge set, positive endpoint sums pick out precisely the matching in the corresponding row of M.

```python
M=[
 [(16,17),(18,19),(10,11),(2,9),(12,13),(14,20),(8,15),(0,7),(26,27),(24,25)],
 [(7,13),(5,6),(14,15),(21,27),(19,20),(11,12),(3,4),(22,23),(9,16),(10,17),(18,25),(1,8)],
 [(23,24),(15,16),(21,22),(7,14),(8,9),(3,10),(17,18),(1,2),(0,6),(13,20),(4,11),(5,12),(19,26)],
 [(25,26),(0,1),(12,19),(15,22),(20,27),(11,18),(17,24),(9,10),(2,3),(6,13),(16,23),(4,5),(14,21),(7,8)]
]
W=[
 [18,-21,20,-21,-21,-21,-21,-17,16,-19,12,-11,-7,8,10,-15,14,-13,-3,4,-9,-21,-21,-21,2,-1,-5,6],
 [-25,2,-25,20,-19,16,-15,-11,-1,-3,-21,18,-17,12,8,-7,4,22,-23,14,-13,-9,6,-5,-25,24,-25,10],
 [-23,22,-21,20,-5,4,24,16,-17,18,-19,6,-3,-25,-15,12,-11,8,-7,2,26,14,-13,10,-9,-27,-1,-27],
 [26,-25,12,-11,6,-5,10,2,-1,14,-13,18,24,-9,4,22,8,16,-17,-23,20,-3,-21,-7,-15,28,-27,-19]
]
E={tuple(sorted((7*a+b,7*a+(b+1)%7))) for a in range(4) for b in range(7)}
E|={(7*a+b,7*(a+1)+b) for a in range(3) for b in range(7)}
assert len(E)==49
assert max(sum(v in e for e in E) for v in range(28))==4
for m,w in zip(M,W):
    assert len(set(v for e in m for v in e))==2*len(m)
    m=set(m)
    assert m<=E
    assert {e for e in E if w[e[0]]+w[e[1]]>0}==m
    E-=m
assert not E
print("pmd(P4 square C7)=4, contrary to Conjecture 4.2")
```

Discovery: randomized matching search with maximum residual degree pruning and pendant-edge peeling; reverse peeling gives the integer weight vectors. All four exact sign checks passed in the working calculation. The explicit certificate, not the randomized search, proves the result.

Targeted searches did not identify a prior disproof of this particular conjecture; absolute priority and independent review remain unverified. The original PDF was not retrievable through the browser in this run, so the conjecture wording was checked against the attributed transcription and the arXiv bibliographic record.
