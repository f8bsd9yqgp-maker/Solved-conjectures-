# Graffiti.pc Conjecture 343 — Annihilation and degree-two components

24 November 2026. AI-assisted written candidate resolution. No Lean verification, independent refereeing or established discovery priority. Source statement: DeLaViña, Written on the Wall II, entry as transcribed in the [6 August 2026 corpus](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), marked open there. The November primary PDF is [here](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf); retrieval of the relevant later page images failed, so the present-day catalogue status and original typography are not independently verified. Neither Davis's current main index nor targeted searches identified an exact full resolution, but this is not an exhaustive priority search.

Let T be a finite tree of order n>2, t its total domination number, a its annihilation number (maximum number of smallest degrees summing to at most n−1), L its leaves, and S its support vertices (neighbors of leaves). Desormeaux, Haynes and Henning, [Relating the annihilation number and the total domination number of a tree](https://doi.org/10.1016/j.dam.2012.09.006), Discrete Applied Mathematics 161 (2013), 349–354, Theorem 1, prove t≤a+1. Their Lemma 10 states that if t=a+1, then the diameter is at least four and S is independent. These are published results, not new claims of this note.

Assume there is at least one degree-two vertex. Let c count the components of the subgraph induced by all degree-two vertices. The claim is t≤a+ceil(c/2). Since c≥1, ceil(c/2)≥1. Apply the published bound t≤a+1. ∎

This is an immediate corollary of existing work; no claim of originality.

## Verification
[Joint exact verifier](../graffiti-pc-348/verify.py): all 985 nonisomorphic trees of orders 3–12 passed every applicable inequality on 24 November 2026. Finite checks supplement the general arguments.
