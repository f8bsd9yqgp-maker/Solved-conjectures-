# Graffiti.pc Conjecture 258 — even-distance count and maximum spanning-tree leaves

24 November 2026. AI-assisted candidate written proof; no prior full resolution identified by targeted searches. Not independently refereed or Lean-verified.

## Statement
E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 258 (announced February 23, 2007, listed open). For a connected simple graph of order n≥2, write t for its total domination number, L for the maximum number of leaves of its spanning trees, and E for the maximum number of vertices at even distance from a single vertex, including the vertex itself. The conjecture is tL≥2E. The singleton is excluded because total domination is undefined. The PDF text was accessible but screenshot retrieval failed.

## Two auxiliary bounds
First, root a breadth-first spanning tree at v. Its bipartition A,B consists of even and odd graph-distance layers. Each tree edge contributes one to the degree sum over A; every nonleaf there has degree at least two. Consequently n−1≥2|A|−ℓ_A≥2|A|−L, where ℓ_A counts tree leaves in A. Maximizing over v yields 2E≤n+L−1.

Second, let D be a minimum total dominating set. Each component of G[D] has at least two vertices, so there are c≤floor(t/2) components. Assign each vertex outside D to a component containing one of its neighbors. The resulting partition into connected clusters has a connected quotient. For each edge of a spanning tree of the quotient, connect the corresponding D-components via the cross-cluster edge and the two endpoint-to-D edges as needed. This adds at most two vertices per quotient edge. The union is a connected dominating set K containing D with |K|≤t+2(c−1)≤2t−2. Take a tree on K and attach each outside vertex to a neighbor in K; this gives L≥n−|K|. Hence n≤L+2t−2.

## Proof
If t≥3 and L≥3, combine the auxiliary bounds:
2E≤n+L−1≤2L+2t−3≤tL,
where the last inequality follows from (t−2)L≥3(t−2)≥2t−3.

If L=2, then G has maximum degree at most two: a star with three or more leaves could otherwise be extended to a spanning tree without losing leaves. Hence G is a path or cycle. In either case E≤ceil(n/2) (on a cycle, there are two vertices at each positive distance below half its order, and just one at the antipode when n is even). Any total dominating vertex covers at most two vertices, giving t≥ceil(n/2). Thus tL≥2E.

It remains to consider t=2. A total dominating pair is an edge, so the second auxiliary bound gives L≥n−2. Every vertex has a neighbor at odd distance, hence E≤n−1. If E≤n−2 the result follows. Otherwise a vertex v has exactly one vertex w at odd distance. Every other vertex must be at distance two from v: any distance at least three would produce a second odd-distance vertex on a geodesic. Each such vertex is adjacent to w, so w is universal and its spanning star has n−1 leaves (for n=2, the single edge has two leaves). Hence L≥n−1=E. This completes all cases. ∎

## Verification
The exact NetworkX atlas check passed all 995 connected nonisomorphic graphs of orders 2–7. It enumerates total dominating subsets and connected dominating subsets, using the standard identity L=n−γ_c for n≥3 (the internal vertices of a spanning tree form a connected dominating set, and conversely a connected dominating set can be extended by leaves). The two-vertex case is handled separately. This is a finite sanity check, not the universal proof. No prior complete solution was identified by targeted searches; that does not establish priority.
