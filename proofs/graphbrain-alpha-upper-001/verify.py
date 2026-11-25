from fractions import Fraction as F
from math import comb
import networkx as nx

results={}
def test(i,a,b,lower=False):
    assert (a<b if lower else a>b),(i,a,b)
    results[i]=(str(a),str(b))
    print(i,a,b,flush=True)
def alpha(g): return max(map(len,nx.find_cliques(nx.complement(g))))
def meeh(g):
    ans=0
    for _,d in nx.all_pairs_shortest_path_length(g):
        E=[v for v,x in d.items() if x%2==0]
        ans=max(ans,len(E)-g.subgraph(E).number_of_edges())
    return ans
def chain(r,k):
    g=nx.disjoint_union_all([nx.complete_graph(k) for _ in range(r)])
    g.add_edges_from((j*k,(j+1)*k) for j in range(r-1))
    assert nx.is_connected(g) and not g.subgraph(range(1,r*k,k)).number_of_edges()
    assert all(g.subgraph(range(j*k,(j+1)*k)).number_of_edges()==comb(k,2) for j in range(r))
    return g
def spider(d):
    t=nx.Graph(); t.add_node(0); n=1
    for l in range(1,d+1):
        u=0
        for j in range(l):t.add_edge(u,n);u=n;n+=1
    assert nx.is_tree(t) and sorted(len(c) for c in nx.connected_components(t.subgraph(set(t)-{0})))==list(range(1,d+1))
    g=nx.complement(t);assert nx.is_connected(g) and nx.diameter(g)==2
    return t,g
