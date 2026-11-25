# Graph Brain alpha upper-041 — Girth, nonadjacent degree sum and periphery

24 November 2026 (US Central). AI-assisted counterexample note. Source: [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. IDs are from the [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Original formulas and author invariant definitions checked. SW is degeneracy plus one, sigma_2 is the minimum degree sum of a nonadjacent pair. The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report HOLD_ARSENAL or HOLD_TIGHT for these entries. Neither Davis's current main index nor this repository previously listed them. Targeted web searches did not identify exact earlier resolutions; this is not an exhaustive priority search. The open issue does not establish current mathematical status. No independent review or Lean verification. All graphs finite, simple, connected.

## Statement
α≤(girth^σ₂−|Per|)^2.

## Disproof
Take a triangle with seven new leaves all attached to one triangle vertex. All leaves and the two other triangle vertices have eccentricity two, while the hub has eccentricity one. Thus |Per|=9, girth=3 and σ₂=2 (two nonadjacent leaves). The claimed bound equals (9−9)^2=0. The seven leaves and one other triangle vertex form an independent set of size eight; no larger set exists. A single exact witness disproves the claim. ∎

[Joint verifier](../graphbrain-alpha-lower-017/verify.py), executed locally 24 November 2026: 10/10 passed. Eigenvalue count checked numerically but proof uses an exact negative eigenspace; theta values use exact sandwich bounds. The written arguments establish the disproofs independently of finite checks.
