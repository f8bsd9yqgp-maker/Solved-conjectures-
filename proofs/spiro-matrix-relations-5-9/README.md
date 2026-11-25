# Spiro Conjecture 5.9 — adjacency-square eigenvector rigidity

**Status:** AI-assisted analytical proof candidate, November 24–25, 2026. Independent review, publication priority and Lean verification outstanding.

Source: Sam Spiro, [Polynomial Relations Between Matrices of Graphs](https://arxiv.org/abs/1706.03298), Conjecture 5.9.

**Claim.** If G is a finite connected simple graph, A its adjacency matrix and D its diagonal degree matrix, and x=D^{1/2}1 is an eigenvector of A², then G is regular or bipartite biregular. This also resolves [Conjecture 5.7](../spiro-matrix-relations-5-7/README.md).

## Proof

The singleton is regular, so assume at least two vertices, making x strictly positive. Suppose A²x=λx.

If G is nonbipartite, A² is irreducible: even walks connect any two vertices of a connected nonbipartite graph (insert an odd closed walk to change parity when needed). Since Ax is strictly positive and A²(Ax)=λAx, Perron–Frobenius uniqueness gives Ax=cx with c>0. Write δ and Δ for minimum and maximum degree. Evaluating at a maximum-degree vertex gives c≥√(Δδ); at a minimum-degree vertex gives c≤√(Δδ). Equality forces every maximum-degree vertex to have exclusively minimum-degree neighbors and conversely. If δ≠Δ, these two nonempty degree classes have no edges leaving their union and no edges within either class. Connectedness makes G bipartite, a contradiction. Thus G is regular.

If G is bipartite with classes U,V, write
$$A=\begin{pmatrix}0&B\\B^\top&0\end{pmatrix},\qquad A^2=\begin{pmatrix}BB^\top&0\\0&B^\top B\end{pmatrix}.$$
Connectedness implies each diagonal block is irreducible (even walks connect any two vertices in the same class). The vectors x_U and Bx_V are strictly positive eigenvectors of BB^T with eigenvalue λ, and x_V and B^T x_U are strictly positive eigenvectors of B^T B with eigenvalue λ. Thus
$$Bx_V=ax_U,\qquad B^\top x_U=bx_V$$
for positive scalars a,b.

Let δ_U,Δ_U,δ_V,Δ_V be the extrema of degrees on the two classes. Evaluating the first equation at the maximum and minimum degree vertices in U yields
$$\sqrt{\Delta_U\delta_V}\le a\le\sqrt{\delta_U\Delta_V}.$$
The second gives
$$\sqrt{\Delta_V\delta_U}\le b\le\sqrt{\delta_V\Delta_U}.$$
Consequently Δ_U/δ_U=Δ_V/δ_V and both intervals collapse. All maximum-degree vertices in U have neighbors only among minimum-degree vertices in V; all minimum-degree vertices in V have neighbors only among maximum-degree vertices in U. Their union is nonempty and closed under adjacency. Connectedness implies it equals the whole vertex set, so each class has constant degree. This is biregularity, proving the conjecture.

Conversely for regular or biregular connected graphs the vector x is an eigenvector of A, hence of A² (the singleton has x=0, so the converse eigenvector assertion is restricted to graphs with an edge).

## Limitations

No computational premise. Targeted repository searches found no matching entry. Worldwide originality and independent review remain unconfirmed.
