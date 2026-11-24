# Graffiti.pc Conjecture 255 — infinite counterexample family

24 November 2026. AI-assisted written disproof. Independent review, publication priority and Lean verification pending.

## Source and statement
E. DeLaViña, [Written on the Wall II, Conjecture 255, p. 148](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf#page=148), announced 23 February 2007, marked open in the 6 November 2026 edition. For a simple connected graph the claim is gamma_t(G) >= 2|C|/M, where C is the center, gamma_t is the total domination number, and M=max{|N(u) union N(v)|: uv an edge}. Neighborhoods are open.

## Construction
For every integer m>=4 take vertices a,b,c and disjoint sets X={x_1,...,x_m}, Y={y_1,...,y_m}. Add edges ab,bc, a-x_i, x_i-y_i, y_i-c for all i, and every edge within X. There are no further edges. This connected simple graph has n=2m+3 vertices.

## Exact invariants
Every vertex has eccentricity 2: distances within X are 1, within Y are at most 2 via c, and x_i to y_j for i!=j is 2 via x_j. The distances involving a,b,c are at most 2 by the defining edges and matched pairs. No vertex is universal (the maximum degree is m+1). Thus C=V.

The set {a,b,c} totally dominates the graph. A two-element total dominating set must be an edge whose endpoints' neighborhoods cover V.

The union of the neighborhoods of either ab or bc has size m+3. For an edge a-x_i the union has size m+3; for an edge x_i-x_j it consists of X together with a,y_i,y_j, again size m+3. For a matching edge x_i-y_i the union consists of X together with a,c,y_i, size m+3. For c-y_i the union has size m+3 as well (Y, b,c,x_i). These are all edge types. Therefore M=m+3<n, and gamma_t=3.

The claimed inequality would imply 3(m+3)>=2(2m+3), equivalent to m<=3. Every m>=4 disproves it. The first member of this family has n=11, gamma_t=3, |C|=11, M=7; the conjectured lower bound is 22/7>3. The difference tends to 1.

## Verification and attribution
The [joint standard-library verifier](../graffiti-pc-256/verify_255_256.py) was run for every m=4,...,100, with 97/97 passing. The symbolic argument above covers all m>=4; the finite tests are sanity checks. The base theta-graph construction is related to the earlier example for Conjecture 254 recorded in the same source catalogue; the added clique ensures self-centeredness. No exclusive originality, independent acceptance or machine-checked proof is claimed.
