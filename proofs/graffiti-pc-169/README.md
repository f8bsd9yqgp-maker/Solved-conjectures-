# Graffiti.pc Conjecture 169 — even-distance variation and spanning-tree leaves

24 November 2026. AI-assisted written proof (GPT-6.2). Independent review, publication priority and Lean verification pending.

## Statement
E. DeLaViña, *Written on the Wall II*, Conjecture 169, announced 8 August 2005, marked open in the [November 2026 catalogue, p. 97](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf#page=97).

For a finite simple connected graph G, let E(v) count vertices at even distance from v (including v), and L=L_s(G) be the maximum number of degree-one vertices of a spanning tree. The conjecture states L ≥ 1+max E(v)−min E(v).

## Theorem and proof
The inequality holds for every finite simple connected graph with n≥2 vertices. For an arbitrary root v choose a breadth-first spanning tree T. The two parts A,B of its bipartition consist of vertices at even and odd graph distance from v, respectively, so |A|=E(v) and |B|=n−E(v).

Let ℓ_A and ℓ_B be the numbers of leaves of T in A and B. Every edge joins the parts, so the sum of tree degrees over either part is n−1. All vertices have positive degree, and nonleaves have degree at least two. Consequently n−1≥2|A|−ℓ_A and n−1≥2|B|−ℓ_B. Since ℓ_A,ℓ_B≤L, we obtain

(n−L+1)/2 ≤ E(v) ≤ (n+L−1)/2.

These bounds apply for every root. Subtracting gives max E−min E≤L−1, as desired. ∎

The proof actually shows that the maximum leaf count among the breadth-first trees obtained by choosing one tree for each root is sufficient.

## Sharpness and edge case
For the star K_{1,m}, m≥2, the center has E=1 and each leaf E=m, while L=m. Thus equality holds for infinitely many graphs. For K₁, the right side is 1; the statement holds if its single vertex is counted as a leaf, but is false under the degree-one-only convention. No other nonempty connected exception exists. Excluding the root from E would subtract one from every value and leave the spread unchanged.

## Verification
The accompanying Python verifier checks the stronger BFS-tree witness against all 995 connected graphs of orders 2 through 7 in the NetworkX graph atlas. All passed on 24 November 2026. The general argument is independent of computation. A targeted prior-work search did not establish an earlier resolution, but exclusive originality is not asserted. No machine-checked proof or external acceptance is claimed.
