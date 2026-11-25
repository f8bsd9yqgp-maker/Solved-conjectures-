# Edge-irregularity deletion conjecture: planar subcubic counterexamples

AI-assisted note, 25 November 2026. Independent academic review and priority for the restricted-class strengthening remain unverified.

Source: J. Bensmail, N. Catherinot, F. Fioravantes, C. Marcille and N. Oijid, Graph Irregularity via Edge Deletions, arXiv:2511.14514v1 (18 November 2025), Conjecture 1, https://arxiv.org/html/2511.14514v1.

The conjecture states that an absolute constant c exists such that every connected simple graph G with m edges has I_e(G)<=m/3+c, where I_e is the minimum number of edges whose removal makes all remaining adjacent vertices have unequal degrees.

Priority: Myeongjin Kang, Unbounded excess over the one-third edge-irregulator bound, https://mathdb.com/abs/2611.00030 (version 1 dated November 4, 2026), previously reports connected simple examples with 6t+1 vertices, 8t edges and I_e=3t. This note independently derives the rooted obstruction and strengthens the reported general disproof to planar subcubic graphs. It is not a first-discovery claim for the original conjecture. The priority of the planar subcubic strengthening is not established.

## Theorem
For every integer k>=2 there exists a finite connected simple planar graph G_k of maximum degree three, with 14k+26 vertices and 18k+33 edges, satisfying
I_e(G_k) >= 6(k+2)+ceil((k-1)/3).
Consequently I_e(G_k)-|E(G_k)|/3 >= 1+ceil((k-1)/3), which is unbounded. In particular the conjecture fails even in this restricted class, and the asymptotic coefficient on this class must be at least 19/54.

## Rooted obstruction
Take vertices 0,...,6 and edges 05,06,12,15,16,23,34,56; root 4. This is a diamond (K4 minus an edge) with a three-edge tail attached at one of the diamond's degree-two vertices. The root is a leaf. Allow arbitrary additional edges at the root, but none at the six other vertices. Every edge-irregulator must delete at least three edges from the copy.

Proof: initially 2 and 3 have degree two. To remove or resolve their conflict, at least one of 12,23,34 must be deleted. Suppose at most two edges of this copy are deleted. If no diamond edge is deleted, 5 and 6 remain adjacent of degree three. Thus exactly one tail edge and exactly one diamond edge must be deleted.

If the tail deletion is 23 or 34, the diamond's vertices 1,5,6 all have degree three and form a triangle. Deleting 05 or 06 leaves two adjacent vertices of degree three in that triangle. Deleting a triangle edge lowers both endpoints to degree two, including at least one of 5,6; that endpoint remains adjacent to vertex 0 of degree two. All choices fail.

If the tail deletion is 12, vertex 1 becomes degree two. Deleting 56 makes vertices 5,6 degree two, each adjacent to 0 of degree two. Deleting 05 or 06 makes the respective endpoint 5 or 6 degree two and adjacent to 1 of degree two. Deleting 15 or 16 makes the respective endpoint 5 or 6 degree two and adjacent to 0 of degree two. Again all choices fail. Every conflict used avoids root 4, so external root edges cannot invalidate the argument.

## Construction and proof
Start with a path on k vertices. Attach two new leaves to each endpoint and one to each other vertex, so all original path vertices have degree three. This connector tree has k+2 leaves and 2k+1 edges.

At each leaf, attach two disjoint rooted obstruction copies by identifying their roots with that leaf. All other vertices of all copies are distinct. Each leaf now has degree three. Every new vertex has degree at most three. The graph is simple, connected and planar, since each planar gadget is attached to a planar tree at a single vertex.

There are 2(k+2) edge-disjoint gadgets, each with 8 edges and 6 new vertices. Hence the total edge count is 2k+1+16(k+2)=18k+33 and the vertex count is k+(k+2)+12(k+2)=14k+26. By the rooted obstruction, any edge-irregulator deletes at least 6(k+2) gadget edges.

There are k-1 original path edges, each initially joining two degree-three vertices whose incident edges all belong to the connector tree. For every such path edge e=uv, at least one connector edge incident to u or v must be deleted: otherwise e remains with both endpoint degrees three, regardless of gadget-edge deletions. A connector edge is incident to endpoints of at most three original path edges: at most three if it is itself a path edge, at most two if it joins a path vertex to a leaf. Thus at least ceil((k-1)/3) connector edges are deleted. These are disjoint from all gadget-edge deletions.

Adding the lower bounds proves the theorem. The excess over m/3 is at least 1+ceil((k-1)/3), and the limiting lower bound on I_e/m is (6+1/3)/18=19/54. No optimality or exact value of I_e for the entire graph is claimed.

## Verification
The companion standard-library Python verifier exhausts all 37 deletion sets of size at most two for the rooted obstruction and checks the graph counts, maximum degree, edge-disjointness and path-incidence bounds for k=2 through 200. The general proof is independent of these finite checks. No external peer review or Lean formalization has been performed.
