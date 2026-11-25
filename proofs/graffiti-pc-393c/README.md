# Graffiti.pc Conjecture 393c — 2-domination via closed pendant neighborhoods

24 November 2026 (US Central). AI-assisted written mathematical note; independent review and Lean verification remain pending. The statement is from the [August 2026 transcription of Written on the Wall II](https://github.com/Kuberwastaken/c5-k4/blob/main/corpora/graffiti_pc_wow2.json), which lists the entry open. The November 2026 PDF is indexed at https://www.uhd.edu/academics/sciences/mathematics-statistics/wowii/files/wowiiaii.pdf, but its later pages could not be retrieved and screenshot requests failed; latest official status is therefore unconfirmed. Davis's main completed table does not list this entry. No discovery priority is claimed.

Throughout let G be a finite simple connected graph on n>2 vertices, P the pendant (degree-one) vertices, S=N(P) their support vertices, X=N(S), with N the union of open neighborhoods, and γ₂ the minimum size of a set D such that every vertex outside D has at least two neighbors in D. P and S are disjoint, P⊆X, and each pendant has exactly one support neighbor.

Write Q={v: |N(v)∩(P∪S)|=1}. The conjecture is γ₂(G)≤n−|X|+|S|+|Q|.

Take D=(V∖X)∪S∪Q. A vertex v outside D belongs to X and is not a support, so it has no pendant neighbor (otherwise v would be a support). Consequently |N(v)∩(P∪S)|=|N(v)∩S|≥1. Since v∉Q this count is at least two. Both neighbors belong to S⊆D. Thus D is 2-dominating and |D|≤n−|X|+|S|+|Q|, as required. ∎

No earlier exact full resolution was identified in targeted searches.

## Verification
[Joint verifier](../graffiti-pc-393a/verify.py) was executed on 24 November 2026 and passed all 994 connected nonisomorphic atlas graphs of orders 3–7 for the 393 entries and general clauses of 412a/b; all 70 eligible bipartite graphs for the bipartite clauses and 412e; all 992 connected graphs of orders 4–7 for 450. Finite tests supplement the written arguments.
