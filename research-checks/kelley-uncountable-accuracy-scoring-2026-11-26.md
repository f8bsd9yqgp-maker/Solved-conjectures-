# Research draft: Proper accuracy scoring on uncountable opinion sets

**Date:** 2026-11-26
**Discipline:** Formal epistemology / mathematical philosophy
**Status:** PRELIMINARY — not independently verified, not established as a novel solution, and not submitted to a journal.

## Problem and provenance
Mikayla Kelley, *A Contextual Accuracy Dominance Argument for Probabilism*, Philosophy and Phenomenological Research 112 (2026), 594–607, DOI: [10.1111/phpr.70098](https://doi.org/10.1111/phpr.70098). The article discusses the impossibility of strictly proper inaccuracy measures on uncountable powersets, and a question regarding other uncountable opinion sets. Exact interpretation of the open question must be confirmed against the article text.

## Candidate counterexample
Let W be an uncountable set and F = {A subset W: A finite or W\\A finite}. F is an uncountable finite-cofinite Boolean algebra. A coherent finitely additive probability p on F is determined by singleton masses a_x=p({x}), with sum_x a_x <= 1 (sum defined as supremum over finite subsums).

For a coherent q, set

    B(q,w) = 1 - 2q({w}) + sum_x q({x})^2.

For any two coherent p,q and any finitely additive extension p* of p to 2^W,

    E_p*[B(q,w)-B(p,w)] = sum_x (p({x})-q({x}))^2.

All sums are meaningful: positive singleton masses have at most countable support, and bounded functions w -> q({w}) are uniformly approximable by finite-support functions. Distinct coherent credences on F differ on a singleton. Therefore B is strictly proper **among coherent reports**.

One simple extension to incoherent reports is I(q,w)=B(q,w) if q is coherent, I(q,w)=3 otherwise. This is bounded and strictly proper against all reports but has discontinuity / truth-directedness limitations.

## Proposed uniform-continuous extension — requires checking
Let d(c,p)=sup_{A in F}|c(A)-p(A)| for all reports in [0,1]^F. Let K be the coherent subset (closed in this metric), D(c)=inf_{p in K}d(c,p), and

    I(c,w)=sup_{p in K}[B(p,w)-4d(c,p)] + 5D(c).

The restriction to K equals B if B is 4-Lipschitz, and the extended rule is Lipschitz. A proposed domination proof for incoherent reports must be checked in full, particularly expected-value inequalities and comparison to a chosen coherent report.

## Proposed truth-directed variational score — not certified
A more complex construction was discussed in chat based on error coordinates e_A(c,w)=|c(A)-1_{w in A}| and a supremum over nonnegative combinations of such errors. The chat argued for weak coordinatewise truth-directedness and strict propriety on the entire Boolean algebra. **This construction and especially its strict-propriety proof have not been independently audited. Do not cite as an established theorem.** Potential weak spots include admissibility of the variational weights in every case, whether penalties and coefficients have the stated bounds, and expectations under finitely additive extensions.

## Product topology obstruction — conditional proposed argument
Let p0 assign 0 to finite and 1 to cofinite sets. If a real-valued score I(-,w) is product-topology continuous at p0 for each w, choose countably many continuity neighborhoods for countably many worlds S. Their coordinates mention only countably many points of W. Choose x outside these points and S; delta_x matches p0 on the selected coordinates. Then I(delta_x,w)=I(p0,w) on S. Any free-ultrafilter finitely additive extension of p0 concentrated on S gives equality of expected scores, contradicting strict propriety. This requires the chosen definition of strict propriety to quantify over *all* finitely additive probability extensions of p0. If strict propriety uses a different expectation convention, reassess.

## Validation / novelty checklist
- Confirm exact Kelley question and definition of strict propriety and continuity in full published article.
- Determine whether earlier constructions already establish the same claim (including Kelley 2023 and referenced works).
- Independently verify all proofs; seek counterexamples to the variational truth-directed score.
- Distinguish coordinatewise, uniform, and product-topology continuity.
- Confirm philosophical axioms (truth-directedness, additivity, extensionality, dominance) applicable to the exact question.
- Obtain external mathematical and philosophical review before a solved entry or journal submission.

## Sources
- Kelley (2026), https://doi.org/10.1111/phpr.70098
- Kelley (2023), *On Accuracy and Coherence with Infinite Opinion Sets*, https://doi.org/10.1017/psa.2021.37

**Repository policy:** This file documents a proposed argument for audit. Its inclusion does not indicate that an open problem has been definitively solved.
