# Three spectral graph inequalities — Cazenave (2026)

Source: Tristan Cazenave, Lemmas and Conjectures in Spectral Graph Theory, Section 7, https://arxiv.org/abs/2611.03879. Written arguments from 25 November 2026; reviewed again here against the original statement. These are candidate resolutions of individually highlighted inequalities from an automatically generated corpus, not claims of independent novelty. All graphs are connected, simple, with n>=2.

Notation: A adjacency matrix, D degree matrix, L=D-A Laplacian, lambda_1>=lambda_2>=... adjacency eigenvalues, mu_1>=mu_2>=... Laplacian eigenvalues, R=sum over edges (d_u d_v)^(-1/2), m=edge count.

## Conjecture 3 (#501193)
Claim: 2R <= rank(A) lambda_1.

B=D^(-1/2) A D^(-1/2) has operator norm 1: it is similar to the row-stochastic matrix D^(-1)A and has eigenvalue 1. Direct expansion gives tr(AB)=2R. By the duality of the operator and nuclear norms, 2R<=||A||_*<=rank(A) lambda_1, since all eigenvalues of a real symmetric nonnegative adjacency matrix have absolute value at most its Perron root. This also proves the intermediate energy bound.

## Conjecture 5 (#239534)
Claim: mu_2+rank(A)<=2m.

If G has a cycle, m>=n; the Laplacian has mu_1<=n because L(G)+L(complement G)=nI-J. Thus mu_2+rank(A)<=2n<=2m.

If G is a tree, its unsigned vertex-edge incidence matrix C satisfies CC^T=D+A, similar to L by a bipartition sign change, and C^TC=2I+A(line graph of G). C has full column rank (remove a leaf inductively), so for n>=3, mu_2=2+lambda_2(line graph).

Lemma: a connected graph H on N>=2 vertices has lambda_2(H)<=floor(N/2)-1. A second eigenvector orthogonal to a strictly positive Perron vector has nonempty positive and negative supports. On each support separately, multiplying the eigen-equation by the absolute value of the eigenvector and summing gives lambda_2 ||x_support||^2 <= x_support^T A(H[support]) x_support. The spectral radius of that induced subgraph is at most its order minus one. Apply this to the smaller support, whose order is <=floor(N/2).

For n>=4 this yields mu_2<=1+floor((n-1)/2)<=n-2. Since rank(A)<=n, the result follows. Directly, K2 has mu_2=0 and rank=2, P3 has mu_2=1 and rank=2, both satisfying the claim.

## Conjecture 6(i)
Claim: R^2 >= (m+1)/2.

Let x_v=sqrt(d_v). The adjacency Rayleigh quotient yields sum_edges sqrt(d_u d_v) <= m lambda_1. Cauchy-Schwarz then gives m^2<=R sum_edges sqrt(d_u d_v)<=R m lambda_1, hence m<=R lambda_1. Hong's classical spectral radius bound for connected graphs (Linear Algebra Appl. 108 (1988)) gives lambda_1^2<=2m-n+1. Therefore R^2>=m^2/(2m-n+1). For n>=3, 2m^2-(m+1)(2m-n+1)=(n-3)m+n-1>0. For K2, R=1 and m=1. Thus equality occurs exactly for K2.

Independent peer review, publication priority and formal proof-assistant verification remain pending.
