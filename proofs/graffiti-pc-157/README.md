# Graffiti.pc Conjecture 157 — Radial-circle edges and spanning-tree leaves

24 November 2026. AI-assisted research note, GPT-6.2. Written proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 157, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let L be maximum spanning-tree leaves, f₁ the number of degree-one vertices, and R(v) the vertices at distance rad(G) from a center v. The claim is L ≥ f₁ + √(2 max_{v center}|E(G[R(v)])|).

Proof for connected graphs of order at least two. In a breadth-first spanning tree rooted at a center v, every vertex of R(v) is a leaf. Every degree-one vertex of G is a leaf in every spanning tree. For n≥3, no degree-one vertex can lie on an edge within R(v): its unique neighbor lies one BFS level closer to v, unless the degree-one vertex is the root, which is not in R(v). Thus if q is the number of nonpendant vertices of R(v), the induced edge count e is at most q(q−1)/2, so √(2e)≤q. The BFS tree has at least f₁+q leaves. Choose v maximizing e. The two-vertex case has two leaves and e=0. The singleton has zero on the right and satisfies the inequality with the degree-one leaf convention. ∎
