# An infinite counterexample family to the Cheeger–Pareto conjecture

Research note, 26 November 2026. Complete analytical disproof of the revised statement; discovery priority and independent review remain provisional.

## Source and scope

The conjecture was posed by jinni on MathOverflow (Conjecture B, edited December 20, 2025) and restated by the same author on Mathematics Stack Exchange on January 5, 2026:

- https://mathoverflow.net/questions/506070/conjecture-involving-the-cheeger-constant-of-a-graph
- https://math.stackexchange.com/questions/5118288/conjecture-involving-the-cheeger-constant-of-a-graph

DSM's earlier spiky-vector examples disproved the version without the floor, not the revised statement. The present construction uses the same broad idea of concentrating weight at one vertex, but a different infinite graph family. On November 26, 2026 both original discussions were rechecked, including DSM's two examples and the subsequent floor-function comment. Neither example contradicts the revised inequality, and no revised-statement answer was displayed.

Before selecting the candidate, both repository README indexes were retrieved. Default-branch searches for Cheeger constant, Pareto-efficient, and 506070 were conducted in both repositories:

- https://github.com/f8bsd9yqgp-maker/Solved-conjectures-
- https://github.com/1337isnot1337/solved-conjectures

No relevant matching entries were returned. The competitor's two matches for the numeric ID were unrelated Frankl transport data. Both repositories were checked again for Cheeger Pareto immediately before submission; both returned no matches. Targeted web searches for the exact title, both source IDs, Cheeger/Pareto terminology and the cut-polytope formulation located the original discussions and unrelated edge-expansion literature, but no earlier resolution of the revised conjecture. This is targeted screening, not an exhaustive review of every publication, branch or unindexed file.

## Definitions and original statement

For a finite simple graph G=(V,E), n=|V|>=2, k=floor(n/2), write d_G(S) for the number of edges with exactly one endpoint in S. For nonnegative x indexed by V write x(S)=sum_{v in S}x_v. Define

    h(G) = min_{1 <= |S| <= k} d_G(S)/|S|,
    P_G = { x >= 0 : x(S) <= d_G(S) whenever |S| <= k },
    rho(G) = min_{x Pareto-efficient in P_G} x(V).

Pareto efficiency means there is no distinct feasible y with y_v >= x_v for every v. The revised conjecture asserts rho(G) >= k h(G) for every finite simple graph.

## Theorem

For each odd integer s>=7 there is a connected simple graph G_s on 3s+1 vertices such that

    h(G_s) = 2 - 1/s,
    rho(G_s) <= 3s-1,
    k h(G_s) - rho(G_s) >= (s-1)/(2s) > 0.

Consequently the conjecture is false. The counterexample family has unbounded order.

## Construction

Write t=(s-1)/2. Build H from three disjoint cliques C_0,C_1,C_2, each with vertices (i,j), 0<=j<s. For each i modulo 3 and 0<=j<t, add the edge from (i,j) to (i+1 mod 3,t+j). These cross edges constitute a matching in H; each clique has exactly 2t=s-1 cross-edge incidences. Add a new universal vertex u adjacent to every vertex of H to obtain G_s. The graph is simple and connected. Here N=|H|=3s and k=(3s+1)/2.

## Cut lemma

For every T subset of V(H) with |T|<=k,

    d_H(T) >= |T|-1,

and in fact d_H(T)>=|T| unless T is exactly one of the three full cliques. Each full clique has d_H(C_i)=s-1.

Proof. If no clique is fully contained in T, write a_i=|T intersect C_i|. Each a_i<=s-1 and the internal clique cut contributes a_i(s-a_i)>=a_i. Summing and ignoring nonnegative cross-edge contributions proves d_H(T)>=|T|.

Otherwise T contains precisely one full clique, since k<2s. Let r=|T|-s, so 0<=r<=(s+1)/2. If r=0 the cut size is s-1 by construction. If r>=1, each of the r extra vertices can absorb at most one cross edge from the full clique, since cross edges form a matching. At least s-1-r of that clique's cross edges remain in the cut. The other two cliques, with selected sizes b,c and b+c=r, contribute

    b(s-b)+c(s-c) >= r(s-r).

Consequently d_H(T)>=s-1-r+r(s-r). Subtracting |T|=s+r gives r(s-r-2)-1>=0, since s>=7 and r<=(s+1)/2 imply s-r>=3. This proves the lemma. QED.

## Feasible Pareto-efficient point

Define x_u=N-1 and x_v=0 for v in H. For any admissible S not containing u, x(S)=0<=d_G(S). If u is in S, let T=S minus {u}. Then

    d_G(S)=N-|T|+d_H(T)>=N-1=x(S).

Thus x is feasible. Each S_i={u} union C_i has size s+1<=k and cut size N-s+(s-1)=N-1=x(S_i). These three tight sets cover all vertices. If y>=x is feasible, for any v select an S_i containing v; then y(S_i)<=x(S_i) and all coordinate differences are nonnegative, forcing y_v=x_v. Thus x is Pareto-efficient. In particular rho(G_s)<=N-1=3s-1.

## Exact Cheeger constant

Let S be nonempty and |S|<=k. If u is absent then d_G(S)=|S|+d_H(S). The cut lemma shows that its ratio is at least 2 except when S is a full clique, where it equals 2-1/s.

If u is present and |S|<=k-1, the feasibility estimate gives d_G(S)/|S| >= (N-1)/(k-1)=2.

If u is present and |S|=k, then T=S minus {u} has size k-1=(3s-1)/2>s, so it is not a single clique. The stronger cut lemma implies d_G(S)>=N. Its ratio is at least N/k=2-1/k>2-1/s, because k>s.

The full clique attains the smallest ratio, proving h(G_s)=2-1/s.

## Strict violation

    k h(G_s) - rho(G_s)
      >= ((3s+1)/2)(2-1/s) - (3s-1)
       = (s-1)/(2s) > 0.

This completes the disproof. The exact value of rho is not needed or claimed.

## Reproducible computational sanity check

Run `python verify.py --s 7` (Python 3.10+). This constructs the graph and enumerates every nonempty subset of size at most k, using exact integer arithmetic and Gray-code updates. It checks feasibility, the minimum cut ratio, tight-set coverage, and strict violation. The run checked 2,449,867 cuts, finding h=13/7 and a Pareto-efficient witness of weight 20, so k h=143/7>20. The recorded output is in verification.txt. The infinite-family proof is independent of this enumeration; the script is only an audit. The check was rerun immediately before submission and passed.

## Status

- Revised universal statement: disproved by written construction, subject to independent mathematical review.
- Numerical case or hillclimb: no.
- Repository searches: no relevant match in the queried indexes and default-branch searches.
- Public priority: no earlier revised-statement solution found in targeted searches; not certified globally.
- Formal proof assistant: not performed.
