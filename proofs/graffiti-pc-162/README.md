# Graffiti.pc Conjecture 162 — simplicial vertices and spanning trees

24 November 2026. AI-assisted written proof (GPT-6.2). Not independently reviewed or Lean-verified; publication priority not established.

## Statement

E. DeLaViña, *Written on the Wall II*, Conjecture 162, announced 8 August 2005 and listed open in the [6 November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf).

For a finite simple connected graph G of order at least two, let L_s(G) be the maximum number of leaves of a spanning tree, δ(G) the minimum degree, λ(v)=α(G[N(v)]) the independence number of the open neighborhood, and m_λ(G) the number of vertices attaining the minimum λ(v). Then

L_s(G) ≥ m_λ(G) floor(1/δ(G)).

The singleton is excluded because the published expression divides by zero there.

## Lemma
Every finite connected noncomplete graph admits a spanning tree in which every simplicial vertex (a vertex whose neighbors form a clique) is a leaf.

Choose two nonadjacent vertices and a shortest path between them. Its first internal vertex has two nonadjacent neighbors and is therefore nonsimplicial. Root a breadth-first search spanning tree at any nonsimplicial vertex r. If a simplicial vertex v has a child w and parent u, then uw is an edge of G since both are neighbors of v. The tree distances from r equal the graph distances, but the edge uw gives a route to w one edge shorter than the tree path. Contradiction. Every simplicial vertex is distinct from the root and has no children, hence has tree degree one. ∎

## Proof
If δ(G)≥2, the floor factor is zero, and the inequality is automatic. If δ(G)=1, every vertex has a nonempty neighborhood and a degree-one vertex has local independence number 1. Thus min λ=1, and the vertices attaining it are precisely the simplicial vertices. If G is noncomplete, the lemma produces a spanning tree containing every such vertex as a leaf. If G is complete, δ=1 implies G=K₂, whose spanning tree has two leaves and both vertices attain min λ. This proves the inequality for every graph on which the expression is defined. ∎

Equality is attained for every nontrivial tree: its simplicial vertices are exactly its leaves, and its unique spanning tree is itself.

## Verification
The accompanying Python program checks the BFS witness on all connected graphs of minimum degree 1 in the NetworkX graph atlas. A replay on 24 November 2026 passed all 412 graphs. This is a finite sanity check, not the general proof. The general proof is above. The elementary structural lemma is not asserted to be novel; no exclusive priority or external acceptance is claimed.
