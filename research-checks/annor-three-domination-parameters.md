# Counterexamples to Annor's former three-domination-parameter conjecture

**Status (2026-11-26): valid counterexamples to a withdrawn conjecture; not a new open-problem resolution.** AI-assisted research note. Discovery priority and independent review not established.

## Source and version audit
Dickson Y. B. Annor, *A Note on Inequalities for Three Domination Parameters*, arXiv:2506.03646.
- [v1, 4 June 2025](https://arxiv.org/abs/2506.03646v1), Conjecture 7: gamma_t >= ceil((3 gamma + 2 gamma_c)/6).
- [v2, 14 February 2026](https://arxiv.org/html/2506.03646v2), Conjecture 7: gamma_t >= floor((3 gamma + 2 gamma_c)/6).
- [v3, 5 June 2026](https://arxiv.org/html/2506.03646v3): the conjecture is absent; Theorem 7 instead gives floor((3 gamma + gamma_c)/6) as a lower bound. The counterexamples below do not refute that theorem. The conjecture was removed before this note was derived; the reason and earlier priority are not established.

## Construction and proof
For integer k >= 2 take a path on 4k-2 vertices numbered 0 through 4k-3. Attach one private leaf at each backbone vertex with index congruent to 0 or 1 modulo 4. Call the tree T_k. There are 2k supports and 2k added leaves, hence 6k-2 total vertices.

Every dominating set must meet each of the 2k disjoint leaf-support pairs. The set S of all support vertices dominates the tree: every intermediate backbone vertex is adjacent to a support, and every added leaf is adjacent to its support. Thus gamma(T_k)=2k. Also every support has an adjacent support, so S is totally dominating. Since total dominating sets are dominating, gamma_t(T_k)=2k.

Every connected dominating set of a tree on at least three vertices contains every nonleaf vertex: deleting a nonleaf separates the tree into at least two components, each of which must meet any dominating set omitting that vertex (otherwise a neighbor of the deleted vertex is undominated). Connectivity then forces inclusion of the deleted vertex. All backbone vertices of T_k are nonleaves, and the backbone is a connected dominating set. Therefore gamma_c(T_k)=4k-2.

The conjectured unrounded expression equals (14k-4)/6 = 2k+(k-2)/3. For v1 (ceiling), every k >= 3 violates the bound. For v2 (floor), every k >= 5 violates the bound. At k=5 the tree has 28 vertices, gamma=gamma_t=10 and gamma_c=18. The v2 lower bound is floor((3*10+2*18)/6)=11, exceeding 10.

## Reproducibility
The indexed path and leaf attachments above uniquely specify each witness. The exact parameter values follow from the proof, without computational assumptions.

## Counting policy
Archive as a disproof of historical formulations, not a newly solved open conjecture. No increase in novel-solution count. The June 2026 revision already removed the conjecture.
