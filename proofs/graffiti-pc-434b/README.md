# Graffiti.pc Conjecture 434b — Independent domination and minimum degree of maximum-degree subgraph

24 November 2026 (US Central). AI-assisted candidate proof, not independently refereed or Lean-verified. Statement from [the August 2026 WOW II transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), listed open there. The November primary PDF returned an error on direct retrieval and the available extracted text ends at #341; later-page status is not established. The current Davis completed index does not list this result. Targeted searches did not identify an exact earlier complete resolution, but discovery priority is not established.

Let F be a nonempty finite graph of degeneracy d (maximum minimum degree over nonempty subgraphs), all of whose maximal cliques have size d+1. Every vertex belongs to such a clique, so its degree is at least d. Degeneracy then guarantees minimum degree exactly d. We prove: if its set L of degree-d vertices is a clique, then F=K_(d+1).

Use induction on |V(F)|. For each x∈L, N_F[x] is a clique Q of size d+1, since x has degree d and belongs to a maximal clique of size d+1. The closed neighborhoods of adjacent degree-d vertices coincide: each is a clique of size d+1 containing the other vertex, and that other's degree is d. Thus all members of L have the same Q. If F=Q, done.

Otherwise consider F'=F−L. Vertices outside Q have no neighbor in L, so their degrees remain >d. Each v∈Q∖L has degree >d in F and hence an outside-Q neighbor z. The edge vz lies in a maximal clique of size d+1, which avoids L since no member of L is adjacent to z. Thus v has degree at least d in F'. The graph F' is nonempty (there is an outside-Q vertex) and d-degenerate. Some vertex y has degree exactly d in F', necessarily in Q∖L. Its clique of size d+1 in F' just constructed equals N_F'[y] and contains Q∖L. Every clique of F' is contained in an original maximal clique of F; if this original maximal clique meets L it is Q and its surviving vertices lie in N_F'[y], and otherwise the original maximal clique survives intact. Consequently every maximal clique of F' has size d+1. Moreover its degree-d vertices lie within the clique Q∖L. By induction F' is K_(d+1). But a vertex outside Q had degree >d unchanged, impossible. This proves the lemma. ∎

Now let G be a connected graph of order n>3, F its complement, d=SW(F) its degeneracy, M the maximum-degree vertices of G (minimum-degree vertices of F), and i the independent domination number. Maximal independent sets of G are maximal cliques of F, so i≤d+1. Moreover i≤δ(F)+1 by extending a minimum-degree vertex of F to a maximal clique. If i=d+1, then all maximal cliques of F have size exactly d+1 and δ(F)=d. The lemma therefore applies if M forms a clique in F. Since F complete would make G edgeless, M cannot be a clique in F in this equality case. In particular, if G[M] has an isolated vertex x, then x is adjacent in F to all other M vertices; N_F[x] is a clique of size d+1, forcing all M to form a clique in F. Thus

i≤d whenever δ(G[M])=0.

This stronger implication is the key shared result.

The conjecture asserts i≤δ(G[M])+1+d and improves the bound by one when diameter exceeds two. In fact the improved bound holds without the diameter condition: if δ(G[M])≥1, then i≤d+1≤d+δ(G[M]); if δ(G[M])=0, the shared result gives i≤d. ∎

A prior report on the disproof of sibling #434c mentions finite checks of #434a and #434b, but no full proof of those two in that report: https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow-conj434c-false-eighty-seven.html.

[Joint exact verifier](../graffiti-pc-372/verify.py). Graph checks executed on 994 connected atlas graphs of order 3–7 (#410a/b), and 992 of order 4–7 (#432b/#434a/b). The tree check independently passed 975 eligible trees. Finite evidence supplements the written arguments, not formal certification.
