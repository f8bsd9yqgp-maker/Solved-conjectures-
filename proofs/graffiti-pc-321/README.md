# Graffiti.pc Conjecture 321 — Average eccentricity versus maximum transmission

24 November 2026. AI-assisted research note, GPT-6.2. Computer-assisted proof. Not independently refereed; not Lean-verified. No novelty or priority claim.

Source: E. DeLaViña, [Written on the Wall II, November 2026 catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 321, marked open in that edition. The current main results index of Cinna Davis's repository lists #318, not this entry. This does not exclude previous work elsewhere.

Let ecc_avg be average vertex eccentricity and T_max be maximum transmission (sum of distances). The claim is that 3 ecc_avg≥T_max implies well total domination.

Let d>0 be the diameter, attained by vertices x,y. For every vertex v the triangle inequality gives dist(x,v)+dist(y,v)≥d. Summing yields T_max≥nd/2. Also ecc_avg≤d. Hence the hypothesis forces n≤6. This reduces the unrestricted conjecture to a finite exact check of all labelled simple graphs on 2–6 vertices.

The accompanying standard-library verifier enumerates every edge subset, rejects disconnected graphs, computes distances by bitmask breadth-first search, then tests 3 sum ecc≥n T_max using integers. It enumerates all vertex subsets and recognizes inclusion-minimal total dominating sets by checking each single-vertex removal (total domination is monotone). Executed 24 November 2026: 27,475 connected labelled graphs, 245 eligible, all 245 have a single minimal-total-domination cardinality. Thus the finite residual cases all pass, completing a computer-assisted proof. ∎

Prior-work caveat: the [AI Village summary](https://grok-ai-village-news-496089.gitlab.io/articles/opus5-wow2-conj309-false-one-hundred-fifty-nine) references earlier work on this group of conjectures.
