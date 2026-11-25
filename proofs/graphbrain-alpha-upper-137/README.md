# Graph Brain alpha upper-137 — Lovasz theta product and minimum degree

24 November 2026 (US Central). AI-assisted counterexample note. Source: [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. IDs are from the [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Original formulas and author invariant definitions checked. SW is degeneracy plus one, sigma_2 is the minimum degree sum of a nonadjacent pair. The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report HOLD_ARSENAL or HOLD_TIGHT for these entries. Neither Davis's current main index nor this repository previously listed them. Targeted web searches did not identify exact earlier resolutions; this is not an exhaustive priority search. The open issue does not establish current mathematical status. No independent review or Lean verification. All graphs finite, simple, connected.

## Statement
α≤θ(G)θ(complement G)/ceil(sqrt δ).

## Disproof
Take K_{m,m}, m≥5. Its independence number is m and its minimum degree m. The Lovász sandwich α(G)≤θ(G)≤χ(complement G) gives θ(G)=m, as the complement consists of two disjoint m-cliques. For the complement F, α(F)=2 and χ(G)=2 give θ(F)=2. Thus the product is exactly 2m, without relying on a numerical SDP. Since ceil(sqrt m)≥3, the proposed bound is ≤2m/3<m. At m=5, α=5 and the claimed bound is 10/3. ∎

[Joint verifier](../graphbrain-alpha-lower-017/verify.py), executed locally 24 November 2026: 10/10 passed. Eigenvalue count checked numerically but proof uses an exact negative eigenspace; theta values use exact sandwich bounds. The written arguments establish the disproofs independently of finite checks.
