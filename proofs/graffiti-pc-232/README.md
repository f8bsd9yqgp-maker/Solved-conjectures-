# Graffiti.pc Conjecture 232 — Radius and peripheral eccentricity

25 November 2026. AI-assisted candidate proof; independent review and discovery priority pending.

[Original catalogue](https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf), entry 232, announced 23 February 2007, marked open in the November 2026 text. Page image retrieval failed, but the statement and definitions were retrieved as text.

For every finite connected simple graph G of order at least two, let B be the periphery and t=max_x d(x,B), using zero when B=V. Then gamma_t(G) >= (rad(G)+t)/2.

Proof. Let D be a minimum total dominating set, k=|D|, and c the number of components of G[D]. Each component has at least two vertices, so c<=floor(k/2). Assign each vertex outside D to a component containing a neighbor. The quotient of these clusters is connected. Each edge of a quotient spanning tree joins two D-components by a path with at most two additional vertices. Thus a connected vertex set S containing D exists with |S|<=k+2(c-1)<=2k-2. Form a spanning tree T of G by taking a tree on S and attaching all other vertices as leaves adjacent to D.

If t>0, select a diametral pair p,q and x with d(x,B)=t. They have pairwise G-distances at least t. Let m be their median in T. For every z, two of p,q,x can be chosen so that their connecting path meets the m-z path only at m: if m is one of the three, use m and a vertex in a branch not containing z; otherwise use two branches not containing z. (If z=m any pair suffices.) Their union is a subtree with at most three leaves outside S: its only possible such vertices are the two selected vertices and z. Hence the sum of the two path lengths is at most |S|+2<=2k. The first path has length at least t, so d_G(m,z)<=2k-t. Maximizing over z proves rad(G)+t<=2k.

If t=0, any path in T has at most two vertices outside S, hence length at most |S|+1<=2k-1. Therefore rad(G)<=rad(T)<=k, which implies the desired inequality. QED.

The previous chat reported an exhaustive atlas check on 995 connected graphs of orders 2–7. The proof above is independent of that computation. No claim of first discovery or Lean verification.
