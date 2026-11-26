# joro's permanent-of-inverse congruences: proof of both original conjectures

AI-assisted mathematical research note, 26 November 2026. General analytical proof for every simple graph of arbitrary order. The proposed extension to symmetric integer matrices with even diagonal remains false, as documented separately. Independent review and worldwide discovery priority remain unconfirmed.

## Original source and prior-art screening

joro, "Conjectured congruences for the permanent of inverse of matrix," MathOverflow, 15 July 2026:
https://mathoverflow.net/questions/513259/conjectured-congruences-for-the-permanent-of-inverse-of-matrix

The retrieved original discussion on 26 November displayed no posted answer. Its first conjecture is per(A^{-1})=1 mod 8 for a simple graph adjacency matrix invertible modulo 8; its second conjecture is 2per(A)+per(A^{-1})=3 mod 24 if A is invertible modulo 24. The optional even-diagonal extension was disproved in the preceding note, not in the primary conjectures.

The competitor catalog was retrieved first in the preceding investigation, followed by the user's repository. Searches for 513259, permanent of inverse, and permanent even diagonal found no relevant competing proof. Immediately before this submission both repositories were searched again for the original title. Competitor matches in CONTENTS.md and HISTORY.md were inspected and concerned unrelated permanent problems; neither contained this result. The earlier supplementary note in the user's repository is not a solution of the original graph conjectures.

- https://github.com/1337isnot1337/solved-conjectures
- https://github.com/f8bsd9yqgp-maker/Solved-conjectures-

