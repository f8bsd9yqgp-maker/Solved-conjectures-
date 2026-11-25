import networkx as nx
from itertools import combinations
from fractions import Fraction

def sigma(g):
    return min(g.degree(u)+g.degree(v) for u,v in nx.non_edges(g))
def clique_leaves(m,handle=False):
    g=nx.complete_graph(m)
    if handle:
        g.add_edge(0,m); g.add_edges_from([(m,m+1),(m,m+2)])
    else:g.add_edges_from([(0,m),(0,m+1)])
    return g
def chain(r):
    g=nx.disjoint_union_all([nx.complete_graph(4) for _ in range(r)])
    g.add_edges_from((4*i,4*(i+1)) for i in range(r-1))
    s=list(range(1,4*r,4)); assert len(s)==r and not g.subgraph(s).number_of_edges()
    assert all(g.subgraph(range(4*i,4*i+4)).number_of_edges()==6 for i in range(r))
    assert len(nx.max_weight_matching(g,maxcardinality=True))==2*r
    return g
def alpha(g):return max(map(len,nx.find_cliques(nx.complement(g))))
def check(id,a,b,lower=True):
    assert (a<b if lower else a>b),(id,a,b)
    print(id,a,b)
g=clique_leaves(6); check('lower-016',alpha(g),max(dict(g.degree()).values())-sigma(g)-1)
g=clique_leaves(10,True);check('lower-022',alpha(g),Fraction(len(nx.periphery(g)),2)-sigma(g))
g=clique_leaves(12);a=alpha(g);assert len(g)-sigma(g)==12 and a==3; assert Fraction(11,4)**3/2<12;check('lower-025',a,4)
g=chain(101);common=max(len(set(g[u])&set(g[v])) for u,v in combinations(g,2));assert common==2;check('lower-049',101,202-10**common)
g=chain(7);assert nx.center(g)==[12] and nx.triangles(g,0)>0;check('lower-051',7,14-2*len(nx.center(g))-3);check('lower-059',7,14-len(nx.center(g))-max(dict(g.degree()).values()))
g=nx.star_graph(51);assert sigma(g)==2 and len(nx.periphery(g))==51;check('upper-015',51,10**sigma(g)-len(nx.periphery(g)),False)
g=nx.balanced_tree(2,9);leaves=[v for v in g if g.degree(v)==1];assert not g.subgraph(leaves).number_of_edges();check('upper-042',len(leaves),nx.diameter(g)**2,False)
g=nx.complete_graph(3);g.add_edges_from((0,j) for j in range(3,27));s=[1]+list(range(3,27));assert not g.subgraph(s).number_of_edges() and nx.diameter(g)==2 and nx.triangles(g,0)>0;assert Fraction(11,4)**2<8;check('upper-065',len(s),24,False)
g=nx.balanced_tree(2,5);leaves=[v for v in g if g.degree(v)==1];assert not g.subgraph(leaves).number_of_edges();check('upper-080',len(leaves),max(nx.radius(g),max(dict(g.degree()).values()))**2+1,False)
print('10/10 witnesses passed')
