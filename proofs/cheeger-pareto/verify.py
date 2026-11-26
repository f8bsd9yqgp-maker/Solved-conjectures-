#!/usr/bin/env python3
"""Exact finite sanity check of the analytic counterexample, s=7 by default.
No optimization or floating-point arithmetic is used.
For larger s the proof in README.md, not exhaustive enumeration, is intended.
"""
from fractions import Fraction
import argparse

def graph(s):
    assert s >= 7 and s % 2 == 1
    n=3*s+1; u=n-1; t=(s-1)//2
    adj=[0]*n
    def edge(a,b):
        assert a!=b and not (adj[a]>>b&1)
        adj[a]|=1<<b; adj[b]|=1<<a
    for i in range(3):
        for a in range(s):
            for b in range(a+1,s): edge(i*s+a,i*s+b)
        for a in range(t): edge(i*s+a,((i+1)%3)*s+t+a)
    for a in range(u): edge(a,u)
    return adj,u

def verify(s):
    adj,u=graph(s); n=len(adj); k=n//2; c=3*s-1
    deg=[a.bit_count() for a in adj]
    prev=0; cut=0; count=0; num=10**9; den=1; covered=0; checked=0; tight=0
    for i in range(1,1<<n):
        mask=i^(i>>1); delta=mask^prev; v=delta.bit_length()-1
        inner=(adj[v]&prev).bit_count()
        if mask&delta:
            count+=1; cut+=deg[v]-2*inner
        else:
            count-=1; cut-=deg[v]-2*inner
        prev=mask
        if not 1<=count<=k: continue
        checked+=1
        weight=c if mask>>u&1 else 0
        assert weight<=cut,(s,mask,weight,cut)
        if weight==cut: covered|=mask; tight+=1
        if cut*den<num*count: num,den=cut,count
    h=Fraction(num,den)
    assert h==Fraction(2*s-1,s)
    assert covered==(1<<n)-1
    gap=k*h-c
    assert gap==Fraction(s-1,2*s)>0
    print(f's={s}, n={n}, edges={sum(deg)//2}, k={k}, cuts_checked={checked}, h={h}, witness_sum={c}, gap_at_least={gap}, tight_sets={tight}, Pareto_cover=all_vertices: PASS')

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--s',type=int,default=7); args=p.parse_args()
    verify(args.s)
