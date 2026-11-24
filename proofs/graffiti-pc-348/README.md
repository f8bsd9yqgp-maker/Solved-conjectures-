# Graffiti.pc Conjecture 348 — External neighborhood of degree-two vertices

24 November 2026. AI-assisted written candidate resolution. No Lean verification, independent refereeing or established discovery priority. Source statement: DeLaViña, Written on the Wall II, entry as transcribed in the [6 August 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), marked open there. The November primary PDF is [here](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf); retrieval of the relevant later page images failed, so the present-day catalogue status and original typography are not independently verified. Neither Davis's current main index nor targeted searches identified an exact full resolution, but this is not an exhaustive priority search.

Let T be a finite tree of order n>2, S its degree-two vertices, U=N(S)∖S, and D a minimum total dominating set of size t. The conjecture states t≥2|U|/3.

We prove the stronger bound |U|≤t+floor(t/2)−1. Let c be the number of components of T[D]. Total domination implies every component has at least two vertices, so c≤floor(t/2).

Partition U into selected vertices A=U∩D, unselected vertices B with a neighbor in S∩D, and remaining vertices F=U∖(A∪B).

Each vertex of B may be assigned to one neighboring vertex of S∩D. Every selected degree-two vertex has a selected neighbor (it must itself be totally dominated), so it has at most one unselected neighbor. Thus these assignments are injective and |B|≤|S∩D|. Since A and S∩D are disjoint subsets of D, |A|+|B|≤t.

For each u∈F, choose an adjacent degree-two vertex s. By definition s∉D. To dominate s, its other neighbor w must belong to D because u∉D. To dominate u, choose a neighbor x∈D. The vertices x,u,s,w are all distinct: otherwise there would be a cycle in T. Thus they form a path with endpoints in D and two internal vertices outside D. For different u these paths have disjoint interiors: u lies outside S, and s cannot be shared since its other neighbor w is selected. Their endpoints must lie in different components of T[D], since otherwise the path together with a path in T[D] forms a cycle. Contract the components of T[D], keeping the paths as edges; the resulting multigraph is acyclic because T is a tree and the paths have disjoint interiors. Hence there are at most c−1 such paths, so |F|≤c−1.

Consequently |U|=|A|+|B|+|F|≤t+c−1≤t+floor(t/2)−1. In particular 3t≥2|U|+2, which is stronger than the conjecture. ∎

This direct counting proof requires no imported total-domination bound. No earlier exact proof was identified in targeted searches; priority remains unverified.

## Verification
[Joint exact verifier](../graffiti-pc-348/verify.py): all 985 nonisomorphic trees of orders 3–12 passed every applicable inequality on 24 November 2026. Finite checks supplement the general arguments.
