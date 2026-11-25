#!/usr/bin/env python3
"""Exact rational certificates for the finite part of the apex-unicyclic phase lemma.
No floating-point computation is used for assertions. Standard library only.
"""
from fractions import Fraction as Q


def bound(d):
    assert isinstance(d,int) and 2 <= d <= 9
    a=Q(101,100)*(d*(d-1)-2)
    def f(t):
        C=t**5+5*t**3+5*t
        return a/(t**5+3*t**3+t)+2*d/(C*t*t)+2*d*(d-1)/(C*(t**4+2*t*t))
    # For t in [i/10,(i+1)/10], atan(f(t)) <= min(11/7, f(i/10)).
    J=Q(0)
    for i in range(10,100):
        t=Q(i,10);u=t+Q(1,10)
        J+=(u*u-t*t)/2*min(Q(11,7),f(t))
    T=Q(10)
    J+=a/(3*T**3)+2*d/(5*T**5)+2*d*(d-1)/(7*T**7)
    return Q(3,4)+Q(2,3)*J


def main():
    expected=[881,1340,1813,2261,2682,3096,3492,3877]
    for d, k in zip(range(2,10),expected):
        U=bound(d)
        assert U < Q(k,1000) < d-1, (d,U)
        print(f'd={d}: certified upper bound < {k}/1000 < {d-1}')
    assert Q(11,5)**2 < 5 < Q(9,4)**2
    assert Q(7,4)**5 > 16
    assert Q(122,121)<Q(101,100)
    assert 9*10>84
    print('All eight finite certificates and elementary constant checks passed.')

if __name__=='__main__':main()
