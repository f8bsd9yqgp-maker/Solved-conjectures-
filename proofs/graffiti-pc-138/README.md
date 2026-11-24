# Graffiti.pc Conjecture 138 — infinite counterexample family

24 November 2026. AI-assisted written disproof candidate; independent review and priority unconfirmed.

Source: E. DeLaViña, [Written on the Wall II](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), November 2026 edition, printed pp. 79–80; statement and page image checked. Announced July 12, 2005 and marked open.

The claim is path(G) ≥ (2+u(G)) dist_min(M(G²)), where path(G) is the maximum order of an induced path, u is the unique maximum independent set indicator, and M denotes the maximum-degree vertices.

## Construction

For any even d≥14 and integer m≥3, start with a path p0,p1,...,pd and attach m private leaves to each endpoint. The resulting graph is a tree with d+1+2m vertices.

In the square graph, each leaf has degree m+1, each endpoint hub has degree m+2, each of p1 and p_(d−1) has degree m+3, and every other internal vertex has degree 4. Thus the maximum-degree set consists exactly of p1,p_(d−1). Their distance in the square graph is (d−2)/2 (each square edge traverses at most two original edges, and jumps of length two attain this value).

Any maximum independent set excludes the two hubs, since replacing a selected hub by its m private leaves increases the size. Every private leaf must then be selected. The remaining internal path has odd order d−1 and its unique maximum independent set comprises p1,p3,...,p_(d−1). Indeed, k nonadjacent indices in a path of order 2k−1 must occupy precisely the alternating positions. Hence u(G)=1.

In a tree every path is induced; the diameter is d+2, attained by opposite-end leaves, so path(G)=d+3. But

(2+u(G)) dist_min(M(G²)) = 3(d−2)/2 > d+3

for d>12. The family disproves the conjecture. Even if the distance is instead measured in the original graph, the right-hand side is 3(d−2), so the same examples work.

For d=14,m=3 the tree has 21 vertices, unique maximum independent set of size 13, induced path order 17, maximum-degree square vertices p1,p13, square distance 6, and claimed lower bound 18.

## Verification

The joint verifier constructs and checks 27 instances (even d=14,...,30; m=3,4,5) using exact distances and a tree dynamic program counting maximum independent sets. All passed on 24 November 2026. The infinite-family argument is exact and does not depend on these finite tests. No exact earlier resolution was identified in targeted searches; priority is not established.

[Joint verifier](../graffiti-pc-259/verify.py).
