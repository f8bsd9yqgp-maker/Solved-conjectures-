# Spiro Conjecture 5.7 — polynomial relations with the normalized Laplacian

**Status:** AI-assisted analytical proof candidate, November 24–25, 2026. Independent review, publication priority and Lean verification outstanding.

Source: Sam Spiro, [Polynomial Relations Between Matrices of Graphs](https://arxiv.org/abs/1706.03298), Conjecture 5.7.

## Claim

For a finite connected simple graph, if A^r=f(ℒ) for a positive integer r and polynomial f, where A is the adjacency matrix and ℒ the normalized Laplacian, then the graph is regular or biregular. In fact for a connected graph with at least two vertices,
$$[A^r,\mathcal L]=0\quad\Longleftrightarrow\quad G\text{ is regular or biregular}.$$

## Proof

The singleton is regular. Otherwise x=D^{1/2}1 is strictly positive and spans the kernel of ℒ. Commutation implies A^r preserves that kernel, so A^r x=cx for some real c. In particular the hypothesized polynomial identity implies commutation. Squaring gives (A²)^r x=c²x. Since A² is real symmetric positive semidefinite, its eigenspaces are unchanged by taking a positive integer power: t↦t^r is injective on its nonnegative spectrum. Therefore x is an eigenvector of A². The [proof candidate for Conjecture 5.9](../spiro-matrix-relations-5-9/README.md) establishes regularity or biregularity.

Conversely in a d-regular graph with an edge, A=d(I-ℒ). In a biregular graph with degrees d_U,d_V, every edge has endpoint degree product d_U d_V, hence A=√(d_U d_V)(I-ℒ). Either identity implies commutation for all positive powers (and indeed the polynomial relation itself). This establishes the stronger equivalence.

## Limitations

The proof depends on the adjacent Conjecture 5.9 note, not on numerical evidence. No independent referee or proof-assistant certification; priority remains unverified.
