# Graph Brain alpha upper-028 — Degree diversity and common neighbors

24 November 2026 US Central. AI-assisted candidate disproof. Original statement from [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and its upper-bound comment, ID from [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions from the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage), including SW=degeneracy+1 and M=max(0,max_v(|Even(v)|-|E(G[Even(v)])|)). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report holds for these entries in tested families. Original author's issue titles and targeted public searches were screened; no exact prior resolution was identified for this entry, but current status and discovery priority remain unconfirmed. No independent review or Lean certification. All graphs finite simple connected.

## Original statement
`independence_number(x) <= 10^arctan(different_degrees(x)) + 1/min_common_neighbors(x)`

## Counterexample
Add a universal vertex to K_{110,110}. Independence number 110, degree diversity 2, and every distinct pair has at least one common neighbor: nonhub pairs share the universal vertex, and hub pairs have original bipartite neighbors. Consequently the proposed right side is at most 10^arctan(2)+1<101, since arctan(2)<pi/2<2. This is smaller than 110. ∎

[Joint witness verifier](../graphbrain-alpha-lower-018/verify.py). Local graph and arithmetic checks passed; analytic reasoning supplies theta and large-family quantities.
