# A constructive linear domatic bound for double-star-free split graphs

Research note, 27 November 2026. AI-assisted candidate proof; independent review and priority confirmation pending.

## Source and scope

Q. Chuet, S. Djelloul, H. La, F. Pirot, H. Zaredehabadi, *A Domatic Analogue of χ-Bounded Graph Classes and the Gyárfás–Sumner Conjecture*, [arXiv:2606.02030v1](https://arxiv.org/abs/2606.02030), 1 June 2026, §8.3, Problem 3. The problem asks whether split graphs excluding an induced balanced double star are DOM-bounded. This answers that problem, not the broader Conjecture 3 for unrestricted graphs.

## Theorem

For every integer r ≥ 1 and every nonempty finite simple split graph G with no induced S_{r,r}, where the double star has r leaves at each of its two adjacent centers,

    dom(G) ≥ max(1, floor((δ(G)+1)/r)).

Here dom is the maximum number of classes in a partition into dominating sets and δ is minimum degree. In particular, the class is DOM-bounded for every r. The result also implies DOM-boundedness for split graphs excluding a fixed unbalanced double star by taking r to be the maximum of its leaf counts.

## Proof

Write V(G)=C ⊔ I, with C a clique and I independent. Let δ=δ(G). If I is empty, G is complete and dom(G)=|C|=δ+1. If δ=0, dom(G)≥1 suffices. Otherwise I is nonempty and |C|≥δ≥1. For u∈C put A_u=N(u)∩I and order C by nonincreasing |A_u|.

**Ordered difference lemma.** If u precedes v, then |A_v\\A_u|≤r−1. Otherwise |A_u\\A_v|≥|A_v\\A_u|≥r. Choosing r elements from each exclusive set together with u,v gives an induced S_{r,r}, a contradiction.

Assume r≥2. Put k=max(1,floor((δ+1)/r)). If k=1 the claim is immediate. Otherwise k≤δ≤|C| and kr≤δ+1. Let T={u_1,...,u_k} be the first k clique vertices; give u_j color j.

Construct a bipartite graph with left vertices (x,j) for x∈I and j∈{1,...,k} such that x is not adjacent to u_j. These are missing-color requests. The right side is C\\T. Join (x,j) to v if x is adjacent to v.

Each left vertex has degree at least δ−k+1 since x has at least δ neighbors in C and misses u_j. Each right vertex v has degree sum_{j=1}^k |A_v\\A_{u_j}| ≤ k(r−1) by the lemma. Since δ−k+1≥k(r−1)>0, every left subset X satisfies

    (δ−k+1)|X| ≤ e(X,N(X)) ≤ k(r−1)|N(X)|.

Thus |N(X)|≥|X| and Hall's theorem yields a matching saturating the left side. Give the distinct right vertex matched to (x,j) color j; color all remaining vertices arbitrarily.

Every clique vertex sees every color in its closed neighborhood because T is a clique subset bearing all colors. Every independent vertex x sees color j either at u_j or at its matched neighbor. Therefore all k color classes dominate G.

For r=1 the lemma implies A_v⊆A_u whenever u precedes v. Every independent vertex has at least δ neighbors, so it is adjacent to the first δ clique vertices. Give these distinct colors 1,...,δ and give every vertex of I color δ+1. If |C|>δ, color the remaining clique vertices δ+1. Then every clique vertex sees all colors in C and every independent vertex sees all colors in its closed neighborhood. If |C|=δ, every independent vertex is adjacent to all of C; each clique vertex sees color δ+1 in nonempty I. This proves the bound. ∎

## Algorithm and verification

Sort the clique vertices, build the missing-color request graph and find a maximum bipartite matching. Given a split partition, this is polynomial time. The mathematical proof is independent of finite testing.

Run `python3 verify.py` using the standard library. The original test run reported 110,783 incidence matrices, including 13,898 with k≥2, without assertion failures. The verifier checks the constructed coloring, not novelty or a formal proof assistant certificate.

## Priority audit

The initial web and arXiv search found no matching resolution. Default-branch code, issue and README searches in both [the competitor repository](https://github.com/1337isnot1337/solved-conjectures) and [this repository](https://github.com/f8bsd9yqgp-maker/Solved-conjectures-) found no matching entry. README blob SHAs at screening were 0659fd4450174e118f8571834b15ce1efc33a6af and 87bf8ec29f860c7d597ef5618ff7ca1b6f95a636 respectively. Follow-up web search did not locate a resolution; MathArena results for this paper concern a different, previously proved cograph bound. Private work, unindexed material and unpublished results are outside the check. Independent review, Lean verification and research priority remain unconfirmed. No author or journal submission is claimed.
