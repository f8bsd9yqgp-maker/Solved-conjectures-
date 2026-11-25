# Asymptotic odd independence of even-dimensional hypercubes

AI-assisted research note, November 25, 2026. Source: Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763, September 2025, Problem 40 in the version inspected (https://arxiv.org/abs/2509.20763).

An odd independent set S is independent and every vertex outside S has either zero or an odd number of neighbors in S. The authors ask in particular whether alpha_od(Q_d)/2^d tends to 1/2 as even d tends to infinity.

## Theorem

For every even integer d>=2, write q=2^floor(log2 d). Then
`(1-1/q) 2^(d-1) <= alpha_od(Q_d) <= ((d-1)/(2d-1)) 2^d`.
In particular `1/2-1/d <= alpha_od(Q_d)/2^d < 1/2`, and the conjectured even-dimensional limit is 1/2. The deficit from half the vertices has order 2^d/d.

## Proof

View Q_d as the binary vector space F_2^d, with adjacency by single-coordinate flips. Let k=floor(log2 d), so q=2^k. Assign the first q coordinate labels a_i to the q distinct elements of F_2^k, and assign label 0 to each of the remaining d-q coordinates. Define the linear syndrome s(x)=sum_i x_i a_i and parity p(x)=sum_i x_i in F_2. Set
`S={x:p(x)=1 and s(x)!=0}`.

S is independent because each edge changes parity. Every odd-parity vertex outside S has zero neighbors in S. For an even-parity vertex x, its d neighbors are odd and their syndromes are s(x)+a_i. Exactly one of the first q flips gives zero syndrome. The other d-q flips all give zero syndrome if s(x)=0 and none do otherwise. Thus the number of neighbors in S is q-1 when s(x)=0 and d-1 otherwise. Both are positive odd integers since q and d are even. Therefore S is odd independent.

The linear map x -> (p(x),s(x)) is surjective onto F_2^(k+1): the column labeled zero gives (1,0), and adding it to columns labeled by the standard basis gives (0,e_j). Each fiber consequently has 2^(d-k-1) elements. Hence |S|=(q-1)2^(d-k-1)=(1-1/q)2^(d-1).

For completeness, if T is any odd independent set, all d|T| edges incident to T leave it. Every vertex outside T has at most d-1 neighbors in T (d is even). Thus d|T| <= (d-1)(2^d-|T|), giving the upper bound. As q<=d<2q, the lower bound is at least (1/2-1/d)2^d. Both normalized bounds tend to 1/2. More explicitly, the normalized deficit is at least 1/(4d-2) and at most 1/(2q)<=1/d. QED.

## Exact result for sets confined to one parity class at power-of-two dimensions

For an odd independent set contained in one parity class, every vertex of the opposite parity must have at least one neighbor missing from the set, because d is even. Double-counting edges from the missing vertices proves that at least 2^(d-1)/d vertices of the chosen parity class must be omitted. If d is a power of two, the construction above attains this bound exactly. This is an exact optimum among one-parity sets, not a claim of exact unrestricted optimum.

## Verification and scope

The companion verify.py exhaustively checks all 349,524 vertices over dimensions 2,4,...,18, including independence, all neighbor counts and the exact size formula. The proof is independent of the finite check.

A targeted literature search found the original question and related extended Hamming-code constructions in open-packing literature, but no earlier resolution of this asymptotic question. The latest arXiv revision could not be retrieved directly in this session; publication priority and external review remain unverified. Exact unrestricted values in arbitrary even dimensions are not established here. The construction uses standard linear coding ideas.
