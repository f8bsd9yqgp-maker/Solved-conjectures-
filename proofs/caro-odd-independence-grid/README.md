# Disproof of the high-dimensional grid odd-independence conjecture

AI-assisted mathematical note, 25 November 2026. Independent academic review and discovery priority remain unverified.

## Source and statement

Y. Caro, M. Petruševski, R. Škrekovski, Zs. Tuza, *The odd independence number of graphs, II: Finite and infinite grids and chessboard graphs*, arXiv:2510.01897v1 (2 October 2025), Section 6.1, Conjecture 28, https://arxiv.org/html/2510.01897v1#S6.SS1.

An odd independent set is an independent vertex set such that every vertex outside it has zero or an odd number of neighbors in it. Write rho_d for the supremal upper density of such sets in the infinite nearest-neighbor integer grid Z^d, using axis-aligned boxes. The conjecture predicts lim_(d->infinity) rho_d=1/3.

## Theorem

Let q be the largest power of two not exceeding 2d. For all positive integers d,

(1-1/q)/2 <= rho_d <= (2d-1)/(4d-1).

In particular lim_(d->infinity) rho_d=1/2, disproving Conjecture 28. The deficit from 1/2 is of order 1/d.

## Proof

The coordinatewise residue map from Z^d to (Z/4Z)^d is locally bijective on open neighborhoods: increasing and decreasing any coordinate modulo four gives distinct residues. Identify each residue cycle C4 with Q2 by the Gray code 0->00, 1->01, 2->11, 3->10. Its d-fold Cartesian product is Q_(2d). Thus the pullback of any odd independent set of Q_(2d) is an odd independent set of Z^d. Its density exists and equals the fraction selected in the finite quotient, because the pattern has period four in each coordinate.

For completeness, construct the finite set explicitly (using the syndrome construction in the preceding companion note in this repository). Write q=2^k and label the first q coordinates of the binary cube Q_(2d) by the distinct vectors of F_2^k; label the remaining 2d-q coordinates by zero. For a binary vertex x, let p(x) be its coordinate parity and s(x) the sum over F_2^k of the coordinate labels weighted by the bits of x. Select x exactly when p(x)=1 and s(x)!=0.

All selected vertices have odd parity, so the set is independent. An odd-parity vertex outside the set has no selected neighbors. For an even-parity vertex x, flipping any coordinate yields odd parity and changes its syndrome by that coordinate's label. Among the first q flips, exactly one yields zero syndrome. Among the remaining flips, either all yield zero syndrome (when s(x)=0) or none do. Therefore the selected neighbor count is q-1 or 2d-1 respectively. Both are odd. This proves odd independence.

The linear map x -> (p(x),s(x)) onto F_2^(k+1) is surjective: the column with label zero gives (1,0), and adding this to columns with basis-vector labels gives (0,e_i). Each fiber has equal size. Consequently the selected fraction is (q-1)/(2q), establishing the lower bound via the periodic pullback.

For the upper bound let S be any odd independent set and let B be an axis-aligned box of side n in Z^d. Write N=n^d and M=|S intersect B|. All 2dM edges incident to selected vertices in B lead to unselected vertices. At most O_d(n^(d-1)) of these edges leave B, uniformly over box position. Every unselected vertex has at most 2d-1 selected neighbors because its full degree 2d is even. Counting the remaining edges at their unselected endpoints gives

2dM <= (2d-1)(N-M)+O_d(n^(d-1)).

Divide by N and take the upper limit in n for fixed d; then take the supremum over S and boxes. This proves rho_d <= (2d-1)/(4d-1).

Finally d<q<=2d, so both bounds tend to 1/2 as d tends to infinity. More precisely 1/(8d-2) <= 1/2-rho_d <= 1/(2q) < 1/(2d). QED.

## Computational check and scope

The companion verify.py directly evaluates the periodic selection rule and the 2d lattice-neighbor residues for all 87,380 vertices of fundamental period cells in dimensions 1 through 8. The local run passed every assertion, including exact density and the odd-neighbor condition. The theorem is independent of these finite checks.

This result is a separate conjecture from the hypercube question in Part I, although it uses the same coding-theoretic construction and the standard covering C4=Q2. Exact densities in fixed dimensions are not claimed. The original arXiv text was checked, and a targeted search found a recent independent solution of the square-grid Problem 29 which explicitly listed Conjecture 28 as open (https://the-omega-institute.github.io/trureturing-mdbook/Problems/caro-petrusevski-skrekovski-tuza-grid-three-eighths.html). No earlier solution of Conjecture 28 was located in that limited search. This is not proof of priority, and no external review or proof-assistant verification has been completed.
