# Graffiti.pc Conjecture 381 — Isolates in support-vertex neighborhoods

24 November 2026. AI-assisted written candidate resolution. Independent review, Lean verification, and discovery priority remain unconfirmed. Source: E. DeLaViña, [Written on the Wall II](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf); the numbered statements are also available in the [August 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json). No prior complete resolution was identified in targeted searches; this is not an exhaustive priority claim.

Let S be the set of support vertices of T, N(S) the union of their open neighborhoods, q the number of isolated vertices of T[N(S)], and Δ_S=max_{s∈S}deg_T(s). The November catalogue, printed p. 224, marks this entry open. Interpreting Δ(S) as the maximum original-tree degree among support vertices, the conjecture is t≥q/(Δ_S−1). In a connected tree of order greater than two every support has degree at least two, so the denominator is positive.

Let J be the supports isolated in T[S]. Every isolated vertex v in T[N(S)] has a support neighbor s; this s cannot itself belong to N(S), since then v would not be isolated. Thus s∈J, and all q isolates lie in the union of the neighborhoods of J. Every support is forced into D. For each s∈J choose a neighbor y_s∈D, which exists by total domination and lies outside S by isolation of s in T[S]. Let Y={y_s:s∈J}, so |Y|≤t−|S|. The union of the neighborhoods of J is contained in Y∪⋃_{s∈J}(N(s)∖{y_s}). Therefore

q≤|Y|+Σ_{s∈J}(deg(s)−1)≤t−|S|+(Δ_S−1)|J|≤(Δ_S−1)t,

using Δ_S≥2 and |J|≤|S|≤t. ∎

This argument in fact holds for all finite connected simple graphs of order greater than two, with the same original-degree interpretation. The source does not separately define Δ(S) in this entry; an induced-subgraph-degree interpretation would require a different analysis.

## Finite verification
[Joint exact verifier](../graffiti-pc-365/verify.py), executed 24 November 2026: all 985 nonisomorphic trees of orders 3–12 passed the applicable claims; 950 had positive denominators in #380. The written arguments, not the finite tests, establish the unrestricted bounds on the specified domains.
