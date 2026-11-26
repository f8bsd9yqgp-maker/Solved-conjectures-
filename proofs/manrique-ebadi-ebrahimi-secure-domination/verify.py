from itertools import combinations


def build(k):
    n = 4*k+3
    out = [0]*n
    def arc(u,v): out[u] |= 1<<v
    for i in range(k):
        for j in range(4): arc(4*i+j,4*i+(j+1)%4)
        arc(4*i,4*k)
    for j in range(3): arc(4*k+j,4*k+(j+1)%3)
    pred = [sum(1<<u for u in range(n) if out[u]>>v&1) for v in range(n)]
    assert all(out) and all(pred)
    seen = 1
    while True:
        nxt = seen
        for v in range(n):
            if seen>>v&1: nxt |= out[v]|pred[v]
        if nxt == seen: break
        seen = nxt
    assert seen == (1<<n)-1
    return out,pred


def secure(S, defenders, pred):
    def dominates(T):
        return all(T>>v&1 or pred[v]&T for v in range(len(pred)))
    if not dominates(S): return False
    for v in range(len(pred)):
        if S>>v&1: continue
        choices = defenders[v]&S
        while choices:
            b = choices&-choices
            choices ^= b
            if dominates((S^b)|(1<<v)): break
        else: return False
    return True


def minimum(defenders,pred):
    for size in range(len(pred)+1):
        for vertices in combinations(range(len(pred)),size):
            if secure(sum(1<<v for v in vertices),defenders,pred): return size
    raise AssertionError('no secure set')


if __name__ == '__main__':
    for k in range(1,4):
        out,pred=build(k)
        oso=minimum(pred,pred)
        iso=minimum(out,pred)
        assert oso==iso==3*k+2
        n=len(out); bound=(2*n+2)//3
        print(f'k={k}: n={n}, OSO={oso}, ISO={iso}, conjectured bound={bound}: PASS')
    for k in range(1,101):
        out,pred=build(k)
        S=((1<<len(out))-1)^sum(1<<(4*i+2) for i in range(k))^(1<<(4*k+2))
        assert S.bit_count()==3*k+2
        assert secure(S,pred,pred) and secure(S,out,pred)
    print('Explicit upper-bound witnesses: 100 weakly connected digraphs passed both security checks.')
