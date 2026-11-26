# Brady's proposed multivariate Cramér-transform tail bound: disproof

AI-assisted research note, 26 November 2026. This is a complete analytical negative answer to a proposed distribution-free estimate in a MathOverflow research discussion, not a claim to resolve a named published conjecture. No computational search is necessary. Independent review and worldwide priority remain unconfirmed.

## Original source and screening

Drew Brady, "Inversion of conjugate to cumulant generating function?", MathOverflow, question 501232, asked 5 October 2025; the specific dimension-dependent prefactor proposal appears in the author's comment of 9 October 2025:
https://mathoverflow.net/questions/501232/inversion-of-conjugate-to-cumulant-generating-function

The retrieved discussion contains an answer by Ofer Zeitouni about the scalar estimate and a correction withdrawing its initial multidimensional argument. No answer settling the proposed vector inequality was displayed.

Before selecting the target, the competitor README was fetched first (blob 79464b8ad27852b02ee2f47795cdb4b7ca429ea3), then the user's README (blob ebe3829a29b6881de8971e7f5d09a71dc0e0f754). Default-branch searches of both repositories for 501232, Drew Brady, Cramer transform, and cumulant generating function identified no relevant solution; competitor matches concerned unrelated cumulant problems and numerical data.

- https://github.com/1337isnot1337/solved-conjectures
- https://github.com/f8bsd9yqgp-maker/Solved-conjectures-

Targeted public searches of the exact question title, author, and combinations of Cramér transform, dimension-dependent tail bounds, spherical and isotropic distributions revealed no explicit prior answer to the proposed inequality. A relevant earlier paper is S. Brazitikos and G. Chasapis, "Sharp estimates for the Cramér transform of log-concave measures and geometric applications," https://arxiv.org/abs/2405.07253 , especially Section 4.1, which gives the sphere marginal Laplace transform and radial reduction. The spherical obstruction is an elementary consequence of standard facts, including those formulas. We claim neither those formulas nor the underlying convex-duality and dominated-convergence techniques as new. Targeted searches do not certify absence of every prior derivation; the novelty of the explicit smooth worst-case statement and its application to Brady's question is provisional.

## Statement

For a centered random vector X in R^d with finite cumulant generating function, let

    Lambda_X(t) = log E exp(<t,X>),
    I_X(x) = sup_{t in R^d} (<t,x> - Lambda_X(t)).

The proposed inequality is P(I_X(X)>delta) <= C_d exp(-delta), with a finite distribution-independent constant C_d and every delta>0.

## Theorem 1 (finite-support exact disproof)

For every d>=2 there exist centered, full-dimensional random vectors with finite support for which I_X(X) is an arbitrarily large finite constant almost surely.

Proof. Choose an arbitrarily large even integer N>=2d and N distinct unit vectors v_1,...,v_N in R^d, closed under negation and spanning R^d. Such configurations exist since the sphere has infinitely many antipodal pairs; include the standard coordinate pairs. Let X be uniform on the N vectors. Then E X=0.

For every t, E exp(<t,X>) >= exp(<t,v_i>)/N, so I_X(v_i)<=log N.

For t=s v_i, s>0,

    <t,v_i>-Lambda_X(t)
      = log N - log(1 + sum_{j != i} exp(-s(1-<v_i,v_j>))).

Distinct unit vectors satisfy <v_i,v_j><1. Letting s tend to infinity proves the reverse inequality. Thus I_X(v_i)=log N for every i. In particular P(I_X(X)>delta)=1 whenever N>exp(delta). Taking delta arbitrarily large disproves the proposed inequality for every d>=2. QED.

## Theorem 2 (smooth isotropic strengthening)

For every integer d>=2 and every delta>0, there is a centered, isotropic, rotationally invariant random vector Y in R^d with a C-infinity compactly supported density such that

    P(I_Y(Y)>delta)=1,

and I_Y(Y) is finite almost surely. Here isotropic means Cov(Y)=identity.

Proof. Let U be uniform on the unit sphere S^{d-1}. Independently choose V with a radially symmetric smooth probability density supported in the closed unit ball; for example a positive normalization of exp(-1/(1-||v||^2)) for ||v||<1, extended by zero. Let X_e=U+e V for 0<e<1/2.

The density of X_e is the convolution of sphere probability measure with the scaled smooth bump density. Differentiation under the integral shows it is smooth, and its support lies in the compact annulus 1-e<=||x||<=1+e. Its mean is zero and its law is rotationally invariant.

For any unit vector u and s>0, rotational invariance and |<u,V>|<=1 imply

    Lambda_{X_e}(s u)
      = log E exp(s<u,U>) + log E exp(s e<u,V>)
      <= log E exp(s U_1) + s e.

For any x in the annulus choose u=x/||x||. Evaluating the defining supremum at s u yields

    I_{X_e}(x)
      >= s(1-e) - log E exp(s U_1) - s e
       = -log E exp(-s(1-U_1)) - 2s e.

In dimension d>=2 the point U_1=1 has probability zero. The integrand exp(-s(1-U_1)) is bounded by 1 and converges to zero almost surely as s tends to infinity. Dominated convergence implies that the negative logarithm of its expectation tends to infinity.

Choose a finite s>0 for which the negative logarithm exceeds delta+1. Then choose 0<e<min(1/2,1/(4s)). The displayed lower bound exceeds delta uniformly on the entire annulus, so P(I_{X_e}(X_e)>delta)=1.

To check finiteness almost surely, note that a sample of a continuous density g lies in {g>0} almost surely. At each such x there exist r,c>0 with g>=c on B(x,r). For any nonzero t, integrate over the ball of radius r/4 centered at x+(r/2)t/||t||. This ball lies within B(x,r), and each point z in it satisfies <t,z>>=<t,x>+(r/4)||t||. Therefore Lambda_{X_e}(t)>=<t,x>+(r/4)||t||+log(c vol(B(0,r/4))). This bounds the supremum defining I_{X_e}(x) by a finite number (the value for t=0 is zero). Hence I_{X_e}(X_e) is finite almost surely.

Finally rotational invariance gives Cov(X_e)=a identity for a>0 (indeed independence and Cov(U)=identity/d give a>=1/d). Set Y=X_e/sqrt(a). For an invertible scalar rescaling b, Lambda_{bX}(t)=Lambda_X(bt), so substituting q=bt in the supremum gives I_{bX}(bx)=I_X(x). Thus normalization preserves the event and finiteness, while giving covariance identity. QED.

## Consequences and scope

For each d>=2 and each delta>0, the supremum of P(I_X(X)>delta) over the smooth compactly supported isotropic laws is exactly 1, and is attained by a law depending on delta. This excludes every nontrivial distribution-free upper envelope in this class, not merely a prefactor multiplying exp(-delta). The scalar bound is unaffected. The examples are not log-concave; no disproof of a separately restricted log-concave conjecture is asserted.

The argument is analytical for all d>=2, all thresholds and arbitrarily large finite supports. It is not a numerical case, a hillclimb, or a computational certificate. No computational checks, Lean formalization or independent referee review were performed. The proofs above are the documentation and can be checked directly.
