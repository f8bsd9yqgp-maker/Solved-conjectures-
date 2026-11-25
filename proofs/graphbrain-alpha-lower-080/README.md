# Graph Brain alpha lower-080 — Girth, maximum degree and even-distance invariant

24 November 2026 US Central. AI-assisted candidate disproof. Original statement from [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and its upper-bound comment, ID from [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions from the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage), including SW=degeneracy+1 and M=max(0,max_v(|Even(v)|-|E(G[Even(v)])|)). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report holds for these entries in tested families. Original author's issue titles and targeted public searches were screened; no exact prior resolution was identified for this entry, but current status and discovery priority remain unconfirmed. No independent review or Lean certification. All graphs finite simple connected.

## Original statement
`independence_number(x) >= -girth(x)^max_degree(x) + 2*max_even_minus_even_horizontal(x)`

## Counterexample
Take the ladder P65 Cartesian product K2. The graph is connected and bipartite with two parts of 65 vertices, and its 65 disjoint rungs show alpha<=65. Either part attains equality. Every even-distance set is a bipartition part and induces no edges, so M=65. Girth 4 (it is bipartite and contains a square), maximum degree 3. The claimed lower bound is -4^3+2*65=66>65. ∎

[Joint witness verifier](../graphbrain-alpha-lower-018/verify.py). Local graph and arithmetic checks passed; analytic reasoning supplies theta and large-family quantities.
