# Graph Brain alpha lower-031 — Triangle and pendant lower bound

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≥ min(10^(number of triangles), |P|+1).

## Disproof
For any m≥3 start with K_m and attach exactly one private pendant to each vertex. The m disjoint support-pendant edges partition the vertices, so an independent set contains at most m vertices; choosing all pendants attains α=m. There are m pendants and C(m,3) triangles, all in the original clique. For m=3, 10^1≥4; for m≥4, C(m,3)≥m, so 10^C(m,3)≥m+1. The asserted right side is therefore m+1, strictly larger than α=m. At m=3 the six-vertex example gives 3<4. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
