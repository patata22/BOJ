def solution(n):
    g= gcd(n,6)
    return (n//g)

def gcd(x,y):
    if y>x: x,y=y,x
    while y:
        x,y=y,x%y
    return x