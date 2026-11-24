# Graffiti.pc Conjecture 362 — Tree radius and support-neighborhood components

24 November 2026. AI-assisted candidate resolution, not independently refereed or Lean-verified. Original problem numbers and statements are from E. DeLaViña's Written on the Wall II, as recorded in the [August 6, 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json). The current primary catalogue PDF could not be retrieved (HTTP 404); thus the current official status is not established. Targeted literature searches found no exact prior full resolution of these five entries, but priority is unverified. The current Davis completed index does not list any of them.

Let T be a finite tree on n>2 vertices, S its support vertices (neighbors of leaves), L its leaves, and c_S the number of components of T[S∪L]. Let t=γ_t(T), and r=rad(T). The conjecture is t≥c_S+(1+r)/3.

Every total dominating set D contains S. Since n>2, L and S are disjoint and every leaf has exactly one support neighbor, so c_S is also the number of components of T[S]. Write a=|D∖S|, b=|S|−c_S=|E(T[S])|, and m=t−c_S=a+b. Write c for the number of components of T[D]. Each such component contains either a vertex of D∖S or an edge of T[S], since total domination excludes singleton components. Thus c≤m, in particular m≥1.

Construct a connected dominating set K containing D by assigning each outside vertex to an adjacent D-component. The resulting clusters are connected and have a connected quotient. For each edge of a quotient spanning tree connect the two corresponding D-components using the crossing edge and the necessary edges to D, adding at most two vertices. Hence |K∖D|≤2(c−1). Every vertex outside K has exactly one neighbor in K and no neighbor outside K, because K is connected and dominating and T is acyclic. In particular all nonleaves belong to K.

Choose a diametral path of length d edges. Its d−1 internal vertices belong to K. Let q be the number of nonsupport internal vertices on this path. Then q≤a+2(c−1). The number of runs of support vertices on the internal path is at most q+1, and the number of edges within these runs is at most b. Hence the number of support vertices there is at most q+1+b. Consequently

d−1 ≤ 2q+1+b ≤ 2a+4(c−1)+1+b ≤ 6m−3.

Thus d≤6m−2, and r=ceil(d/2)≤3m−1. Rearrangement proves the conjecture. ∎

Prior computational screening of this entry (without a resolution) is reported in https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj378-false-one-hundred-sixty-four.

## Exact finite checks
[Joint verifier](../graffiti-pc-379/verify.py), run 24 November 2026: 985 trees of orders 3–12 for #362 and #379; 148 unique-degree-two-mode trees for #367; 456 connected diameter-at-most-two atlas graphs for #416; and 992 connected atlas graphs of order 4–7 for #423. All applicable checks passed. These are sanity checks, not substitutes for the written proofs.
