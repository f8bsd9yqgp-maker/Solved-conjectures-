# Graffiti.pc Conjecture 320 — Even-distance count and minimum transmission

24 November 2026. AI-assisted research note, GPT-6.2. Written proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 320, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Write E(v) for the number of vertices at even distance from v (including v), and T(v) for the sum of distances to all vertices. The claim is that max E(v)=min T(v) implies G is well total dominated.

For every connected graph of order n>1, max E≤n−1 since every vertex has a neighbor; min T≥n−1 since every other vertex is at positive distance. Equality of the two extrema therefore implies both equal n−1. There is a universal vertex u (a vertex of transmission n−1) and a degree-one vertex w (one odd-distance vertex, hence just one neighbor). That unique neighbor must be u. Every total dominating set must include u, and then must include another vertex to dominate u. Conversely u together with any other vertex totally dominates. All minimal total dominating sets have size two. ∎

The [AI Village summary](https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj309-false-one-hundred-fifty-nine) refers to previous work on this and related entries. No priority is claimed.
