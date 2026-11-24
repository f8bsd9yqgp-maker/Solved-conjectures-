# Graffiti.pc Conjecture 161 — spanning-tree leaf bound

24 November 2026. AI-assisted written proof (GPT-6.2). Independent review, publication priority and Lean verification remain pending.

## Statement and source

E. DeLaViña, *Written on the Wall II*, Conjecture 161, announced 8 August 2005, marked open in the [6 November 2026 catalogue, page 92](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf#page=92).

For a nonempty finite simple connected graph G, let L_s(G) be the maximum number of degree-one vertices in a spanning tree of G. Let λ_max(H) be the maximum, over vertices v of H, of the independence number of the graph induced by the open neighborhood of v. The conjecture is L_s(G) ≥ λ_max(complement G).

## Lemma

If G contains a proper clique C of cardinality k≥2, then L_s(G)≥k.

Because G is connected and C is proper and nonempty, there is an edge xy with x in C and y outside C. The edges from x to all other vertices of C, together with xy, form a star subgraph with k leaves. Extend this tree to a spanning tree by repeatedly attaching a new vertex along one edge from the current tree; connectedness guarantees such an edge until every vertex belongs to the tree. Each addition creates a leaf and loses at most one previous leaf. Hence the spanning tree has at least k leaves. ∎

## Proof of the conjecture

Let k=λ_max(complement G). For k≥2, choose a vertex v and an independent set C of size k in its complement neighborhood. The vertices of C are pairwise adjacent in G, and C excludes v, so C is a proper clique. The lemma gives L_s(G)≥k. For k=0 the inequality is automatic, including the singleton graph. For k=1 the graph has at least two vertices, and every spanning tree has at least two leaves. This covers all cases. ∎

## Stronger bound and sharpness

For every connected noncomplete graph, a maximum clique is proper and has at least two vertices. Therefore L_s(G)≥ω(G), where ω is the clique number. For each k≥2, take a k-clique, choose a vertex x of it, and attach a two-edge pendant path x–y–z. The vertex z is nonadjacent to the whole clique, hence λ_max(complement G)≥k; equality follows because the graph's clique number is k. The graph has k+2 vertices and no universal vertex, so no spanning tree is a star; every spanning tree has at least two internal vertices and at most k leaves. The lemma gives equality. Thus the conjectured bound is sharp for every k≥2.

## Verification status

The original statement and definitions were checked against the source catalogue. The argument is elementary and complete as written, but neither external acceptance nor exclusive discovery priority is claimed. No machine-checked Lean proof is supplied.
