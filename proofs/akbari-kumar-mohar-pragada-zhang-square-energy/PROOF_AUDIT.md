# Proof audit — unrestricted positive square-energy conjecture

Status: complete written candidate proof, self-audited in the same execution. No independent reviewer or proof assistant has certified the full proof. This audit does not substitute for independent mathematical scrutiny.

## Critical checks

| Step | Audit finding |
|---|---|
| Statement | The proof treats the strict assertion for every connected finite simple unsigned graph with cycle rank r≥2. It proves the original non-strict conjecture as a consequence. |
| DNN normalization and folding | Nonnegative entries with sum 1 form a compact feasible set; folding cancels nonedges using positive semidefinite rank-one terms, preserving the total sum and edge entries. |
| DNN cut-vertex splitting | Gram spans on opposite sides are orthogonal; decomposing the shared vertex preserves the edge sum and squared norm of the total Gram-vector sum. Scalar Cauchy–Schwarz gives the required deficit inequality. |
| Deletion envelopes | For 2-connected B, B−v is connected. The identities sum q(B−v)=(N−2)(q−1) and sum T(M−v)=(N−2)T+tr M yield the stated envelope, including zero principal matrices. |
| Triangle-free base cases | Cycle rank two forces a theta graph; the three terminal-correlation cases exhaust path-length patterns. All costs are below q−1. For rank three, Mantel forces N≥6 and 13N²−46N−112>0. For higher rank, the deficit sum is at least N−2 and the decisive polynomial is N²+N−4m≥N. |
| Spectral transfer | The Hadamard square of either PSD spectral part is DNN. Signed trace on edges is bounded by the absolute sum; folding and the DNN bound apply to either sign. |
| Determinant phase | Uses the unwrapped sum of arctangents, not the possibly discontinuous principal argument of the full determinant. The Schur ratio itself has positive real part, so its principal argument equals the continuous phase difference. |
| Cut-vertex phase bound | Re(z_H+z_K−t) is at least either constituent real part. Positive imaginary contributions are bounded by subadditivity of arctangent, and negative contributions may be discarded. Taking maxima over all induced subgraphs is justified also when the common vertex is absent. |
| Matching and cofactor identities | Transpositions contribute +1 to det(tI+iA). A unique odd graph cycle contributes exactly two orientations, with sign i^L. The inverse cofactor sum enumerates simple paths; the sign is (−i)^length and the remaining determinant is on deleted path vertices. |
| Forest remainder | Only lengths 3 mod 4 contribute positively; there is at most one path per pair, and opposite bipartition classes bound the count. The integral is bounded separately at rank two and all ranks ≥3. |
| Unicyclic remainder | Every induced subgraph retains the same unique odd cycle or is a forest. Its determinant has nonnegative phase in the interval [0,theta_C]. The ratio estimates apply even when the induced subgraph is disconnected. Two distinct paths differ in parity because the sole cycle is odd. A triangle at the root excludes two ordered positive odd paths, even after maximizing over induced subgraphs. |
| Finite analytic certificate | Eight exact rational upper sums for d=2,…,9 are below d−1. The companion standard-library verifier checks the rational inequalities, not approximate eigenvalues. For d≥10, (7d+68)/16<d−1. These ranges cover all integer degrees. |
| Rooted cluster reduction | Removing a block's edges partitions G into connected components rooted at its vertices. A triangle in a block with ≥4 vertices yields a proper induced connected subgraph; its square energy is strictly above its order by strict minimality or the unicyclic triangle formula. The sum of cluster row contributions is at least the squared norm on the triangle's cluster union. At least one cluster contributes more than its cardinality. Removing that entire cluster leaves a smaller connected graph whose square energy is below its order, so its rank is at most one and any unique cycle is 1 mod 4. |
| Terminal coverage | A triangle-free noncycle block is ruled out by DNN. A triangle-containing noncomplete noncycle block is controlled by one of the two phase lemmas. Complete blocks and cycles have separate estimates. Bridge blocks contribute zero. Cycle ranks add, so every possible remaining block pattern contradicts strict minimality. |

## Rejected inferences not used

The argument does not require monotonicity of positive square energy under edge addition, lossless single-leaf deletion, or an upper bound of half the cycle rank for arbitrary block-phase integrals. Previously found counterexamples to these shortcuts therefore do not affect the proof. The pointwise induced-subgraph phase maximum is not interchanged with an integral maximum; a uniform pointwise bound is integrated instead.

## Verification status

- All eight scalar certificates passed exact Fraction arithmetic.
- Numerical falsification tests on 23 Atlas block/root pairs (78,647 sample comparisons) and 100 seeded apex-unicyclic graphs (255,000 sample comparisons) passed. These are supplementary, not proof premises.
- Full Lean verification: not performed; Lean was not found on the execution path.
- Independent mathematical review: outstanding.
- Worldwide priority: outstanding. Earlier targeted repository and literature searches were not an exhaustive priority investigation.

The intended next verification is a line-by-line independent mathematical audit, in particular Sections 3, 5.2 and 6 of the full proof.
