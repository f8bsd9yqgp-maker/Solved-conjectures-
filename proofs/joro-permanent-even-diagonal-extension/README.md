# Proposed even-diagonal extension of joro's permanent-of-inverse congruences

Research note, 26 November 2026. Both proposed extensions are false. The original two adjacency-matrix conjectures are NOT resolved here; do not count this note as a solution of either graph-specific conjecture.

## Source and screening

Original source: joro, 15 July 2026, https://mathoverflow.net/questions/513259/conjectured-congruences-for-the-permanent-of-inverse-of-matrix . The retrieved discussion has no answers and explicitly suggests that the two conjectures might extend to symmetric matrices with even diagonal. That suggestion is the scope of the counterexamples below.

The competitor's README (blob 1ddea291bef7620b75639449634d9abdef7e55f2) was retrieved before the user's README (blob 392a9fff8c6cccf002b37536c92d3a15206a024e). Both repositories were searched for 513259, permanent of inverse, and permanent even diagonal. No relevant match was identified. Competitor hits included unrelated numerical data, permanental compounds and other results; relevant-looking catalog and audit hits were inspected. Targeted web searches using the original title and modulo-8/even-diagonal terminology did not find an explicit previous refutation of this extension. This is targeted screening, not worldwide priority certification.

## Disproof

Let a,c be odd integers with 3 dividing ac. Define

    M = [[2a,1],[1,2c]].

Since ac is an odd multiple of 3, 4ac=12 mod 24. Thus det(M)=4ac-1=11 mod 24 and per(M)=4ac+1=13 mod 24. In particular M is invertible modulo 24 and modulo 8. Its inverse modulo 24 is

    (4ac-1)^(-1) [[2c,-1],[-1,2a]].

Since 11^2=1 mod 24, homogeneity of the two-by-two permanent gives

    per(M^(-1))=(4ac+1)/(4ac-1)^2=13 mod 24.

Therefore the first extended congruence fails (13=5 mod 8) and the second extended congruence fails (2*13+13-3=12 mod 24).

For each integer k>=0 append k diagonal blocks J=[[0,1],[1,0]]. Both J and its inverse have permanent 1. The permanent is multiplicative on block diagonal matrices, so the congruence violations persist for order 2k+2. Moreover, adding arbitrary symmetric entrywise multiples of 24 preserves all congruences and invertibility; one may make every off-diagonal entry nonzero. This disproves the unrestricted even-diagonal extension, including arbitrarily large irreducible symmetric matrices, not merely a fixed-dimensional special case.

## Original adjacency conjectures

The modulo-3 component of the second original conjecture follows from per(M^-1)=per(M) modulo 3 for any invertible matrix. This identity was already reported in *Congruences for the matrix permanent mod 3, 4, 6*, https://doi.org/10.13140/RG.2.2.11189.23524 , and is not claimed as new.

For completeness, a pairing proof uses R=F_3[x_1,...,x_n]/(x_1^3,...,x_n^3). Linear substitution acts invertibly on this ring because cubes of linear forms vanish by Frobenius. The pairing on degree n given by the coefficient of x_1^2...x_n^2 in a product is invariant: the action on top degree is det(M)^2=1, as follows directly from elementary generators (transvections, permutations, nonzero diagonal scalings). The squarefree monomial x_1...x_n is its own unique monomial dual. Pairing its transform against itself gives the permanent, and pairing invariance gives the inverse identity.

For a symmetric zero-diagonal matrix with odd determinant, the permanent is 1 mod 4: reversing each long cycle pairs its orientations; permutations with odd cycles have at least two odd cycles and hence vanish mod 4. The remaining cycle-cover sum equals the square of the hafnian, via ordered pairs of perfect matchings. The hafnian is odd because modulo 2 the determinant equals the square of the hafnian. Thus the second graph-specific conjecture reduces via CRT to the modulo-8 first conjecture. That essential claim remains unproved here.

## Verification and scope

The companion script checks 80 residue representatives of the two-parameter counterexample family. The arithmetic proof covers all parameters and arbitrary even orders independently of those checks. Preliminary tests of zero-diagonal matrices did not find a violation, but no finite test constitutes a proof of the graph-specific conjectures.

Status: proposed even-diagonal extension disproved; main graph conjectures outstanding. Independent review and worldwide discovery priority unverified. This is a supplementary research note, not a complete new solution of the two primary conjectures.
