# Graffiti.pc Conjecture 256 — infinite theta-graph counterexamples

24 November 2026. AI-assisted written disproof. Independent review, publication priority and Lean verification pending.

## Source and statement
E. DeLaViña, [Written on the Wall II, Conjecture 256, p. 149](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf#page=149), announced 23 February 2007, marked open in the 6 November 2026 edition. For simple connected G, gamma_t(G)>=2|N(A)|/M, where A is the set of vertices of minimum degree, M=max{|N(u) union N(v)|: uv an edge}, and N(A) is the union of the open neighborhoods of its members, as defined in the catalogue. In particular it may intersect A.

## Construction and proof
For integer m>=6 take vertices a,b,c, x_1,...,x_m, y_1,...,y_m and exactly the edges ab,bc and a-x_i, x_i-y_i, y_i-c for each i. This is a connected simple theta graph, with one two-edge path and m three-edge paths between a and c. It has n=2m+3 vertices.

The degree of a and c is m+1, and every other vertex has degree 2. Hence A={b} union X union Y. Its neighborhood is {a,c} union X union Y, size 2m+2: each x_i and y_i is adjacent to another member of A, while b has no neighbor in A.

The unions for the edge types ab,bc,a-x_i,c-y_i have size m+3. For x_i-y_i the union has size 4. Consequently M=m+3. The set {a,b,c} totally dominates, and no pair can totally dominate since such a pair would have to be an edge with neighborhood union V, whereas M<n. Thus gamma_t=3.

The conjecture would require 3(m+3)>=2(2m+2), equivalent to m<=5. All m>=6 are counterexamples. The first member of the family has n=15, gamma_t=3, |N(A)|=14, M=9, giving 28/9>3. The gap tends to 1.

## Verification and attribution
The standard-library verifier was executed for m=6,...,100: 95/95 passed. The proof is symbolic and covers the entire infinite family. The theta construction is already present in the catalogue's counterexample to Conjecture 254; the contribution here is applying it to the distinct minimum-degree-neighborhood claim 256. This does not assert novel graph construction or exclusive priority. The argument uses the catalogue's union-of-open-neighborhoods definition, not N(A) minus A. No Lean proof or independent acceptance is claimed.
