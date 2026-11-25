import networkx as nx
from fractions import Fraction
from math import ceil

def sigma(g): return min(g.degree(u)+g.degree(v) for u,v in nx.non_edges(g))
def alpha(g): return max(map(len,nx.find_cliques(nx.complement(g))))
def check(g,s): assert nx.is_connected(g) and g.subgraph(s).number_of_edges()==0; return len(s)

g=nx.complete_graph(10);g.add_edges_from([(0,10),(10,11),(10,12)])
a=alpha(g);dd=len(set(dict(g.degree()).values()));s=sigma(g);cv=len(list(nx.articulation_points(g)));n=len(g)
assert (a,dd,s,cv,n)==(3,4,2,2,13)
assert a<Fraction(2*dd,s) and a<min(dd,2*cv) and a<min(dd,Fraction(n,s))
print('lower 041,043,050',a,dd,s,cv,n)
r=6;g=nx.path_graph(4*r-2);g.add_edges_from((0,4*r-2+i) for i in range(r));g.add_edges_from((4*r-3,5*r-2+i) for i in range(r));s=list(range(4*r-2,6*r-2));a=check(g,s);mu=len(nx.max_weight_matching(g,maxcardinality=True));p=len(nx.periphery(g));assert (a,mu,p)==(12,12,12);assert a>10;print('upper 024',a,mu,p)
for h in [84,10]:
    g=nx.complete_graph(3)
    for b in [3,3+h]:
        g.add_edge(0,b);g.add_edges_from((j,j+1) for j in range(b,b+h-1))
    a=check(g,list(range(3,3+h,2))+list(range(3+h,3+2*h,2)));d=max(dict(g.degree()).values());c=len(nx.center(g));p=len(nx.periphery(g));assert (d,c,p)==(4,1,2);assert a>(3**d+c if h==84 else (3**c)**p);print('upper','034' if h==84 else '037',a,d,c,p)
m=12;g=nx.complete_bipartite_graph(m,m);g.add_edges_from([(0,24),(24,25),(25,26),(0,27),(27,28),(28,29)]);a=check(g,list(range(m,2*m))+[24,26,27,29]);p=len(nx.periphery(g));dd=len(set(dict(g.degree()).values()));den=Fraction(g.number_of_edges(),len(g)*(len(g)-1)//2);assert a>max(p,dd)/den;print('upper 047',a,p,dd,den,max(p,dd)/den)
g=nx.complete_bipartite_graph(5,10);a=check(g,list(range(5,15)));assert nx.diameter(g)==2 and 2*g.number_of_edges()==100;print('upper 076',a,0)
m=20;g=nx.complete_graph(m);g.add_edges_from((i,m+2*i+j) for i in range(m) for j in range(2));a=check(g,list(range(m,3*m)));d=max(dict(g.degree()).values());den=Fraction(g.number_of_edges(),len(g)*(len(g)-1)//2);assert min(dict(g.degree()).values())==1 and a>max(d,Fraction(11,4)/den);print('upper 038',a,d,den,Fraction(11,4)/den)
m=4;g=nx.disjoint_union(nx.complete_bipartite_graph(m,m),nx.complete_bipartite_graph(m,m));g.add_edge(0,2*m);a=check(g,list(range(m,2*m))+list(range(3*m,4*m)));delta=min(dict(g.degree()).values());k=nx.node_connectivity(g);rhs=ceil(Fraction(len(g),delta-k));assert a>rhs;print('upper 046',a,delta,k,rhs)
print('10/10')
