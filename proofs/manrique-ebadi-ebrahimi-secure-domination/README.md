# Manrique–Ebadi–Ebrahimi secure domination conjecture (Conjecture 6.4)

AI-assisted research note, 26 November 2026. Analytical disproof of both inequalities as stated, including a weakly connected infinite family. Independent review and worldwide discovery priority remain unconfirmed.

## Source and screening

S. M. Manrique, I. Ebadi and M. Ebrahimi, *Secure Domination in Digraphs*, arXiv:1503.04048 (2015), Conjecture 6.4: https://arxiv.org/abs/1503.04048 . The paper defines OSODS and ISODS and computes the secure out-domination parameters of directed cycles in Propositions 2.9 and 5.9. The authors' cycle results are prior work and are not claimed as new. Targeted public searches for the title, arXiv identifier, author names, Conjecture 6.4, out-secure out-domination, in-secure out-domination and counterexamples did not reveal an explicit prior resolution. This is not exhaustive worldwide priority certification.

The competitor README (blob 1ddea291bef7620b75639449634d9abdef7e55f2) was retrieved first, then the user's README (blob 9380e7e69d894b71e2eb98c738c80322793e5934). Default-branch searches of both repositories for 1503.04048, secure domination in digraphs, out-secure out-domination, and Manrique Ebadi returned no matches.

## Definitions and original claim

A vertex set S out-dominates D if each v outside S has an incoming arc from a vertex of S. An out-secure out-dominating set (OSODS) additionally requires that each v outside S have an in-neighbor u in S such that (S minus {u}) union {v} is out-dominating. An in-secure out-dominating set (ISODS) requires an out-neighbor u in S with the same swap property. Their minimum cardinalities are gamma_oso and gamma_iso.

Conjecture 6.4 asserts that both parameters are at most ceil(2n/3) whenever the minimum semidegree is at least 1. No strong connectivity assumption is stated. Both inequalities are false even under weak connectivity.

## Theorem

For every positive integer k there exists a weakly connected oriented graph D_k on 4k+3 vertices with minimum semidegree 1 and

    gamma_oso(D_k) = gamma_iso(D_k) = 3k+2.

In particular, both numbers exceed ceil(2n/3) by floor(k/3), so every k>=3 is a counterexample.

## Construction

Start with k vertex-disjoint directed four-cycles C_i=(a_i,b_i,c_i,d_i), with arcs a_i->b_i->c_i->d_i->a_i, and one directed triangle H=(h_0,h_1,h_2), with arcs h_0->h_1->h_2->h_0. Add precisely one arc a_i->h_0 from each four-cycle. There are no other arcs.

Every vertex has positive in-degree and out-degree. Some vertices have both equal to one, so the minimum semidegree is exactly one. The underlying undirected graph is connected. The orientation is not strongly connected; the conjecture does not require strong connectivity.

## Lower bound

Let S be an OSODS or ISODS. Because there are no incoming arcs from outside a peripheral four-cycle, its restriction must out-dominate that directed cycle. It follows that at most two vertices of that cycle are omitted, and if two are omitted then they are opposite.

For OSODS, suppose opposite vertices v and w of some four-cycle are omitted. The only possible defender for v is its predecessor u on that cycle. After swapping u out and v in, the vertex u is outside the new set and its only predecessor w is also outside. Thus u is not dominated, contradiction.

For ISODS, at least one of the two opposite omitted vertices is not a_i. Call it v. It has precisely one out-neighbor u, its successor on the cycle. After swapping u out and v in, the opposite omitted vertex w has its only predecessor u outside the new set, contradiction. Therefore in both cases every four-cycle contributes at least three vertices to S.

At least one vertex of H must be in S because h_1 and h_2 have no external predecessors. If exactly one hub vertex is selected, out-domination of h_1 and h_2 forces it to be h_1: selecting just h_0 leaves h_2 undominated, and selecting just h_2 leaves h_1 undominated.

But with only h_1 selected in H, OSODS security for h_2 forces the defender h_1; the swap leaves h_1 undominated, since h_0 is absent. For ISODS, h_2 has only one out-neighbor h_0, which is not selected, so it has no defender. Thus at least two hub vertices are selected in either case.

Summing these lower bounds gives |S|>=3k+2.

## Upper bound

Select all but one vertex in each directed four-cycle and all but one vertex in the directed triangle. This gives 3k+2 vertices. On each cycle, the omitted vertex has both its predecessor and successor selected. Swapping either one for the omitted vertex leaves exactly one omitted vertex on that cycle, which remains out-dominated by its predecessor. The other cycles are unchanged, and each independently out-dominates itself. Extra arcs between cycles cannot invalidate out-domination.

Consequently this set is both an OSODS and ISODS, giving equality with the lower bound.

Since n=4k+3,

    3k+2 - ceil(2n/3)
      = 3k - ceil(8k/3)
      = floor(k/3).

QED.

## Prior result and disconnected counterexample

The original paper's cycle formulas already imply that the disjoint union of k directed four-cycles has both parameters equal to 3k, by additivity over disjoint components. This immediately contradicts the claimed bound for k>=3. The connected construction above supplies a separate elementary argument and shows that merely adding weak connectivity would not repair the conjecture. Strong connectivity is not addressed by this proof.

## Verification

The included standard-library Python script exhaustively checks all subsets in increasing size until each exact minimum is obtained for k=1,2,3. It also checks weak connectivity, positive semidegree and both security properties of the explicit upper-bound witnesses for k=1,...,100. All checks passed in the executed run recorded in verification.txt. The analytical argument does not depend on computation.

No formal proof-assistant verification or independent peer review has been performed. The original cycle formulas are credited, and the possibility of unindexed prior observations remains open.
