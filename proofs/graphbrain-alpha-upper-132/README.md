# Graph Brain alpha upper-132 — Normalized theta and Szekeres-Wilf

24 November 2026 US Central. AI-assisted candidate disproof. Original statement from [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and its upper-bound comment, ID from [corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). Definitions from the [author implementation](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage), including SW=degeneracy+1 and M=max(0,max_v(|Even(v)|-|E(G[Even(v)])|)). The August 2026 [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report holds for these entries in tested families. Original author's issue titles and targeted public searches were screened; no exact prior resolution was identified for this entry, but current status and discovery priority remain unconfirmed. No independent review or Lean certification. All graphs finite simple connected.

## Original statement
`independence_number(x) <= maximum(szekeres_wilf(x), 10^floor(lovasz_theta_over_root_n(x)))`

## Counterexample
Take twelve disjoint K6 cliques, each with a designated hub, and join consecutive hubs with single bridges. Order 72, alpha=12 (one vertex per clique upper bound, one nonhub per clique attains it). Theta=12 by the clique partition and the Lovasz sandwich theorem. Degeneracy is 5: each clique has minimum degree five; any induced subgraph containing a nonhub has a vertex of degree at most five, and a hubs-only subgraph is a path forest. The author's SW invariant is degeneracy+1=6. Thus floor(theta/sqrt(72))=floor(sqrt(2))=1 and the proposed upper bound is max(6,10)=10<12. ∎

[Joint witness verifier](../graphbrain-alpha-lower-018/verify.py). Local graph and arithmetic checks passed; analytic reasoning supplies theta and large-family quantities.
