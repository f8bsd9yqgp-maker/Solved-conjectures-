# Graph Brain alpha lower-026 — Matching and minimum-degree lower bound

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≥ (μ(G)−δ(G))/2.

## Disproof
Take r≥4 disjoint copies of K8, joined in a chain by one bridge between each consecutive pair; use distinct bridge endpoints within each interior clique. Every independent set contains at most one vertex from each clique, and selecting a nonbridge vertex per clique attains α=r. Each clique admits a perfect matching, giving μ=4r, and the minimum degree is δ=7. The asserted lower bound is (4r−7)/2=2r−7/2, strictly larger than r for r≥4. At r=4, α=4 and the right side is 9/2. Thus the conjecture is false for infinitely many connected graphs. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
