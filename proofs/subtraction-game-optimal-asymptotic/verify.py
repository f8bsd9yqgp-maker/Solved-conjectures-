"""Exact affine backward induction certificate."""
from functools import cache

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])

def verify(s0, expected):
    S=tuple(zip(s0,(1,1,2,2,2)))
    assert all(a>0 and b>=0 for a,b in S)
    @cache
    def calc(h,sign):
        c=[]
        for s in S:
            r=sub(h,s)
            if r[0]<0:
                assert r[1]<=0
                continue
            assert r[1]>=0
            b,a=calc(r,sign)
            c.append((add(s,a),b))
        if not c: return (0,0),(0,0)
        a,b=max(c,key=lambda p:(p[0][0],sign*p[1][0]))
        for x,y in c:
            d=sub(a,x)
            if d[0]>0:
                assert d[1]>=0
            else:
                assert d==(0,0)
                d=sub(b,y) if sign==1 else sub(y,b)
                assert d[0]>=0 and d[1]>=0
        return a,b
    result=(calc((6954,14),1),calc((6954,14),-1))
    assert result==expected
    print(s0,result,calc.cache_info())

if __name__=='__main__':
    verify((474,513,989,993,1000), (((3532,7),(3026,6)),((3513,7),(3441,7))))
    verify((474,513,988,992,1001), (((3532,7),(3028,6)),((3516,7),(3438,7))))
