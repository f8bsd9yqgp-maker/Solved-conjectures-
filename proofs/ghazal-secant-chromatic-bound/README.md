# Ghazal–Al-Mniny secant-free normal-tree coloring conjecture: unbounded chromatic number

AI-assisted mathematical research note, 26 November 2026. General analytical disproof of the conjectured universal chromatic bound, and hence of the earlier four-color conjecture. Independent review and worldwide priority remain unconfirmed.

## Sources and screening

- Darine Al-Mniny and Salman Ghazal, *Remarks on the subdivisions of bispindles and two-blocks cycles in highly chromatic digraphs*, arXiv:2010.10787 (2020), Conjecture 4: https://arxiv.org/abs/2010.10787 . The full-text mirror https://www.academia.edu/106231637/Remarks_on_the_subdivisions_of_bispindles_and_two_blocks_cycles_in_highly_chromatic_digraphs identifies the four-color formulation.
- Salman Ghazal, *A New Four-Color Problem*, AppliedMath 6(8), 133 (2026), Conjecture 1 and Problem 1: https://doi.org/10.3390/appliedmath6080133 . The article search extract reproduces the precise conjecture and definition. A subsequent direct retrieval of the article returned HTTP 429.
- Darine Al-Mniny, Maria Abiaad and Salman Ghazal, *About the Chromatic Number of Graphs Without Secant Edges Relative to Normal Spanning Trees*, posted 24 November 2026, https://www.preprints.org/manuscript/202611.2375 . Full HTML inspected, including Definition 2, Conjecture 2, Problem 1, and the concluding remarks. The paper proves a bound for at most two branching vertices per root-to-leaf path and a bound depending on the number of branching vertices; it explicitly leaves the universal bound open.

Before selecting the candidate, competitor README blob 6823cef6300ed1de1f7dedb19a00d554fd9ead1c was fetched first, followed by user README blob 0afb39427c005842bd723e7ce10a15e64b108660. Default-branch searches of both repositories for Ghazal secant edges, appliedmath6080133, 202611.2375, and normal spanning tree returned no relevant result. Generic competitor hits were retrieved and inspected; they concerned unrelated conjectures and contained no matching terms.

- https://github.com/1337isnot1337/solved-conjectures
- https://github.com/f8bsd9yqgp-maker/Solved-conjectures-

Targeted searches for the original paper, authors, secant-free normal spanning trees, unbounded chromatic number and counterexamples identified no previous general resolution. Online graph coloring adversary arguments are classical; see e.g. *Tight Bounds for Online Coloring of Basic Graph Classes*, https://doi.org/10.1007/s00453-020-00759-7 . We do not claim novelty for online adversary methods in general. The specific suffix game and universal normal-tree construction are presented here as a disproof of the stated conjecture. No exhaustive worldwide priority certification is claimed.

## Statement

A rooted spanning tree T of a finite simple graph G is normal when the endpoints of each graph edge are comparable in the ancestor order of T. Edges ab and cd, with the upper endpoints listed first, are secant if a<c<b<d or c<a<d<b in the strict ancestor order. The 2026 conjecture asserts that an absolute constant bounds the chromatic number of every G admitting a normal spanning tree with no secant edges. The 2020 conjecture asserts the particular bound four.

## Theorem

For every positive integer q, there is a finite connected simple graph G_q with a normal spanning tree T_q, no secant edges relative to T_q, and chromatic number greater than q. The rooted tree can be taken to have depth at most 2^q, where depth counts edges from the root. In fact, the construction gives an explicitly specified universal finite graph for each q, independent of any coloring.

## 1. The suffix game

Start with a rooted path consisting of one vertex. At every stage maintain an ordered list S=(s_1,...,s_m) of active vertices on the current path, ordered from root toward its last vertex. Call a vertex active if it is not strictly between the endpoints of any previously added edge on this path. The last vertex is always active. Initially S is just the root.

A legal extension chooses an index i in {1,...,m}, appends a new vertex v as a child of the current last vertex in the rooted path, and adds edges from v to all vertices s_i,...,s_m. In particular the edge to its parent s_m is present.

Every new edge has comparable endpoints. It cannot be secant with an old edge ab: because v is below every old vertex, a secant pair would require its upper endpoint s_j to satisfy a<s_j<b, contrary to activity. Two new edges share v and cannot be secant. The active list after the move is exactly

    (s_1,...,s_i,v).

Indeed the edge s_i v covers all old active vertices after s_i in the path interior, and no earlier active vertex is covered. Old inactive vertices remain inactive. This proves the invariant by induction.

