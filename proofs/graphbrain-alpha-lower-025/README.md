# Graph Brain alpha lower-025 — Order and inverse hyperbolic sine lower bound

24 November 2026 (US Central). AI-assisted written disproof. Source: [Graph Brain open alpha conjectures](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted September 7, 2017. ID is the transcription identifier from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The original statement and [author invariant implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage) were checked. In particular sigma_2 is the minimum degree sum of a nonadjacent pair, NOT the second-smallest degree, and SW is degeneracy plus one. The prior [lower-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) mark this entry HOLD_ARSENAL (no counterexample in their tested families, not a proof). No earlier exact resolution was identified in targeted searches; the old issue's open status does not establish current mathematical status or discovery priority. Not independently refereed or Lean-verified. All graphs are finite, simple and connected.

## Statement
α≥ceil(asinh(n−σ₂)).

## Disproof
Take K_m with two private pendants attached to one clique vertex, m≥12. As in lower-016, α=3 and σ₂=2, while n=m+2. Therefore n−σ₂=m. The exponential series gives e<11/4, so sinh(3)<e³/2<(11/4)³/2<12≤m. Since sinh is strictly increasing, asinh(m)>3 and the ceiling is at least four, violating the conjecture. At m=12, asinh(12) is between three and four (for example sinh(4)>12 follows from its positive series terms 4+4³/6+4⁵/120). ∎

[Joint witness verifier](../graphbrain-alpha-lower-016/verify.py): all ten witness tests passed in Python/NetworkX on 24 November 2026. Infinite-family proofs are independent of finite testing.
