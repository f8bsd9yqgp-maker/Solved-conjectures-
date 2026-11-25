# Graph Brain alpha lower-016 — Maximum degree and nonadjacent degree sum

24 November 2026 (US Central). AI-assisted written disproof. Source: [Graph Brain open alpha conjectures](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted September 7, 2017. ID is the transcription identifier from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The original statement and [author invariant implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage) were checked. In particular sigma_2 is the minimum degree sum of a nonadjacent pair, NOT the second-smallest degree, and SW is degeneracy plus one. The prior [lower-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) mark this entry HOLD_ARSENAL (no counterexample in their tested families, not a proof). No earlier exact resolution was identified in targeted searches; the old issue's open status does not establish current mathematical status or discovery priority. Not independently refereed or Lean-verified. All graphs are finite, simple and connected.

## Statement
α≥Δ−σ₂−1.

## Disproof
Take K_m with two pendant vertices adjacent to the same clique vertex, m≥6. The pendants are independent and together with any other clique vertex give α=3; no independent set can take more than one clique vertex or more than the two pendants. The maximum degree is m+1, while σ₂=2 because the two pendants are nonadjacent and all degrees are positive. The claimed lower bound is m−2>3. At m=6 the exact witness is α=3<4. ∎

[Joint witness verifier](../graphbrain-alpha-lower-016/verify.py): all ten witness tests passed in Python/NetworkX on 24 November 2026. Infinite-family proofs are independent of finite testing.
