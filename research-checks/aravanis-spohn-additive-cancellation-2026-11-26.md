# Four-world additive cancellation obstruction to unrestricted Spohn imitation

Date: 2026-11-26. AI-assisted draft; independent review pending.
Source: Theofanis Aravanis, Mathematics 13(6), 933 (2025), https://doi.org/10.3390/math13060933, Definitions 6–11 and Section 9.
Status: Candidate negative answer for the literal all-consistent-input reading of Definition 6. NOT a resolution of the narrower regime in Sections 3–4 in which every input contradicts the current beliefs. No novelty or confirmed-solved claim.

## Construction

Four worlds 0,1,2,3 (two Boolean atoms). Use tagged epistemic states carrying strict total orders, with a distinguished starting state S with order 0<1<2<3. Belief content is the theory of the first world. Every nonempty event is revised by stable lexicographic promotion (all event worlds first, maintaining both internal orders) except for two transitions from S:

- A={0,1}: successor order 0<2<3<1.
- B={1,3}: successor order 1<0<2<3.

All successors are tagged as ordinary states, never returning to the distinguished state S. Tautologies preserve the order. Work on the consistent-input fragment, as in the paper; contradictory formulas are not part of the numerical conditionalization considered here.

All transitions preserve the internal order in the event and its complement (R1,R2), and their minimum is exactly the old minimum restricted to the event. Hence the faithful preorder criterion for modified AGM holds for consistent inputs.

## SPN1 and SPN2

Use Definitions 8–11 of the paper. A pair is biased along a history when its two endpoints are on the same side of every input split. All orders are strict, so the indifference-distance equivalence on unordered pairs (including singletons) is identity: endpoint ties between different worlds never occur. Consequently SPN1 follows immediately from Definition 11.

For SPN2 it is enough to assign an auxiliary scalar to each pair so that every generating strict-distance relation from Definition 10 strictly increases that scalar. This scalar is not asserted to be an additive rank distance. At S use

    singleton: 0
    {2,3}: 1
    {0,1}, {1,2}: 2
    {0,2}: 3
    {1,3}: 4
    {0,3}: 5.

Each properly nested interval in the initial order has smaller scalar than its enclosing interval (including any nesting with the right endpoints shared, as in Definition 10).

For any all-lexicographic history, pairs that are biased have endpoints in a common membership-signature class. Lexicographic updates order those signature classes as disjoint contiguous blocks, preserving the original order within a class. Thus two biased non-singleton pairs that exhibit strict nesting must be in the same class, and the nesting already held in the starting order. Singleton comparisons introduce no obstruction: any strict nesting with a singleton as the inner pair increases the scalar, and a singleton cannot be the outer pair of a strict nesting.

For a history from S starting with A or B, the only possible biased non-singleton pairs after the first split are the two complementary two-world sets. Subsequent lexicographic updates either preserve their relative interleaving (if all four endpoints remain in the same later membership-signature class) or separate them, or destroy the bias condition. The only new strict nesting for A is {2,3} inside {0,1}; for B it is {0,2} inside {1,3}. Both increase the scalar given above. Tautologies at S do not affect the argument, whether they preserve the distinguished tag or end it. Hence every generating edge, and every nonidentity edge in its transitive closure, strictly increases the scalar. SPN2 follows.

At every ordinary state, all transitions are lexicographic. The same membership-signature argument applies using ordinary integer rank distances in its starting strict order as the auxiliary scalar. Thus SPN1 and SPN2 hold at all states.

## Failure of imitation even with history-specific firmness

Suppose a common OCF k imitates the operator at S under Definition 6, allowing separate firmness choices for every history. Single-step pair events force k0<k1<k2<k3 (and the initial zero rank at 0). Put x=k1-k0 and z=k3-k2.

History 1: first A={0,1}, then C={1,3}. The qualitative terminal minimum is 3. After the first numerical revision with any d>0, the ranks of 1 and 3 are respectively x and z+d. The second conditionalization chooses the smallest pre-update rank within C, regardless of its firmness. To reproduce the unique terminal world 3 requires z+d<x. Hence z<x.

History 2: first B={1,3}, then D={2,3}. The qualitative terminal minimum is 2. After the first numerical revision with any e>0, ranks of 2 and 3 are respectively k2-k0+e and k3-k1. The second conditionalization chooses world 2 uniquely only if k2-k0+e<k3-k1, i.e. x+e<z. Hence x<z.

Contradiction. No common initial OCF exists even when each history is allowed independent positive firmness choices. This proof does not rely on inferring a common numerical representation of a successor preorder from separate continuations.

## Interpretation and limitation

The argument is a candidate negative resolution of the conjunction R1, R2, SPN1, SPN2 for Definition 6 literally applied to all nonempty proper evidence events. The first A update, however, is already believed at S, and its exceptional transition violates independence for that confirming update. Sections 3–4 expressly focus on the narrower case in which input contradicts current beliefs. The first history is outside that narrower restriction; no conclusion about sufficiency within that regime follows. The same qualification applies to the paper's own derivation of independence using contradictory evidence. The counterexample is not a confirmed solution of the intended restricted research question.

No external submission or independent peer review. Earlier repository checks found no matching Aravanis/Spohn path; priority of this new construction has not been comprehensively established. Keep the confirmed solved count unchanged.
