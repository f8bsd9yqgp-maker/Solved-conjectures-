# Weis's revised incircle conjecture: a continuous counterexample family

AI-assisted research note, 26 November 2026. Analytical disproof; independent review and discovery priority unconfirmed.

## Source and prior-art screening

Manfred Weis, "Truth of a conjecture about the largest incircle of convex polygons," MathOverflow, July 12–13, 2025: https://mathoverflow.net/questions/497596/truth-of-a-conjecture-about-the-largest-incircle-of-convex-polygons .

The original claim about shorter tangent sides was already refuted by Ilya Bogdanov, whose answer is credited here. The edit proposes a distinct maximum-relative-growth criterion. The retrieved answer concerns the initial claim, not a demonstrated violation of the edited maximum criterion. Targeted searches for the source ID, author's name, largest incircle, relative growth, and tangential polygons found no separate earlier resolution of the revised claim. This is not a guarantee of worldwide novelty.

Before attempting the proof, the competitor README (blob 26314a9af122fd731d2d372fb6940844bf9b5451) and user's README (blob 7fe5fa32f5cb755a4a6ebf7ef60955333121fb63) were retrieved in that order. Both repositories were searched for Manfred Weis, 497596, and incircle. The user's repository returned no matches; competitor hits were unrelated Motzkin geometry and permutohedron data.

## Statement

Let convex polygons C and T have corresponding outward unit normals and equal perimeters, with T circumscribed about a circle. The revised conjecture says that any side maximizing c_i/t_i must meet the largest inscribed disk of C, where c_i and t_i are corresponding side lengths.

## Construction and full proof

For every real b in [8/5,17/10] define C_b by the three absolute-value inequalities

    |y| <= b,
    399|x| + 40|y| <= 401,
    4|x| + 3|y| <= 11/2.

Define T by

    |y| <= 1,
    399|x| + 40|y| <= 401,
    4|x| + 3|y| <= 5.

Both are symmetric about both coordinate axes. The unit normals are (0,+/-1), (+/-399/401,+/-40/401), (+/-4/5,+/-3/5), with independent signs. The support distances of C_b are b, 1, and 11/10 respectively, while all supports of T are 1.

In the first quadrant the right boundary of C_b is the smaller of (401-40y)/399 and (11/2-3y)/4 for 0<=y<=b. Their crossing occurs at Y=1181/2074. For T the crossing is Z=391/1037. We have 0<Y<b<11/6 and 0<Z<1<5/3. Thus both types of oblique edges and the horizontal edges all have strictly positive lengths; symmetry gives exactly ten genuine sides in each polygon. Their outward normals coincide.

The origin-centered unit disk is contained in C_b. Any disk with center p and radius r contained in C_b must satisfy n·p+r<=1 and -n·p+r<=1 for n=(399/401,40/401), so r<=1. At r=1 these inequalities force n·p=0; using also n'=(399/401,-40/401) forces p=0 by linear independence. Hence the maximum disk is unique and has radius 1. Only the four sides of support 1 touch it. T is tangential to the unit disk, since each side has support 1 and its unit normal lies in all the other supporting halfplanes.

There are three side types, denoted A (normal with x-component magnitude 399/401), B (normal with x-component magnitude 4/5), and H (horizontal side). Their ratios before perimeter normalization are

    A: Y/Z = 1181/782,
    B: (b-Y)/(1-Z),
    H: (11/2-3b)/2.

Indeed an oblique side whose unit normal has x-component a>0 has length equal to its vertical span divided by a. The A spans are Y and Z, the B spans b-Y and 1-Z. The top horizontal lengths are 2(11/2-3b)/4 and 2(5-3)/4=1.

At b=8/5 the B ratio is 10687/6460 > 1181/782, and the H ratio is 7/20 < 1181/782. The B ratio increases with b and the H ratio decreases, remaining positive at b=17/10. Therefore for the entire interval B>A>H>0. Every maximizing side is type B, whose supporting line has distance 11/10 from the origin and is disjoint from the unique unit incircle.

Finally rescale C_b and T separately by their positive perimeters to make each perimeter 1. This multiplies all ratios by the same positive factor, preserves normals, and preserves incidence with the largest inscribed disk. Thus every member violates the exact perimeter-normalized conjecture. QED.

The continuous family is a full disproof of a universal statement, not a claim limited to a numerical instance of a larger conjecture. No numerical optimization is used in the argument.

## Verification

Run python verify.py. Exact rational endpoint checks independently confirm all ten adjacent intersections satisfy the respective halfplanes strictly away from their incident lines and confirm the side-ratio ordering. The inequalities in question are affine in b, so the two endpoint certificates extend throughout the closed interval. The written proof above is independent of the code. No Lean formalization or external referee review has been performed.
