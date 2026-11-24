# Graffiti.pc Conjecture 365 — Isolated support vertices and degree-two edges

24 November 2026. AI-assisted written candidate resolution. Independent review, Lean verification, and discovery priority remain unconfirmed. Source: E. DeLaViña, [Written on the Wall II](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf); the numbered statements are also available in the [August 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json). No prior complete resolution was identified in targeted searches; this is not an exhaustive priority claim.

Let S be the support vertices (neighbors of leaves), J the isolated vertices of T[S], j=|J|, and A the degree-two vertices. The conjecture is t≥j+|E(T[A])|/3. All support vertices belong to D. Write c for the number of components of T[D], s=|(D∩A)∖J|, and h=|D∩L|, where L is the leaf set. The set J is independent, and every D-component contains at least one vertex not in J, so c≤t−j. Also s+h≤t−j.

Partition the edges of T[A] into three classes. Edges with an endpoint in (D∩A)∖J number at most 2s, since each such vertex has degree two. Of the remaining edges, those having an endpoint in J have their other endpoint outside D (two members of J cannot be adjacent). A degree-two support vertex has a leaf as its other neighbor; this leaf must belong to D to dominate that support vertex. Such edges can be charged injectively to selected leaves, hence number at most h. Finally, an edge with both endpoints outside D must have the other neighbor of each endpoint in D, by total domination. It therefore defines a three-edge path connecting distinct D-components, with two internal vertices outside D. These paths have pairwise disjoint interiors (an outside degree-two vertex cannot have two unselected neighbors). Contracting D-components gives a forest on the c component vertices when these paths are replaced by edges; hence their number is at most c−1.

Thus |E(T[A])|≤2s+h+c−1≤3(t−j)−1, proving the stronger bound t≥j+(|E(T[A])|+1)/3. ∎

The August transcription marks this entry open. The relevant November page image could not be retrieved. Prior finite screens are reported in https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj378-false-one-hundred-sixty-four, but no complete proof was identified there.

## Finite verification
[Joint exact verifier](../graffiti-pc-365/verify.py), executed 24 November 2026: all 985 nonisomorphic trees of orders 3–12 passed the applicable claims; 950 had positive denominators in #380. The written arguments, not the finite tests, establish the unrestricted bounds on the specified domains.
