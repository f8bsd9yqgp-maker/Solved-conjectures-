# Graffiti.pc Conjecture 423 — Independent domination and minimum-degree neighborhoods

24 November 2026. AI-assisted candidate resolution, not independently refereed or Lean-verified. Original problem numbers and statements are from E. DeLaViña's Written on the Wall II, as recorded in the [August 6, 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json). The current primary catalogue PDF could not be retrieved (HTTP 404); thus the current official status is not established. Targeted literature searches found no exact prior full resolution of these five entries, but priority is unverified. The current Davis completed index does not list any of them.

Let G be a finite simple connected graph on n>3 vertices. Let A be the set of minimum-degree vertices and M the set of maximum-degree vertices. Let i(G) denote the minimum size of a maximal independent set. The conjecture is i(G)≤|E(G[M])|+α(G[N[A]])α(G[V∖A]), where N[A] is the closed neighborhood of A.

If A=V, G is regular and M=V. Connectedness gives |E(G[M])|≥n−1≥i(G), proving the claim.

Otherwise put a=α(G[N[A]]) and b=α(G[V∖A]), both positive. If a,b≥2, every independent set has at most a members in A and b in V∖A; hence i(G)≤α(G)≤a+b≤ab.

If a=1, the induced graph on N[A] is complete. Connectedness gives a vertex w∈N(A)∖A. It is adjacent to every vertex of A. Extend {w} greedily to a maximal independent set. This set lies entirely in V∖A, so it has size at most b=ab.

If b=1, the induced graph on V∖A is complete. Choose w∈N(A)∖A as above and extend {w} to a maximal independent set. Since w is adjacent to all other vertices outside A, every other member lies in A. Hence the resulting set is contained in N[A] and has size at most a=ab.

This proves the conjecture and the stronger inequality i(G)≤ab for every proper nonempty A, regardless of degree assumptions, in a connected graph. ∎

## Exact finite checks
[Joint verifier](../graffiti-pc-379/verify.py), run 24 November 2026: 985 trees of orders 3–12 for #362 and #379; 148 unique-degree-two-mode trees for #367; 456 connected diameter-at-most-two atlas graphs for #416; and 992 connected atlas graphs of order 4–7 for #423. All applicable checks passed. These are sanity checks, not substitutes for the written proofs.
