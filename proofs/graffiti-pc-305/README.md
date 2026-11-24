# Graffiti.pc Conjecture 305 — Complement-edge neighborhoods and total domination

24 November 2026. AI-assisted candidate written proof. Independent review, priority and Lean verification pending. The [November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf) lists this entry open; PDF text was accessible but page image retrieval failed. Neither Davis's main results table nor targeted searches revealed a full resolution of this exact entry. This is not proof of originality.

Let G be connected of order n>2 and noncomplete, H its complement, and M=max_{uv∈E(H)} |N_H(u)∪N_H(v)|. We prove γ_t(G)≤ceil(2M/3), using the edge-neighborhood definition in H. For complete graphs this maximum is undefined; assigning zero would make the literal inequality false (γ_t=2).

Choose uv∈E(H) attaining M, put U=N_H(u)∪N_H(v), W=V\U. Both u,v belong to U and are adjacent in G to every vertex in W. If W is empty, the classical connected-graph total domination bound γ_t≤floor(2n/3) suffices.

Otherwise construct G' on U plus a new vertex z, preserving G[U] and joining z to exactly those U vertices adjacent in G to every vertex of W. We show G' is connected. Any component of G[U] containing u or v already contains a neighbor of z. For a component S containing neither, take x∈S. Since there are no G-edges between S and the other components, S⊆N_H(u) and U\S⊆N_H(x). Moreover xu is an H-edge. The union of their H-neighborhoods contains U, and has size at most M=|U| by maximality. Thus it equals U; x has no H-neighbor in W and is a neighbor of z in G'. Every component meets N_{G'}(z), proving connectedness.

Let D' be a minimum total dominating set of G'. It contains a neighbor of z, which is adjacent in G to all W. If z belongs to D', replace it by any w∈W. Every U vertex previously dominated by z is adjacent to w, every U vertex previously dominated by another selected vertex remains dominated, and all W (including w if selected) are dominated by the selected neighbor of z. If z is not selected simply retain D'. In either case obtain a total dominating set of G of size |D'|.

Since |V(G')|=M+1≥3, the classical connected-graph bound gives γ_t(G)≤γ_t(G')≤floor(2(M+1)/3)=ceil(2M/3). ∎

Dependency: Cockayne, Dawes and Hedetniemi's classical total domination bound. Prior computational work mentions #305 but does not provide a resolution in the README (https://github.com/Kuberwastaken/c5-k4). Exact check: all 989 noncomplete connected atlas graphs of order 3–7 passed. Scope: complement edges, not original edges.

[Joint exact finite verifier](../graffiti-pc-208/verify_batch.py). Finite tests are sanity checks, not substitutes for the general argument.
