# The sharp list-majority edge-colouring threshold

27 November 2026 — AI-assisted candidate proof. Independent review and priority confirmation pending.

## 1. Statement

Conjecture 22 of P. Pękała and J. Przybyło, *On List Extensions of the Majority Edge Colourings*, Electronic Journal of Combinatorics 32(4) (2025), #P4.38, DOI https://doi.org/10.37236/13882, arXiv:2502.12688v1, p. 26, asserts that for every integer k >= 2, a finite simple graph G of minimum degree at least k^2 has a 1/k-majority edge colouring from every assignment of lists of size k+1. The claim is that each edge receives a colour in its own list and each colour occurs at most floor(d_G(v)/k) times at each vertex v. Theorem 9 of that paper proves the bound 2k^2-2k, in particular settling k=2. The proof here establishes every remaining k >= 3, without assumptions about regularity, connectivity or intersections of the lists.

## 2. Established ingredients

(A) Nash-Williams–Tutte spanning-tree packing theorem: a graph contains h edge-disjoint spanning trees if every partition into p nonempty parts has at least h(p-1) crossing edges.

(B) Hasanvand, *Modulo orientations with bounded out-degrees*, Discrete Mathematics (2024), arXiv:1702.07039v3, Theorem 1.5, p. 3: for integer L >= 3, a graph H containing 2L-2 edge-disjoint spanning trees has an orientation with prescribed outdegree residues p(v) modulo L whenever sum_v p(v) = |E(H)| modulo L. The theorem also gives bounds on the outdegrees, which are not needed here. It covers even as well as odd L. See https://arxiv.org/abs/1702.07039 and https://www.sciencedirect.com/science/article/pii/S0012365X23003205.

(C) Galvin, *The List Chromatic Index of a Bipartite Multigraph*, Journal of Combinatorial Theory, Series B 63 (1995), 153–158, DOI https://doi.org/10.1006/jctb.1995.1011: a bipartite multigraph of maximum degree at most L can be properly edge-coloured from arbitrary lists of size L.

## 3. Dense-block decomposition with a one-edge interface

For a nonempty vertex set B of a finite simple graph G, define C(B) as the graph obtained from G[B] by adding a new vertex z and one edge zv for each v in B. Fix a positive integer h >= 2. There exist pairwise disjoint nonempty sets B_1,...,B_t such that each C(B_i) contains h edge-disjoint spanning trees and the graph on the remaining vertices R is (2h-3)-degenerate (every nonempty induced subgraph has a vertex of degree at most 2h-3).

Proof. Choose disjoint blocks with the stated cone property greedily until no additional block exists. If some nonempty S subset R induces minimum degree at least 2h-2, then e(G[S]) >= (h-1)|S|, so e(C(S)) >= h|S|. In C(S), choose an inclusion-minimal set T with |T| >= 2 and e(C(S)[T]) >= h(|T|-1). It exists because T=V(C(S)) qualifies. For any partition of T into p >= 2 nonempty parts A_i, each part is proper; a singleton has zero edges, and a nonsingleton has fewer than h(|A_i|-1) edges by minimality. Therefore the crossing edge count is at least h(|T|-1)-h(|T|-p)=h(p-1). By (A), C(S)[T] has h edge-disjoint spanning trees.

If z belongs to T, set B=T minus {z}; C(B) is exactly C(S)[T]. Otherwise G[T] itself has h spanning trees. Simplicity and e(G[T]) >= h(|T|-1) imply |T| >= 2h. Add z and extend each of the h trees by a different edge zv (choose h distinct vertices in T). These remain edge-disjoint spanning trees of C(T). In either case there is a new block in R, contrary to maximality. QED.

## 4. Orientation condition and available residues

Fix k >= 3. Write L=k+1, h=2L-2=2k, D=2h-3=4k-3. For every original vertex v write d=d_G(v), q=floor(d/k), s=Lq-d. Euclidean division d=kq+r, 0<=r<=k-1, gives q>=k and s=q-r>=1.

We seek an orientation of G with outdegree x_v and indegree d-x_v such that

    ceil(x_v/L)+ceil((d-x_v)/L) <= q.                 (1)

For x=La+t, 0<=t<L, the first ceiling is a if t=0, otherwise a+1, and the second is q-a-floor((s+t)/L). It follows that if s>=L-1 all residues t are permitted; if 1<=s<L-1, the permitted residues are exactly

    0, L-s, L-s+1, ..., L-1.                         (2)

In particular 0 and -1 are always permitted. The longest consecutive cyclic run of forbidden residues has length f=max(0,L-s-1). Any f+1 consecutive integers contain a permitted residue.

## 5. Constructing a suitable orientation

Apply Section 3 with h=2k. Orient every edge between distinct blocks arbitrarily. The remainder R admits an ordering v_1,...,v_m in which each v_i has at most D neighbours among v_{i+1},...,v_m, by iteratively removing a vertex of degree at most D. Process this order backwards. When processing v_i, its already-oriented incident edges are precisely those to later vertices of R (at most D); its edges to earlier R vertices and to all blocks remain flexible. If s>=L-1, orient these arbitrarily. Otherwise at least d-D flexible edges are available, and

    d+s = Lq >= k(k+1) >= 5k-3 = D+L-1,

