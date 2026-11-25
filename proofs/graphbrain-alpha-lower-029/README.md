# Graph Brain alpha lower-029 — Degree diversity and degeneracy

24 November 2026 (US Central). AI-assisted counterexample note. Source: [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. IDs are from the [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Original formulas and author invariant definitions checked. SW is degeneracy plus one, sigma_2 is the minimum degree sum of a nonadjacent pair. The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report HOLD_ARSENAL or HOLD_TIGHT for these entries. Neither Davis's current main index nor this repository previously listed them. Targeted web searches did not identify exact earlier resolutions; this is not an exhaustive priority search. The open issue does not establish current mathematical status. No independent review or Lean verification. All graphs finite, simple, connected.

## Statement
α≥2dd−2SW.

## Disproof
Take a clique c_1,...,c_k and an independent set i_1,...,i_k, with i_j adjacent to c_1,...,c_j, k≥5. The independent vertices have degrees 1,...,k and clique vertices degrees 2k−1,...,k, so dd=2k−1. The clique together with i_k has order k+1, and all other independent vertices have degree ≤k, so degeneracy equals k and SW=k+1. The independent set of size k attains α=k: choosing c_j permits at most j−1 independent vertices and no other clique vertex. The proposed bound is 2k−4>k. At k=5, α=5<6. ∎

[Joint verifier](../graphbrain-alpha-lower-017/verify.py), executed locally 24 November 2026: 10/10 passed. Eigenvalue count checked numerically but proof uses an exact negative eigenspace; theta values use exact sandwich bounds. The written arguments establish the disproofs independently of finite checks.
