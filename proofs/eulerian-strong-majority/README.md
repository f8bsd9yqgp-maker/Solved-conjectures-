# Three colors suffice for finite simple Eulerian graphs

27 November 2026 — AI-assisted candidate full proof of Conjecture 5 of Sylwia Antoniuk, Magdalena Prorok and Nika Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212 (https://arxiv.org/abs/2607.00212). Independent peer review, formal certification and priority confirmation remain pending.

## 1. Statement and notation

**Theorem.** Every finite simple Eulerian graph has a strong-majority edge coloring with at most three colors. In addition, the coloring is vertex-balanced at every vertex of degree at least four: no color occurs on more than half of its incident edges. Degree-two vertices need not be vertex-balanced. The latter distinction is essential, since some cycles cannot have both properties simultaneously.

For an edge uv and a color a, the required inequality is

    d_a(u)+d_a(v)-2[c(uv)=a] <= (d(u)+d(v))/2-1.

Color connected components independently, ignoring isolated vertices. Let G be connected with at least one edge. Write an Euler tour as e_0,...,e_{m-1}, with cyclic indices, and let p_i be the vertex between e_i and e_{i+1}. A visit means a transition position i. The positions belonging to vertex v are precisely d(v)/2 in number. Define a chord to be any unordered pair of distinct visit positions belonging to the same vertex; chords may share endpoints. For a visit i put

    R_i = { ((j-i) mod m) mod 3 : j != i, p_j=p_i }.

The first remainder is in {0,...,m-1}. R_i is empty exactly at a degree-two vertex. Simplicity forbids cyclic distances 1 and 2 between positions of any chord: they would traverse a loop or repeat an undirected edge.

For a cyclic step word s_i in {-1,0,+1} with total divisible by three, define c_0=0 and c_{i+1}=c_i+s_i mod 3. We use zero steps only at degree-two vertices, and never at consecutive positions. At vertices of degree at least four each tour pair has two distinct colors, so the coloring is vertex-balanced.

**Sign-change lemma.** For each e_i, partition its adjacent edges into the two tour partners e_{i-1},e_{i+1} and the remaining transition pairs at both endpoints. These pairs are disjoint because the graph is simple. Each remaining pair has distinct colors (a zero transition, occurring at a degree-two vertex, cannot be a remaining pair of an endpoint). The two partners differ if s_{i-1}+s_i is nonzero mod 3. If the two partners coincide in color a, the edge satisfies the strong-majority condition if and only if at least one remaining pair omits a. Thus any edge is automatically valid except a sign change between +1 and -1 (the selected zeros are nonconsecutive). This gives an exact local criterion at each sign change.

A closed-subtrail reversal of a chord (a,b), a<b, reverses the order and directions of e_{a+1},...,e_b. It produces another Euler tour of G. It fixes endpoint and exterior positions, and reflects each interior transition x to x'=a+b-x. If a chord has exactly one endpoint x strictly inside and its other endpoint strictly outside, then its new forward-distance residue at x' is the old one at x plus 2x-a-b modulo three. Chords entirely inside have the same unordered pair of forward residues (their order reverses); exterior chords are unchanged.

## 2. Immediate cases

If m=0 mod 3, take all steps +1. This is the periodic construction already in the original paper. If m=1 mod 3 and there is a degree-two vertex, take a zero at its unique transition and +1 elsewhere. If m=2 mod 3 and there are two nonadjacent degree-two vertices, take zeros at those transitions and +1 elsewhere. The step sums are divisible by three, and the sign-change lemma gives validity. The two zero positions are nonconsecutive because their vertices are nonadjacent. A connected graph with at least three degree-two vertices either contains a nonadjacent pair, or is the triangle (already handled). Thus the only m=2 cases left have no degree-two vertex, exactly one, or two adjacent degree-two vertices.

## 3. Residue m=1: generalization of the 4-regular argument

It remains in this case to treat minimum degree at least four, so all R_i are nonempty.

Reverse exactly two consecutive increments s_i,s_{i+1} to -1, with all others +1. The two sign-change edges are e_i and e_{i+2}. Such a block succeeds if and only if

    (1 in R_i or 2 in R_{i-1}) and (2 in R_{i+2} or 0 in R_{i+1}).        (1)

To derive this, rotate to i=0. The edge colors are 0,2,1 and c_p=p-4 mod 3 for p>=2. The partners of both boundary edges have color 2. The only negative transitions are p=0,1, each containing color 2. Every other visit of the four endpoint transitions (m-1,0,1,2) lies outside these negative transitions, by the exclusion of chord distances 1 and 2. An outside transition omits color 2 exactly at index 1 mod 3. Translating the forward cyclic distances to such a visit gives (1) for both boundary edges. The sign-change lemma proves the equivalence; the argument uses all other visits, not just one.

Suppose (1) fails everywhere. Then for any selection r_i in R_i, all the following patterns are prohibited, with cyclic indices:

    r_i=1 and r_{i+1}=0;
    r_i=1 and r_{i+2}=2;
    r_i=2 and r_{i+2}=0;
    r_i=2 and r_{i+3}=2.                                  (2)

Indeed these are the four conjunctions obtained from expanding (1). Every selection must obey them.

Consecutive 11 is impossible in any selection: the next set R_{i+2} must be {1} since 0 and 2 are forbidden. Repetition around the cycle forces every R to be {1}. This contradicts that the residues of the two directed distances of each chord sum to 1 mod 3 (a reverse distance for residue 1 has residue 0). Consecutive 00 is excluded by the reverse argument, using the first and third prohibitions. Thus every 1 is followed by 2 and every 0 is preceded by 2. Consecutive 22 is impossible: the following symbol is 1 or 2, not 0. If 1, its successor 2 violates the last prohibition; if 2, the next symbol must be 1 (0 and 2 are prohibited), and its successor 2 again violates the last prohibition. A 0 followed by 1 is impossible, because the preceding 2 and following 2 are three positions apart. Therefore every 0 is followed by 2 and every 1 is preceded by 2. Every selection strictly alternates 2 and symbols in {0,1}.

In particular m is even, and the sets R_i equal {2} on one parity, while the other parity has nonempty subsets of {0,1}. To see that the parity cannot vary between selections, change a single selected coordinate: its neighbors remain fixed and determine whether that coordinate is 2 or not. Since selections are independent coordinatewise, this proves the assertion about sets. Both ends of each chord have the same parity, since the reverse distance of residue 2 has residue 2, and the reverse distance of 0 or 1 is 1 or 0.

Choose the shortest positive cyclic distance d of any chord, rotate its positions to 0,d, and reverse the corresponding closed subtrail. Every visit strictly inside has all its other visits strictly outside: any inside partner or endpoint partner would give a shorter positive distance. The distance d is even and at least 4. The chord 0,d remains, with its endpoint residues unchanged for that pair. If the new tour also failed (1), its alternating parity for {2} would be the same as before, because the retained chord fixes the classification of position 0, and reflection x -> d-x preserves parity. In particular all reflected visits that originally had residue set {2} must still have set {2}.

If the chosen chord is not residue 2, positions 1 and 3 are interior and have R={2}. If the chord is residue 2, d is even and 2 mod 3, so d>=8; use interior positions 2 and 4. For either two positions x separated by two, choose any other visit outside the interval. Its new directed distance residue at the reflected position is 2+2x-d mod 3. The two shifts differ by 4=1 mod 3, so they cannot both leave residue 2 unchanged. Contradiction. Thus (1) succeeds on the new tour. This completes m=1 for every degree mixture.

## 4. Residue m=2: eligibility and one-zero repair

Define the set of eligible edge indices

    S = {i : 2 in R_i or 0 in R_{i-1}}.

A reversed block of length L, with L=1 mod 3, closes the step word. It succeeds exactly when both boundary indices are in S. To prove this, rotate the first boundary to 0. Its partners have color 2. An ordinary transition with index p in either the negative or positive block omits 2 precisely when p=2 mod 3: the negative block has colors -p,-p-1; the positive block has colors p-2L,p-2L+1. Excluding the two endpoint transitions, the existence of an omitting pair is exactly 2 in R_0 or 0 in R_{m-1}. Rotate to the second boundary and negate all colors; the two blocks interchange and both lengths are 1 mod 3. The same test applies. Hence a two-defect block exists exactly when S has i<j with j-i=1 mod 3. The complementary cyclic distance then also has residue 1. This includes empty R at degree-two vertices.

**One-zero repair lemma.** Suppose s is the transition at a degree-two vertex. Rotate to put s at m-1. If some chord has both endpoints of residue 1, or both of residue 2, in this new indexing, a strong-majority coloring exists. Indeed take a zero at m-1, negative steps at 0,...,L-1, positive steps at L,...,m-2, where L=2 mod 3 and 2<=L<=m-3. The sum m-1-2L is divisible by three. There is only one sign-change edge e_L, whose partners have color 2. A negative transition omits 2 precisely at residue 2, and a positive transition omits 2 precisely at residue 1 (use the formulas above with L=2 mod 3). For a chord x<y of residue 2 at both ends choose L=y: the endpoint transition p_L has another visit x in the negative block omitting 2. For residue 1 at both ends choose L=x+1: p_{L-1} has another visit y in the positive block omitting 2. Both lengths meet the stated bounds, as m=2 mod 3 and the singleton is at m-1. All other edges are automatically valid. This proves the lemma.

## 5. Residue m=2: normal form and three crossing restrictions

Suppose neither two-defect nor one-zero repair is attainable on any Euler tour, and assume the immediate cases from Section 2 fail. There are h<=2 singleton visits, and when h=2 they are consecutive cyclically (their vertices are adjacent). All other positions have at least one partner.

Call a chord neutral if both directed distances have residue 1, otherwise nonneutral (residues 0 and 2). Choose an Euler tour maximizing the number N of nonneutral chords over all tours; count every unordered pair even if chords share endpoints. Normalize by rotation as follows. When the two-defect test fails, the increasing list of eligible indices cannot contain a residue followed by its successor modulo three. At most two residues occur (three distinct residues would force an increasing successor pair); if two occur, they occur in blocks first r then r-1. Rotating at the first index of the second block makes all eligible indices residue 0, since wrapping adds m=2 mod 3. If only one residue occurs, rotate at its first eligible index; if S is empty use any origin. N is invariant under rotation.

In this normal form, a chord (a,b), a<b, with b-a=0 mod 3 would contribute a+1 and b to S, a contradiction because their residues differ (a+1 cannot wrap). A chord with b-a=2 mod 3 contributes a and b+1 (cyclic) to S, so a has residue 0 and b residue 2; b=m-1 is impossible because it has residue 1. Neutral chords have b-a=1 mod 3. Thus all chords connect distinct index residues. A type-C chord connects residues 0 and 2: it is nonneutral directed 0->2 or neutral directed 2->0. Each vertex has at most three visits, as all its pairs connect distinct residues; a vertex with three visits must have residues 0,1,2 in that linear order (the pairs 0,1 and 1,2 must have the indicated neutral direction). In particular a neutral type-C chord belongs to a vertex with precisely two visits.

There exists a type-C chord. Indeed write m=3k+2, with k>=3 in the remaining cases. To justify k>=3: a connected noncycle simple graph has a vertex of degree at least four. For m<=8 and h<=2, the degree sum gives n<=5; if n=5, m=8 and h=2 are necessary, and then all three other vertices have degree four, contradicting degree two at the remaining vertices. If n<=4 no degree-four vertex is possible. Cycles were covered in Section 2. Hence m>=11. There are 2k+1 positions of residues 0 or 2 and k+1 positions of residue 1. If no type-C chord existed, each nonsingleton position of residue 0 or 2 would have a residue-1 partner. Such partners must be distinct: two sharing a partner belong to one vertex and hence form a chord of the same residue or a type-C chord. This would require 2k+1-h<=k+1, impossible for k>=3, h<=2.

Two chords cross if their endpoints strictly interleave. The next restrictions hold even for overlapping visit-pair systems; each crossing uses four distinct indices.

**A.** A neutral chord crossing a nonneutral chord (a,b) has its interior endpoint only at residue 1. Otherwise reverse the closed subtrail (a,b). The chosen chord remains nonneutral and a,b+1 stay eligible, both of residue 0. If the neutral interior endpoint x has residue 0, then x'=a+b-x has residue 2 and its new directed distance has residue 1+2x-a-b=2. Hence x' becomes eligible and (b+1)-x'=1 mod 3. If x has residue 2, then x' has residue 0 and new directed distance 0, so x'+1 is eligible and (x'+1)-a=1 mod 3. Either gives a valid two-defect block, contrary to the hypothesis. In particular neutral type-C chords never cross nonneutral chords. This uses only the chosen two visits, even if they belong to a vertex with a third visit.