Targeted public searches for the original title, inverse adjacency permanent modulo 8, and symmetric-matrix permanent/hafnian congruences found no prior proof of the original statements. The modulo-3 inverse identity is prior work in "Congruences for the matrix permanent mod 3, 4, 6" (https://doi.org/10.13140/RG.2.2.11189.23524); the related modulo-4 discussion is https://mathoverflow.net/questions/513095/congruences-for-the-permanent-of-symmetric-matrices-with-even-diagonal . We credit these prior results. Ryser's formula, Cauchy–Binet and the complementary principal minor identity are classical. Targeted screening does not guarantee worldwide discovery priority.

## Theorem 1

Let A be a symmetric 0/1 matrix with zero diagonal, invertible modulo 8. Then per(A^{-1})=1 mod 8.

Proof. The order n is even, since A modulo 2 is a nonsingular alternating matrix. The empty case is immediate; write n=2m>=2. Choose a symmetric integer representative B of A^{-1} modulo 8. All congruences in the first part of the proof are modulo 8, unless explicitly reduced to modulo 2.

Notation:

- 1 is the all-ones vector, e_i the ith coordinate vector, and A_i the ith column.
- r=A1 mod 2, with entries chosen in {0,1}; rsum=sum_i r_i is even by the handshaking identity.
- R=diag(r), D=I-2R, U=B R A.
- t=(B r-1)/2 is an integer vector because B r=1 modulo 2. Put T=sum_i t_i and a_i=1+t_i-U_ii.
- For a vector v, E_2(v)=sum_{i<j} v_i v_j. For a square matrix X, e_2(X) is the sum of its principal 2-by-2 minors.
- Whenever we reduce modulo 2, define K=A entrywise-multiplied by (B mod 2), L=K A, and w_ij=U_ij+L_ij modulo 2. In this notation matrix products are ordinary products, not entrywise products except in the definition of K.

### 1. Ryser reduction to at most two zero coordinates

Ryser's inclusion-exclusion formula gives

    per(B) = sum_{x in {0,1}^n} (-1)^{n-|x|} product_l (Bx)_l.

Because B is invertible over F_2, x -> Bx mod 2 is a bijection. Terms with at least three zero coordinates in Bx mod 2 vanish modulo 8. For a subset Z of size at most two let x_Z be the unique binary vector with Bx_Z=1+sum_{i in Z} e_i modulo 2. Since x_Z=A(1+sum e_i) modulo 2, its sign in Ryser's formula is (-1)^{sum_{i in Z}r_i}. Here n and rsum are even, and the parity of column i of A is r_i.

The binary representatives are exactly

    x_empty = r,
    x_{i} = r + D A_i,
    x_{i,j} = r + D(A_i+A_j-2(A_i entrywise-multiplied by A_j)).

These follow coordinatewise from the binary XOR identities and use A's binary entries.

Multiplying by B and using BA=I modulo 8 gives

    Bx_empty = 1+2t,
    Bx_{i} = 1+e_i+2(t-U_i),
    Bx_{i,j} = 1+e_i+e_j+2(t-U_i-U_j-V^{ij}),

where U_i is column i of U, and V^{ij}=B D(A_i entrywise-multiplied by A_j).

Modulo 2, D=I, and V^{ij}_i=sum_k B_ik A_ki A_kj=L_ij, using symmetry of A. Similarly V^{ij}_j=L_ji. Thus the two even factors in the product for x_{i,j} are congruent to 2(a_i+w_ij) and 2(a_j+w_ji) modulo 4; all the other factors are odd.

Write c_i=sum_l U_li. The zero-, one-, and two-zero contributions to Ryser's formula, including their signs, are respectively

    1+2T+4 E_2(t),
    2a_i+4a_i(T-t_i-c_i+U_ii-r_i),
    4(a_i+w_ij)(a_j+w_ji).

The first expansion discards terms with three factors of 2. The second expansion uses (-1)^{r_i}=1-2r_i. The last uses that the sign and all other factors are odd. These are valid modulo 8.

Summing, and noting tr(U)=tr(RAB)=rsum modulo 8, gives

    T+sum_i a_i = n+2T-tr(U) = n+2T-rsum modulo 8.

Consequently per(B)=1+4Q modulo 8, where the parity Q is

    Q = (n-rsum)/2 + T + E_2(t)
        + sum_i a_i(T-t_i-c_i+U_ii-r_i)
        + sum_{i<j}(a_i+w_ij)(a_j+w_ji)   (mod 2).

All following computations take place over F_2, except halves of explicitly even integer weights.

Since sum_i a_i=T modulo 2, the two T terms cancel. Also t_i+U_ii=a_i+1 modulo 2, so a_i(t_i+U_ii)=0. This leaves

    Q = (n-rsum)/2 + E_2(t)
        + sum_i a_i(c_i+r_i)
        + sum_{i<j}(a_i+w_ij)(a_j+w_ji).                  (1)

### 2. Elimination of the lift-dependent variables

The matrix K is symmetric, with zero diagonal and every row sum equal to 1 over F_2: its row sum at i is (BA)_ii. Since A is binary, L_ii=sum_j K_ij A_ji=1. The column sums of L are r_i, because K is symmetric with row sums 1. Hence

    sum_{j != i} w_ji = c_i + U_ii + r_i + 1.

Expanding the final sum in (1) therefore gives

    Q = (n-rsum)/2 + E_2(t)+E_2(a)
        + sum_i a_i(1+U_ii) + sum_{i<j} w_ij w_ji.

Let z_i=1+U_ii over F_2. Then a=t+z, and sum_i z_i=n+tr(U)=0 modulo 2. The elementary expansion of E_2(t+z) shows

    E_2(t)+E_2(a)+sum_i a_i z_i=E_2(z).

Thus

    Q = (n-rsum)/2 + E_2(z) + sum_{i<j} w_ij w_ji.      (2)

Let d be the binary vector of diagonal entries of U and dsum its integer weight. Since dsum is even, E_2(d)=dsum/2 modulo 2; likewise E_2(r)=rsum/2. The vector z=1+d has even integer weight n-dsum. Because n is even,

    (n-rsum)/2+E_2(z) = E_2(r)+E_2(d) modulo 2.

Modulo 2 the matrix U=B R A is similar to R. Its second characteristic coefficient therefore equals E_2(r). Direct expansion of its principal two-by-two minors gives

    e_2(U)=E_2(d)+sum_{i<j}U_ij U_ji=E_2(r).

Substitution in (2), with w=U+L, cancels the U-only terms and yields

    Q = sum_{i<j}(U_ij L_ji + L_ij U_ji + L_ij L_ji).

### 3. The final parity cancellation

Since L_ii=1, the mixed terms above are tr(UL)+tr(U). But

    tr(UL)=tr(B R A K A)=tr(R A K)=sum_i r_i=0 modulo 2,

because (AK)_ii=1. Also tr(U)=0. Therefore

    Q=sum_{i<j} L_ij L_ji = e_2(L)+binom(n,2) modulo 2.

We evaluate e_2(L) by Cauchy–Binet. Sum over all unordered two-element index sets I and J:

    e_2(KA)=sum_{I,J} det(K[I,J]) det(A[J,I]).

Symmetry of K and A makes the terms indexed by (I,J) and (J,I) identical. Terms with I != J cancel in characteristic 2. For I=J={i,j}, both matrices have zero diagonal, so the remaining product is K_ij^2 A_ij^2=K_ij. Hence

    e_2(L)=sum_{i<j} K_ij.

It remains to evaluate this last sum. Let h(A) denote the number of perfect matchings in the simple graph. Over F_2, det(A)=h(A)^2, either by the Pfaffian identity or by pairing every non-involutive permutation with its inverse in the determinant expansion. Thus h(A)=1 modulo 2. The same identity applies to every even principal submatrix of A.

The complementary principal minor identity for the inverse gives

    det(B[{i,j}]) = det(A[V minus {i,j}])/det(A) modulo 2.

Since B is alternating modulo 2 (the inverse of a nonsingular alternating matrix is alternating), the left side equals B_ij^2=B_ij modulo 2. The right side equals h(A[V minus {i,j}]) modulo 2. Therefore

    K_ij = A_ij B_ij

is precisely the parity of the number of perfect matchings containing edge ij.

Summing over all unordered pairs counts each perfect matching m=n/2 times. Hence

    sum_{i<j} K_ij = m h(A)=m modulo 2.

Since binom(2m,2)=m modulo 2, we conclude Q=0. Ryser's formula now yields per(B)=1 modulo 8, as required. QED.

The alternating-inverse fact used above follows immediately from x^T B x = (Bx)^T A(Bx)=0 over F_2, for every x. The complementary principal minor identity is Jacobi's determinant identity, valid for every invertible matrix over a field.

## Theorem 2

If the same graph adjacency matrix A is invertible modulo 24, then

    2 per(A)+per(A^{-1})=3 modulo 24.

Proof. First, per(A)=1 modulo 4. Indeed, fixed points give zero in the permutation expansion because the diagonal is zero. The number of odd cycles in a permutation on an even vertex set with no fixed points is even. Terms with odd cycles can be grouped by independently reversing these cycles; each orbit has size divisible by four and equal weight. The remaining permutations have only even cycles. Their total weight equals h(A)^2: two perfect matchings give doubled edges and even alternating cycles; each nontrivial even cycle has two ways to assign alternating edges to the ordered pair of matchings, just as it has two possible orientations. Thus per(A)=h(A)^2=1 modulo 4 since h(A) is odd.

By Theorem 1, per(A^{-1})=1 modulo 8. Hence the desired combination is 3 modulo 8.

For completeness we prove the established general identity per(C^{-1})=per(C) modulo 3 for any invertible matrix C over F_3. Work in the graded ring F_3[x_1,...,x_n]/(x_1^3,...,x_n^3). Linear substitution by C induces an automorphism g, by the Frobenius identity. The coefficient of x_1^2...x_n^2 in the product of two homogeneous degree-n elements is a bilinear pairing. It is invariant under g: elementary coordinate swaps, nonzero diagonal scalings and elementary shears all fix the top-degree monomial (the squares of nonzero elements of F_3 equal one, and the extra shear terms contain a cube). These generate the invertible matrices. For f=x_1...x_n, the pairing <g f,f> is per(C), because only the coefficient of the squarefree monomial f in g f contributes. Pairing invariance and symmetry show <g f,f>=<f,g^{-1}f>=per(C^{-1}). This is the claimed modulo-3 identity. It is prior work, not a claimed new result.

Apply the identity to A modulo 3. Then 2per(A)+per(A^{-1})=3per(A)=0 modulo 3. Together with the congruence modulo 8, the Chinese remainder theorem gives the result modulo 24. QED.

## Verification and scope

The analytical proof covers all graph orders and does not rely on computation. An independent seeded C++ search evaluated Ryser's permanent modulo 8 on 18,483 invertible random graphs among 43,600 draws of orders 4 through 16, with no violations. A separate seeded Python calculation verified the intermediate parity identities for 513 invertible graphs of orders 2 through 12. The executable source and recorded results accompany this note.

The primary graph conjectures are proved by the argument above, subject to independent review. The optional broader even-diagonal extension remains disproved. No claim of Lean formalization, peer review, or certified worldwide priority is made.
