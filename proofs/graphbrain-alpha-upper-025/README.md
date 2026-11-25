# Graph Brain alpha upper-025 — Diameter-squared and maximum-degree upper bound

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≤ 2 diam(G)^2 + Δ(G).

## Disproof
Take the complete rooted binary tree of depth h≥10, where depth counts edges. The 2^h leaves form an independent set, the diameter is 2h, and maximum degree is three. The proposed upper bound is 8h²+3. At h=10, 2^h=1024>803. For h≥10, 2(8h²+3)−(8(h+1)²+3)=8h²−16h−5>0, so doubling and induction show 2^h>8h²+3 for every h≥10. An independent-set lower witness is sufficient; computing the exact independence number is unnecessary. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
