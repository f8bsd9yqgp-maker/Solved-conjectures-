# Graph Brain alpha lower-042 — Matching number minus exponential degree bound

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≥ μ(G)−10^δ(G).

## Disproof
Take r≥12 disjoint copies of K4, join consecutive copies by bridges, using distinct bridge endpoints in each interior clique, and attach a single pendant to a nonbridge vertex of the first clique. The resulting graph has 4r+1 vertices and δ=1. Each clique contributes at most one independent vertex, so α≤r+1; choosing the pendant and one nonbridge vertex distinct from its support in each clique attains equality. The perfect matchings of the cliques yield μ≥2r, and the order bound μ≤floor((4r+1)/2)=2r gives equality. The conjectured lower bound is 2r−10, strictly greater than r+1 for r≥12. For r=12, α=13 and the right side is 14. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
