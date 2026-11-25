# Graph Brain alpha upper-046 — Minimum degree minus vertex connectivity

24 November 2026 (US Central). AI-assisted mathematical counterexample. All graphs are finite, simple and connected. The original [lower-bound issue](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086) were checked, including the author-project definition of sigma_2 as the minimum degree sum over nonadjacent pairs. IDs are from the [corpus transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) label the corresponding entries HOLD_ARSENAL, which is not a proof or comprehensive priority search. Neither Davis's main index nor our existing index includes these entries. Targeted web searches returned no relevant results; current mathematical status and discovery priority are unconfirmed. Independent review and Lean verification remain pending.

## Statement
α ≤ ceil(n/(δ−κ)).

## Disproof
For m≥4 join two disjoint copies of K_{m,m} by a single bridge between selected vertices. Its order is 4m, minimum degree is m, and vertex connectivity is one because a bridge endpoint is a cut vertex. In particular the denominator is positive. Choosing the part opposite the bridge endpoint in each copy gives an independent set of size 2m. The asserted bound is ceil(4m/(m−1))≤6 for m≥4, strictly less than 2m≥8. At m=4 the right side is six. ∎

[Joint witness verifier](../graphbrain-alpha-lower-041/verify.py). All ten witness checks passed in a local Python/NetworkX execution on 24 November 2026. The written counterexamples suffice independently of the finite checks.
