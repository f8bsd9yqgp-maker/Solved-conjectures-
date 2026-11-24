# Graffiti.pc Conjecture 160 — Local independence and incident triangles

24 November 2026. AI-assisted research note, GPT-6.2. Written proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 160, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let λ(v)=α(G[N(v)]), T(v) count triangles through v, and χ be 1 when G has no (not necessarily induced) 4-cycle and 0 otherwise. The claim is L≥max λ+χ max T.

Proof. A star centered at a vertex of maximum λ extends to a spanning tree without decreasing leaves, giving L≥max λ (the order-one and order-two cases hold directly). Assume G is C4-free and choose a,b maximizing λ,T respectively. In a C4-free graph each neighborhood induces a matching and isolated vertices: a two-edge path inside N(v) would form a 4-cycle with v. Consequently deg(v)=λ(v)+T(v), and deg(v)≥2T(v). Put t=T(b). For t=0 use the star bound; if a=b or T(a)≥t use the star at a.

For t≥2 and a≠b, join the stars at a,b along a shortest path if they are at distance ≥3 (disjoint stars), losing at most two leaves. At distance 2 the stars share exactly one neighbor, and their union is a tree with deg(a)+deg(b)−2 leaves. At distance 1 use ab and attach each other neighbor of a or b once: there are deg(a)+deg(b)−2−s leaves, where s≤1 is the common-neighbor count. If s=1 then T(a)≥1. These constructions yield at least λ(a)+2t−2≥λ(a)+t leaves. Extend the tree to span G.

For t=1, if T(a)>0 its star suffices. Otherwise a lies in no triangle. A shortest path from a to a triangle meets it only at its final vertex. Extend the star at a along that path (the first edge is already in the star, and subsequent vertices are outside it by shortestness), then attach the other two triangle vertices to the final vertex. They are not already in the star (if distance to the triangle is 1, two neighbors in the triangle would give a triangle through a). This adds one net leaf, at least λ(a)+1, and spanning extension finishes the proof. In the nontrivial t=1, T(a)=0 case deg(a)≥2, since a graph with max λ=1 is complete and then a is in a triangle. ∎

Prior work: the catalogue notes a July 2026 proposed proof, and [Formal Conjectures issue 4575](https://github.com/google-deepmind/formal-conjectures/issues/4575) reports an earlier Lean proof. This is an alternative written derivation, not a first resolution.
