# Graph Brain alpha upper-038 — Maximum degree, minimum degree and density

24 November 2026 (US Central). AI-assisted mathematical counterexample. All graphs are finite, simple and connected. The original [lower-bound issue](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086) were checked, including the author-project definition of sigma_2 as the minimum degree sum over nonadjacent pairs. IDs are from the [corpus transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) label the corresponding entries HOLD_ARSENAL, which is not a proof or comprehensive priority search. Neither Davis's main index nor our existing index includes these entries. Targeted web searches returned no relevant results; current mathematical status and discovery priority are unconfirmed. Independent review and Lean verification remain pending.

## Statement
α ≤ max(Δ,e^δ/density).

## Disproof
For m≥20 take K_m and attach two private leaves to every original vertex. There are 3m vertices, m(m−1)/2+2m edges, minimum degree one and maximum degree m+1. All 2m leaves are independent. Density=(m+3)/(3(3m−1))>1/9. Since e<11/4, e/density<99/4<25. The maximum degree m+1 is also strictly smaller than 2m. Thus the asserted upper bound is smaller than the exhibited independent set for every m≥20. At m=20, density=23/177, and e/density<1947/92<22, while Δ=21 and α≥40. The exponential-series estimate e<11/4 follows by summing through 1/2! and bounding the remaining terms by a geometric series of ratio 1/4. ∎

[Joint witness verifier](../graphbrain-alpha-lower-041/verify.py). All ten witness checks passed in a local Python/NetworkX execution on 24 November 2026. The written counterexamples suffice independently of the finite checks.
