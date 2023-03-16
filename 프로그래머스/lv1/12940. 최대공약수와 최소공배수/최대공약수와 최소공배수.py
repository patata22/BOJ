def solution(n, m):
    g=gcd(n,m)
    return g, n*m//g

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x