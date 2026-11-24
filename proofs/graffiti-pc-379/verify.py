import itertools as it, networkx as nx
from collections import Counter

def subsets(V):
 return (set(s) for k in range(len(V)+1) for s in it.combinations(V,k))
def N(g,s):return set().union(*(set(g[v]) for v in s))
def ind(g,s):return g.subgraph(s).number_of_edges()==0
nt=nm=ng=n416=0
for n in range(3,13):
 for g in nx.nonisomorphic_trees(n):
  V=set(g); deg=dict(g.degree()); L={v for v in V if deg[v]==1}; S=N(g,L); M={v for v in V if deg[v]==max(deg.values())}; t=len(S)+next(len(s) for s in subsets(V-S) if N(g,S|s)==V)
  cs=nx.number_connected_components(g.subgraph(S|L)); cm=nx.number_connected_components(g.subgraph(M)); dd=len(set(deg.values()))
  assert 3*(t-cs)>=1+nx.radius(g)
  assert 3*(t-cm)>=dd
  f=Counter(deg.values())
  if f[2]>max(v for d,v in f.items() if d!=2):
   assert 3*t>=4*dd; nm+=1
  nt+=1
for g in nx.graph_atlas_g():
 if len(g)<3 or not nx.is_connected(g):continue
 V=set(g); inds=[s for s in subsets(V) if ind(g,s)]; deg=dict(g.degree()); P={v for v in V if deg[v]==1}; A={v for v in V if deg[v]==min(deg.values())};M={v for v in V if deg[v]==max(deg.values())}
 if nx.diameter(g)<=2:
  score=max(len(s)-len(N(g,s)) for s in inds); crit=[s for s in inds if len(s)-len(N(g,s))==score]; k=max(map(len,crit)); H=set().union(*(s for s in crit if len(s)==k)); iso=len(list(nx.isolates(g.subgraph(N(g,N(g,P))))));assert len(H)>=iso-2; n416+=1
 if len(g)>3:
  i=min(len(s) for s in inds if s|N(g,s)==V); a=max(len(s) for s in inds if s<=A|N(g,A)); b=max(len(s) for s in inds if s<=V-A); assert i<=g.subgraph(M).number_of_edges()+a*b;ng+=1
assert (nt,nm,ng,n416)==(985,148,992,456)
print(nt,nm,ng,n416)
