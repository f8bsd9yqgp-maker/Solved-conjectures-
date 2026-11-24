from itertools import combinations
counts=[0,0,0]
for n in range(2,7):
    E=list(combinations(range(n),2)); full=(1<<n)-1
    for code in range(1<<len(E)):
        a=[0]*n
        for i,(u,v) in enumerate(E):
            if code>>i&1: a[u]|=1<<v; a[v]|=1<<u
        ds=[]
        for r in range(n):
            seen=front=1<<r; d=tot=0
            while front:
                new=0
                for j in range(n):
                    if front>>j&1: new|=a[j]
                front=new&~seen
                if not front: break
                seen|=front; d+=1; tot+=d*front.bit_count()
            if seen!=full: break
            ds.append((d,tot))
        if len(ds)!=n: continue
        counts[0]+=1
        if 3*sum(d for d,_ in ds)<n*max(t for _,t in ds): continue
        counts[1]+=1
        def dom(s):
            c=0
            for i in range(n):
                if s>>i&1: c|=a[i]
            return c==full
        sizes={s.bit_count() for s in range(1,full+1) if dom(s) and all(not dom(s^(1<<i)) for i in range(n) if s>>i&1)}
        assert len(sizes)==1,(n,code,sizes)
        counts[2]+=1
assert counts==[27475,245,245]
print(counts)
