# Wigner negativity of pure spin states

**Theorem.** Let $j\in\{\tfrac12,1,\tfrac32,2,\ldots\}$ and let $\psi$ be a unit vector in the irreducible spin-$j$ representation. Its self-dual $\mathrm{SU}(2)$ Stratonovich–Weyl function satisfies

$$
\min_{\mathbf n\in S^2}W_\psi(\mathbf n)<0.
$$

This settles the mathematical statement of problem F18. Davis, Hennigar, Mann and Ghose proved the coherent-state case in 2023. The general argument uses an orthogonal rotation of each pure state.

## Proof

Write $D^j$ for the spin representation. Its image is compact and connected and acts irreducibly on a complex vector space of dimension $2j+1>1$. By Gichev’s Corollary 1, the orbit of $\psi$ meets every complex hyperplane. Taking the hyperplane $\psi^\perp$ gives $g\in\mathrm{SU}(2)$ such that $\langle\psi,D^j(g)\psi\rangle=0$.

Let $R$ be the spatial rotation induced by $g$, let $d\Omega$ denote solid angle, and set $d\mu=(2j+1)d\Omega/(4\pi)$. Covariance and traciality of the self-dual Wigner function give

$$
\int_{S^2} W_\psi(\mathbf n)\,W_\psi(R^{-1}\mathbf n)\,d\mu(\mathbf n)
=\bigl|\langle\psi,D^j(g)\psi\rangle\bigr|^2=0.
$$

Suppose $W_\psi$ were everywhere nonnegative. It integrates to one and is a finite sum of spherical harmonics through degree $2j$, hence real analytic. If it vanished on an open patch, it would vanish on all of the connected sphere. Its positive set is therefore open and dense. The positive set of the rotated function is also open and dense. Their intersection contains a nonempty open patch.

The integrand would be nonnegative everywhere and strictly positive on that patch, giving a strictly positive integral. This contradicts the overlap identity. Thus $W_\psi$ takes a negative value and, by continuity, is negative on a region of positive area.

## Negative volume at fixed spin

In the same normalization, the manuscript derives the state-independent bound

$$
\mathcal N(\psi)=\int_{S^2}\max\{0,-W_\psi(\mathbf n)\}\,d\mu(\mathbf n)
\ge \frac{1}{4\sqrt{2j+1}\,\binom{8j}{4j}}.
$$

The three-page manuscript includes a direct proof of the orthogonal-rotation step on page 2 and the derivation of the volume bound on page 3. For spin one-half the bound is $1/(24\sqrt 2)$, and direct integration gives $1/\sqrt 3-1/2$.

[Download the full proof (PDF)](Pure_Spin_Wigner_Negativity.pdf)

## Sources

- V. M. Gichev, *A note on common zeroes of Laplace–Beltrami eigenfunctions* (2004), Corollary 1. [Paper](https://arxiv.org/abs/math/0511688)
- J. Davis, R. A. Hennigar, R. B. Mann and S. Ghose, *Stellar representation of extremal Wigner-negative spin states* (2023), equations (11)–(14) and section III. [Paper](https://arxiv.org/abs/2206.00195)
- Open Quantum Problems, *No pure spin state has a non-negative SU(2) Wigner function*. [Problem F18](https://open-quantum-problems.vercel.app/p/F18)

Manuscript dated 18 November 2026. Independent review and publication priority remain unverified.
