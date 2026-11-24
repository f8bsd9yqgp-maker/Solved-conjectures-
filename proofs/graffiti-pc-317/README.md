# Graffiti.pc Conjecture 317 — Induced tree size and well total domination

24 November 2026. AI-assisted research note, GPT-6.2. Written proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 317, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let t be the maximum order of an induced tree of G and m=|E(complement G)|. The claim is that t≥m implies G is well total dominated (every inclusion-minimal total dominating set has minimum size).

For t≥2, the complement edges within an induced t-vertex tree number (t−1)(t−2)/2. If m≤t, then t≤4 and m≤4.

Suppose a minimal total dominating set D has k≥3 vertices. For each s∈D there is a distinct private witness w_s with N(w_s)∩D={s}; otherwise s could be removed. For k≥5 each witness contributes at least k−2 distinct complement edges to D. Each edge is counted at most twice since witnesses are distinct, so m≥k(k−2)/2>4.

For k=3, G[D] has minimum degree at least one and is either a triangle or a three-vertex path. In the triangle all three private witnesses lie outside D, giving at least six distinct complement edges. For the path, both endpoints have private witnesses outside D (no vertex within D has just that endpoint as its neighbor in D). Those two witnesses give four distinct complement edges; the nonedge between the path endpoints gives a fifth. Both cases contradict m≤4.

For k=4, the same counting gives m≥4. Equality forces all four distinct witnesses to belong to D, because an outside witness would contribute three rather than two missing edges. Hence every vertex in G[D] has degree one there, so G[D] is two disjoint edges. The four complement edges lie entirely within D; every outside vertex is universal. An induced tree containing a universal vertex can have at most three vertices because the remaining graph has independence number at most two. An induced tree within D has at most two vertices. Thus t≤3<m=4, a contradiction. All minimal total dominating sets therefore have size two, proving the claim. ∎