**B.** For a neutral type-C chord (a,b), all crossing chords have interior endpoint residue 1. By A all crossing chords are neutral. The chosen neutral type-C chord is the only chord at its vertex, as proved above. Reversing it preserves N for all wholly interior/exterior chords and the chosen chord. A crossing neutral chord's directed residue changes to 1+2x-a-b; with a+b=2 mod 3 this remains 1 exactly for x=1 mod 3. Any crossing at residue 0 or 2 strictly increases N, and none decreases N. This contradicts maximality of N.

**C.** A nonneutral chord (a,b) cannot be crossed from both sides by nonneutral chords (c,d) and (f,g) with c<a<d<b and a<f<b<g. Reverse (a,b). The interior endpoint d has residue 2 and reflects to residue 0, equal to the exterior endpoint c's residue. This creates an eligible position c+1 of residue 1 (because a chord of linear distance 0 mod 3 contributes its earlier endpoint plus one and its later endpoint). Likewise f reflects from residue 0 to residue 2, equal to g's residue, making g eligible with residue 2. Since c+1<g, the eligible distance is 1 mod 3, contradiction. The argument requires only these individual pairs and is unaffected by other visits.

## 6. Residue m=2: shortest type-C chord contradiction

Choose a type-C chord (a,b) of shortest ordinary linear span. There is no type-C chord with both endpoints strictly inside it.

