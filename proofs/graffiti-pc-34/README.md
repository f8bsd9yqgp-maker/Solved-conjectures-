# Graffiti.pc Conjecture 34 — Longest induced path versus distance averages

24 November 2026. AI-assisted research note. **Counterexample, prior disproof exists.** Not independently refereed or machine-verified in this repository; no first-discovery claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 34. Checked against the current Davis main results index (only Graffiti.pc #318 listed).

Let C be the centers and M the maximum-degree vertices; the conjecture bounds longest induced path order below by ceil(dist_avg(C,V)+dist_avg(M,V)), averaging only nonzero distances.

Take a path p0,…,p10, a clique K22 sharing exactly p0 with the path, and attach twenty vertices b_i to p10. Attach twenty private leaves to each b_i. The resulting graph has 11+21+20+400=452 vertices. Its maximum degree is 22, uniquely at p0 (the other clique vertices, p10 and the b_i have degree 21). The diameter is 13, from a non-p0 clique vertex to a leaf. Every induced path is geodesic: inside the clique it uses at most two vertices, and all connections outside the clique are tree edges, with the only clique exit at p0. Hence the longest induced path has 14 vertices.

The centers are exactly p5 and p6: at p_j the eccentricity is max(j+1,12−j), minimized at j=5,6 with value 7. Off-path vertices have eccentricity greater than 7. The distance sums from p0,p5,p6 respectively are 5096,3076,2678, by summing the clique, path, branching vertices and leaves. Thus dist_avg(M,V)=5096/451 and dist_avg(C,V)=2877/451. Their sum is 7973/451, whose ceiling is 18. Since 14<18, the conjecture is false. ∎

The numerical invariants were checked using NetworkX; the argument is exact. Prior disproof of #34 by a clique-spider family is reported in the [AI Village August 21, 2026 dispatch series](https://grok-ai-village-news-496089.gitlab.io/series/wow.html). Our witness is an independent construction, not a first disproof.
