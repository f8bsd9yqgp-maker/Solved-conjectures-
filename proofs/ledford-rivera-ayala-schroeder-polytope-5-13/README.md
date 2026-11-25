# Radon subdivision proof of Ledford–Rivera-Ayala–Schroeder Conjecture 5.13

25 November 2026. AI-assisted proof candidate. Source: A note concerning frames and geometric inequalities, arXiv:2509.05611v1, Section 5, Conjecture 5.13 and Remark 5.14, https://arxiv.org/html/2509.05611v1. Independent review and priority pending.

## Statement and interpretation

Let Q be a full-dimensional d-polytope with N=d+2 vertices v_i. Complete its edge set by adding every missing vertex pair Q^o, as in the paper's quadrilateral, pyramid and bipyramid cases. Put E=sum_{i<j} ||v_i-v_j||^2. For the Radon subdivision described below, with simplex-volume vector T, we prove

||T||_2^2 + epsilon(T) <= E^d / [2 N^(d-1) (d!)^2 d^d],

with an explicit quadratic form 0<=epsilon(T)<=vol_d(Q)^2. This holds even without the inscribed-sphere hypothesis. We interpret the printed vol_d(Q^o) in Conjecture 5.13 as vol_1(Q^o), consistent with the edge-frame expressions preceding the conjecture. The proof uses the intersection-induced subdivision indicated in Remark 5.14, not an arbitrary prescribed interior point. For degenerate affine circuits it also supplies a refinement with a common interior point.

## 1. The determinant identity

Let c=(1/N)sum_i v_i and W have columns v_i-c. The complete edge frame operator is S=sum_{i<j}(v_i-v_j)(v_i-v_j)^T=N WW^T. The augmented (d+1)-by-N matrix B with columns (1,v_i)^T has det(BB^T)=N det(WW^T) by centering the coordinate rows. Cauchy–Binet applied to B gives

det(S)=N^(d-1)(d!)^2 sum_i U_i^2,

where U_i is the d-volume of the simplex obtained by omitting v_i (zero if affinely dependent). Since tr S=E, eigenvalue AM–GM yields

(1/2) sum_i U_i^2 <= E^d/[2 N^(d-1)(d!)^2 d^d].

## 2. Radon subdivision

There is a unique affine dependence up to scaling, because B has rank d+1 and N=d+2. Write it as sum_{i in P} a_i v_i = sum_{j in M} b_j v_j = p, where a_i,b_j>0 and sum a_i=sum b_j=1. Let Z be the remaining, zero-coefficient indices. Both P and M have at least two elements because every listed point is a vertex of Q.

The simplices Q_i=conv{v_l:l!=i} for i in P form a triangulation of Q. Indeed, for any nonnegative barycentric representation of x, subtract t times the signed affine dependence with t=min_{i in P}(lambda_i/a_i). At least one positive-side coefficient becomes zero. The resulting representation is unique because two representations differ by a multiple of the affine dependence and a nonzero multiple cannot preserve the condition min_{i in P}(lambda_i/a_i)=0. Thus these simplices cover Q and meet only along common faces. The same argument applies to the negative side M.

Inside each Q_i, p is in the relative interior of its face spanned by M. Subdivide that face by coning its boundary facets to p, then join each cell with the complementary vertices. This yields d-simplices T_ij=conv({p} union {v_l:l!=i,j}), i in P, j in M. They are nondegenerate because p has positive barycentric coefficient b_j in Q_i; the subdivision is a triangulation since the face subdivision agrees on common faces. The same cells arise by subdividing the M-triangulation at p. Writing t_ij for their volumes, we obtain U_i=sum_j t_ij for i in P, U_j=sum_i t_ij for j in M, and U_z=0 for z in Z (the remaining vertices have an affine dependence). Their total V=sum_ij t_ij is vol_d(Q).

Define epsilon(T)=(1/2)sum_i(row_i)^2+(1/2)sum_j(col_j)^2-sum_ij t_ij^2. Expanding, this equals the sum of all products of two distinct cell volumes sharing a row or column; each unordered pair is counted at most once. Hence 0<=epsilon(T)<=V^2/2. Moreover

||T||_2^2+epsilon(T)=(1/2)sum_i U_i^2.

Combining with Step 1 proves the claimed inequality.

## 3. Degenerate circuits and a common interior point

If Z is empty, p is a strictly positive convex combination of all vertices by averaging its P and M representations, so it is interior. If Z is nonempty, every T_ij contains the common face F=conv({p} union {v_z:z in Z}); F is a simplex. Choose q in its relative interior. Since q has a representation with positive coefficients at every original vertex, q is interior to Q. Subdivide F at q by coning its facets, and join these pieces to the complementary vertices of each T_ij. The resulting simplices partition Q, all contain q, and no other vertex is common to all. Each original volume t_ij is the sum of its refined cell volumes t_ijr. Set epsilon_ref=(1/2)sum_i(row_i)^2+(1/2)sum_j(col_j)^2-sum_ijr t_ijr^2, using the row and column sums over all refined cells. This is a quadratic form with nonnegative cross terms; each unordered pair appears at most twice, so 0<=epsilon_ref<=V^2. The same determinant identity and bound apply exactly. This also handles iterated pyramids.

## Scope

This proves the intended completed-edge, intersection-induced formulation with an explicit correction, including non-generic configurations and arbitrary dimensions. The printed notation for added-edge lengths and any alternative universal quantifier over all interior points would require clarification with the authors. The proof does not assert the inequality for all independently selected centers. The targeted literature search did not identify a prior general resolution; absolute priority remains unverified.
