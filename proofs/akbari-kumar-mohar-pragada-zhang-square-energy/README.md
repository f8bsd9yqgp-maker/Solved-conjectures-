# A proof of the unrestricted Akbari–Kumar–Mohar–Pragada–Zhang positive square-energy conjecture

Research continuation, November 24, 2026 (US Central). Status: complete written candidate proof, self-audited, with exact rational certificates for a finite set of analytic bounds. Not independently peer reviewed; no Lean compilation or established discovery priority. The proof treats arbitrary finite connected simple graphs, not just graphs of bounded cycle rank or minimum degree. The companion verifier uses only Python's standard-library rational arithmetic. It verifies eight explicit rational inequalities; no graph enumeration is a premise of the proof.

## 1. Main statement and outline

**Theorem.** For every finite connected simple unsigned graph G with n vertices and m≥n+1 edges, the sum of the squares of the strictly positive adjacency eigenvalues satisfies s⁺(G)>n.

In particular this proves the non-strict inequality proposed in Conjecture 1.2 in Akbari, Kumar, Mohar, Pragada and Zhang, *Refinement of a conjecture on positive square energy of graphs*, arXiv:2506.07264 (2025).

Notation: A denotes the real symmetric adjacency matrix; A=A₊−A₋ is its orthogonal spectral splitting into positive semidefinite parts. Thus s⁺=||A₊||²_F, s⁻=||A₋||²_F, and s⁺+s⁻=2m. The cycle rank of a connected graph J is r_J=|E(J)|−|V(J)|+1. A block is a maximal 2-connected subgraph or a bridge K₂. Cycle ranks add over blocks, since edge sets partition the edges and sum_B(|V(B)|−1)=|V(G)|−1. A 2-connected graph here has at least three vertices. Empty induced graphs have zero spectral sums and determinant one.

The proof consists of four ingredients:

1. A quantitative doubly nonnegative (DNN) matrix bound excludes any graph having a triangle-free 2-connected noncycle block.
2. A minimal-counterexample argument using entire rooted vertex clusters, rather than individual vertex deletion, shows that every remaining noncomplete noncycle block has a vertex on a triangle whose deletion leaves a tree or a unicyclic graph with a cycle of length 1 modulo 4.
3. Uniform determinant-phase integral estimates show that each such block, even with arbitrary vertex deletions, contributes less than its cycle rank minus one to the possible spectral deficit. The nontrivial unicyclic remainder is handled for every possible degree: eight exact rational bounds and one analytic estimate for all larger degrees.
4. The determinant phase is subadditive under the block decomposition after taking the maximum over induced subgraphs. Summing block estimates contradicts the existence of a minimal counterexample.

The DNN framework in Sections 2–3 is based on Liu–Tang–Zhang (arXiv:2607.18031), the block-deficit formulation of Akbari–Hu–Liu (arXiv:2609.06778), and the simplified deletion-envelope combination of Hu–Han (arXiv:2608.18492). Details are reproduced below; the remaining arguments do not assume the published minimum-degree-two theorem. The quantitative triangle-free lemma and the phase analysis are developed from the preceding research execution. The new closing step is Sections 5–7.

## 2. DNN machinery

For connected H with at least two vertices put q(H)=2|E(H)|-|V(H)|+1. A DNN matrix is PSD and entrywise nonnegative. Define D(H) to be the DNN matrices supported on the diagonal and edges of H, S_H(M)=sum_{uv in E(H)} sqrt(M_uv), T(M)=1^T M 1, and

    kappa(H)=max_{M in D(H), T(M)=1} 4 S_H(M)^2,
    delta(H)=q(H)-kappa(H).

For a singleton define q=kappa=delta=0. The maximum is attained: entries of the normalized nonnegative matrices lie in [0,1], the PSD and support constraints are closed, and the objective is continuous. Scaling gives the equivalent homogeneous inequality. A nonzero DNN matrix has T>0.

### 2.1 Folding and block splitting

A general DNN matrix M can be made graph-supported by adding, for each distinct unordered nonedge uv, M_uv (e_u-e_v)(e_u-e_v)^T. The summands are PSD, remove the two nonedge entries and preserve edge entries and T. Nonnegativity remains true.

At a cut vertex v, split the components of H-v into two nonempty sets U,W, and write M as a Gram matrix of vectors z_u. The spans of z_u for u in U and for u in W are orthogonal by the support assumption. Decompose z_v into its two orthogonal projections and the residual orthogonal to both. Assign the residual to either side. This yields supported DNN matrices M_1,M_2 on the two connected induced subgraphs H_1,H_2 containing v. Edge entries are preserved, S=S_1+S_2, T=T_1+T_2, and q=q_1+q_2. Cauchy–Schwarz gives kappa(H)≤kappa(H_1)+kappa(H_2). Recurse down the block-cut tree:

    delta(H) ≥ sum_{blocks B} delta(B).                 (2.1)

### 2.2 Deletion envelopes (Liu–Tang–Zhang)

For a 2-connected B of order N≥3 and size M_e, write q=2M_e-N+1, D=sum_v delta(B-v), and x=tr(M)/T in [0,1] for a nonzero supported DNN matrix M. Here every B-v is connected. Edge Cauchy–Schwarz gives

    4 S^2/T ≤ 2 M_e (1-x).                              (2.2)

