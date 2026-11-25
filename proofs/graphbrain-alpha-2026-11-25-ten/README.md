# Ten Graph Brain independence-number candidate resolutions

25 November 2026. AI-assisted written arguments; independent review, priority, and formal verification pending. Original source: https://github.com/math1um/objects-invariants-properties/issues/421 (lower entries in the issue body; upper entries in the first comment). The IDs are one-based positions in the respective lists. These are ten distinct catalogue entries, not a claim of ten novel mathematical discoveries.

Write alpha for independence number, n for order, k=degeneracy+1 (Szekeres–Wilf), mu for matching number, C for the center, I for the independence-irreducible part, delta for minimum degree, sigma2 for minimum nonadjacent degree sum, and M for max(0, max_v (|E_v|-|E(G[E_v])|)), where E_v is the set of vertices at even distance from v, including v. Graphs are finite, simple, connected, with the original invariants defined.

## lower-019 — proof
Claim alpha >= ceil(|I|/k). Greedy degeneracy coloring uses at most k colors. Restrict it to I; one independent color class contains at least ceil(|I|/k) vertices. In fact the statement holds for any vertex subset.

## lower-021 — proof
Claim alpha >= ceil(|C|/k). Apply the preceding subset lemma to C.

## lower-038 — proof
Claim alpha >= ceil(2mu/k). Apply the subset lemma to the 2mu distinct endpoints of a maximum matching.

## lower-052 — disproof
Claim alpha >= min(|Aut(G)|,delta-max_common_neighbors). Take the Paley graph on Z/17Z with adjacency differences in Q={1,2,4,8,9,13,15,16}. Each vertex has degree 8; translations give at least 17 automorphisms. For each nonzero difference d, |Q intersect (d+Q)| is either 3 or 4 (direct enumeration), hence maximum common-neighbor count is 4. The set {0,3,6} is independent. There is no independent 4-set: by translation a putative set contains 0, and the remaining three must belong to the eight nonresidues R={3,5,6,7,10,11,12,14}; enumeration of the 56 triples of R shows none has all three pairwise differences in R. The exact verifier below reproduces these finite checks. Thus alpha=3<4.

## lower-058 — disproof
Claim alpha >= (|C|-2mu)diameter. For K_(2,b), b>=2, all vertices have eccentricity 2, mu=2 and alpha=b. The right side is 2(b-2), exceeding b for every integer b>=5. In particular b=10 yields 10<16.

## lower-060 — disproof
Claim alpha >= min(tan(m),mu-|C|), with radians and m=edge count. Join 43 disjoint K4 cliques by edges between consecutive designated vertices, one designated vertex per clique. There are 300 edges, alpha=43 by the clique partition and choice of one nondesignated vertex per clique, and mu=86 by the internal perfect matchings. The sole center is the designated vertex of the middle clique (eccentricity 22; every other vertex has greater eccentricity). Consequently mu-|C|=85. Let t=191*pi/2-300. Using 3.14159265358979<pi<3.14159265358980 gives 0<t<0.02211; tan(300)=cot(t)>=(1-t^2/2)/t>43. Both terms in the minimum exceed 43.

## lower-067 — disproof
Claim alpha >= (# cut vertices)/2+M-radius. Use the full binary tree of height 3: 15 vertices, radius 3, seven cut vertices, bipartition sizes 5 and 10. Thus M=10 because each even-distance set is exactly one part, with no internal edges. The size-10 part is independent; a matching saturating the size-5 part exists (match the root to a child, then each of the four depth-2 vertices to a distinct child), so alpha=10 by the disjoint matching-edge upper bound n-mu. RHS=7/2+10-3=10.5.

## lower-084 — disproof
Claim alpha >= tan(M*radius+1). P52 has alpha=26 (alternating vertices and a perfect matching), radius=26, M=26 (equal bipartition parts). Let t=431*pi/2-677. The same rational pi interval gives 0<t<0.01322. Thus tan(677)=cot(t)>=(1-t^2/2)/t>26.

## upper-043 — proof
Claim alpha <= max(M,n-delta-1). For a maximum independent set S, each of its vertices has degree at most n-|S|. Hence |S|<=n-delta. If strict, integrality proves the claim. If equality, each vertex of S is adjacent to every vertex outside S. For a connected graph with n>=2, each even-distance set rooted in S is then precisely S, so M>=|S|. The singleton also satisfies the bound directly with M=1.

## upper-074 — proof
Claim alpha <= n-ceil(sigma2/2). On the domain where sigma2 is defined (noncomplete graphs), choose two vertices in a maximum independent set. Both have degree at most n-alpha, so sigma2<=2(n-alpha), and the result follows by integrality. No convention for sigma2 on complete graphs is assumed.

## Reproducible exact checks

Python standard library only. The rational bounds on pi are proved by alternating arctangent series and Machin's identity; the cotangent lower bound follows from sin(t)<=t and cos(t)>=1-t^2/2 for 0<t<1.

```python
from itertools import combinations
from fractions import Fraction as F
Q={1,2,4,8,9,13,15,16}
R=set(range(1,17))-Q
assert max(len(Q & {(d+q)%17 for q in Q}) for d in range(1,17))==4
assert all((a-b)%17 in R for a,b in combinations([0,3,6],2))
assert not any(all((a-b)%17 in R for a,b in combinations(T,2))
               for T in combinations(R,3))
def atan_interval(q,N):
    s=sum(((-1)**i*q**(2*i+1)/F(2*i+1) for i in range(N)),F(0))
    r=(-1)**N*q**(2*N+1)/F(2*N+1)
    return min(s,s+r),max(s,s+r)
a,b=atan_interval(F(1,5),14)
c,d=atan_interval(F(1,239),5)
lo,hi=16*a-4*d,16*b-4*c
pl,ph=F('3.14159265358979'),F('3.14159265358980')
assert pl<lo<hi<ph
for x,j,B in [(300,191,43),(677,431,26)]:
    l,h=j*pl/2-x,j*ph/2-x
    assert 0<l<h<1 and (1-h*h/2)/h>B
```

The other witness quantities were checked using NetworkX. The first three proofs are corollaries of the established degeneracy coloring bound. Current individual external resolution status is not independently established, even though the catalogue issue is open. No first-discovery claim.
