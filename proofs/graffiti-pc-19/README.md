# Graffiti.pc Conjecture 19 — Average eccentricity and local independence

24 November 2026. AI-assisted research note. **Proof reproduction.** Not independently refereed or machine-verified in this repository; no first-discovery claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 19. Checked against the current Davis main results index (only Graffiti.pc #318 listed).

For a nontrivial connected simple graph let b be maximum induced bipartite order, d its diameter, e the average eccentricity, and λ the maximum independence number of an open neighborhood. The conjecture states b≥floor(e+λ).

If e<d, integrality gives floor(e+λ)≤d−1+λ, which is the established WOWII #13 bound (DeLaViña and Waller, 2004, credited in the catalogue). Otherwise e=d, so every vertex has eccentricity d. Choose v maximizing λ, an independent S⊆N(v) of size λ, and a geodesic v=p0,p1,…,pd of length d. The set {p0,p2,…,pd}∪S has size d+λ: no p_i with i≥2 is a neighbor of v. Color p_i by parity of i and all of S by odd parity. The geodesic has no chords, S is independent, and a vertex of S cannot be adjacent to p_i for i≥3 because that would shorten the geodesic from v. All remaining edges respect the coloring. Hence b≥d+λ=e+λ. The singleton case, if included, has right side zero. ∎

Prior work: this argument is a reproduction of the established two-case proof strategy, not a new resolution. See Sadeghi's [July 2026 Lean-verified proof](https://www.preprints.org/manuscript/202607.0114) and [MathWorld](https://mathworld.wolfram.com/InducedBipartiteSubgraphNumber.html). We did not independently replay Lean.
