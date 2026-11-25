# Graph Brain alpha lower-020 — Theta minus center size

24 November 2026 (US Central). AI-assisted candidate disproof, not independently refereed or Lean-verified. Original [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. Identifiers follow the [corpus transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions checked against the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage). In particular SW=degeneracy+1, sigma_2=min degree sum over nonadjacent pairs, M=max(0, max_v(|Even(v)|−|E(G[Even(v)])|)), with distance zero included. All graphs finite, simple, connected. Prior [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) record these entries as HOLD_ARSENAL or HOLD_TIGHT. All seven pages of author-project issue titles were screened; no exact earlier closed resolution of the selected 30 was identified there. Targeted public literature search was not exhaustive; issue #421's open status is not proof of present mathematical status or novelty. Davis's main index does not list these entries. No discovery-priority claim.

## Statement
alpha ≥ floor(theta)−|C|.

## Disproof
Take r disjoint copies of C5 and join a new universal vertex to all their vertices. The independence number is 2r, the center is the universal vertex alone, the periphery is the 5r cycle vertices, and the Welsh-Powell invariant is four (all cycle vertices have degree three, and only the universal vertex has higher degree).

Use the SDP definition theta(G)=max sum_ij X_ij, X positive semidefinite, trace one, X_ij=0 for edges. On C5 set X=(I+(3/5)A(complement C5))/5. The complement cycle has smallest adjacency eigenvalue −(1+sqrt(5))/2>−5/3, so X is positive definite. Its trace is one and its entry sum is 11/5. For r disjoint copies, the block matrix J_r tensor X divided by r is PSD, has trace one, zeros on all edges, and entry sum 11r/5. Extending with a zero row and column for the universal hub remains feasible. Thus theta≥11r/5 exactly. At r=30, alpha=60 and theta≥66.
At r=30, RHS≥66−1=65>60.

[Joint exact witness verifier](../graphbrain-alpha-upper-001/verify.py). Local Python/NetworkX execution (24 November 2026 US Central) completed 30/30 checks, including rational analytic comparisons. A strict witness suffices; the numerical tests are not independent refereeing.
