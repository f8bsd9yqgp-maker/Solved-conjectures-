# Graph Brain alpha upper-076 — Diameter and degree sum

24 November 2026 (US Central). AI-assisted mathematical counterexample. All graphs are finite, simple and connected. The original [lower-bound issue](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086) were checked, including the author-project definition of sigma_2 as the minimum degree sum over nonadjacent pairs. IDs are from the [corpus transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) label the corresponding entries HOLD_ARSENAL, which is not a proof or comprehensive priority search. Neither Davis's main index nor our existing index includes these entries. Targeted web searches returned no relevant results; current mathematical status and discovery priority are unconfirmed. Independent review and Lean verification remain pending.

## Statement
α ≤ |10^diam−sum of degrees|.

## Disproof
Take K_{5,10}. Its diameter is two and its edge count is fifty, hence the degree sum is one hundred. The right side is |100−100|=0. Its independence number is exactly ten, since any independent set is confined to one part, and the larger part has ten vertices. This single exact witness suffices to disprove the universal claim. No infinite family is asserted here. ∎

[Joint witness verifier](../graphbrain-alpha-lower-041/verify.py). All ten witness checks passed in a local Python/NetworkX execution on 24 November 2026. The written counterexamples suffice independently of the finite checks.
