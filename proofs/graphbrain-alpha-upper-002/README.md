# Graph Brain alpha upper-002 — Average-distance exponential upper bound

**Priority correction (24 November 2026):** the author project already documented this exact formula as false in [closed issue #226](https://github.com/math1um/objects-invariants-properties/issues/226). This is an independently constructed counterexample to a previously disproved conjecture, not an original resolution. The original negative priority search below was incomplete.

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≤ floor(10^sqrt(average distance)).

## Disproof
Take the star K_{1,r} with r≥32. Its independence number is r. Among unordered vertex pairs, r pairs have distance one and C(r,2) have distance two. Their average is 2r/(r+1)<2. Hence 10^sqrt(average distance)<10^(3/2)=sqrt(1000)<32, since 1000<32². The floor is at most 31, strictly smaller than r. This also works if the average includes distance-zero pairs, since that only decreases it. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
