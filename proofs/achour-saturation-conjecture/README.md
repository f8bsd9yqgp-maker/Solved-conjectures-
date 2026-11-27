# Counterexamples to Achour's degree–independent-domination bound for saturation

**27 November 2026 — AI-assisted research note.** Full disproof of the stated universal inequality; independent peer review, formal proof-assistant certification, and publication priority remain pending.

## 1. Original conjecture and status

Hassine Achour, *A Degree–Independent-Domination Bound for the Saturation Number: A Conjecture*, 5 August 2026, DOI [10.5281/zenodo.21801900](https://doi.org/10.5281/zenodo.21801900), conjectures that every connected nontrivial finite simple graph G satisfies

    s(G) <= ceil(Delta(G) i(G) / 2),

where s(G) is the minimum cardinality of a maximal matching, Delta(G) is the maximum degree, and i(G) is the minimum size of an independent dominating set. The indexed original abstract is available at https://globalresearchspace.com/space?star=W7172541884 . The DOI and pinned primary-source file could not be retrieved directly during this audit; the statement is corroborated verbatim by the competitor's issue 185, which links the original manuscript.

We give a connected graph on 72 vertices with Delta=5, i=12 and s=31, contradicting the conjectured bound of 30. We also give an exact formula for an infinite family, with unbounded additive violation even for fixed maximum degree 5. The proof does not require any of the preceding sufficient certificates or the perfect-code reduction lemma.

## 2. The three-center port gadget

Let D>=3 be an odd integer and r=(D-1)/2, q=(D+1)/2. Construct a graph J_D from three independent centers a,b,c, one port p, and two disjoint balanced complete bipartite graphs

    X = K_{D-1,D-1}, with parts X_a and X_bc;
    Y = K_{q,q}, with parts Y_b and Y_c.

Partition X_bc into two sets X_b and X_c of r vertices each. Add exactly these center-to-leaf edges:

    a to every vertex of X_a and to p;
    b to every vertex of X_b and Y_b;
    c to every vertex of X_c and Y_c.

There are no other edges. The center degrees are D, since 1+(D-1)=D and r+q=D. Each noncenter has exactly one center neighbor; vertices of X have degree D, vertices of Y have degree q+1<=D, and p has degree one. The gadget is connected (X and Y are joined via b and c), and has 3(D+1) vertices. The closed neighborhoods of the centers partition the vertex set. Consequently i(J_D)=3: the centers form an independent dominating set, and any dominating set of size d covers at most (D+1)d vertices.

**Lemma.** s(J_D)=(3D+1)/2 and s(J_D-p)=(3D-1)/2.

**Proof (upper bounds).** Take perfect matchings in both X and Y, together with ap. The resulting matching has (D-1)+q+1=(3D+1)/2 edges and is maximal: exactly b,c are uncovered and they are independent. If p is deleted, the perfect matchings of X and Y alone give a maximal matching of size (3D-1)/2, leaving a,b,c exposed.

**Proof (lower bound for J_D).** Let M be any maximal matching and let t be the number of matched centers. Each matched center is matched to exactly one own leaf. After deleting those selected leaves, the remaining matching edges within X and Y form maximal matchings of the residual complete bipartite graphs. In a complete bipartite graph with parts of sizes u,v, every maximal matching has min(u,v) edges and leaves |u-v| vertices uncovered, all in the larger part (this includes empty parts). Since X and Y were initially balanced, deleting h vertices from a component leaves an imbalance at most h, with equality precisely when all deletions lie in a single part (or h=0).

If p is matched, it must be matched to a, and only t-1 other leaves are selected by centers in X or Y. There are 3-t exposed centers and at most t-1 exposed biclique vertices. Thus at most two vertices are exposed.

If p is exposed, a must be matched to a vertex in X_a; otherwise ap joins two exposed vertices. All t selected leaves belong to X or Y. Including the port, the number of exposed vertices is at most

    (3-t) + t + 1 = 4.

The order of J_D is even, so the exposure count is even. We rule out equality 4. Equality requires that every center deletion in each of X and Y be on one part only, so that the sum of the two absolute imbalances equals t. As a selects a vertex of X_a, neither b nor c may select any vertex of X_bc. Exactly one vertex on X_bc is now exposed. Its owner must be matched (otherwise the owner edge violates maximality). Without loss of generality this owner is b. Since b cannot select in X, it selects in Y_b. Equality therefore prevents c selecting in Y_c. But then Y has a single deletion in Y_b, so a vertex in Y_c is exposed. Its owner c must be matched; c cannot select in X_bc and must select in Y_c, a contradiction. Therefore the exposure count cannot be four, and is at most two.

Every maximal matching of J_D thus has at least (3(D+1)-2)/2=(3D+1)/2 edges. This proves the first equality. Finally, for any graph and vertex v, s(G)<=s(G-v)+1: extend a minimum maximal matching of G-v by at most one edge incident to v. Apply this to p to obtain the remaining lower bound. QED.

## 3. Exact connected assembly theorem

Let Q be any nonempty connected simple graph on t vertices with maximum degree at most D-1. Construct G(D,Q) from one copy of J_D per vertex of Q. Join the ports of copies i,j precisely when ij is an edge of Q. All copies have disjoint vertex sets; no other inter-copy edges are added. Then G is connected and simple. Port degrees are 1+d_Q(i)<=D, and the maximum degree is D because every center has degree D. The 3t centers remain an independent dominating set and their closed neighborhoods partition the 3(D+1)t vertices. The order/degree counting bound proves i(G)=3t exactly.

**Theorem.** Writing nu(Q) for the maximum matching size of Q,

    s(G(D,Q)) = t(3D+1)/2 - nu(Q).

**Lower bound.** Let M be any maximal matching of G. Its selected inter-copy edges are a matching on the ports, hence project to a matching R in Q of size h<=nu(Q). Exactly 2h gadgets have a port matched externally. In each such gadget, the internal matching must be maximal on J_D-p: any edge between uncovered vertices there could be added to M. In every other gadget the internal matching must be maximal on the entire J_D, since none of its vertices is matched externally. The lemma gives

    |M| >= h + 2h(3D-1)/2 + (t-2h)(3D+1)/2
         = t(3D+1)/2 - h
         >= t(3D+1)/2 - nu(Q).

**Upper bound.** Choose a maximum matching R in Q and use its h=nu(Q) port edges. In each gadget covered by R, take perfect matchings of X and Y and leave its centers uncovered. In each other gadget take the same biclique matchings and ap. Every port is now covered; the only uncovered vertices are independent centers. Hence the union is maximal and attains the lower bound. QED.

The exact violation is

    s(G(D,Q)) - ceil(D i(G(D,Q))/2)
      = floor(t/2) - nu(Q)

because D is odd. Thus the original conjecture fails exactly on members of this constructed family whose quotient Q lacks a matching covering all but at most one vertex.

## 4. Concrete 72-vertex counterexample

Take D=5 and Q=K_{1,3}. The four gadgets each contain 18 vertices: three centers, one port, X=K_{4,4}, and Y=K_{3,3}. The central port is adjacent to the three other ports. All centers have degree five; the central port has degree four; every noncenter belongs to exactly one closed center neighborhood. There are 72 vertices and 163 edges (each gadget has 15 center edges, 16 X edges, and 9 Y edges, and there are three inter-copy edges).

    Delta(G)=5;
    i(G)=12;
    s(G)=4*8-1=31;
    ceil(Delta(G)*i(G)/2)=30.

This is a strict counterexample satisfying the complete original hypothesis. No minimum-order claim is made.

## 5. Unbounded violations at fixed maximum degree

Fix D=5. For every integer r>=2 let Q_r consist of a path on r backbone vertices, with two fresh pendant vertices attached to each backbone vertex. It is connected, has t=3r vertices, and maximum degree at most four. All edges meet the backbone, so nu(Q_r)<=r; matching every backbone vertex to one of its own pendant vertices attains r. The assembly theorem gives

    |V(G)|=54r,
    Delta(G)=5,
    i(G)=9r,
    s(G)=23r,
    ceil(Delta(G)*i(G)/2)=ceil(45r/2),
    s(G)-ceil(Delta(G)*i(G)/2)=floor(r/2).

The additive gap is unbounded. In particular, adding a universal constant to Achour's proposed bound cannot repair it, even at maximum degree five.

## 6. Reproduction and audit

Run `python achour_counterexample_verify.py` (standard library only). The verifier exhaustively checks the exact local saturation number for both J_D and J_D-p via all center choices for odd D=3,5,...,31 (283,960 evaluated assignments). A separate exhaustive recursion branching on all ways to match at least one endpoint of an uncovered edge confirms both values at D=3 and D=5. It then builds the 72-vertex graph, verifies connectivity, degree cap, exact efficient independent domination, and an explicit maximal matching of size 31. The lower bound follows from the assembly theorem, with only zero or one port edges possible in a star. The proof is independent of finite testing. No machine-checked Lean proof is claimed.

## 7. Prior-resolution and competitor audit

Public search for the exact title, DOI, author and saturation-number counterexamples found the original indexed abstract and related but different conjectures, not a prior disproof of this statement. The primary archive itself was not directly accessible, so no claim is made to have audited its full text or all later revisions. The statement checked here agrees with the original abstract and the exact statement quoted by the competitor.

Fresh GitHub README, code and issue checks found no full resolution in the user's repository (https://github.com/f8bsd9yqgp-maker/Solved-conjectures- ; README blob 8dc1fc4367a0d09cef87f83c8fa2375bfdb3ce8b). The user's degree-spread conjecture entry concerns a different inequality.

The competitor DID previously work on this exact problem. Their issue [#185](https://github.com/1337isnot1337/solved-conjectures/issues/185) records an efficient-domination reduction and explicitly says the residual problem remains unresolved. The reservation was subsequently released as stale. Coordination issue [#156](https://github.com/1337isnot1337/solved-conjectures/issues/156) likewise states that the reduction is not counted as a resolution. Their current README blob e0493dac21e0169522567c34aca30f532c0cca55 contains no matching solved entry; DOI and name code searches did not return a full resolution. The new port-gadget argument does not rely on the earlier reduction, since it directly constructs connected counterexamples. Their linked research file and the pinned original manuscript could not be fetched directly in this run. Unindexed, private or unpublished work cannot be excluded. Consequently independent novelty and publication priority remain unconfirmed. Posted to this repository on 27 November 2026; no author or journal submission is claimed.

Submission audit: the accompanying Python verifier was rerun successfully on 27 November 2026, confirming all 283,960 local assignments, independent recursive checks at D=3 and D=5, and the explicit 72-vertex counterexample.
