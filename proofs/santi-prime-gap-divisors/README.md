# Santi's prime-gap prime-divisor conjecture

AI-assisted research note, 26 November 2026. Both proposed estimates are disproved unconditionally, and an exact summatory asymptotic for the distinct-prime weight of prime gaps is established. Discovery priority and independent review remain unconfirmed.

## Source and screening

Augusto Santi, 11 November 2020, "A conjectured upper bound for the mean value of prime divisors inside prime gaps," https://mathoverflow.net/questions/376217/a-conjectured-upper-bound-for-the-mean-value-of-prime-divisors-inside-prime-gaps . The retrieved original post displayed no answers; it proposes a pointwise asymptotic and derives a mean bound using Cramér's conjecture.

Competitor README blob 26314a9af122fd731d2d372fb6940844bf9b5451 was retrieved first, then user's README blob e468973e0e4d6d8da75dc7176bbcdb8bf8d3dcdd. Searches in both repositories for Augusto Santi, 376217, and prime divisors inside prime gaps found no relevant entry. The competitor's numerical-ID results were unrelated data. Its CONTENTS.md and docs/lean-checkpoints-1.md were retrieved to examine textual matches; none concerned this problem. Both repositories were rechecked for Santi prime-gap before submission and returned no matches.

Targeted web searches for the source ID, author, exact title, distinct prime divisors of prime gaps and weighted prime-gap sums located no explicit prior resolution. Related literature includes K. Alladi and P. Erdős, "On an additive arithmetic function," Pacific J. Math. 71 (1977), 275–294, https://msp.org/pjm/1977/71-2/pjm-v71-n2-p01-s.pdf . The retrieved paper's p. 285 explicitly establishes the average order of the sum of distinct prime factors of individual integers. This already yields a simple upper bound refuting the proposed pointwise scale once applied to gap products. No novelty is claimed for that older theorem, the prime number theorem, or their standard consequences; the gap-level deduplication argument below is provided to establish the precise replacement summatory asymptotic. Worldwide priority for the application and replacement theorem is not certified.

A separate related discussion about the *count* (rather than sum) of distinct gap factors is https://math.stackexchange.com/questions/3721677/how-many-distinct-prime-factors-are-there-in-the-numbers-between-two-primes . We do not claim to resolve its count asymptotic or Grimm's conjecture.

## Definitions and statement

Let p_n be the nth prime, V(n)=product_{p_n<m<p_{n+1}}m (empty product 1), S_n=sum_{q prime, q|V(n)}q, W_n=omega(V(n)). All logarithms natural. The 2020 post proposes

    S_n = 2n(log n)^(3/2)+O(n log n)

and, invoking Cramér's conjecture, an upper bound which in particular implies

    S_n/W_n < 2n/sqrt(log n)

eventually. For n>=2, W_n>0. We disprove both displayed estimates, without conditional hypotheses. This does not disprove Cramér's conjecture itself: its use alongside the false estimate and incorrect inequality direction cannot establish the proposed bound.

## Theorem

With c=(zeta(2)-1)/2=pi^2/12-1/2>0,

    sum_{n<=N} S_n ~ c N^2 log N.

Moreover, for every fixed epsilon>0,

    #{2<=n<=N : S_n >= epsilon*n*(log n)^(3/2)} = o(N).

There is an absolute c0>0 such that every sufficiently large dyadic block N/2<n<=N contains some n with

    S_n/W_n >= c0*n/log log n.

Consequently limsup_{n->infinity} (S_n/W_n)*sqrt(log n)/n = infinity. In particular there are infinitely many violations of the proposed upper bound.

## Proof

Put X=p_{N+1}, and let A(X) count the weighted prime factors of individual composites up to X:

    A(X)=sum_{m<=X, m composite} sum_{q prime,q|m}q
        =sum_{q<=X/2, q prime} q(floor(X/q)-1)
        =sum_{k>=2} sum_{q<=X/k, q prime} q.

The middle equality holds because among multiples of q up to X only q itself is prime. The final equality counts the cofactor k. The prime number theorem (PNT) and partial summation give sum_{q<=y} q ~ y^2/(2 log y). Indeed partial summation gives y*pi(y)-integral_2^y pi(t)dt, and the PNT evaluates the two terms asymptotically as y^2/log y and y^2/(2 log y).

