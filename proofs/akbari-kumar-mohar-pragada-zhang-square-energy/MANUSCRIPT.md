# Strict positive square energy for connected graphs with at least two independent cycles

## Abstract

A complete written candidate proof establishes that every finite connected simple graph with n vertices and at least n+1 edges has positive square energy strictly greater than n. The proposed proof strengthens Conjecture 1.2 of Akbari, Kumar, Mohar, Pragada and Zhang (arXiv:2506.07264). It combines a quantitative doubly nonnegative matrix deficit estimate for triangle-free 2-connected noncycle blocks with a rooted-cluster argument in a minimum-order counterexample. The latter reduces every other difficult block to a triangle vertex whose removal leaves a tree or a unicyclic graph with a cycle of length one modulo four. Uniform determinant-phase estimates, including eight exact rational integral certificates, show that those blocks cannot create enough spectral deficit to violate the conjecture. A subadditive phase envelope then sums over all blocks. There is no bound on graph order, degree, cycle rank, or pendant-tree size in the proof.

The full mathematical argument and bibliography are in SQUARE_ENERGY_COMPLETE_PROOF.md. The exact finite step is reproduced by running `python verify_integral_bounds.py`; `EXACT_VERIFICATION.log` records the output. The supplementary numerical phase tests require NumPy and NetworkX. See SQUARE_ENERGY_PROOF_AUDIT.md for the self-audit and the remaining independent-verification limitations.

## Status

Complete written proof candidate; the eight explicit rational arithmetic inequalities have been verified. Independent review, a complete Lean formalization, and confirmation of priority are not yet obtained. The proof is not represented as externally certified or published.
