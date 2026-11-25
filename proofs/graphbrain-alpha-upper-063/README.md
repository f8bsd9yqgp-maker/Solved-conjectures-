# Graph Brain alpha upper-063 — Parity, maximum degree and periphery

24 November 2026 US Central. AI-assisted candidate disproof. Original statement from [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and its upper-bound comment, ID from [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions from the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage), including SW=degeneracy+1 and M=max(0,max_v(|Even(v)|-|E(G[Even(v)])|)). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report holds for these entries in tested families. Original author's issue titles and targeted public searches were screened; no exact prior resolution was identified for this entry, but current status and discovery priority remain unconfirmed. No independent review or Lean certification. All graphs finite simple connected.

## Original statement
`independence_number(x) <= max_even_minus_even_horizontal(x) + maximum(max_degree(x), card_periphery(x)) + 1`

## Counterexample
Take 51 copies of K5 and connect consecutive designated hubs with one bridge. Alpha=51 by the clique partition and selecting one nonhub per clique. Maximum degree 6. The periphery is precisely the four nonhubs at each end clique (diameter 52), so its size is 8. For any root, its own clique contributes the root alone to the even-distance set. Other cliques alternate along each side of the root clique between a single hub and four nonhubs inducing K4. Write H,Q for their respective counts, so H+Q=50 and H-Q<=2. The even-set order minus its induced edge count is at most 1+H-2Q<=3-Q<0. Thus the author's clamped maximum M equals zero. The right side equals 0+max(6,8)+1=9<51. ∎

[Joint witness verifier](../graphbrain-alpha-lower-018/verify.py). Local graph and arithmetic checks passed; analytic reasoning supplies theta and large-family quantities.