**Neutral case.** Here a=2, b=0 mod 3, and b-a=3l+1, l>=1. The interior has l positions of each residue. By B all nonsingleton interior positions of residue 0 or 2 must have their partners inside; none can be an endpoint partner because the chosen neutral type-C chord belongs to a two-visit vertex. No partner can have residue 0 or 2, by the normal form and shortest choice. They must therefore pair to distinct residue-1 positions (a shared partner would give an interior type-C or equal-residue chord). With at most h singleton positions, this requires 2l-h<=l, hence l<=h<=2.

If l=1, the interior residues are 0,1,2. Both the 0 and 2 positions must be singletons, since their only possible partner is at distance one, forbidden. These singletons are not consecutive cyclically, contradicting the remaining cases. If l=2, both singletons must have residues 0 or 2, and they must be consecutive. The interior residues in order are 0,1,2,0,1,2, so the singletons must be a+3,a+4. The remaining residue-0 position a+1 must pair to a+5 (residue 1), since a+2 is adjacent. The remaining residue-2 position a+6 must pair to a+2 (residue 1), since a+5 is adjacent. Thus p_{a+1}=p_{a+5} and p_{a+2}=p_{a+6}, so e_{a+2} and e_{a+6} are the same undirected edge. This violates simplicity. The neutral case is impossible.

