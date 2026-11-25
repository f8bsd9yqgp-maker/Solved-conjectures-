# Graph Brain alpha upper-008 — Order-to-minimum-degree exponential upper bound

24 November 2026 (US Central). AI-assisted counterexample note. Source: the Graph Brain Project's [open independence-number issue](https://github.com/math1um/objects-invariants-properties/issues/421), posted September 7, 2017; upper bounds are in [the accompanying comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086). The issue remains open. IDs below are the transcription identifiers from [the 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json), not original conjecture numbers. The original formula was checked against the issue or comment. Neither the user's existing index nor Davis's main index lists these entries; targeted public searches did not establish prior exact resolutions. The issue's age and open status do not guarantee that each statement was still mathematically unresolved. No first-discovery, independent-review, or Lean-verification claim is made. All graphs are finite, simple, and connected.

## Statement
α(G) ≤ ceil(e^(n/δ(G))).

## Disproof
Take K_{r,r} for r≥9. Its order is 2r, minimum degree r, and independence number r. The right side is ceil(e²)≤8, because e<11/4 and (11/4)²<8. For completeness, the series for e gives e≤1+1+1/2+(1/6)/(1−1/4)=49/18<11/4. Hence the asserted upper bound is at most eight, whereas α≥9. ∎

[Joint exact witness verifier](../graphbrain-alpha-lower-026/verify.py). All nine witness checks passed in the local Python/NetworkX execution on 24 November 2026. The infinite-family argument, not a numerical search alone, establishes the disproof.
