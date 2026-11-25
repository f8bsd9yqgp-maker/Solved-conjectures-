import networkx as nx
from fractions import Fraction
from itertools import combinations
import numpy as np

def chain(r,k,arms=False):
    g=nx.disjoint_union_all([nx.complete_graph(k) for _ in range(r)])
    g.add_edges_from((j*k,(j+1)*k) for j in range(r-1))
    if arms:
        n=r*k;g.add_edges_from([(0,n),(n,n+1),((r-1)*k,n+2),(n+2,n+3)])
    s=[j*k+1 for j in range(r)]+([r*k+1,r*k+3] if arms else [])
    assert nx.is_connected(g) and g.subgraph(s).number_of_edges()==0
    assert all(g.subgraph(range(j*k,(j+1)*k)).number_of_edges()==k*(k-1)//2 for j in range(r))
    return g,len(s)
def alpha(g):return max(map(len,nx.find_cliques(nx.complement(g))))
def sigma(g):return min(g.degree(u)+g.degree(v) for u,v in nx.non_edges(g))
def lower(i,a,b):assert a<b,(i,a,b);print(i,a,b)
def upper(i,a,b):assert a>b,(i,a,b);print(i,a,b)
g,a=chain(4,8);neg=sum(np.linalg.eigvalsh(nx.to_numpy_array(g))<-1e-8);cn=max(len(set(g[u])&set(g[v])) for u,v in combinations(g,2));assert neg>=24 and cn==6;lower('lower-017',a,Fraction(neg,2)-cn)
k=5;g=nx.complete_graph(k);g.add_nodes_from(range(k,2*k));g.add_edges_from((k+j,i) for j in range(k) for i in range(j+1));a=alpha(g);dd=len(set(dict(g.degree()).values()));sw=1+max(nx.core_number(g).values());assert (a,dd,sw)==(5,9,6);lower('lower-029',a,2*dd-2*sw)
g=nx.complete_graph(6);g.add_edges_from([(0,6),(6,7),(0,8),(8,9)]);a=alpha(g);p=len(nx.periphery(g));c=len(nx.center(g));assert (a,p,c)==(3,2,1);lower('lower-032',a,Fraction(len(g),p)-c)
g,a=chain(10,4,True);mu=len(nx.max_weight_matching(g,maxcardinality=True));p=len(nx.periphery(g));assert (a,mu,p)==(12,22,2);assert nx.triangles(g,0)>0;lower('lower-048',a,mu-3**p)
g,a=chain(6,12,True);mu=len(nx.max_weight_matching(g,maxcardinality=True));p=len(nx.periphery(g));dd=len(set(dict(g.degree()).values()));assert (a,mu,p,dd)==(8,38,2,4);lower('lower-057',a,Fraction(mu-p,dd))
g=nx.complete_graph(3);g.add_edges_from((0,j) for j in range(3,10));a=alpha(g);p=len(nx.periphery(g));assert sigma(g)==2 and p==9;upper('upper-041',a,(3**sigma(g)-p)**2)
g=nx.complete_bipartite_graph(7,7);g.add_edge(0,1);a=7;assert not g.subgraph(range(7,14)).number_of_edges() and sigma(g)==14 and nx.triangles(g,0)>0;upper('upper-086',a,2*max(3,len(g)-sigma(g)))
g,a=chain(13,4);tri=sum(nx.triangles(g).values())//3;avg=Fraction(2*g.number_of_edges(),len(g));assert tri==len(g);upper('upper-090',a,max(avg**2,len(g)-tri))
g=nx.complete_graph(3);g.add_edge(0,3);g.add_edges_from((j,j+1) for j in range(3,17));s=[1]+list(range(3,18,2));assert g.subgraph(s).number_of_edges()==0 and nx.radius(g)==8;upper('upper-078',len(s),Fraction(3*len(g),nx.radius(g)-1))
g=nx.complete_bipartite_graph(5,5);assert alpha(g)==5 and alpha(nx.complement(g))==2 and nx.is_bipartite(g)
# theta values via exact sandwich bounds rather than a numerical SDP
assert all(g.degree(v)==5 for v in g);upper('upper-137',5,Fraction(10,3))
print('10/10 checks passed')
