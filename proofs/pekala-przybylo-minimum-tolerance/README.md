# Sharp-order minimum-tolerance thresholds for majority edge colouring

27 November 2026. AI-assisted candidate analytical result. Independent review and priority confirmation pending.

## Source and scope
P. Pękała and J. Przybyło, *On List Extensions of the Majority Edge Colourings*, Electronic Journal of Combinatorics 32(4) (2025), #P4.38, DOI 10.37236/13882, arXiv:2502.12688v1, Section 7, Conjectures 24 and 26: https://arxiv.org/html/2502.12688v1 . They ask for sufficient minimum-degree bounds O(1/(a epsilon)) for tolerance functions bounded below by a and lists with total tolerance at least 1+epsilon, and for their common-palette counterpart. Their parameter domain explicitly permits epsilon>0, but the paper indicates small epsilon is typical. We distinguish the usual small-epsilon asymptotic interpretation from a uniform assertion on the entire domain. Previous work in this research series gave the upper bound 2(1+epsilon)/(a epsilon), and noted the large-epsilon issue; the matching lower bound and the high-tolerance regime below are the new deductions in this note.

## Definitions and theorem
Let 0<a<1 and epsilon>0. A finite simple graph G has finite edge lists L(e) and a color tolerance function alpha with a<=alpha(c)<1 and sum_{c in L(e)} alpha(c)>=1+epsilon. A valid list colouring chooses one listed color for each edge and satisfies d_c(v)<=alpha(c)d(v) for every vertex and color. Let D_list(a,epsilon) be the least nonnegative integer minimum-degree threshold guaranteeing this property for all such graphs and assignments. D_common is the corresponding threshold when all edges have the same palette. Define b=max(0,2a-1) and X=(1+epsilon)/(a epsilon+b). Then

    X/20 <= D_common(a,epsilon) <= D_list(a,epsilon) <= 9 X.

In particular the two thresholds are of exactly the same order, uniformly in both parameters. These are constant-factor bounds, not an exact integer threshold. All lower bounds use complete graphs with a common palette of equal tolerances. No earlier candidate proof other than the self-contained rounding argument below is a logical dependency.

## Lemma: one-sided sparse rounding (reproduced from the earlier Conjecture 23 work)
Given fractional assignments x_(e,c)>=0 with sum_c x_(e,c)=1, there exists an integral assignment respecting the lists, with d_c(v)<=sum_{e incident to v}x_(e,c)+2, never selecting any initially zero variable.

Proof. Permanently fix every variable at 0 or 1, and keep all edge sum equations. Initially retain every vertex-color load equation. Let N be the number of still-fractional variables and M the number of edges containing at least one such variable. Each of these edges has at least two fractional variables whose sum is 1, hence N>=2M. A retained vertex-color row r has upward potential U_r=sum_{i in r fractional}(1-x_i). The sum of these potentials is at most 2(N-M), because each variable belongs to at most two retained load rows. If a retained row containing fractional variables has U_r<=2, drop it permanently; the load at the moment of dropping equals its initial load, and its final increase is at most U_r. Rows without fractional variables are already fixed and may be ignored. Otherwise, if there are R>0 remaining load rows containing fractional variables, 2R<2(N-M), so M+R<N. If R=0 and N>0, M<N also holds. Choose a nonzero homogeneous null direction of the remaining equations restricted to the fractional variables. Move until one variable reaches a boundary of [0,1]; the step is positive and finite and preserves all retained sums. Fix the newly integral variables. Every step either drops a row or fixes a variable, and the process terminates. The dropped rows have excess at most two, and the others retain their original loads. The preserved edge sums yield one selected color per edge. QED.

## Upper bound
For each edge let A_e=sum_{c in L(e)}alpha(c) and use x_(e,c)=alpha(c)/A_e. Then F_(v,c)<=alpha(c)d(v)/(1+epsilon). The rounding lemma gives d_c(v)<=alpha(c)d(v) whenever d(v)>=2(1+epsilon)/(a epsilon). Therefore D_list<=ceil(2(1+epsilon)/(a epsilon)). This is the previous upper bound.

If a>1/2, each list has at least two colors (a single color has tolerance less than 1). Select any two distinct listed colors and set their fractional weights to 1/2, all others to zero. Rounding gives d_c(v)<=d(v)/2+2<=a d(v) provided d(v)>=2/(a-1/2)=4/b. Thus D_list<=ceil(4/b) as well.

If b<=a epsilon, the first unrounded bound is at most 4X. If b>a epsilon, the second unrounded bound is at most 8/(a epsilon+b)<=8X. Since X>1 (a epsilon+b<1+epsilon), rounding up yields D_list<=9X. The common-palette problem is a restriction of the list problem, so D_common<=D_list.