For v, set sigma_v=sum_{u~v} sqrt(M_uv). Apply the defining kappa inequality to the principal matrix M-v:

    2(S-sigma_v) ≤ sqrt(kappa(B-v) T(M-v)).

Sum over v, use Cauchy–Schwarz and the identities

    sum_v (S-sigma_v)=(N-2)S,
    sum_v q(B-v)=(N-2)(q-1),
    sum_v T(M-v)=(N-2)T+tr(M).

This gives

    4 S^2/T ≤ [q-1-D/(N-2)] [1+x/(N-2)].              (2.3)

The first factor is nonnegative by its expression as sum_v kappa(B-v)/(N-2).

### 2.3 Nonnegative deficit on all connected graphs

For K2, 4M_12≤M_11+M_22+2M_12=T by PSD and AM-GM. Hence kappa(K2)≤1=q(K2). Induct on graph order, using block splitting at cut vertices. For a 2-connected graph, D≥0 by induction, so replace D by 0 in (2.3). Take the convex combination of this bound and (2.2) with respective weights (N-1)/N and 1/N (the short proof in Hu–Han, arXiv:2608.18492). The result is

    4 S²/T ≤ q + [q-(N-1)^2] x/[N(N-2)] ≤ q,

because 2M_e≤N(N-1). Thus delta≥0 universally.

### 2.4 Correlation certificate

For any PSD matrix C with C_uu=1 and C_uv<1 on edges, use the Schur trace inequality tr(CM)≥0 (trace of a product of PSD matrices). Support gives

    T(M)≥ 2 sum_{uv in E(H)} (1-C_uv) M_uv.

Weighted Cauchy–Schwarz yields

    4 S_H(M)^2 ≤ [sum_{uv in E(H)} 2/(1-C_uv)] T(M).

Therefore a Gram assignment of unit vectors x_u gives

    kappa(H) ≤ Phi_H(C)=sum_edges 2/(1-<x_u,x_v>).      (2.4)

For a path of length L with specified terminal unit vectors of correlation c, put theta=arccos((-1)^L c). Assign unit vectors along a plane arc with alternating signs, adjusting the orthogonal direction to meet the given terminal vector. This gives each edge correlation -cos(theta/L) and cost

    L sec²(theta/(2L)) = L+L tan²(theta/(2L)).         (2.5)

When endpoints are equal/opposite the plane can be chosen with an added orthogonal direction. The expression L tan²(a/L) decreases for fixed a>0 on a/L in (0,pi/2), as its derivative is tan² z - 2z tan z sec² z<0 for z=a/L. The zero case is immediate. We never use a singular edge cost.

### 2.5 Transfer from DNN to signed square energy

For a signing sigma of the edges, let A=A_sigma be the signed adjacency matrix, with entries ±1 on edges and zero elsewhere (the unsigned case uses all +1). For either spectral part X=A_+ or A_-, X PSD and ||X||_F²=s^±. By Schur product X∘X is DNN with T=||X||_F². The absolute sum of X_uv over edges is at least half the appropriate signed sum, which is s^±/2 because tr(AX)=s^+ for A_+, and -tr(AX)=s^- for A_-. Fold X∘X to graph support. Thus (s^±)^2 ≤ kappa(G)s^±. Connected graphs with an edge have both square energies positive, since tr A=0 and A nonzero. Consequently

    s^±≤kappa(G),
    min(s^+,s^-)≥2m-kappa(G)=n-1+delta(G).             (2.6)

This step applies to EVERY signing. The q bound proves the known n-1 theorem, and delta(G)>1 suffices for strict improvement past n.

## 3. Quantitative triangle-free block lemma

**Lemma.** Every triangle-free 2-connected noncycle B satisfies delta(B)>1.

We prove it by induction on N. All hypotheses concern ordinary unsigned support graphs, not signs.

### 3.1 Cyclic blocks

For a cycle C_L, q=L+1. For even L, choose antipodal alternating unit vectors: Phi=L and delta≥1. For odd L≥5 choose successive alternating vectors on an arc, with total sign-corrected angle pi around the cycle. Edge correlations are -cos(pi/L), so

    delta(C_L) ≥ 1-L tan²(pi/(2L))
                 ≥ 1-5 tan²(pi/10)=2 sqrt(5)-4 > 7/15.

The last identity follows from cos(pi/5)=(1+sqrt(5))/4, and the strict inequality follows from (67/30)^2<5. Let c_0=7/15. Every cyclic block in a triangle-free graph is either a cycle or a triangle-free 2-connected noncycle. Thus if the induction hypothesis holds for smaller blocks, a connected smaller triangle-free graph F with cycle rank r_F satisfies

    delta(F) ≥ 0         if r_F=0,
             ≥ c_0      if r_F=1,
             ≥ 2 c_0    if r_F=2,
             ≥ 1        if r_F≥3.                      (3.1)

Indeed block cycle ranks add. If any noncycle cyclic block is present, its deficit is >1 by the induction hypothesis. Otherwise all cyclic blocks are cycles, each contributing at least c_0; 3c_0>1. Bridge blocks have nonnegative deficit.

### 3.2 Base in cycle rank: r_B=2

