# Graffiti.pc Conjecture 361 — Isolated support vertices and tree centers

24 November 2026. AI-assisted written candidate resolution. No Lean verification, independent refereeing or established discovery priority. Source statement: DeLaViña, Written on the Wall II, entry as transcribed in the [6 August 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), marked open there. The November primary PDF is [here](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf); retrieval of the relevant later page images failed, so the present-day catalogue status and original typography are not independently verified. Neither Davis's current main index nor targeted searches identified an exact full resolution, but this is not an exhaustive priority search.

Let T be a finite tree of order n>2, S its support vertices, i the number of isolates in T[S], C the set of center vertices, and t its total domination number. The conjecture states t≥i+|C|.

Every total dominating set contains all support vertices. A tree has either one center or two adjacent centers. If T[S] contains an edge, it has at least two nonisolated support vertices, so t≥|S|≥i+2≥i+|C|.

Otherwise S is independent, so i=|S|. A total dominating set must contain S and at least one additional vertex, because S is nonempty and none of its vertices has a neighbor in S. Thus t≥i+1. If |C|=1 this suffices.

Suppose |C|=2 and t=i+1. Then a minimum total dominating set is S∪{x} for some x outside S, and x must be adjacent to every support vertex. Every leaf is therefore within distance two of x; in a tree, a vertex attaining the maximum distance from x is a leaf. Thus the eccentricity of x is at most two. If S has at least two members, leaves attached to distinct supports have distance four via x, so the diameter is exactly four and the center is unique. If S has one member, the tree is a star, again with a unique center. Both contradict |C|=2. Thus t≥i+2 in the two-center case, completing the proof. ∎

The proof is elementary and self-contained. No earlier exact proof was identified in targeted searches; priority remains unverified.

## Verification
[Joint exact verifier](../graffiti-pc-348/verify.py): all 985 nonisomorphic trees of orders 3–12 passed every applicable inequality on 24 November 2026. Finite checks supplement the general arguments.
