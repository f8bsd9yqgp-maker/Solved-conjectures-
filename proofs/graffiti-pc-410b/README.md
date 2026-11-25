# Graffiti.pc Conjecture 410b — Critical independent sets and minimum even-distance counts

24 November 2026 (US Central). AI-assisted candidate proof, not independently refereed or Lean-verified. Statement from [the August 2026 WOW II transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), listed open there. The November primary PDF returned an error on direct retrieval and the available extracted text ends at #341; later-page status is not established. The current Davis completed index does not list this result. Targeted searches did not identify an exact earlier complete resolution, but discovery priority is not established.

Let G be a finite simple connected graph on n>2 vertices, A and M the minimum- and maximum-degree sets, and H the union of all maximum critical independent sets. A critical independent set maximizes |I|−|N(I)|, and a maximum critical independent set has maximum cardinality among the critical sets. Let D_e denote the vertices attaining the specified extremum of the number of vertices at even distance. We prove |H|≤|V∖A|+|V∖M|+|E(G[D_e])| for either extremum.

If G is not regular, A∩M is empty, so the first two terms already sum to at least n. Suppose G is k-regular. Connectedness and n>2 give k≥2. For any independent set I, its k|I| incident edges enter N(I), so k|N(I)|≥k|I|. The maximum difference is zero (attained by the empty set). If a nonempty critical independent set exists, equality holds in the degree count; every edge incident to N(I) goes to I. Thus I∪N(I) is an entire connected component, and G is bipartite with equal-sized parts I,N(I). If H is empty the claim is immediate. Otherwise G is such a balanced bipartite graph. Every vertex has exactly n/2 vertices at even distance, including itself. Hence D_e=V for both extrema and |E(G[D_e])|=kn/2≥n≥|H|. ∎

This proof also proves the regular-graph special case flagged in the source commentary (see https://github.com/Kuberwastaken/c5-k4/blob/main/results/verification.md).

For #410b, D_e is the minimum even-distance-count set.

[Joint exact verifier](../graffiti-pc-372/verify.py). Graph checks executed on 994 connected atlas graphs of order 3–7 (#410a/b), and 992 of order 4–7 (#432b/#434a/b). The tree check independently passed 975 eligible trees. Finite evidence supplements the written arguments, not formal certification.
