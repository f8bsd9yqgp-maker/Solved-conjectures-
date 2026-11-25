# Subcubic tree counterexamples to Achour's degree-spread bound

AI-assisted note, 25 November 2026. Source: Hassine Achour, *A Degree-Spread Bound Between Independent Domination and Minimum Maximal Matchings: A Conjecture*, 5 August 2026, DOI 10.5281/zenodo.21806397 (abstract inspected via https://globalresearchspace.com/space?star=W7172521502; DOI landing page unavailable in this session). The conjecture asserts i(G)-s(G)<=Delta(G)-delta(G) for every connected nontrivial graph, where i is minimum independent dominating set size and s is minimum maximal matching size.

Priority: a regular-graph counterexample to the underlying inequality had already been reported in July 2026 (https://github.com/djma/TxGraffiti-conjecture3-counterexample/blob/main/counterexample_note.md). This is a restricted-class counterexample and independent finite check, not a first resolution of the general assertion. Priority of the tree-specific observation is unverified.

## General construction

For any finite graph H of order m attach one private leaf to each vertex, obtaining its corona C. Each independent dominating set contains exactly one vertex from each core-leaf pair: at least one to dominate the leaf, and at most one by independence. All leaves constitute such a set, so i(C)=m.

Every maximal matching saturates every core vertex; otherwise both that vertex and its private leaf are unmatched. If it contains x core-core edges and y pendant edges, 2x+y=m, and its size is m-x>=m-nu(H), where nu(H) denotes maximum matching size. Conversely, take a maximum matching of H and add a pendant edge at every unmatched core vertex. The resulting matching saturates every core vertex, is maximal, and has size m-nu(H). Thus s(C)=m-nu(H) and i(C)-s(C)=nu(H).

In particular H=P_(2k), k>=2, gives a tree of order 4k, maximum degree 3, minimum degree 1, i=2k and s=k. The conjecture fails for k>=3 with excess k-2. No bound depending solely on maximum and minimum degrees can hold even for subcubic trees.

## An 11-vertex witness

Take the spine 2,1,0,6,7. Attach leaves 3,4 to 2; 5 to 1; 10 to 6; and 8,9 to 7. The edge list is (1,0),(1,2),(1,5),(0,6),(2,3),(2,4),(6,7),(6,10),(7,8),(7,9). Degree spread is 2.

Each of the four support vertices 1,2,6,7 must be saturated in every maximal matching, so at least two matching edges are necessary. Edges 12 and 67 form a maximal matching. Thus s=2.

In an independent dominating set, within the block {1,2,3,4,5}, choosing 1 requires both leaves of 2, choosing 2 requires leaf 5, and choosing neither requires all three leaves. At least two vertices must be selected, with equality only for {2,5}. Likewise the other block {6,7,8,9,10} requires at least two, with equality only for {7,10}. The only possible set of size at most four is therefore {2,5,7,10}, which fails to dominate 0. The set {1,3,4,7,10} is independent and dominating, so i=5. Consequently i-s=3>2.

## Verification

Run python3 verify.py for exact checks of the witness and seven corona paths. Run python3 verify.py --atlas (requires NetworkX) for tree enumeration. All 200 nonisomorphic trees of orders 2 through 10 have no counterexamples, and exactly one of 235 trees of order 11 is a counterexample. All checks passed locally on 25 November 2026. Minimality is among trees, not all connected graphs. No external peer review or formal proof-assistant verification was performed; no novelty claim is made for the elementary corona identities.
