# Strong NP-completeness of line-sum optimization with arbitrary vertex costs

AI-assisted research note, November 25, 2026. Candidate for independent mathematical review. This is a complexity classification, not a proof of P != NP. The literature search has not established publication priority.

## Statement and sources

S. Onn, *On Line Sum Optimization*, Linear Algebra and its Applications 610 (2021), 474–479, arXiv:2012.02617, conjectures that the general binary matrix line-sum optimization problem is polynomial-time solvable. M. Koutecký and S. Onn, *Uniform and Monotone Line Sum Optimization*, Discrete Applied Mathematics 298 (2021), 165–170, DOI 10.1016/j.dam.2021.04.008, explicitly conjecture polynomial-time solvability of separable degree optimization on complete bipartite and complete graphs for arbitrary integer-valued vertex functions. See also Onn, *Degree Sequence Optimization in Bounded Treewidth*, arXiv:2303.12560 (2023).

**Theorem.** The decision version of line-sum optimization for explicitly tabulated nonnegative integer functions is strongly NP-complete, even when column sums are prescribed. The version with unconstrained column sums and separable penalties is likewise strongly NP-complete. Separable degree optimization on complete graphs is also strongly NP-complete. Thus the conjectured polynomial algorithms exist if and only if P=NP (under the standard finite input model).

## Proof: reduction from 3-PARTITION

Take a strongly NP-complete 3-PARTITION instance with positive integers a_1,...,a_(3m), sum mB, and B/4 < a_i < B/2. We may restrict to B polynomially bounded in the input size, by strong NP-completeness. Set R=3m, L=B+2, C=(m-1)L+B.

Let d be the nonincreasing vector of length R formed by the triples
(jL+B,jL,jL), j=0,...,m-1. Define column sums c_k = #{i:d_i >= k}, for k=1,...,C. Thus d is the conjugate of c. The Gale–Ryser theorem says that a row vector r is realizable by a binary R-by-C matrix with these column sums iff r is majorized by d (including equality of their totals).

For each row i allow exactly the m possible sums r_i=jL+a_i, j=0,...,m-1. Let Tset={jL-1,jL:1<=j<m} and define h(x)=sum_(t in Tset) max(x-t,0). For each t, majorization implies
sum_i max(r_i-t,0) <= sum_i max(d_i-t,0).
Indeed, the left side is the maximum over k of the sum of the k largest r_i minus kt; the corresponding prefix sums of d dominate those of r. Hence sum_i h(r_i)<=sum_i h(d_i), with equality iff every one of these inequalities is tight.

Let H=h(C), and let Q=RH-sum_i h(d_i), a nonnegative integer. Row i has cost H-h(x) on its allowed values, and Q+1 elsewhere. All costs are nonnegative. For free column sums give each column k cost 0 at c_k and Q+1 elsewhere. The decision threshold is Q. A solution of cost at most Q must respect every allowed row value and prescribed column sum; it must also attain equality in all hinge inequalities.

**Forward direction.** A partition into m triples of sum B determines row sums r_i=jL+a_i with exactly three rows in each bin j. For each bin, the triple of offsets (a_i,a_l,a_p) is majorized by (B,0,0), since its entries are nonnegative and sum B. Adding jL preserves majorization; concatenating the disjoint ordered bins preserves it as well (each completed bin has equal sum, and the prefix within any bin is dominated). Thus r is majorized by d and Gale–Ryser guarantees a matrix. At the two thresholds associated with each bin boundary, each bin either contributes zero or contributes its total minus three times the threshold; consequently every hinge inequality is tight. Its cost is Q.

**Reverse direction.** Let a matrix have cost at most Q. Its allowed row sums determine bin labels. For j=1,...,m-1, equality at both t=jL-1 and t=jL implies equality of their difference:
#{i:r_i>=jL}=#{i:d_i>=jL}=3(m-j).
Here max(x-(jL-1),0)-max(x-jL,0) equals the indicator of x>=jL on integer x. Because bins are separated by L=B+2, those counts are exactly the cumulative numbers of rows in bins j and above. Subtract consecutive counts, using total R=3m and an empty bin m, to obtain precisely three rows per bin. Equality at t=jL now gives
sum_(b>=j) sum_(i assigned b) a_i = (m-j)B,
after subtracting the known baseline 3L sum_(b>=j)(b-j). The corresponding value for j=0 follows from the original input total. Taking differences shows the three offsets in every bin sum to B. They constitute a valid 3-PARTITION.

All dimensions, table lengths and costs are polynomially bounded when B is polynomially bounded, and the threshold and all costs are polynomial in m,B. A binary matrix is a polynomial-length certificate checkable by summing its entries and looking up integer costs. The reduction establishes strong NP-completeness for both prescribed and freely penalized columns.

## Complete graph variant

Start from the prescribed-column construction, with R row vertices and C column vertices in a complete graph K_(R+C). Require each column vertex k to have degree C-1+c_k. Let S=sum_k c_k, K=Q+1 and threshold Q'=KS+Q. Give each row vertex with degree x<=C its original cost f_i(x)+Kx; for degrees x>C assign Q'+1. Give each column vertex cost zero at its required degree, Q'+1 otherwise.

In a candidate of cost <=Q', the column degrees are correct, all row costs are nonnegative, and row degrees are within range. Write e_CC and e_RR for edges within the column and row sets respectively. The difference of degree sums gives
C(C-1)+S - sum_i deg(i) = 2(e_CC-e_RR) <= C(C-1).
Thus sum_i deg(i)>=S. Since K>Q, the budget forces sum_i deg(i)=S. Equality forces e_CC=C(C-1)/2 and e_RR=0. The remaining edges are exactly a binary R-by-C matrix with prescribed c and row cost <=Q. Conversely, any such matrix extends to a graph by making the column set a clique and the row set independent. This is a polynomial reduction with polynomially bounded costs. Membership in NP is immediate.

## Verification and limits

The companion verify.py tests 267 small 3-PARTITION instances (185 yes, 82 no) and all 95,564 bin assignments, computing the reduction's nonnegative tables and testing graphicality using the direct Gale–Ryser prefix inequalities, not the hinge formulation. All equivalences passed in the local run. The general proof above is independent of these tests.

A targeted literature search found the original 2021 conjectures, the 2023 open-status discussion and subsequent work on special cases; no earlier general reduction was located. This does not establish novelty. No external peer review or proof-assistant verification has been performed. This theorem does not contradict polynomial algorithms for uniform costs or inputs restricted to monotone matrices, nor does it assert hardness for fixed-dimensional matrices or bounded prescribed sums.

The conjecture about polynomial time is conditional on the unresolved P vs NP question; the unconditional result is strong NP-completeness, not a proof that P differs from NP.
