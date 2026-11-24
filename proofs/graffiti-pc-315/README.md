# Graffiti.pc Conjecture 315 — well total dominated graphs with maximum pendant set

24 November 2026. AI-assisted written proof (GPT-6.2). Independent review, publication priority and Lean verification remain pending.

## Statement and source
E. DeLaViña, *Written on the Wall II*, Conjecture 315, announced 4 March 2007, listed open in the [November 2026 catalogue, p. 185](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf#page=185).
Let G be finite, simple and connected with n>1, and P its pendant (degree-one) vertices. If α(G)=|P|, then G is well total dominated: all inclusion-minimal total dominating sets have minimum possible cardinality.

## Proof
K2 fails the hypothesis since α=1 and |P|=2. Assume n≥3. Then P is independent. Put U=V(G)\P. If a vertex u in U has no neighbor in P, then P∪{u} is an independent set larger than α(G), a contradiction. Hence every vertex of U is a support vertex adjacent to at least one pendant vertex. Every total dominating set must contain U, since a pendant vertex has only its support as a neighbor.

The induced subgraph G[U] is connected: any simple path between two vertices of U has no pendant internal vertex. If |U|≥2, its connectedness implies that each vertex of U has a neighbor in U, while each pendant vertex also has a neighbor in U. Thus U is itself a total dominating set and is contained in all such sets. It is the unique inclusion-minimal total dominating set, with γ_t(G)=|U|.

If |U|=1, G is a star with at least two leaves. Every total dominating set contains its center and at least one leaf to dominate the center. The minimal total dominating sets consist of the center and exactly one leaf; all have cardinality two. Thus G is well total dominated in all cases. ∎

## Stronger characterization
For connected graphs of order at least three, α(G)=|P| is equivalent to every nonpendant vertex having a pendant neighbor. Necessity was proved above. For sufficiency, choose one pendant neighbor p(u) of each u in U; these choices are distinct since pendant vertices have unique neighbors. For an arbitrary independent set I, each u in I∩U excludes its distinct p(u) from I∩P, giving |I|≤|P|. Since P is independent, equality follows. This also describes every minimal total dominating set in the conjecture's domain.

## Verification
The accompanying verifier screened all 995 connected graphs of orders 2 through 7 in the NetworkX graph atlas. Exactly 16 satisfy the hypothesis, and exhaustive subset checks confirmed that all 16 are well total dominated. It also checks the bound for Conjecture 241 on 986 trees. This computation is a sanity check rather than the proof. No claim of exclusive originality or machine verification is made.
