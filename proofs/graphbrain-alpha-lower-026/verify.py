import networkx as nx
from fractions import Fraction
from math import comb

def chain(r,k):
    g=nx.disjoint_union_all([nx.complete_graph(k) for _ in range(r)])
    g.add_edges_from((j*k+1,(j+1)*k) for j in range(r-1))
    return g

def alpha_small(g):
    return max(map(len,nx.find_cliques(nx.complement(g))))

def indep(g,s):
    assert len(set(s))==len(s)
    assert g.subgraph(s).number_of_edges()==0

def chain_check(r,k,leaf=False):
    g=chain(r,k)
    if leaf:g.add_edge(2,r*k)
    assert nx.is_connected(g)
    for j in range(r):
        assert g.subgraph(range(j*k,(j+1)*k)).number_of_edges()==comb(k,2)
    # Each clique contributes at most one independent vertex. Vertex 3 of each
    # clique, and the optional leaf, attain the resulting upper bound.
    s=[j*k+3 for j in range(r)]+([r*k] if leaf else [])
    indep(g,s)
    mu=len(nx.max_weight_matching(g,maxcardinality=True))
    return g,len(s),mu

g,a,mu=chain_check(4,8);delta=min(dict(g.degree()).values());assert (a,mu,delta)==(4,16,7);assert 2*a<mu-delta
print('lower-026',a,Fraction(mu-delta,2))
g=nx.disjoint_union(nx.complete_graph(4),nx.complete_graph(4));g.add_edges_from((8,v) for v in range(8));a=alpha_small(g);d=max(nx.core_number(g).values());D=max(dict(g.degree()).values());assert (a,d,D)==(2,4,8);assert nx.triangles(g,8)>0;assert a<min(3,D-(d+1))
print('lower-028',a,min(3,D-(d+1)))
g=nx.complete_graph(3);g.add_edges_from((v,v+3) for v in range(3));a=alpha_small(g);p=sum(d==1 for _,d in g.degree());t=sum(nx.triangles(g).values())//3;assert (a,p,t)==(3,3,1);assert a<min(10**t,p+1)
print('lower-031',a,min(10**t,p+1))
g,a,mu=chain_check(12,4,True);delta=min(dict(g.degree()).values());assert (a,mu,delta)==(13,24,1);assert a<mu-10**delta
print('lower-042',a,mu-10**delta)
g,a,mu=chain_check(9,4);D=max(dict(g.degree()).values());d=max(nx.core_number(g).values());assert (a,mu,D,d)==(9,18,4,3);assert a<mu-D-(d+1)
print('lower-044',a,mu-D-(d+1))
g=nx.star_graph(32);s=list(range(1,33));indep(g,s);assert nx.is_connected(g);avg=Fraction(sum(sum(x.values()) for _,x in nx.all_pairs_shortest_path_length(g)),len(g)*(len(g)-1));assert avg==Fraction(64,33)<Fraction(9,4);assert 10**3<32**2
print('upper-002',len(s),'RHS < 32')
g=nx.complete_bipartite_graph(9,9);indep(g,list(range(9)));assert len(g)==18 and min(dict(g.degree()).values())==9;assert Fraction(11,4)**2<8
print('upper-008',9,'RHS <= 8')
g=nx.balanced_tree(2,10);s=[v for v,d in g.degree() if d==1];indep(g,s);D=max(dict(g.degree()).values());diam=nx.diameter(g);assert (len(s),D,diam)==(1024,3,20);assert len(s)>2*diam**2+D
print('upper-025',len(s),2*diam**2+D)
g=nx.path_graph(16);s=list(range(0,16,2));indep(g,s);avg=Fraction(2*g.number_of_edges(),len(g));D=max(dict(g.degree()).values());assert avg<2 and D**2==4 and Fraction(11,4)**2<8
print('upper-061',len(s),'RHS < 8')
