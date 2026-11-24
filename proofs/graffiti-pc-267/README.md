# Graffiti.pc Conjecture 267 — Total domination versus distance from minimum-degree vertices

24 November 2026. AI-assisted research note. **Infinite counterexample family, prior disproof exists.** Not independently refereed or machine-verified in this repository; no first-discovery claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 267. Checked against the current Davis main results index (only Graffiti.pc #318 listed).

For connected graphs of girth at least five, the conjecture is γ_t≥ceil(dist_avg(A,V)), where A is the set of minimum-degree vertices and only positive distances are averaged.

For any integer m≥3, start with the six-cycle b-x-y-c-z-w-b. Add edges a-b and c-d, then attach m private leaves to a and m private leaves to d. The resulting graph has order 2m+8, girth 6 and minimum-degree set A equal to its 2m leaves. The set {a,b,c,d} totally dominates: a and d cover their leaves, a and b dominate each other, c and d dominate each other, and all remaining cycle vertices are adjacent to b or c. In fact γ_t=4 because a,d are forced by leaves and their open neighborhoods are disjoint, requiring at least two additional distinct vertices.

From a leaf on the a side, distances to the m−1 same-side leaves are 2, to the m opposite leaves are 7, and the sum of distances to the eight core vertices is 28. By symmetry every leaf has the same sum 9m+26. Hence dist_avg(A,V)=(9m+26)/(2m+7)>4 precisely when m>2. Since γ_t=4, every m≥3 disproves the claim. At m=30 the exact average is 296/67, ceiling 5, order 68. ∎

The m=30 distance calculation was checked with NetworkX. Earlier counterexamples to #267 are reported in the [AI Village August 24, 2026 dispatch series](https://grok-ai-village-news-496089.gitlab.io/series/wow.html); this is a different explicit family, not a first disproof.
