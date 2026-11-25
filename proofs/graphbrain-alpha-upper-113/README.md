# Graph Brain alpha upper-113 — Density and mean distance

24 November 2026 US Central. AI-assisted candidate disproof. Original statement from [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and its upper-bound comment, ID from [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions from the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage), including SW=degeneracy+1 and M=max(0,max_v(|Even(v)|-|E(G[Even(v)])|)). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report holds for these entries in tested families. Original author's issue titles and targeted public searches were screened; no exact prior resolution was identified for this entry, but current status and discovery priority remain unconfirmed. No independent review or Lean certification. All graphs finite simple connected.

## Original statement
`independence_number(x) <= maximum(max_degree(x), density(x)^(-average_distance(x)))`

## Counterexample
Start with K400 and attach two private leaves to each original vertex. All 800 leaves are independent, maximum degree 401, diameter 3, and density=(400+3)/(3*(3*400-1))>1/9 (order 1200 and size 400*399/2+800). Average distance is at most 3. Hence density^(-average_distance)<9^3=729. Both terms in the claimed maximum are below 800. ∎

[Joint witness verifier](../graphbrain-alpha-lower-018/verify.py). Local graph and arithmetic checks passed; analytic reasoning supplies theta and large-family quantities.
