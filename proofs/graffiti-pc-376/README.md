# Graffiti.pc Conjecture 376 — Isolated maximum-degree vertices and minimum transmission

24 November 2026. AI-assisted written candidate resolution. Independent review, Lean verification, and discovery priority remain unconfirmed. Source: E. DeLaViña, [Written on the Wall II](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf); the numbered statements are also available in the [August 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json). No prior complete resolution was identified in targeted searches; this is not an exhaustive priority claim.

The conjecture is t≥i+|Z|, where Z is the set minimizing the sum of distances to all vertices (the tree centroid set, not the eccentricity center).

Let T be a finite tree of order n>2, D a minimum total dominating set, t=|D|, Δ the maximum degree, M the set of maximum-degree vertices, and i the number of isolated vertices of T[M]. Let c be the number of components of T[D], and U=V(T)∖D. Each D-component has at least two vertices. Contract each to a single vertex. The resulting graph is a tree; every vertex u of U has at least one neighbor in D, and it has at most one neighbor in each D-component. Write a(u)=|N(u)∩D| and b(u)=|N(u)∩U|, and e_U=|E(T[U])|. Counting edges in the contracted tree gives

Σ_{u∈U}(a(u)−1)+e_U=c−1. (1)

For any independent subset A of U, Σ_{u∈A}b(u)≤e_U, and so (1) yields Σ_{u∈A}(deg(u)−1)≤c−1.

Choose one representative from each of the c_M components of T[M]. They are independent, so their incident edges are distinct, giving Δc_M≤n−1. Total domination implies n≤Σ_{v∈D}deg(v)≤Δt. Consequently t≥c_M+1≥i+1. If M is not independent, c_M≥i+1 and t≥i+2.

The only potentially tight case t=i+1 is therefore M independent, |M|=i. Assume Δ≥3. Put k=|M∖D|. Then |D∖M|=k+1. Every D-component contains a member of D∖M, since M is independent and no D-component is a singleton. Thus c≤k+1. Apply (1) to the independent set M∖D: k(Δ−1)≤c−1≤k. Since Δ≥3, k=0. Therefore D=M∪{x} for one vertex x outside M. Total domination forces x adjacent to every vertex of M, so T[D] is a star. As D is connected and dominating in a tree, every vertex outside D has exactly one neighbor in D and no neighbors outside D: any further edge would create a cycle. Thus T consists of x joined to i vertices of degree Δ, each of which has Δ−1 private leaves, together with ℓ≥0 leaves attached to x, where i+ℓ=deg(x)<Δ. This classifies the tight case.

If Δ=2, T is a path. For n=3 the maximum-degree set is one vertex and t=2; for n≥4 the maximum-degree vertices induce a nontrivial path and i=0.

The centroid set of a tree has one vertex or two adjacent vertices; the latter case occurs exactly when removing their connecting edge splits the tree into two equal orders. Indeed, if deleting an edge xy gives a y-side of size q, the difference in transmission from x to y is n−2q. These differences along paths establish the centroid criterion.

If t≥i+2 the assertion follows. In the classified tight case with Δ≥3, an edge incident to a leaf cannot split T equally since n>2. Removing an edge between x and a maximum-degree vertex splits off exactly Δ vertices. For i≥2, n=1+iΔ+ℓ>2Δ. For i=1, ℓ≤Δ−2, so n≤2Δ−1. In either case n≠2Δ. Thus the centroid is unique and t=i+1 suffices. If Δ=2, the three-vertex path has a unique centroid and t=i+1=2, while longer paths have i=0 and t≥2. ∎

The August transcription marks this entry open; the relevant November page image could not be retrieved.

## Finite verification
[Joint exact verifier](../graffiti-pc-365/verify.py), executed 24 November 2026: all 985 nonisomorphic trees of orders 3–12 passed the applicable claims; 950 had positive denominators in #380. The written arguments, not the finite tests, establish the unrestricted bounds on the specified domains.
