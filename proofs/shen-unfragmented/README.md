# Shen's unfragmented-set conjecture: hereditary fragmentation and four-element obstructions

AI-assisted mathematical research note, 26 November 2026. Written proof under explicit ordering conventions; independent review and discovery priority remain unverified.

## Source and screening

Yu-Fu Shen, MathOverflow, 3 March 2025, edited 10 March 2025:
https://mathoverflow.net/questions/488756/conjecture-on-the-preservation-of-unfragmented-sets-under-element-addition

Both repository README indexes were fetched before choosing the candidate, competitor first:
- https://github.com/1337isnot1337/solved-conjectures (README blob 26314a9af122fd731d2d372fb6940844bf9b5451)
- https://github.com/f8bsd9yqgp-maker/Solved-conjectures- (README blob 78eb9a6616e5b9369cfb0eec13f5e6e2587f8792)

Default-branch searches for unfragmented, Yu-Fu Shen, and 488756 returned zero matches in each repository. Both were searched again for unfragmented immediately before submission, with zero matches. The original post, reopened on November 26, displayed no answers and one comment requesting clarification about comparison. Targeted public searches using the title, author, source ID and edge-ordering terminology found no exact prior resolution. Related edge-ordered graph terminology is found in *Turán problems for edge-ordered graphs* (https://www.sciencedirect.com/science/article/pii/S0095895622001265). This is targeted screening, not a certification of worldwide priority or exhaustive full-text review.

## Statement and conventions

Given a finite set A of pairwise incomparable elements and a commutative pair operation whose outputs can be compared, associate each unordered pair {a,b} with its output a ⊗ b. Order these indexed pairs by output value. On a remaining set of m>=2 elements, consider the first m-1 pairs. If some element occurs in all of them, delete that element and repeat. Otherwise stop. The set is fragmented if the process deletes every element; otherwise it is unfragmented. A singleton is removed automatically, as is implicit in the stated goal of reaching the empty set. At size two either endpoint may be deleted and both choices succeed.

The original conjecture states that adjoining an admissible element to an unfragmented set leaves it unfragmented.

For equal output values we use a single total ordering of indexed pairs refining the value order, inherited under restriction. This is automatic for distinct values. The original question does not specify a tie rule; variants are treated separately below.

## Theorem 1 (hereditary fragmentation)

Every subset of a fragmented set is fragmented under the inherited pair order.

Proof. The first m-1 pairs form the entire star centered at the deleted vertex v: there are exactly m-1 incident pairs and all have been selected. Thus v is removable exactly when every pair incident to v precedes every pair not incident to v.

Suppose v_1,...,v_n is a successful deletion order of A, with the final singleton removed by convention. For every i, each pair v_i v_j (j>i) precedes every pair v_r v_s (i<r<s). Restrict this ordering of vertices to an arbitrary subset B. Each comparison needed at a deletion step of B was already valid in A, so the first vertex of the restricted order is removable, as are all successive vertices. This proves fragmentation of B. For m>=3 a removable vertex is unique (two distinct stars cannot be the same set of m-1 pairs), so the restricted successful order is consistent with the procedure. At m=2 either endpoint works. QED.

Taking the contrapositive with B=A and the larger set A∪{x} proves Shen's conjecture, even for addition of arbitrarily many elements.

## Theorem 2 (four-element obstruction)

An ordered complete graph is fragmented if and only if every four-element induced subset is fragmented. For fewer than four vertices fragmentation is automatic. Equivalently, every unfragmented set contains four elements whose first three induced pairs do not form a star.

Proof. Necessity follows from Theorem 1. For sufficiency suppose n>=4 and every four-element subset has its first three edges forming a star. Use induction on n. Write ab for the globally earliest pair. The second pair must meet ab: otherwise the four endpoints would contain these two disjoint earliest pairs, preventing a star. Relabel the endpoints so the second pair is ac.

For any d outside {a,b,c}, the quartet {a,b,c,d} has earliest edges ab and ac, so its first three must be ab, ac, ad. In particular ax precedes bx whenever x is distinct from a and b: for x=c this follows from ac being globally second; for x outside {a,b,c} it follows from that quartet.

For any distinct x,y outside {a,b}, the quartet {a,b,x,y} contains globally earliest ab, so its star center must be a or b. Since ax precedes bx, center b is impossible (a star centered at b would put bx before ax). Therefore the center is a. It follows in particular that for every three distinct vertices a,x,y, the two pairs ax and ay precede xy: when neither x nor y is b use {a,b,x,y}; when one is b use ab globally first and the established ax<bx comparison.

Finally compare arbitrary pairs az and xy, where a is distinct from x,y. If z equals x or y, the preceding observation gives az<xy. Otherwise use the quartet {a,z,x,y}. Its star center must be a: for each potential center w≠a choose another non-a vertex q in that quartet; the pair aq precedes wq by the observation, contradicting the requirement that all edges at w precede all edges not at w. Hence az<xy also in this case.

All n-1 edges incident to a therefore precede every other edge; a can be removed. The remaining set inherits the four-element hypothesis, so induction finishes its deletion. QED.

The four-element bound is sharp: order the six pairs on {a,b,c,d} with ab, ac, bc first. This is not a star, but every proper subset has at most three vertices and fragments.

## Counting corollary

For n>=2, the number F(n) of total orders on the indexed pairs of a labeled n-set that are fragmented is

    F(n) = (n!/2) × product_{j=1}^{n-1} j!.

Indeed F(2)=1, and for n>=3 the first center is unique, with n choices; its n-1 incident pairs may occur in any of (n-1)! orders, and the remaining pair order can be any fragmented order on n-1 vertices. Thus F(n)=n(n-1)!F(n-1). In particular F(4)=144 of 720 orders and F(5)=17,280 of 3,628,800 orders.

## Equal values and scope

- Distinct values or a fixed, restriction-consistent tie-break: the original conjecture and both theorems hold.
- If fragmented means that at least one refinement of the tied values permits complete deletion, Theorem 1 follows by restricting that successful refinement. Thus its contrapositive also holds.
- If fragmented means that every refinement permits complete deletion, Theorem 1 follows because any refinement on a subset extends to a refinement on the whole set (insert the other pairs in their value classes). Thus its contrapositive holds here too.
- If ties are re-sorted arbitrarily and independently between the smaller and larger sets, the classification need not be well-defined by the values alone. For example, make every pair value equal. On four vertices select ab, ac, bc first, causing failure. On the five-vertex extension select all four pairs incident to the new vertex first, then use a star-first ordering on the remaining four. This makes the larger set fragmented under independent tie choices, but is not a counterexample under a fixed inherited ordering.

The four-element characterization was proved for a fixed total order; no claim is made here about its analogue with existential/universal tie quantifiers.

## Verification

Run python verify.py. The script enumerates all 720 four-vertex edge orders, generates all 17,280 fragmented five-vertex orders, and checks a deterministic 5,000-order sample on each of n=5,6,7. The 33,000 checks passed when rerun immediately before submission. See verification.txt. These are supplementary sanity checks; the written arguments cover every finite size.

No hillclimb, numerical optimization, or unproved computational reduction is used. The proof is not Lean-formalized or independently refereed.
