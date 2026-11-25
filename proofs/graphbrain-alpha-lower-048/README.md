# Graph Brain alpha lower-048 — Matching, girth and periphery exponential

24 November 2026 (US Central). AI-assisted counterexample note. Source: [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. IDs are from the [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Original formulas and author invariant definitions checked. SW is degeneracy plus one, sigma_2 is the minimum degree sum of a nonadjacent pair. The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report HOLD_ARSENAL or HOLD_TIGHT for these entries. Neither Davis's current main index nor this repository previously listed them. Targeted web searches did not identify exact earlier resolutions; this is not an exhaustive priority search. The open issue does not establish current mathematical status. No independent review or Lean verification. All graphs finite, simple, connected.

## Statement
α≥μ−girth^|Per|.

## Disproof
Let B(r,k) consist of r disjoint K_k cliques, each with one distinguished hub, and join consecutive hubs by one bridge. Let A(r,k) be B(r,k) with an extra two-edge pendant path at each end hub. Then α(B)=r and α(A)=r+2: partition into the r cliques and (when present) two additional edges, and choose one nonhub in each clique and the two terminal leaves. For even k, perfect matchings within each clique and the additional edges give μ(B)=rk/2 and μ(A)=rk/2+2. For r≥3 the two terminal leaves of A are exactly its periphery, since their distance r+3 exceeds every other pair distance. Girth is three for k≥3.
Use A(r,4) with r≥10. The claimed lower bound is 2r+2−9=2r−7>r+2=α. For r=10 the bound is thirteen, while α=12. ∎

[Joint verifier](../graphbrain-alpha-lower-017/verify.py), executed locally 24 November 2026: 10/10 passed. Eigenvalue count checked numerically but proof uses an exact negative eigenspace; theta values use exact sandwich bounds. The written arguments establish the disproofs independently of finite checks.