The minimum degree of B is at least 2 and sum_v(d_v-2)=2. One degree-four vertex and all other degrees two is impossible: deleting that vertex would leave N-1 vertices and N-3 edges, hence a disconnected graph. Thus exactly two vertices u,v have degree three, with all others degree two. Their three incident chains form three internally vertex-disjoint u-v paths. A chain returning to the same branch vertex would make it a cut vertex, which is forbidden. No two paths have length one because the graph is simple. Their pairwise cycle lengths are at least four because B is triangle-free.

Let their lengths be L1,L2,L3. Choose the terminal correlation and use (2.5) for each path (in separate additional dimensions if required). Denote a path's excess over its length by eta. The desired total cost Phi < M_e+1 = q-1 is equivalent to sum eta<1.

* If one length is 1, take terminal correlation -1/2. That path costs 4/3, excess 1/3. The other lengths are ≥3, and any even one is ≥4. For odd lengths theta=pi/3 and for even theta=2pi/3. Monotonicity in L gives an excess at most 4 tan²(pi/12)=28-16sqrt(3) for either type (for odd lengths use 3 tan²(pi/18)<4 tan²(pi/12)). Total excess at most 1/3+56-32sqrt(3)<1.
* If there is no length 1 and at most one length 2, take orthogonal terminals. Excess of a length 2 path is 6-4sqrt(2); of each length ≥3 path at most 21-12sqrt(3). The former bound is larger than the latter. Total at most (6-4sqrt(2))+2(21-12sqrt(3))<1.
* If at least two lengths equal 2 and the remaining length is even, the graph is bipartite: antipodal vectors on its two parts give zero excess. Otherwise the remaining length is odd and ≥3. Choose terminal correlation +1/2. The two length-2 paths have theta=pi/3 and combined excess 4tan²(pi/12). The odd path has theta=2pi/3, excess at most 3tan²(pi/9)<3tan²(pi/8)=9-6sqrt(2). Total <4(7-4sqrt(3))+9-6sqrt(2)<1.

All numerical inequalities can be certified with rational lower bounds sqrt(2)>1414/1000, sqrt(3)>1732/1000 (squaring). This exhausts theta configurations, and (2.4) proves delta(B)>1.

### 3.3 Induction for r_B=3

Write r=r_B, N=|V(B)|, M_e=N-1+r. The deletion graph B-v has rank r_v=r-d(v)+1. Connectedness gives d(v)≤r+1, while 2-connectivity gives d(v)≥2. Put e_v=d(v)-2≥0; sum e_v=2(r-1). For r=3, e_v is 0,1,2 and r_v=2-e_v. By (3.1), delta(B-v)≥c_0(2-e_v). Thus

    D=sum_v delta(B-v) ≥ c_0(2N-4)=14(N-2)/15.

Mantel gives M_e=N+2≤N²/4, so N≥6 (N=3,4,5 are impossible). For completeness, in a triangle-free graph the neighbor sets of the endpoints of any edge are disjoint, so d(u)+d(v)≤N on every edge. Summation gives sum_v d(v)^2≤N M_e, while Cauchy–Schwarz gives sum_v d(v)^2≥4M_e²/N. This proves the bound. Put x_0=N/(2M_e). For x>x_0 the edge bound (2.2) is strictly below q-1=2M_e-N. For x≤x_0 the deletion bound (2.3) is strictly below q-1 if

    D > N(2M_e-N)/(2M_e+N/(N-2)).                      (3.2)

This equivalence follows by multiplying positive denominators; the first factor of (2.3) is nonnegative. Substitute M_e=N+2 and the displayed lower bound on D. Clearing denominators gives

    13N²-46N-112 > 0.

For N≥6 the left side is 13(N-6)²+110(N-6)+80>0. Hence the strict deficit follows for r=3.

### 3.4 Induction for r_B≥4

Again put e_v=d(v)-2, so 0≤e_v≤r-1, sum e_v=2(r-1), and r_v=r-1-e_v. The bounds (3.1) imply pointwise

    delta(B-v) ≥ 1-e_v/(r-1).                         (3.3)

To see this: for r_v≥3 use delta≥1; for r_v=2 use delta≥2c_0=14/15≥2/(r-1); for r_v=1 use delta≥c_0=7/15≥1/(r-1); and for r_v=0 use nonnegativity. Therefore D≥N-2.

The sufficient strict inequality (3.2) now holds because

    (N-2)(2M_e+N/(N-2)) - N(2M_e-N)
     = N²+N-4M_e ≥ N > 0,

by Mantel. As in §3.3 the edge and deletion envelopes give strictly less than q-1 for all normalized matrices. Compactness of the normalized DNN feasible set ensures its maximum is strictly less than q-1. This completes the induction, including all boundary cases.

## 4. Determinant phase, induced-subgraph envelopes, and cycles

### 4.1 Integral identity

For any real symmetric trace-zero A and t>0 define the continuous phase

    theta_A(t) = sum_j arctan(lambda_j/t).

This is the argument of det(tI+iA), unwrapped continuously from zero at infinity. Each eigenvalue contributes an angle in (-pi/2,pi/2). Direct integration gives

    (1/2) tr(A²) - s⁺(A) = (2/pi) integral_0^infinity t theta_A(t) dt.     (4.1)

