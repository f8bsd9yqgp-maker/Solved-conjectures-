# Graph Brain alpha upper-055 — Mean distance and squared radius

24 November 2026 (US Central). AI-assisted counterexample note. Source: [Graph Brain issue #421](https://github.com/math1um/objects-invariants-properties/issues/421) and [upper-bound comment](https://github.com/math1um/objects-invariants-properties/issues/421#issuecomment-327846086), posted 2017; ID from the [August 2026 transcription](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graphbrain_open_alpha.json). The author [invariant definitions](https://github.com/math1um/objects-invariants-properties/blob/master/src/Invariants/invariants.sage) were checked: SW is degeneracy plus one and MEEH is the maximum of zero and the number of even-distance vertices minus their induced edge count. The prior [lower sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_lower.md) and [upper sweep](https://github.com/Kuberwastaken/c5-k4/blob/main/results/expansion/graphbrain_upper.md) report these entries as holds in the tested families. A targeted public search did not establish earlier exact resolutions; current mathematical status and discovery priority remain unconfirmed. No independent review or Lean certification. Graphs are finite, simple and connected.

## Statement
α≤10^ceil(average distance)/rad².

## Disproof
For m≥200, start with K_{m,m}, choose a hub h, and attach two internally disjoint three-edge paths starting at h and otherwise disjoint from the core. Denote this graph J_m. Its order is 2m+6 and its degree values are 1,2,m,m+2, so dd=4. Its diameter is six, attained by the two arm endpoints; core vertices are at distance at most five from an endpoint and every other nonendpoint also has eccentricity at most five. Thus the periphery has size two. The hub h has eccentricity three, and the diameter gives radius at least three, so radius is exactly three. The m vertices in the core part opposite h together with the first and third vertices of each arm form an independent set of size m+4. Therefore α≥m+4.

The unordered distance sum within the core is 3m²−2m. There are 12m+15 remaining unordered vertex pairs, each at distance at most six. The total distance sum is at most 3m²+70m+90, which is strictly less than 2 times the number of unordered pairs, (2m+6)(2m+5), because m²−48m−60>0 for m≥200. Average distance is therefore strictly less than two.
The asserted bound is at most 100/9, far smaller than m+4. ∎

[Joint witness verifier](../graphbrain-alpha-lower-037/verify.py): the Python/NetworkX script was executed locally and all ten checks passed. Analytic inequalities bound transcendental terms without relying on floating-point approximations. The family proof establishes the disproof independently of the test.
