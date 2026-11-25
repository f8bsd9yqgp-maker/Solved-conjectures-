# Graph Brain alpha lower-028 — Girth, maximum degree and Szekeres–Wilf lower bound

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≥ min(girth(G), Δ(G)−SW(G)).

## Disproof
For any k≥4 take two disjoint copies of K_k and add one new vertex adjacent to all 2k original vertices. The resulting graph is connected, has girth three, maximum degree 2k, and independence number two: one vertex from each original clique can be chosen, while the new vertex is universal. The degeneracy is k because each original vertex has degree k and no induced subgraph without the universal vertex has minimum degree greater than k; the same upper bound holds for any subgraph containing an original vertex. Thus SW=k under the source convention of maximum minimum degree over subgraphs. Even under the alternate convention SW=k+1, the difference 2k−SW≥3. In either convention the right side is three, contradicting α=2. The k=4 graph has nine vertices. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
