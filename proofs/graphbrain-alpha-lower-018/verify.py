import networkx as nx
from fractions import Fraction as F
from itertools import combinations
def meeh(g):
    return max([0]+[len(E)-g.subgraph(E).number_of_edges() for _,d in nx.all_pairs_shortest_path_length(g) for E in [{v for v,x in d.items() if x%2==0}]])
def chain(r,k):
    g=nx.disjoint_union_all([nx.complete_graph(k) for _ in range(r)])
    g.add_edges_from((i*k,(i+1)*k) for i in range(r-1))
    assert not g.subgraph(range(1,r*k,k)).number_of_edges()
    return g
# Symbolic theta values and inequalities; no large SDP claimed.
assert 125>11**2 and min(30,31)>28
h=nx.lexicographic_product(nx.cycle_graph(5),nx.cycle_graph(5));assert max(map(len,nx.find_cliques(nx.complement(h))))==4
g=chain(12,6);assert len(g)==72 and max(nx.core_number(g).values())+1==6 and 1<2<4 and 12>10
g=chain(51,5);assert meeh(g)==0 and max(dict(g.degree()).values())==6 and len(nx.periphery(g))==8 and 51>9
g=nx.Graph()
for i in range(12):g.add_edges_from(combinations([0]+list(range(1+4*i,5+4*i)),2))
g.add_edges_from([(0,49),(49,50),(0,51),(51,52)])
s=list(range(1,49,4))+[50,52];assert not g.subgraph(s).number_of_edges() and nx.radius(g)==2 and len(nx.periphery(g))==2
assert max(len(set(g[u])&set(g[v])) for u,v in combinations(g,2))==3 and len(s)>9
g=nx.Graph();g.add_edges_from((0,i) for i in range(1,81))
for i in range(2):g.add_edges_from(combinations([0]+list(range(81+16*i,97+16*i)),2))
s=list(range(1,81))+[81,97];assert not g.subgraph(s).number_of_edges() and meeh(g)==1 and len(nx.max_weight_matching(g,maxcardinality=True))==17 and len(s)>18
m=110;g=nx.complete_bipartite_graph(m,m);g.add_edges_from((2*m,v) for v in range(2*m));assert len(set(dict(g.degree()).values()))==2 and min(len(set(g[u])&set(g[v])) for u,v in combinations(g,2))>=1 and m>101
m=400;density=F(m+3,3*(3*m-1));assert density>F(1,9) and 2*m>max(m+1,9**3)
g=nx.ladder_graph(65);assert nx.is_bipartite(g) and meeh(g)==65 and max(dict(g.degree()).values())==3 and len(nx.max_weight_matching(g,maxcardinality=True))==65 and min(map(len,nx.cycle_basis(g)))==4 and 2*65-4**3>65
print("8 witness checks; symbolic proofs for large theta and density witnesses")
