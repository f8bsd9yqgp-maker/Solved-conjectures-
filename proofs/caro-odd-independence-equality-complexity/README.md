# Complexity of odd-independence equality: both parts of Problem 34

AI-assisted research note, 25 November 2026. Independent review and discovery priority remain unverified.

Source: Y. Caro, M. Petruševski, R. Škrekovski, Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763v2, 16 February 2026, Problem 34 (https://arxiv.org/html/2509.20763v2). The problem asks for a characterization OR recognition complexity for each of alpha_od(G)=alpha(G) and alpha_od(G)=alpha(G^2).

## Theorem
Both equality languages are Theta_2^P-complete under polynomial many-one reductions, even on connected graphs: diameter at most two for the first and at most three for the second.

Throughout, graphs are finite and simple. An odd independent set is independent and each outside vertex has either zero or an odd number of neighbors in it. The square G^2 joins distinct vertices of distance at most two. Write alpha for ordinary independence and o for odd independence.

Membership: each threshold predicate alpha(G)>=k, o(G)>=k, alpha(G^2)>=k is in NP by checking the proposed set. Binary searches recover the relevant two values using O(log |V(G)|) NP queries. Hence both languages are in Theta_2^P = P^NP[O(log n)].

For hardness use the standard Theta_2^P-complete comparison problem alpha(A)>=alpha(B) on two graphs (also known as Compare-Independent-Set, e.g. Spakowski and Vogel, *Theta_2^p-completeness: a classical approach for new results*, 2000). Inputs can be restricted to nonempty graphs by adding one isolated vertex to both.

## Lemma 1: a gadget that realizes ordinary independence as odd independence
For every vertex v of H, make independent twins x_v,y_v, a vertex a_v adjacent to both, and a private leaf b_v adjacent only to a_v. For every original edge uv add all four cross edges between the twin pairs. Call the resulting graph T(H), and let n=|V(H)|.

In any independent set, the groups containing at least one selected twin correspond to independent vertices of H. Such a group contributes at most three selected vertices; each other group contributes at most one since a_v and b_v are adjacent. Therefore alpha(T(H))<=n+2alpha(H).

Take a maximum independent set I of H. Select x_v,y_v,b_v for v in I and a_v otherwise. This is independent with n+2alpha(H) vertices. In a selected group, its sole outside vertex a_v sees three selected neighbors. In an unselected group, b_v sees one and each twin sees 1+2|N_H(v) intersect I|. All are odd. Thus o(T(H))=alpha(T(H))=n+2alpha(H).

## First equality
Let L be the least even integer at least |V(B)|. Let X be the independent two-fold blowup of A (replace each vertex by two independent twins and each edge by all four cross edges), plus L isolated vertices. Let Y=T(B) plus L+1-|V(B)| isolated vertices. Then alpha(X)=2alpha(A)+L, even, and o(Y)=alpha(Y)=2alpha(B)+L+1, odd. Isolated vertices increase both invariants by their number.

Form the complete join G=X join Y. Every nonempty independent set is wholly in one side. If alpha(B)>=alpha(A), Y has larger independence number and its maximum odd independent set remains odd independent in G, because every opposite-side vertex sees its odd cardinality. If alpha(A)>alpha(B), X has larger independence number and every maximum independent set has positive even size, so every opposite-side vertex violates the odd condition. Hence o(G)=alpha(G) iff alpha(B)>=alpha(A). Swapping inputs reduces the standard comparison problem. G is connected and has diameter at most two.

## Lemma 2: a packing gadget
Form the corona of H by attaching one private leaf to each vertex, and let P(H) be its line graph. A line graph is claw-free: three independent neighbors of one edge would be three pairwise disjoint edges all incident to one of its two endpoints, impossible. Consequently an odd independent set in a line graph is exactly an independent set in its square: no outside vertex can see two selected neighbors (even), nor three or more (claw), so at most one; conversely a distance-three packing has this property.

An independent set in the square of a line graph is an induced matching in the original graph. For an induced matching of the corona, choose one original H endpoint per matching edge (every edge has one). These chosen vertices are distinct and independent in H; an edge between two would contradict the induced matching property. Conversely the pendant edges at any independent set of H form an induced matching. Thus o(P(H))=alpha(P(H)^2)=alpha(H).

## Lemma 3: a midpoint join
For graphs U,V each of order at least two, keep their disjoint union and add one vertex m_uv per pair u in U,v in V, adjacent to u and v. Make all added vertices a clique. Call the result J(U,V).

Each cross-side original pair is at distance two. Every midpoint is at distance at most two from every original vertex and every other midpoint. Distances at most two between vertices of the same original side are unchanged, since each midpoint has exactly one neighbor from that side. Thus alpha(J^2)=max(alpha(U^2),alpha(V^2),1).

An odd independent set containing no midpoint cannot meet both sides: the midpoint of two selected opposite-side vertices would see exactly two neighbors. Any odd independent set from one original side lifts, since midpoints see at most one selected neighbor. If a set contains a midpoint m_uv, it cannot contain any other midpoint, nor u or v. Every other midpoint m_ab sees 1 plus the two endpoint membership indicators. Odd independence requires those indicators equal. The complete bipartite graph on U,V minus the edge uv is connected because both parts have size at least two. Therefore all indicators equal zero (u,v excluded). The midpoint-containing set is a singleton. Hence o(J)=max(o(U),o(V),1). The graph is connected, with diameter at most three via the midpoint clique.

## Second equality
With L as before, take H to be the independent two-fold blowup of A plus L+1 isolates. Set U=P(H). Lemma 2 gives o(U)=alpha(U^2)=2alpha(A)+L+1. Set Y=T(B) plus L+1-|V(B)| isolates, and let V be Y with one universal vertex added. Its square is complete, and o(V)=alpha(Y)=2alpha(B)+L+1: the maximum odd independent set in Y has odd size and extends unchanged, and alpha(V)=alpha(Y). Both U,V have at least two vertices.

Apply Lemma 3 to J(U,V). Its packing number is 2alpha(A)+L+1 and its odd independence number is max(2alpha(A)+L+1,2alpha(B)+L+1). Thus equality holds iff alpha(A)>=alpha(B). The constructions have polynomially many vertices and edges, including the midpoint clique. This proves hardness and completes both classifications.

## Reproduction and limitations
The companion standard-library Python verifier checked 75 gadget instances, 1,529 ordered comparisons for the first reduction (1,099 yes and 430 no), and nine ordered comparisons for the second (seven yes and two no). These are finite sanity checks; the general argument is the proof. A larger exhaustive second-reduction test was curtailed for runtime. A targeted literature search did not locate a previous solution, but is not exhaustive. No independent review or proof-assistant verification has been completed. This answers the decision-complexity alternatives, not the structural-characterization alternatives or other problems in the paper.
