# Quantum transport polygon bound (Conjecture 7.7)

**AI-assisted candidate proof, 26 November 2026.** Independent specialist review, formal verification and discovery priority remain unestablished.

## Source and precise scope

Anonymous, *Quantum transport cost cones: exponent monotonicity, sharp operator-norm approximation and the sign of the centred cost*, version 0.1.0-candidate, 15 November 2026, Proposition 7.5 and Conjecture 7.7. [Original source](https://github.com/ipitchford/quantum-transport-cost-cones/blob/main/manuscript.tex), [DOI](https://doi.org/10.5281/zenodo.24261889).

For every finite-spectrum self-adjoint observable A and 0 < p <= 1, q > 1, the polygon bound is exact and an optimizer is a sum of at most n-1 weighted spectral-projection costs, equivalently a single exponent-one cost of an increasing function of A. This is the nontrivial approximation regime. At q=1 the same conclusion holds with zero error. At 0<q<1 the distance is zero by the hierarchy in the source (Theorem 2.1 and Corollary 4.3), but if the conjecture is read as asserting a single exponent-one cost even in this regime, that part is false: the spectrum 0,1,2 gives distances 1,1,2^q, which are strictly triangular and hence cannot be the three distances between points on the real line. The q>1 theorem does not extend to p>1.

## Theorem

Let x_1 < ... < x_n be the distinct eigenvalues of A and P_i its spectral projections. Put w_ij=|x_j-x_i|^q. Let D be the maximum of zero and the quantities

$$\frac{w_{i_0 i_m}-\sum_{k=1}^m w_{i_{k-1}i_k}}{m+1}$$

over increasing chains i_0<...<i_m, m>=1. Then for 0<p<=1 and q>1,

$$\operatorname{dist}_{op}(G_q(A),\mathcal C_p)=D.$$

Here G_p(B)=|B tensor I - I tensor B^T|^p, and the cone consists of finite sums of such costs. The maximum over no chains is defined to be zero.

## Proof

For n=1 the target is zero. Assume n>=2. The lower bound follows from the triangle inequality for product-vector entries (source Lemma 7.1, or integrate |a-c|^p <= |a-b|^p+|b-c|^p over independent spectral measurements of each vector). For any approximant with error e, the entries on unit eigenvectors along a chain satisfy w_{i_0 i_m}-e <= sum_k(w_{i_{k-1} i_k}+e), proving e>=D.

For the upper bound we construct nondecreasing y_1,...,y_n such that w_ij-D <= y_j-y_i <= w_ij+D for i<j.

### Difference constraints

Use a directed complete graph on the spectral levels, with edge cost c(i,j)=D+w_ij for i<j, and c(i,j)=D-w_ij for i>j. The desired two-sided constraints, ignoring monotonicity for now, are exactly y_j<=y_i+c(i,j) for all distinct i,j. They are feasible if all directed cycles have nonnegative cost.

Suppose a negative cycle exists and choose a negative cycle of minimum length. It is simple (a repeated vertex permits decomposition into shorter cycles, one negative), and has at least three edges since every two-edge cycle costs 2D>=0.

Two descending edges a->b->c with x_a>x_b>x_c can be replaced by a->c without increasing cost, since (u+v)^q>=u^q+v^q for u,v>=0. Also, an ascending edge followed by a descending edge a->b->c with x_a<x_c<x_b can be replaced by the ascending edge a->c: superadditivity gives w_ab>=w_ac+w_bc. Both replacements save at least D in the graph cost. Minimality prohibits both configurations. Thus every descending edge is isolated, and after an ascent followed immediately by a descent the descent ends below the starting vertex of that ascent.

Partition the cycle into maximal strictly ascending runs, separated by single descending edges. Write m_R for the number of edges in a run R, and K for total cycle length. Then sum_R(m_R+1)=K.

### Integral comparison

Let H be the sum of w over descending edges minus the sum of w over ascending edges. For a<b,

$$(b-a)^q=q(q-1)\int_{a<s<t<b}(t-s)^{q-2}\,ds\,dt.$$

The kernel is integrable on bounded triangles for q>1. Fix x_1<s<t<x_n away from the finitely many spectral coordinates, and partition vertices into L={x<s}, M={s<x<t}, R={x>t}. Write N_UV for the number of cycle edges from U to V. At these s,t, the integrand of H divided by the kernel is N_RL-N_LR. Flow conservation at L gives N_RL-N_LR=N_LM-N_ML.

Every edge L->M is ascending. If its terminal vertex is an interior vertex of its ascending run, charge it to that run; a run has at most one such L->M edge. Otherwise the next edge is descending, and by the forbidden ascent-descent configuration its terminal vertex is below the initial vertex of the L->M edge, so the next edge is M->L. This gives an injective pairing with M->L edges for all uncharged L->M edges. Consequently N_RL-N_LR is at most the number of ascending runs having an interior vertex in M.

For each run, extend its first and last vertices to the global extremes x_1,x_n, keeping all interior vertices in place. The resulting increasing chain has m_R edges (for a one-edge run it consists only of the two extremes). Its polygon defect H_R is the power-cost of the whole interval minus the sum of the power-costs of its chain edges. By the integral identity, its integrand divided by the kernel is exactly one when some interior chain vertex lies between s and t, and zero otherwise: the whole interval contains s,t and at most one chain edge contains both. Thus H<=sum_R H_R by integrating the pointwise comparison against the nonnegative kernel. By definition H_R<=(m_R+1)D. Summing yields H<=KD, contradicting negative cycle cost KD-H<0.

### Construction

There are therefore no negative cycles. Add a super-source with zero-cost edges to all vertices and take shortest-path distances y_i. These are finite and satisfy the difference constraints. Replace them by z_i=max_{k<=i} y_k.

For i<j, choose k<=i attaining z_i. Then z_j-z_i>=y_j-y_k>=w_kj-D>=w_ij-D. For the upper bound, if z_j=z_i it is immediate. Otherwise choose l with i<l<=j attaining z_j. Then z_j-z_i<=y_l-y_i<=w_il+D<=w_ij+D. Hence z is nondecreasing and satisfies both bounds.

Put Q_k=sum_{i>k} P_i, and form

$$C^*=\sum_{k=1}^{n-1}(z_{k+1}-z_k)G_p(Q_k).$$

Every coefficient is nonnegative; by homogeneity a coefficient can be absorbed in scaling its projection by the coefficient to the power 1/p. On block P_i tensor P_j^T the entry equals |z_j-z_i|, since each intervening cut contributes its gap. Thus C* is in the cone and its operator-norm error is at most D. The lower bound proves equality. Moreover C*=G_1(f(A)) for f(x_i)=z_i. QED.

For q=1 take z_i=x_i directly. For q<1, see the scope qualification above.

## Reproduction and limitations

The accompanying exact integer verifier tests 960 deterministic instances, 30 per combination of n=3,...,10 and q=2,3,4,6. It computes the polygon value by enumerating chains, constructs shortest-path potentials, and checks equality of the maximum absolute error and the polygon value after taking prefix maxima. No numerical tolerance is used. It is a sanity check only, not a proof.

A targeted 26 November search located the original conjecture and did not identify a prior proof of its nontrivial regime; this is not an exhaustive priority determination. The source itself is an unrefereed candidate. The argument above also applies to the pure-state uniform approximation error using the same lower bound and block construction. No assertion is made about unbounded observables or general p>1.
