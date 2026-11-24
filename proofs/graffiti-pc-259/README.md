# Graffiti.pc Conjectures 259–261 — common proof

24 November 2026. Candidate written proofs (AI-assisted). No independent refereeing, Lean verification or established priority.

Source: E. DeLaViña, [Written on the Wall II](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), November 2026 edition, printed pp. 150–151. Entries 259, 260, 261 (announced February 23, 2007) are marked open. The PDF text was retrieved; screenshot requests for these two pages failed with HTTP 404. The definitions identify L(G) in these formulas as the maximum spanning-tree leaf count L_s(G).

Let G be a finite simple connected graph of order n≥2, t its total domination number, L its maximum spanning-tree leaf count, Δ its maximum degree, and q(X)=|N(X) minus X|. The three assertions are tL≥2q(X), respectively for the set of maximum-degree vertices, peripheral vertices (maximum eccentricity), and degree-two vertices.

## Connected domination bound

Take a minimum total dominating set D, of size t≥2. Every component of G[D] has at least two vertices, so there are c≤floor(t/2) components. Assign every outside vertex to a component containing one of its neighbors, making a partition into connected clusters. The quotient is connected. For each edge of a quotient spanning tree, join its two D-components via the cross-cluster edge and, where needed, the two endpoint-to-D edges. This adds at most two vertices per quotient edge. The resulting union K is connected and dominating, contains D, and has size at most t+2(c−1). A spanning tree of K extended by attaching each remaining vertex directly to K has at least n−|K| leaves. Thus

n≤L+t+2 floor(t/2)−2.

Also L≥Δ by extending a star at a maximum-degree vertex to a spanning tree without losing existing leaf count (K2 is immediate).

## General theorem for L≥3

For every X, prove tL≥2q(X).

If X is empty, q=0. If X is a singleton, q≤Δ≤L and t≥2. Otherwise q≤n−2.

If t=2, the connected domination bound gives n≤L+2, proving the claim. If t≥3 and L≥4, then q≤L+2t−4 and tL−2(L+2t−4)=(t−2)(L−4)≥0.

If L=3, then Δ≤3. Put s=|X|. We have q≤min(3s,n−s)≤3n/4. For even t, the connected domination bound gives n≤2t+1, so q≤floor(3t/2+3/4)=3t/2. For odd t it gives n≤2t, so q≤3t/2 directly. This completes the theorem.

## L=2 and the three conjectures

Here Δ≤2, hence G is a path or a cycle. In a cycle, all three specified sets are V(G), so their external neighborhoods are empty. For a path of order at least three, the maximum-degree and degree-two sets are the internal vertices, whose external neighborhood has at most two vertices. The peripheral set consists of the two endpoints, with external neighborhood of size at most two as well. Thus tL≥4≥2q in each case. In K2 the maximum-degree and peripheral sets are the entire graph, and the degree-two set is empty. This proves all three conjectures. ∎

## Verification

The accompanying Python program exactly enumerates vertex subsets to obtain t and the connected domination number on all 995 connected graphs in the NetworkX atlas of orders 2–7. For n≥3 the maximum leaf count equals n minus the connected domination number: internal tree vertices form a connected dominating set, and a connected dominating set can be extended into a spanning tree with every outside vertex a leaf. K2 is handled separately. All three inequalities passed, and the stronger arbitrary-X theorem passed for every subset of every tested graph with L≥3. Run on 24 November 2026. The general proof is independent of computation.

No exact prior resolution of these entries was identified in targeted searches. This is not a claim of priority.