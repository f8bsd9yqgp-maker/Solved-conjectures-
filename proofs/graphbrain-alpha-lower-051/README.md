# Graph Brain alpha lower-051 — Matching, center size and girth

24 November 2026 (US Central). AI-assisted written disproof. Source: [Graph Brain open alpha conjectures](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted September 7, 2017. ID is the transcription identifier from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The original statement and [author invariant implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage) were checked. In particular sigma_2 is the minimum degree sum of a nonadjacent pair, NOT the second-smallest degree, and SW is degeneracy plus one. The prior [lower-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) mark this entry HOLD_ARSENAL (no counterexample in their tested families, not a proof). No earlier exact resolution was identified in targeted searches; the old issue's open status does not establish current mathematical status or discovery priority. Not independently refereed or Lean-verified. All graphs are finite, simple and connected.

## Statement
α≥μ−2|C|−girth.

## Disproof
Use the hub-chain of r K4 cliques from lower-049 with odd r≥7. Then α=r, μ=2r, and girth=3. The unique center is the middle clique's hub: if the hubs are numbered 1,...,r, hub j has eccentricity 1+max(j−1,r−j); a nonhub in that clique has eccentricity one greater, as r≥3 and it must reach a different end clique. Consequently |C|=1. The right side is 2r−5>r. At r=7, α=7 and the conjectured bound is nine. ∎

[Joint witness verifier](../graphbrain-alpha-lower-016/verify.py): all ten witness tests passed in Python/NetworkX on 24 November 2026. Infinite-family proofs are independent of finite testing.
