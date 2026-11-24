# Graffiti.pc Conjecture 235 — Periphery and total domination in bipartite graphs

24 November 2026. AI-assisted candidate written proof. Independent review, priority and Lean verification pending. The [November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf) lists this entry open; PDF text was accessible but page image retrieval failed. Neither Davis's main results table nor targeted searches revealed a full resolution of this exact entry. This is not proof of originality.

Let G be connected of order at least two, B its peripheral vertices (maximum eccentricity), e=max_v dist(v,B), and t=γ_t(G). The claim is t≥2e/3+1 if G is bipartite, and t≥2e/3 otherwise. Take e=0 if B=V (the natural distance-to-set extension).

Henning and Yeo (2014), DOI https://doi.org/10.1016/j.dam.2014.03.013, prove t≥(3e+2)/4. This directly covers the nonbipartite case. For bipartite G it covers e≥6 by comparison, and e=0,1,3,4,5 by t≥2 and integrality. Only e=2 and t=2 remains.

A total dominating pair is an edge uv. In the bipartition A,C with u∈A, v∈C, u is adjacent to all of C and v to all of A, hence diameter≤3. If diameter≤2, G is complete bipartite: every opposite-side pair has odd distance at most 2 and therefore is adjacent. In this case e≤1, including stars. If diameter=3, both parts contain peripheral vertices, namely the endpoints of a diametral pair. A nonperipheral vertex has eccentricity at most 2, so it is adjacent to every vertex of the opposite part (odd distance at most 2). In particular it is adjacent to a peripheral vertex. Again e≤1. Thus e=2,t=2 is impossible, proving the claim. ∎

This proof is a corollary of the stronger published bound used to solve WOW II #233, with a separate bipartite exceptional-case argument. No claim of novelty for that theorem. Exact check: 995 connected atlas graphs of order 2–7 passed.

[Joint exact finite verifier](../graffiti-pc-208/verify_batch.py). Finite tests are sanity checks, not substitutes for the general argument.