## Lower bound: explicit regular capacity obstructions
In every case we produce a common-palette instance on K_(d+1) that cannot be colored. This implies D_common>=d+1, and in particular D_common>=d. The obstructions are purely local: the sum of integer color capacities at a degree-d vertex is less than d.

Case I: a<=1/2 and 0<epsilon<=1/4. Take L=floor(1/a)>=2, q=floor(1/(4 epsilon))>=1, d=Lq+1 and L colors each of tolerance alpha=(1+epsilon)/L. Then alpha>=a, alpha<1, and the palette has total tolerance 1+epsilon. Moreover

    alpha*d = q + epsilon*q + (1+epsilon)/L
             <= q + 1/4 + 5/8 = q+7/8 < q+1.

Hence each color may appear at most q times, and Lq=d-1 is insufficient. Since L>=1/(2a) and q>=1/(8 epsilon), d>=1/(16a epsilon)>=X/20 (here b=0 and 1+epsilon<=5/4).

Case II: a<=1/2 and epsilon>=1/4. Take d=floor(1/(2a))>=1 and enough colors of tolerance exactly a that their total is at least 1+epsilon. As a*d<=1/2, not even one edge may receive any color at a vertex of degree d. Also d>=1/(4a) and X=(1+epsilon)/(a epsilon)<=5/a, so d>=X/20.

Case III: a>1/2 and 0<epsilon<1. Put t=max(2a-1,epsilon), so 0<t<1. Use two colors, each of tolerance alpha=(1+t)/2>=a. Their total is 1+t>=1+epsilon and alpha<1. Let d be the largest positive odd integer strictly less than 1/t. Such an integer exists, and d>=1/(3t): writing x=1/t>1, for 1<x<=3 the integer 1 works, and for x>3 the largest odd integer strictly below x is at least x-2>=x/3. Because t*d<1, alpha*d<(d+1)/2, and hence each color can be used at most (d-1)/2 times. The two caps sum to d-1, a contradiction. Since a epsilon+b>=t/2 and 1+epsilon<2, X<=4/t and d>=X/12>=X/20.

Case IV: a>1/2 and epsilon>=1. Take d=1 and enough colors of tolerance a that their total is at least 1+epsilon. None can be used on the single edge of K_2. Here X<=(1+epsilon)/(a epsilon)<=4, so d>=X/4>=X/20.

All cases give D_common>=X/20. Together with the upper bound this proves the stated theorem. QED.

## Consequences for the conjectures
For 0<epsilon<=1, the previously conjectured sufficient O(1/(a epsilon)) bound follows for all a, since X<=(1+epsilon)/(a epsilon)<=2/(a epsilon). When a<=1/2 the order is also necessary. For fixed a>1/2 the threshold instead stays bounded as epsilon tends to zero, with the sharper uniform formula above describing the transition as a tends to 1/2 from above. For fixed a, the threshold is never below 2, since K_2 with sufficiently many colors of tolerance a is infeasible. Thus an O(1/(a epsilon)) bound uniform as epsilon tends to infinity is impossible; the corrected uniform order is the theorem above. This is a qualified resolution of the published statements, not a claim that their authors intended the false large-epsilon interpretation.

## Transfer of methods
Achour saturation: construct a capacity obstruction and certify infeasibility by a local invariant. Eulerian strong-majority: track odd degree and integer rounding obstructions; odd-degree witnesses are used in Case III. Ordinary majority: introduce slack before applying a general coloring theorem. List-majority: keep arbitrary lists and count their local capacity. Diversified majority: reuse the additive-two rounding proof. The new ingredient is the two-color fractional restriction at high tolerance and matching common-palette capacity obstructions, yielding a uniform two-parameter sharp-order theorem. No claim that all these techniques are new in the literature.

## Screening and limitations
On 27 November 2026, inspected the exact statements of Conjectures 24 and 26 in arXiv:2502.12688v1, searched for earlier resolutions by article identifier, conjecture number, authors, and rounding/threshold terms. The open-problem entry https://www.emergentmind.com/open-problems/improved-threshold-positive-minimum-tolerance was retrieved; no matching completed sharp-order theorem was found. The public search is not exhaustive. Both repository READMEs, code and issues were checked: competitor https://github.com/1337isnot1337/solved-conjectures (README e0493dac21e0169522567c34aca30f532c0cca55); user https://github.com/f8bsd9yqgp-maker/Solved-conjectures- (README 289836502bf6a4f0d6dfd1e0ffa5ef489f546d65). Competitor issue #24 concerns a Hadamard matrix and is unrelated. The user's existing diversified-majority manuscript explicitly contains the previous upper bound and large-epsilon caveat, but not the matching lower bounds or the high-tolerance refinement. Do not count those repeated deductions as new. No independent peer review or formal proof-assistant certification is claimed. Emailed to both original authors and posted to this repository on 27 November 2026.