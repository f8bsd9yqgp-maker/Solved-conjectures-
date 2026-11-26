# The limits of alpha-cut coherence: a fixed countably infinite counterexample

**Date:** 2026-11-26
**Field:** Formal epistemology / imprecise probability
**Status:** Candidate negative resolution of the unrestricted question, with a complete elementary proof under the assumptions below. AI-assisted research draft; independent verification and priority confirmation pending. Not a journal submission.

## 1. Published question and prior work

Seamus Bradley, "Learning by Ignoring the Most Wrong", Kriterion 36(1) (2022), 9–31, https://doi.org/10.1515/krt-2021-0028, Section 4, asks whether a sufficiently small positive alpha always avoids sure loss in a given learning scenario. Footnote 23 credits Marco Cattaneo with a finite two-lottery example. Footnote 24 explicitly cautions about infinite evidence partitions. The related finite-partition observation is already present in Bradley's discussion; it is not claimed as novel here.

William Peden, Mantas Radzvilas, Daniele Tortoli and Francesco De Pretis, "Ambiguity, Coherence and Performance", Economics & Philosophy 42(2) (2026), 420–456 (online November 6, 2025), https://doi.org/10.1017/S026626712510059X, Section 4.4, repeats the open question and distinguishes sequential choice from accepting a package of gambles.

The proposed contribution is to assemble the finite-lottery obstruction into one fixed countable scenario, with a fixed countable menu of allowable offers, such that every positive alpha admits a two-stage sure loss. This differs from selecting a new finite lottery after fixing alpha.

## 2. Definitions

A prior credal set C consists of countably additive probabilities on a countable space Omega with its power set sigma algebra. For an evidence cell E with positive upper probability M_E = sup_{P in C} P(E), alpha-cut updating retains P satisfying P(E) >= alpha M_E and conditions those probabilities on E, where 0 < alpha <= 1. We assume the agent accepts bounded gambles with strictly positive lower expectation under its current credal set, linear utility for payoffs, and sequential acceptance without vetoing locally favorable gambles on the basis of the aggregate package. A sure loss here means a finite sequence of accepted offers whose total payoff is bounded above by a strictly negative constant at every world.

## 3. Theorem

There exists a fixed countably infinite evidence partition and a nonempty, convex, total-variation compact set of countably additive priors, each strictly positive on every singleton, such that every 0 < alpha <= 1 permits sure loss.

### Construction

Let Omega = {(n,j,c): n >= 1, 1 <= j <= n, c in {H,T}}. Put w_n = 2^(-n), so sum_n w_n = 1.

Let C contain all distributions of the form

    P(n,j,H) = w_n/(2n),
    P(n,j,T) = (w_n/2) b_(n,j),

where each block independently has sum_j b_(n,j) = 1 and b_(n,j) >= 1/(2n).

The block probability is w_n, and the unconditional probability of each coin outcome within block n is w_n/2. These constraints make C nonempty and convex; every atom has positive probability. For compactness, the independent block parameter spaces are compact finite-dimensional simplexes with lower bounds. Given any sequence of priors, diagonal extraction yields convergence on every finite collection of blocks. The common tail mass sum_{n>N} w_n tends to zero, hence the extracted subsequence converges in total variation to a member of C. Sequential compactness in the total variation metric proves compactness.

The fixed evidence partition consists of E_(n,j) = {(n,j,H),(n,j,T)}. Its upper likelihood is attained by putting the minimum allowed tail mass on every other ticket in that block:

    max b_(n,j) = (n+1)/(2n),
    M_(n,j) = w_n(n+3)/(4n).

For every retained prior,

    P(H | E_(n,j)) = [w_n/(2n)]/P(E_(n,j))
                  <= 2/[alpha(n+3)].

Fix any alpha in (0,1]. Choose a positive integer n with n+3 > 8/alpha. At every evidence cell in block n, all retained posteriors give P(T|E_(n,j)) > 3/4. The retained set is nonempty because the upper likelihood is attained.

### The sure-loss offers

Let N denote the block index. The first bounded gamble, offered before observing evidence, is

    G_n = 1_{N=n}(1_H - 3/8) - w_n/16.

Its expectation under every prior is

    E_P G_n = w_n(1/2 - 3/8) - w_n/16 = w_n/16 > 0.

After observing E_(n,j) within the selected block, offer

    K = 1_T - 11/16.

Every retained posterior gives E[K|E_(n,j)] > 1/16. Outside the selected block, offer nothing. Thus each actual offer has strictly positive lower expectation (uniform posterior bound 5/16 - 2/[alpha(n+3)] > 1/16 in the selected block).

The total payoff is G_n + 1_{N=n} K. Inside the selected block, 1_H+1_T=1, so the total is -1/16 - w_n/16. Outside, the total is -w_n/16. Therefore the total payoff is everywhere <= -w_n/16 < 0.

The prior set, evidence partition, and allowed menu {G_n : n >= 1} plus the conditional K offer are fixed independently of alpha. Only the choice of which existing offer to make depends on alpha. This proves the claimed quantifier order: one scenario, every positive alpha, a sure-loss witness. QED.

## 4. Complementary finite-partition result (context, not a novelty claim)

Suppose the evidence partition is finite and choose any P0 in C. For each cell E with P0(E)>0, the ratio P0(E)/sup_{Q in C} Q(E) is positive. Let alpha0 be the minimum of these finitely many ratios. Then alpha0 > 0, and for 0 < alpha <= alpha0, P0 survives at every cell with positive P0 probability. For a bounded initial gamble with nonnegative lower expectation and bounded contingent second-stage gambles with nonnegative lower posterior expectation, their total expected payoff under P0 is nonnegative by the law of total expectation. Hence the total cannot be uniformly strictly negative. This is a one-update result; arbitrary iterated updates require separate hypotheses.

## 5. Scope and philosophical significance

The result rules out a universal strictly positive cutoff for the unrestricted countable scenario under the stated sequential acceptance assumptions. It does not contradict the finite partition case or the alpha=0 generalized conditioning case. It does not establish failure for a fixed finite menu of allowable initial gambles, for agents who evaluate the aggregate package, or for every possible alternate definition of dynamic coherence. It does not establish that a state-dependent cutoff would fail. The paper's wording and these modeling distinctions should be confirmed with the original author.

## 6. Novelty and repository audit

The preceding targeted literature search found Bradley's original finite-lottery example and the 2026 journal article's continued description of the issue as open; no matching fixed-scenario resolution was identified. The construction explicitly credits Cattaneo's example as reported by Bradley. The source article and subsequent discussion were rechecked at submission; the 2026 article first appeared online in 2025.

A previous GitHub audit in this conversation inspected complete default-branch tree listings (not individual contents of every file), README indexes, and targeted code searches for Bradley, alpha-cut, sure loss, and the original paper title:
- f8bsd9yqgp-maker/Solved-conjectures-: 412 tree entries
- 1337isnot1337/solved-conjectures: 19,095 tree entries
- f8bsd9yqgp-maker/Math: 296 tree entries

No relevant duplicate was identified. This is not an exhaustive worldwide priority certification; indexing omissions, aliases, and unpublished work remain possible. Independent peer review and formal verification have not been performed. Keep the confirmed solved-problem count unchanged pending review.

## References

- Bradley (2022), https://doi.org/10.1515/krt-2021-0028
- Peden et al. (2026), https://doi.org/10.1017/S026626712510059X
