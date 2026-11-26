from fractions import Fraction as F

def check(b):
    y=F(1181,2074); z=F(391,1037)
    assert 0<y<b<F(11,6) and 0<z<1
    ratios=(y/z,(b-y)/(1-z),(F(11,2)-3*b)/2)
    assert ratios[1]>ratios[0]>ratios[2]>0
    N=[(F(399,401),F(40,401)),(F(4,5),F(3,5)),(F(0),F(1)),(F(-4,5),F(3,5)),(F(-399,401),F(40,401))]
    N += [(-x,-y) for x,y in N]
    for H in ([F(1),F(11,10),b,F(11,10),F(1)]*2,[F(1)]*10):
        for i,(a,c) in enumerate(N):
            j=(i+1)%10; d,e=N[j]; det=a*e-c*d
            assert a*a+c*c==1 and det>0
            p=((H[i]*e-c*H[j])/det,(a*H[j]-H[i]*d)/det)
            for k,((x,y),h) in enumerate(zip(N,H)):
                slack=h-x*p[0]-y*p[1]
                assert slack==0 if k in (i,j) else slack>0
    return ratios

if __name__=='__main__':
    for b in (F(8,5), F(17,10)):
        print(f'b={b}: ratios={check(b)}; all adjacent vertices feasible, strict nonincident slacks: PASS')
    print('Endpoint certificates imply all affine inequalities throughout [8/5,17/10].')
