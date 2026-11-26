# Four-world counterexample to Spohn expressibility under belief-contradicting revision

Date: 2026-11-26. AI-assisted proof draft. Status: candidate complete negative answer to the restricted sufficiency question; independent review and research priority pending. This supersedes the earlier additive-cancellation note's limitation involving a confirming update.

Source: Theofanis Aravanis, "Darwiche and Pearl’s Iterated Belief Revision: Not Always Spohn-Expressible", Mathematics 13(6), 933 (2025), https://doi.org/10.3390/math13060933, Sections 3–4, Definitions 6–11, Section 9.

## Theorem

There is a modified AGM revision operator on the four valuations of a two-atom propositional language satisfying R1, R2, the Independence condition (IndR), SPN1 and SPN2 but not Spohn-expressible, even if imitation is tested only on consistent evidence contradicting the current qualitative beliefs. Imitation here permits separate positive firmness parameters for each entire history (terminal belief equality, not online or prefix-consistent numerical imitation). All assertions concern consistent input revisions, as in the restricted problem.

## Operator

Use tagged states S0,S1,S2 and ordinary states carrying strict total orders. Initial order at S0 is 0<1<2<3 (the leftmost world is most plausible). Beliefs are exactly the theory of the first world. The distinguished path is

    S0 -- A={1,2} --> S1: 1<0<2<3
    S1 -- B={2,3} --> S2: 2<3<1<0
    S2 -- C={0,3} --> ordinary: 3<2<1<0
       -- D={0,1} --> ordinary: 1<0<3<2.

At every other transition use stable lexicographic promotion: first list event worlds in their old order, then complement worlds in their old order, and enter an ordinary state. Ordinary states never return to special tags. Tautology uses the same rule (no order change). In particular all four distinguished inputs exclude the previous minimum.

The revised minimum is always the old minimum within the input, giving the modified AGM faithful-preorder representation on consistent inputs. R1 and R2 follow from preservation of each internal order. IndR follows because no input-world previously ahead of a complement-world is subsequently moved behind it; this is immediate for lexicographic updates, and by inspecting A and C for the two nonlexicographic updates. Thus the DP and Independence conditions hold.

## SPN1 and SPN2, globally

Use the source's Definitions 8–11. For any starting state, a pair is biased along an input sequence if its endpoints share membership in each input. The strict nesting edges in Definition 10 point from an inner interval to an enclosing interval with a strictly earlier left endpoint. The indifference relation is identity because every preorder is strict: equality of corresponding endpoints implies identity of unordered pairs. Hence SPN1 holds.

At any starting state, the initial strict nesting graph is acyclic, since every strict containment increases the number of positions spanned. Singleton pairs, if included, can have outgoing strict nesting edges to nonsingleton pairs but cannot be the outer interval in any strict nesting edge. They cannot participate in a directed cycle. It suffices to inspect nonsingleton pairs.

Lexicographic-tail lemma: after any sequence of stable lexicographic promotions, worlds are sorted by their reversed membership signatures, breaking ties by their order before that sequence. Each signature class is contiguous. A pair biased along the full history must lie in a single such class. Two such pairs in distinct classes cannot nest. If they share a class, any strict nesting of their endpoints already held at the beginning of the lexicographic tail. Consequently a history that follows a finite distinguished prefix and then enters ordinary lexicographic states introduces no additional nesting edges beyond those seen at the prefix endpoints. The same holds for an ordinary starting state. This reduces the universal check over histories of arbitrary length to the distinguished prefixes from each tagged root.

At S0 after A, the only biased nonsingleton pairs are {0,3} and {1,2}. They interleave in order 1<0<2<3, so no new nesting. After A,B, the four worlds have distinct membership signatures; no biased nonsingleton pair survives. Nothing further can add edges.

At S1 after B, the only biased nonsingleton pairs are {0,1} and {2,3}; their intervals are disjoint. After B,C all four signatures are distinct, so no such pair survives.

At S2 after C, the only biased nonsingleton pairs are {0,3} and {1,2}. Their new order 3<2<1<0 produces the single additional edge {1,2} -> {0,3}. In the initial order 2<3<1<0, their intervals interleave: {1,2} occupies positions [1,3] and {0,3} occupies positions [2,4]. Neither contains the other. Every directed path of initial strict nesting edges implies strict interval containment, so there is no reverse path from {0,3} to {1,2}. Adding this one edge creates no cycle.

At ordinary states there are only lexicographic transitions, covered by the lemma. Thus every root's graph of strict nesting generators is acyclic, and its transitive closure is asymmetric. SPN2 follows. The argument checks all histories, not merely contradictory ones.

## Terminal-only nonimitability

Any candidate initial integer OCF must have strictly increasing ranks k0<k1<k2<k3. Single-step pair evidence {i,j}, 1<=i<j<=3, is contradictory at S0 and forces ki<kj via the unchanged order within the event. To force k0<k1 without using a confirming query, use the two-step history {2}, {0,1}. Both inputs contradict the successive qualitative minima, and the first input is an ordinary lexicographic transition. Its numerical revision preserves the difference of ranks for 0 and 1 (both outside {2}); the second selects 0 uniquely only if k0<k1. Normalization gives k0=0.

Write x=k2-k1>0 and let d1,d2,d3,d4>0 be arbitrary firmness parameters for A,B,C,D. Spohn conditionalization subtracts the minimum rank in the input from all input ranks, and subtracts the minimum complement rank and adds d from all complement ranks.

After A the ranks of worlds (0,1,2,3) are

    (d1, 0, x, k3+d1).

After B they are

    (d1+d2, d2, 0, k3+d1-x).

Since k3-x>0, put m=min(d2,k3-x)>0. The minimum rank within C={0,3} is d1+m and the complement minimum is 0. After C, world 0 has rank d2-m and world 1 has rank d2+d3. Thus

    rank(1)-rank(0) = d3+m > 0.

Revision by D={0,1} must choose 0 uniquely, irrespective of d4. The qualitative terminal belief instead selects 1 uniquely. This contradiction holds for every choice of positive firmness in this single history, after the contradictory probe histories have forced the initial order. If numerical revision is also required to contradict its own intermediate beliefs, that only further restricts the candidate parameters: the impossibility was established even allowing the broader numerical update operation. QED.

The proof does not assume the firmness parameters used for one history also apply to another.

## Novelty and review

A targeted renewed search of the exact paper title, Aravanis, SPN1/SPN2 and Spohn expressibility located the source paper and no directly matching later resolution. Recursive default-branch tree checks (not exhaustive full-file reviews) on 2026-11-26 returned 415 entries in f8bsd9yqgp-maker/Solved-conjectures- (the only relevant paths were the two earlier notes from this project), 19,108 entries in 1337isnot1337/solved-conjectures (none matching), and 296 in f8bsd9yqgp-maker/Math (none matching). Earlier targeted repository content searches also found no prior matching solution. This does not certify worldwide priority.

No external peer review or proof-assistant certification has yet been performed. The argument is complete for the stated consistent-input setting; keep the independently confirmed solved count unchanged pending external verification. No journal submission.
