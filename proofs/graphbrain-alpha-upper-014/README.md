# Graph Brain alpha upper-014 — Even-distance invariant and matching

24 November 2026 US Central. AI-assisted candidate disproof. Original statement from [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and its upper-bound comment, ID from [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions from the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage), including SW=degeneracy+1 and M=max(0,max_v(|Even(v)|-|E(G[Even(v)])|)). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report holds for these entries in tested families. Original author's issue titles and targeted public searches were screened; no exact prior resolution was identified for this entry, but current status and discovery priority remain unconfirmed. No independent review or Lean certification. All graphs finite simple connected.

## Original statement
`independence_number(x) <= max_even_minus_even_horizontal(x)^2 + matching_number(x)`

## Counterexample
Take one universal hub, 80 singleton leaves, and two disjoint K16 cliques, with no edges between the blocks except via the hub. The leaves and one vertex from each clique form an independent set of size 82. Matching number 17: at most one hub edge and eight internal edges per K16, attained by matching the hub to a leaf and each clique perfectly. For the hub the even-distance set is just itself, with score one. For a leaf it is all 112 nonhub vertices, inducing 240 edges. For a block vertex it consists of itself, eighty leaves and the other K16, inducing 120 edges on 97 vertices. Thus M=1. The claimed upper bound is 1^2+17=18<82. ∎

[Joint witness verifier](../graphbrain-alpha-lower-018/verify.py). Local graph and arithmetic checks passed; analytic reasoning supplies theta and large-family quantities.
