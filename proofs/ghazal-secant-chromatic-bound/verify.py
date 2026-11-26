from functools import lru_cache

# A state is the stack of colors of visible vertices, canonicalized
# by order of first occurrence. A move attaches to an entire suffix.
def canonical(s):
    d={}
    return tuple(d.setdefault(c,len(d)) for c in s)

@lru_cache(None)
def force(q,s,h):
    if h==0: return False
    for i in range(len(s)):
        allowed=set(range(q))-set(s[i:])
        if all(force(q,canonical(s[:i+1]+(c,)),h-1) for c in allowed):
            return True
    return False

# Construct universal branching graph explicitly for modest depth;
# check the stack invariant on every root-to-node path.
def audit_tree(depth):
    count=0
    def visit(path,edges,stack,h):
        nonlocal count
        count+=1
        visible=tuple(i for i in range(len(path)) if not any(a<i<b for a,b in edges))
        assert stack==visible
        assert all(not (a<c<b<d or c<a<d<b) for a,b in edges for c,d in edges)
        if h==0:return
        v=len(path)
        for i in range(len(stack)):
            new=tuple((u,v) for u in stack[i:])
            assert (v-1,v) in new
            visit(path+(v,),edges+new,stack[:i+1]+(v,),h-1)
    visit((0,),(),(0,),depth)
    return count

if __name__=='__main__':
    for q in range(1,6):
        h=2**q
        assert force(q,(0,),h)
        print(f'{q} colors: forced failure within {h} moves; {force.cache_info().currsize} cached states',flush=True)
        force.cache_clear()
    print('Universal tree depth 8:',audit_tree(8),'nodes; all stack and noncrossing checks passed.',flush=True)
