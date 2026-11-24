# Graffiti.pc Conjecture 179 — Spanning-tree leaves, domination and local independence

24 November 2026. AI-assisted research note. **Written proof, priority unverified.** Not independently refereed or machine-verified in this repository; no first-discovery claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 179. Checked against the current Davis main results index (only Graffiti.pc #318 listed).

Let L be the maximum number of spanning-tree leaves, b the largest induced bipartite order, γ the domination number, λ the maximum local independence, and δ the minimum degree. The claim for connected graphs on at least two vertices is L+b≥δ+γ+λ.

Choose a vertex v with an independent set S⊆N(v) of size λ. Extend {v} greedily to a maximal independent set I of G. Since v belongs to I, the set I is disjoint from S. Maximality implies I is a dominating set, so |I|≥γ. Both I and S are independent, and G[I∪S] is therefore bipartite, giving b≥γ+λ.

A star on a maximum-degree vertex extends to a spanning tree by repeatedly adding one new vertex via one edge. For degree at least two it initially has Δ leaves and never loses net leaves. If Δ=1 the connected graph is K2 and has two leaves. Thus L≥Δ≥δ. In fact the stronger inequality L+b≥Δ+γ+λ holds. ∎

No first-discovery claim; independent review and literature priority remain outstanding. The proof covers either minimum or maximum degree in the right-hand side.
