import math

def gcd(x,y):
    while y:x,y=y,x%y
    return x
    

a,b=map(int,input().split())
answer=math.isqrt(b)-math.isqrt(a)
total=b-a
if not answer:print(0)
else:
    g=gcd(total,answer)
    total//=g
    answer//=g
    print(f'{answer}/{total}')
