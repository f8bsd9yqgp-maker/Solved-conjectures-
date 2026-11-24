# Graffiti.pc Conjecture 325 — Complement-edge neighborhoods and degree-two components

24 November 2026. AI-assisted research note, GPT-6.2. Written proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 325, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let S be the degree-two vertices, c the number of components of G[N[S]], and m the minimum cardinality of N_complement(u)∪N_complement(v) over nonadjacent distinct u,v in G. The claim is m≤1+c implies well total domination. A complete graph is well total dominated independently; its minimum over complement edges is undefined.

Choose a nonedge uv attaining m. Its complement-neighborhood union consists of all vertices except common G-neighbors of u,v, including u,v themselves. Thus m≥2, so c≥1. Each component of G[N[S]] contains a degree-two vertex and its two neighbors, hence n≥3c.

Suppose c≥2. If u or v belongs to S then there are at most two common G-neighbors, so m≥n−2≥3c−2>c+1. Otherwise neither lies in S. If no vertex of S is a common G-neighbor, choose one S-vertex per component; together with u,v these give m≥c+2. If some s∈S is a common neighbor, then both u,v belong to the same component of G[N[S]] as s. Every vertex in each other component is nonadjacent to both endpoints in G; there are at least 3(c−1) such vertices, plus u,v, giving m≥3(c−1)+2>c+1. All alternatives contradict the hypothesis.

Hence c=1 and m=2. The nonadjacent pair u,v is adjacent to every other vertex. For n≥5, these vertices have degree n−2≥3 and some degree-two vertex s∈S distinct from them has N(s)={u,v}. Every total dominating set must include one of u,v. Any set containing u (or v) must also contain a neighbor x; the pair {u,x} (or {v,x}) totally dominates G. Thus all minimal sets have size two. For n=3, the graph is P3 and the claim holds. For n=4, the other two vertices are either adjacent or not; the graph is K4 minus one edge or C4, respectively. In either graph any total dominating set containing u or v contains a dominating edge, and a total dominating set avoiding both can only consist of the other two vertices, also a pair. The hypothesis is impossible at n=2 for a connected graph with a nonedge. ∎

Earlier discussion of this group is referenced in the [AI Village summary](https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj309-false-one-hundred-fifty-nine).
