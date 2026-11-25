# Delayed amnesiac flooding: explicit nontermination certificates

Walter Hussak and Amitabh Trehan, Termination of amnesiac flooding, Distributed Computing (2023), DOI https://doi.org/10.1007/s00446-023-00448-y, Sections 4.2 and 5, Open Problems 2 and 5. AI-assisted candidate answers dated 25 November 2026. Exact finite-state computations; independent review and novelty verification pending.

## Model and exact recurrence

At time zero each initiating vertex sends to every neighbor. A directed transmission (u,v,r) in state T has r>=1 ticks remaining before reception; each directed edge has fixed positive integer transit time d(u,v)=d(v,u). To update, decrement r for r>1, gather all arriving messages (r=1) by destination, and for each destination with at least one arrival send to every neighbor except those from which it received in that tick. Newly sent messages enter the next state with their full edge transit time. Crossing messages in transit do not cancel: the source paper distinguishes intermediate tick positions from actual vertices, and its Theorem 4.3 proof allows cancellation only at actual vertices. Distinct messages with identical remaining time on the same oriented edge can be represented as one, since the protocol only uses sender sets. A nonempty repeating state certifies indefinite flooding. The numbering here starts with the state just after initial sends, so it differs by a harmless round-index shift from the paper.

## Open Problem 2: a negative answer

The paper asks whether multiple-source flooding always terminates on a bipartite graph with exactly one fixed-delay edge. Let the graph be the cycle 0-1-2-3-0. Edge 0-1 has transit time 2 in both directions; all other edges have transit time 1. Initiators {0,1,2}. Exact states (each triple is sender, recipient, remaining ticks):

    T0: (0,1,2) (0,3,1) (1,0,2) (1,2,1) (2,1,1) (2,3,1)
    T1: (0,1,1) (1,0,1) (1,0,2) (2,3,1)
    T2: (0,3,1) (1,0,1) (1,2,1) (3,0,1)
    T3: (2,3,1) (3,2,1)
    T4: (2,1,1) (3,0,1)
    T5: (0,1,2) (1,0,2)
    T6: (0,1,1) (1,0,1)
    T7: (0,3,1) (1,2,1)
    T8=T3.

Thus the cycle repeats every five ticks. This is a negative answer to Open Problem 2 under the stated model.

### Consequence: candidate correction to published Theorem 4.3

The very same example also refutes the claimed weighted-cycle termination theorem; it is not counted as a separate conjecture. In its proof the authors define a relation on initial nodes using meeting positions of clockwise and anticlockwise waves, and assert transitivity. In our cycle the expanded positions mod 5 have real vertices at {0,2,3,4} and a tick node at 1. The three sources occupy positions 0,2,3. The relation a~b holds iff 2m=b-a mod 5 and a+m is a real vertex. We have 0~3 (m=4, meeting position 4), 3~2 (m=2, position 0), but not 0~2 (the unique solution m=1 meets at tick position 1). Thus the asserted equivalence relation is not transitive, pinpointing the proof gap.

## Open Problem 5: a negative answer for the proposed Cartesian cylinder grids

Take C4 Cartesian product P2 (the cube). Label (i,j) by 2i+j; edges connect equal j in consecutive cyclic layers, or equal i and distinct j. The two edges {0,2} and {0,6} have transit time 2; all others have transit time 1. Initiators {0,3}. Exact recurrence gives T8=T13, with T8={(0,2,2),(0,6,2),(2,0,2),(2,4,1),(5,4,1),(6,0,2),(6,4,1)}. Nontermination follows. This also answers negatively the variant allowing an acyclic factor, since P2 is a tree.

If the product notation is read as the categorical/tensor product rather than Cartesian, there is also a counterexample: C3 tensor P3 (label (i,j) by 3i+j), delayed edges {0,4} of transit time 2 and {0,7} of transit time 3, initiators {0,1}, with T3=T10.

For Cartesian tori, C4 Cartesian C4 (label 4i+j), initiators {10,12,3,5,14,4,9}, delayed edges {0,3}:2, {7,11}:2, {0,1}:2, {0,12}:3, {6,7}:3 yield T10=T28. These are variants of the same open problem and not additional independent conjectures.

## Standard-library verifier

```python
def trace(n,edges,S,delays,horizon):
    N={u:set() for u in range(n)}
    for u,v in edges:
        N[u].add(v); N[v].add(u)
    def d(u,v): return delays.get(tuple(sorted((u,v))),1)
    st=frozenset((u,v,d(u,v)) for u in S for v in N[u])
    history=[st]
    for _ in range(horizon):
        arrivals={}
        nxt=set()
        for u,v,r in st:
            if r==1: arrivals.setdefault(v,set()).add(u)
            else: nxt.add((u,v,r-1))
        for v,orig in arrivals.items():
            for w in N[v]-orig: nxt.add((v,w,d(v,w)))
        st=frozenset(nxt)
        history.append(st)
    return history

def cart_cycle_path(a,b,wrap_second=False):
    E=set()
    for i in range(a):
        for j in range(b):
            u=i*b+j
            E.add(tuple(sorted((u,((i+1)%a)*b+j))))
            if j+1<b or wrap_second:
                E.add(tuple(sorted((u,i*b+(j+1)%b))))
    return E

H=trace(4,[(0,1),(1,2),(2,3),(0,3)],{0,1,2},{(0,1):2},8)
assert H[3] and H[3]==H[8]
assert H[3]==frozenset({(2,3,1),(3,2,1)})
H=trace(8,cart_cycle_path(4,2),{0,3},{(0,2):2,(0,6):2},13)
assert H[8] and H[8]==H[13]
assert H[8]==frozenset({(0,2,2),(0,6,2),(2,0,2),(2,4,1),(5,4,1),(6,0,2),(6,4,1)})
E={(u,v) for u in range(9) for v in range(u+1,9)
   if (u//3-v//3)%3 in (1,2) and abs(u%3-v%3)==1}
H=trace(9,E,{0,1},{(0,4):2,(0,7):3},10)
assert H[3] and H[3]==H[10]
H=trace(16,cart_cycle_path(4,4,True),{10,12,3,5,14,4,9},
        {(0,3):2,(7,11):2,(0,1):2,(0,12):3,(6,7):3},28)
assert H[10] and H[10]==H[28]
print("All four nontermination certificates passed")
```

The cases were reproduced with exact integer-state simulation. Targeted literature search did not establish an earlier correction; discovery priority remains unverified. The fixed-delay assumptions and paper's meaning of graph product should be confirmed with the authors before claiming publication-level resolution.
