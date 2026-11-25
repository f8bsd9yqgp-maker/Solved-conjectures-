# Graffiti.pc Conjecture 76: counterexample

AI-assisted research note, 25 November 2026. Independent review and publication priority remain unverified.

Source: Ermelinda DeLaViña, *Written on the Wall II*, Conjecture 76 (announced April 4, 2004), catalogue updated November 5, 2026, p. 45: https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf

The conjecture asserts that the maximum order t(G) of an induced tree in a simple connected graph is at least f/floor(d_avg), where f is the number of vertices attaining the maximum number of incident triangles.

## Construction and proof

Let G consist of five disjoint copies of K4, one central and four peripheral. Label the central vertices 0,1,2,3 and the peripheral blocks 4..7, 8..11, 12..15, 16..19. Add precisely the bridges (0,4), (1,8), (2,12), (3,16).

There are 20 vertices and 5*6+4=34 edges. Every vertex belongs to exactly three triangles, all within its own K4. Thus f=20 and floor(d_avg)=floor(68/20)=3.

An induced tree contains at most two vertices of any clique, as three form a triangle. If it meets the central block, it contains at most two central vertices and can meet only the peripheral blocks attached to those vertices: the bridges are the sole connections. Its order is at most 2+2*2=6. If it misses the central block, connectivity confines it to one peripheral clique, so its order is at most two. The set {0,1,4,5,8,9} induces a six-vertex path. Hence t(G)=6 and 6<20/3, disproving the conjecture.

## Infinite family

For an integer L>=1, replace each peripheral K4 by a chain of L copies of K4 connected by individual bridges. Use distinct incoming and outgoing attachment vertices within any internal peripheral clique. There are 4(1+4L) vertices and 6(1+4L)+4L edges. Every vertex still belongs to exactly three triangles, and the average degree lies strictly between 3 and 4. A connected induced tree meeting the central clique intersects at most two branches and at most two vertices per block, so has order at most 2+4L. This bound is attained by selecting two central vertices and two vertices per block in their branches, including bridge endpoints. A tree missing the central clique cannot exceed 2L. Therefore t=2+4L < 4(1+4L)/3 for every L>=1, giving an unbounded additive violation.

## Verification

Run python3 verify.py. The independent finite check enumerates all 77,520 seven-vertex subsets, checks no induced tree of that order exists, checks a six-vertex witness, and counts triangles exactly. Larger induced trees would contain seven-vertex induced subtrees by leaf deletion. The proof does not depend on the enumeration.

No claim of first discovery is made; the November catalogue lists the conjecture open and a targeted search found no earlier resolution, but that is not exhaustive. No proof-assistant verification or external peer review has been completed.
