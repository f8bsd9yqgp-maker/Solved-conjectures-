# Graffiti.pc Conjecture 208 — Matching number and Hamiltonian paths

24 November 2026. AI-assisted candidate written proof. Independent review, priority and Lean verification pending. The [November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf) lists this entry open; PDF text was accessible but page image retrieval failed. Neither Davis's main results table nor targeted searches revealed a full resolution of this exact entry. This is not proof of originality.

Let G be a connected simple graph of order n>1, m=|E(complement G)| and μ its matching number. The hypothesis is 2m+3≤6μ. We prove G has a Hamiltonian path.

Adjoin one universal vertex to obtain H on n+1 vertices. A Hamiltonian cycle of H is equivalent to a Hamiltonian path of G. Suppose none exists. By Chvátal's degree criterion (1972), for some integer i with 1≤i<(n+1)/2, the ordered degrees of H satisfy d_i(H)≤i and d_{n+1−i}(H)≤n−i. The corresponding degrees of G are at most i−1 for its first i entries and at most n−i−1 for its first n+1−i entries. Connectedness gives i≥2. Counting missing degrees yields

2m≥i(n−i)+(n+1−2i)i=i(2n+1−3i).

Write k=floor(n/2). The hypothesis implies m≤3k−3/2. The concave quadratic i(2n+1−3i)/2 is minimized on 2≤i≤k at an endpoint. At i=2 it is 2n−5; at i=k it is k(k+1)/2 for even n and k(k+3)/2 for odd n. Both exceed 3k−3/2 for n≥9 and also for n=5,7. Orders 2 and 3 are trivial.

For n=4 the only possible i=2 forces three leaves; G is a star, contradicting the premise (m=3, μ=1).

For n=6 we have m≤7. If i=2, the bound gives m≥7, so equality forces degree sequence (1,1,3,3,3,5). Both leaves are adjacent to the universal vertex, so μ≤2, contrary to the premise. If i=3, four vertices S have degree at most 2. Let x,y,z be counts of missing edges within S, crossing S, and outside S. Then 2x+y≥12 and x+y+z≤7, hence x≥5. If x=6, S is independent, so μ≤2, inconsistent with m≥6. If x=5, y=2 and z=0. There is just one G-edge pq within S; each of p,q has at most one neighbor outside S, so each misses exactly one crossing edge. The other two vertices a,b of S are adjacent to both outside vertices u,v. Choose u adjacent to q. Then p,q,u,a,v,b is a Hamiltonian path, contradiction.

For n=8, the bound eliminates i=2 and 3. For i=4 it gives m≥10, and the premise gives m≤10. Exactly five vertices have missing degree 4 and the other three have missing degree 0. Thus the five form an independent set, so μ≤3; this contradicts m=10 and the premise. All cases are exhausted. ∎

Dependency: V. Chvátal, On Hamilton's ideals (1972), degree sequence criterion; see https://www.cs.bme.hu/~szeszler/newchvatal.pdf. The catalogue records that the proposed hypothesis does not directly imply Chvátal's condition; the small exceptional orders above are essential to this approach. Exact atlas check: all 235 eligible connected graphs on 2–7 vertices have a Hamiltonian path.

[Joint exact finite verifier](../graffiti-pc-208/verify_batch.py). Finite tests are sanity checks, not substitutes for the general argument.