Proof: since sum_j lambda_j=0, subtract lambda_j/t from each arctangent before integration. For each real lambda,

    integral_0^infinity t[arctan(lambda/t)−lambda/t] dt
        = −pi lambda |lambda|/4.

Indeed, the derivative of the integrand with respect to lambda is −lambda²/(t²+lambda²), dominated by 1 near zero and a constant times 1/t² at infinity on bounded lambda intervals. Integrating the derivative in t gives −pi |lambda|/2; integrate in lambda from zero. Summing this finite set of identities proves (4.1), including convergence. For adjacency matrices the first term is m.

For any graph J define

    Phi_J(t)=max_{S subset V(J)} theta_{A(J[S])}(t),
    I(J)=(2/pi) integral_0^infinity t Phi_J(t) dt.                         (4.2)

Include the empty set, so Phi_J≥0. The maximum is a finite maximum of continuous functions and is O(t^−3) as t→infinity (trace zero), bounded near zero. In particular every I(J) exists and is nonnegative. Write theta_J for the phase of J itself.

### 4.2 Subadditivity under cut-vertex splitting

For a graph J and a vertex v, order v first, and write b for its real neighbor indicator vector. By the Schur complement,

    z_J = det(tI+iA_J)/det(tI+iA_{J-v})
        = t + b^T(tI+iA_{J-v})^(−1)b.                                     (4.3)

The real part of the inverse is t(t²I+A²)^(−1), which is positive definite. Thus Re z_J≥t>0. Moreover theta_J−theta_{J-v}=arg z_J, the principal argument in (−pi/2,pi/2): both sides are continuous in t>0, agree modulo 2pi, and tend to zero at infinity.

Suppose G is formed from H and K by identifying exactly one vertex v and adding no other cross edges. The matrix of G−v is a direct sum, and (4.3) gives

    z_G=z_H+z_K−t.

Its real part is at least the real part of each summand. If both imaginary parts are positive, monotonicity of arctan and atan(a+b)≤atan(a)+atan(b) for a,b≥0 imply

    arg z_G≤max(0,arg z_H)+max(0,arg z_K).

If one or both imaginary parts are nonpositive, the same bound follows by discarding the negative contributions and using the real-part bounds. The inequality atan(a+b)≤atan(a)+atan(b) follows, for example, by integrating the decreasing derivative of atan over [a,a+b] versus [0,b]. Therefore

    theta_G≤max(theta_H,theta_{H-v})+max(theta_K,theta_{K-v}).

Apply this to each induced subgraph of G, using its restrictions to H and K; if it omits v, the phase is exactly additive because the restrictions are disjoint. Taking maxima yields

    Phi_G(t)≤Phi_H(t)+Phi_K(t).

Repeated splitting at cut vertices gives the general block inequality

    m−s⁺(G) ≤ I(G) ≤ sum_{blocks B} I(B).                                 (4.4)

No monotonicity of square energy under edge addition or pendant attachments is assumed here.

### 4.3 Matching polynomials and unicyclic graphs

Define M_J(t)=sum_{j≥0} m_j(J)t^(|V(J)|−2j), where m_j counts matchings with j edges. Independent matchings in induced subgraphs J[S] and J[V−S] yield

    M_J(t) ≥ M_{J[S]}(t) M_{J[V−S]}(t)     (t>0).                         (4.5)

A forest has det(tI+iA_J)=M_J(t)>0. Indeed, in the permutation expansion every nontrivial permutation cycle must be a transposition corresponding to a graph edge, contributing a positive factor 1, while unused vertices contribute t. Thus every forest has phase zero.

For a graph J whose only cycle is an odd cycle C_L (possibly with other forest components), the same expansion has the additional two orientations of this cycle:

    det(tI+iA_J)=M_J(t)+2 i^L M_{J−V(C_L)}(t).                             (4.6)

The sign of the imaginary part is positive for L≡1 mod4 and negative for L≡3 mod4. The real part is positive. The unwrapped phase is the principal arctangent, because this expression is continuous and the phase tends to zero at infinity. In the positive case, (4.5) gives

    0≤theta_J(t)≤theta_C_L(t)=atan(2/M_C_L(t)).                            (4.7)

This also applies to every induced subgraph of such a graph, with phase zero if its cycle is destroyed. For an even unicyclic graph the graph is bipartite and s⁺=s⁻=m by spectral symmetry. For a connected unicyclic graph with L≡3 mod4, (4.1) and (4.6) give s⁺>m=n. Thus a connected unicyclic graph with s⁺<n must have its cycle length congruent to 1 modulo 4.

For any unsigned cycle C_L, its eigenvalues are 2cos(2pi j/L). When L=4k+1, the positive eigenvalues correspond to j=−k,...,k modulo L. The finite geometric sum gives

    s⁺(C_L)=2(2k+1)+2 sin((2k+1)2pi/L)/sin(2pi/L)
           =L+1−sec(pi/L).

For L=4k+3 the same range gives s⁺(C_L)=L−1+sec(pi/L). For even L, s⁺=L. Every proper induced subgraph of a cycle is a forest. Hence for any cycle

    I(C_L) ≤ sqrt(5)−2 < 1/4,                                              (4.8)

