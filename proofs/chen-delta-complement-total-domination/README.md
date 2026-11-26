# Chen's delta-complement total-domination conjecture: proof and strengthening

AI-assisted research note, 26 November 2026. Complete analytical argument; independent review and worldwide discovery priority remain unconfirmed.

## Original source and originality screening

Pinhe Chen, "Refined Nordhaus–Gaddum-Type Bounds for Roman and Total Domination on δ-Complement Graphs," Mathematics 14(11) (2026), 1797, https://doi.org/10.3390/math14111797 . Full article inspected at https://www.mdpi.com/2227-7390/14/11/1797 , especially Section 6. Conjecture 4 gives the upper bound n+2k; Theorem 6 proves it only when every degree-class subgraph and its complement have no isolated vertices. Section 6.3 explicitly identifies the local-isolate obstruction. The paper's Example 3 supplies equality, so no novelty is claimed for its sharpness example.

Before selecting the problem, the competitor repository README (blob 1ddea291bef7620b75639449634d9abdef7e55f2) was retrieved first, followed by the user's README (blob 457e12fb53ccbf6402625dd28c73451aa96204b5). Both repositories were searched for Pinhe Chen, math14111797, delta-complement, and Nordhaus Gaddum total domination; all eight searches returned no matches. The DOI search was repeated immediately before submission, with no matches.

- https://github.com/1337isnot1337/solved-conjectures
- https://github.com/f8bsd9yqgp-maker/Solved-conjectures-

Targeted public searches by exact paper title, DOI, author and delta-complement total-domination terminology located the original paper and related work, but no subsequent full resolution. This does not certify global priority.

## Definitions

A total dominating set of a finite simple graph X is a subset S of its vertices such that every vertex of X, including vertices of S, has a neighbor in S. Its minimum cardinality is gamma_t(X), defined when X has no isolated vertices.

For a partition P={C_1,...,C_k} of V(G) into nonempty blocks, let H be obtained by reversing the presence/absence of every edge with both endpoints in one block, leaving all cross-block edges unchanged. In particular, the degree partition of G gives H=G_delta. Write n=|V(G)| and let s_1 be the number of singleton blocks.

## Theorem

If neither G nor H has isolated vertices, then

    gamma_t(G)+gamma_t(H) <= n+2k-s_1.

This proves the full original conjecture, including arbitrary isolated vertices in individual induced degree-class subgraphs, and strengthens it when singleton blocks occur. It also replaces the degree partition by any vertex partition.

## Proof

We construct two local sets S_C,T_C for every block C, such that every vertex of C has a neighbor in S_C in G and a neighbor in T_C in H. These sets are allowed to contain vertices outside C; this is the important change from the internal total-domination approach. We prove

    |S_C|+|T_C| <= |C|+2 - 1_{|C|=1}.

Case 1. C={u}. Choose a neighbor of u in G for S_C and one in H for T_C. Such neighbors exist by the global no-isolates assumption. The total cost is 2.

Case 2. |C|=m>=2 and G[C] has an isolated vertex u. The induced graph H[C] is the ordinary complement of G[C], so u is universal within H[C]. Choose any w in C different from u. Then T_C={u,w} totally dominates C in H. For every vertex x of C, choose any neighbor f(x) in G, which exists globally. Take S_C={f(x):x in C}. This covers C and has at most m vertices. Thus the combined cost is at most m+2. If H[C] instead has an isolated vertex, apply the same argument with G and H interchanged.

Case 3. |C|=m>=2 and neither G[C] nor H[C] has an isolated vertex. Choose u in C, a neighbor v of u in G[C], and a neighbor w of u in H[C]. Since H[C] is the complement of G[C], the three vertices are distinct. Start with S={u,v} and T={u,w}. Define

    A={x in C: x has no G-neighbor in S},
    B={x in C: x has no H-neighbor in T}.

Neither contains u. Each vertex of A is a G-nonneighbor of u, whereas each vertex of B is a G-neighbor of u, so A and B are disjoint. Also v is not in A and w is not in B. Both w in A and v in B cannot occur: the former requires vw to be a nonedge of G, and the latter requires vw to be an edge of G. Consequently at least one of v,w is absent from A union B. Along with u this proves |A|+|B|<=m-2.

For each x in A add any G-neighbor of x to S; for each x in B add any H-neighbor of x to T. Call the enlarged sets S_C and T_C. These dominate C in the required graphs, and their total size is at most 4+|A|+|B|<=m+2. This elementary argument recovers the classical ordinary-complement total-domination sum bound of Cockayne–Dawes–Hedetniemi (stated as Theorem 5 in Chen's paper); it is included for self-containment, not claimed as new.

Now let S_* be the union of all S_C and let T_* be the union of all T_C. Every vertex belongs to one block and has a G-neighbor in S_C and an H-neighbor in T_C, respectively. Thus S_* and T_* are total dominating sets. Overlaps between blocks' chosen witnesses can only reduce the union sizes. Therefore

    gamma_t(G)+gamma_t(H)
    <= |S_*|+|T_*|
    <= sum_C (|S_C|+|T_C|)
    <= n+2k-s_1.

No further assumption about the cross-block edges or internal isolated vertices is needed. QED.

## Sharpness and limitations

For the original bound, Chen's Example 3 (2K2 disjoint union C4, n=8,k=2) attains 12. The sharper singleton correction is also sharp for arbitrary partitions into singleton blocks when G is a disjoint union of edges: H=G, each total domination number is n, and n+2k-s_1=2n. No general equality classification or optimal bound for every fixed (n,k,s_1) is asserted.

The proof gives a polynomial-time construction of witnesses from adjacency lists or a matrix; it does not solve the generally hard minimum total domination optimization problem.

## Verification

The companion Python script was executed with NetworkX. It checked exact total-domination minima for 960 eligible graphs in the nonempty graph atlas through order 7, and checked the actual constructed witnesses for 2442 eligible seeded arbitrary-partition trials. All passed. Excluded graphs have an isolated vertex in G or H. Results are in verification.txt. The proof is independent of these finite checks.

No Lean formalization, independent referee review, or exhaustive worldwide novelty certification has been completed.