For any fixed integer K>=2, the terms 2<=k<=K thus contribute asymptotically

    X^2/(2 log X) * sum_{k=2}^K 1/k^2.

The remaining terms have total at most X*pi(X/K), because each prime involved is at most X/K and its weight across all possible cofactors is at most X. Dividing by X^2/log X and taking X to infinity, the limsup of the remainder is at most 1/K. Taking K to infinity establishes

    A(X) ~ c X^2/log X.

This intermediate asymptotic also follows from Alladi–Erdős's result on individual integers after subtracting the prime inputs.

Now set T(X)=sum_{n<=N} S_n and D(X)=A(X)-T(X). Since every composite m<X occurs in exactly one of the first N gaps, D(X) is the weight of repeated appearances of the same prime within individual gaps. It is nonnegative.

Let G(X)=max_{1<=n<=N}(p_{n+1}-p_n). The PNT implies G(X)=o(X): since p_{n+1}/p_n ->1, for every delta>0 all sufficiently late gaps have length <=delta*p_n<=delta*X, while the finitely many earlier gaps are bounded independently of X. A prime q>G(X) cannot divide two different integers in the same gap, because their difference is a positive multiple of q. Therefore all repeated weight comes from primes q<=G(X), and

    0<=D(X)<=sum_{q<=G(X), q prime} q floor(X/q) <= X*pi(G(X)).

For each fixed delta>0, eventually G(X)<=delta*X, so the PNT gives limsup D(X)/(X^2/log X)<=delta. Letting delta decrease to zero shows D(X)=o(X^2/log X). Hence T(X)~c X^2/log X. Finally X=p_{N+1}~N log N by the PNT, so T(X)~c N^2 log N. This proves the replacement theorem.

If the proposed S_n asymptotic held, summing it would instead yield sum_{n<=N} S_n~N^2(log N)^(3/2), using integral comparison (or elementary summation by parts). This contradicts the established order by a diverging factor. For the stronger density conclusion, fix 0<delta<1 and epsilon>0. Among delta*N<=n<=N, each index with S_n>=epsilon*n*(log n)^(3/2) contributes at least epsilon*delta*N*(log(delta*N))^(3/2). Since the total is O(N^2 log N), there are O_{epsilon,delta}(N/sqrt(log N)) such indices. The remaining initial segment contains at most delta*N indices. Let N tend to infinity and then delta to zero. This proves density zero.

For the mean bound, deduplication also yields

    sum_{n<=N} W_n <= sum_{m<=X} omega(m)
                   = sum_{q<=X, q prime} floor(X/q)
                   <= X*sum_{q<=X, q prime} 1/q
                   = O(X log log X)
                   = O(N log N log log N).

The reciprocal-prime bound follows from the PNT and partial summation; the full Mertens prime theorem is unnecessary.

The summatory theorem implies

    sum_{floor(N/2)<n<=N} S_n ~ (3c/4) N^2 log N.

All W_n are positive on a sufficiently late block. The maximum ratio S_n/W_n on that block is at least the weighted mean sum S_n / sum W_n, which is >= c1*N/log log N for some absolute c1>0. For N/2<n<=N this implies >=c0*n/log log n after adjusting the constant. Thus along infinitely many n the ratio divided by n/sqrt(log n) grows at least as a positive constant times sqrt(log n)/log log n, which tends to infinity. The claimed upper bound is false infinitely often. QED.

## Verification

The supplemental Python sieve calculates exact distinct-prime weights in every complete gap with right endpoint <=1,000,000, checks the composite-factor accounting identity at selected endpoints, and counts certified finite violations of the weaker proposed mean bound. To avoid floating-point decisions, it takes j=floor(log_3 n), so log n>=j*log 3>=j, and checks j*S_n^2>4*n^2*W_n^2 with integers. The asymptotic ratio printed is illustrative only.

The run checked 78,497 complete gaps, found 6,052 integer-certified violations, and passed the integer accounting checks. The proof is not dependent on computation. See verify.py and verification.txt. Neither Lean formalization nor external review has been completed.