with equality in the first bound for L=5. Indeed the only positive phases occur when L≡1 mod4, L≥5, and their integrated value is sec(pi/L)−1≤sec(pi/5)−1=sqrt(5)−2. This uses cos(pi/5)=(1+sqrt(5))/4. The upper bound 1/4 is strict since 5<(9/4)².

For every complete graph K_k (including a bridge K₂), its phase is atan((k−1)/t)−(k−1)atan(1/t)≤0 by concavity of atan on nonnegative arguments and atan(0)=0. Its induced subgraphs are complete, so I(K_k)=0.

### 4.4 Path cofactor identity

Let F be any simple graph, and u,w vertices. With W_P the set of vertices on a simple u–w path P, and ell(P) its edge length,

    [(tI+iA_F)^(−1)]_uw
       = sum_{P:u→w} (−i)^ell(P) det(tI+iA_{F−W_P})/det(tI+iA_F).          (4.9)

If u=w, the sum consists of the path of length zero. If u,w lie in different components it is empty. To prove the identity, use the cofactor formula for the inverse, or differentiate the determinant with respect to the single matrix entry at (w,u). A permutation that uses the directed entry w→u completes a unique simple directed path from u to w to form that permutation cycle. The sign of the cycle is (−1)^ell(P), and the remaining ell(P) entries of the cycle each contribute i. The other permutation cycles sum to the determinant on the remaining vertices. This proves (4.9), including the diagonal case.

Deleting k vertices in succession and applying (4.3) at each deletion shows the general modulus estimate

    |det(tI+iA_{F−W})/det(tI+iA_F)| ≤ t^(−|W|).                            (4.10)

Indeed each inverse Schur ratio has modulus at most 1/t. All determinants are nonzero for t>0 by the real spectrum.

## 5. Uniform phase bounds for the two difficult block types

We prove a bound for each block itself and every one of its induced subgraphs simultaneously. This distinction is essential for (4.4).

### 5.1 Tree remainder

**Lemma 5.1.** Let B be a 2-connected graph of cycle rank r≥2 with a vertex v such that B−v is a tree. Then I(B)<r−1.

Here d=d_B(v)=r+1, since B−v is connected and has cycle rank zero. For any induced subgraph J of B containing v, F=J−v is a forest, not necessarily connected. In (4.3), expand the inverse via (4.9). The determinant ratios are real positive for each existing path. The imaginary terms with positive sign arise only for paths of length ell≡3 mod4 (ell≥3). Their endpoints lie in opposite parts of the bipartition of F. Each pair of distinct vertices is joined by at most one path, so the number N of contributing unordered pairs is at most floor(d²/4), even if some of the original d neighbors are missing. This follows by choosing a bipartition of the entire forest and maximizing ab subject to a+b≤d.

Each contributing path P has an even number of vertices at least four. The matching polynomials of paths obey M_{P_{j+2}}=t M_{P_{j+1}}+M_{P_j}≥M_{P_j}, so M_P(t)≥M_{P_4}(t)=t⁴+3t²+1 for all t>0. By (4.5),

    M_{F−W_P}/M_F≤1/M_P≤1/(t⁴+3t²+1).

Each unordered pair appears twice in the quadratic form. Since Re z_J≥t and theta_F=0, (4.3) implies the pointwise bound

    Phi_B(t)≤atan(2 floor((r+1)²/4)/(t⁵+3t³+t)).                          (5.1)

If J does not contain v its phase is zero, so the same envelope holds.

For r=2, use 2 floor(3²/4)=4. The integral of t atan(...) over (0,1), normalized by 2/pi, is at most 1/2. Over [1,2], t atan(...)≤4/(t⁴+3t²+1)≤1/t² since (t²−1)²≥0. Over [2,infinity), t atan(...)≤4/t⁴. Thus

    I(B)≤1/2+(2/pi)(1/2+1/6)=1/2+4/(3pi)<1=r−1.

For r≥3 we use the exact identity, for a≥0,

    (2/pi) integral_0^infinity t atan(a/t⁵)dt
      = a^(2/5)/(2 cos(pi/5)).                                            (5.2)

For a>0, integration by parts yields (5a/pi) times the integral of t⁶/(t¹⁰+a²). Substitute t=a^(1/5)u, and use the elementary beta integral integral_0^infinity u⁶/(1+u¹⁰)du=pi/(10 sin(7pi/10)). The boundary terms vanish. The zero case is immediate. Since a=2 floor((r+1)²/4)≤2(r−1)² and 1/(2cos(pi/5))<2/3, (5.1)–(5.2) give

    I(B) < (2/3)2^(2/5)(r−1)^(4/5) < r−1.

The last inequality follows from r−1≥2 and (2/3)2^(1/5)<1. This proves Lemma 5.1.

### 5.2 Unicyclic remainder with a bad odd cycle

**Lemma 5.2 (new closing estimate).** Let B be a 2-connected graph of cycle rank r≥2 with a vertex v lying on a triangle, such that B−v is unicyclic and its cycle C_L has length L≡1 mod4. Then I(B)<r−1.

