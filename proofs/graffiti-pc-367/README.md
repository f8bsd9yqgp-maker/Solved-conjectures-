# Graffiti.pc Conjecture 367 — Degree-two mode and number of distinct degrees

24 November 2026. AI-assisted candidate resolution, not independently refereed or Lean-verified. Original problem numbers and statements are from E. DeLaViña's Written on the Wall II, as recorded in the [August 6, 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json). The current primary catalogue PDF could not be retrieved (HTTP 404); thus the current official status is not established. Targeted literature searches found no exact prior full resolution of these five entries, but priority is unverified. The current Davis completed index does not list any of them.

Source cross-check: [Graffiti.pc on the Total Domination Number of a Tree, Conjecture 6, p.12](https://math1um.github.io/Research/r05.pdf#page=12), page image inspected. The conjecture is γ_t(T)≥(4/3)dd(T) when degree two is the most frequently occurring degree. We prove the unique-mode reading and give a counterexample to the inclusive-tie reading.

Let t=γ_t(T), D a minimum total dominating set, c the number of components of T[D], and U=V∖D. All components of T[D] have at least two vertices, so c≤floor(t/2). Contract them to vertices. Write a(u) for the number of neighbors of u∈U in D and e_U=|E(T[U])|. Each a(u)≥1, and acyclicity ensures at most one neighbor per D-component. Edge counting in the contracted tree gives Σ(a(u)−1)+e_U=c−1. Consequently Σ_{u∈U}(deg(u)−1)=c−1+e_U≤2(c−1). Every nonleaf outside D contributes at least one, so the number h of all nonleaves is at most t+2 floor(t/2)−2.

Let k be the number of distinct degrees greater than two. Under the unique-mode assumption the number n2 of degree-two vertices exceeds the number l of leaves. The tree degree-sum identity gives l=2+Σ_{deg(v)≥3}(deg(v)−2)≥2+k(k+1)/2, since the k distinct positive excesses have sum at least 1+…+k. Hence h≥n2+k≥3+k(k+1)/2+k. Also dd=k+2.

If k=0, the tree is a path of order at least five, and t≥3 by the bound on h. If k=1, h≥5 implies t≥4. If k=2, h≥8 excludes t≤5, because t+2 floor(t/2)−2≤7 for those values. Thus t≥6. These three cases give 3t≥4(k+2). If k≥3, then h≤2t−2 implies t≥(k²+3k+10)/4≥4(k+2)/3, since 3k²−7k−2≥0 for k≥3. This proves the unique-mode case. ∎

If the hypothesis allows ties, P4 is a counterexample: degrees 1 and 2 each occur twice, dd=2 and γ_t=2<8/3. Thus the two natural interpretations are resolved separately. The corpus glossary notes that mode_min and mode_max distinguish ties; this conjecture does not specify which tie convention is intended.

## Exact finite checks
[Joint verifier](../graffiti-pc-379/verify.py), run 24 November 2026: 985 trees of orders 3–12 for #362 and #379; 148 unique-degree-two-mode trees for #367; 456 connected diameter-at-most-two atlas graphs for #416; and 992 connected atlas graphs of order 4–7 for #423. All applicable checks passed. These are sanity checks, not substitutes for the written proofs.
