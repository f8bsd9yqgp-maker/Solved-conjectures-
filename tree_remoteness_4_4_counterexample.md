# Counterexample to Conjecture 4.4: Minimum remoteness with prescribed tree segment lengths

**Date:** 2026-11-23 (US Central time). **Status:** exact counterexample, computationally checked; external review pending. AI-assisted investigation using ChatGPT; independent attribution and novelty review pending.

Source: Imran Allie, Brandon Du Preez, Zion Hefty, Sonwabile Mafunda, *Proximity and Remoteness in Trees with given Segment Sequence*, arXiv:2611.27685v1, Conjecture 4.4 (20 November 2026), https://arxiv.org/html/2611.27685v1 .

## Statement and construction

The conjecture asserts that a remoteness-minimizing tree with prescribed segment lengths can be chosen with at most two branch vertices. Take
D = (408, 213, 175, 67, 65, 65, 65, 8, 1 repeated 15 times).
Join A--B by a path of length 408 and B--C by a path of length 213. Attach pendant paths of lengths (65,65,65) to A, (175,67,8) to B, and fifteen length-one paths to C. All subdivisions use fresh vertices. There are 1082 vertices and 23 maximal segments.

## Exact proof

Let S=1081, C0=sum(l(l+1)/2 for l in D)=130391, and B(l)=l(S-l). For any leaf v, orient segments away from v. Each segment of length l whose nearer endpoint is at distance d contributes ld+l(l+1)/2 to the transmission (count its l vertices excluding the nearer endpoint). Consequently transmission is C0+F(v), where F(v)=sum(l*d). A maximum transmission is achieved at a leaf: for a non-leaf vertex at least one incident component has at most (n-1)/2 vertices; moving into that component increases transmission by n-2 times its size (i.e. n minus twice its size). Thus rho=(C0+max F)/S.

For a leaf on a pendant segment of length p at A, B or C, its adjusted transmission is B(p) plus the adjusted transmission of that branch vertex. B(p) is increasing for all lengths here (p <= 408 < S/2). Writing X=195, Y=250, Z=15 for pendant totals at A,B,C, the maxima are:
- A: B(65)+408*(Y+213+Z)+213*Z = 264259.
- B: B(175)+408*X+213*Z = 241305.
- C: B(1)+213*(X+408+Y)+408*X = 262329.

Hence max F=264259 and rho=394650/1081.

Every starlike competitor has max F=B(408)=274584. Every two-branch competitor with a pendant length-408 segment has max F at least B(408). It remains to check the two-branch trees whose sole internal segment has length 408.

Let q be the total pendant length on the side not containing the length-213 pendant segment, and p the largest pendant length on that side. The other side has largest pendant 213. Directly from the transmission formula, max F equals
max(184884+408*q, 274584+B(p)-408*q).

If this maximum were <=264443 then q<=194. For p=1,8,65,67,175 respectively, the second term requires q>=28,46,187,192,414 respectively (integer ceilings). But under q<=194, the largest attainable q for p=1,8,65,67 is respectively 15,23,153,155; for p=175 the bound q<=194 already contradicts q>=414. These are all possibilities. Thus every such competitor has max F>=264444. Equality is achieved by choosing the three length-65 pendants on the side not containing 213 (q=195).

Therefore the best one- or two-branch competitor has rho=394835/1081, strictly greater than 394650/1081. The gap is exactly 185/1081. No determination of the global minimizer is needed to refute Conjecture 4.4.

## Reproduction

Run the accompanying tree_remoteness_4_4_verify.py with Python 3; it enumerates all multiset bipartitions for every possible internal length and independently evaluates graph distances for the explicit subdivided tree.

This is a negative resolution of the stated conjecture, not a claim to have characterized all minimizing trees. Please report any errors or prior counterexamples.