Here d=d_B(v)=r because deleting v leaves a connected graph of cycle rank one. In particular d≥2. Fix any induced subgraph J of B. If v is absent, (4.7) bounds its phase by theta_C_L. If v is present, set F=J−v, and let b be the neighbor indicator in (4.3). Every induced subgraph of B−v is a forest or has exactly the same unique cycle C_L, perhaps with forest components. Thus for every such subgraph F', write

    det(tI+iA_F') = M_F'(t)(1+i beta_F'(t)),
    0≤beta_F'(t)≤2/M_C_L(t).

This follows directly from (4.5)–(4.7); it is valid also for the empty graph. In particular Re z_J≥t and theta_F≤theta_C_L. For 0<t<1 simply use arg z_J≤pi/2. It follows that, uniformly over all J,

    Phi_B(t)≤theta_C_L(t)+pi/2  (0<t<1).                                  (5.3)

For t≥1, put C(t)=t⁵+5t³+5t. We have M_C_L(t)≥C(t): the cycle has one empty matching, L single-edge matchings, and at least L distinct two-edge matchings (choose edges at cyclic distance two), with exponents L,L−2,L−4 respectively and L≥5. Since t≥1, these three terms are at least t⁵, 5t³, 5t. Hence 0≤beta_F'≤2/C(t)≤2/11.

For a simple path P in F, let R_P be the determinant ratio appearing in (4.9). Set beta=beta_F, beta'=beta_{F−W_P}, and h=M_{F−W_P}/M_F. We have

    R_P=h(1+i beta')/(1+i beta),
    Re R_P=h(1+beta beta')/(1+beta²)≥0,
    |Im R_P|=h |beta'−beta|/(1+beta²)≤2h/C(t).                              (5.4)

Moreover, beta beta'−beta²≤(beta')²/4≤1/121. Therefore

    Re R_P ≤ (122/121) h < (101/100)h.                                    (5.5)

By (4.5), h≤1/M_{F[W_P]}, and M_{F[W_P]}≥M_P because the path edges form a spanning subgraph of that induced graph. Thus h≤1/M_P. For a path with ell≥3, its first three matching terms show M_P≥t⁴+3t²+1 at t≥1 (or use the path recurrence). If ell≥2, M_P≥t³+2t at t≥1. For ell=0, M_P=t.

Now expand b^T(tI+iA_F)^(−1)b by (4.9). Separate path lengths as follows.

* Odd length ell≡1 mod4: the factor (−i)^ell=−i, so its imaginary contribution is −Re R_P≤0. These terms can be discarded in an upper bound.
* Odd length ell≡3 mod4: its contribution is Re R_P≤(101/100)/(t⁴+3t²+1). For each ordered pair of distinct neighbors there is at most one odd path: two distinct paths in a unicyclic graph differ by traversing opposite arcs of the unique odd cycle, so they have opposite parity; in a forest there is at most one path in total. At least one pair of the d original neighbors is adjacent because v lies on a triangle. If J retains all d neighbors, both orderings of that pair have an odd path of length one and hence cannot contribute an odd path of length 3 mod4. If J retains fewer than d neighbors, there are at most (d−1)(d−2) ordered pairs, which is at most d(d−1)−2 for d≥2. Thus at most d(d−1)−2 ordered paths can contribute in this class.
* Positive even lengths ell≥2: for each ordered pair of distinct neighbors there is at most one even path, by the same parity argument. Its imaginary part, regardless of sign (−i)^ell=±1, is bounded above by |Im R_P|≤2/[C(t)(t³+2t)]. There are at most d(d−1) such ordered paths.
* Length zero: there is one diagonal term per retained neighbor. Its imaginary part is at most 2/[C(t)t], with at most d terms.

These estimates bound the positive imaginary part of z_J from above by a nonnegative expression. Divide by Re z_J≥t, and use monotonicity of arctan. With a=(101/100)[d(d−1)−2], we obtain the following bound on the entire envelope for t≥1:

    Phi_B(t) ≤ theta_C_L(t) + atan(f_d(t)),                                (5.6)

    f_d(t) = a/(t⁵+3t³+t)
           + 2d/[C(t)t²]
           + 2d(d−1)/[C(t)(t⁴+2t²)].

All quantities on the right depend only on the original d and L, not on J. Thus taking the maximum over J in (4.2) is legitimate.

#### Small degrees d=2,...,9: exact finite rational proof

By (4.8), (5.3), and (5.6),

    I(B) < 3/4 + (2/pi) integral_1^infinity t atan(f_d(t))dt.

Here 3/4 is a strict rational upper bound on (sqrt(5)−2)+1/2. All three terms in f_d are nonnegative and decreasing on [1,infinity); the first coefficient is nonnegative because d≥2. On the interval [j/10,(j+1)/10] (j=10,...,99), bound atan(f_d(t)) by min(11/7,f_d(j/10)), using pi<22/7 and atan(x)≤x for x≥0. At t≥10, bound f_d(t) by a/t⁵+2d/t⁷+2d(d−1)/t⁹. Use 2/pi<2/3. It follows that

    I(B) < U_d,
    U_d = 3/4 + (2/3) [
       sum_{j=10}^{99} ((j+1)²−j²)/200 * min(11/7,f_d(j/10))
       + a/(3*10³) + 2d/(5*10⁵) + 2d(d−1)/(7*10⁷)
    ].                                                                  (5.7)

Every expression in U_d is rational. The following finite arithmetic inequalities follow by direct substitution and fraction arithmetic; the accompanying `verify_integral_bounds.py` reproduces them with exact integer-based fractions and no floating-point assertions:

| d | Exact strict upper bound on U_d | d−1 |
|---:|---:|---:|
| 2 | 881/1000 | 1 |
| 3 | 1340/1000 | 2 |
| 4 | 1813/1000 | 3 |
| 5 | 2261/1000 | 4 |
| 6 | 2682/1000 | 5 |
| 7 | 3096/1000 | 6 |
| 8 | 3492/1000 | 7 |
| 9 | 3877/1000 | 8 |

Thus I(B)<d−1=r−1 for every d in this finite range. These are scalar integral certificates, not checks of a bounded collection of graphs.

#### All degrees d≥10: analytic proof

For completeness use a looser bound that grows sublinearly in d. For t≥1, (4.10) gives |R_P|≤t^(−ell−1). The arguments of both determinants in R_P lie in [0,theta_C_L(t)], so the difference lies in [−theta_C_L(t),theta_C_L(t)]. Since theta_C_L(t)≤atan(2/t⁵), the absolute imaginary part is at most 2 t^(−ell−6). Odd paths of length 1 mod4 again contribute nonpositively. Positive odd-length contributions require ell≥3 and are at most t^−4. Even-length contributions, including ell=0, are at most 2/t⁶≤2/t⁴. There are at most two paths per ordered pair (including a diagonal pair, for which there is just one), and at most d² ordered pairs. Hence Im z_J≤4d²/t⁴, giving the uniform bound

    Phi_B(t)≤theta_C_L(t)+atan(4d²/t⁵)  (t≥1).

Combine this with (5.3), (4.8), and (5.2):

    I(B) < 3/4 + (4d²)^(2/5)/(2cos(pi/5))
         < 3/4 + (35/32)d^(4/5)
         ≤ (7d+68)/16.

For the second inequality, 4^(2/5)<7/4 (raise to the fifth power), and cos(pi/5)>4/5 because sqrt(5)>11/5. For the last inequality, concavity of x^(4/5) gives the tangent bound x^(4/5)≤(2/5)x+16/5 at x=32. For d≥10, (7d+68)/16<d−1 since 9d>84. Thus I(B)<r−1 for all remaining d, completing Lemma 5.2. QED.

## 6. Rooted-cluster deletion in a minimal counterexample (new)

Assume for contradiction that the strict theorem is false, and choose a counterexample G of minimum vertex count, so r_G≥2 and s⁺(G)≤|V(G)|. Every connected graph with fewer vertices and cycle rank at least two then satisfies the strict theorem.

The following principal-submatrix lower bound is useful. If P=A_G,+ and N=A_G,− then P=A_G+N. For any vertex set S, P[S]=A_{G[S]}+N[S] with N[S] positive semidefinite. For any real symmetric X and any PSD Y, we have

    ||X+Y||²_F ≥ ||X₊||²_F,

since X=X₊−X₋ with tr(X₊X₋)=0, and expanding gives ||X₊||²_F+||Y−X₋||²_F+2tr(X₊Y)≥||X₊||²_F. Therefore

    ||P[S]||²_F ≥ s⁺(G[S]).                                               (6.1)

**Lemma 6.1.** If B is any 2-connected block of G with at least four vertices and containing a triangle, then some vertex v of that triangle satisfies: B−v is a tree, or B−v is connected unicyclic with a cycle of length 1 modulo 4.

Proof: Delete all edges of B from G. The components are indexed by vertices of B, each containing exactly one such vertex, by the standard block-cut tree property. Explicitly, if an outside path joined distinct vertices of B, adjoining this ear to B would contradict maximal 2-connectivity; connectivity ensures every outside component reaches B. Let T_u be the set of vertices of the component rooted at u∈V(B). These sets partition V(G), and each G[T_u] is connected. The only edges between different sets T_u,T_w are the corresponding edges uw of B.

Let a,b,c form a triangle in B, and put S=T_a∪T_b∪T_c. Then G[S] is connected, contains that triangle, and is a proper induced subgraph because B has at least four vertices and each rooted set is nonempty. If it is multicyclic it satisfies s⁺(G[S])>|S| by minimality. Otherwise it is unicyclic with unique cycle a triangle, and (4.6) and (4.1) give the same strict bound. In either case

    ||P[S]||²_F ≥ s⁺(G[S]) > |S|.                                        (6.2)

For any root u∈V(B), define its full row-and-column contribution

    w_u=||P[T_u,T_u]||²_F + 2||P[T_u,V(G)−T_u]||²_F.

The sum of w_a,w_b,w_c counts every squared matrix entry within P[S] at least once; the entries joining two of the three sets are counted twice, and every extra term is nonnegative. Consequently w_a+w_b+w_c>|S|=|T_a|+|T_b|+|T_c|. There is at least one root v among a,b,c with w_v>|T_v|.

For this v,

    s⁺(G)=w_v+||P[V(G)−T_v]||²_F
          > |T_v|+s⁺(G−T_v),                                          (6.3)

by (6.1). Since G is a counterexample, s⁺(G−T_v)<|V(G−T_v)|. But G−T_v is nonempty and connected: its core B−v is connected by 2-connectivity, and all other rooted components remain attached. It has fewer vertices than G. By minimality it cannot have cycle rank at least two. If its cycle rank is zero it is a tree. If its cycle rank is one, its unique cycle must have length 1 modulo 4 by the unicyclic facts of Section 4.3. In either case the connected induced subgraph B−v has cycle rank at most one, and any cycle it contains has the same length 1 modulo 4. The chosen v lies on the original triangle. This proves Lemma 6.1. QED.

The cluster construction is what permits the proof to handle arbitrary pendant trees, including trees attached to every vertex of a triangle. No assumption is made that removing a single leaf preserves the conjectured bound. It also permits arbitrary cyclic blocks attached outside B.

## 7. Terminal contradiction: all graphs covered

Retain the hypothetical minimum-order counterexample G. The DNN transfer (2.6) and triangle-free block lemma (Section 3) exclude the presence of any triangle-free 2-connected noncycle block: such a block has delta(B)>1 and hence s⁺(G)>n, contradicting the counterexample assumption.

Classify every block B of G into the following exhaustive cases.

* A bridge: I(B)=0 and r_B=0.
* A cycle: I(B)≤sqrt(5)−2<1/4, and r_B=1. (A triangle is included.)
* A complete noncycle: I(B)=0<r_B−1 because a complete graph with at least four vertices has cycle rank at least three.
* Any other 2-connected noncycle: it must contain a triangle by the DNN exclusion, and it has at least four vertices. Apply Lemma 6.1 to choose a triangle vertex v. If B−v is a tree use Lemma 5.1; if B−v is unicyclic with its cycle of length 1 mod4 use Lemma 5.2. Both give I(B)<r_B−1.

If any noncycle block of cycle rank at least two occurs, its I(B) is strictly less than r_B−1, while every other block has I(B)≤r_B. Since the ranks add, (4.4) yields

    m−s⁺(G) ≤ sum_B I(B) < r_G−1 = m−n,

contradicting s⁺(G)≤n.

Otherwise G consists entirely of bridges and cycle blocks. The number of cycle blocks equals r_G≥2. By (4.8),

    m−s⁺(G) ≤ sum_B I(B) ≤ r_G(sqrt(5)−2) < r_G/4 < r_G−1,

again a contradiction. Every possible block type is covered. Thus no minimal counterexample exists, and the theorem follows:

    s⁺(G) > n for every finite connected simple unsigned graph with m≥n+1.  QED.

### Scope of strictness

The proof deliberately chooses a minimum-order graph violating the strict assertion, not merely the original non-strict conjecture. In the rooted-cluster argument, every smaller multicyclic induced graph has strictly more positive square energy than its order, and a unicyclic graph with a triangle has the same strict inequality by its determinant phase. Thus the cluster contribution in (6.3) is strict. This proves that equality s⁺=n does not occur in the conjecture's domain. No uniform positive gap beyond n is asserted for the unrestricted graph class.

## 8. Reproduction and prior work

The sole finite arithmetic step is (5.7), independently reproducible with `python verify_integral_bounds.py` using only Python's standard library. The supplementary `test_phase_bound.py` compares the new phase inequality numerically with induced-subgraph spectra of small and seeded random apex-unicyclic examples; those tests are not used in the proof.

Principal sources (with theorem scope kept distinct):

- Akbari, Kumar, Mohar, Pragada and Zhang, *Refinement of a conjecture on positive square energy of graphs*, arXiv:2506.07264, Conjecture 1.2; cycle spectral formulas. https://arxiv.org/abs/2506.07264
- Liu, Tang and Zhang, *The positive and negative square-energy conjecture*, arXiv:2607.18031, DNN framework and n−1 theorem. https://arxiv.org/abs/2607.18031
- Akbari, Hu and Liu, *Positive square energy of graphs with minimum degree at least two*, arXiv:2609.06778, block deficit and correlation certificate framework. https://arxiv.org/abs/2609.06778
- Hu and Han, *From the square-energy conjecture to signed graphs*, arXiv:2608.18492, convex combination of deletion and edge Cauchy–Schwarz inequalities. https://arxiv.org/abs/2608.18492
- Akbari, Hu and Liu, *Positive and negative square energies of 2-connected graphs*, arXiv:2609.04069, published 2-connected results (not assumed to cover tree attachments). https://arxiv.org/abs/2609.04069
- Ning and Zeng, *A proof of a conjecture on positive and negative square energies of unicyclic graphs*, arXiv:2605.24668, unicyclic Coulson identity and modulo-four sign result, rederived in Sections 4.1 and 4.3. https://arxiv.org/abs/2605.24668
- Zhang, *Extremal values for the square energies of graphs*, arXiv:2409.15504, earlier projection inequalities, extremal examples. https://arxiv.org/abs/2409.15504

Previously failed shortcuts (edge addition monotonicity, lossless leaf pruning, and the phase bound r_B/2 for all blocks) are not used. The proof is specific to the unsigned conjecture in the triangle-containing part; it does not extend the unrestricted assertion to arbitrary signed graphs. No claim of peer review, Lean formalization, or verified worldwide originality is made.
