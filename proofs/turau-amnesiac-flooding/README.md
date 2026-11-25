# Counterexample to Turau's amnesiac flooding conjecture

Source: Volker Turau, Analysis of Amnesiac Flooding (2020), Section 8, https://arxiv.org/abs/2002.10752. Original conjecture for connected non-bipartite graphs: k Flood_k(G) >= Rad(G)+k-1. The paper counts nonempty sending rounds (e.g. Flood_n(G)=1). AI-assisted counterexample dated 25 November 2026.

Let G=P20 lexicographic product K2, so vertices (i,j) have i=0,...,19, j=0,1. The two vertices within each layer are adjacent; every pair across consecutive layers is adjacent. It has 40 vertices and 96 edges, is connected and contains triangles. Distances across distinct layers are |i-h|, and vertices in the same layer are adjacent. Radius is 10. Initiators are (2,0),(7,0),(12,0),(17,0).

Let M_t be the directed messages sent in round t. Start with all outgoing directed edges of initiators. In subsequent rounds, a receiver sends to each neighbor from which it did not receive a message in the preceding sending round. Exact set recurrence gives message counts 20,80,92,0; hence Flood_4(G)<=3. The conjecture would require 12>=13, impossible. Turau's weaker proven bound Flood_k>=Rad/k+1/2 implies Flood_4=3 exactly.

Reproduce with Python 3, no dependencies:

```python
V=[(i,j) for i in range(20) for j in range(2)]
N={v:{w for w in V if w!=v and abs(v[0]-w[0])<=1} for v in V}
assert sum(map(len,N.values()))==192
S={(i,0) for i in (2,7,12,17)}
M={(v,w) for v in S for w in N[v]}
counts=[]
for _ in range(4):
    counts.append(len(M))
    M={(v,w) for _,v in M for w in N[v] if (w,v) not in M}
assert counts==[20,80,92,0]
assert 4*3<10+4-1
```

No independent review or discovery-priority claim. The later SOFSEM version and literature should be checked for prior resolution.
