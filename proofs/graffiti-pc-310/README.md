# Graffiti.pc Conjecture 310 — minimum transmission and total domination

24 November 2026. AI-assisted candidate written proof. Independent review, priority and Lean verification remain pending.

## Original statement

E. DeLaViña, [Written on the Wall II, entry 310, printed page 182](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf#page=182), announced March 1, 2007 and listed open in the November 6, 2026 catalogue. Both the PDF text and its page image were checked.

For every finite simple connected graph G with n>2, the conjecture is

γ_t(G) ≤ ceil(1+Tr_min(G)/3),

where Tr_min is the minimum over vertices r of the sum of distances from r to all vertices, and γ_t is the total domination number.

## Proof

Choose a vertex r attaining the minimum transmission S=Tr_min(G). Take a breadth-first spanning tree T rooted at r. Write I for the number of vertices of T having at least one child, including r. For each nonroot vertex having a child, select exactly one edge to a child. On the nonroot vertices, the selected edges form a disjoint union of directed chains: indegree and outdegree are at most one, and depth strictly increases. Each chain ends at a vertex with no child, and each other vertex of the chain has a child. A chain containing k vertices therefore contains exactly k−1 vertices counted in I.

The depths of a chain with k vertices are consecutive positive integers. Their sum is at least k(k+1)/2, which is at least 3(k−1) since (k−2)(k−3)≥0 for all positive integers k. Summing over all chains yields S≥3(I−1); the BFS tree preserves distances from r.

If I≥2, the vertices having a child induce a connected subtree and totally dominate T: every leaf has an internal parent, and every internal vertex has another internal neighbor because the internal subtree is connected and nontrivial. They therefore totally dominate G as well. Hence γ_t(G)≤I≤1+S/3, which is stronger than the conjectured ceiling bound.

If I=1 then T is a star, and r together with any child is a total dominating pair. Since n>2, S=n−1≥2, so ceil(1+S/3)≥2. This finishes the proof. ∎

## Verification and scope

The accompanying script constructs the witness on all 994 connected nonisomorphic graphs of orders 3–7 in the NetworkX graph atlas; all passed in a replay on 24 November 2026. The finite check is supplementary, not the proof.

Neither the current Davis main results table nor targeted searches for Graffiti.pc/WOWII #310 and minimum transmission with total domination revealed an earlier full resolution. A computational project mentions checking this conjecture on a particular family without resolving it (https://github.com/Kuberwastaken/c5-k4). No exclusive priority or external acceptance is claimed. No Lean proof has been checked.
