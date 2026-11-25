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

## Smaller 28-vertex counterexample and sharp family (25 November 2026)

Let G_k be a path on 5k spine vertices, split consecutively into k blocks of five (a,b,c,d,e). In every block add two new vertices x,y with edges xb,xc,yc,yd. Thus two triangles are attached along the edges bc and cd. The initiators are the k middle vertices c, one per block. G_k is connected, planar, and nonbipartite; it has 7k vertices and 9k-1 edges.

The spine is an isometric path: every detour via an added vertex can be replaced by a walk along the spine of no greater length. Its endpoints therefore have distance 5k-1, giving radius at least floor(5k/2). A middle spine vertex has distance at most floor(5k/2) to every spine vertex and every off-spine vertex (the latter is adjacent to two consecutive spine vertices). Thus Rad(G_k)=floor(5k/2).

Flooding from all block centers proceeds as follows, with synchronous sends in each round.

- Round 1: c sends to b,d,x,y.
- Round 2: b sends to a,x; d sends to e,y; x sends to b; y sends to d.
- Round 3: b sends to a,c; d sends to e,c; x and y send to c. The spine endpoints a,e of neighboring blocks also send to each other across the bridge (where present).
- Round 4: no messages. Each c received from all its neighbors in round 3. Each a/e received from all its neighbors, and no other vertex received a message.

Hence the exact counts of directed messages in the three nonempty rounds are 4k,6k,8k-2. In particular Flood_k(G_k)<=3. Theorem 4(3) in arXiv:2002.10752v4 gives k Flood_k >= Rad+k/2, so Flood_k>=3 and equality holds. In integer form the original proven bound is k Flood_k >= Rad+ceil(k/2), and our construction attains it for every k>=1. The stronger conjecture fails for every k>=4, with excess floor(k/2)-1. For k=4, the graph has 28 vertices and 35 edges, radius 10 and optimal flooding time 3.

The companion verify_smaller.py uses exact discrete message propagation and BFS to verify k=1..50, and exhaustively checks all 20,475 four-source sets of the 28-vertex graph. All checks passed; only the displayed four-source choice finishes in three rounds. This does not establish minimum counterexample order over all graphs. This strengthens the existing repository entry; it is not a second conjecture resolution. Targeted searches did not locate a prior resolution of the original conjecture, but priority and independent review remain unverified.

