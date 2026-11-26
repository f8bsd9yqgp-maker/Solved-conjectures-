# Discrete strict-convex expert aggregation: alternative construction

Date: 2026-11-26
Status: **Previously resolved question — alternative construction only. Not counted as a new solved conjecture.** No journal submission or independent review.

## Literature and priority

Snow Zhang, "Coherent combination of experts' opinions: another impossibility result", Theory and Decision 100 (2026), 451–478, https://doi.org/10.1007/s11238-025-10092-6, proves an impossibility result for finite domains.

Brian Weatherson, "Deference and Infinite Frames", section 1, already supplies a continuous counterexample to the infinite extension, using normal distributions: https://philarchive.org/rec/WEADAI-2 and https://brian.weatherson.org/quarto/posts/defer-infinite/defer-infinite.html . This prior resolution disqualifies the present work as a new solution of the original question. The novelty of the discrete alternative below is unverified.

## Discrete model

Let Omega = Z x {0,1}, with all subsets measurable. Put p_k = 2^(-|k|)/3 and r_k = 1/2 + k/[4(1+|k|)]. Then sum p_k = 1 and r_k is strictly increasing in (1/4,3/4). Define P(k,1)=p_k r_k and P(k,0)=p_k(1-r_k). Let A = Z x {1}.

Define z_j=(p_(j-1) r_(j-1)+p_j r_j)/(p_(j-1)+p_j). Strict monotonicity gives r_(j-1)<z_j<r_j<z_(j+1). For even k, set (X,Y)=(z_k,z_(k+1)); for odd k, set (X,Y)=(z_(k+1),z_k). Both reports are independent of the second coordinate conditional on k.

For X, each possible value z_j (j even) occurs exactly on indices j-1 and j. For Y, the same holds for j odd. Consequently P(A|X)=X and P(A|Y)=Y. The unordered pair {z_k,z_(k+1)} uniquely identifies k, so P(A|X,Y)=r_k. Thus min(X,Y)<r_k<max(X,Y) everywhere. In particular P(X != Y)=1. All conditioning events used have positive probability.

## Any finite number n >= 2 of experts

For each residue s modulo n, partition Z into blocks B_(s,j)={s+nj,...,s+nj+n-1}. Expert s reports the weighted mean of r over the block containing k, with weights p. Weighted means of blocks of fixed length are strictly increasing in their starting point: when shifting a block one position to the right, deleting its smallest entry and adding an entry larger than every remaining entry strictly increases the mean (all weights positive).

Consequently a report identifies its block, and each expert is calibrated. The n blocks containing k have starting points k-n+1,...,k, and intersection {k}. Their means are all distinct; the leftmost block has mean strictly below r_k and the rightmost block has mean strictly above r_k. The joint posterior r_k therefore satisfies strict convexity everywhere.

## Scope and limitations

This explicit countably additive atomic construction demonstrates the phenomenon on a countable domain, with strictly positive probability for each atom, and arbitrarily many distinct finite experts. It does not contradict fixed-weight linear-pooling impossibility results. It is an alternative to an existing resolution, not a claim of priority. A targeted literature check found the prior continuous example, but has not established whether the discrete construction or its finite-expert extension has appeared previously. No addition to the repository's solved count is warranted.
