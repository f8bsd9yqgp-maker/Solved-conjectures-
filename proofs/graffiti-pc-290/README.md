# Graffiti.pc Conjecture 290 — Total domination and the first Havel–Hakimi zero

24 November 2026. AI-assisted candidate written proof. Independent review, priority and Lean verification pending. The [November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf) lists this entry open; PDF text was accessible but page image retrieval failed. Neither Davis's main results table nor targeted searches revealed a full resolution of this exact entry. This is not proof of originality.

Let G be a connected simple graph with n>2, Δ its maximum degree, and k the first Havel–Hakimi iteration whose resulting sequence contains a zero. We prove γ_t(G)≤kΔ.

For iteration i (1≤i≤k), let d_i be the largest residual degree before the step and H_i the number of residual degrees at least 2 at that moment. Prior to step k all entries are positive. At step k at least one selected entry is 1, so at most d_k entries of the pre-step sequence are at least 2: H_k≤d_k.

For i<k, the change H_i−H_{i+1} is at most d_i+1, accounting for the removed entry and decremented degree-2 entries. Assume Δ≥3. If d_i≤Δ−1 this is at most Δ. If d_i=Δ and there is another entry at least 3, at least one of the d_i selected entries is at least 3 and does not drop below 2; the loss is again at most Δ. The only possible exceptional step has d_i=Δ and all other entries at most 2. Its loss is at most Δ+1, and all later maxima are at most 2. There can be at most one such step; the final bound H_k≤d_k≤2 absorbs its excess of one since Δ≥3. Summing gives H_1≤kΔ in either case.

The nonleaf vertices of a connected graph induce a connected graph (a shortest path between nonleaves cannot have an internal leaf). If at least two nonleaves exist, they form a total dominating set, so γ_t≤H_1. If exactly one exists, G is a star and γ_t=2≤Δ. This proves the claim for Δ≥3.

If Δ=2, G is a path or cycle. Each pre-final loss is at most 3, and H_k≤2, hence H_1≤3k−1. There are at most two leaves, so n≤3k+1. The classical Cockayne–Dawes–Hedetniemi bound for connected graphs of order n≥3 gives γ_t≤floor(2n/3)≤2k. This proves the remaining case. ∎

Prior work: the catalogue mentions a 2012 argument for Δ=3,n≥12; an August 25, 2026 report states the k=1 case (https://grok-ai-village-news-496089.gitlab.io/series/wow.html). This note supplies the unrestricted argument; no claim of priority. Exact check: all 994 connected atlas graphs on 3–7 vertices passed.

[Joint exact finite verifier](../graffiti-pc-208/verify_batch.py). Finite tests are sanity checks, not substitutes for the general argument.
