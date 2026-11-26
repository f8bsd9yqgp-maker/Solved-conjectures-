# A finite-history integer-feasibility criterion for Spohn expressibility

Date: 2026-11-26. AI-assisted research note.
Status: **Partial progress only. Original open problem not solved.** Do not count this as a confirmed solved conjecture.

## Source and question

Theofanis Aravanis, *Darwiche and Pearl’s Iterated Belief Revision: Not Always Spohn-Expressible*, Mathematics 13(6), 933 (2025), https://doi.org/10.3390/math13060933 . Section 9 asks whether conditions R1, R2, SPN1 and SPN2 suffice for Spohn expressibility. Definition 6 quantifies over finite evidence sequences and allows a separate choice of positive integer firmness parameters for each sequence; the stated equality is of the terminal belief content. The following result respects that quantifier order. It does not settle the sufficiency question.

## Setup

Let W be a finite set of possible worlds. A regular integer ranking k:W -> nonnegative integers has minimum zero. A nonempty proper evidence event A and positive integer firmness d induce Spohn conditionalization

    k'(w) = k(w) - min_{v in A} k(v)                 if w in A,
    k'(w) = k(w) - min_{v notin A} k(v) + d           otherwise.

The belief content corresponds to the set of worlds attaining rank zero. Tautological inputs may be omitted on the numeric side; contradictory inputs are excluded here. Any intended restriction on surprising inputs should be enforced on the tested qualitative histories. We use finite regular ranks, the finite-world setting and the above revision rule.

## Theorem 1: Exact criterion for a finite history

Fix an initial rank k, a history of nonempty proper events A_1,...,A_m, and a nonempty desired terminal set M. Define integer variables s_i and unnormalized ranks

    x_0(w) = k(w),
    x_i(w) = k(w) + sum_{j=1}^i s_j 1_{w notin A_j}.

The terminal set M is attainable by Spohn conditionalization along the specified history if and only if there exist choices a_i in A_i and integer s_i satisfying the following finite disjunction of systems of linear equalities and inequalities:

    x_i(v) >= x_i(a_i)       for v in A_i,
    x_i(v) >= x_i(a_i)+1     for v notin A_i,

for all i, and, for an arbitrary fixed m0 in M,

    x_m(w) = x_m(m0)         for w in M,
    x_m(w) >= x_m(m0)+1      for w notin M.

If one seeks the stronger prefix-matching property, impose the same terminal equalities and inequalities at each prefix using the desired prefix minimizer set. That is a separate requirement from the literal terminal-only Definition 6.

### Proof

Forward: at step i, put

    s_i = min_{A_i} x_(i-1) - min_{W\A_i} x_(i-1) + d_i.

Adding s_i to the complement while leaving the event unchanged differs from Spohn conditionalization only by a common additive normalization. Choose a_i minimizing x_i within A_i. Since d_i is an integer >=1, every complement world has rank at least x_i(a_i)+1. The minimizer constraints are exactly the stated terminal inequalities.

Reverse: if the inequalities hold, set

    d_i = min_{W\A_i} x_i - min_{A_i} x_i.

Each d_i is a positive integer. Normalizing x_i by its global minimum reproduces the conditionalization of normalized x_(i-1) with firmness d_i, by direct substitution in the two cases w in A_i and w notin A_i. Induction yields precisely M as the terminal belief worlds. QED.

## Theorem 2: Finite-batch feasibility with a shared initial rank

Given finitely many qualitative histories at a starting state S, introduce a common initial vector k, distinct shift variables for each history, and constraints from Theorem 1. Choose a fixed initial zero-rank world from the belief models of S, impose nonnegative initial ranks, and require exactly those belief models to have zero rank. One can additionally impose any desired initial total preorder via equality and strict ordering inequalities.

A shared integer ranking realizes this finite batch exactly when at least one of the finitely many disjunctive linear systems is feasible over the rationals. Indeed, a rational solution can be multiplied by a common positive integer denominator: homogeneous equalities and weak inequalities are unchanged, and margins >=1 remain >=1. This yields integer initial ranks and shifts. The reverse direction is immediate. Ordinary rational linear-programming feasibility can therefore decide each branch of the finite-batch problem. This rescaling argument does not apply if the initial integer rank is held numerically fixed.

A finite infeasible batch, without imposing stronger-than-required preorder or prefix constraints, is a certificate that the operator cannot be Spohn-expressible at S.

## Quantifier limitation

The original definition requires a single initial integer ranking k for every finite history, not a possibly different k for each finite batch. Finite-batch feasibility alone cannot justify exchanging these quantifiers. Moreover, equality of terminal beliefs for every individual history is not by itself a guarantee that one choice of firmness parameters for a prefix reproduces the entire qualitative preorder at that prefix simultaneously for every possible continuation. The stronger online and prefix-consistent representations require separate proof.

## Original problem status

It remains to show that R1, R2, SPN1 and SPN2 imply the existence of the required common initial ranking, or construct a revision operator satisfying all four conditions whose histories violate feasibility. No such proof or certified counterexample was obtained in this run.

## Search and repository audit

Targeted public literature searches for Aravanis, Spohn expressibility, the sufficiency question, and ranking-function linear constraints found the source paper and related representation-theory literature, but no directly matching resolution. This is not a comprehensive novelty certification; the feasibility criterion itself may be a known reformulation of conditionalization.

Recursive default-branch tree checks found no matching path for Aravanis, Spohn, Darwiche or belief revision in:
- f8bsd9yqgp-maker/Solved-conjectures- (413 entries at inspection)
- 1337isnot1337/solved-conjectures (19,108 entries)
- f8bsd9yqgp-maker/Math (296 entries)

Targeted code searches for Spohn-expressible, Aravanis and SPN1 returned no hits. These checks are not full-content inspections of every file.

No peer review, formal verification, or journal submission. The confirmed solved count must remain unchanged.
