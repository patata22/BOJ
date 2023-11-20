def ari(a,d,n):
    return n*(2*a+(n-1)*d)//2

def geo(a,r,n):
    return a*(r**n-1)//(r-1)

while True:
    n=int(input())
    if not n: break
    a,b,c=map(int,input().split())
    if c-b==b-a: print(ari(a,b-a,n))
    else: print(geo(a,b//a, n))
