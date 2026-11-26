# Bai's edge-coloring extension-count problem

**AI-assisted research note, 26 November 2026. Candidate complete resolution; independent review and worldwide priority not established.**

Original question: Yuhang Bai, "An inequality relates to edge chromatic-polynomial," MathOverflow (June 3, 2024; revised December 22, 2024): https://mathoverflow.net/questions/472523/an-inequality-relates-to-edge-chromatic-polynomial

## Problem

For a finite simple graph G with m edges, let N be its number of proper k-edge-colorings. Let F be a set of s edges with a prescribed extendable coloring f, and let N(F,f)>0 count the proper extensions. Does some absolute c>0 guarantee

    N / N(F,f) >= (c k)^s

perhaps under the condition k >= 6m/7?

## Theorem 1: qualified conjecture

For every finite simple graph G, every integer k >= 6m/7, and every extendable assignment on s edges,

    N / N(F,f) >= (k / 10^10)^s.

The constant is not claimed sharp. For s=0 the inequality is equality.

### Lemma 1 (global count)

When k >= 6m/7 and a proper coloring exists,

    N >= (k/10)^m.

**Proof.** If k <= 8, the right side is at most 1, so existence suffices. Suppose k >= 9. Let Delta be maximum degree. If Delta <= m/3, greedy edge coloring has at least k-(2Delta-2) >= k-2m/3 >= 2k/9 choices per edge. If Delta > m/3, first color the Delta edges incident to a maximum-degree vertex v. They have (k)_Delta possible assignments. As Delta <= k and the factors decrease, their geometric mean is at least (k!)^(1/k) >= k/e. For an edge outside the star, at most two incident already colored edges belong to the star (because G is simple), and at most m-Delta-1 belong outside the star. Consequently it has at least k-(m-Delta+1) > k-2m/3-1 >= 2k/9-1 >= k/10 available colors. Multiplying gives the result. The empty graph is immediate. QED.

### Lemma 2 (one-edge extension)

Let T be t prescribed edges, e an unprescribed edge, and a a color. Let A be colorings extending T and B the subset with e colored a. Then

    |A| >= (k - m/2 - 3t) |B|.

**Proof.** When the coefficient is nonpositive the claim is trivial. Given phi in B and b != a, consider the component containing e in the two-color subgraph formed by a- and b-colored edges, and swap a and b on that component. This preserves properness. For b=a use the identity map. Call b safe if the operation does not change a prescribed edge. Discard the at most t colors b used on T, apart from a. For any remaining unsafe b, its two-color component containing e must meet a prescribed a-edge. Let D be the number of these b whose component contains precisely one b-edge. That edge must join an endpoint of e to an endpoint of a prescribed a-edge, hence D <= 4t in a simple graph. Each other unsafe component has at least two b-edges. As b-color edge classes are disjoint across colors, if R colors are unsafe after the first discard then 2R-D <= m, so R <= m/2+2t. Hence at least k-t-R >= k-m/2-3t colors (including a) are safe.

The map (phi,b) to the resulting coloring is injective: the output color of e identifies b, and swapping on the same two-color component reconstructs phi. Counting images proves the lemma. QED.

### Completion

For 1 <= s <= k/8, prescribe edges successively. At stage t<s,

    k-m/2-3t >= k - 7k/12 - 3k/8 = k/24,

so the product of extension ratios gives

    N / N(F,f) >= (k/24)^s.

For s>k/8, Lemma 1 and N(F,f) <= k^(m-s) yield

    N / N(F,f) >= k^s / 10^m.

Because m <= 7k/6 < (28/3)s < 10s,

    N / N(F,f) >= (k/10^10)^s.

Both cases establish the theorem. QED.

## Theorem 2: unrestricted claim is false

There is no absolute positive c guaranteeing the inequality without a palette-size restriction, even on connected regular bipartite graphs.

**Proof.** For integers k,t >= 2, take t copies of K_(k,k), with parts U_i,V_i and marked vertices u_i in U_i and v_i in V_i. Delete the edge u_i v_i from each copy and add the bridge u_i v_(i+1), with cyclic indices. The resulting graph is simple, connected, k-regular, bipartite, and has m=tk^2 edges. Proper k-edge-colorings exist: label both sides 0,...,k-1, color each remaining internal edge (a,b) by b-a modulo k, and each bridge by 0.

In any proper k-edge-coloring, each color class is a perfect matching. Fix one block i and one color h. Counting matching edges incident to U_i and V_i separately, the internal edges contribute equally to both counts. The remaining outgoing and incoming bridge indicators must therefore agree. This holds for every h, so all t bridges have the same color in every coloring. By color-name symmetry, exactly N/k proper colorings assign a specified color to all bridges. For this s=t edge prescription, N/N(F,f)=k.

For arbitrary c>0 choose k>max(1/c,1), and then t large enough that (ck)^t>k, contradicting the claimed lower bound. QED.

## Verification and limitations

The accompanying Python verifier runs independent small-graph exact edge-coloring counts, partial-assignment extension counts and the one-edge switching inequality, plus randomized switching checks and checks of the connected k-regular bipartite construction. A previously executed run yielded:

- Atlas graphs: 265.
- Exact extension-count checks: 234,187.
- Exact prefix checks: 234,187.
- Randomized proper-coloring switch checks: 1,152.
- Explicit regular ring constructions: 15.
- All assertions passed.

Finite tests supplement rather than prove the general theorems.

Prior-repository screening on November 26, 2026: competitor https://github.com/1337isnot1337/solved-conjectures (README and CONTENTS) first, user's https://github.com/f8bsd9yqgp-maker/Solved-conjectures- (README) second. No matching entry found under the author's name, original question number 472523, the title, precoloring/precolouring or Kempe. The MathOverflow source showed no posted answer, and targeted public-source searches found no matching resolution. This does **not** prove worldwide novelty. Related works on chromatic-polynomial ratios and on partial edge-coloring extensions are different questions. Independent review, formal verification, full-text novelty screening and priority certification remain pending. The proof uses standard two-color Kempe switches, not claimed as a novel method.

Reproduce with Python and NetworkX: python verify.py. Output recorded in verification.txt.
