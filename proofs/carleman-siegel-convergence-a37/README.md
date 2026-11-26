# A37: Uniform Carleman convergence under a Diophantine nonresonance condition

**AI-assisted candidate proof, 26 November 2026.** Independent mathematical review, formal verification, and discovery priority are not established.

## Source and scope

David Jennings, Kamil Korzekwa, Matteo Lostaglio, Andrew T. Sornborger, Yiğit Subaşı and Guoming Wang, *Quantum algorithms for general nonlinear dynamics based on the Carleman embedding*, Quantum 10, 2233 (2026), [DOI](https://doi.org/10.22331/q-2026-10-08-2233), [arXiv:2509.07155](https://arxiv.org/abs/2509.07155). See [Open Quantum Problems A37](https://open-quantum-problems.vercel.app/p/A37), which lists the problem as open at the time of this note. The argument uses classical Siegel analytic linearization ideas; the contribution claimed here is the explicit dimension-independent estimate and its application to Carleman truncation, not the qualitative linearization theorem itself.

## Theorem

Consider the complex quadratic ODE x'=F_1 x+F_2(x tensor x) in finite dimension N, with F_1=Q Lambda Q^{-1}, Lambda diagonal, Re(lambda_i)<=0, Q invertible. Suppose that for every multi-index alpha in N_0^N of total degree m>=2,

$$|\lambda_i-\alpha\cdot\lambda|\ge \Delta(m-1)^{-\nu},\qquad \Delta,\nu>0.$$

Use Euclidean vector and induced operator norms, with the Hilbert tensor-product norm. Write B=Q^{-1}F_2(Q tensor Q), let s be its maximum number of nonzero entries per column, and put r=||Q^{-1}x(0)||. If

$$s\|B\|r/\Delta\le 2^{-(8+8\nu)},$$

then the nonlinear solution exists globally forward in time and the first block of its usual order-k Carleman truncation, initialized with x(0) tensor powers, satisfies

$$\sup_{t\ge0}\|x(t)-y_k^{[1]}(t)\|\le (32/7)\|Q\|r\,2^{-k},\quad k\ge1.$$

The condition on the trajectory supremum asked for in A37 implies the stated initial-radius condition, so this is sufficient for that question. The proof does not require the spectrum to be strictly in the Siegel domain, and hence includes that case. If r=0 or B=0 the conclusion is immediate.

## Proof

### 1. Formal tree expansion

Set z=Q^{-1}x and seek h(w)=w+sum_{m>=2} h_m(w), where h_m is homogeneous of degree m, satisfying

$$Dh(w)\Lambda w=\Lambda h(w)+B(h(w)\otimes h(w)).$$

The nonresonance hypothesis determines each homogeneous coefficient uniquely. Iteratively substituting the quadratic term gives an expansion indexed by ordered full binary trees with m leaves, labeled by coordinates. At each internal vertex v the corresponding factor is an entry of B divided by the signed complex homological denominator (sum of leaf eigenvalues minus the eigenvalue of the output label at v). The magnitude of the denominator is

$$d_v=\left|\lambda_{i_v}-\sum_{\ell\in L(v)}\lambda_{i_\ell}\right|.$$

Here L(v) is the set of leaves descending from v. All labeling sums are finite at each degree. The denominator estimates below apply uniformly to each labeling of each tree.

### 2. Small-denominator counting

For each integer j>=0, mark v when d_v<Delta/2^{1+j nu}. If u is a strict descendant of v and both are marked, subtract their signed homological denominators. The resulting expression is lambda_{i_v}-lambda_{i_u}-sum_{ell in L(v) minus L(u)}lambda_{i_ell}, of degree 1+|L(v)|-|L(u)|>=2. Its modulus is less than Delta*2^{-j nu}, so the nonresonance hypothesis implies |L(v)|-|L(u)|>2^j. Also every marked vertex has |L(v)|-1>2^j by applying the hypothesis directly.

Make a forest of the marked vertices, with children the maximal proper marked descendants. For a terminal marked vertex assign its descendant leaves to it. For a marked vertex with exactly one marked child assign the leaves beneath it but outside its marked child's subtree. These assigned leaf sets are pairwise disjoint: if two vertices are nested, the lower one's leaves lie in one of the upper one's marked child subtrees. Each assigned set has more than 2^j leaves. If T is the terminal count, U the one-child count, and H the count of vertices with at least two children, then T+U<=m/2^j and H<=T (by the forest edge count). Consequently the number N_j of marked vertices is at most 2m/2^j, and sum_{j>=0} N_j<=4m.

For each denominator, let n_v be the number of scales at which it is marked. These scales are an initial finite segment, and failure at the next scale gives Delta/d_v<=2^{1+nu n_v}. Multiplying yields

$$\prod_v d_v^{-1}\le \Delta^{-(m-1)}2^{m-1+4\nu m}.$$

This estimate replaces factorial growth by exponential growth.

### 3. Uniform analytic majorant

For a matrix B with at most s nonzero entries per column, let |B| be the entrywise absolute-value matrix. For any vector u, applying Cauchy--Schwarz separately to each column of B gives

$$\||B|^*u\|^2\le s\sum_i |u_i|^2\sum_j |B_{ij}|^2\le s\|B\|^2\|u\|^2.$$

Thus || |B| ||<=sqrt(s)||B||<=s||B|| for s>=1. For each labeled tree, take absolute values of the coefficient entries, dominate the product of denominators by the uniform bound of Section 2, then sum all labels. The resulting nonnegative multilinear tree expression is an iterated composition of |B| acting on tensor products; its norm is bounded by (s||B||)^{m-1} times the product of the Euclidean input norms. The number of ordered binary trees with m leaves is the Catalan number C_{m-1}<=4^{m-1}. Since m<=2(m-1) for m>=2, the resulting homogeneous multilinear representation of h_m has norm at most a^{m-1}, where

$$a=2^{3+8\nu}s\|B\|/\Delta.$$

In particular ||h_m(w)||<=a^{m-1}||w||^m and ||Dh_m(w)||<=m a^{m-1}||w||^{m-1}. Hence h converges absolutely on ||w||<1/a, and termwise differentiation on smaller balls is valid. Its formal equation becomes the analytic conjugacy equation there.

For aR<=1/8, on the closed radius-R ball,

$$\|h(w)-w\|\le R/7,\qquad \|Dh(w)-I\|\le 15/49.$$

Indeed the respective geometric sums are R(aR)/(1-aR) and (1-aR)^{-2}-1. For ||z||<=R/2, the map w -> z-(h(w)-w) maps the closed radius-R ball into itself and is a contraction. Its unique fixed point g(z) satisfies h(g(z))=z. The inverse is holomorphic on an open neighborhood of the closed radius-R/2 ball: the mapping estimate has strict slack, and the analytic implicit function theorem applies because Dh is invertible. This also proves the required inverse property without assuming a global inverse.

### 4. Uniform holomorphic flow

Choose R=4r. The smallness condition implies aR<=1/8. For each ||z_0||<=R/2, the expression h(e^{t Lambda}g(z_0)) solves the transformed ODE with initial value z_0 by the conjugacy equation. Since ||e^{t Lambda}||<=1 for t>=0, the linear orbit remains in the radius-R ball forever. Thus the expression gives a global solution by uniqueness and its norm is at most 8R/7.

Let z_*=Q^{-1}x(0). The vector-valued analytic function Phi_t(zeta)=h(e^{t Lambda}g(zeta z_*)) is holomorphic on a neighborhood of |zeta|<=2 and obeys ||Phi_t(zeta)||<=32r/7 there, uniformly in t>=0. Cauchy's integral formula on the radius-two circle therefore gives

$$\|[\zeta^m]\Phi_t\|\le (32r/7)2^{-m}.$$

### 5. Exact relation to the finite Carleman hierarchy

For each j>=1, the tensor power Phi_t(zeta)^{tensor j} satisfies a linear equation with a degree-j diagonal block L_j (sum of copies of Lambda acting on each factor) and a coupling block M_j to the degree-(j+1) tensor power (sum of insertions of B). Since Phi_t(0)=0, the jth tensor power vanishes through amplitude degree j-1.

Taking Taylor polynomials modulo zeta^{k+1} commutes with these linear differential equations in time, by local holomorphic dependence on initial conditions. The degree-(k+1) tensor block is identically zero modulo zeta^{k+1}; thus the first k blocks obey the finite truncated Carleman ODE exactly, with initial blocks zeta^j z_*^{tensor j}. Evaluate the polynomials at zeta=1. Uniqueness of the finite linear ODE proves that the first block is exactly the Taylor polynomial of Phi_t at degree k evaluated at 1. The same equality holds after conjugating each tensor block by Q^{tensor j} to original coordinates.

The error is bounded by the geometric tail:

$$\|x(t)-y_k^{[1]}(t)\|\le \|Q\|(32r/7)\sum_{m=k+1}^{\infty}2^{-m}=(32/7)\|Q\|r\,2^{-k}.$$

This holds uniformly over t>=0, proving the theorem. QED.

## Consequences and limitations

A truncation order at least max(1,ceil(log_2(32||Q||r/(7 epsilon)))) suffices for absolute error epsilon. The threshold depends on nu, not directly on N or the time horizon. The bound is deliberately conservative. It does not imply end-to-end quantum algorithm efficiency: preparation, normalization, linear-system conditioning and implementation costs require further analysis.

The source catalogue lists A37 as open. Targeted searches in the previous research run did not identify an earlier explicit resolution, but classical quantitative Siegel linearization literature may contain related results; no claim of priority is made. The proof has been checked for internal consistency, not independently peer-reviewed or machine-formalized. No computational test count is asserted.
