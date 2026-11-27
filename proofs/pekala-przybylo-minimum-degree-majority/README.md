# The sharp minimum-degree threshold for generalized majority edge-colourings

27 November 2026 — AI-assisted candidate proof; independent review and publication priority pending.

## 1. Target and source

Paweł Pękała and Jakub Przybyło, *On Generalised Majority Edge-Colourings of Graphs*, Electronic Journal of Combinatorics 31(4) (2024), #P4.66, DOI https://doi.org/10.37236/12416, Conjecture 11, p. 8; https://arxiv.org/abs/2309.16624.

The conjecture states that for every integer k >= 2 and every finite simple graph G of minimum degree at least k^2, there is an edge-colouring with k+1 colours in which the number of incident edges of any single colour at v is at most floor(d_G(v)/k). This is ordinary generalized majority edge-colouring, not the strong-majority condition on edge neighbourhoods. The source proves k <= 4 and the bipartite case; the proof below handles every k and does not assume bipartiteness. No list-colouring claim is made.

## 2. Classical input

Hilton and de Werra's equitable edge-colouring theorem states that a finite simple graph H admits an equitable edge-colouring with L colours, for an integer L >= 2, if no vertex degree of H is divisible by L. Equitable means that at each vertex the counts of any two colours differ by at most one. In particular each colour occurs at most ceil(d_H(v)/L) times at v.

Reference: A. J. W. Hilton and D. de Werra, *A sufficient condition for equitable edge-colourings of simple graphs*, Discrete Mathematics 128 (1994), 179–201, https://doi.org/10.1016/0012-365X(94)90112-0. The exact hypothesis is corroborated by the original abstract and Theorem 3 of Antoniuk, Prorok and Salia, https://arxiv.org/abs/2607.00212 (p. 2). Some PDF text extraction loses the negation slash; the page image explicitly says L does NOT divide the vertex degree. The full 1994 article was not accessible directly during this audit; the theorem is used as an established result, not reproved here.

## 3. General capacity lemma

Let L >= 2 and let G be a finite simple graph. Assign a positive integer capacity b(v) to each vertex, satisfying d_G(v) <= L b(v)-1. Then there is an L-edge-colouring of G with d_c(v) <= b(v) for every vertex and colour.

Proof. For every original vertex v whose degree is divisible by L, attach exactly one fresh pendant vertex to v; use distinct fresh vertices. Let H be the resulting graph. Every original vertex now has degree not divisible by L, and every new vertex has degree one. H is simple. The classical theorem gives an equitable L-edge-colouring of H. For each original vertex, d_H(v) <= d_G(v)+1 <= L b(v), so every colour occurs at most ceil(d_H(v)/L) <= b(v) times. Restrict to the edges of G. Counts cannot increase. QED.

The lemma also covers isolated vertices if their capacity is positive (their new degree is one). An equivalent slightly wasteful construction pads each original vertex to L b(v)-1 using distinct leaves. The one-leaf version above is enough.

## 4. Proof of Conjecture 11

Fix k >= 2 and G with minimum degree at least k^2. Write d_G(v) = k q_v + r_v by Euclidean division, with q_v >= k and 0 <= r_v <= k-1. Then

    (k+1) q_v - d_G(v) = q_v - r_v >= 1.

Thus the capacity lemma applies with L=k+1 and b(v)=q_v=floor(d_G(v)/k). It yields a colouring with k+1 colours and

    d_c(v) <= q_v <= d_G(v)/k

at every vertex for every colour. This is precisely Conjecture 11. QED.

No bounded-order assumption, fixed k assumption, numerical computation or conjectural lemma enters this proof. It is a direct corollary of the published equitable-colouring theorem.

## 5. Sharpness (prior work, restated for completeness)

Observation 10 of Pękała–Przybyło gives the following construction. Start with K_{k^2+1}, remove a Hamiltonian cycle, and add a new universal vertex u. Each old vertex has degree k^2-1; u has degree k^2+1. If a 1/k-majority (k+1)-edge-colouring existed, each old vertex would have exactly k-1 incident edges of each colour, since (k+1)(k-1)=k^2-1. The apex has degree k^2+1, and some colour must appear k times there (its cap is k). The degree sum of that colour class would be (k^2+1)(k-1)+k, an odd number for every k. This contradicts the handshake lemma. Thus minimum degree k^2-1 is not sufficient. Together with Section 4 the sharp threshold is exactly k^2. The lower-bound construction is the original authors' result, not a new discovery.

## 6. Method transfer and scope

The earlier Achour saturation counterexample used pendant ports and controlled composition to modify graph structure while preserving an exact global invariant. Here the adapted operation is the addition of at most one pendant port per original vertex, followed by restriction, which preserves the desired local capacity. The earlier Eulerian strong-majority project isolated modular obstructions and repaired them before applying a periodic colouring. Here the obstruction is vertex degree zero modulo the number of colours; padding removes it everywhere. The actual colouring existence theorem is Hilton–de Werra's published theorem. Neither earlier candidate proof is a logical prerequisite, and the result is not a resolution of the broader strong-majority four-colour conjecture or the arbitrary-list extension.

## 7. Priority and duplicate audit

On 27 November 2026, the original journal article (Conjecture 11 and Observation 10) was inspected, including its page image. Searches by title, authors, conjecture number, arXiv identifier, and combinations of majority colouring, equitable colouring and Hilton–de Werra retrieved the original and related work but did not identify a previous general resolution. MathDB problem 367168 lists the general conjecture as open: https://mathdb.com/p/367168/the-minimum-degree-conjecture-for-majority-edge-colourings . The public searches are bounded and cannot rule out unindexed, unpublished or private work. This is a particularly short deduction from a 1994 theorem, so earlier implicit or explicit recognition is a meaningful priority risk.

Both GitHub repositories were checked using their README, code searches for 2309.16624, Pękała, generalised majority, and majority edge, plus issue searches. No matching completed resolution was found. Competitor: https://github.com/1337isnot1337/solved-conjectures (README blob e0493dac21e0169522567c34aca30f532c0cca55). User: https://github.com/f8bsd9yqgp-maker/Solved-conjectures- (README blob 2a9a67ab9dd15817123d657a0238187fd5c106a5). The user's Eulerian strong-majority entry concerns a different statement. The competitor's unrelated search hits are not a resolution of this conjecture.

No formal proof-assistant verification or computational colouring test is claimed. The candidate proof was emailed to both original authors on 27 November 2026 and submitted to this repository. The proof is analytical and depends on a classical theorem whose statement is checked against multiple sources. Independent review and priority confirmation remain pending.