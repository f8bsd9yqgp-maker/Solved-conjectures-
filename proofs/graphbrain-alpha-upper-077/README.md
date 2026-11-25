# Graph Brain alpha upper-077 — Radius power and even-distance bound

24 November 2026 (US Central). AI-assisted candidate disproof, not independently refereed or Lean-verified. Original [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017. Identifiers follow the [corpus transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions checked against the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage). In particular SW=degeneracy+1, sigma_2=min degree sum over nonadjacent pairs, M=max(0, max_v(|Even(v)|−|E(G[Even(v)])|)), with distance zero included. All graphs finite, simple, connected. Prior [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) record these entries as HOLD_ARSENAL or HOLD_TIGHT. All seven pages of author-project issue titles were screened; no exact earlier closed resolution of the selected 30 was identified there. Targeted public literature search was not exhaustive; issue #421's open status is not proof of present mathematical status or novelty. Davis's main index does not list these entries. No discovery-priority claim.

## Statement
alpha ≤ max(2M,rad^n).

## Disproof
Take r≥4 disjoint K5s and a new universal hub h. The clique partition gives alpha=r, realized by one vertex per clique. Radius is one, vertex connectivity is one, and minimum common-neighbor count is one (attained by vertices of different cliques, with h the common neighbor; all pairs have a common neighbor). Rooting at h gives even set {h}, of value one; rooting at another vertex gives that vertex plus all r−1 other cliques, of value 1−5(r−1)≤0. Thus M=1.
RHS=max(2,1)=2<r.

[Joint exact witness verifier](../graphbrain-alpha-upper-001/verify.py). Local Python/NetworkX execution (24 November 2026 US Central) completed 30/30 checks, including rational analytic comparisons. A strict witness suffices; the numerical tests are not independent refereeing.
