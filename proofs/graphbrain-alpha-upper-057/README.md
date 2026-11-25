# Graph Brain alpha upper-057 — Periphery, common neighbors and radius

24 November 2026 US Central. AI-assisted candidate disproof. Original statement from [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and its upper-bound comment, ID from [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions from the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage), including SW=degeneracy+1 and M=max(0,max_v(|Even(v)|-|E(G[Even(v)])|)). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report holds for these entries in tested families. Original author's issue titles and targeted public searches were screened; no exact prior resolution was identified for this entry, but current status and discovery priority remain unconfirmed. No independent review or Lean certification. All graphs finite simple connected.

## Original statement
`independence_number(x) <= maximum(card_periphery(x), max_common_neighbors(x))^radius(x)`

## Counterexample
Take twelve K5 cliques sharing a single common hub, and attach two internally disjoint two-edge pendant paths at that hub. Diameter four is attained only between the two terminal leaves, and hub eccentricity two proves radius two. The periphery has size two. The maximum common-neighbor count is three: two nonhub vertices of the same block or the hub and a block nonhub have exactly three common neighbors; other pairs have at most one. Choose one nonhub in each block and both terminal leaves, an independent set of size fourteen. The asserted upper bound is max(2,3)^2=9<14. ∎

[Joint witness verifier](../graphbrain-alpha-lower-018/verify.py). Local graph and arithmetic checks passed; analytic reasoning supplies theta and large-family quantities.
