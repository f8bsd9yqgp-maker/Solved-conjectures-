# Graph Brain alpha upper-061 — Average and maximum degree exponential upper bound

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≤ max(e^(average degree), Δ(G)^2).

## Disproof
Take the path P_n for n≥15. Its independence number is ceil(n/2)≥8, by selecting alternating vertices and partitioning the path into consecutive pairs and a possible singleton. The average degree is 2(n−1)/n<2 and maximum degree is two. Using e<11/4 (from the exponential series, as shown in the upper-008 note), e^(average degree)<e²<8, while Δ²=4. Therefore the right side is strictly below eight. The 16-vertex witness has α=8 and the right side below eight. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
