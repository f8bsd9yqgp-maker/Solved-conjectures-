# Graffiti.pc Conjecture 450 — Dissociation number via private neighbors of low-degree vertices

24 November 2026 (US Central). AI-assisted written mathematical note; independent review and Lean verification remain pending. The statement is from the [August 2026 transcription of Written on the Wall II](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), which lists the entry open. The November 2026 PDF is indexed at https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf, but its later pages could not be retrieved and screenshot requests failed; latest official status is therefore unconfirmed. Davis's main completed table does not list this entry. No discovery priority is claimed.

Let G be a finite simple connected graph of order n>3, S its support vertices, A₂ its degree-two vertices and B={v:deg(v)≤2}=V∖H₃. Write pN(Z) for the number of vertices having exactly one neighbor in Z (including vertices of Z), as in the source glossary. Let α₂ be the largest order of an induced subgraph of maximum degree at most one. The conjecture is α₂≤n−|S|+pN(A₂)+pN(B).

Let D be any dissociation set, with complement W. Call a support counted if it has exactly one neighbor in A₂ or exactly one neighbor in B; the number counted is at most pN(A₂)+pN(B). We injectively charge each uncounted support to a vertex in W.

First, if an uncounted support is not in D, charge it to itself. If an uncounted support in D has at least two pendant neighbors, then at least one of its pendants is outside D (because G[D] has maximum degree one); charge a private omitted pendant. If an uncounted support in D has exactly one pendant neighbor p and p∈W, charge p. The pendant charges are all distinct and disjoint from support charges.

The remaining uncounted supports u are in D with exactly one pendant neighbor p∈D. Since u is uncounted, it must have at least two degree-two neighbors: with no such neighbor, u has exactly one B-neighbor, namely p; with exactly one, it has exactly one A₂-neighbor. All its degree-two neighbors are outside D since u already has selected neighbor p. Such a neighbor w cannot be an uncounted support: any degree-two support in a connected graph of order >3 has exactly one pendant and one other neighbor, so it is counted (if the other neighbor has degree two, it has one A₂-neighbor; otherwise, it has exactly one B-neighbor). Thus these degree-two neighbors are disjoint from previous charges, which are leaves or uncounted supports. Each remaining u has at least two available neighbors, and each degree-two vertex can be adjacent to at most two remaining supports. For any subset R of these supports, counting incidences gives |N(R)∩A₂|≥|R|. Hall's marriage theorem supplies distinct omitted degree-two neighbors for all remaining charges.

This gives |W|≥|S|−pN(A₂)−pN(B). Rearranging and maximizing |D| proves the conjecture. ∎

No earlier exact resolution was identified in targeted searches; earlier work on #446 and #449 was found and those entries are not claimed here. The pN definition is confirmed in the [corpus glossary](https://github.com/Kuberwastaken/c5-k4/blob/main/data/INVARIANT-GLOSSARY.md).

## Verification
[Joint verifier](../graffiti-pc-393a/verify.py) was executed on 24 November 2026 and passed all 994 connected nonisomorphic atlas graphs of orders 3–7 for the 393 entries and general clauses of 412a/b; all 70 eligible bipartite graphs for the bipartite clauses and 412e; all 992 connected graphs of orders 4–7 for 450. Finite tests supplement the written arguments.
