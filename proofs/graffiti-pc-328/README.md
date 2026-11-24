# Graffiti.pc Conjecture 328 — Counterexample family for matching and K4 incidence

24 November 2026. AI-assisted research note, GPT-6.2. Written disproof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 328, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let f count vertices attaining the maximum number of incident K4 subgraphs. The claim is 4μ(G)≤f implies well total domination.

For integer r≥3 start with path a-b-c-d-e and attach r additional leaves to b. This is a tree of order r+5≥8; the vertex cover {b,d} has size two and the disjoint edges ab,de give a matching of size two. Thus μ=2. All vertices have zero incident K4, so f=r+5≥8=4μ.

The total dominating set D1={b,c,d} is inclusion-minimal: b and d are forced by leaves a,e, and c is needed to dominate both b and d. D2={a,b,d,e} is also inclusion-minimal: b,d are forced, a is the only selected neighbor of b, and e is the only selected neighbor of d. Every vertex is dominated by each set, including c by b or d, and the extra leaves by b. Since their sizes are 3 and 4, the graph is not well total dominated. This disproves the conjecture for infinitely many r. The first graph has 8 vertices. ∎

Prior work: [AI Village summary](https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj309-false-one-hundred-fifty-nine) explicitly records #328 as already disproved by another team. This is a independently derived counterexample family, not a priority claim.
