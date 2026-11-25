# Hu–Han signed square-energy equality problem

**Status:** AI-assisted written proof candidate, November 24–25, 2026. Independent mathematical review, Lean verification and publication priority remain outstanding.

Source: Fu-Tao Hu and Xiao Han, [From the Square-Energy Conjecture to Signed Graphs: Sharp Bounds for Positive Square Energy](https://arxiv.org/abs/2608.18492), Problem 6.1.

## Claim

For a connected signed simple graph with n vertices and m edges, the known bounds are
$$n-1\le s^+\le 2m-n+1.$$
The lower equality holds exactly for signed trees or antibalanced complete signed graphs; the upper equality holds exactly for signed trees or balanced complete signed graphs. Balance means switching-equivalence to an all-positive signing; antibalance means switching-equivalence to an all-negative signing.

## Proof candidate

It suffices to characterize the upper equality, since negation of the signing interchanges the positive and negative spectral energies. The singleton is immediate. Write the signed adjacency matrix as A=X-Y, where X=A_+, Y=A_- are positive semidefinite with XY=0. Put q=2m-n+1 and let M be the Hadamard square of X, folded onto the graph support by adding X_ij^2(e_i-e_j)(e_i-e_j)^T for each unordered nonedge ij. This preserves the sum of entries, T=||X||_F^2=q, and all edge entries. The Schur product theorem makes M positive semidefinite and entrywise nonnegative.

By the DNN inequality of Liu–Tang–Zhang (arXiv:2607.18031) and Hu–Han (arXiv:2608.18492),
$$q=\operatorname{tr}(AX)=2\sum_{ij\in E}\sigma_{ij}X_{ij}
\le 2\sum_{ij\in E}|X_{ij}|\le\sqrt{qT}=q.$$
Every inequality is equality. In particular edge signs agree with the signing wherever the entries are nonzero.

Use the equality rigidity for normalized graph-supported DNN matrices from Hu–Liu–Wang, [Extremal graphs for a conjecture on the square energy of graphs](https://arxiv.org/abs/2608.17329), Proposition 4.3. This matrix theorem depends on the underlying graph, not the signing. Every block B is complete, and
$$M=\sum_B\alpha_B^2\mathbf 1_B\mathbf 1_B^\top,\qquad\alpha_B=(|B|-1)/|B|.$$
Thus X_ij=σ_ij α_B on an edge of B. If h has coordinate sum zero on each block, then h^T M h=0. Each folding summand is PSD, so for every nonedge ij,
$$X_{ij}^2(h_i-h_j)^2=0.$$

A zero-sum assignment on one block extends along the block-cut tree: at each new block assign the negative of the entry vertex's value to one new vertex and zero to the others. If the entry value is zero, its entire branch may be zero. This implies that if the block path joining nonadjacent i,j contains a clique of size at least three, one can choose h with h_i≠h_j. To see this, choose two path vertices a,b in that clique (the entrance and exit), prescribe h_a=0, h_b=1, and assign -1 to a third clique vertex. Extend along the side toward i with zeros; on the side toward j choose the successive path vertices to have negatives of their preceding values (and set the other new vertices to zero). This makes h_i=0 and h_j=±1. Therefore X_ij=0 for such nonedges.

### Bridge–clique interface

Suppose uv is a bridge and v belongs to a clique B of size at least three. Pick w in B other than v. Every z adjacent to u other than v forms a nonedge zw whose path contains B, so X_zw=0. Likewise for every z adjacent to w other than v, uz is a nonedge with a block path containing B, so X_uz=0. Using AX=XA at entry uw gives
$$\sigma_{uv}\sigma_{vw}\alpha_B=\sigma_{uv}\sigma_{vw}/2,$$
impossible because α_B>1/2. A connected block-cut tree containing both bridge and nontrivial clique blocks necessarily contains such an interface.

### Multiple nontrivial cliques without bridges

All nonedges now have X_ij=0 by the block-path argument. If two blocks B,C meet at v, choose u in B-v and w in C-v. Their only common neighbor is v, since any second common neighbor would place the cycle through them inside one block. The identity X²=AX at uw therefore gives
$$\sigma_{uv}\sigma_{vw}\alpha_B\alpha_C=\sigma_{uv}\sigma_{vw}\alpha_C,$$
which would force α_B=1, impossible.

### One block or a tree

Only a complete graph or a tree remains. For a complete graph the decomposition gives X_ii=α_B (nonnegative) and |X_ij|=α_B. Equality in Gram Cauchy–Schwarz forces all Gram vectors to be collinear. Hence X=α_B ss^T for a vector s with entries ±1, and σ_ij=s_i s_j, so the signing is balanced. Conversely a balanced complete graph switches to K_n, whose positive energy is (n-1)^2=q. Every signed tree switches to an ordinary tree, whose bipartite spectrum is symmetric and gives s^+=m=n-1. Negation proves the lower equality characterization.

## Limitations

This uses the published DNN equality theorem as an external dependency. No independent referee or proof assistant has checked the signed extension. Targeted repository searches for the source ID and author names found no overlapping solution; this is not an exhaustive originality search. The earlier chat reported a finite signed-graph sanity check; its underlying computation is not attached here and is not a proof premise.
