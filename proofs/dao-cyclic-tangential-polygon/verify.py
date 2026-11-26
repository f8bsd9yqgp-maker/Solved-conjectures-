from math import cos, pi
from random import Random

def check(angles):
    from math import sin
    n=len(angles); c=cos(pi/n)
    verts=[(cos(t),sin(t)) for t in angles]
    def gap(p):
        x,y=p
        D=sum(1-x*a-y*b for a,b in verts)
        d=0
        for i,t in enumerate(angles):
            u=angles[i+1] if i+1<n else angles[0]+2*pi
            m=(t+u)/2
            d+=cos((u-t)/2)-x*cos(m)-y*sin(m)
        return c*D-d
    for p in verts:
        assert gap(p)>=-1e-10,(angles,p,gap(p))
    p=tuple(sum(v[j] for v in verts)/n for j in (0,1))
    assert gap(p)>=-1e-10
    return n+1,gap(p)

def main():
    rng=Random(244984); cases=0; checks=0
    for n in range(3,51):
        k,g=check([2*pi*i/n for i in range(n)])
        assert abs(g)<1e-10
        cases+=1; checks+=k
        for _ in range(100):
            angles=sorted(rng.random()*2*pi for _ in range(n))
            k,g=check(angles); cases+=1; checks+=k
    print(f'{cases} polygons; {checks} vertex/interior checks; 48 regular equality checks: PASS (floating-point tolerance 1e-10)')

if __name__=='__main__': main()
