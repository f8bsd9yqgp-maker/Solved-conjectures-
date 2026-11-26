# Sharp asymptotic discrepancy in self-interest subtraction games

AI-assisted research note, 25 November 2026 (US Central). Source: Bhagat, Kulkarni, Larsson and Murali, Tie-breaking in self interest cumulative subtraction games, arXiv:2510.24280v2, Section 6, Problem 1: https://arxiv.org/html/2510.24280v2#S6.

## Theorem
Let D(M) be the maximum, over nonempty finite positive integer subtraction sets S with max S=M, nonnegative heap sizes and either player, of the absolute difference between FvF and AvA equilibrium scores. For M>=2,
D(M) <= floor((M-2)/2).
For even M>=1000, D(M)>=M/2-85; for odd M>=1001, D(M)>=(M-181)/2. Consequently lim D(M)/M=1/2 and D(M)=M/2-O(1). The exact finite-M function is not determined.

## Upper bound
Write m=min S and h=qM+r, 0<=r<M. Each player's utility in any subgame-perfect equilibrium is at least the score they can secure by taking M whenever possible: the first player secures ceil(q/2)M and the second floor(q/2)M. Call these the baseline scores. Total utility never exceeds h, so every coordinate discrepancy is at most r.

A second bound is m-1. For either player, let v be the minimax value in the auxiliary zero-sum game whose payoff is that player's own accumulated score. This player can secure v, and the other can hold that score to at most v, thereby securing at least h-(m-1)-v for themselves (terminal leftover is at most m-1). In every self-interest equilibrium, the first player's score lies in [v,v+m-1], using these guarantees and the total-utility bound. This applies to either player. Thus the claimed upper bound follows if m<=floor(M/2) or r<floor(M/2).

Otherwise m>floor(M/2) and r>=floor(M/2), so m+r>=M. Singleton sets trivially have zero discrepancy. Write q=2k+epsilon, epsilon in {0,1}, n=k+1, p=M-m>0. The player who would have the extra move after q total moves can plan n legal moves (each either M or m) of total at most kM+r, if such a choice exists: the opponent has at most k+epsilon preceding turns, each removing at most M. Each planned move is feasible since the sum of all planned moves fits even against these maximum opponent removals.

If np>=M-r, take j=ceil((M-r)/p)<=n moves of size m and n-j of size M. The extra-move player secures nM-jp, while the other secures their original baseline. Their combined guaranteed scores leave a slack jp-(M-r)<=p-1. Consequently either coordinate discrepancy is at most p-1<=floor((M-2)/2).

If np<M-r, then nm>kM+r. There cannot be q+2 moves: for even q, (2k+2)m>2kM+2r>=h; for odd q, (2k+3)m>2kM+2r+m>=h, since m+r>=M. The baseline guarantees require at least q moves. If there were q+1, the player without the extra move would have exactly their baseline number of turns and therefore would take M every turn to meet their guarantee. The extra-move player would then have available at most kM+r in total, but n moves cost at least nm>kM+r, a contradiction. Thus every equilibrium has exactly q moves and both scores equal their baselines. This proves the universal upper bound.

## Lower bound: exact affine certificates
For every integer k>=0 use heap h=6954+14k. In the even family S=(474+k,513+k,989+2k,993+2k,1000+2k), the FvF score pair is (3532+7k,3026+6k) and the AvA score pair is (3513+7k,3441+7k). The second-coordinate difference is 415+k=M/2-85.
In the odd family S=(474+k,513+k,988+2k,992+2k,1001+2k), the pairs are (3532+7k,3028+6k) and (3516+7k,3438+7k). The second-coordinate difference is 410+k=(M-181)/2.

The included verify.py certifies these affine outcomes by exact symbolic backward induction on the constant term of the heap. Each heap and score is represented as a pair of integer coefficients (constant,slope). The verifier checks that every legal or illegal move at the constant term stays legal or illegal for all k>=0, that every strict primary comparison stays strict and that primary ties stay identical, and that the selected secondary tie-break remains optimal. Since every move has positive constant term, recursion terminates. The 2800 even-family states and 2920 odd-family states were verified. The base even witness was also evaluated independently by bottom-up exact-integer C++ and Python recurrence.

The upper and lower bounds squeeze D(M)/M to 1/2 over both parity classes. In particular the earlier proposed 3M/8 upper bound is false (M=1000, discrepancy 415).

## Scope and priority
This resolves the optimal asymptotic coefficient of Problem 1, not its exact finite-M formula. Targeted literature searches and both repository README indexes on 25 November 2026 did not reveal this asymptotic result. Independent review and exhaustive priority verification remain pending. No claim of a full resolution of Problem 1 is made.
