# Levit–Itskovich's subsequence-counting conjecture: proof for all graphs

AI-assisted research note, 26 November 2026. Complete analytical proof; independent review, formal verification and worldwide discovery priority remain unconfirmed.

## Source and priority audit

Vadim E. Levit and Elizabeth J. Itskovich, *New Upper Bounds on the Number of Maximum Independent Sets in a Graph*, Axioms 14 (2025), 900, Section 5, Conjecture 1, https://doi.org/10.3390/axioms14120900 . Full published article inspected at https://www.mdpi.com/2075-1680/14/12/900 . The article gives the product bound with prefactor ((n+1)/2)^2 in Corollary 15 and conjectures the improved prefactor n. The January 2025 preprint https://www.preprints.org/manuscript/202501.2351 was also located. We credit the paper's projection lemma, graph interpretation of monotone subsequences, and existing bounds.

Before selecting the problem, the competitor repository README (blob 79464b8ad27852b02ee2f47795cdb4b7ca429ea3) was retrieved first, then the user's README (blob bef1cb04f0dcabd49a282429d885994841918ff6). Searches in both for Itskovich, axioms14120900, and longest increasing decreasing subsequences identified no relevant result. Competitor hits for the generic subsequence phrase concerned the Pantone–Bóna and Elizalde–Rivera–Zhuang problems, not this conjecture; relevant-looking catalog and proof matches were inspected. The DOI search was repeated immediately before submission, with no matches in either repository.

- https://github.com/1337isnot1337/solved-conjectures
- https://github.com/f8bsd9yqgp-maker/Solved-conjectures-

Targeted public searches using the article title, DOI, author names, subsequence-count conjecture and maximum independent-set/maximum-clique product terminology found no explicit prior general resolution. Related earlier counting results are credited; targeted screening does not guarantee worldwide priority or exhaustive coverage of all unindexed literature.

## Definitions and result

For a nonempty finite simple graph G of order n, let a=alpha(G), b=omega(G), and let I and C be the collections of its maximum independent sets and maximum cliques, respectively. Put k=n-a-b+1. Since any independent set and clique intersect in at most one vertex, k>=0.

Theorem. For every such graph,

    |I| |C| <= n 4^k.

More precisely, if every pair (S,T) in I x C intersects, then |I||C|<=n 2^k. Otherwise k>=1 and |I||C|<=(1+2(a+b))4^(k-1). These stronger case-specific bounds are also proved below.

For a sequence of distinct real numbers, use its inversion graph: vertices are indices and edges join inversions. Its maximum independent sets and cliques correspond exactly to longest increasing and decreasing subsequences, respectively. Thus the graph theorem proves the original Conjecture 1 for every length n>=1. The coefficient n in the original inequality is attained by any increasing sequence (k=0, one LIS and n singleton LDSs).

## Elementary counting lemma

A graph H on h vertices with independence number t has at most 2^(h-t) maximum independent sets. Fix one maximum independent set S of size t. Any other maximum independent set J is uniquely determined by X=J minus S: its part inside S must consist of every vertex of S nonadjacent to all vertices of X. Otherwise that vertex could be added to J, contradicting maximality. Thus the projection J -> X is injective, and there are at most 2^(h-t) choices. The same bound holds for maximum cliques with t replaced by the clique number, by complementation. This elementary projection argument is related to the lemma in Section 2.1 of the original paper; no novelty is claimed for it.

## Case 1: all maximum independent-set/clique pairs intersect

For each vertex v write I_v and C_v for the numbers of maximum independent sets and maximum cliques containing v. Every pair intersects in exactly one vertex, so

    |I||C| = sum_v I_v C_v.

If either count vanishes the corresponding summand is zero. Otherwise let d=deg_G(v). Removing v from sets counted by I_v gives maximum independent sets of size a-1 in the induced graph on the n-1-d nonneighbors of v. Its independence number is exactly a-1, since an independent set there extends by v in G. Likewise removing v from cliques counted by C_v gives maximum cliques of size b-1 in the d-vertex neighborhood graph, which has clique number exactly b-1. The lemma gives

    I_v <= 2^(n-d-a),
    C_v <= 2^(d-b+1),
    I_v C_v <= 2^(n-a-b+1)=2^k.

Summing proves |I||C|<=n 2^k<=n 4^k.

## Case 2: a disjoint maximum pair exists

Fix disjoint S in I and T in C. Let R=V(G) minus (S union T), and put r=|R|=k-1>=0.

For t in T define d_t=|N(t) intersect S|. Because S is maximum independent and t is outside it, d_t>=1. For s in S define e_s to be the number of vertices of T not adjacent to s. Since T is maximum clique, e_s>=1.

Set

    w_t=2^(1-d_t), u_s=2^(1-e_s),
    W=sum_{t in T} w_t, U=sum_{s in S} u_s.

All weights lie in (0,1], so W<=b and U<=a.

Every maximum independent set contains either zero or exactly one vertex of T. Those containing none are maximum independent sets of G[S union R], whose independence number is a because S is present. Their number is at most 2^r by the lemma.

For a fixed t in T, any maximum independent set whose intersection with T is {t} consists of t and an independent set of size a-1 in the graph induced on the nonneighbors of t in S union R. If such a set exists, that graph has independence number exactly a-1; it has at most a+r-d_t vertices. By the lemma there are at most 2^(r+1-d_t)=2^r w_t such sets. If no such set exists the same upper bound is automatic. Summing yields

    |I| <= 2^r(1+W).

Applying the complementary argument to maximum cliques gives

    |C| <= 2^r(1+U).

The decisive observation is that every cross pair (s,t) is either adjacent or nonadjacent, and a large number of choices on one side causes exponential suppression on the other:

    WU = sum_{s in S,t in T} u_s w_t.

For adjacent pairs the sum is at most

    sum_{t in T} d_t w_t <= b,

because u_s<=1 and j*2^(1-j)<=1 for every integer j>=1.

For nonadjacent pairs the sum is at most

    sum_{s in S} e_s u_s <= a,

by the same elementary inequality and w_t<=1. Therefore WU<=a+b.

It follows that

    |I||C| <= 4^r(1+W)(1+U)
            <= 4^r(1+2(a+b))
            <= 4^(k-1)(1+2n)
            <= n 4^k.

The last inequality holds for every positive integer n. This completes both cases and proves the theorem. QED.

## Verification

The accompanying Python script was executed, not merely drafted. It computes exact maximum-independent-set and maximum-clique counts via NetworkX maximal-clique enumeration, checks both strengthened bounds in the appropriate cases, and independently uses dynamic programming to count longest increasing and decreasing subsequences for every permutation through length eight.

Results: 1252 nonempty graphs in the graph atlas; 1000 seeded random graphs of orders 2 through 24; 46233 permutations through length eight. All checks passed. The analytical proof covers every finite order and is independent of these finite sanity checks.

No hillclimb, numerical optimization, or restriction to a fixed order is used in the proof. No independent peer review or Lean formalization has been performed.
