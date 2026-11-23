# Fel's Conjecture 1: determinant bounds for planar multiphase conductivity

**Status:** AI-assisted candidate proof, 23 November 2026. Independent review and priority are unverified. No claim of sharpness or of a confirmed new discovery.

**Source problem:** L. G. Fel, *Self-Dual Symmetric Polynomials and Effective Isotropic Conductivity of Two-Dimensional Composites*, Mathematics 14 (2026), 1519, Section 7, Conjecture 1, equations (100)–(101). https://doi.org/10.3390/math14091519

## Statement

Let n ≥ 2, and let x_1,...,x_n > 0 be the scalar conductivities of a planar periodic composite. Suppose cyclically permuting phase labels leaves its effective tensor equal to the same scalar tensor sI. Define L as the unique positive root of

    sum_i L / ((n-1)x_i + L) = 1.

Then L(x) ≤ s ≤ U(x), where U(x) = 1/L(1/x). Equivalently, U is the unique positive solution of

    sum_i x_i / ((n-1)U + x_i) = 1.

The periodic proof below also applies to stationary ergodic homogenization with square-integrable potential correctors, as explained at the end.

## Proof

1. Put D = diag((n-1)x_i + L), and M = D - L ee^T, where e is the all-ones vector. The defining equation of L gives L e^T D^{-1}e = 1. The determinant lemma yields det M = 0, while D^{-1/2} M D^{-1/2} = I - ww^T, w = sqrt(L) D^{-1/2}e, is an orthogonal projection. Hence M is positive semidefinite. The defining sum is strictly increasing from 0 to n, so the positive root is unique. M has diagonal entries (n-1)x_i and off-diagonal entries -L, exactly the matrix in (100).

2. Normalize the periodic cell to unit measure. For each of the n cyclic relabelings let a_j be the local scalar conductivity and let E_j have columns e_k + grad(v_{jk}), where v_{jk} is the periodic corrector for macroscopic field e_k, k=1,2. Each column solves div(a_j E_j[:,k])=0. Thus <E_j>=I and <a_j |E_j|_F^2>=tr(sI)=2s. At each point (a_1,...,a_n) is a permutation of x.

3. Apply the corresponding permuted positive semidefinite M to (|E_1|_F,...,|E_n|_F). Pointwise,

    (n-1) sum_j a_j |E_j|_F^2 ≥ 2L sum_{i<j}|E_i|_F |E_j|_F.

For 2x2 matrices define B(A,C) = (det(A+C)-det A-det C)/2. The identity 2B(A,C)=cof(A):C and |cof A|_F=|A|_F give 2|B(A,C)|≤|A|_F|C|_F. The determinant is a null Lagrangian for matrices with periodic gradient columns (by integration by parts and density), so <det E_j>=1 and <det(E_i+E_j)>=4. Therefore <B(E_i,E_j)>=1.

4. Averaging the inequality in step 3 now gives

    2n(n-1)s ≥ 4L sum_{i<j}<B(E_i,E_j)> = 2n(n-1)L.

Thus s≥L.

5. Planar duality maps the effective tensor A* of a positive scalar conductivity a to R^T (A*)^{-1} R for the reciprocal conductivity, with R a quarter-turn. Each relabeled reciprocal field consequently has effective tensor s^{-1}I. Apply the lower bound to these fields to obtain 1/s≥L(1/x), or s≤U(x). The determinant equation for L(1/x)=1/U is precisely (101).

QED in the stated setting.

## Stationary extension

For stationary ergodic uniformly elliptic scalar media, replace cell averages by expectations and the periodic gradients by mean-zero square-integrable stationary potential fields. The mixed determinant identity still holds: rotating a mean-zero potential field by a quarter-turn produces a solenoidal field, orthogonal in L² to every mean-zero potential field. Expanding each mixed determinant thus leaves only the determinant polarization of the means, namely B(I,I)=1. The energy identity follows from the same potential/solenoidal orthogonality for the corrector and flux. The rest of the argument is unchanged. This covers the standard stationary ergodic model with phase-interchange symmetry and isotropic effective tensors.

## Scope and review

This addresses the two determinant inequalities, not Conjecture 2, and does not establish physical attainment or optimality. Earlier work by V. Nesi, *Multiphase interchange inequalities*, Journal of Mathematical Physics 32 (1991), https://iris.uniroma1.it/handle/11573/70888, is particularly relevant and may already imply the result. The original paper itself discusses earlier null-Lagrangian bounds. Priority and the full intended scope require specialist review. This note was generated with AI assistance and is shared for scrutiny rather than certified as an independently verified solution.
