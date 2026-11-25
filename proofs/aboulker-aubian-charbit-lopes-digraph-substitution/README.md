# Counterexample to closure under substitution for dichromatically bounded digraph classes

25 November 2026. AI-assisted candidate disproof of Aboulker, Aubian, Charbit and Lopes, Clique Number of Tournaments, Conjecture 6.2 in the published version (Conjecture 6.1 in the earlier preprint numbering), Electronic Journal of Combinatorics 33(3), P3.56 (2026), https://doi.org/10.37236/12557; https://arxiv.org/abs/2310.04265. Independent review and discovery priority remain unverified. This does not contradict their theorem for tournaments.

## Definitions and claim

For a finite digraph D and a linear order < on its vertices, its backedge graph has an undirected edge uv whenever D contains an arc from the later vertex to the earlier one. The directed clique number omega_d(D) is the minimum of the clique number of the backedge graph over all linear orders. The dichromatic number chi_d(D) is the minimum number of colors needed to partition V(D) into acyclic sets. A class is dichromatically bounded if chi_d(D)<=f(omega_d(D)) for some function f and every member D.

Substituting a digraph for a vertex replaces that vertex by the digraph, with each new vertex inheriting the old vertex's incoming and outgoing adjacency to outside vertices. The conjecture says that closure under substitution preserves dichromatic boundedness.

## Construction of a bounded generating class

For every finite triangle-free simple graph H with a fixed vertex order 1,...,h, form an oriented graph X(H). Its vertices are the original vertices of H and a distinct auxiliary vertex b_ij for each edge ij of H with i<j. Its arcs are exactly j->i, i->b_ij, b_ij->j for each such edge.

The original vertices induce an acyclic digraph (all arcs point towards smaller indices), and auxiliary vertices form an independent set. Therefore chi_d(X(H))<=2. Let C consist of the one-vertex graph and all induced subdigraphs of all X(H) for triangle-free H, with all choices of vertex order. C is hereditary and chi_d-bounded by the constant function 2.

Order X(H) by listing each original vertex i immediately followed by all b_ij with smaller endpoint i, before the next original vertex. The only backward arcs are j->i on the original vertices. Thus its backedge graph is H plus isolated vertices, so omega_d(X(H))<=2. If H has an edge, its corresponding directed triangle implies omega_d>=2: a backedge graph with no edges would give a topological ordering, which is impossible.

## Inductive construction in C's substitution closure

Let D_1 be one vertex. For each k>=1 choose a finite triangle-free graph H_k of ordinary chromatic number k+1; these exist by the classical Mycielski construction starting with K2. Let D_(k+1) be X(H_k) with every auxiliary vertex replaced by a disjoint copy of D_k. This is a finite sequence of allowed substitutions, hence lies in C^subst by induction.

Inductive claim: chi_d(D_k)=k and D_k has an order with a triangle-free backedge graph.

Base k=1 is immediate.

Upper bound: assign all original vertices of H_k one new color, and use the same k other colors in each D_k copy. Original vertices induce an acyclic digraph, and there are no arcs between distinct copies. Every color class is therefore acyclic; chi_d(D_(k+1))<=k+1.

Lower bound: suppose D_(k+1) has a dicoloring with at most k colors. Each copy of D_k, whose dichromatic number equals k by induction, must contain every one of the k colors. If original endpoints i,j of any H_k edge receive the same color c, choose a vertex x of color c in the copy replacing b_ij. The arcs j->i, i->x, x->j form a monochromatic directed triangle, a contradiction. Thus the original vertices would provide a proper k-coloring of H_k, which is impossible. Hence chi_d(D_(k+1))=k+1.

Clique bound: in the order for X(H_k) described above, replace each auxiliary position by its entire D_k copy in the triangle-free backedge order supplied by induction. Every intermodule arc involving a copy is forward, because i precedes the block for b_ij and j follows it. There are no arcs between copies. The backedge graph is exactly the disjoint union of H_k and the backedge graphs of the copies. All are triangle-free, proving omega_d(D_(k+1))<=2. Since a digraph of dichromatic number at least two is not acyclic, its directed clique number is at least two.

Therefore, for every k>=2, omega_d(D_k)=2 and chi_d(D_k)=k. No finite-valued function of the directed clique number can bound the dichromatic number of C^subst. This disproves the stated general digraph conjecture, even for hereditary classes of oriented graphs with dichromatic number at most two.

## Remarks

The proof is entirely combinatorial; no finite computational search is needed. The unbounded sequence is necessary to disprove existence of an arbitrary bounding function. The generating graphs are not tournaments, so the published tournament substitution theorem remains unaffected. The targeted literature search found the tournament theorem and subsequent work on polynomial bounds for tournament substitutions but no earlier disproof of this precise general digraph conjecture; priority is not established.

Mycielski reference: J. Mycielski, Sur le coloriage des graphes, Colloquium Mathematicum 3 (1955), 161–162.