**Nonneutral case.** Here a=0, b=2 mod 3 and b-a=3l+2 with l>=1. Let x=a+2 (residue 2), y=b-2 (residue 0). They are distinct interior positions. Neither can be a singleton: if a singleton s equals x or y, rotate the tour to s+1, making s the last transition. The chord (a,b) then has both endpoints of residue 1-s mod 3, equal to 2 if s=2 mod 3 or 1 if s=0 mod 3. The one-zero repair lemma gives a valid coloring, a contradiction.

Position x has at least one partner. It cannot pair to a (distance two), b (equal residue), an interior residue 2 (equal residue), or an interior residue 0 (a shorter type-C chord). Any interior residue-1 partner must precede x by the normal form (neutral 1->2), but the only such earlier interior position is a+1, adjacent to x. So x pairs outside. A rules out a crossing neutral chord with interior residue 2. Its partner must therefore be a residue-0 position strictly before a (the nonneutral direction is 0->2). Symmetrically y cannot pair to either endpoint, or to an interior position of residue 0 or 2, or to an interior residue-1 position except the adjacent b-1 (neutral 0->1). Hence it pairs outside; A rules out a neutral crossing. Its partner is a residue-2 position strictly after b. These two crossing chords contradict C. The nonneutral case is also impossible.

We have contradicted the assumption that every Euler tour fails both repair types. This completes m=2, and hence proves the theorem. QED.

