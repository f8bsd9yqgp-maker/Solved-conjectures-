# Enumeration of ascent sequences simultaneously avoiding 0120 and 0121

AI-assisted candidate solution, 25 November 2026. Independent review and discovery priority remain pending.

Source: Qi Liu, Sergey Kitaev and Philip B. Zhang, [Simultaneous avoidance of length-4 patterns in ascent sequences](https://doi.org/10.46298/dmtcs.17977), Discrete Mathematics & Theoretical Computer Science 28(3), published 20 October 2026; [arXiv:2604.06735](https://arxiv.org/abs/2604.06735). The paper explicitly leaves simultaneous avoidance of 0120 and 0121 open. This note addresses that pair only, not the two individual avoidance problems.

## Exact scalar enumeration

An ascent sequence starts at 0 and each subsequent entry is a nonnegative integer at most one plus the number of earlier ascents. Let a_n count the sequences avoiding both patterns and a_0=1.

For n>=1, sum over p,r,s, and triples (l_i,d_i,q_i) and record values M_i as follows:

- 2<=p<n, 1<=r<=floor(p/2), 1<=s<=n-p.
- l_i>=1, sum l_i=n-p, 0<=q_i<=d_i<l_i.
- 2<=M_1<...<M_s, M_i<=r+i+sum_{h<i}q_h.

Then

$$a_n=2^{n-1}+\sum \binom{p}{2r}\prod_{i=1}^{s}\binom{M_i-2-\sum_{h<i}(d_h+1)}{d_i}B_{l_i,d_i,q_i}.$$

Binomial coefficients with inadmissible integer arguments are zero. For d=0, B_{l,0,0}=1 for l>=1. In general,

$$ B_{l,d,q}=\sum_{\substack{b_0+\cdots+b_d=l\\b_j\ge1}}\sum_{\substack{\epsilon_1,\ldots,\epsilon_d\in\{0,1\}\\\sum_j\epsilon_j=q}}\prod_{j=1}^d[(1-\epsilon_j)(A_j+1)+\epsilon_j(L_j-1-A_j)],$$

where L_j=sum_{h=0}^{j-1} b_h and A_j=sum_{h=1}^{j-1} epsilon_h. Empty products equal one. This is a finite scalar formula without matrices, determinants, or recursively defined quantities; the number of summation indices grows with n.

## Proof

Every binary word starting with 0 is an ascent sequence and avoids both patterns. There are 2^{n-1} of them. A nonbinary sequence has a unique maximal binary prefix of length p with r ascents. The number of such prefixes is C(p,2r): choose either 2r-1 or 2r transitions among the p-1 gaps, and use Pascal's identity. The prefix contains 01, so after the first entry >=2 any 0 or 1 would complete 0120 or 0121. Hence the entire suffix uses entries >=2.

With the initial 0, a 121 subsequence in the suffix is precisely an obstruction from 0121. Conversely, any occurrence of 0120 with its repeated smallest entry in the suffix would contain a smaller-larger-smaller subsequence there; if its repeated smallest entry is in the prefix, it cannot recur after the first >=2. Any 0121 occurrence must likewise either repeat 1 after the first >=2 (impossible), or give a 121 in the suffix. Thus binary prefix plus 121-avoiding suffix is equivalent to simultaneous avoidance, subject to ascent bounds.

Split the suffix just before each new record maximum M_i. The i-th block starts with M_i, uses d_i other distinct smaller values, and has l_i entries and q_i internal ascents. Every value occurring in an earlier block is forbidden in this block, since the intervening new record is larger and would give 121 if the old value recurred. Thus there are exactly C(M_i-2-sum_{h<i}(d_h+1),d_i) ways to select the other values. The ascent bound for the first entry in block i is M_i<=r+i+sum_{h<i}q_h. Since the bound is nondecreasing and every other entry of the block is at most M_i, no additional bound is needed inside the block.

For a chosen alphabet, construct the block by inserting letters in decreasing order. Start with b_0 copies of its maximum. In the word restricted to the letters inserted so far, all copies of the next smallest letter must form a single contiguous run: a larger letter between two copies would give 121. The run cannot precede the first maximum. Conversely, inserting such a run creates no forbidden 121, and deleting smaller letters recovers the insertion history uniquely. If the old word has length L and A ascents, exactly A+1 allowed gaps (the ascent gaps and the final gap) preserve the ascent count; L-1-A allowed gaps (the other internal gaps) increase it by one. This proves the stated block factor. Multiplication and summation now count each nonbinary sequence exactly once. QED.

## Growth obstruction

Here is a separate, weaker but sufficient asymptotic bound for excluding standard Catalan-style formulas:

$$ n\log n-2n\log\log n-O(n)\le \log a_n \le n\log n-n\log\log n+O(n).$$

Lower bound: start with (01)^r followed by M=r+1. There are r-1 unused smaller letters >=2. In each cycle choose d of them, append the chosen letters in increasing order, then M, then the new record M+d+1. Every chosen letter is used only once, and the old record does not occur again after the new record. Thus the suffix avoids 121. The ascent bound permits the new record: the d-1 ascents among the chosen letters and the ascent back to M unlock d additional values before the final record. After the cycle the number of unused smaller letters is unchanged: d+1 newly available smaller values replace the d chosen letters and old record. Indeed, with old free pool size M-2-U (U earlier used values below M), the new free pool is (M+d+1)-2-(U+d+1)=M-2-U. Padding by copies of the final record is legal. Therefore a_n>=C(r-1,d)^floor((n-2r-1)/(d+2)). Set r=floor(n/(2 log n)), d=floor(log n), for sufficiently large n.

Upper bound: after the first suffix letter the number of allowed values in [2,1+asc] is at most r+1, counting not-yet-used values and used values not yet followed by a larger suffix entry. Each suffix ascent makes the preceding letter permanently forbidden and unlocks at most one new value. Nonascents do not increase the allowed count. The initial suffix letter has at most r choices. Thus a_n<=2^{n-1}+sum_{p=2}^{n-1} 2^{p-1}(floor(p/2)+1)^{n-p}. Maximizing the bound over p gives the stated upper estimate: for p<=n/log n the result is immediate; for p>n/log n write p=un/log n, so (n-p)log p <= n log n-n log log n+n log u - un(1-o(1)), and log u-u/2 is bounded above. Polynomial prefactors and the binary-prefix factors contribute O(n).

Consequently the exponential generating function F(z)=sum a_n z^n/n! is entire, but its coefficients decay too slowly for any finite order of growth (Cauchy's estimate for an entire function of finite order gives log |[z^n]F|<=-c n log n+O(n) for some c>0). An entire D-finite function has finite order: outside a disk containing the zeros of its leading polynomial, its differential equation is a linear first-order system with polynomially bounded rational coefficients, and integration along radial segments bounds growth by exp(O(R^K)) for some finite K. Therefore F is not D-finite, so (a_n) is not P-recursive, by closure of P-recursive sequences under multiplication by 1/n!. This excludes standard terminating proper-hypergeometric multisums with fixed dimension and a valid holonomic summation setup, including Catalan-type factorial ratios. It does not exclude arbitrary elementary expressions.

## Verification and scope

Run python3 verify.py. It checks direct avoidance by subsequence enumeration through n=10 and evaluates the proven formula through n=20 using cached block-count recurrences. Results: 1,1,2,5,13,34,90,244,683,1980,5945,18470,59306,196547,671306,2359338,8519890,31569075,119876994,465979065,1852291651 (starting at n=0).

The exact enumeration is the candidate resolution. A simpler elementary formula outside the excluded classes is not established. The stronger matching second-order asymptotic claim and other operator formulas from earlier conversation are not included because they have not been audited to the same standard here. No claim of first discovery, peer review, or formal verification.
