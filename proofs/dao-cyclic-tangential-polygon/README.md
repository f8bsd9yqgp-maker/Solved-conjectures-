# Đào Thanh Oai's cyclic–tangential polygon conjecture

AI-assisted research note, 26 November 2026. General proof and interior equality characterization under the standard perpendicular-to-side-line interpretation. Independent review and worldwide priority remain unverified.

## Source and screening

Original conjecture: Oai Thanh Đào, 24 July 2016, https://mathoverflow.net/questions/244984/an-inequality-in-cyclic-polygon-and-tangential-polygon (edited July 2024). The retrieved discussion displayed no answers, but included comments about obtuse triangles and a suggested nonregular equality case. The author cites the already-proved triangle case: T. O. Dao, T. D. Nguyen, N. M. Pham, A strengthened version of the Erdős–Mordell inequality, Forum Geometricorum 16 (2016), 317–321. Another triangle paper is D. S. Marinescu, M. Monea, About a strengthened version of the Erdős–Mordell inequality, Forum Geometricorum 17 (2017), 197–202. Neither full text was retrieved successfully; no novelty is claimed for triangles. Targeted searches for the exact title, source ID, author, tangential/cyclic polygon and Erdős–Mordell terminology located related inequalities but no full resolution of this precise general conjecture. Known classical discrete spectral inequalities are used, not claimed as new.

Before research, the competitor README (blob 26314a9af122fd731d2d372fb6940844bf9b5451) and user's README (blob 57b2830ecf2576d7733557c0c787161d35875b26) were retrieved in that order. Searches in both repositories for 244984, tangential polygon, Erdős–Mordell and cyclic tangential polygon conjecture found no relevant entry. Competitor numeric matches were unrelated Lean data, and its polygon match was the Erdős–Oler packing research log. This is targeted screening, not an exhaustive full-text priority certification.

## Statement

Let A_0,...,A_{n-1} be distinct points on a circle of radius R>0 in cyclic order, n>=3, and let P be in their convex hull K. Write d_i(P) for the perpendicular distance to the full line through A_i and A_{i+1}, with indices modulo n, and D_i(P) for the perpendicular distance to the tangent to the circle at A_i.

Then

    sum_i D_i(P) >= sec(pi/n) sum_i d_i(P).

At an interior point of K, equality holds if and only if the polygon is regular.

When the tangent lines form the usual bounded circumscribed polygon, their side lines are exactly these tangent lines, giving the original conjecture. If the circle center is outside or on the boundary of K, the tangent halfplanes can instead form an unbounded region; the same line-distance assertion still holds. Distances to finite side segments, rather than their supporting lines, are not asserted.

## Proof

Translate the circle center to the origin and let A_i = R(cos theta_i, sin theta_i), with theta_0 < ... < theta_{n-1} < theta_n=theta_0+2pi.

The tangent distance is D_i(P)=R-P dot (cos theta_i,sin theta_i), since K lies in the closed disk. Write m_i=(theta_i+theta_{i+1})/2. The chord distance is

    d_i(P) = R cos((theta_{i+1}-theta_i)/2) - P dot (cos m_i,sin m_i).

The sign is nonnegative on K: every other cyclic vertex lies on the complementary arc and hence on the indicated inner side of the chord. This is valid even for a gap greater than pi. Both distances are affine functions on K. Consequently the difference

    F(P)=cos(pi/n) sum_i D_i(P) - sum_i d_i(P)

is affine on K, and it suffices to prove F at the vertices.

Relabel cyclically so the tested vertex is A_0 and rotate to theta_0=0, theta_n=2pi. Put x_i=sin(theta_i/2), i=0,...,n. Thus x_0=x_n=0 and x_i>0 for 0<i<n.

At P=A_0, the elementary trigonometric identities give

    D_i(A_0)=R(1-cos theta_i)=2R x_i^2,
    d_i(A_0)=R[cos((theta_{i+1}-theta_i)/2)-cos((theta_i+theta_{i+1})/2)]
            =2R x_i x_{i+1}.

It follows that

    F(A_0)/(2R) = cos(pi/n) sum_{i=1}^{n-1} x_i^2
                  - sum_{i=1}^{n-2} x_i x_{i+1}.

For completeness, prove this expression is nonnegative without importing any external theorem. Set s_i=sin(i pi/n), i=0,...,n. Then s_0=s_n=0, all interior s_i>0, and s_{i-1}+s_{i+1}=2 cos(pi/n)s_i. Direct expansion gives the exact identity

    cos(pi/n) sum_{i=1}^{n-1} x_i^2 - sum_{i=1}^{n-2} x_i x_{i+1}
    = (1/2) sum_{i=1}^{n-2} s_i s_{i+1}(x_i/s_i-x_{i+1}/s_{i+1})^2 >= 0.

This is also the Rayleigh quotient bound for the path adjacency matrix of order n-1, divided by two. The proof applies at every cyclic vertex and therefore throughout K by affinity. QED.

## Equality

The sum-of-squares expression vanishes exactly when x_i=c s_i for all 1<=i<n, for a positive constant c. In particular x_1=x_{n-1}; at the vertex used as A_0, the lengths of its two incident sides are therefore equal, since those lengths are 2R x_1 and 2R x_{n-1}.

Every interior point P of the convex hull can be written as a convex combination of all vertices with strictly positive coefficients. For example, their mean Q is interior; for sufficiently small positive epsilon, P'=(P-epsilon Q)/(1-epsilon) lies in K; express P' as any convex combination of vertices. Since all vertex gaps F(A_i)>=0, interior equality forces equality at every vertex. Thus each pair of consecutive sides has equal lengths, so all sides have the same length.

A cyclic polygon with distinct vertices and equal side lengths is regular: its positive consecutive central gaps must each equal either alpha or 2pi-alpha for a fixed alpha in (0,pi]. If one gap is 2pi-alpha>pi, all remaining gaps equal alpha, and the total would be 2pi+(n-2)alpha>2pi, impossible. Alpha=pi is also impossible for n>=3. Hence all gaps equal 2pi/n. Conversely, in a regular polygon each vertex has x_i=s_i, giving equality at every vertex and hence throughout K. The factor sec(pi/n) is sharp.

## Verification and limitations

The analytic proof is independent of computation. A deterministic floating-point check over regular and randomly generated cyclic polygons with n=3,...,50 passed: 4,848 polygons, 133,320 vertex/interior checks, and 48 regular equality checks. Tolerance 1e-10. Run python verify.py; this is a sanity check, not an exact proof or formal verification. The proof's line-distance convention and the inability to retrieve two historical full texts must be retained in any novelty claim.