## 7. Constructive algorithm and audit

The proof yields a polynomial-time algorithm. Test the immediate cases and the relevant block criteria on a tour. For m=1 a shortest closed-subtrail reversal suffices if the test fails. For m=2, the proof of A-C and Section 6 shows that from a failed normalized tour, some reversal either yields an eligible coloring or increases N: if none exists, A and C hold and B holds by the absence of a local increase, giving exactly the same shortest-chord contradiction. Thus a global maximizing-tour search is unnecessary. Test all visit-pair reversals and accept any successful coloring or strict increase in N. Reversing the complementary subtrail is equivalent up to rotating and reversing the entire tour, preserving N and existence of either repair (for the one-zero repair both nonzero blocks have length 2 mod 3). Hence testing nonwrapping reversals suffices. N is bounded by the total number of visit pairs, at most m(m-1)/2. Each operation and each certificate test takes polynomial time. No minimum-order restrictions occur in the theorem.

The accompanying `eulerian_universal_verify.py` (Python 3 and NetworkX) checks the algorithm by directly counting colors adjacent to each edge, separately from the certificate logic. A seeded run checked 3,592 graphs: 51 connected Eulerian atlas graphs, 900 mixed-degree graphs of minimum degree four, 900 with one subdividing degree-two vertex, 900 with two adjacent subdividing degree-two vertices, and 841 other connected randomly generated even-degree graphs. All returned valid colorings. Two of these instances required a tour reversal. These are finite implementation tests, not exhaustive proof, and do not by themselves establish the theorem. The mathematical argument is independent of these tests.

## 8. Sources and scope

- Original statement: Antoniuk, Prorok and Salia, *Strong Majority Edge-Coloring*, Conjecture 5, p. 3, arXiv:2607.00212v1 (https://arxiv.org/abs/2607.00212). The periodic m=0 case is prior work. The conjecture statement and page were inspected in this investigation.
- Pękała and Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122 (https://arxiv.org/abs/2608.04122), prove three colors for general graphs of minimum degree at least five. This is prior work and is not claimed as part of the novelty here.
- This note extends the previous 4-regular construction by allowing overlapping pairs of visits and treats all degree-two exceptions. It concerns finite simple Eulerian graphs as in the source, not unrestricted graphs of odd degree or multigraphs.
- Independent proof review, Lean formalization, and confirmation of priority are outstanding. The candidate proof was emailed to all three original authors and posted to this repository on 27 November 2026. No journal submission is claimed.

## 9. Additional targeted tests and duplicate screening

A separate targeted generator (`eulerian_targeted_test.py`, importing the preceding verifier) constructed 270 simple connected Eulerian tours satisfying the failed two-defect normal form, including 180 with one or two singleton visits and 130 with a three-visit vertex (the categories overlap). Every tour produced a directly verified coloring. Of these, 194 used a two-defect coloring after repair and 76 used the one-zero-one-defect construction. 195 instances required changing the tour. Combined with Section 7, this gives 3,862 successful tests. These are sampled tests, not a proof assistant verification.

Fresh duplicate screening on 27 November checked README, code (arXiv identifier 2607.00212) and issues ("strong majority" "Eulerian") in both repositories. Neither produced a matching result: https://github.com/1337isnot1337/solved-conjectures (README blob e0493dac21e0169522567c34aca30f532c0cca55), https://github.com/f8bsd9yqgp-maker/Solved-conjectures- (README blob 30a5b3fa59b934fd76b4359f0278a4a2c01b7ce0). Public searches for the exact conjecture, source identifier and subsequent Eulerian three-color proofs retrieved related research but no completed resolution. These searches do not exclude unindexed or unpublished results; priority is unconfirmed.