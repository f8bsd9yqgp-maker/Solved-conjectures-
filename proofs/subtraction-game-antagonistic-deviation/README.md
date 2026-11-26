# A counterexample to antagonistic-deviation monotonicity in self-interest subtraction games

AI-assisted research note, November 25, 2026 (US Central).

## Source problem
Bhagat, Kulkarni, Larsson and Murali, *Tie-breaking in self interest cumulative subtraction games*, arXiv:2510.24280v2 (20 January 2026), Section 6, Problem 6: https://arxiv.org/html/2510.24280v2#S6 . The question asks whether switching from AvF or FvA to AvA can ever produce a positive utility discrepancy. Our witness benefits the actual switching player, so it also refutes that narrower interpretation.

## Counterexample
Use S = {5,7,18,23,24} and h = 153. With first and second coordinates in starting-player order, the outcomes are:

| Profile | Score pair |
|---|---|
| AvA | (79,74) |
| AvF | (79,73) |
| FvA | (79,74) |
| FvF | (79,74) |

Bob, the second player, increases his utility by one by switching from F to A while Alice remains A. Hence the universal assertion in Problem 6 is false.

## Exact proof certificate
For a profile (a,b) in {A,F}^2, let U_ab(h) be the current mover's and other player's equilibrium scores. If h < min(S), U_ab(h)=(0,0). Otherwise, for each legal move s, write (y,x)=U_ba(h-s) and form (s+x,y). Select a candidate maximizing its first coordinate; among those maximizing it, minimize the second coordinate for a=A and maximize it for a=F. This uniquely defines the score pair by induction on h, and implements the source's backward induction exactly.

At h=153 the candidate pairs in move order 5,7,18,23,24 are:
| Move | AvA | AvF |
|---|---|---|
| 5 | (77,76) | (77,76) |
| 7 | (79,74) | (79,74) |
| 18 | (78,72) | (79,73) |
| 23 | (78,75) | (78,75) |
| 24 | (79,74) | (79,74) |

Since the mover is antagonistic in both profiles, the selected pairs are (79,74) and (79,73), respectively. The included verifier computes all necessary smaller subpositions in exact integers by a terminating recursive recurrence, with assertions for all four outcomes. A separate bottom-up C++ search also returned the same witness. No numerical tolerances are involved. This is a finite counterexample proof, not merely sampling support for a universal statement.

## Scope and priority
This addresses Problem 6, not Conjecture 4 (previously refuted elsewhere) or the previously recorded Problem 3 preperiod result. Both competing repository README indexes and targeted searches for the source authors, problem number, equivalent phrasing, and witness were checked on November 25, 2026; no previous resolution of Problem 6 was located. Search coverage is not exhaustive and publication priority and independent expert review remain unverified. No minimality claim is made.
