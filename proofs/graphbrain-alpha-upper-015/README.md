# Graph Brain alpha upper-015 — Exponential degree-sum and periphery upper bound

24 November 2026 (US Central). AI-assisted written disproof. Source: [Graph Brain open alpha conjectures](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted September 7, 2017. ID is the transcription identifier from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The original statement and [author invariant implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage) were checked. In particular sigma_2 is the minimum degree sum of a nonadjacent pair, NOT the second-smallest degree, and SW is degeneracy plus one. The prior [lower-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper-bound sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) mark this entry HOLD_ARSENAL (no counterexample in their tested families, not a proof). No earlier exact resolution was identified in targeted searches; the old issue's open status does not establish current mathematical status or discovery priority. Not independently refereed or Lean-verified. All graphs are finite, simple and connected.

## Statement
α≤10^σ₂−|Per(G)|.

## Disproof
Use K_{1,r} with r≥51. All r leaves are independent and the hub is universal, so α=r. All leaves have eccentricity two, the hub has eccentricity one, and any two leaves are nonadjacent with degree sum two, hence |Per|=r and σ₂=2. The right side is 100−r<r. The first stated witness is α=51>49. ∎

[Joint witness verifier](../graphbrain-alpha-lower-016/verify.py): all ten witness tests passed in Python/NetworkX on 24 November 2026. Infinite-family proofs are independent of finite testing.
