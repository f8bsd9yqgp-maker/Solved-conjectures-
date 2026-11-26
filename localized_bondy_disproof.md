# Localizing Bondy's metaconjecture on Hamiltonicity

Source: https://mathoverflow.net/questions/251557/localizing-bondys-metaconjecture-on-hamiltonicity (2016).

## Counterexample to the literal formulation
Let P(H) hold if H has exactly two vertices, or H is complete on at least three vertices. This property is monotone under edge addition on a fixed vertex set.

Every connected locally P graph on at least three vertices is a cycle or a complete graph. Indeed, every vertex has degree at least two. If every degree is two, the graph is a cycle. Otherwise take a vertex v of degree at least three. Its closed neighborhood S is a clique of size at least four. Each u in S has degree at least three, so its neighborhood is complete. If u has a neighbor w outside S, then u is not v, and v and w are both neighbors of u; hence vw is an edge, contradicting w outside S. Thus no edge leaves S, and connectedness implies S is the whole graph.

Both cycles and complete graphs are Hamiltonian. But C_n for every n >= 4 is locally P and is not pancyclic. This disproves the stated implication, even with edge-addition monotonicity.

## Scope and verification
This is an elementary analytical counterexample family, not a numerical search. It addresses the literal universal formulation, not broader versions of Bondy's informal metaconjecture or formulations excluding cycles. Repository-index and targeted literature screening in the preceding research session found no matching resolution, but full file-level screening, independent verification, and publication priority remain unconfirmed. Do not count this as a certified novel discovery until those checks are complete.