Assume a proper coloring is assigned as the path grows, with earlier colors fixed. A move must assign v a color not present on the selected suffix. The following forcing lemma works even if the available palette is unlimited.

## 2. Forcing lemma

Let P be the entire active list at some stage, so P is nonempty. For each integer r>=1, a strategy of at most 2^r-1 legal moves either exposes an impossible coloring move (if the palette is exhausted) or obtains an active list P followed by a nonempty list of fresh vertices using at least r distinct colors. All vertices of P remain active throughout, with unchanged colors. The strategy may observe the colors already assigned.

Proof by induction. For r=1, append a vertex adjacent only to the last vertex of P. The new list is P followed by that one vertex.

For r>=2, apply the lemma for r-1 with protected prefix P. If coloring fails we are done. Otherwise the active list is P,A, with the fresh list A using at least r-1 colors. If A already uses at least r colors, stop. Otherwise A uses exactly r-1 colors.

Now protect the entire current active list P,A and apply the same induction hypothesis a second time. If it succeeds, the list is P,A,B, with B using at least r-1 colors. If the union of colors on A and B contains at least r colors, stop. Otherwise both lists have exactly the same set of r-1 colors.

In this remaining case append a vertex v adjacent to the entire suffix B, by choosing the first vertex of B as the suffix start. The active list becomes P,A,b_1,v. The color of v is absent from B and thus absent from A, so A together with v uses at least r colors. All of P remained protected. If no color for v exists, the failure alternative holds.

The number of moves is at most 2(2^(r-1)-1)+1=2^r-1. This completes the induction.

In particular, starting at the root and protecting it, a palette of q colors can be exhausted in at most 2^q moves: first obtain q colors among the fresh active vertices, then append a vertex adjacent to that entire fresh suffix. It has no available color. If an earlier move failed, the contradiction occurs sooner.

## 3. Turning the adaptive strategy into a fixed finite graph

The suffix game is only a proof device. To define G_q without reference to any coloring, let h=2^q. Construct a rooted tree of height h whose root has active list consisting of itself.

At every node w at depth less than h, with active list S=(s_1,...,s_m) on its ancestor path, create exactly m distinct children v_1,...,v_m. For each i, join v_i to the vertices s_i,...,s_m, and define the child's active list to be (s_1,...,s_i,v_i). Do this recursively at every node until depth h. The tree parent-child edge is among the graph edges because w=s_m. There are no other graph edges.

This is finite, since the active list at depth d has at most d+1 vertices and the depth is finite. The tree spans the graph; every graph edge joins an ancestor to a descendant, so the spanning tree is normal and the graph connected. No secant pair exists: any putative secant pair lies along a single ancestor path, but along that path each step is a legal suffix-game move and Section 1 proves that no such pair can appear.

Suppose there were a proper q-coloring of G_q. Start at the root and observe its assigned color. Follow the forcing strategy of Section 2, choosing the child corresponding to each legal suffix move. Every required child is present in the fixed graph, because it contains every legal continuation through depth h. All colors along the chosen path are inherited from the hypothetical proper coloring, and thus each chosen child must have a color absent from its neighbors in the selected suffix. The forcing lemma guarantees a move with all q colors forbidden no later than depth h. Its child exists but cannot be colored. Contradiction.

Therefore chi(G_q)>q for every q>=1. This disproves any absolute bound, including four. QED.

## 4. Scope and relation to prior work

Each individual root-to-leaf path with the edges induced on it is a noncrossing ordered graph and hence outerplanar. The high chromatic number is caused by requiring one coloring to work simultaneously on all the branches; no branch is claimed to require more than three colors in isolation. The recent bounds in terms of the number of branching vertices remain consistent with the construction: the depth and branching complexity grow with q.

The result concerns the exact secant definition in the cited papers. It does not settle Cohen et al.'s separate conjectures about subdivisions of oriented cycles, nor does it establish optimal order, minimum branching depth or the exact chromatic number of these examples. No numeric dimension restriction, hillclimb or optimization is used.

## 5. Reproducibility

Run python verify.py with Python 3. The script independently checks the finite suffix-color game by memoization, using canonical color patterns, for q=1,...,5. It also enumerates every node of the universal tree through depth 8, checking the active-list invariant and absence of crossings on all ancestor paths. All those checks were actually executed and passed. The q=6 optional search was interrupted after a 10-second limit; no q=6 computational verification is claimed. The analytical argument proves the full theorem regardless of the finite checks. See verification.txt.

No Lean formalization or independent peer review has yet been performed.