# Exact bounds on e and pi, using Taylor and Machin's identity.
e_lo=sum((F(1,__import__('math').factorial(k)) for k in range(5)),F(0))
e_hi=sum((F(1,__import__('math').factorial(k)) for k in range(6)),F(0))+F(1,720)*F(7,6)
assert F(27,10)<e_lo<e_hi<F(68,25)<F(11,4)<3
def atan_interval(q,N):
    s=sum(((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(N)),F(0));z=(-1)**N*q**(2*N+1)/F(2*N+1)
    return min(s,s+z),max(s,s+z)
a,b=atan_interval(F(1,5),14);c,d=atan_interval(F(1,239),5)
pi_lo,pi_hi=16*a-4*d,16*b-4*c
assert F('3.14159265358979')<pi_lo<pi_hi<F('3.14159265358980')
pl,ph=F('3.14159265358979'),F('3.14159265358980')
def cot_lower(x,odd):
    lo=odd*pl/2-x;hi=odd*ph/2-x
    assert 0<lo<hi<1
    return (1-hi*hi/2)/hi
# K5 hub chain: MEEH exactly zero
r=51;g=chain(r,5);M=meeh(g);D=max(dict(g.degree()).values());rad=nx.radius(g);m=g.number_of_edges();mu=len(nx.max_weight_matching(g,maxcardinality=True));cv=len(list(nx.articulation_points(g)));dd=len(set(dict(g.degree()).values()));c=len(nx.center(g))
assert (M,D,rad,m,cv,dd,c)==(0,6,26,560,51,3,1) and mu>=2*r
test('upper-001',r,27);test('upper-005',r,D*D-mu);test('upper-073',r,F(m,rad));test('upper-095',r,28);test('upper-097',r,F(1,cv));test('lower-078',r,F(mu*mu,D*D),True)
r=201;g=chain(r,5);cv=len(list(nx.articulation_points(g)));avg=F(2*g.number_of_edges(),len(g));assert cv==r and avg>4 and cv>125 and F(11,4)**4<4**3
# avg^log(cv) = cv^log(avg) > cv^(4/3) > 5cv=n
assert cv>125;test('upper-059',r,0)
# Two groups of K5s, complete join between groups, two arms.
r=20;core=nx.disjoint_union_all([nx.complete_graph(5) for _ in range(2*r)]);g=core.copy();g.add_edges_from((u,v) for u in range(5*r) for v in range(5*r,10*r));n=len(g);g.add_edges_from([(0,n),(n,n+1),(n+1,n+2),(0,n+3),(n+3,n+4),(n+4,n+5)]);s=list(range(5*r,10*r,5))+[n,n+2,n+3,n+5];assert not g.subgraph(s).number_of_edges();M=meeh(g);p=len(nx.periphery(g));diam=nx.diameter(g);dd=len(set(dict(g.degree()).values()));delta=min(dict(g.degree()).values());assert (M,p,diam,dd,delta)==(0,2,6,4,1)
test('upper-006',len(s),(p+diam)**(M+1));test('upper-033',len(s),p**dd+M);test('upper-048',len(s),10**M+max(delta,p))
# Universal hub over disjoint K5s.
r=4;g=nx.disjoint_union_all([nx.complete_graph(5) for _ in range(r)]);g.add_edges_from((5*r,v) for v in range(5*r));assert alpha(g)==r and meeh(g)==1 and nx.radius(g)==1 and nx.node_connectivity(g)==1;mn=min(len(set(g[u])&set(g[v])) for u,v in __import__('itertools').combinations(g,2));assert mn==1;test('upper-077',r,2);test('upper-082',r,3)
# Exact theta sandwiches.
g=nx.complete_graph(100);g.remove_edge(0,1);assert alpha(g)==2 and nx.is_connected(g);assert 10<2**5;test('upper-120',2,1)
g=nx.complete_graph(397);g.add_edges_from((0,j) for j in range(397,400));assert alpha(g)==4 and min(len(set(g[u])&set(g[v])) for u,v in __import__('itertools').combinations(g,2))==0
# theta=4 by clique cover; cosh(1/5) <= sum (1/5)^(2k) =25/24<5/4; exp(5/4)<4
assert F(25,24)<F(5,4) and F(11,4)**5<4**4
# use exact rational strict upper bound: e^(5/4)<15/4 because (11/4)^5 < (15/4)^4
assert F(11,4)**5 < F(15,4)**4;test('upper-129',4,F(15,4))
# K3 chain; all nonempty independent sets have negative difference by distinct neighbors in their own clique.
g=chain(50,3);ds=sorted((d for _,d in g.degree()),reverse=True);wp=max(min(i+1,d+1) for i,d in enumerate(ds));assert wp==5 and len(g)==150;assert F(27,10)**5>143 and F(68,25)**5<150;test('upper-138',50,49)
# Complements of asymmetric spiders. Their automorphism group is trivial by unique hub and distinct arm lengths.
t,g=spider(6);n=len(g);delta=min(dict(g.degree()).values());cn=max(len(set(g[u])&set(g[v])) for u,v in __import__('itertools').combinations(g,2));assert alpha(g)==2 and n==22 and cn-delta>=3;test('lower-046',2,cn-delta,True);assert g.number_of_edges()>F(68,25)**5;test('lower-024',2,4,True)
# Blowup C15[K2], connectivity >=4 by at most one deleted cluster.
g=nx.lexicographic_product(nx.cycle_graph(15),nx.complete_graph(2));avg=F(sum(sum(d.values()) for _,d in nx.all_pairs_shortest_path_length(g)),len(g)*(len(g)-1));assert alpha(g)==7 and avg>3 and nx.node_connectivity(g)==4;test('lower-074',7,16,True)
# Union of C5's joined to a universal hub. Feasible theta matrix on cycle: (I+3A(complement C5)/5)/5.
# Exact positive definiteness by eigenvalues of the cycle: min  -(1+sqrt(5))/2, with sqrt(5)<7/3.
assert (F(1)+F(7,3))/2*F(3,5)==1  # strict since sqrt5<7/3
r=30;g=nx.disjoint_union_all([nx.cycle_graph(5) for _ in range(r)]);g.add_edges_from((5*r,v) for v in range(5*r));assert len(nx.center(g))==1 and len(nx.periphery(g))==5*r
# alpha=2r by disjoint cycle partition; a feasible common Gram matrix gives theta>=11r/5.
a=2*r;theta=F(11*r,5);ds=sorted((d for _,d in g.degree()),reverse=True);wp=max(min(i+1,d+1) for i,d in enumerate(ds));assert wp==4
for i,b in [('lower-011',min(5*r,theta)),('lower-015',theta-wp),('lower-020',theta-1)]:test(i,a,b,True)
# Triangle with two long arms.
k=10;g=nx.complete_graph(3)
for j in [3,3+k]:g.add_edge(0,j);g.add_edges_from((v,v+1) for v in range(j,j+k-1))
assert nx.radius(g)==k and alpha(g)==11 and sum(d==1 for _,d in g.degree())==2;test('lower-027',11,2*(k-3),True)
# Binary tree whose leaves each receive four additional clique vertices.
h=4;g=nx.balanced_tree(2,h);leaves=[v for v,d in g.degree() if d==1];n=len(g)
for j,v in enumerate(leaves):g.add_edges_from(__import__('itertools').combinations([v]+list(range(n+4*j,n+4*j+4)),2))
p=len(nx.periphery(g));c=len(nx.center(g));D=max(dict(g.degree()).values());assert (p,c,D)==(64,1,5);test('lower-075',2**(h+1)-1,p-c-D*D,True)
# Two-edge links between cliques, no articulation points.
sizes=[4,6,8,10];g=nx.disjoint_union_all([nx.complete_graph(k) for k in sizes]);offset=0
for j in range(len(sizes)-1):
    nxt=offset+sizes[j];g.add_edges_from([(offset+sizes[j]-2,nxt),(offset+sizes[j]-1,nxt+1)]);offset=nxt
assert nx.is_connected(g) and len(list(nx.articulation_points(g)))==0;dd=len(set(dict(g.degree()).values()));diam=nx.diameter(g);assert dd>=5 and diam>=5;test('lower-036',4,min(dd,diam),True)
# Trigonometric claims; rational bounds from Machin pi interval and elementary sin/cos inequalities.
g=nx.lexicographic_product(nx.cycle_graph(5),nx.complete_graph(7));assert alpha(g)==2 and 1+max(nx.core_number(g).values())==21;assert cot_lower(14,9)>3;test('lower-034',2,3,True)
cn=max(len(set(g[u])&set(g[v])) for u,v in __import__('itertools').combinations(g,2));assert cn>=3 and cot_lower(36,23)>3;test('lower-039',2,3,True)
g=nx.complete_graph(11);t=sum(nx.triangles(g).values())//3;assert t==165;eps=max(abs(F(t)-105*pl/2),abs(F(t)-105*ph/2));assert eps<F(1,10) and 1-eps**2/2>(F(11,4)**4-1)/(F(11,4)**4+1);test('lower-053',1,2,True)
t,g=spider(4);assert len(g)==11 and len(nx.center(g))==11 and alpha(g)==2;dd=len(set(dict(g.degree()).values()));assert dd==3;lo=11-7*ph/2;hi=11-7*pl/2;assert 0<lo<hi<F(1,3);test('lower-064',2,3,True)
t,g=spider(5);tr=sum(nx.triangles(g).values())//3;assert tr==370 and alpha(g)==2 and cot_lower(372,237)>3;test('lower-070',2,cot_lower(372,237)-1,True)
t,g=spider(8);m=g.number_of_edges();sw=1+max(nx.core_number(g).values());assert (m,sw)==(630,34) and alpha(g)==2;test('lower-088',2,cot_lower(664,423),True)
assert len(results)==30, len(results)
print('30/30 verified')
