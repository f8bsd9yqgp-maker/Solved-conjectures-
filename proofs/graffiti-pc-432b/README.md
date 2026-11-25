# Graffiti.pc Conjecture 432b — Independent domination, supports and distance parity

24 November 2026 (US Central). AI-assisted candidate proof, not independently refereed or Lean-verified. Statement from [the August 2026 WOW II transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), listed open there. The November primary PDF returned an error on direct retrieval and the available extracted text ends at #341; later-page status is not established. The current Davis completed index does not list this result. Targeted searches did not identify an exact earlier complete resolution, but discovery priority is not established.

Let G be connected on n>3 vertices, P its pendants, S=N(P) its support vertices, i its independent domination number and E(v),O(v) the even- and odd-distance counts (including distance zero in E). The claim is i≤n−|S|+χ_bipartite min_v(E(v)−O(v)).

If G is nonbipartite, P is independent (distinct adjacent leaves would make the graph K2). Extend P to a maximal independent set, which avoids S. This yields i≤n−|S|.

If G is bipartite, let its part sizes be a≤b. Every vertex in either part has a neighbor, so the smaller part is a maximal independent set and i≤a. For each support vertex in the larger part, choose a distinct pendant neighbor in the smaller part. These chosen leaves are disjoint from the support vertices in the smaller part (a vertex cannot be both leaf and support in a connected graph of order >2). Thus |S|≤a. Every vertex in the smaller part has E=a,O=b, and every vertex in the larger part has E=b,O=a. Hence the claimed right side is a+b−|S|+(a−b)=2a−|S|≥a≥i. ∎

[Joint exact verifier](../graffiti-pc-372/verify.py). Graph checks executed on 994 connected atlas graphs of order 3–7 (#410a/b), and 992 of order 4–7 (#432b/#434a/b). The tree check independently passed 975 eligible trees. Finite evidence supplements the written arguments, not formal certification.
