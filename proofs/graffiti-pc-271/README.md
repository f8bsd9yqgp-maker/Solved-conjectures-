# Graffiti.pc Conjecture 271 — Total domination and maximum-degree distances

24 November 2026. AI-assisted research note, GPT-6.2. Written proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 271, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let k=γ_t(G), M be the set of vertices of maximum degree, and d_M=max_{u,v∈M}dist(u,v). The claim k≥ceil(√(2d_M)) is equivalent to k²≥2d_M.

For a minimum total dominating set D of order k, let c be the number of components of G[D]. Each has at least two vertices. Partition the remaining vertices among components adjacent to them. The quotient of the clusters is connected. Join the D-components along quotient spanning-tree edges via paths of length at most 3, giving a connected subgraph of order at most k+2(c−1). A spanning tree of this subgraph with all remaining vertices attached directly to D has diameter at most k+2c−1. For k=3, c=1 gives d_M≤4, so 2d_M≤8<9. For k≥4 the bound d_M≤2k−1 gives 2d_M≤4k−2≤k².

For k=2 a dominating edge xy gives deg(x)+deg(y)≥n, so Δ≥n/2. If two distinct maximum-degree vertices u,v were at distance at least 3, their neighborhoods would be disjoint and exclude u,v, giving 2Δ≤n−2, a contradiction. Thus d_M≤2 and k²≥2d_M. The proof covers all connected graphs of order at least two. ∎
