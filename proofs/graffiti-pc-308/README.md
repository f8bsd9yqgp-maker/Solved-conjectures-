# Graffiti.pc Conjecture 308 — Total domination, Maxine and complement edge neighborhoods

24 November 2026. AI-assisted research note. **Counterexample reproduction.** Not independently refereed or machine-verified in this repository; no first-discovery claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 308. Checked against the current Davis main results index (only Graffiti.pc #318 listed).

The conjecture bounds γ_t above by (Maxine(G)+min_e |N_complement(e)|)/2. Maxine is at most α, since the greedy maximum-degree deletion process ends with an independent set.

Take K_m with one edge uv removed, m≥5. For each core vertex x attach a private two-edge pendant path x-s_x-l_x. This connected graph has 3m vertices. Each support s_x is forced into any total dominating set by l_x; to dominate s_x, one must also include x or l_x, independently for each x. Conversely choosing all supports and leaves is a total dominating set. Thus γ_t=2m.

Any independent set contains at most two core vertices and at most one from each pair {s_x,l_x}. Hence Maxine≤α≤m+2. In the complement, uv is an edge, and the union of its endpoints' open neighborhoods consists of u,v and all 2m pendant vertices, of size 2m+2. Thus the minimum over complement edges is at most 2m+2. If the alternate reading uses original-graph edges instead, choose two adjacent core vertices; their complement neighborhood union has size at most 2m+1, so the same upper bound applies.

The conjectured upper bound is therefore at most (3m+4)/2<2m for m≥5, a contradiction. For m=5, γ_t=10 and the upper bound is at most 9.5. ∎

Prior work: this is a reproduction of the K_m-minus-edge pendant-path family reported in the [AI Village August 24, 2026 series](https://grok-ai-village-news-496089.gitlab.io/series/wow.html), not a new counterexample discovery. No Lean replay performed.
