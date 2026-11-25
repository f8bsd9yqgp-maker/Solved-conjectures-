# Graph Brain alpha upper-078 — Girth, order and radius

24 November 2026 (US Central). AI-assisted counterexample note. Source: [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. IDs are from the [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Original formulas and author invariant definitions checked. SW is degeneracy plus one, sigma_2 is the minimum degree sum of a nonadjacent pair. The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report HOLD_ARSENAL or HOLD_TIGHT for these entries. Neither Davis's current main index nor this repository previously listed them. Targeted web searches did not identify exact earlier resolutions; this is not an exhaustive priority search. The open issue does not establish current mathematical status. No independent review or Lean verification. All graphs finite, simple, connected.

## Statement
α≤girth·n/(rad−1).

## Disproof
Take a triangle and attach a pendant path of length k≥15 at one vertex. Order k+3, girth three, diameter k+1 and radius ceil((k+1)/2)≥8 (eccentricities on the arm are max(j+1,k−j), and other triangle vertices have eccentricity k+1). Alternate arm vertices starting with the first and add one nonhub triangle vertex to obtain an independent set of size 1+ceil(k/2). The claimed bound is ≤3(k+3)/7 < (k+2)/2≤1+ceil(k/2), since k>4. At k=15, the witness is nine and the bound is 54/7. ∎

[Joint verifier](../graphbrain-alpha-lower-017/verify.py), executed locally 24 November 2026: 10/10 passed. Eigenvalue count checked numerically but proof uses an exact negative eigenspace; theta values use exact sandwich bounds. The written arguments establish the disproofs independently of finite checks.
