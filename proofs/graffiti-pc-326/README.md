# Graffiti.pc Conjecture 326 — Degree-two subgraph and matching number

24 November 2026. AI-assisted research note, GPT-6.2. Written proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 326, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let S be the degree-two vertices, μ(G) the maximum matching size. The claim is 3μ(G)≤|E(G[S])| implies well total domination.

Every component of H=G[S] has maximum degree two, so is a path (possibly isolated) or cycle. For a path with at least one edge, its edge count is strictly less than three times its matching number. The same is true for every cycle of length at least four. For a triangle equality holds. Any triangle component in H must be an entire component of G, since its vertices already have degree two within H. By connectedness this forces G=K3.

If G≠K3 and H has edges, summing the strict bounds gives |E(H)|<3μ(H)≤3μ(G). If H has no edges then the hypothesis is also impossible, since G is connected of order greater than one. Thus the only eligible graph is K3, whose minimal total dominating sets are precisely its pairs. ∎

Earlier public work: [AI Village summary](https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj327-false-one-hundred-fifty-seven) explicitly mentions a prior proof/classification of #326. This note is a reproduction/alternative derivation.
