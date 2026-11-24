# Graffiti.pc Conjecture 241 — total domination and neighborhood components

24 November 2026. AI-assisted written proof (GPT-6.2). Independent review, publication priority and Lean verification remain pending.

## Statement and source
E. DeLaViña, *Written on the Wall II*, Conjecture 241, announced 23 February 2007 and listed open in the [November 2026 catalogue, p. 140](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf#page=140).
For a tree T, let S be its degree-two vertices, C its center, and c the number of connected components of the subgraph induced by N[S], the closed neighborhood of S. The stated inequality is
γ_t(T) ≥ floor(c + dist_avg(C)),
where γ_t is the minimum cardinality of a total dominating set and the average is over distinct center vertices.

## Stronger general theorem
For every finite nonempty simple graph G without isolated vertices, and every S ⊆ V(G), let c be the number of components of G[N[S]]. Then γ_t(G) ≥ max(2,c+1).

Proof. Each component of G[N[S]] contains a vertex s of S: every other vertex of N[S] has a neighbor in S. All neighbors of s belong to the same component as s. A total dominating set D must therefore meet each component, giving |D|≥c. If c≥1 and |D|=c, exactly one member of D belongs to each component and there are no members outside N[S]. Distinct components have no edges between them. Thus D is independent, contradicting the requirement that every member of D have a neighbor in D. Hence |D|≥c+1. Independently, every total dominating set of a nonempty loopless graph has at least two vertices. This proves the theorem. ∎

## Application and domain
The center of a finite tree has either one vertex or two adjacent vertices. For a two-vertex center the stated average is 1, hence the general theorem proves the conjecture. For a one-vertex center the published average over distinct vertices is empty; if assigned the natural value zero, the inequality also holds. Trees of order one have no total dominating set, so the result concerns nontrivial trees. Equality occurs on P4, where c=1, the two centers are adjacent, and γ_t=2.

## Verification
Exhaustive computation checked the stronger bound on all 986 nonisomorphic trees of orders 2 through 12; all passed. The general written proof is independent of the computation. See the [joint verifier](../graffiti-pc-315/verify_241_315.py). No machine-checked proof or claim of exclusive originality is made.
