# Graph Brain alpha upper-120 — Theta over square root of order

24 November 2026 (US Central). AI-assisted candidate disproof, not independently refereed or Lean-verified. Original [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. Identifiers follow the [corpus transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions checked against the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage). In particular SW=degeneracy+1, sigma_2=min degree sum over nonadjacent pairs, M=max(0, max_v(|Even(v)|−|E(G[Even(v)])|)), with distance zero included. All graphs finite, simple, connected. Prior [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) record these entries as HOLD_ARSENAL or HOLD_TIGHT. All seven pages of author-project issue titles were screened; no exact earlier closed resolution of the selected 30 was identified there. Targeted public literature search was not exhaustive; issue #421's open status is not proof of present mathematical status or novelty. Davis's main index does not list these entries. No discovery-priority claim.

## Statement
alpha ≤ floor(10^(theta/sqrt(n))).

## Disproof
Take K_n minus one edge, n≥100. Alpha=2, and the graph can be covered by two cliques, so Lovasz's sandwich gives theta=2 exactly. Thus theta/sqrt(n)≤1/5 and 10^(1/5)<2 since 10<2^5. RHS is at most one, contrary to alpha=2. At n=100 this is an exact witness.

[Joint exact witness verifier](../graphbrain-alpha-upper-001/verify.py). Local Python/NetworkX execution (24 November 2026 US Central) completed 30/30 checks, including rational analytic comparisons. A strict witness suffices; the numerical tests are not independent refereeing.
