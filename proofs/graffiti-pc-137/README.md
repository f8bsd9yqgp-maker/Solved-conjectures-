# Graffiti.pc Conjecture 137 — proof for nontrivial connected graphs

24 November 2026. AI-assisted note (GPT-6.2). Written proof; independent review, priority and Lean verification pending.

## Statement
E. DeLaViña, *Written on the Wall II*, Conjecture 137 (12 July 2005), [November 2026 catalogue, p. 79](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf). Let L(G) be the maximum order of an induced path; p(G) is the minimum number of vertex-disjoint ordinary paths partitioning V(G), including singleton paths. The published inequality is equivalent to L(G)p(Ḡ) ≥ 4 for nonempty connected G.

## Theorem
The inequality holds for every finite simple connected graph of order at least two, with best possible constant 4. The singleton K₁ is the only nonempty connected exception to the literal formulation.

## Proof of the structural lemma
If a graph H of order at least two and its complement are both connected, H contains an induced P₄. This classical cograph characterization has the following direct proof. Induct on order. At order two simultaneous connectivity is impossible. Suppose H and H̄ are connected, H is P₄-free, and its order is at least three. Remove a leaf v of a spanning tree of H; H−v remains connected and P₄-free. By induction the complement of H−v is disconnected, with components C₁,…,Cₖ, k≥2. Each component contains a complement-neighbor of v, since H̄ is connected. As H is connected, some component, say C₁, also contains an H-neighbor of v. A complement path inside C₁ crossing between these two types gives vertices a,b such that va is an H-edge and vb,ab are H-nonedges. Choose c in C₂ adjacent to v in the complement. Distinct complement components are fully joined in H, hence ac and bc are H-edges and vc is a nonedge. Thus v,a,c,b induce a P₄, a contradiction. ∎

## Proof of the inequality
Connectedness and order at least two give L(G)≥2, while nonemptiness gives p(Ḡ)≥1. If p(Ḡ)≥2, the product is at least 2·2=4. Otherwise p(Ḡ)=1, so Ḡ has a spanning path and is connected; the structural lemma gives L(G)≥4. This exhausts the cases. ∎

Sharpness: P₄ and its complement are both four-vertex paths, giving product 4. For K₁ both invariants equal one, giving product 1. This explicitly distinguishes the literal disproof from the proof of the nontrivial version.

The structural lemma is classical; no claim of a novel cograph theorem or exclusive discovery priority is made. The earlier Lean sketch was not compiled and contained unproved obligations. This note makes no claim of machine verification or external acceptance.
