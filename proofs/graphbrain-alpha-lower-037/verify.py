import networkx as nx
from fractions import Fraction
from itertools import combinations

def average(g):
    return Fraction(sum(sum(d.values()) for _,d in nx.all_pairs_shortest_path_length(g)),len(g)*(len(g)-1))
def meeh(g):
    ans=0
    for _,d in nx.all_pairs_shortest_path_length(g):
        E={v for v,l in d.items() if l%2==0}
        ans=max(ans,len(E)-g.subgraph(E).number_of_edges())
    return ans
def lower(i,a,b):
    assert a<b,(i,a,b);print(i,a,b)
def upper(i,a,b):
    assert a>b,(i,a,b);print(i,a,b)

k=7;g=nx.complete_graph(k+1);g.add_nodes_from(range(k+1,2*k+1));g.add_edges_from((k+1+j,i) for j in range(k) for i in range(j+2))
a=max(map(len,nx.find_cliques(nx.complement(g)))); dd=len(set(dict(g.degree()).values())); sw=1+max(nx.core_number(g).values()); delta=min(dict(g.degree()).values()); assert (a,dd,sw,delta)==(7,13,9,2);lower('lower-037',a,(dd-sw)*delta)

r=51;k=5;g=nx.disjoint_union_all([nx.complete_graph(k) for _ in range(r)]);g.add_edges_from((j*k,(j+1)*k) for j in range(r-1));s=[j*k+1 for j in range(r)];assert nx.is_connected(g) and not g.subgraph(s).number_of_edges();assert all(g.subgraph(range(j*k,(j+1)*k)).number_of_edges()==10 for j in range(r));a=len(s);m=meeh(g);D=max(dict(g.degree()).values());delta=min(dict(g.degree()).values());c=len(nx.center(g));cn=max(len(set(g[u])&set(g[v])) for u,v in combinations(g,2));t=sum(nx.triangles(g).values())//3;avg=average(g);assert (a,m,D,delta,c,cn,t)==(51,0,6,4,1,3,510);assert nx.triangles(g,0)>0
# e < 3; ceil(e^3) <=27; sinh(6)<3^6/2
upper('upper-004',a,27+m)
upper('upper-012',a,max(D**2,m+delta))
upper('upper-013',a,10**c+m)
upper('upper-035',a,max(2*m,D,c))
upper('upper-093',a,max(D**2,avg+m))
upper('upper-102',a,cn+2*D+m)
upper('upper-110',a,Fraction(3**6,2*t)+m)

m=200;g=nx.complete_bipartite_graph(m,m);g.add_edges_from([(0,2*m),(2*m,2*m+1),(2*m+1,2*m+2),(0,2*m+3),(2*m+3,2*m+4),(2*m+4,2*m+5)]);s=list(range(m,2*m))+[2*m,2*m+2,2*m+3,2*m+5];assert nx.is_connected(g) and not g.subgraph(s).number_of_edges();a=len(s);rad=nx.radius(g);p=len(nx.periphery(g));dd=len(set(dict(g.degree()).values()));avg=average(g);assert (a,rad,p,dd)==(204,3,2,4) and 1<avg<=2;upper('upper-055',a,Fraction(100,rad**2));upper('upper-092',a,max(rad**2,p**dd));print('10/10 passed')