because k(k+1)-(5k-3)=(k-1)(k-3)>=0. Therefore d-D>=L-s-1=f. By choosing how many of these flexible edges point out of v_i, its total outdegree can be any integer in an interval of length at least f+1 (counting integers). Select a permitted residue, and fix these orientations. They cannot affect the outdegrees of previously processed vertices. After this process all vertices in R meet (1); all block-boundary edges are oriented.

For a block B, write b(v) for the number of its already-oriented outgoing boundary edges. In C(B), prescribe p(v)=-b(v) mod L for every original vertex v in B. Prescribe p(z)=|E(C(B))|-sum_{v in B}p(v) mod L at the auxiliary root. The prescription satisfies the global congruence of (B). Since C(B) has h=2L-2 edge-disjoint spanning trees, orient it using (B). Delete z and all its incident edges. At each v in B its total outdegree in G (including the fixed boundary edges) is 0 or -1 modulo L: before deletion it was 0, and deletion subtracts either zero or one from the outdegree. Both residues are permitted by Section 4. This may be done independently for each block, because all edges between blocks were fixed beforehand. Thus all vertices of G satisfy (1).

## 6. Bipartite detachment and list-colouring

Replace each vertex v with ceil(x_v/L) outgoing clones and ceil((d(v)-x_v)/L) incoming clones (zero if the respective count is zero). Partition the outgoing and incoming incident edges separately into groups of size at most L, one group per clone. An oriented edge uv becomes an edge from its outgoing clone at u to its incoming clone at v. The resulting graph H is bipartite (outgoing clones versus incoming clones) and has maximum degree at most L. Every original edge corresponds to exactly one edge of H, retaining its original list of L colours.

Apply Galvin's theorem (C). Pull the proper list edge-colouring back to G. Each colour can occur at most once at each clone of v; by (1), v has at most q=floor(d(v)/k) clones in total. Hence each colour occurs at most q times at v. This is precisely the conjecture. QED.

The case k=2 is Theorem 9 of the original paper. Combining it with Sections 3–6 proves the statement for every integer k>=2, subject to independent review of this argument.

## 7. Sharpness

The non-list lower bound from Pękała–Przybyło, *On Generalised Majority Edge-Colourings of Graphs*, DOI https://doi.org/10.37236/12416 (Observation 10), transfers by assigning the same list of k+1 colours to every edge. For completeness: remove a Hamilton cycle from K_(k^2+1) and add a new vertex adjacent to all old vertices. The old vertices have degree k^2-1, the new vertex degree k^2+1. Each colour would occur exactly k-1 times at every old vertex. Some colour must occur k times at the new vertex by the degree sum and majority cap. The sum of degrees of that colour class would be (k^2+1)(k-1)+k, odd for all k, contradicting the handshake lemma. Thus k^2 is the sharp threshold. The lower bound is prior work.

## 8. Method transfer, scope, and verification status

- Achour saturation project: isolate blocks, use a controlled interface, then compose local solutions while preserving an exact invariant. Here the interface is one temporary root edge per block vertex.
- Eulerian strong-majority project: identify the modular obstruction and use a local correction. Here the allowed outdegree residues and the root's freely chosen residue replace the earlier tour exchanges.
- Non-list majority project: augment a graph, invoke an established theorem, then delete the added edges with bounded effect. Here the added edges absorb the global congruence; Galvin's theorem handles arbitrary lists after bipartite splitting.

The previous candidate proofs are not logical prerequisites. The three classical theorems are explicit dependencies. The argument is analytical and does not depend on finite tests. No Lean verification or independent refereeing has been performed. No polynomial-time complexity claim is made for the displayed block-selection procedure. The conclusion is a candidate resolution rather than certified publication.

## 9. Duplicate and literature screening

27 November 2026: inspected the original preprint, Conjecture 22 on p. 26, and Theorem 9; inspected the statement of Hasanvand's Theorem 1.5 on p. 3 of arXiv:1702.07039v3. The journal publication metadata confirms the 2025 article. Searches for the exact conjecture, article identifier, and majority list-colouring with modulo orientations returned the original statement and related work, not a matching completed proof. The preprint numbering is explicitly used here.

Both repositories were searched by README, code (2502.12688, list majority, list-majority, 13882), and issues. No matching resolution was identified. Competitor: https://github.com/1337isnot1337/solved-conjectures (README blob e0493dac21e0169522567c34aca30f532c0cca55). User: https://github.com/f8bsd9yqgp-maker/Solved-conjectures- (README blob 99587333ed0e95701ffb1e35515fdf016f711e86). Search hits for the numerical DOI suffix and broad terms in the competitor repository were unrelated by filename/description; the prior user proof concerns the common-palette, non-list conjecture. Search coverage is not exhaustive; unindexed and unpublished results may exist. No priority claim is made. The candidate proof was emailed to both original authors on 27 November 2026 and posted to this repository.