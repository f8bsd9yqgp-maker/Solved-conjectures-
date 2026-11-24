# Graffiti.pc Conjecture 379 — Maximum-degree components and degree diversity

24 November 2026. AI-assisted candidate resolution, not independently refereed or Lean-verified. Original problem numbers and statements are from E. DeLaViña's Written on the Wall II, as recorded in the [August 6, 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json). The current primary catalogue PDF could not be retrieved (HTTP 404); thus the current official status is not established. Targeted literature searches found no exact prior full resolution of these five entries, but priority is unverified. The current Davis completed index does not list any of them.

Source cross-check: [Graffiti.pc on the Total Domination Number of a Tree, Conjecture 1, p.11](https://math1um.github.io/Research/r05.pdf#page=11), page image inspected. It asks whether t=γ_t(T)≥r+dd(T)/3, where M is the maximum-degree set and r is the number of components of T[M].

Choose one representative from each component of T[M], forming an independent set R of size r. Let Δ be the maximum degree. The incident edge sets of these representatives are pairwise disjoint, hence Δr≤n−1. Total domination gives n≤Δt, so k=t−r≥1.

Let D be a minimum total dominating set, U=V∖D, and c the number of components of T[D]. Put u=|R∖D| and a=|D∖R|=k+u. Since R is independent and every component of T[D] contains an edge, c≤a.

Contract the D-components in the tree. For v∈U let a(v) count its D-neighbors and b(v) its U-neighbors. Every a(v)≥1. No two neighbors in D of any v can belong to the same D-component. If e_U is the number of U-edges, contracted-tree edge counting gives

Σ_{v∈U}(a(v)−1)+e_U=c−1.

For any independent subset A of U, Σ_{v∈A}b(v)≤e_U. Apply this to A=R∖D to obtain u(Δ−1)≤c−1≤k+u−1, so u(Δ−2)≤k−1.

Moreover every v outside D has degree at most c: in the contracted tree, each of its a(v) neighbors that is a D-component is distinct, and each of its b(v) outside neighbors has a D-component neighbor distinct from these and from those chosen for the other outside neighbors. Any repetition would form a cycle. Thus at most c distinct degrees occur outside D. Inside D there are at most a+1 distinct degrees (every member of R has degree Δ). Therefore dd(T)≤a+1+c≤2(k+u)+1.

If Δ≤3, dd≤3≤3k. If Δ≥4, then 2u≤k−1 by the preceding inequality, so dd≤2k+2u+1≤3k. This completes the proof in all cases. ∎

The cited paper proves the individual bounds t≥r+1 and t≥2dd/3, and states the stronger combined conjecture. The present argument proves that combined bound; it does not claim originality of either individual bound.

## Exact finite checks
[Joint verifier](../graffiti-pc-379/verify.py), run 24 November 2026: 985 trees of orders 3–12 for #362 and #379; 148 unique-degree-two-mode trees for #367; 456 connected diameter-at-most-two atlas graphs for #416; and 992 connected atlas graphs of order 4–7 for #423. All applicable checks passed. These are sanity checks, not substitutes for the written proofs.
