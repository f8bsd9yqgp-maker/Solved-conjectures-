# Project Nose: sharp identifiability and stability of airflow-modulated mixtures

**Date:** 2026-11-26 (US Central)  
**Status:** Analytical model theorem; independent review and novelty verification pending.  
**Scope:** A self-formulated inverse problem, not a claimed resolution of an independently published conjecture or a demonstrated property of human olfaction.

## Model and assumptions

Let 0<a<b be known constants, q>0 a controlled airflow, and t=1/q. For a mixture with at most n distinct positive effective sorption rates k_i and positive concentrations c_i, define the scalar normalized uptake
[
F(t)=\sum_i c_i(e^{-ak_it}-e^{-bk_it}).
]
This is an idealized linear, first-order transport model. Chemical species with the same effective rate are represented by their aggregate concentration. It does not model receptor nonlinearities, turbulent flow, or neural decoding.

## Lemma: exponential-polynomial zero bound

If the real exponents lambda_i are distinct and P_i are nonzero real polynomials of degrees d_i, then a nonzero function H(u)=sum_i P_i(u) exp(lambda_i u) has at most sum_i(d_i+1)-1 distinct real zeros.

Proof by induction on the number of terms. For one term, the bound is the polynomial degree. For multiple terms, multiply by exp(-lambda_1 u) and differentiate d_1+1 times. The first polynomial vanishes; each remaining term retains its degree and nonzero leading coefficient because lambda_i-lambda_1 is nonzero. The induction hypothesis applies to this derivative. If the original function had at least sum_i(d_i+1) distinct zeros, repeated Rolle's theorem would give at least sum_{i>1}(d_i+1) zeros of the derivative, contradicting induction. This also proves linear independence of the constituent exponential-polynomial terms.

## Theorem 1: sharp sample count

Choose 2n positive sampling times with t_(j+1) >= (b/a)t_j. The resulting measurements uniquely determine every mixture with at most n distinct rates, up to permutation.

Proof. Subtract two mixtures, combine equal rates, and discard zero coefficients. If the difference is nontrivial it consists of m<=2n distinct rates with nonzero signed coefficients d_i. Its value at t_j is the integral from a t_j to b t_j of H(u)=sum_i d_i k_i exp(-k_i u). If the measurements agree, every integral is zero. Continuity forces an interior zero of H on every interval (otherwise its sign is constant there). The interiors are disjoint. Thus H has at least 2n distinct zeros, contradicting the lemma's bound m-1. Therefore the mixtures agree.

Necessity: exactly n positive concentrations and strictly ordered positive rates form a nonempty open subset of R^(2n). If a continuous measurement map into R^M were injective with M<2n, padding with zero coordinates would give a continuous injection into R^(2n) whose image lies in a proper coordinate subspace. Invariance of domain requires the image to be open, a contradiction. Consequently 2n is optimal for continuous fixed-dimensional measurement maps.

## Theorem 2: uniform Lipschitz inverse on separated compact domains

Restrict to exactly n ordered rates in [k_min,k_max], with k_min>0, consecutive gaps at least Delta>0, and concentrations in [c_min,c_max], with c_min>0. Assume this parameter set D is nonempty. Let F denote the 2n-vector of samples from Theorem 1.

The Jacobian is nonsingular throughout D. For a directional perturbation (alpha_i,beta_i) of concentrations and rates, its jth component is the integral over [a t_j,b t_j] of
H(u)=sum_i [alpha_i k_i + c_i beta_i(1-k_i u)] exp(-k_i u).
A null direction would force 2n distinct zeros. The zero-bound lemma gives at most 2n-1 unless every coefficient vanishes. Positivity of c_i and k_i then forces beta_i=alpha_i=0. Hence the Jacobian is nonsingular.

Global stability: if no finite C satisfied ||x-y|| <= C||F(x)-F(y)|| on D, compactness would give sequences of distinct points x_l,y_l with the ratio ||F(x_l)-F(y_l)||/||x_l-y_l|| tending to zero, and convergent subsequences. Boundedness and continuity imply equality of the limiting measurements, and injectivity implies a common limit x*. Since F is continuously differentiable in an open neighborhood of x*, the difference F(x_l)-F(y_l) equals J(x*)(x_l-y_l)+o(||x_l-y_l||), by integrating the Jacobian along the line segment. The smallest singular value of J(x*) is strictly positive, contradicting the ratio tending to zero. Thus such a finite C exists.

If observed data are z=F(x)+e with ||e||<=epsilon, any global least-squares minimizer x_hat on D exists by compactness and has residual at most epsilon. The triangle inequality and stability give ||x_hat-x||<=2C epsilon.

## Limitations and design implications

- Identical effective rates cannot be distinguished by this model, regardless of sample count.
- No uniform rate-recovery bound persists as concentrations approach zero or rate gaps approach zero: the Jacobian degenerates in those limits. For two coalescing rates, distinct allocations of concentrations can also yield arbitrarily close observations.
- The separated-interval sampling design requires q_max/q_min >= (b/a)^(2n-1); this is a requirement of this sufficient design, not a proven universal flow-range lower bound.
- The theorem establishes existence of a stability constant, not a numerical estimate of that constant or a guarantee for local optimization algorithms.
- Real nasal validation, model calibration, quantitative conditioning bounds, and independent literature review remain outstanding.

## Related literature and priority

- A mass transport model of olfaction (1994): https://pubmed.ncbi.nlm.nih.gov/8207942/
- A numerical model of nasal odorant transport for the analysis of human olfaction (1997): https://pubmed.ncbi.nlm.nih.gov/9219668/
- Tuning to odor solubility and sorption pattern in olfactory epithelial responses (2014): https://pubmed.ncbi.nlm.nih.gov/24501345/
- Active Sensing in Olfaction: https://www.ncbi.nlm.nih.gov/books/NBK55978/
- Minimal identification of sums of exponentials with unknown parameters: https://experts.umn.edu/en/publications/minimal-identification-of-sums-of-exponentials-with-unknown-param/

The proof uses classical exponential-polynomial zero bounds and invariance of domain; related Prony and Chebyshev-system literature may contain equivalent results. A targeted search does not establish priority. Do not count this entry as a verified novel solved public conjecture. Numerical claims from earlier conversation are not included because no reproducible execution record was verified for this submission.
