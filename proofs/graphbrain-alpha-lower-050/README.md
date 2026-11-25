# Graph Brain alpha lower-050 — Degree diversity and order-to-degree-sum ratio

24 November 2026 (US Central). AI-assisted mathematical counterexample. All graphs are finite, simple and connected. The original [lower-bound issue](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086) were checked, including the author-project definition of sigma_2 as the minimum degree sum over nonadjacent pairs. IDs are from the [corpus transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) label the corresponding entries HOLD_ARSENAL, which is not a proof or comprehensive priority search. Neither Davis's main index nor our existing index includes these entries. Targeted web searches returned no relevant results; current mathematical status and discovery priority are unconfirmed. Independent review and Lean verification remain pending.

## Statement
α ≥ min(dd,n/σ₂).

## Disproof
For any m≥5, take a clique K_m with distinguished vertex h, add a vertex x adjacent only to h and two new leaves p,q adjacent to x. The graph has n=m+3 vertices, degrees 1,3,m−1,m (four distinct values), and precisely two cut vertices h,x. The leaves are nonadjacent so sigma_2=2, since all degrees are at least one. Its independence number is exactly three: the original clique contributes at most one vertex and the three-vertex path p-x-q at most two; choosing p,q and any original clique vertex attains three. For m≥5, n/σ₂≥4, so the right side is four, contradicting α=3. The tested member uses m=10. ∎

[Joint witness verifier](../graphbrain-alpha-lower-041/verify.py). All ten witness checks passed in a local Python/NetworkX execution on 24 November 2026. The written counterexamples suffice independently of the finite checks.
