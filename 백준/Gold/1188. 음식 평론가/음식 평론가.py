def gcd(x,y):
    while y: x,y=y,x%y
    return x

n,m=map(int,input().split())
print(m-gcd(n,m))
